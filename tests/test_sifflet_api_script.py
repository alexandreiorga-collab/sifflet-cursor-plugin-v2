"""Tests for skills/sifflet-api/scripts/sifflet_api.py.

The script is the sanctioned way for the sifflet-api skill to call the
Sifflet public REST API, and its confirmation gate is the safety mechanism
for that skill (the bundled guard hook cannot see arbitrary HTTP calls).
These tests exercise the real contract: invoke the script as a subprocess
and assert on exit code / stdout / stderr, the same way
tests/test_guard_sifflet_destructive.py exercises the guard hook.

Run from the repository root:  pytest tests/
"""

import json
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

SCRIPT = (
    Path(__file__).resolve().parent.parent
    / "skills"
    / "sifflet-api"
    / "scripts"
    / "sifflet_api.py"
)

UNUSED_BACKEND_URL = "http://127.0.0.1:1"  # nothing listens here; a real request would error


def run_script(args, env_extra=None, timeout=10):
    import os

    env = dict(os.environ)
    env.pop("SIFFLET_API_TOKEN", None)
    env.pop("SIFFLET_BACKEND_URL", None)
    env.pop("SIFFLET_CONFIG_INI", None)
    env.setdefault("SIFFLET_API_TOKEN", "test-token")
    env.setdefault("SIFFLET_BACKEND_URL", UNUSED_BACKEND_URL)
    if env_extra:
        env.update(env_extra)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)] + args,
        capture_output=True,
        text=True,
        timeout=timeout,
        env=env,
    )
    return proc


# ---------------------------------------------------------------- gating: reads need no token


def test_get_needs_no_confirm():
    proc = run_script(["GET", "/v1/users", "--query", "page=0"])
    # No confirm passed; should not be refused by the gate. It will fail to
    # actually reach the network (nothing listens on UNUSED_BACKEND_URL),
    # but that failure must be a network error, not a gate refusal.
    assert "Refusing to send" not in proc.stderr


def test_post_read_lookup_paths_need_no_confirm():
    for path in (
        "/v1/assets/search",
        "/v1/assets/get-asset-with-uri",
        "/v1/sources/search",
    ):
        proc = run_script(["POST", path, "--data", "{}"])
        assert "Refusing to send" not in proc.stderr, path


# ---------------------------------------------------------------- gating: mutate tier


def test_post_create_without_confirm_is_refused():
    proc = run_script(["POST", "/v1/users", "--data", "{}"])
    assert proc.returncode == 1
    assert "Refusing to send" in proc.stderr
    assert "CONFIRM SIFFLET MUTATE" in proc.stderr


def test_patch_without_confirm_is_refused():
    proc = run_script(["PATCH", "/v1/teams/123", "--data", "{}"])
    assert proc.returncode == 1
    assert "CONFIRM SIFFLET MUTATE" in proc.stderr


def test_post_create_with_wrong_confirm_is_refused():
    proc = run_script(["POST", "/v1/users", "--data", "{}", "--confirm", "yes"])
    assert proc.returncode == 1
    assert "Refusing to send" in proc.stderr


def test_post_create_with_correct_confirm_passes_gate():
    proc = run_script(
        ["POST", "/v1/users", "--data", "{}", "--confirm", "CONFIRM SIFFLET MUTATE"]
    )
    assert "Refusing to send" not in proc.stderr


# ---------------------------------------------------------------- gating: delete tier


def test_delete_resource_tokens():
    cases = {
        "/v1/users/1": "DELETE USER",
        "/v1/teams/1": "DELETE TEAM",
        "/v1/domains/1": "DELETE DOMAIN",
        "/v1/credentials/name": "DELETE CREDENTIAL",
        "/v1/calendars/1": "DELETE CALENDAR",
        "/v1/notification-rules/1": "DELETE NOTIFICATION RULE",
        "/v2/sources/1": "DELETE SOURCE",
    }
    for path, token in cases.items():
        refused = run_script(["DELETE", path])
        assert refused.returncode == 1, path
        assert token in refused.stderr, (path, refused.stderr)

        allowed = run_script(["DELETE", path, "--confirm", token])
        assert "Refusing to send" not in allowed.stderr, (path, allowed.stderr)


