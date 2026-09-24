#!/usr/bin/env python3
"""Generate docs/api/*.md from docs/api/openapi.json.

The Sifflet public REST API has no officially downloadable OpenAPI file (see
docs/api/README.md for how openapi.json was obtained). This script is the
one source of truth for turning that spec into the per-domain Markdown docs,
so refreshing the docs after a spec update is one deterministic command
instead of hand-editing 60+ endpoint write-ups.

Usage (from repo root):
    python3 scripts/generate_api_docs.py

Reads:  docs/api/openapi.json
Writes: docs/api/<domain>.md for every OpenAPI tag, plus docs/api/README.md
"""

import json
import os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API_DIR = os.path.join(ROOT, "docs", "api")
SPEC_PATH = os.path.join(API_DIR, "openapi.json")

ENUM_DISPLAY_LIMIT = 12

TAG_TO_FILE = {
    "Assets": ("assets", "Assets", "Search, read, and edit catalog assets."),
    "Calendars": ("calendars", "Calendars", "Maintenance-window calendars used by monitor schedules."),
    "Credentials": ("credentials", "Credentials", "Stored credentials referenced by data sources."),
    "Declarative Assets and Lineage": (
        "declarative-assets-and-lineage",
        "Declarative Assets and Lineage (Workspace sync)",
        "Push declarative assets/lineage and delete the resulting workspace.",
    ),
    "Domains": ("domains", "Domains", "Organizational domains used to group assets."),
    "External Catalog": ("external-catalog", "External Catalog", "Push external catalog metadata (tags, terms, descriptions) onto assets."),
    "dbt integration": ("dbt-integration", "dbt Integration", "Submit dbt metadata files and trigger the related datasource refresh."),
    "Notification Rules": ("notification-rules", "Notification Rules", "Rules that route monitor/incident notifications."),
    "Rule": ("monitoring-rules", "Monitoring Rules", "Sifflet monitors (rules): list, details, manual run, as-code export."),
    "Rule Run": ("monitoring-rules", "Monitoring Rules", "Sifflet monitors (rules): list, details, manual run, as-code export."),
    "Workspace": ("monitoring-rules", "Monitoring Rules", "Sifflet monitors (rules): list, details, manual run, as-code export."),
    "Sources (deprecated)": ("sources-v1", "Sources (v1, deprecated)", "Deprecated data-source management. Use Sources (v2) for new integrations."),
    "Sources (v2)": ("sources-v2", "Sources (v2)", "Data-source management: create, edit, test connections, trigger ingestion."),
    "Teams": ("teams", "Teams", "Teams used for asset ownership and access."),
    "Users": ("users", "Users", "User accounts: list, create, update, delete, reset password."),
}


def load_spec():
    with open(SPEC_PATH) as f:
        return json.load(f)


def ref_name(ref):
    return ref.split("/")[-1]


