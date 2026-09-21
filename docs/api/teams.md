# Teams

Teams used for asset ownership and access.

[← Back to API index](README.md)

## `GET /v1/teams`

**Get list of teams**

- **operationId**: `publicGetTeams`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `page (query)` | integer (int32) | no | The page number to retrieve. Starts at 0. |
| `itemsPerPage (query)` | integer (int32) | no | The number of elements to be returned inside the page. |

**Response**

- `200` — Teams retrieved: [`PublicPageDtoPublicGetTeamDto`](#schema-publicpagedtopublicgetteamdto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/teams" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "data": [
    {
      "name": "string",
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }
  ]
}
```

**Errors**

| Status | Description |
|---|---|
| `401` | Unauthorized |
| `403` | Forbidden |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `POST /v1/teams`

**Create a team**

- **operationId**: `publicCreateTeam`

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no | Description of the team |
| `domainPermissions` | array<[`PublicTeamPermissionAssignmentDto`](#schema-publicteampermissionassignmentdto)> | no | Domains permissions granted to the team |
| `name` | string | yes | Name of the team |
| `users` | array<[`PublicReferenceByIdOrEmailDto`](#schema-publicreferencebyidoremaildto)> | no | Users belonging to the team |

**Response**

- `201` — Team created: [`PublicGetTeamDto`](#schema-publicgetteamdto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v1/teams" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string"
}'
```

Example `201` response:

```json
{
  "name": "string",
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

**Errors**

| Status | Description |
|---|---|
| `400` | Bad request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `DELETE /v1/teams/{id}`

**Delete a team**

- **operationId**: `publicDeleteTeam`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `204` — Team deleted (no body)

**Example call**

```bash
curl -X DELETE \
  "https://{tenant}.siffletdata.com/api/v1/teams/{id}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

**Errors**

| Status | Description |
|---|---|
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Resource not found |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `GET /v1/teams/{id}`

**Get a team by id**

- **operationId**: `publicGetTeam`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `200` — Team retrieved: [`PublicGetTeamDto`](#schema-publicgetteamdto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/teams/{id}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "name": "string",
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

**Errors**

| Status | Description |
|---|---|
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Resource not found |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `PATCH /v1/teams/{id}`

**Update a team**

- **operationId**: `publicUpdateTeam`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no | Description of the team |
| `domainPermissions` | array<[`PublicTeamPermissionAssignmentDto`](#schema-publicteampermissionassignmentdto)> | no | Domains permissions granted to the team |
| `name` | string | yes | Name of the team |
| `users` | array<[`PublicReferenceByIdOrEmailDto`](#schema-publicreferencebyidoremaildto)> | no | Users belonging to the team |

**Response**

- `200` — Team updated: [`PublicGetTeamDto`](#schema-publicgetteamdto)

**Example call**

```bash
curl -X PATCH \
  "https://{tenant}.siffletdata.com/api/v1/teams/{id}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string"
}'
```

Example `200` response:

```json
{
  "name": "string",
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

**Errors**

| Status | Description |
|---|---|
| `400` | Bad request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Resource not found |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## Referenced object schemas

### `PublicTeamPermissionAssignmentDto` {#schema-publicteampermissionassignmentdto}

Domains permissions granted to the team

| Name | Type | Required | Description |
|---|---|---|---|
| `domainId` | string (uuid) | yes | Id of the domain |
| `domainRole` | enum (`EDITOR`, `MONITOR_RESPONDER`, `CATALOG_EDITOR`, `VIEWER`) | yes | Domain role assigned to the team for accessing the referenced domain |


### `PublicPageDtoPublicGetTeamDto` {#schema-publicpagedtopublicgetteamdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `data` | array<[`PublicGetTeamDto`](#schema-publicgetteamdto)> | yes |  |
| `totalCount` | integer (int64) | no |  |


### `PublicGetTeamDto` {#schema-publicgetteamdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no | Description of the team |
| `domainPermissions` | array<[`PublicTeamPermissionAssignmentDto`](#schema-publicteampermissionassignmentdto)> | no | Domains permissions granted to the team |
| `id` | string (uuid) | yes |  |
| `name` | string | yes | Name of the team |
| `users` | array<[`PublicReferenceByIdOrEmailDto`](#schema-publicreferencebyidoremaildto)> | no | Users belonging to the team |


### `PublicReferenceByIdOrEmailDto` {#schema-publicreferencebyidoremaildto}

Id or email reference to an owner

| Name | Type | Required | Description |
|---|---|---|---|
| `email` | string | no | Email of the referenced owner |
| `id` | string (uuid) | no | Id of the referenced owner |

