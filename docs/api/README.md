# Sifflet Public API

Reference for the Sifflet **public REST API** (`/api/v1`, `/api/v2`) that the
`sifflet` plugin's commands, skills, and any future capabilities call into.
This complements — it does not replace — the Sifflet CLI (`sifflet code ...`,
documented in the `sifflet-quality-as-code` skill) and the Sifflet MCP server
(documented in the `sifflet-mcp` skill), which cover Monitors as Code and
catalog discovery respectively. Reach for this API reference when a plugin
capability needs an operation the CLI/MCP don't expose (e.g. managing users,
teams, domains, credentials, calendars, notification rules, or sources).

**Canonical upstream reference:** https://docs.siffletdata.com/reference/overview-1
If this documentation and the upstream reference ever disagree, the upstream
reference wins — file a follow-up to refresh `openapi.json` (see below).

## Authentication

Every endpoint requires a bearer **Access Token** ([docs](https://docs.siffletdata.com/docs/access-tokens), [generate one](https://docs.siffletdata.com/docs/generate-an-api-token)):

```
Authorization: Bearer <SIFFLET_API_TOKEN>
```

## Base URL

- **SaaS**: `https://{tenant}.siffletdata.com/api` — if you access to Sifflet with `https://abcdef.siffletdata.com`, then your tenant would be `abcdef`
- **Self-hosted**: `<sifflet-ui-url>/api/v2` (some deployments use a separate
  `backendApiUrl` from Helm config, without the `/api` segment — check with the
  customer's deployment config before hardcoding a URL).

Both `application/json` and `application/x-yaml` request bodies are accepted
where noted.

## Standard error format

Non-2xx responses return `application/problem+json` shaped as `ApiProblemSchema`:

| Name | Type | Description |
|---|---|---|
| `type` | string | Problem type URI |
| `title` | string | Short, human-readable summary |
| `status` | integer | HTTP status code |
| `detail` | string | Human-readable explanation specific to this occurrence |
| `response` | string | Additional response context |

## Versioning

- **Sources**: v1 (`/v1/sources`, tag *Sources (deprecated)*) is deprecated — use
  **v2** (`/v2/sources`) for any new integration. See
  [sources-v1.md](sources-v1.md) and [sources-v2.md](sources-v2.md).
- Everything else currently lives under `/v1`.

## Domains

| File | Domain | Endpoints |
|---|---|---|
| [assets.md](assets.md) | Assets | 3 |
| [calendars.md](calendars.md) | Calendars | 5 |
| [credentials.md](credentials.md) | Credentials | 5 |
| [dbt-integration.md](dbt-integration.md) | dbt Integration | 1 |
| [declarative-assets-and-lineage.md](declarative-assets-and-lineage.md) | Declarative Assets and Lineage (Workspace sync) | 2 |
| [domains.md](domains.md) | Domains | 5 |
| [external-catalog.md](external-catalog.md) | External Catalog | 1 |
| [monitoring-rules.md](monitoring-rules.md) | Monitoring Rules | 10 |
| [notification-rules.md](notification-rules.md) | Notification Rules | 5 |
| [sources-v1.md](sources-v1.md) | Sources (v1, deprecated) | 7 |
| [sources-v2.md](sources-v2.md) | Sources (v2) | 12 |
| [teams.md](teams.md) | Teams | 5 |
| [users.md](users.md) | Users | 6 |

Each file documents every endpoint in that domain: method + path,
description, parameters, request/response schema, a runnable `curl`
example, and possible error statuses.

## Raw spec

[`openapi.json`](openapi.json) is the full OpenAPI 3.0 document these
pages are generated from. It has no officially published download URL —
it was extracted from the `document.api.schema` field embedded in the
server-rendered props of any `docs.siffletdata.com/reference/*` page
(inspect the `#ssr-props` `<script>` tag). To refresh after an upstream
API change:

1. Fetch any reference page, e.g. `curl -sL https://docs.siffletdata.com/reference/publicgetasset-1`.
2. Extract the JSON in `<script id="ssr-props">...</script>`, then pull `.document.api.schema`.
3. Save it as `docs/api/openapi.json`.
4. Run `python3 scripts/generate_api_docs.py` to regenerate every file below.

This extraction path is undocumented vendor internals, not a stable public
contract — if it stops working, fall back to reading
https://docs.siffletdata.com/reference/overview-1 by hand.
