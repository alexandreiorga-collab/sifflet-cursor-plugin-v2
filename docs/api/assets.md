# Assets

Search, read, and edit catalog assets.

[← Back to API index](README.md)

## `PATCH /v1/assets`

**Edit an asset**

- **operationId**: `publicEditAsset`

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `columns` | array<[`PublicUpdateAssetColumnDto`](#schema-publicupdateassetcolumndto)> | no | Fields of the asset |
| `customMetadataValues` | array<[`PublicCustomMetadataEntryLabelReferenceDto`](#schema-publiccustommetadataentrylabelreferencedto) or [`PublicCustomMetadataEntryStringReferenceDto`](#schema-publiccustommetadataentrystringreferencedto) or [`PublicCustomMetadataEntryTeamReferenceDto`](#schema-publiccustommetadataentryteamreferencedto) or [`PublicCustomMetadataEntryUserReferenceDto`](#schema-publiccustommetadataentryuserreferencedto)> | no | Custom metadata entries of the asset |
| `description` | string | no | Description of the asset |
| `owners` | array<[`PublicReferenceByIdOrEmailDto`](#schema-publicreferencebyidoremaildto)> | no | Owners of the asset |
| `tags` | array<[`PublicTagReferenceDto`](#schema-publictagreferencedto)> | no |  |
| `terms` | array<[`PublicReferenceByIdOrNameDto`](#schema-publicreferencebyidornamedto)> | no | Terms of the asset |
| `uri` | string | yes | URI string identifying the asset. <a href="https://docs.siffletdata.com/docs/uri">[Read more about URIs]</a> |

**Response**

- `200` — Asset edited: [`PublicGetAssetDto`](#schema-publicgetassetdto)

**Example call**

```bash
curl -X PATCH \
  "https://{tenant}.siffletdata.com/api/v1/assets" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "uri": "string"
}'
```

Example `200` response:

```json
{
  "name": "string",
  "usage": "UNSUPPORTED",
  "uri": "string",
  "technology": "ATHENA",
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "healthStatus": "URGENT_INCIDENTS",
  "type": "CONNECTOR",
  "ingestionMethod": "DECLARATIVE",
  "urn": "string",
  "domains": [
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
| `400` | Bad request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Resource not found |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `POST /v1/assets/get-asset-with-uri`

**Get asset by uri**

- **operationId**: `publicGetAsset`

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `uri` | string | yes | URI string identifying the asset. <a href="https://docs.siffletdata.com/docs/uri">[Read more about URIs]</a> |

**Response**

- `200` — Asset retrieved: [`PublicGetAssetDto`](#schema-publicgetassetdto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v1/assets/get-asset-with-uri" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "uri": "string"
}'
```

Example `200` response:

```json
{
  "name": "string",
  "usage": "UNSUPPORTED",
  "uri": "string",
  "technology": "ATHENA",
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "healthStatus": "URGENT_INCIDENTS",
  "type": "CONNECTOR",
  "ingestionMethod": "DECLARATIVE",
  "urn": "string",
  "domains": [
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
| `400` | Bad request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Resource not found |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `POST /v1/assets/search`

**Get search results for assets**

- **operationId**: `publicGetAssets`

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `filter` | [`PublicAssetFilterDto`](#schema-publicassetfilterdto) | no | Filter to apply on the assets search |
| `pagination` | [`PublicAssetPaginationDto`](#schema-publicassetpaginationdto) | no | Pagination to apply on the assets search |
| `sort` | array<string (property,ASC\|DESC)> | no | Sort to apply on the assets search. Possible values for field are 'name' and 'relevance' |

**Response**

- `200` — Assets retrieved: [`PublicPageDtoPublicGetAssetListDto`](#schema-publicpagedtopublicgetassetlistdto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v1/assets/search" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "filter": {
    "assetType": [
      "string"
    ],
    "customMetadataValues": [
      "..."
    ],
    "domainId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "externalTerms": [
      {
        "id": "02a15477-1e58-490e-aa5c-1c7388fcb136",
        "name": "Product",
        "kind": "ATLAN_EXTERNAL"
      }
    ]
  },
  "pagination": {
    "itemsPerPage": 0,
    "page": 0
  },
  "sort": [
    {
      "direction": "ASC",
      "field": "name"
    }
  ]
}'
```

Example `200` response:

```json
{
  "data": [
    {
      "name": "string",
      "usage": "UNSUPPORTED",
      "uri": "string",
      "technology": "ATHENA",
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "healthStatus": "URGENT_INCIDENTS",
      "type": "CONNECTOR",
      "ingestionMethod": "DECLARATIVE",
      "urn": "string"
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
| `404` | Resource not found |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## Referenced object schemas

### `PublicAssetPaginationDto` {#schema-publicassetpaginationdto}

Pagination to apply on the assets search

| Name | Type | Required | Description |
|---|---|---|---|
| `itemsPerPage` | integer (int32) | no | Number of items per page. Value -1 returns all items. |
| `page` | integer (int32) | no | Page number. Default value returns first page. |


### `PublicAssetFilterDto` {#schema-publicassetfilterdto}

Filter to apply on the assets search

| Name | Type | Required | Description |
|---|---|---|---|
| `assetType` | array<string> | no | List of asset types to filter on. Valid values are TABLE_AND_VIEW, PIPELINE, DASHBOARD, ML_MODEL. For filtering declared assets with custom types, you can use the format declared-asset_{custom sub type}. For example: declared-asset_Storage |
| `customMetadataValues` | array<[`PublicCustomMetadataEntryLabelReferenceDto`](#schema-publiccustommetadataentrylabelreferencedto) or [`PublicCustomMetadataEntryStringReferenceDto`](#schema-publiccustommetadataentrystringreferencedto) or [`PublicCustomMetadataEntryTeamReferenceDto`](#schema-publiccustommetadataentryteamreferencedto) or [`PublicCustomMetadataEntryUserReferenceDto`](#schema-publiccustommetadataentryuserreferencedto)> | no | List of custom metadata values to filter on |
| `domainId` | string (uuid) | no | Domain to search on |
| `externalTerms` | array<[`PublicExternalTermReferenceDto`](#schema-publicexternaltermreferencedto)> | no | List of external business terms to filter on |
| `healthStatus` | array<enum (`URGENT_INCIDENTS`, `HIGH_RISK_INCIDENTS`, `NO_INCIDENTS`, `NOT_MONITORED`, `UNSUPPORTED`)> | no | List of health status to filter on |
| `ingestionMethod` | array<enum (`DECLARATIVE`, `SIFFLET_SOURCED`)> | no | List of ingestion methods to filter on |
| `levelOfUsage` | array<enum (`UNSUPPORTED`, `LOW`, `MEDIUM`, `HIGH`)> | no | List of usage qualifications to filter on |
| `owners` | array<[`PublicReferenceByIdOrEmailDto`](#schema-publicreferencebyidoremaildto)> | no | List of owners to filter on |
| `sourceId` | array<string (uuid)> | no | List of subSources to filter on by id. You should prefer using `subSourceUri` filter, and `subSourceUri` filter will be considered in priority if both of those filters are used. |
| `subSourceUri` | array<string> | no | List of subSources to filter on by subSource uri. SubSources uri for a given source can be fetched using <a href="https://docs.siffletdata.com/reference/publicgetsourceschemalist">[the list sub-sources endpoint]</a> |
| `tags` | array<[`PublicTagReferenceDto`](#schema-publictagreferencedto)> | no | List of tags to filter on |
| `terms` | array<[`PublicReferenceByIdOrNameDto`](#schema-publicreferencebyidornamedto)> | no | List of business terms to filter on |
| `textSearch` | string | no | Text to match in the asset names |


### `PublicCustomMetadataEntryTeamReferenceDto` {#schema-publiccustommetadataentryteamreferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `customMetadataName` | string | yes | Name of the referenced custom metadata |
| `type` | enum (`LABEL`, `STRING`, `USER`, `TEAM`) | yes |  |
| `name` | string | no | Value of the referenced custom metadata team name |


### `PublicPageDtoPublicGetAssetListDto` {#schema-publicpagedtopublicgetassetlistdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `data` | array<[`PublicGetAssetListDto`](#schema-publicgetassetlistdto)> | yes |  |
| `totalCount` | integer (int64) | no |  |


### `PublicReferenceByIdOrNameDto` {#schema-publicreferencebyidornamedto}

Id or name reference to an object

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | Id of the referenced object |
| `name` | string | no | Name of the referenced object |


### `PublicCustomMetadataEntryLabelReferenceDto` {#schema-publiccustommetadataentrylabelreferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `customMetadataName` | string | yes | Name of the referenced custom metadata |
| `type` | enum (`LABEL`, `STRING`, `USER`, `TEAM`) | yes |  |
| `labelValue` | string | no | Value of the referenced custom metadata label |


### `PublicCustomMetadataEntryStringReferenceDto` {#schema-publiccustommetadataentrystringreferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `customMetadataName` | string | yes | Name of the referenced custom metadata |
| `type` | enum (`LABEL`, `STRING`, `USER`, `TEAM`) | yes |  |
| `stringValue` | string | no | Value of the referenced custom metadata string |


### `PublicTagReferenceDto` {#schema-publictagreferencedto}

Tags of the source. A tag can either be referenced by its id or its name or its name and kind.

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | Id of the referenced object |
| `kind` | enum (`TAG`, `CLASSIFICATION`) | no | Type of the referenced tag |
| `name` | string | no | Name of the referenced object |


### `PublicReferenceByIdOrEmailDto` {#schema-publicreferencebyidoremaildto}

Id or email reference to an owner

| Name | Type | Required | Description |
|---|---|---|---|
| `email` | string | no | Email of the referenced owner |
| `id` | string (uuid) | no | Id of the referenced owner |


### `PublicGetAssetDto` {#schema-publicgetassetdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `columns` | array<[`PublicGetAssetColumnDto`](#schema-publicgetassetcolumndto)> | no | Fields of the asset |
| `customMetadataValues` | array<[`PublicGetCustomMetadataEntryLabelDto`](#schema-publicgetcustommetadataentrylabeldto) or [`PublicGetCustomMetadataEntryStringDto`](#schema-publicgetcustommetadataentrystringdto) or [`PublicGetCustomMetadataEntryTeamDto`](#schema-publicgetcustommetadataentryteamdto) or [`PublicGetCustomMetadataEntryUserDto`](#schema-publicgetcustommetadataentryuserdto)> | no | Custom metadata values of the asset |
| `description` | string | no | Description of the asset |
| `domains` | array<[`PublicDomainGetDto`](#schema-publicdomaingetdto)> | yes | Domains of the asset |
| `externalDescriptions` | array<[`PublicDescriptionDto`](#schema-publicdescriptiondto)> | no | Descriptions of the asset from external providers |
| `externalTags` | array<[`PublicExternalTagReferenceDto`](#schema-publicexternaltagreferencedto)> | no | Asset tags from external providers |
| `externalTerms` | array<[`PublicExternalTermReferenceDto`](#schema-publicexternaltermreferencedto)> | no | Business terms from external providers |
| `healthStatus` | enum (`URGENT_INCIDENTS`, `HIGH_RISK_INCIDENTS`, `NO_INCIDENTS`, `NOT_MONITORED`, `UNSUPPORTED`) | yes | Asset health status |
| `id` | string (uuid) | yes |  |
| `ingestionMethod` | enum (`DECLARATIVE`, `SIFFLET_SOURCED`) | yes | Ingestion method of the asset |
| `name` | string | yes | Name of the asset |
| `owners` | array<[`PublicReferenceByIdOrEmailDto`](#schema-publicreferencebyidoremaildto)> | no | Owners of the asset |
| `tags` | array<[`PublicTagReferenceDto`](#schema-publictagreferencedto)> | no | Tags of the asset |
| `technology` | enum (`ATHENA`, `BIGQUERY`, `FIREBOLT`, `PRESTO`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `ADF`, `MSSQL`, `MYSQL`, `SYNAPSE`, … 449 more — full list in `openapi.json`) | yes | Technology of the asset |
| `terms` | array<[`PublicReferenceByIdOrNameDto`](#schema-publicreferencebyidornamedto)> | no | Business terms of the asset |
| `transformationRun` | [`PublicTransformationRunDto`](#schema-publictransformationrundto) | no | Transformation associated to the asset |
| `type` | enum (`CONNECTOR`, `DAG`, `DASHBOARD`, `EXTERNAL_TABLE`, `MATERIALIZED_VIEW`, `ML_MODEL`, `MODEL`, `ORCHESTRATOR`, `OTHER`, `PIPELINE`, `REPORT`, `SNOWFLAKE_STREAM`, … 3 more — full list in `openapi.json`) | yes | Type of the asset |
| `uri` | string | yes | URI string identifying the asset. <a href="https://docs.siffletdata.com/docs/uri">[Read more about URIs]</a> |
| `urn` | string | yes | Internal Sifflet identifier for the asset |
| `usage` | enum (`UNSUPPORTED`, `LOW`, `MEDIUM`, `HIGH`) | yes | Usage level of the asset |


### `PublicCustomMetadataEntryUserReferenceDto` {#schema-publiccustommetadataentryuserreferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `customMetadataName` | string | yes | Name of the referenced custom metadata |
| `type` | enum (`LABEL`, `STRING`, `USER`, `TEAM`) | yes |  |
| `email` | string | no | Value of the referenced custom metadata user email |


### `PublicUpdateAssetColumnDto` {#schema-publicupdateassetcolumndto}

Fields of the asset

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no | Description of the field |
| `name` | string | yes | Name of the field |
| `tags` | array<[`PublicTagReferenceDto`](#schema-publictagreferencedto)> | no | Tags of the field |
| `terms` | array<[`PublicReferenceByIdOrNameDto`](#schema-publicreferencebyidornamedto)> | no | Terms of the field |


### `PublicExternalTermReferenceDto` {#schema-publicexternaltermreferencedto}

Asset business glossary from external providers.

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | Id of the referenced object |
| `kind` | enum (`ATLAN_EXTERNAL`, `ALATION_EXTERNAL`, `AMUNDSEN_EXTERNAL`, `APACHE_ATLAS_EXTERNAL`, `CASTOR_DOC_EXTERNAL`, `COLLIBRA_EXTERNAL`, `DATAGALAXY_EXTERNAL`, `INFORMATICA_EXTERNAL`, `SECODA_EXTERNAL`, `SELECT_STAR_EXTERNAL`, `GENERIC_CATALOG_EXTERNAL`) | no | Type of the referenced tag |
| `name` | string | no | Name of the referenced object |


### `PublicGetAssetListDto` {#schema-publicgetassetlistdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no | Description of the asset |
| `externalDescriptions` | array<[`PublicDescriptionDto`](#schema-publicdescriptiondto)> | no | Descriptions of the asset from external providers |
| `externalTags` | array<[`PublicExternalTagReferenceDto`](#schema-publicexternaltagreferencedto)> | no | Asset tags from external providers |
| `externalTerms` | array<[`PublicExternalTermReferenceDto`](#schema-publicexternaltermreferencedto)> | no | Business terms from external providers |
| `healthStatus` | enum (`URGENT_INCIDENTS`, `HIGH_RISK_INCIDENTS`, `NO_INCIDENTS`, `NOT_MONITORED`, `UNSUPPORTED`) | yes | Asset health status |
| `id` | string (uuid) | yes |  |
| `ingestionMethod` | enum (`DECLARATIVE`, `SIFFLET_SOURCED`) | yes | Ingestion method of the asset |
| `name` | string | yes | Name of the asset |
| `owners` | array<[`PublicReferenceByIdOrEmailDto`](#schema-publicreferencebyidoremaildto)> | no | Owners of the asset |
| `tags` | array<[`PublicTagReferenceDto`](#schema-publictagreferencedto)> | no | Tags of the asset |
| `technology` | enum (`ATHENA`, `BIGQUERY`, `FIREBOLT`, `PRESTO`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `ADF`, `MSSQL`, `MYSQL`, `SYNAPSE`, … 449 more — full list in `openapi.json`) | yes | Technology of the asset |
| `terms` | array<[`PublicReferenceByIdOrNameDto`](#schema-publicreferencebyidornamedto)> | no | Business terms of the asset |
| `transformationRun` | [`PublicTransformationRunDto`](#schema-publictransformationrundto) | no | Transformation associated to the asset |
| `type` | enum (`CONNECTOR`, `DAG`, `DASHBOARD`, `EXTERNAL_TABLE`, `MATERIALIZED_VIEW`, `ML_MODEL`, `MODEL`, `ORCHESTRATOR`, `OTHER`, `PIPELINE`, `REPORT`, `SNOWFLAKE_STREAM`, … 3 more — full list in `openapi.json`) | yes | Type of the asset |
| `uri` | string | yes | URI string identifying the asset. <a href="https://docs.siffletdata.com/docs/uri">[Read more about URIs]</a> |
| `urn` | string | yes | Internal Sifflet identifier for the asset |
| `usage` | enum (`UNSUPPORTED`, `LOW`, `MEDIUM`, `HIGH`) | yes | Usage level of the asset |


### `PublicDescriptionDto` {#schema-publicdescriptiondto}

Descriptions of the asset from external providers

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no |  |
| `origin` | enum (`ATHENA`, `BIGQUERY`, `FIREBOLT`, `PRESTO`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `ADF`, `MSSQL`, `MYSQL`, `SYNAPSE`, … 449 more — full list in `openapi.json`) | no |  |


### `PublicGetCustomMetadataEntryUserDto` {#schema-publicgetcustommetadataentryuserdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `customMetadataName` | string | yes | Name of the referenced custom metadata |
| `type` | enum (`LABEL`, `STRING`, `USER`, `TEAM`) | yes |  |
| `email` | string | no |  |


### `PublicGetCustomMetadataEntryTeamDto` {#schema-publicgetcustommetadataentryteamdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `customMetadataName` | string | yes | Name of the referenced custom metadata |
| `type` | enum (`LABEL`, `STRING`, `USER`, `TEAM`) | yes |  |
| `name` | string | no |  |


### `PublicGetAssetColumnDto` {#schema-publicgetassetcolumndto}

Fields of the asset

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no | Description of the field |
| `externalDescriptions` | array<[`PublicDescriptionDto`](#schema-publicdescriptiondto)> | no | Descriptions of the field from external providers |
| `externalTags` | array<[`PublicExternalTagReferenceDto`](#schema-publicexternaltagreferencedto)> | no | Asset tags from external providers |
| `id` | string (uuid) | yes |  |
| `name` | string | yes | Name of the field |
| `tags` | array<[`PublicTagReferenceDto`](#schema-publictagreferencedto)> | no | Tags of the column |
| `terms` | array<[`PublicReferenceByIdOrNameDto`](#schema-publicreferencebyidornamedto)> | no | Business glossaries of the field |
| `type` | string | yes | Type of the field |


### `PublicDomainGetDto` {#schema-publicdomaingetdto}

Domains of the asset

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | yes |  |
| `name` | string | yes |  |


### `PublicTransformationRunDto` {#schema-publictransformationrundto}

Transformation associated to the asset

| Name | Type | Required | Description |
|---|---|---|---|
| `lastRunDate` | integer (int64) | no | Last run date of the transformation |
| `lastRunStatus` | enum (`SUCCESS`, `ERROR`, `SKIPPED`, `PARTIAL_SUCCESS`, `NOT_TARGETED`, `UNKNOWN`) | no | Last run status of the transformation |
| `type` | string | no | Type of the transformation |


### `PublicGetCustomMetadataEntryStringDto` {#schema-publicgetcustommetadataentrystringdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `customMetadataName` | string | yes | Name of the referenced custom metadata |
| `type` | enum (`LABEL`, `STRING`, `USER`, `TEAM`) | yes |  |
| `stringValue` | string | no |  |


### `PublicExternalTagReferenceDto` {#schema-publicexternaltagreferencedto}

Asset tag from external providers.

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | Id of the referenced object |
| `kind` | enum (`BIGQUERY_EXTERNAL`, `SNOWFLAKE_EXTERNAL`, `DBT_EXTERNAL`, `DATABRICKS_EXTERNAL`, `ADF_EXTERNAL`, `ATLAN_EXTERNAL`, `ALATION_EXTERNAL`, `AMUNDSEN_EXTERNAL`, `APACHE_ATLAS_EXTERNAL`, `CASTOR_DOC_EXTERNAL`, `COLLIBRA_EXTERNAL`, `DATAGALAXY_EXTERNAL`, … 4 more — full list in `openapi.json`) | no | Type of the referenced tag |
| `name` | string | no | Name of the referenced object |


### `PublicGetCustomMetadataEntryLabelDto` {#schema-publicgetcustommetadataentrylabeldto}

| Name | Type | Required | Description |
|---|---|---|---|
| `customMetadataName` | string | yes | Name of the referenced custom metadata |
| `type` | enum (`LABEL`, `STRING`, `USER`, `TEAM`) | yes |  |
| `labelValue` | string | no |  |

