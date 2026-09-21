---
name: sifflet-api
description: Call the Sifflet public REST API (users, teams, domains, credentials, calendars, notification rules, sources, assets, external catalog, dbt integration, declarative workspace sync, monitor/source run triggers) for operations the Sifflet CLI and MCP server don't expose. Use when the user wants to list/create/update/delete Sifflet users, teams, domains, credentials, calendars, or notification rules, manage sources directly via the API, edit or search assets, push external catalog metadata, submit dbt metadata, or trigger a monitor/source run via HTTP.
---

# Sifflet public REST API

## When to use this

- Use for operations the Sifflet CLI (Monitors as Code) and the Sifflet MCP
  server don't expose: users, teams, domains, credentials, calendars,
  notification rules, direct source management, asset edits/search, external
  catalog import, dbt metadata submission, ad-hoc monitor/source run
  triggers.
- Do **not** use this for Monitors as Code (workspace/monitor YAML) — use
  **sifflet-quality-as-code** plus the `mac-plan-workspace` /
  `mac-apply-workspace` commands instead; that flow shows a plan/diff before
  mutating, which this API mostly cannot.
- Do **not** use this for read-heavy catalog discovery that the MCP server
  already covers — prefer **sifflet-mcp** for that. Reach for this skill
  when you need a write, or a domain the MCP server doesn't cover (users,
  teams, domains, credentials, calendars, notification rules, sources).

## Source of truth

`docs/api/<domain>.md` documents every endpoint (method, path, parameters,
request/response schema, a runnable `curl` example, and possible errors).
Read the relevant file before making a call — do not guess a request/response
shape from memory. If it looks stale versus the live API, refresh it first
per the procedure in `docs/api/README.md`.

Domain files: `assets`, `calendars`, `credentials`, `dbt-integration`,
`declarative-assets-and-lineage`, `domains`, `external-catalog`,
`monitoring-rules`, `notification-rules`, `sources-v1` (deprecated — see
Versioning below), `sources-v2`, `teams`, `users`.

## Always call through the helper script

Never hand-roll `curl` for this API. Always invoke:

```bash
python3 "$CLAUDE_PLUGIN_ROOT/skills/sifflet-api/scripts/sifflet_api.py" \
  <METHOD> <PATH> [--data '<json>'] [--data-file <file>] \
  [--query k=v ...] [--confirm '<TOKEN>']
```

(If `$CLAUDE_PLUGIN_ROOT` isn't set in your environment, use the plugin's
checkout path instead, e.g. `skills/sifflet-api/scripts/sifflet_api.py`
relative to the repo root.)

The script resolves auth exactly the way the rest of the plugin does
(`SIFFLET_API_TOKEN` / `SIFFLET_BACKEND_URL`, falling back to
`~/.sifflet/config.ini`'s `[APP]` section — same resolution
`run-sifflet-mcp.sh` uses). Do not introduce a second way to read
credentials, and never print the resolved token into the conversation.

This is also the safety mechanism: the script **refuses to send any
non-`GET` request unless `--confirm` carries the exact required token**,
before it touches the network. Do not try to work around it by calling
`curl` directly — see the destructive-call gating rule in
`.claude/rules/api.md`. Bypassing the sanctioned path is a contract
violation, not a shortcut.

## Reads — no confirmation needed

Any `GET`, plus three documented endpoints that use `POST` for read
semantics (lookups, not mutations): `POST /v1/assets/search`,
`POST /v1/assets/get-asset-with-uri`, `POST /v1/sources/search`. Call these
directly.

List endpoints return a paginated envelope (`data` + `totalCount`,
`pagination.page` / `itemsPerPage`) — never assume a bare array.

## Mutations — confirmation protocol (mandatory)

This extends the **destructive-change confirmation protocol** from
`sifflet-quality-as-code` to the REST API. Same rule: the token must be
exact, case-sensitive, and typed by the user this turn — a casual "yes",
"ok", or "go ahead" never satisfies it, and you must never generate the
token yourself.

Before **any** non-read call:

1. Show the exact method, path, and body you're about to send.
2. State the effect in plain language, and whether it's reversible.
3. Get the token from the user, then pass it via `--confirm`.

Required tokens:

- Any non-delete `POST` / `PATCH` / `PUT` (create, update, test-connection,
  trigger a run, external catalog import, dbt metadata submit):
  **`CONFIRM SIFFLET MUTATE`** — reusing the token `sifflet-mcp` already
  uses for mutating MCP tools, for consistency.
- Any `DELETE`: **`DELETE <RESOURCE>`**, e.g. `DELETE USER`, `DELETE TEAM`,
  `DELETE DOMAIN`, `DELETE CREDENTIAL`, `DELETE CALENDAR`,
  `DELETE NOTIFICATION RULE`, `DELETE SOURCE`. State plainly that it cannot
  be undone.
- `DELETE /v1/assets/{name}` (delete workspace by name — the REST
  equivalent of `sifflet code workspace delete`): **`DELETE WORKSPACE`**,
  the same token the CLI flow uses, because it's the same underlying
  operation.
- `POST /v1/assets/sync` (declarative workspace sync — the REST equivalent
  of `sifflet code workspace apply`, but with **no dry-run**): prefer the
  CLI flow (`mac-plan-workspace` → `mac-apply-workspace`) so the user sees a
  plan first. Only call this endpoint directly if the user explicitly wants
  the raw API after being told there's no diff step; then require
  **`CONFIRM SIFFLET APPLY`**.

The script enforces the token match, but it only checks the string — you
still have to actually do steps 1–2 before asking for it.

## Versioning

Always use `/v2/sources/*`; `/v1/sources/*` (`sources-v1.md`) is deprecated
— only use it if the user explicitly needs v1 behavior.

## Errors

Non-2xx responses are `application/problem+json` (`ApiProblemSchema`):
`type`, `title`, `status`, `detail`, `response`. The script prints
`status` / `title` / `detail` to stderr on failure — surface `detail` to the
user rather than inventing a different error shape.

## Never

- Never print the resolved API token into the conversation.
- Never call the script with a confirm token you generated yourself — it
  must come from the user's own message, this turn.
- Never bypass the script by calling `curl` or another HTTP client for this
  API.
