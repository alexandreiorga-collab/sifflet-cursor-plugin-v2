# Users

User accounts: list, create, update, delete, reset password.

[← Back to API index](README.md)

## `GET /v1/users`

**Get list of users**

- **operationId**: `publicGetUsers`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `page (query)` | integer (int32) | no | The page number to retrieve. Starts at 0. |
| `itemsPerPage (query)` | integer (int32) | no | The number of elements to be returned inside the page. |

**Response**

- `200` — Users retrieved: [`PublicPageDtoPublicUserGetDto`](#schema-publicpagedtopublicusergetdto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/users" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "data": [
    {
      "name": "string",
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "role": "ADMIN",
      "authTypes": [
        "..."
      ],
      "permissions": [
        "..."
      ],
      "email": "string",
      "status": "ENABLED",
      "teams": [
        "..."
      ]
    }
  ]
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

## `POST /v1/users`

**Create a user**

- **operationId**: `publicCreateUser`

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `authTypes` | array<enum (`SAML2`, `LOGIN_PASSWORD`)> | no | Authorized authentication type of the user |
| `email` | string | yes | Email of the user |
| `name` | string | yes | Name of the user |
| `permissions` | array<[`PublicUserPermissionAssignmentDto`](#schema-publicuserpermissionassignmentdto)> | no | Domain access permissions of the user |
| `role` | enum (`ADMIN`, `EDITOR`, `VIEWER`) | yes | System role of the user |

**Response**

- `201` — User created: [`PublicUserGetDto`](#schema-publicusergetdto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v1/users" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "role": "ADMIN",
  "email": "string",
  "name": "string"
}'
```

Example `201` response:

```json
{
  "name": "string",
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "role": "ADMIN",
  "authTypes": [
    "SAML2"
  ],
  "permissions": [
    {
      "domainId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }
  ],
  "email": "string",
  "status": "ENABLED",
  "teams": [
    {
      "teamId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }
  ]
}
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

## `DELETE /v1/users/{id}`

**Delete a user**

- **operationId**: `publicDeleteUser`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `204` — User deleted (no body)

**Example call**

```bash
curl -X DELETE \
  "https://{tenant}.siffletdata.com/api/v1/users/{id}" \
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

## `GET /v1/users/{id}`

**Get a user by id**

- **operationId**: `publicGetUser`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `200` — User retrieved: [`PublicUserGetDto`](#schema-publicusergetdto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/users/{id}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "name": "string",
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "role": "ADMIN",
  "authTypes": [
    "SAML2"
  ],
  "permissions": [
    {
      "domainId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }
  ],
  "email": "string",
  "status": "ENABLED",
  "teams": [
    {
      "teamId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }
  ]
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

## `PATCH /v1/users/{id}`

**Update a user**

- **operationId**: `publicUpdateUser`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `authTypes` | array<enum (`SAML2`, `LOGIN_PASSWORD`)> | no | Authorized authentication type of the user |
| `name` | string | yes | Name of the user |
| `permissions` | array<[`PublicUserPermissionAssignmentDto`](#schema-publicuserpermissionassignmentdto)> | no | Domain access permissions of the user |
| `role` | enum (`ADMIN`, `EDITOR`, `VIEWER`) | yes | System role of the user |

**Response**

- `200` — User updated: [`PublicUserGetDto`](#schema-publicusergetdto)

**Example call**

```bash
curl -X PATCH \
  "https://{tenant}.siffletdata.com/api/v1/users/{id}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "role": "ADMIN",
  "name": "string"
}'
```

Example `200` response:

```json
{
  "name": "string",
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "role": "ADMIN",
  "authTypes": [
    "SAML2"
  ],
  "permissions": [
    {
      "domainId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }
  ],
  "email": "string",
  "status": "ENABLED",
  "teams": [
    {
      "teamId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }
  ]
}
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

## `POST /v1/users/{id}/reset-password`

**Reset a user password**

- **operationId**: `publicResetUserPassword`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `200` — User password reset: [`PublicUserResetPasswordDto`](#schema-publicuserresetpassworddto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v1/users/{id}/reset-password" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "password": "string"
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

## Referenced object schemas

### `PublicUserGetDto` {#schema-publicusergetdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `authTypes` | array<enum (`SAML2`, `LOGIN_PASSWORD`)> | yes | Authorized authentication type of the user |
| `email` | string | yes | Email of the user |
| `id` | string (uuid) | yes |  |
| `name` | string | yes | Name of the user |
| `permissions` | array<[`PublicUserPermissionAssignmentDto`](#schema-publicuserpermissionassignmentdto)> | yes | Domain access permissions of the user |
| `role` | enum (`ADMIN`, `EDITOR`, `VIEWER`) | yes | System role of the user |
| `status` | enum (`ENABLED`, `DISABLED`) | yes | Status of the user |
| `teams` | array<[`PublicUserTeamDto`](#schema-publicuserteamdto)> | yes | Teams of the user |


### `PublicPageDtoPublicUserGetDto` {#schema-publicpagedtopublicusergetdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `data` | array<[`PublicUserGetDto`](#schema-publicusergetdto)> | yes |  |
| `totalCount` | integer (int64) | no |  |


### `PublicUserResetPasswordDto` {#schema-publicuserresetpassworddto}

| Name | Type | Required | Description |
|---|---|---|---|
| `password` | string | yes |  |


### `PublicUserPermissionAssignmentDto` {#schema-publicuserpermissionassignmentdto}

Domain access permissions of the user

| Name | Type | Required | Description |
|---|---|---|---|
| `domainId` | string (uuid) | yes | Id of the domain |
| `domainRole` | enum (`EDITOR`, `MONITOR_RESPONDER`, `CATALOG_EDITOR`, `VIEWER`) | no | Domain role assigned to the principal for accessing the referenced domain |


### `PublicUserTeamDto` {#schema-publicuserteamdto}

Teams of the user

| Name | Type | Required | Description |
|---|---|---|---|
| `teamId` | string (uuid) | yes | Id of the team |

