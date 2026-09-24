# Sifflet plugin — working notes for Claude Code

This repo is a Cursor / Claude Code **plugin** for Sifflet data observability
(see `README.md`). It ships three ways to talk to Sifflet, each with its own
scope — do not blend them:

- **Sifflet CLI** (`sifflet code ...`) — Monitors as Code. Covered by the
  `sifflet-quality-as-code` skill.
- **Sifflet MCP server** (bundled via `mcp.json` / `.mcp.json`) — read-heavy
  catalog/incident discovery from Agent chat. Covered by the `sifflet-mcp`
  skill. Most of its tools are read-only; `open_incident_by_id` /
  `close_incident_by_id` mutate state.
- **Sifflet public REST API** (`/api/v1`, `/api/v2`) — everything else: users,
  teams, domains, credentials, calendars, notification rules, sources, and
  direct asset/monitor access. Covered by the `sifflet-api` skill.
  **`docs/api/` is the source of truth for this API** — read it before
  writing any code or command that calls it.

## `docs/api/` is the source of truth

- `docs/api/README.md` — index, auth, base URL, error format, versioning.
- `docs/api/<domain>.md` — one file per API domain (assets, sources-v2, users,
  …), each endpoint with signature, parameters, response, a `curl` example,
  and possible errors.
- `docs/api/openapi.json` — the raw OpenAPI spec these pages are generated
  from, and `scripts/generate_api_docs.py` regenerates the `.md` files from
  it (see `docs/api/README.md` for the refresh procedure — there is no
  officially downloadable spec URL, so this is semi-manual).

Before adding or changing any plugin capability (command, skill, script) that
calls the Sifflet REST API: **check `docs/api/` first.** Do not guess a
request/response shape from memory or invent an endpoint — verify it exists
in `docs/api/`, and if it's missing or looks stale, refresh
`docs/api/openapi.json` and regenerate before relying on it.

When you add, remove, or change which Sifflet API endpoint a command/skill
uses, **update the relevant `docs/api/*.md` in the same change** (or note
in the PR description that a spec refresh is needed). Docs and behavior
must not drift.

Detailed API conventions (auth, versioning, error handling, destructive-call
gating) live in **[.claude/rules/api.md](.claude/rules/api.md)** — read it
before writing code that calls the Sifflet API.

## Never silently break a contract

Do not change an existing plugin capability's request shape, response
shape, exit code, or hook decision format without calling it out explicitly
to the user — other people's scripts, CI pipelines, and installed plugin
copies depend on these staying stable. This applies to:

- The guard hook's stdin/stdout JSON contract (`hooks/guard-sifflet-destructive.py`).
- Any command/skill's documented inputs or outputs (`commands/*.md`, `skills/*/SKILL.md`).
- How a plugin capability calls the Sifflet API (which endpoint, method, params).

If a change is genuinely necessary, say so plainly, explain what breaks, and
prefer additive changes over silently altering existing behavior.

## Other conventions

- Run `python3 scripts/validate_manifests.py` after touching any manifest,
  hook config, skill, or command — it also validates that every `.json` in
  the repo (including `docs/api/openapi.json`) parses.
- Run `bash scripts/selftest.sh` after touching the guard hook.
- See `TESTING.md` for the full test layering.
