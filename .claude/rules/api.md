# Sifflet API rules

Detailed rules for any plugin capability (command, skill, script) that calls
the Sifflet **public REST API** directly (as opposed to going through the
Sifflet CLI or the bundled MCP server). Referenced from the root `CLAUDE.md`.
Source of truth for the API itself is `docs/api/` — this file is about how to
use it safely inside this plugin.

## Before writing any API call

1. Look up the endpoint in `docs/api/<domain>.md`. If it's not there, or the
   plugin's `docs/api/openapi.json` looks older than the behavior you're
   seeing from the live API, refresh it first (procedure in
   `docs/api/README.md`) rather than guessing the shape.
2. Confirm which base URL applies: SaaS (`https://{tenant}.siffletdata.com/api`)
   vs self-hosted (`<sifflet-ui-url>/api/v2`, or a custom `backendApiUrl`).
   Never hardcode a tenant or assume SaaS.
3. Confirm auth: every endpoint needs `Authorization: Bearer <token>`. Reuse
   the same credential resolution the rest of the plugin uses
   (`SIFFLET_API_TOKEN` / `SIFFLET_BACKEND_URL`, falling back to
   `~/.sifflet/config.ini` — see the `configure-sifflet-auth` command).
   Do not introduce a second, inconsistent way to read credentials.

## Conventions in the API itself (reflect these in new capabilities)

- **Naming**: operation IDs are `public<Verb><Resource>`
  (`publicGetAssets`, `publicCreateSource`, …); path segments are
  lower-kebab (`/v1/notification-rules`). Match this style in any
  command/skill names you add for consistency, even though the plugin's own
  command names already follow their own `kebab-case` convention.
- **Versioning**: a resource can have a `(deprecated)` v1 and a current v2
  tag (currently only Sources: `/v1/sources` vs `/v2/sources`). Always use
  the non-deprecated version for new capabilities; only touch a deprecated
  endpoint if the user explicitly needs the old behavior.
- **Errors**: non-2xx responses are `application/problem+json`,
  `ApiProblemSchema` (`type`, `title`, `status`, `detail`, `response`) — see
  `docs/api/README.md#standard-error-format`. Surface `detail` to the user
  rather than swallowing it; do not invent a different error shape for a new
  capability.
- **Response format**: bodies are `application/json` (some requests also
  accept `application/x-yaml`). List endpoints return a paginated envelope
  (`data` + `totalCount`, `pagination.page` / `itemsPerPage`) — do not assume
  a bare array.
- **Response codes for mutations**: `201` for create, `204` (no body) for
  delete, `200` for edit — check the specific endpoint's doc, this is not
  100% uniform across domains.

## Destructive-call gating — read this before adding a mutating capability

The bundled guard hook (`hooks/guard-sifflet-destructive.py`) only inspects
**Bash commands** (regexes in `classify_shell`) and **MCP tool names**
(`classify_mcp`). It does **not** understand arbitrary HTTP calls. If a new
plugin capability calls a mutating Sifflet API endpoint
(`POST`/`PATCH`/`PUT`/`DELETE` per `docs/api/`) — whether via `curl` in a
documented command, a Python/Node script, or any other client — the existing
guard will **not** automatically catch it unless the shape of the shell
command you generate happens to match an existing regex.

When you add such a capability, do one of:

1. **Extend the guard.** Add a pattern to `classify_shell` (for a
   shell/curl-based capability) so destructive calls are recognized the same
   way `sifflet ... apply` and `workspace delete` are today. Add coverage in
   `tests/test_guard_sifflet_destructive.py` and re-run
   `bash scripts/selftest.sh`.
2. **Embed the protocol in the command/skill itself.** Follow the
   **destructive-change confirmation protocol** in the
   `sifflet-quality-as-code` skill: show what will change, state what's
   irreversible, and require an explicit typed confirmation before calling
   a mutating endpoint (deleting a user/team/domain/source/credential/
   notification rule/calendar, or any operation that removes data or
   revokes access). Never accept a casual "yes" for a `DELETE` call.

Do not ship a new capability that calls a mutating Sifflet endpoint with
neither of these — that is the gap this plugin exists to close.

## Never silently break a contract

Do not change what a shipped command/skill sends to, or expects back from,
the Sifflet API without calling it out explicitly (see root `CLAUDE.md`).
Concretely: don't rename a parameter a command passes, don't switch which
API version it targets, and don't change how it parses a response, without
flagging that as a breaking change in the PR/commit description — someone
may have scripted around the current behavior.