def test_delete_workspace_path_reuses_cli_token():
    refused = run_script(["DELETE", "/v1/assets/my-workspace"])
    assert refused.returncode == 1
    assert "DELETE WORKSPACE" in refused.stderr

    allowed = run_script(["DELETE", "/v1/assets/my-workspace", "--confirm", "DELETE WORKSPACE"])
    assert "Refusing to send" not in allowed.stderr


def test_delete_unmapped_path_falls_back_to_generic_token():
    refused = run_script(["DELETE", "/v1/something-new/1"])
    assert refused.returncode == 1
    assert "DELETE SIFFLET RESOURCE" in refused.stderr


# ---------------------------------------------------------------- gating: apply tier


def test_assets_sync_requires_apply_token():
    refused = run_script(["POST", "/v1/assets/sync", "--data", "{}"])
    assert refused.returncode == 1
    assert "CONFIRM SIFFLET APPLY" in refused.stderr

    allowed = run_script(
        ["POST", "/v1/assets/sync", "--data", "{}", "--confirm", "CONFIRM SIFFLET APPLY"]
    )
    assert "Refusing to send" not in allowed.stderr


# ---------------------------------------------------------------- happy path against a stub server


class _StubHandler(BaseHTTPRequestHandler):
    seen = {}

    def _handle(self):
        length = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(length) if length else b""
        _StubHandler.seen = {
            "method": self.command,
            "path": self.path,
            "headers": dict(self.headers),
            "body": body,
        }
        if self.path.startswith("/v1/missing"):
            payload = json.dumps(
                {
                    "type": "about:blank",
                    "title": "Not Found",
                    "status": 404,
                    "detail": "No such user",
                    "response": "",
                }
            ).encode("utf-8")
            self.send_response(404)
            self.send_header("Content-Type", "application/problem+json")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        payload = json.dumps({"data": [{"id": "1"}], "totalCount": 1}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        self._handle()

    def do_POST(self):
        self._handle()

    def do_PATCH(self):
        self._handle()

    def do_PUT(self):
        self._handle()

    def do_DELETE(self):
        self._handle()

    def log_message(self, *a):
        pass


def _start_stub_server():
    server = HTTPServer(("127.0.0.1", 0), _StubHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def test_happy_path_sends_request_and_relays_response():
    server = _start_stub_server()
    try:
        base_url = f"http://127.0.0.1:{server.server_port}"
        proc = run_script(
            ["GET", "/v1/users", "--query", "page=0"],
            env_extra={"SIFFLET_BACKEND_URL": base_url, "SIFFLET_API_TOKEN": "secret-token"},
        )
        assert proc.returncode == 0, proc.stderr
        assert json.loads(proc.stdout) == {"data": [{"id": "1"}], "totalCount": 1}
        assert _StubHandler.seen["method"] == "GET"
        assert _StubHandler.seen["path"] == "/v1/users?page=0"
        assert _StubHandler.seen["headers"]["Authorization"] == "Bearer secret-token"
        assert "secret-token" not in proc.stdout
        assert "secret-token" not in proc.stderr
    finally:
        server.shutdown()


def test_error_path_relays_problem_detail():
    server = _start_stub_server()
    try:
        base_url = f"http://127.0.0.1:{server.server_port}"
        proc = run_script(
            [
                "PATCH",
                "/v1/missing/1",
                "--data",
                "{}",
                "--confirm",
                "CONFIRM SIFFLET MUTATE",
            ],
            env_extra={"SIFFLET_BACKEND_URL": base_url},
        )
        assert proc.returncode == 1
        assert "No such user" in proc.stderr
    finally:
        server.shutdown()


# ---------------------------------------------------------------- config.ini fallback


def test_config_ini_fallback_when_env_vars_unset(tmp_path):
    ini_path = tmp_path / "config.ini"
    ini_path.write_text(
        "[APP]\n"
        "tenant = demo\n"
        "token = ini-token\n"
        "backend_url = https://demo.siffletdata.com/api/\n"
    )
    import os

    env = dict(os.environ)
    env.pop("SIFFLET_API_TOKEN", None)
    env.pop("SIFFLET_BACKEND_URL", None)
    env["SIFFLET_CONFIG_INI"] = str(ini_path)
    # No network reachable at that host in this test env; assert it at least
    # gets past the gate and attempts to use the resolved token/url rather
    # than failing on "missing credentials".
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "GET", "/v1/users"],
        capture_output=True,
        text=True,
        timeout=10,
        env=env,
    )
    assert "missing SIFFLET_API_TOKEN" not in proc.stderr