def make_helpers(comps):
    def resolve(node):
        if not isinstance(node, dict):
            return node
        if "$ref" in node:
            return comps.get(ref_name(node["$ref"]), {})
        return node

    def format_enum(values):
        if len(values) > ENUM_DISPLAY_LIMIT:
            shown = ", ".join(f"`{v}`" for v in values[:ENUM_DISPLAY_LIMIT])
            return f"enum ({shown}, … {len(values) - ENUM_DISPLAY_LIMIT} more — full list in `openapi.json`)"
        return "enum (" + ", ".join(f"`{v}`" for v in values) + ")"

    def type_str(node):
        if not isinstance(node, dict):
            return "any", []
        refs = []
        if "$ref" in node:
            name = ref_name(node["$ref"])
            target = comps.get(name, {})
            if target.get("enum"):
                return format_enum(target["enum"]), []
            if target.get("type") == "object" or "properties" in target:
                return f"[`{name}`](#schema-{name.lower()})", [name]
            return type_str(target)
        if "oneOf" in node or "anyOf" in node:
            names, opt_refs = [], []
            for o in node.get("oneOf") or node.get("anyOf"):
                t, r = type_str(o)
                names.append(t)
                opt_refs.extend(r)
            return " or ".join(names), opt_refs
        if "allOf" in node:
            names, opt_refs = [], []
            for o in node["allOf"]:
                t, r = type_str(o)
                names.append(t)
                opt_refs.extend(r)
            return " & ".join(names), opt_refs
        t = node.get("type")
        if t == "array":
            it, r = type_str(node.get("items", {}))
            return f"array<{it}>", r
        if node.get("enum"):
            return format_enum(node["enum"]), []
        fmt = node.get("format")
        base = t or "any"
        return (f"{base} ({fmt})" if fmt else base), refs

    def fields_of(schema_node):
        node = resolve(schema_node) if "$ref" in (schema_node or {}) else (schema_node or {})
        if "allOf" in node:
            props, required = {}, []
            for part in node["allOf"]:
                p = resolve(part)
                props.update(p.get("properties", {}))
                required.extend(p.get("required", []))
            node = {"type": "object", "properties": props, "required": required}
        props = node.get("properties", {})
        required = set(node.get("required", []))
        out, nested = [], set()
        for name, pschema in props.items():
            t, refs = type_str(pschema)
            nested.update(refs)
            desc = pschema.get("description", "") or resolve(pschema).get("description", "")
            out.append((name, t, name in required, desc))
        return out, nested

    def example_value(pschema, depth=0):
        if depth > 3:
            return "..."
        node = resolve(pschema) if isinstance(pschema, dict) and "$ref" in pschema else pschema
        if not isinstance(node, dict):
            return None
        if "example" in node:
            return node["example"]
        if node.get("enum"):
            return node["enum"][0]
        t, fmt = node.get("type"), node.get("format")
        if "oneOf" in node or "anyOf" in node:
            return example_value((node.get("oneOf") or node.get("anyOf"))[0], depth + 1)
        if t == "array":
            return [example_value(node.get("items", {}), depth + 1)]
        if t == "object" or "properties" in node:
            obj, props = {}, node.get("properties", {})
            required = set(node.get("required", [])) & set(props.keys())
            keys = list(required) if required else list(props.keys())[:4]
            for k in keys:
                obj[k] = example_value(props[k], depth + 1)
            return obj
        if t == "string":
            if fmt == "uuid":
                return "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            if fmt in ("date", "date-time"):
                return "2024-01-01T00:00:00Z"
            return "string"
        if t == "integer" or t == "number":
            return 0
        if t == "boolean":
            return True
        return None

    return resolve, type_str, fields_of, example_value


def md_table(fields):
    if not fields:
        return "_No fields._\n"
    lines = ["| Name | Type | Required | Description |", "|---|---|---|---|"]
    for name, t, req, desc in fields:
        desc = (desc or "").replace("\n", " ").replace("|", "\\|")
        t = (t or "").replace("\n", " ").replace("|", "\\|")
        lines.append(f"| `{name}` | {t} | {'yes' if req else 'no'} | {desc} |")
    return "\n".join(lines) + "\n"


