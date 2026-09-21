#!/usr/bin/env python3
"""Call the Sifflet public REST API, with a built-in confirmation gate.

This is the ONLY sanctioned way for the sifflet-api skill to hit the public
REST API (`docs/api/`). It resolves auth the same way the rest of the plugin
does (env vars, falling back to ~/.sifflet/config.ini — same precedence as
run-sifflet-mcp.sh), and it refuses to send any non-GET request unless the
caller passes the exact confirmation token required for that operation's
tier. That refusal happens before any network access, so it is a real
software gate, not just an instruction the calling agent is trusted to
follow — see the destructive-call gating rule in .claude/rules/api.md.

Usage:
    python3 sifflet_api.py <METHOD> <PATH> [--data JSON] [--data-file FILE]
                            [--query k=v ...] [--confirm TOKEN]

Examples:
    python3 sifflet_api.py GET /v1/users
    python3 sifflet_api.py DELETE /v1/teams/123 --confirm 'DELETE TEAM'
"""

import argparse
import configparser
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

MUTATE_TOKEN = "CONFIRM SIFFLET MUTATE"
APPLY_TOKEN = "CONFIRM SIFFLET APPLY"

APPLY_PATH = "/v1/assets/sync"
READ_EXEMPT_POST_PATHS = {
    "/v1/assets/search",
    "/v1/assets/get-asset-with-uri",
    "/v1/sources/search",
}

# First path segment after the version prefix -> noun used in the DELETE
# confirmation token. `/v1/assets/{name}` is the REST equivalent of
# `sifflet code workspace delete`, so it reuses that CLI token verbatim.
DELETE_RESOURCE_TOKENS = {
    "users": "DELETE USER",
    "teams": "DELETE TEAM",
    "domains": "DELETE DOMAIN",
    "credentials": "DELETE CREDENTIAL",
    "calendars": "DELETE CALENDAR",
    "notification-rules": "DELETE NOTIFICATION RULE",
    "sources": "DELETE SOURCE",
    "assets": "DELETE WORKSPACE",
}
DEFAULT_DELETE_TOKEN = "DELETE SIFFLET RESOURCE"


class GateError(Exception):
    """Raised when a call is refused before any network access."""


def _normalized_path(path):
    return path.split("?", 1)[0].rstrip("/") or "/"


def _resource_segment(path):
    parts = [p for p in _normalized_path(path).split("/") if p]
    # parts look like ["v1", "users", "123"] or ["v2", "sources"]
    return parts[1] if len(parts) > 1 else (parts[0] if parts else "")


def classify(method, path):
    """Return (tier, required_token_or_None) for a request. No network."""
    method = method.upper()
    norm_path = _normalized_path(path)

    if method == "GET":
        return "read", None
    if method == "POST" and norm_path in READ_EXEMPT_POST_PATHS:
        return "read", None
    if method == "POST" and norm_path == APPLY_PATH:
        return "apply", APPLY_TOKEN
    if method == "DELETE":
        resource = _resource_segment(norm_path)
        token = DELETE_RESOURCE_TOKENS.get(resource, DEFAULT_DELETE_TOKEN)
        return "delete", token
    if method in ("POST", "PATCH", "PUT"):
        return "mutate", MUTATE_TOKEN
    raise GateError(f"Unsupported HTTP method: {method}")


def check_gate(method, path, confirm):
    """Raise GateError if this call needs a confirm token that's missing/wrong."""
    tier, required = classify(method, path)
    if required is None:
        return tier
    if confirm != required:
        got = "none" if confirm is None else repr(confirm)
        raise GateError(
            f"Refusing to send {method.upper()} {path} without confirmation.\n"
            f"This is a '{tier}' operation. Re-run with --confirm '{required}' "
            "only after the user has explicitly typed that exact token this turn "
            "(see the sifflet-api skill's confirmation protocol) — do not "
            "generate the token yourself."
        )
    return tier


def _with_https_scheme(raw):
    u = (raw or "").strip()
    if not u:
        return u
    if u.startswith("http://") or u.startswith("https://"):
        return u
    return "https://" + u.lstrip("/")


