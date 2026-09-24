# Sources (v1, deprecated)

Deprecated data-source management. Use Sources (v2) for new integrations.

[← Back to API index](README.md)

## `POST /v1/sources`

**Create a source** — This endpoint is deprecated and will be removed soon. Please use the Sources V2 endpoint instead - POST /api/v2/sources.

- **operationId**: `publicCreateSource`
- **Status**: ⚠️ deprecated

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `credentials` | string | no | Credentials of the source. Required for all sources type except 'ATHENA', 'DBT', 'QUICKSIGHT'. |
| `description` | string | no | Description of the source |
| `name` | string | yes | Name of the source |
| `parameters` | [`PublicAirflowParametersDto`](#schema-publicairflowparametersdto) or [`PublicAthenaParametersDto`](#schema-publicathenaparametersdto) or [`PublicBigQueryParametersDto`](#schema-publicbigqueryparametersdto) or [`PublicDatabricksParametersDto`](#schema-publicdatabricksparametersdto) or [`PublicDbtCloudParametersDto`](#schema-publicdbtcloudparametersdto) or [`PublicDbtParametersDto`](#schema-publicdbtparametersdto) or [`PublicDeclarativeParametersDto`](#schema-publicdeclarativeparametersdto) or [`PublicFivetranParametersDto`](#schema-publicfivetranparametersdto) or [`PublicLookerParametersDto`](#schema-publiclookerparametersdto) or [`PublicMssqlParametersDto`](#schema-publicmssqlparametersdto) or [`PublicMysqlParametersDto`](#schema-publicmysqlparametersdto) or [`PublicOracleParametersDto`](#schema-publicoracleparametersdto) or [`PublicPostgresqlParametersDto`](#schema-publicpostgresqlparametersdto) or [`PublicPowerBiParametersDto`](#schema-publicpowerbiparametersdto) or [`PublicQuicksightParametersDto`](#schema-publicquicksightparametersdto) or [`PublicRedshiftParametersDto`](#schema-publicredshiftparametersdto) or [`PublicSnowflakeParametersDto`](#schema-publicsnowflakeparametersdto) or [`PublicSynapseParametersDto`](#schema-publicsynapseparametersdto) or [`PublicTableauParametersDto`](#schema-publictableauparametersdto) | yes |  |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |
| `tags` | array<[`PublicTagReferenceDto`](#schema-publictagreferencedto)> | no |  |
| `timezone` | string | no | A string representing a timezone identifier (e.g. 'UTC' or 'Europe/Paris') |

**Response**

- `201` — Source created: [`PublicGetSourceDto`](#schema-publicgetsourcedto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v1/sources" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "parameters": {},
  "name": "string"
}'
```

Example `201` response:

```json
{
  "parameters": {},
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

## `POST /v1/sources/search`

**Get search results for sources** — This endpoint is deprecated and will be removed soon. Please use the Sources V2 endpoint instead - GET /api/v2/sources.

- **operationId**: `publicGetSources`
- **Status**: ⚠️ deprecated

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `filter` | [`PublicSourceFilterDto`](#schema-publicsourcefilterdto) | no | Filter to apply on the sources search |
| `pagination` | [`PublicSourcePaginationDto`](#schema-publicsourcepaginationdto) | no | Pagination to apply on the sources search |
| `sort` | array<string (property,ASC\|DESC)> | no | Sort to apply on the sources search |

**Response**

- `200` — Sources retrieved: [`PublicPageDtoPublicGetSourceDto`](#schema-publicpagedtopublicgetsourcedto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v1/sources/search" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "filter": {
    "tags": [
      [
        {
          "id": "02a15477-1e58-490e-aa5c-1c7388fcb136",
          "name": "PII",
          "kind": "CLASSIFICATION"
        },
        {
          "name": "tag-name"
        },
        {
          "name": "PII",
          "kind": "CLASSIFICATION"
        }
      ]
    ],
    "textSearch": "string",
    "types": [
      "ATHENA"
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
      "parameters": "...",
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

## `POST /v1/sources/test-connection`

**Test connection with given source params** — This endpoint is deprecated and will be removed soon. Please use the Sources V2 endpoint instead

- **operationId**: `testSourceConnection`
- **Status**: ⚠️ deprecated

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `credentials` | string | no | Credentials of the source. Required for all sources type except 'ATHENA', 'DBT', 'QUICKSIGHT'. |
| `description` | string | no | Description of the source |
| `name` | string | yes | Name of the source |
| `parameters` | [`PublicAirflowParametersDto`](#schema-publicairflowparametersdto) or [`PublicAthenaParametersDto`](#schema-publicathenaparametersdto) or [`PublicBigQueryParametersDto`](#schema-publicbigqueryparametersdto) or [`PublicDatabricksParametersDto`](#schema-publicdatabricksparametersdto) or [`PublicDbtCloudParametersDto`](#schema-publicdbtcloudparametersdto) or [`PublicDbtParametersDto`](#schema-publicdbtparametersdto) or [`PublicDeclarativeParametersDto`](#schema-publicdeclarativeparametersdto) or [`PublicFivetranParametersDto`](#schema-publicfivetranparametersdto) or [`PublicLookerParametersDto`](#schema-publiclookerparametersdto) or [`PublicMssqlParametersDto`](#schema-publicmssqlparametersdto) or [`PublicMysqlParametersDto`](#schema-publicmysqlparametersdto) or [`PublicOracleParametersDto`](#schema-publicoracleparametersdto) or [`PublicPostgresqlParametersDto`](#schema-publicpostgresqlparametersdto) or [`PublicPowerBiParametersDto`](#schema-publicpowerbiparametersdto) or [`PublicQuicksightParametersDto`](#schema-publicquicksightparametersdto) or [`PublicRedshiftParametersDto`](#schema-publicredshiftparametersdto) or [`PublicSnowflakeParametersDto`](#schema-publicsnowflakeparametersdto) or [`PublicSynapseParametersDto`](#schema-publicsynapseparametersdto) or [`PublicTableauParametersDto`](#schema-publictableauparametersdto) | yes |  |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |
| `tags` | array<[`PublicTagReferenceDto`](#schema-publictagreferencedto)> | no |  |
| `timezone` | string | no | A string representing a timezone identifier (e.g. 'UTC' or 'Europe/Paris') |

**Response**

- `204` — Connection test result (no body)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v1/sources/test-connection" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "parameters": {},
  "name": "string"
}'
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

## `DELETE /v1/sources/{id}`

**Delete a source by id** — This endpoint is deprecated and will be removed soon. Please use the Sources V2 endpoint instead - DELETE /api/v2/sources/{id}.

- **operationId**: `publicDeleteSourceById`
- **Status**: ⚠️ deprecated

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `204` — Source deleted (no body)

**Example call**

```bash
curl -X DELETE \
  "https://{tenant}.siffletdata.com/api/v1/sources/{id}" \
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

## `GET /v1/sources/{id}`

**Get a source by id** — This endpoint is deprecated and will be removed soon. Please use one of the Sources V2 endpoints instead - GET /api/v2/sources/ or GET /api/v2/sources/{id}.

- **operationId**: `publicGetSource`
- **Status**: ⚠️ deprecated

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `200` — Source retrieved: [`PublicGetSourceDto`](#schema-publicgetsourcedto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/sources/{id}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "parameters": {},
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

## `PATCH /v1/sources/{id}`

**Edit a source** — This endpoint is deprecated and will be removed soon. Please use the Sources V2 endpoint instead - PATCH /api/v2/sources/{id}.

- **operationId**: `publicEditSource`
- **Status**: ⚠️ deprecated

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `credentials` | string | no | Credentials of the source. Required for all sources type except 'ATHENA', 'DBT', 'QUICKSIGHT'. |
| `description` | string | no | Description of the source |
| `name` | string | no | Name of the source |
| `parameters` | [`PublicAirflowParametersDto`](#schema-publicairflowparametersdto) or [`PublicAthenaParametersDto`](#schema-publicathenaparametersdto) or [`PublicBigQueryParametersDto`](#schema-publicbigqueryparametersdto) or [`PublicDatabricksParametersDto`](#schema-publicdatabricksparametersdto) or [`PublicDbtCloudParametersDto`](#schema-publicdbtcloudparametersdto) or [`PublicDbtParametersDto`](#schema-publicdbtparametersdto) or [`PublicDeclarativeParametersDto`](#schema-publicdeclarativeparametersdto) or [`PublicFivetranParametersDto`](#schema-publicfivetranparametersdto) or [`PublicLookerParametersDto`](#schema-publiclookerparametersdto) or [`PublicMssqlParametersDto`](#schema-publicmssqlparametersdto) or [`PublicMysqlParametersDto`](#schema-publicmysqlparametersdto) or [`PublicOracleParametersDto`](#schema-publicoracleparametersdto) or [`PublicPostgresqlParametersDto`](#schema-publicpostgresqlparametersdto) or [`PublicPowerBiParametersDto`](#schema-publicpowerbiparametersdto) or [`PublicQuicksightParametersDto`](#schema-publicquicksightparametersdto) or [`PublicRedshiftParametersDto`](#schema-publicredshiftparametersdto) or [`PublicSnowflakeParametersDto`](#schema-publicsnowflakeparametersdto) or [`PublicSynapseParametersDto`](#schema-publicsynapseparametersdto) or [`PublicTableauParametersDto`](#schema-publictableauparametersdto) | no |  |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |
| `tags` | array<[`PublicTagReferenceDto`](#schema-publictagreferencedto)> | no |  |
| `timezone` | string | no | A string representing a timezone identifier (e.g. 'UTC' or 'Europe/Paris') |

**Response**

- `200` — Source edited: [`PublicGetSourceDto`](#schema-publicgetsourcedto)

**Example call**

```bash
curl -X PATCH \
  "https://{tenant}.siffletdata.com/api/v1/sources/{id}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "credentials": "string",
  "description": "string",
  "name": "string",
  "parameters": {}
}'
```

Example `200` response:

```json
{
  "parameters": {},
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

## `POST /v1/sources/{id}/run`

**Manually trigger a source metadata ingestion job** — This endpoint is deprecated and will be removed soon. Please use the Sources V2 endpoint instead - POST /api/v2/sources/run-subsource.

- **operationId**: `publicSourceIngestionManualRun`
- **Status**: ⚠️ deprecated

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `204` — Job triggered (no body)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v1/sources/{id}/run" \
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

## Referenced object schemas

### `PublicPostgresqlParametersDto` {#schema-publicpostgresqlparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `database` | string | no | Your database name |
| `host` | string | no | Your PostgreSQL server host |
| `port` | integer (int32) | no | Your PostgreSQL server port |
| `schema` | string | no | Your schema name |


### `PublicTableauParametersDto` {#schema-publictableauparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `host` | string | no | Your Tableau Server hostname |
| `site` | string | no | Your Tableau Server site. Leave empty if your Tableau environment is using the Default Site. |


### `PublicGetSourceDto` {#schema-publicgetsourcedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `credentials` | string | no | Credentials of the source |
| `description` | string | no | Description of the source |
| `id` | string (uuid) | yes |  |
| `lastRun` | [`PublicGetLastRunDto`](#schema-publicgetlastrundto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `parameters` | [`PublicAirflowParametersDto`](#schema-publicairflowparametersdto) or [`PublicAthenaParametersDto`](#schema-publicathenaparametersdto) or [`PublicBigQueryParametersDto`](#schema-publicbigqueryparametersdto) or [`PublicDatabricksParametersDto`](#schema-publicdatabricksparametersdto) or [`PublicDbtCloudParametersDto`](#schema-publicdbtcloudparametersdto) or [`PublicDbtParametersDto`](#schema-publicdbtparametersdto) or [`PublicDeclarativeParametersDto`](#schema-publicdeclarativeparametersdto) or [`PublicFivetranParametersDto`](#schema-publicfivetranparametersdto) or [`PublicLookerParametersDto`](#schema-publiclookerparametersdto) or [`PublicMssqlParametersDto`](#schema-publicmssqlparametersdto) or [`PublicMysqlParametersDto`](#schema-publicmysqlparametersdto) or [`PublicOracleParametersDto`](#schema-publicoracleparametersdto) or [`PublicPostgresqlParametersDto`](#schema-publicpostgresqlparametersdto) or [`PublicPowerBiParametersDto`](#schema-publicpowerbiparametersdto) or [`PublicQuicksightParametersDto`](#schema-publicquicksightparametersdto) or [`PublicRedshiftParametersDto`](#schema-publicredshiftparametersdto) or [`PublicSnowflakeParametersDto`](#schema-publicsnowflakeparametersdto) or [`PublicSynapseParametersDto`](#schema-publicsynapseparametersdto) or [`PublicTableauParametersDto`](#schema-publictableauparametersdto) | yes |  |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |
| `tags` | array<[`PublicTagReferenceDto`](#schema-publictagreferencedto)> | no | Tags of the source |
| `timezone` | string | no | A string representing a timezone identifier (e.g. 'UTC' or 'Europe/Paris') |


### `PublicDatabricksParametersDto` {#schema-publicdatabricksparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `catalog` | string | no | Your Databricks catalog |
| `host` | string | no | Your Databricks server hostname |
| `httpPath` | string | no | Your Databricks HTTP path |
| `port` | integer (int32) | no | Your Databricks server port |
| `schema` | string | no | Your Databricks schema |


### `PublicSynapseParametersDto` {#schema-publicsynapseparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `database` | string | no | Your database name |
| `host` | string | no | The host of your Synapse server |
| `port` | integer (int32) | no | Your Synapse server port |
| `schema` | string | no | Your schema name |


### `PublicBigQueryParametersDto` {#schema-publicbigqueryparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `billingProjectId` | string | no | Your billing project ID |
| `datasetId` | string | no | Your BigQuery dataset ID |
| `projectId` | string | no | Your BigQuery project ID |
| `workerProjectIds` | string | no | Comma separated list of project ids where your queries run. Optional if it's the same as the projectId parameter |


### `PublicSourcePaginationDto` {#schema-publicsourcepaginationdto}

Pagination to apply on the sources search

| Name | Type | Required | Description |
|---|---|---|---|
| `itemsPerPage` | integer (int32) | no | Default value returns all items. |
| `page` | integer (int32) | no |  |


### `PublicMssqlParametersDto` {#schema-publicmssqlparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `database` | string | no | Your database name |
| `host` | string | no | Your MSSQL server hostname |
| `port` | integer (int32) | no | Your MSSQL server port |
| `schema` | string | no | Your schema name |
| `ssl` | boolean | no | Whether to use SSL to connect to your MSSQL server (recommended: true) |


### `PublicPageDtoPublicGetSourceDto` {#schema-publicpagedtopublicgetsourcedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `data` | array<[`PublicGetSourceDto`](#schema-publicgetsourcedto)> | yes |  |
| `totalCount` | integer (int64) | no |  |


### `PublicPowerBiParametersDto` {#schema-publicpowerbiparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `clientId` | string | no | Your Azure AD client ID |
| `tenantId` | string | no | Your Azure AD tenant ID |
| `workspaceId` | string | no | Your Power BI workspace ID |


### `PublicDbtParametersDto` {#schema-publicdbtparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `projectName` | string | no | Your dbt project name (the 'name' value in your dbt_project.yml file) |
| `target` | string | no | Your dbt target name (the 'target' value in your profiles.yml file) |


### `PublicTagReferenceDto` {#schema-publictagreferencedto}

Tags of the source. A tag can either be referenced by its id or its name or its name and kind.

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | Id of the referenced object |
| `kind` | enum (`TAG`, `CLASSIFICATION`) | no | Type of the referenced tag |
| `name` | string | no | Name of the referenced object |


### `PublicMysqlParametersDto` {#schema-publicmysqlparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `database` | string | no | Your database name |
| `host` | string | no | Your MySQL server hostname |
| `mysqlTlsVersion` | enum (`TLS_V_1_2`, `TLS_V_1_3`) | no | The TLS version to use to connect to your MySQL server |
| `port` | integer (int32) | no | Your MySQL server port |


### `PublicSnowflakeParametersDto` {#schema-publicsnowflakeparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `accountIdentifier` | string | no | Your Snowflake account identifier |
| `database` | string | no | Your database name |
| `schema` | string | no | Your schema name |
| `warehouse` | string | no | Your Snowflake warehouse |


### `PublicLookerParametersDto` {#schema-publiclookerparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `gitConnections` | array<[`GitConnection`](#schema-gitconnection)> | no | The LookML configuration. See https://docs.siffletdata.com/docs/looker. If you don't use LookML, use an empty list `[]` |
| `host` | string | no | URL of the Looker site and append at the end the following "/api/4.0". For instance if you usually connect to Looker on "https://abcdef.cloud.looker.com/",  then you should add the following on host: "https://abcdef.cloud.looker.com/api/4.0"  |


### `PublicQuicksightParametersDto` {#schema-publicquicksightparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `accountId` | string | no | Your AWS account ID |
| `awsRegion` | string | no | Your AWS region |
| `roleArn` | string | no | The ARN for your QuickSight role |


### `PublicDeclarativeParametersDto` {#schema-publicdeclarativeparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |


### `PublicAthenaParametersDto` {#schema-publicathenaparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `database` | string | no | Your Athena database name |
| `datasource` | string | no | Your Athena data source name |
| `region` | string | no | Your Athena instance AWS region |
| `roleArn` | string | no | ARN of the IAM role to use for Athena queries |
| `s3OutputLocation` | string | no | The S3 location where Athena query results are stored |
| `vpcUrl` | string | no | Your VPC URL for Athena connection |
| `workgroup` | string | no | Your Athena workgroup name |


### `PublicRedshiftParametersDto` {#schema-publicredshiftparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `database` | string | no | Your database name |
| `host` | string | no | Your Redshift server host |
| `port` | integer (int32) | no | Your Redshift server port |
| `schema` | string | no | Your schema name |
| `ssl` | boolean | no | Whether to use SSL to connect to your Redshift server |


### `PublicDbtCloudParametersDto` {#schema-publicdbtcloudparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `accountId` | string | no | Your dbt Cloud account ID |
| `baseUrl` | string | no | Your dbt Cloud base URL |
| `jobDefinitionId` | string | no | Your dbt Cloud job ID |
| `projectId` | string | no | Your dbt Cloud project ID |


### `PublicOracleParametersDto` {#schema-publicoracleparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `database` | string | no | Your database name |
| `host` | string | no | Your Oracle server hostname |
| `port` | integer (int32) | no | Your Oracle server port |
| `schema` | string | no | Your schema name |


### `PublicSourceFilterDto` {#schema-publicsourcefilterdto}

Filter to apply on the sources search

| Name | Type | Required | Description |
|---|---|---|---|
| `tags` | array<[`PublicTagReferenceDto`](#schema-publictagreferencedto)> | no | List of tags to filter on |
| `textSearch` | string | no | Text to search in the name of the sources |
| `types` | array<enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`)> | no | List of source types to filter on |


### `PublicAirflowParametersDto` {#schema-publicairflowparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `host` | string | no | Your Airflow server hostname |
| `port` | integer (int32) | no | Your Airflow server port |


### `PublicFivetranParametersDto` {#schema-publicfivetranparametersdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, `TABLEAU`, … 8 more — full list in `openapi.json`) | yes |  |
| `host` | string | no | Your Fivetran environment URL |


### `PublicGetLastRunDto` {#schema-publicgetlastrundto}

Information about the last run of the source

| Name | Type | Required | Description |
|---|---|---|---|
| `status` | enum (`PENDING`, `RUNNING`, `SUCCESS`, `FAILURE`, `SKIPPED_DATASOURCE_ALREADY_RUNNING`, `SKIPPED_DATASOURCE_DEACTIVATED`) | no | Last run status of the source |
| `timestamp` | string (date-time) | no | Timestamp of the last update of the source |


### `GitConnection` {#schema-gitconnection}

The LookML configuration. See https://docs.siffletdata.com/docs/looker.
If you don’t use LookML or omit this field, it will default to an empty list.


| Name | Type | Required | Description |
|---|---|---|---|
| `authType` | enum (`HTTP_AUTHORIZATION_HEADER`, `USER_PASSWORD`, `SSH`) | yes |  |
| `branch` | string | no |  |
| `secretId` | string | yes |  |
| `url` | string | yes |  |

