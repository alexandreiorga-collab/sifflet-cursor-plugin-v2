# dbt Integration

Submit dbt metadata files and trigger the related datasource refresh.

[← Back to API index](README.md)

## `POST /v1/metadata/dbt/{projectName}/{target}`

**Submit dbt metadata files and trigger the related datasource refresh**

- **operationId**: `uploadDbtMetadataFiles`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `projectName (path)` | string | yes |  |
| `target (path)` | string | yes |  |

**Request body** (optional, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `catalog` | string (binary) | no |  |
| `manifest` | string (binary) | no |  |
| `run_results` | string (binary) | no |  |

**Response**

- `204` — Successfully updated files (no body)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v1/metadata/dbt/{projectName}/{target}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "catalog": "string",
  "manifest": "string",
  "run_results": "string"
}'
```

**Errors**

| Status | Description |
|---|---|
| `400` | Bad request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `409` | Conflict |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---
