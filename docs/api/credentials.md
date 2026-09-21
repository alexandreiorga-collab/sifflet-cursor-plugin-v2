# Credentials

Stored credentials referenced by data sources.

[← Back to API index](README.md)

## `GET /v1/credentials`

**Get list of credentials**

- **operationId**: `publicGetAllCredentials`

**Response**

- `200` — Credentials retrieved: [`PublicCredentialsPageDtoPublicCredentialsGetDto`](#schema-publiccredentialspagedtopubliccredentialsgetdto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/credentials" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "data": [
    {
      "name": "string"
    }
  ]
}
```

**Errors**

| Status | Description |
|---|---|
| `401` | Unauthorized |
| `403` | Forbidden |
| `429` | Too many requests |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `POST /v1/credentials`

**Create credentials** — This operation is eventually consistent. If you create a secret and attempt to retrieve it immediately, the GET endpoint may return a NotFound response

- **operationId**: `publicCreateCredentials`

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no | Description of credentials |
| `name` | string | yes | Name of credentials. Must start and end with a letter, and contain only letters, digits, and hyphens |
| `value` | string | yes | Value of credentials. Double quotes must be escaped with a backslash. |

**Response**

- `201` — Credentials created (no body)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v1/credentials" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "value": "{\"user\":\"rmwEPZILBnEYLtJxEFea\",\"password\":\"NoEGLWfNCMctymuJTYHMMeJt\"}",
  "name": "looker"
}'
```

**Errors**

| Status | Description |
|---|---|
| `400` | Bad request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `409` | Conflict |
| `429` | Too many requests |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `DELETE /v1/credentials/{name}`

**Delete credentials**

- **operationId**: `publicDeleteCredentials`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `name (path)` | string | yes |  |

**Response**

- `204` — Credentials deleted (no body)

**Example call**

```bash
curl -X DELETE \
  "https://{tenant}.siffletdata.com/api/v1/credentials/{name}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

**Errors**

| Status | Description |
|---|---|
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Resource not found |
| `429` | Too many requests |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `GET /v1/credentials/{name}`

**Get credentials by name**

- **operationId**: `publicGetCredentials`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `name (path)` | string | yes |  |

**Response**

- `200` — Credentials retrieved: [`PublicCredentialsGetDto`](#schema-publiccredentialsgetdto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/credentials/{name}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "name": "string"
}
```

**Errors**

| Status | Description |
|---|---|
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Resource not found |
| `429` | Too many requests |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `PATCH /v1/credentials/{name}`

**Update credentials**

- **operationId**: `publicUpdateCredentials`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `name (path)` | string | yes |  |

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no | Description of credentials |
| `value` | string | no | Value of credentials. Double quotes must be escaped with a backslash. |

**Response**

- `204` — Credentials updated (no body)

**Example call**

```bash
curl -X PATCH \
  "https://{tenant}.siffletdata.com/api/v1/credentials/{name}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "description": "Credentials for Looker",
  "value": "{\"user\":\"rmwEPZILBnEYLtJxEFea\",\"password\":\"NoEGLWfNCMctymuJTYHMMeJt\"}"
}'
```

**Errors**

| Status | Description |
|---|---|
| `400` | Bad request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Resource not found |
| `429` | Too many requests |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## Referenced object schemas

### `PublicCredentialsPageDtoPublicCredentialsGetDto` {#schema-publiccredentialspagedtopubliccredentialsgetdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `data` | array<[`PublicCredentialsGetDto`](#schema-publiccredentialsgetdto)> | yes |  |
| `totalCount` | integer (int64) | no | Number of credentials on the account |


### `PublicCredentialsGetDto` {#schema-publiccredentialsgetdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no | Description of credentials |
| `name` | string | yes | Name of credentials |

