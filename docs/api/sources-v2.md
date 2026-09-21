# Sources (v2)

Data-source management: create, edit, test connections, trigger ingestion.

[← Back to API index](README.md)

## `GET /v2/sources`

**Get list of sources**

- **operationId**: `publicGetSourcesV2`

**Response**

- `200` — Sources retrieved: [`PublicPageDtoPublicGetSourceV2Dto`](#schema-publicpagedtopublicgetsourcev2dto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v2/sources" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "data": [
    {}
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
| `409` | Conflict |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `POST /v2/sources`

**Create a source**

- **operationId**: `publicCreateSourceV2`

**Request body** (required, `application/json`)

_No fields._

**Response**

- `201` — Source created: [`PublicGetAdfSourceV2Dto`](#schema-publicgetadfsourcev2dto) or [`PublicGetAirflowSourceV2Dto`](#schema-publicgetairflowsourcev2dto) or [`PublicGetAthenaSourceV2Dto`](#schema-publicgetathenasourcev2dto) or [`PublicGetBigQuerySourceV2Dto`](#schema-publicgetbigquerysourcev2dto) or [`PublicGetDatabricksJobsSourceV2Dto`](#schema-publicgetdatabricksjobssourcev2dto) or [`PublicGetDatabricksSourceV2Dto`](#schema-publicgetdatabrickssourcev2dto) or [`PublicGetDbtCloudSourceV2Dto`](#schema-publicgetdbtcloudsourcev2dto) or [`PublicGetDbtSourceV2Dto`](#schema-publicgetdbtsourcev2dto) or [`PublicGetFivetranSourceV2Dto`](#schema-publicgetfivetransourcev2dto) or [`PublicGetLookerSourceV2Dto`](#schema-publicgetlookersourcev2dto) or [`PublicGetMicrostrategySourceV2Dto`](#schema-publicgetmicrostrategysourcev2dto) or [`PublicGetMssqlSourceV2Dto`](#schema-publicgetmssqlsourcev2dto) or [`PublicGetMysqlSourceV2Dto`](#schema-publicgetmysqlsourcev2dto) or [`PublicGetOracleSourceV2Dto`](#schema-publicgetoraclesourcev2dto) or [`PublicGetPostgresqlSourceV2Dto`](#schema-publicgetpostgresqlsourcev2dto) or [`PublicGetPowerBiSourceV2Dto`](#schema-publicgetpowerbisourcev2dto) or [`PublicGetQlikSourceV2Dto`](#schema-publicgetqliksourcev2dto) or [`PublicGetQuicksightSourceV2Dto`](#schema-publicgetquicksightsourcev2dto) or [`PublicGetRedshiftSourceV2Dto`](#schema-publicgetredshiftsourcev2dto) or [`PublicGetSnowflakeSourceV2Dto`](#schema-publicgetsnowflakesourcev2dto) or [`PublicGetSynapseSourceV2Dto`](#schema-publicgetsynapsesourcev2dto) or [`PublicGetTableauSourceV2Dto`](#schema-publicgettableausourcev2dto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v2/sources" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

Example `201` response:

```json
{}
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

## `POST /v2/sources/run-subsource`

**Manually trigger a subsource metadata ingestion job**

- **operationId**: `publicRunSubsourceV2`

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `uri` | string | yes |  |

**Response**

- `204` — Job triggered (no body)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v2/sources/run-subsource" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "uri": "string"
}'
```

**Errors**

| Status | Description |
|---|---|
| `400` | Bad request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Resource not found |
| `409` | Conflict |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `POST /v2/sources/test-connection`

**Test connection with given source params**

- **operationId**: `publicTestSourceConnectionV2`

**Request body** (required, `application/json`)

_No fields._

**Response**

- `200` — Connection test result: [`PublicTestSourceConnectionResponseV2Dto`](#schema-publictestsourceconnectionresponsev2dto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v2/sources/test-connection" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

Example `200` response:

```json
{
  "errorMessages": [
    "string"
  ],
  "status": "SUCCESS",
  "successMessages": [
    "string"
  ],
  "warningMessages": [
    "string"
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

## `POST /v2/sources/test-subsource-connection`

**Test connection with given subsource params**

- **operationId**: `publicTestSubsourceConnectionV2`

**Request body** (required, `application/json`)

_No fields._

**Response**

- `200` — Connection test result: [`PublicTestSourceConnectionResponseV2Dto`](#schema-publictestsourceconnectionresponsev2dto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v2/sources/test-subsource-connection" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

Example `200` response:

```json
{
  "errorMessages": [
    "string"
  ],
  "status": "SUCCESS",
  "successMessages": [
    "string"
  ],
  "warningMessages": [
    "string"
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

## `POST /v2/sources/test-subsource-connection-by-uri`

**Test connection for an existing subsource identified by its URI**

- **operationId**: `publicTestSubsourceConnectionByUriV2`

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `uri` | string | yes |  |

**Response**

- `200` — Connection test result: [`PublicTestSourceConnectionResponseV2Dto`](#schema-publictestsourceconnectionresponsev2dto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v2/sources/test-subsource-connection-by-uri" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "uri": "string"
}'
```

Example `200` response:

```json
{
  "errorMessages": [
    "string"
  ],
  "status": "SUCCESS",
  "successMessages": [
    "string"
  ],
  "warningMessages": [
    "string"
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
| `409` | Conflict |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `DELETE /v2/sources/{id}`

**Delete a source**

- **operationId**: `publicDeleteSourceV2`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `204` — Source deleted (no body)

**Example call**

```bash
curl -X DELETE \
  "https://{tenant}.siffletdata.com/api/v2/sources/{id}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

**Errors**

| Status | Description |
|---|---|
| `400` | Bad request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Resource not found |
| `409` | Conflict |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `GET /v2/sources/{id}`

**Get a source by id**

- **operationId**: `publicGetSourceV2`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `200` — Source retrieved: [`PublicGetAdfSourceV2Dto`](#schema-publicgetadfsourcev2dto) or [`PublicGetAirflowSourceV2Dto`](#schema-publicgetairflowsourcev2dto) or [`PublicGetAthenaSourceV2Dto`](#schema-publicgetathenasourcev2dto) or [`PublicGetBigQuerySourceV2Dto`](#schema-publicgetbigquerysourcev2dto) or [`PublicGetDatabricksJobsSourceV2Dto`](#schema-publicgetdatabricksjobssourcev2dto) or [`PublicGetDatabricksSourceV2Dto`](#schema-publicgetdatabrickssourcev2dto) or [`PublicGetDbtCloudSourceV2Dto`](#schema-publicgetdbtcloudsourcev2dto) or [`PublicGetDbtSourceV2Dto`](#schema-publicgetdbtsourcev2dto) or [`PublicGetFivetranSourceV2Dto`](#schema-publicgetfivetransourcev2dto) or [`PublicGetLookerSourceV2Dto`](#schema-publicgetlookersourcev2dto) or [`PublicGetMicrostrategySourceV2Dto`](#schema-publicgetmicrostrategysourcev2dto) or [`PublicGetMssqlSourceV2Dto`](#schema-publicgetmssqlsourcev2dto) or [`PublicGetMysqlSourceV2Dto`](#schema-publicgetmysqlsourcev2dto) or [`PublicGetOracleSourceV2Dto`](#schema-publicgetoraclesourcev2dto) or [`PublicGetPostgresqlSourceV2Dto`](#schema-publicgetpostgresqlsourcev2dto) or [`PublicGetPowerBiSourceV2Dto`](#schema-publicgetpowerbisourcev2dto) or [`PublicGetQlikSourceV2Dto`](#schema-publicgetqliksourcev2dto) or [`PublicGetQuicksightSourceV2Dto`](#schema-publicgetquicksightsourcev2dto) or [`PublicGetRedshiftSourceV2Dto`](#schema-publicgetredshiftsourcev2dto) or [`PublicGetSnowflakeSourceV2Dto`](#schema-publicgetsnowflakesourcev2dto) or [`PublicGetSynapseSourceV2Dto`](#schema-publicgetsynapsesourcev2dto) or [`PublicGetTableauSourceV2Dto`](#schema-publicgettableausourcev2dto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v2/sources/{id}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{}
```

**Errors**

| Status | Description |
|---|---|
| `400` | Bad request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Resource not found |
| `409` | Conflict |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `PATCH /v2/sources/{id}`

**Edit a source**

- **operationId**: `publicEditSourceV2`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Request body** (required, `application/json`)

_No fields._

**Response**

- `200` — Source edited: [`PublicGetAdfSourceV2Dto`](#schema-publicgetadfsourcev2dto) or [`PublicGetAirflowSourceV2Dto`](#schema-publicgetairflowsourcev2dto) or [`PublicGetAthenaSourceV2Dto`](#schema-publicgetathenasourcev2dto) or [`PublicGetBigQuerySourceV2Dto`](#schema-publicgetbigquerysourcev2dto) or [`PublicGetDatabricksJobsSourceV2Dto`](#schema-publicgetdatabricksjobssourcev2dto) or [`PublicGetDatabricksSourceV2Dto`](#schema-publicgetdatabrickssourcev2dto) or [`PublicGetDbtCloudSourceV2Dto`](#schema-publicgetdbtcloudsourcev2dto) or [`PublicGetDbtSourceV2Dto`](#schema-publicgetdbtsourcev2dto) or [`PublicGetFivetranSourceV2Dto`](#schema-publicgetfivetransourcev2dto) or [`PublicGetLookerSourceV2Dto`](#schema-publicgetlookersourcev2dto) or [`PublicGetMicrostrategySourceV2Dto`](#schema-publicgetmicrostrategysourcev2dto) or [`PublicGetMssqlSourceV2Dto`](#schema-publicgetmssqlsourcev2dto) or [`PublicGetMysqlSourceV2Dto`](#schema-publicgetmysqlsourcev2dto) or [`PublicGetOracleSourceV2Dto`](#schema-publicgetoraclesourcev2dto) or [`PublicGetPostgresqlSourceV2Dto`](#schema-publicgetpostgresqlsourcev2dto) or [`PublicGetPowerBiSourceV2Dto`](#schema-publicgetpowerbisourcev2dto) or [`PublicGetQlikSourceV2Dto`](#schema-publicgetqliksourcev2dto) or [`PublicGetQuicksightSourceV2Dto`](#schema-publicgetquicksightsourcev2dto) or [`PublicGetRedshiftSourceV2Dto`](#schema-publicgetredshiftsourcev2dto) or [`PublicGetSnowflakeSourceV2Dto`](#schema-publicgetsnowflakesourcev2dto) or [`PublicGetSynapseSourceV2Dto`](#schema-publicgetsynapsesourcev2dto) or [`PublicGetTableauSourceV2Dto`](#schema-publicgettableausourcev2dto)

**Example call**

```bash
curl -X PATCH \
  "https://{tenant}.siffletdata.com/api/v2/sources/{id}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

Example `200` response:

```json
{}
```

**Errors**

| Status | Description |
|---|---|
| `400` | Bad request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Resource not found |
| `409` | Conflict |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `POST /v2/sources/{id}/run`

**Manually trigger an integration ingestion job**

- **operationId**: `publicRunSourceV2`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `204` — Job triggered (no body)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v2/sources/{id}/run" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

**Errors**

| Status | Description |
|---|---|
| `400` | Bad request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Resource not found |
| `409` | Conflict |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `GET /v2/sources/{id}/schemas`

**Get all schemas for a given source id**

- **operationId**: `publicGetSourceSchemaList`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `200` — Source schemas retrieved: [`PublicGetSourceSchemaListDto`](#schema-publicgetsourceschemalistdto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v2/sources/{id}/schemas" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "schemas": [
    {
      "uri": "string"
    }
  ],
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
| `409` | Conflict |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `POST /v2/sources/{id}/test-connection`

**Test connection for an existing source**

- **operationId**: `publicTestExistingSourceConnectionV2`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `200` — Connection test result: [`PublicTestSourceConnectionResponseV2Dto`](#schema-publictestsourceconnectionresponsev2dto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v2/sources/{id}/test-connection" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "errorMessages": [
    "string"
  ],
  "status": "SUCCESS",
  "successMessages": [
    "string"
  ],
  "warningMessages": [
    "string"
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
| `409` | Conflict |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## Referenced object schemas

### `PublicGetPostgresqlSourceV2Dto` {#schema-publicgetpostgresqlsourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `credentials` | string | no | Credentials of the source |
| `postgresqlInformation` | [`PostgresqlInformation`](#schema-postgresqlinformation) | no | PostgreSQL connection settings |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PublicGetSnowflakeSourceV2Dto` {#schema-publicgetsnowflakesourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `credentials` | string | no | Credentials of the source |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |
| `snowflakeInformation` | [`SnowflakeInformation`](#schema-snowflakeinformation) | no | Snowflake connection settings |


### `PublicTestSourceConnectionResponseV2Dto` {#schema-publictestsourceconnectionresponsev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `errorMessages` | array<string> | no |  |
| `status` | enum (`SUCCESS`, `WARNING`, `ERROR`) | no |  |
| `successMessages` | array<string> | no |  |
| `warningMessages` | array<string> | no |  |


### `PublicGetPowerBiSourceV2Dto` {#schema-publicgetpowerbisourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `credentials` | string | no | Credentials of the source |
| `powerBiInformation` | [`PowerBiInformation`](#schema-powerbiinformation) | no | Power BI connection settings |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PublicGetAthenaSourceV2Dto` {#schema-publicgetathenasourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `athenaInformation` | [`AthenaInformation`](#schema-athenainformation) | no | Athena connection settings |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PublicGetOracleSourceV2Dto` {#schema-publicgetoraclesourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `credentials` | string | no | Credentials of the source |
| `oracleInformation` | [`OracleInformation`](#schema-oracleinformation) | no | Oracle connection settings |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PublicPageDtoPublicGetSourceV2Dto` {#schema-publicpagedtopublicgetsourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `data` | array<[`PublicGetAdfSourceV2Dto`](#schema-publicgetadfsourcev2dto) or [`PublicGetAirflowSourceV2Dto`](#schema-publicgetairflowsourcev2dto) or [`PublicGetAthenaSourceV2Dto`](#schema-publicgetathenasourcev2dto) or [`PublicGetBigQuerySourceV2Dto`](#schema-publicgetbigquerysourcev2dto) or [`PublicGetDatabricksJobsSourceV2Dto`](#schema-publicgetdatabricksjobssourcev2dto) or [`PublicGetDatabricksSourceV2Dto`](#schema-publicgetdatabrickssourcev2dto) or [`PublicGetDbtCloudSourceV2Dto`](#schema-publicgetdbtcloudsourcev2dto) or [`PublicGetDbtSourceV2Dto`](#schema-publicgetdbtsourcev2dto) or [`PublicGetFivetranSourceV2Dto`](#schema-publicgetfivetransourcev2dto) or [`PublicGetLookerSourceV2Dto`](#schema-publicgetlookersourcev2dto) or [`PublicGetMicrostrategySourceV2Dto`](#schema-publicgetmicrostrategysourcev2dto) or [`PublicGetMssqlSourceV2Dto`](#schema-publicgetmssqlsourcev2dto) or [`PublicGetMysqlSourceV2Dto`](#schema-publicgetmysqlsourcev2dto) or [`PublicGetOracleSourceV2Dto`](#schema-publicgetoraclesourcev2dto) or [`PublicGetPostgresqlSourceV2Dto`](#schema-publicgetpostgresqlsourcev2dto) or [`PublicGetPowerBiSourceV2Dto`](#schema-publicgetpowerbisourcev2dto) or [`PublicGetQlikSourceV2Dto`](#schema-publicgetqliksourcev2dto) or [`PublicGetQuicksightSourceV2Dto`](#schema-publicgetquicksightsourcev2dto) or [`PublicGetRedshiftSourceV2Dto`](#schema-publicgetredshiftsourcev2dto) or [`PublicGetSnowflakeSourceV2Dto`](#schema-publicgetsnowflakesourcev2dto) or [`PublicGetSynapseSourceV2Dto`](#schema-publicgetsynapsesourcev2dto) or [`PublicGetTableauSourceV2Dto`](#schema-publicgettableausourcev2dto)> | yes |  |
| `totalCount` | integer (int64) | no |  |


### `PublicGetMssqlSourceV2Dto` {#schema-publicgetmssqlsourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `credentials` | string | no | Credentials of the source |
| `mssqlInformation` | [`MssqlInformation`](#schema-mssqlinformation) | no | MSSQL connection settings |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PublicGetDbtCloudSourceV2Dto` {#schema-publicgetdbtcloudsourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `credentials` | string | no | Credentials of the source |
| `dbtCloudInformation` | [`DbtCloudInformation`](#schema-dbtcloudinformation) | no | DBT Cloud connection settings |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PublicGetQlikSourceV2Dto` {#schema-publicgetqliksourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `credentials` | string | no | Credentials of the source |
| `qlikInformation` | [`QlikInformation`](#schema-qlikinformation) | no | Qlik connection settings |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PublicGetAdfSourceV2Dto` {#schema-publicgetadfsourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `adfInformation` | [`AdfInformation`](#schema-adfinformation) | no | ADF connection settings |
| `credentials` | string | no | Credentials of the source |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PublicGetDbtSourceV2Dto` {#schema-publicgetdbtsourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `dbtInformation` | [`DbtInformation`](#schema-dbtinformation) | no | DBT connection settings |


### `PublicGetSynapseSourceV2Dto` {#schema-publicgetsynapsesourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `credentials` | string | no | Credentials of the source |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |
| `synapseInformation` | [`SynapseInformation`](#schema-synapseinformation) | no | Synapse connection settings |


### `PublicGetQuicksightSourceV2Dto` {#schema-publicgetquicksightsourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `quicksightInformation` | [`QuicksightInformation`](#schema-quicksightinformation) | no | QuickSight connection settings |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PublicGetDatabricksJobsSourceV2Dto` {#schema-publicgetdatabricksjobssourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `credentials` | string | no | Credentials of the source |
| `databricksJobsInformation` | [`DatabricksJobsInformation`](#schema-databricksjobsinformation) | no | Databricks Jobs connection settings |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PublicGetTableauSourceV2Dto` {#schema-publicgettableausourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `credentials` | string | no | Credentials of the source |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |
| `tableauInformation` | [`TableauInformation`](#schema-tableauinformation) | no | Tableau connection settings |


### `PublicGetLookerSourceV2Dto` {#schema-publicgetlookersourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `credentials` | string | no | Credentials of the source |
| `lookerInformation` | [`LookerInformation`](#schema-lookerinformation) | no | Looker connection settings |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PublicGetMicrostrategySourceV2Dto` {#schema-publicgetmicrostrategysourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `credentials` | string | no | Credentials of the source |
| `microstrategyInformation` | [`MicrostrategyInformation`](#schema-microstrategyinformation) | no | MicroStrategy connection settings |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PublicGetAirflowSourceV2Dto` {#schema-publicgetairflowsourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `airflowInformation` | [`AirflowInformation`](#schema-airflowinformation) | no | Airflow connection settings |
| `credentials` | string | no | Credentials of the source |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PublicGetDatabricksSourceV2Dto` {#schema-publicgetdatabrickssourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `credentials` | string | no | Credentials of the source |
| `databricksInformation` | [`DatabricksInformation`](#schema-databricksinformation) | no | Databricks connection settings |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PublicGetSourceSchemaListDto` {#schema-publicgetsourceschemalistdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | yes |  |
| `schemas` | array<[`PublicGetSourceSchemaDto`](#schema-publicgetsourceschemadto)> | yes | Schemas existing for the source |


### `PublicGetFivetranSourceV2Dto` {#schema-publicgetfivetransourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `credentials` | string | no | Credentials of the source |
| `fivetranInformation` | [`FivetranInformation`](#schema-fivetraninformation) | no | Fivetran connection settings |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PublicGetBigQuerySourceV2Dto` {#schema-publicgetbigquerysourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `bigQueryInformation` | [`BigQueryInformation`](#schema-bigqueryinformation) | no | BigQuery connection settings |
| `credentials` | string | no | Credentials of the source |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PublicGetRedshiftSourceV2Dto` {#schema-publicgetredshiftsourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `credentials` | string | no | Credentials of the source |
| `redshiftInformation` | [`RedshiftInformation`](#schema-redshiftinformation) | no | Redshift connection settings |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PublicGetMysqlSourceV2Dto` {#schema-publicgetmysqlsourcev2dto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | id the source |
| `lastRun` | [`PublicGetLastRunV2Dto`](#schema-publicgetlastrunv2dto) | no | Information about the last run of the source |
| `name` | string | yes | Name of the source |
| `type` | enum (`ATHENA`, `BIGQUERY`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `MSSQL`, `MYSQL`, `POSTGRESQL`, `ORACLE`, `SYNAPSE`, `LOOKER`, … 11 more — full list in `openapi.json`) | yes | Source type |
| `credentials` | string | no | Credentials of the source |
| `mysqlInformation` | [`MysqlInformation`](#schema-mysqlinformation) | no | MySQL connection settings |
| `schedule` | string | no | Schedule of the source. Supports CRON syntax. If empty, the source won't be scheduled. |


### `PostgresqlInformation` {#schema-postgresqlinformation}

PostgreSQL connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `database` | string | yes | Your database name |
| `host` | string | yes | Your PostgreSQL server host |
| `port` | integer (int32) | yes | Your PostgreSQL server port |


### `PublicGetLastRunV2Dto` {#schema-publicgetlastrunv2dto}

Information about the last run of the source

| Name | Type | Required | Description |
|---|---|---|---|
| `status` | enum (`RUNNING`, `SUCCESS`, `FAILURE`) | no | Last run status of the source |
| `timestamp` | string (date-time) | no | Timestamp of the last update of the source |


### `SnowflakeInformation` {#schema-snowflakeinformation}

Snowflake connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `accountIdentifier` | string | yes | Your Snowflake account identifier |
| `warehouse` | string | yes | Your Snowflake warehouse |


### `PowerBiInformation` {#schema-powerbiinformation}

Power BI connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `clientId` | string | yes | Your Azure AD client ID |
| `tenantId` | string | yes | Your Azure AD tenant ID |


### `AthenaInformation` {#schema-athenainformation}

Athena connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `datasource` | string | yes | Your Athena data source name |
| `region` | string | yes | Your Athena instance AWS region |
| `roleArn` | string | yes | ARN of the IAM role to use for Athena queries |
| `s3OutputLocation` | string | yes | The S3 location where Athena query results are stored |
| `vpcUrl` | string | no | Your VPC URL for Athena connection |
| `workgroup` | string | yes | Your Athena workgroup name |


### `OracleInformation` {#schema-oracleinformation}

Oracle connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `database` | string | yes | Your database name |
| `host` | string | yes | Your Oracle server hostname |
| `port` | integer (int32) | yes | Your Oracle server port |


### `MssqlInformation` {#schema-mssqlinformation}

MSSQL connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `database` | string | yes | Your database name |
| `host` | string | yes | Your MSSQL server hostname |
| `port` | integer (int32) | yes | Your MSSQL server port |
| `ssl` | boolean | yes | Whether to use SSL to connect to your MSSQL server (recommended: true) |


### `DbtCloudInformation` {#schema-dbtcloudinformation}

DBT Cloud connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `accountId` | string | yes | Your dbt Cloud account ID |
| `baseUrl` | string | yes | Your dbt Cloud base URL |


### `QlikInformation` {#schema-qlikinformation}

Qlik connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `host` | string | yes | Your Qlik server URL |


### `AdfInformation` {#schema-adfinformation}

ADF connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `factoryName` | string | yes | Your ADF Factory Name |
| `resourceGroup` | string | yes | Your ADF Resource Group |
| `subscriptionId` | string | yes | Your ADF Subscription ID |
| `tenantId` | string | yes | Your ADF Tenant ID |


### `DbtInformation` {#schema-dbtinformation}

DBT connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `projectName` | string | yes | Your dbt project name (the 'name' value in your dbt_project.yml file) |
| `target` | string | yes | Your dbt target name (the 'target' value in your profiles.yml file) |


### `SynapseInformation` {#schema-synapseinformation}

Synapse connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `host` | string | yes | The host of your Synapse server |
| `port` | integer (int32) | yes | Your Synapse server port |


### `QuicksightInformation` {#schema-quicksightinformation}

QuickSight connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `accountId` | string | yes | Your AWS account ID |
| `awsRegion` | string | yes | Your AWS region |
| `roleArn` | string | yes | The ARN for your QuickSight role |


### `DatabricksJobsInformation` {#schema-databricksjobsinformation}

Databricks Jobs connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `host` | string | yes | Your Databricks Jobs server hostname |
| `httpPath` | string | yes | Your Databricks Jobs HTTP path |
| `port` | integer (int32) | yes | Your Databricks Jobs server port |


### `TableauInformation` {#schema-tableauinformation}

Tableau connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `host` | string | yes | Your Tableau Server hostname |
| `site` | string | yes | Your Tableau Server site. Leave empty if your Tableau environment is using the Default Site. |


### `LookerInformation` {#schema-lookerinformation}

Looker connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `gitConnections` | array<[`GitConnection`](#schema-gitconnection)> | no | The LookML configuration. See https://docs.siffletdata.com/docs/looker. If you don’t use LookML or omit this field, it will default to an empty list.  |
| `host` | string | yes | URL of the Looker site and append at the end the following "/api/4.0". For instance if you usually connect to Looker on "https://abcdef.cloud.looker.com/",  then you should add the following on host: "https://abcdef.cloud.looker.com/api/4.0"  |


### `MicrostrategyInformation` {#schema-microstrategyinformation}

MicroStrategy connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `host` | string | yes | Your MicroStrategy host |


### `AirflowInformation` {#schema-airflowinformation}

Airflow connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `host` | string | yes | Your Airflow server hostname |
| `port` | integer (int32) | yes | Your Airflow server port |


### `DatabricksInformation` {#schema-databricksinformation}

Databricks connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `host` | string | yes | Your Databricks server hostname |
| `httpPath` | string | yes | Your Databricks HTTP path |
| `port` | integer (int32) | yes | Your Databricks server port |


### `PublicGetSourceSchemaDto` {#schema-publicgetsourceschemadto}

Schemas existing for the source

| Name | Type | Required | Description |
|---|---|---|---|
| `uri` | string | yes |  |


### `FivetranInformation` {#schema-fivetraninformation}

Fivetran connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `host` | string | yes | Your Fivetran environment URL |


### `BigQueryInformation` {#schema-bigqueryinformation}

BigQuery connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `billingProjectId` | string | no | Your billing project ID |
| `projectId` | string | yes | Your BigQuery project ID |
| `workerProjectIds` | string | no | Comma separated list of project ids where your queries run. Optional if it's the same as the projectId parameter |


### `RedshiftInformation` {#schema-redshiftinformation}

Redshift connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `host` | string | yes | Your Redshift server host |
| `port` | integer (int32) | yes | Your Redshift server port |
| `ssl` | boolean | yes | Whether to use SSL to connect to your Redshift server |


### `MysqlInformation` {#schema-mysqlinformation}

MySQL connection settings

| Name | Type | Required | Description |
|---|---|---|---|
| `database` | string | yes | Your database name |
| `host` | string | yes | Your MySQL server hostname |
| `mysqlTlsVersion` | enum (`TLS_V_1_2`, `TLS_V_1_3`) | yes | The TLS version to use to connect to your MySQL server |
| `port` | integer (int32) | yes | Your MySQL server port |


### `GitConnection` {#schema-gitconnection}

The LookML configuration. See https://docs.siffletdata.com/docs/looker.
If you don’t use LookML or omit this field, it will default to an empty list.


| Name | Type | Required | Description |
|---|---|---|---|
| `authType` | enum (`HTTP_AUTHORIZATION_HEADER`, `USER_PASSWORD`, `SSH`) | yes |  |
| `branch` | string | no |  |
| `secretId` | string | yes |  |
| `url` | string | yes |  |

