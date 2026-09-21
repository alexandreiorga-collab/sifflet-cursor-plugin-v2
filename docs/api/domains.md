# Domains

Organizational domains used to group assets.

[← Back to API index](README.md)

## `GET /v1/domains`

**Get list of domains**

- **operationId**: `publicGetDomains`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `page (query)` | integer (int32) | no | The page number to retrieve. Starts at 0. |
| `itemsPerPage (query)` | integer (int32) | no | The number of elements to be returned inside the page. |

**Response**

- `200` — Domains retrieved: [`PublicPageDtoPublicGetDomainDto`](#schema-publicpagedtopublicgetdomaindto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/domains" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "data": [
    {
      "assetCount": 0,
      "assetContentDefinition": "...",
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

## `POST /v1/domains`

**Create a domain**

- **operationId**: `publicCreateDomain`

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `assetContentDefinition` | [`PublicDynamicDomainContentDefinitionDto`](#schema-publicdynamicdomaincontentdefinitiondto) or [`PublicStaticDomainContentDefinitionDto`](#schema-publicstaticdomaincontentdefinitiondto) | yes |  |
| `description` | string | no | Description of the domain |
| `name` | string | yes | Name of the domain |
| `parentDomainId` | string (uuid) | no | Id of the parent domain if the new domain is a subdomain. Do not specify this field if the new domain is not a subdomain. |

**Response**

- `201` — Domain created: [`PublicGetDomainDto`](#schema-publicgetdomaindto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v1/domains" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "assetContentDefinition": {}
}'
```

Example `201` response:

```json
{
  "assetCount": 0,
  "assetContentDefinition": {},
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

## `DELETE /v1/domains/{id}`

**Delete a domain**

- **operationId**: `publicDeleteDomain`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `204` — Domain deleted (no body)

**Example call**

```bash
curl -X DELETE \
  "https://{tenant}.siffletdata.com/api/v1/domains/{id}" \
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

## `GET /v1/domains/{id}`

**Get a domain by id**

- **operationId**: `publicGetDomain`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `200` — Domain retrieved: [`PublicGetDomainDto`](#schema-publicgetdomaindto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/domains/{id}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "assetCount": 0,
  "assetContentDefinition": {},
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

## `PATCH /v1/domains/{id}`

**Update a domain**

- **operationId**: `publicUpdateDomain`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `assetContentDefinition` | [`PublicDynamicDomainContentDefinitionDto`](#schema-publicdynamicdomaincontentdefinitiondto) or [`PublicStaticDomainContentDefinitionDto`](#schema-publicstaticdomaincontentdefinitiondto) | yes |  |
| `description` | string | no | Description of the domain |
| `name` | string | yes | Name of the domain |

**Response**

- `200` — Domain updated: [`PublicGetDomainDto`](#schema-publicgetdomaindto)

**Example call**

```bash
curl -X PATCH \
  "https://{tenant}.siffletdata.com/api/v1/domains/{id}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "assetContentDefinition": {}
}'
```

Example `200` response:

```json
{
  "assetCount": 0,
  "assetContentDefinition": {},
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

### `PublicPageDtoPublicGetDomainDto` {#schema-publicpagedtopublicgetdomaindto}

| Name | Type | Required | Description |
|---|---|---|---|
| `data` | array<[`PublicGetDomainDto`](#schema-publicgetdomaindto)> | yes |  |
| `totalCount` | integer (int64) | no |  |


### `PublicStaticDomainContentDefinitionDto` {#schema-publicstaticdomaincontentdefinitiondto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`STATIC`, `DYNAMIC`) | yes | Type of the domain content definition |
| `assets` | array<string> | no | List of the assets of the domain |


### `PublicDynamicDomainContentDefinitionDto` {#schema-publicdynamicdomaincontentdefinitiondto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`STATIC`, `DYNAMIC`) | yes | Type of the domain content definition |
| `conditions` | array<[`PublicSourceFilterDomainConditionDto`](#schema-publicsourcefilterdomainconditiondto) or [`PublicTagFilterDomainConditionDto`](#schema-publictagfilterdomainconditiondto)> | no | List of the conditions defining content of the domain |
| `filterLogicalOperator` | enum (`AND`, `OR`) | no | Logical operator to use between conditions |


### `PublicGetDomainDto` {#schema-publicgetdomaindto}

| Name | Type | Required | Description |
|---|---|---|---|
| `assetContentDefinition` | [`PublicDynamicDomainContentDefinitionDto`](#schema-publicdynamicdomaincontentdefinitiondto) or [`PublicStaticDomainContentDefinitionDto`](#schema-publicstaticdomaincontentdefinitiondto) | yes |  |
| `assetCount` | integer (int32) | yes | Current count of assets contained in the domain |
| `description` | string | no | Description of the domain |
| `id` | string (uuid) | yes |  |
| `name` | string | yes | Name of the domain |
| `parentDomainId` | string (uuid) | no | Id of the parent domain, if the domain has a parent |
| `teamPermissions` | array<[`PublicDomainTeamPermissionDto`](#schema-publicdomainteampermissiondto)> | no | Teams permissions granted in the domain |


### `PublicSourceFilterDomainConditionDto` {#schema-publicsourcefilterdomainconditiondto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`SOURCE`, `TAG`) | yes | Type of the condition |
| `operator` | enum (`IS`, `IS_NOT`) | no | Operator of the condition |
| `sources` | array<string> | no | List of the sources in the condition in URI format. <a href="https://docs.siffletdata.com/docs/uri">[Read more about URIs]</a> |


### `PublicTagFilterDomainConditionDto` {#schema-publictagfilterdomainconditiondto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`SOURCE`, `TAG`) | yes | Type of the condition |
| `operator` | enum (`IS`, `IS_NOT`) | no | Operator of the condition |
| `tags` | array<[`PublicExternalTagReferenceDto`](#schema-publicexternaltagreferencedto)> | no | List of the tags references in the condition |


### `PublicDomainTeamPermissionDto` {#schema-publicdomainteampermissiondto}

Teams permissions granted in the domain

| Name | Type | Required | Description |
|---|---|---|---|
| `domainRole` | enum (`EDITOR`, `MONITOR_RESPONDER`, `CATALOG_EDITOR`, `VIEWER`) | yes | Domain role assigned to the referenced team for accessing domain |
| `teamId` | string (uuid) | yes | Id of the team |


### `PublicExternalTagReferenceDto` {#schema-publicexternaltagreferencedto}

Asset tag from external providers.

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | Id of the referenced object |
| `kind` | enum (`BIGQUERY_EXTERNAL`, `SNOWFLAKE_EXTERNAL`, `DBT_EXTERNAL`, `DATABRICKS_EXTERNAL`, `ADF_EXTERNAL`, `ATLAN_EXTERNAL`, `ALATION_EXTERNAL`, `AMUNDSEN_EXTERNAL`, `APACHE_ATLAS_EXTERNAL`, `CASTOR_DOC_EXTERNAL`, `COLLIBRA_EXTERNAL`, `DATAGALAXY_EXTERNAL`, … 4 more — full list in `openapi.json`) | no | Type of the referenced tag |
| `name` | string | no | Name of the referenced object |