def resolve_auth():
    """Resolve (token, base_url), mirroring run-sifflet-mcp.sh's precedence:
    SIFFLET_API_TOKEN / SIFFLET_BACKEND_URL env vars first, else
    ~/.sifflet/config.ini's [APP] section (token, backend_url, tenant).
    """
    token = (os.environ.get("SIFFLET_API_TOKEN") or "").strip()
    base_url = (os.environ.get("SIFFLET_BACKEND_URL") or "").strip()

    if token and base_url:
        return token, _with_https_scheme(base_url)

    ini_path = Path(os.environ.get("SIFFLET_CONFIG_INI") or (Path.home() / ".sifflet" / "config.ini"))
    if ini_path.is_file():
        cp = configparser.ConfigParser()
        read_ok = cp.read(ini_path, encoding="utf-8")
        if read_ok and "APP" in cp:
            app = cp["APP"]
            if not token:
                token = (app.get("token") or "").strip()
            if not base_url:
                base_url = (app.get("backend_url") or "").strip()
                tenant = (app.get("tenant") or "").strip()
                if not base_url and tenant:
                    base_url = f"https://{tenant}.siffletdata.com/api/"

    return token, _with_https_scheme(base_url)


def build_url(base_url, path, query_pairs):
    base = base_url.rstrip("/")
    url = f"{base}{path if path.startswith('/') else '/' + path}"
    if query_pairs:
        url += "?" + urllib.parse.urlencode(query_pairs)
    return url


def send_request(method, url, token, body_bytes):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    if body_bytes is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body_bytes, method=method.upper(), headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            status = resp.status
            raw = resp.read()
    except urllib.error.HTTPError as e:
        raw = e.read()
        _print_problem(e.code, raw)
        return 1
    except urllib.error.URLError as e:
        print(f"sifflet_api: network error calling {url}: {e.reason}", file=sys.stderr)
        return 1

    if not raw:
        print(f"{status} (no body)")
        return 0
    try:
        print(json.dumps(json.loads(raw.decode("utf-8")), indent=2))
    except (ValueError, UnicodeDecodeError):
        sys.stdout.write(raw.decode("utf-8", errors="replace"))
    return 0


def _print_problem(status, raw):
    detail = title = None
    if raw:
        try:
            problem = json.loads(raw.decode("utf-8"))
            title = problem.get("title")
            detail = problem.get("detail")
        except (ValueError, UnicodeDecodeError):
            pass
    print(f"sifflet_api: request failed: {status} {title or ''}".rstrip(), file=sys.stderr)
    if detail:
        print(detail, file=sys.stderr)
    elif raw:
        print(raw.decode("utf-8", errors="replace"), file=sys.stderr)


def parse_query(pairs):
    result = []
    for p in pairs or []:
        if "=" not in p:
            raise GateError(f"--query expects k=v, got: {p!r}")
        k, v = p.split("=", 1)
        result.append((k, v))
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("method", help="HTTP method: GET, POST, PATCH, PUT, DELETE")
    parser.add_argument("path", help="API path, e.g. /v1/users or /v2/sources/{id}")
    parser.add_argument("--data", help="Request body as a raw JSON string")
    parser.add_argument("--data-file", help="Path to a file containing the JSON request body")
    parser.add_argument("--query", action="append", help="Query param as k=v (repeatable)")
    parser.add_argument("--confirm", help="Confirmation token required for non-GET calls")
    args = parser.parse_args(argv)

    try:
        check_gate(args.method, args.path, args.confirm)
        query_pairs = parse_query(args.query)
    except GateError as e:
        print(str(e), file=sys.stderr)
        return 1

    body_bytes = None
    if args.data_file:
        body_bytes = Path(args.data_file).read_bytes()
    elif args.data is not None:
        body_bytes = args.data.encode("utf-8")

    token, base_url = resolve_auth()
    if not token or not base_url:
        print(
            "sifflet_api: missing SIFFLET_API_TOKEN/SIFFLET_BACKEND_URL and no usable "
            "~/.sifflet/config.ini. Run `sifflet configure` or set the env vars "
            "(see the configure-sifflet-auth command).",
            file=sys.stderr,
        )
        return 1

    url = build_url(base_url, args.path, query_pairs)
    return send_request(args.method, url, token, body_bytes)


if __name__ == "__main__":
    sys.exit(main())