def build_operation_md(method, path, op, comps_to_expand, helpers):
    resolve, type_str, fields_of, example_value = helpers
    lines = []
    summary = op.get("summary", "")
    description = op.get("description", "")
    lines.append(f"## `{method} {path}`")
    lines.append("")
    lines.append(f"**{summary}**" + (f" — {description}" if description and description != summary else ""))
    lines.append("")
    lines.append(f"- **operationId**: `{op.get('operationId', '')}`")
    if op.get("deprecated"):
        lines.append("- **Status**: ⚠️ deprecated")
    lines.append("")

    params = op.get("parameters", [])
    if params:
        lines.append("**Parameters**")
        lines.append("")
        rows = []
        for p in params:
            t, refs = type_str(p.get("schema", {}))
            comps_to_expand.update(refs)
            rows.append((f"{p['name']} ({p.get('in')})", t, p.get("required", False), p.get("description", "")))
        lines.append(md_table(rows))

    rb = op.get("requestBody")
    example_body = None
    if rb:
        content = rb.get("content", {})
        media = content.get("application/json") or content.get("application/x-yaml") or next(iter(content.values()), {})
        body_schema = media.get("schema", {})
        fields, nested = fields_of(body_schema)
        comps_to_expand.update(nested)
        lines.append(f"**Request body** ({'required' if rb.get('required') else 'optional'}, `application/json`)")
        lines.append("")
        lines.append(md_table(fields))
        example_body = example_value(body_schema)

    lines.append("**Response**")
    lines.append("")
    responses = op.get("responses", {})
    example_response, response_status = None, None
    for code in [c for c in responses if c.startswith("2")]:
        r = responses[code]
        content = r.get("content", {})
        if not content:
            lines.append(f"- `{code}` — {r.get('description', '')} (no body)")
            continue
        media = content.get("application/json") or next(iter(content.values()), {})
        rschema = media.get("schema", {})
        t, refs = type_str(rschema)
        comps_to_expand.update(refs)
        lines.append(f"- `{code}` — {r.get('description', '')}: {t}")
        if example_response is None:
            example_response = example_value(rschema)
            response_status = code
    lines.append("")

    lines.append("**Example call**")
    lines.append("")
    lines.append("```bash")
    curl = [f"curl -X {method} \\", f'  "https://{{tenant}}.siffletdata.com/api{path}" \\', '  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \\']
    if rb:
        curl.append('  -H "Content-Type: application/json" \\')
        curl.append(f"  -d '{json.dumps(example_body, indent=2) if example_body else '{}'}'")
    else:
        curl[-1] = curl[-1].rstrip(" \\")
    lines.append("\n".join(curl))
    lines.append("```")
    if example_response is not None:
        lines.append("")
        lines.append(f"Example `{response_status}` response:")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(example_response, indent=2))
        lines.append("```")
    lines.append("")

    error_codes = [c for c in responses if not c.startswith("2")]
    if error_codes:
        lines.append("**Errors**")
        lines.append("")
        lines.append("| Status | Description |")
        lines.append("|---|---|")
        for code in sorted(error_codes):
            lines.append(f"| `{code}` | {responses[code].get('description', '')} |")
        lines.append("")
        lines.append("Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).")
        lines.append("")

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def build_schema_appendix(names, comps, helpers):
    _, _, fields_of, _ = helpers
    lines = ["## Referenced object schemas", ""]
    seen, queue = set(), list(names)
    while queue:
        name = queue.pop(0)
        if name in seen:
            continue
        seen.add(name)
        node = comps.get(name, {})
        lines.append(f"### `{name}` {{#schema-{name.lower()}}}")
        lines.append("")
        if node.get("description"):
            lines.append(node["description"])
            lines.append("")
        fields, nested = fields_of(node)
        lines.append(md_table(fields))
        lines.append("")
        for n in nested:
            if n not in seen:
                queue.append(n)
    return "\n".join(lines)


def build_readme(manifest, spec):
    servers = spec.get("servers", [])
    prod = next((s for s in servers if "tenant" in s.get("url", "")), servers[0] if servers else {})
    lines = [
        "# Sifflet Public API",
        "",
        "Reference for the Sifflet **public REST API** (`/api/v1`, `/api/v2`) that the",
        "`sifflet` plugin's commands, skills, and any future capabilities call into.",
        "This complements — it does not replace — the Sifflet CLI (`sifflet code ...`,",
        "documented in the `sifflet-quality-as-code` skill) and the Sifflet MCP server",
        "(documented in the `sifflet-mcp` skill), which cover Monitors as Code and",
        "catalog discovery respectively. Reach for this API reference when a plugin",
        "capability needs an operation the CLI/MCP don't expose (e.g. managing users,",
        "teams, domains, credentials, calendars, notification rules, or sources).",
        "",
        "**Canonical upstream reference:** https://docs.siffletdata.com/reference/overview-1",
        "If this documentation and the upstream reference ever disagree, the upstream",
        "reference wins — file a follow-up to refresh `openapi.json` (see below).",
        "",
        "## Authentication",
        "",
        "Every endpoint requires a bearer **Access Token** "
        "([docs](https://docs.siffletdata.com/docs/access-tokens), "
        "[generate one](https://docs.siffletdata.com/docs/generate-an-api-token)):",
        "",
        "```",
        "Authorization: Bearer <SIFFLET_API_TOKEN>",
        "```",
        "",
        "## Base URL",
        "",
        f"- **SaaS**: `{prod.get('url', 'https://{tenant}.siffletdata.com/api')}` — "
        + prod.get("variables", {}).get("tenant", {}).get(
            "description", "`tenant` is the subdomain you use to access the Sifflet UI."
        ),
        "- **Self-hosted**: `<sifflet-ui-url>/api/v2` (some deployments use a separate",
        "  `backendApiUrl` from Helm config, without the `/api` segment — check with the",
        "  customer's deployment config before hardcoding a URL).",
        "",
        "Both `application/json` and `application/x-yaml` request bodies are accepted",
        "where noted.",
        "",
        "## Standard error format",
        "",
        "Non-2xx responses return `application/problem+json` shaped as `ApiProblemSchema`:",
        "",
        "| Name | Type | Description |",
        "|---|---|---|",
        "| `type` | string | Problem type URI |",
        "| `title` | string | Short, human-readable summary |",
        "| `status` | integer | HTTP status code |",
        "| `detail` | string | Human-readable explanation specific to this occurrence |",
        "| `response` | string | Additional response context |",
        "",
        "## Versioning",
        "",
        "- **Sources**: v1 (`/v1/sources`, tag *Sources (deprecated)*) is deprecated — use",
        "  **v2** (`/v2/sources`) for any new integration. See",
        "  [sources-v1.md](sources-v1.md) and [sources-v2.md](sources-v2.md).",
        "- Everything else currently lives under `/v1`.",
        "",
        "## Domains",
        "",
        "| File | Domain | Endpoints |",
        "|---|---|---|",
    ]
    for fname, title, desc, n in manifest:
        lines.append(f"| [{fname}]({fname}) | {title} | {n} |")
    lines.append("")
    lines.append("Each file documents every endpoint in that domain: method + path,")
    lines.append("description, parameters, request/response schema, a runnable `curl`")
    lines.append("example, and possible error statuses.")
    lines.append("")
    lines.append("## Raw spec")
    lines.append("")
    lines.append("[`openapi.json`](openapi.json) is the full OpenAPI 3.0 document these")
    lines.append("pages are generated from. It has no officially published download URL —")
    lines.append("it was extracted from the `document.api.schema` field embedded in the")
    lines.append("server-rendered props of any `docs.siffletdata.com/reference/*` page")
    lines.append("(inspect the `#ssr-props` `<script>` tag). To refresh after an upstream")
    lines.append("API change:")
    lines.append("")
    lines.append("1. Fetch any reference page, e.g. `curl -sL https://docs.siffletdata.com/reference/publicgetasset-1`.")
    lines.append("2. Extract the JSON in `<script id=\"ssr-props\">...</script>`, then pull `.document.api.schema`.")
    lines.append("3. Save it as `docs/api/openapi.json`.")
    lines.append("4. Run `python3 scripts/generate_api_docs.py` to regenerate every file below.")
    lines.append("")
    lines.append("This extraction path is undocumented vendor internals, not a stable public")
    lines.append("contract — if it stops working, fall back to reading")
    lines.append("https://docs.siffletdata.com/reference/overview-1 by hand.")
    lines.append("")
    return "\n".join(lines)


def main():
    spec = load_spec()
    comps = spec["components"]["schemas"]
    helpers = make_helpers(comps)

    by_file = defaultdict(list)
    titles = {}
    for path, methods in spec["paths"].items():
        for method, op in methods.items():
            if method not in ("get", "post", "put", "patch", "delete"):
                continue
            tag = (op.get("tags") or ["Untagged"])[0]
            slug, title, desc = TAG_TO_FILE.get(tag, (tag.lower().replace(" ", "-"), tag, ""))
            titles[slug] = (title, desc)
            by_file[slug].append((method.upper(), path, op))

    manifest = []
    for slug in sorted(by_file):
        ops = sorted(by_file[slug], key=lambda x: (x[1], x[0]))
        comps_to_expand = set()
        title, desc = titles[slug]
        body = [f"# {title}", "", desc, "", "[← Back to API index](README.md)", ""]
        for method, path, op in ops:
            body.append(build_operation_md(method, path, op, comps_to_expand, helpers))
        if comps_to_expand:
            body.append(build_schema_appendix(comps_to_expand, comps, helpers))
        with open(os.path.join(API_DIR, f"{slug}.md"), "w") as f:
            f.write("\n".join(body))
        manifest.append((f"{slug}.md", title, desc, len(ops)))

    with open(os.path.join(API_DIR, "README.md"), "w") as f:
        f.write(build_readme(manifest, spec))

    print(f"Generated {len(manifest)} domain files + README.md in {API_DIR}")
    for fname, title, _, n in manifest:
        print(f"  {fname:45} {title:45} {n} operations")


if __name__ == "__main__":
    main()
