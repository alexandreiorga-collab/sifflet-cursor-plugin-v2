# Monitoring Rules

Sifflet monitors (rules): list, details, manual run, as-code export.

[← Back to API index](README.md)

## `GET /v1/rules`

**Get all Sifflet rules**

- **operationId**: `getAllRule`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `textSearch (query)` | string | no | Global text search |
| `ruleTemplateName (query)` | array<string> | no | Filter on given rule template name |
| `lastRunStatus (query)` | array<enum (`PENDING`, `RUNNING`, `SUCCESS`, `REQUIRES_YOUR_ATTENTION`, `TECHNICAL_ERROR`, `FAILED`)> | no | Filter on given last run statuses |
| `ruleStatus (query)` | array<enum (`NOT_EVALUATED`, `PASSING`, `NEEDS_ATTENTION`, `FAILING`)> | no | Filter on given rule status |
| `dataset (query)` | array<string (uuid)> | no | Filter on given dataset ids |
| `tag (query)` | array<string (uuid)> | no | Filter on given tag ids |
| `datasource (query)` | array<string (uuid)> | no | Filter on given datasource ids |
| `criticality (query)` | array<integer (int32)> | no |  |
| `domain (query)` | string | no | Domain searched |
| `page (query)` | integer (int32) | no | The requested page number. Zero-based page index (0..N) |
| `itemsPerPage (query)` | integer (int32) | no | The number of elements to be returned inside the page. Pass a value of -1, to bypass pagination and fetch all items |
| `sort (query)` | array<string (property,ASC\|DESC)> | no | The resource fields on which to apply the sort, format : property,ASC\|DESC |

**Response**

- `200` — Successfully fetch all rule catalog assets: [`MonitoringSearchDto`](#schema-monitoringsearchdto)
- `206` — Successfully fetch partial content of rule catalog assets: [`MonitoringSearchDto`](#schema-monitoringsearchdto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/rules" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "catalogFilters": [
    {
      "children": [
        "..."
      ],
      "id": "string",
      "name": "string",
      "query": "string"
    }
  ],
  "searchRules": {
    "data": [
      {
        "datasets": "...",
        "supportAsCodeYAMLConversion": "...",
        "tags": "...",
        "multiDimensional": "...",
        "msTeams": "...",
        "id": "...",
        "mails": "...",
        "ruleType": "...",
        "ruleStatus": "...",
        "lastWeekStatuses": "...",
        "hasAiRecommendations": "...",
        "terms": "...",
        "slackChannels": "...",
        "readOnly": "...",
        "name": "...",
        "canManuallyRun": "...",
        "sourcePlatform": "...",
        "datasetFieldNames": "...",
        "criticality": "...",
        "selectable": "..."
      }
    ]
  }
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

## `GET /v1/rules/_all-as-code`

**Convert all monitors to as-code** — Fetches monitors, converts each to its as-code representation, and returns them in a paginated list.

- **operationId**: `getAllMonitorsAsCode`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `mode (query)` | enum (`RELAXED`, `STRICT`, `EXPANDED`) | no |  |
| `textSearch (query)` | string | no | Global text search |
| `ruleTemplateName (query)` | array<string> | no | Filter on given rule template name |
| `lastRunStatus (query)` | array<enum (`PENDING`, `RUNNING`, `SUCCESS`, `REQUIRES_YOUR_ATTENTION`, `TECHNICAL_ERROR`, `FAILED`)> | no | Filter on given last run statuses |
| `ruleStatus (query)` | array<enum (`NOT_EVALUATED`, `PASSING`, `NEEDS_ATTENTION`, `FAILING`)> | no | Filter on given rule status |
| `dataset (query)` | array<string (uuid)> | no | Filter on given dataset ids |
| `tag (query)` | array<string (uuid)> | no | Filter on given tag ids |
| `datasource (query)` | array<string (uuid)> | no | Filter on given datasource ids |
| `criticality (query)` | array<integer (int32)> | no |  |
| `domain (query)` | string | no | Domain searched |
| `page (query)` | integer (int32) | no | The requested page number. Zero-based page index (0..N) |
| `itemsPerPage (query)` | integer (int32) | no | The number of elements to be returned inside the page. Pass a value of -1, to bypass pagination and fetch all items |
| `sort (query)` | array<string (property,ASC\|DESC)> | no | The resource fields on which to apply the sort, format : property,ASC\|DESC |

**Response**

- `200` — Successfully converted monitors to as-code: array<[`AsCodeMonitorDto`](#schema-ascodemonitordto)>

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/rules/_all-as-code" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
[
  {
    "joins": [
      {
        "joinCondition": "...",
        "dataset": "...",
        "joinType": "..."
      }
    ],
    "name": "string",
    "incident": {
      "severity": "Low"
    },
    "version": 0,
    "parameters": {}
  }
]
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

## `GET /v1/rules/runs/{runId}/decrypt`

**Decrypt rule run groups**

- **operationId**: `decryptRuleRunGroups`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `runId (path)` | string (uuid) | yes |  |

**Response**

- `200` — Successfully fetch rule run groups decryption: [`GroupDecryptedValuesDto`](#schema-groupdecryptedvaluesdto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/rules/runs/{runId}/decrypt" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "decryptedValues": {}
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

## `POST /v1/rules/{id}/_run`

**Trigger a run of the given Sifflet rule id**

- **operationId**: `siffletRuleManualRun`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `200` — Successfully trigger Sifflet rule manual run: [`RuleRunDto`](#schema-rulerundto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v1/rules/{id}/_run" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "canShowFailingRows": true,
  "hasGraph": true,
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "debuggable": true,
  "hasGroupBy": true
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

## `GET /v1/rules/{id}/decrypt`

**Decrypt rule groups**

- **operationId**: `decryptRuleGroups`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `200` — Successfully fetch rule groups decryption: [`GroupDecryptedValuesDto`](#schema-groupdecryptedvaluesdto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/rules/{id}/decrypt" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "decryptedValues": {}
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

## `GET /v1/rules/{id}/details`

**Get Sifflet rule details by rule id**

- **operationId**: `getSiffletRuleDetails`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `200` — Successfully fetch rule details: [`RuleDetailsDto`](#schema-ruledetailsdto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/rules/{id}/details" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "createdByProvider": {},
  "modifiedByProvider": {},
  "slackChannels": [
    {
      "type": "SLACK",
      "name": "string",
      "externalHook": "string",
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }
  ],
  "tags": [
    {
      "type": "GENERIC",
      "name": "string",
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }
  ],
  "provider": {},
  "msTeams": [
    {
      "type": "SLACK",
      "name": "string",
      "externalHook": "string",
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }
  ],
  "webhooks": [
    {
      "type": "SLACK",
      "name": "string",
      "externalHook": "string",
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }
  ],
  "terms": [
    {
      "type": "GENERIC",
      "name": "string",
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }
  ],
  "mails": [
    {
      "type": "SLACK",
      "name": "string",
      "externalHook": "string",
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
| `409` | Conflict |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `GET /v1/rules/{id}/info`

**Get Sifflet rule information by rule id**

- **operationId**: `getSiffletRuleInfo`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `200` — Successfully fetch rule info: [`RuleInfoDto`](#schema-ruleinfodto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/rules/{id}/info" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "readOnly": true,
  "name": "string",
  "supportAsCodeYAMLConversion": true,
  "canManuallyRun": true,
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "canBeScheduled": true,
  "ruleTemplateName": "string",
  "sourcePlatform": "SIFFLET",
  "unresolvedIncidents": 0,
  "ruleLabel": "string",
  "canHaveFailingRows": true,
  "criticality": "CRITICAL",
  "canBeQualified": true,
  "ruleStatus": "NOT_EVALUATED"
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

## `GET /v1/rules/{id}/overview`

**Get Sifflet rule overview by rule id**

- **operationId**: `getSiffletRuleOverview`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `200` — Successfully fetch rule overview: [`RuleOverviewDto`](#schema-ruleoverviewdto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/rules/{id}/overview" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "description": "string"
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

## `GET /v1/rules/{id}/runs`

**Get all Sifflet rule runs by rule id**

- **operationId**: `getSiffletRuleRuns`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |
| `status (query)` | array<enum (`PENDING`, `RUNNING`, `SUCCESS`, `REQUIRES_YOUR_ATTENTION`, `TECHNICAL_ERROR`, `FAILED`)> | no | Filter by run status |
| `page (query)` | integer (int32) | no | The requested page number. Zero-based page index (0..N) |
| `itemsPerPage (query)` | integer (int32) | no | The number of elements to be returned inside the page. Pass a value of -1, to bypass pagination and fetch all items |
| `sort (query)` | array<string (property,ASC\|DESC)> | no | The resource fields on which to apply the sort, format : property,ASC\|DESC |

**Response**

- `200` — Successfully fetch Sifflet rule Runs: [`SearchCollectionRuleRunDto`](#schema-searchcollectionrulerundto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/rules/{id}/runs" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "data": [
    {
      "canShowFailingRows": true,
      "hasGraph": true,
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "debuggable": true,
      "hasGroupBy": true
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
| `409` | Conflict |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `GET /v1/rules/{id}/runs/{runId}`

**Get a Sifflet rule run by rule id and run id**

- **operationId**: `getSiffletRuleRun`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |
| `runId (path)` | string (uuid) | yes |  |
| `expand (query)` | array<enum (`VALUES`)> | no |  |

**Response**

- `200` — Successfully fetch Sifflet rule run: [`RuleRunDto`](#schema-rulerundto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/rules/{id}/runs/{runId}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "canShowFailingRows": true,
  "hasGraph": true,
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "debuggable": true,
  "hasGroupBy": true
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

### `RuleInfoDto` {#schema-ruleinfodto}

| Name | Type | Required | Description |
|---|---|---|---|
| `canBeQualified` | boolean | yes |  |
| `canBeScheduled` | boolean | yes |  |
| `canHaveFailingRows` | boolean | yes |  |
| `canManuallyRun` | boolean | yes |  |
| `criticality` | enum (`CRITICAL`, `HIGH`, `MODERATE`, `LOW`) | yes |  |
| `customMetadata` | array<[`EntityCustomMetadataDto`](#schema-entitycustommetadatadto)> | no |  |
| `datasets` | array<[`DatasetBriefDto`](#schema-datasetbriefdto)> | no |  |
| `id` | string (uuid) | yes |  |
| `lastIncident` | [`IncidentLightDto`](#schema-incidentlightdto) | no |  |
| `lastRunStatus` | enum (`PENDING`, `RUNNING`, `SUCCESS`, `REQUIRES_YOUR_ATTENTION`, `TECHNICAL_ERROR`, `FAILED`) | no |  |
| `lastRunTimestamp` | integer (int64) | no |  |
| `lastUnresolvedIncident` | [`IncidentLightDto`](#schema-incidentlightdto) | no |  |
| `mails` | array<[`AlertingHookDto`](#schema-alertinghookdto)> | no |  |
| `msTeams` | array<[`AlertingHookDto`](#schema-alertinghookdto)> | no |  |
| `muted` | boolean | no |  |
| `mutedUntil` | integer (int64) | no |  |
| `mutingMode` | enum (`INDEFINITE`, `UNTIL_DATE`, `UNTIL_NEXT_STATUS_IMPROVES`, `NOT_MUTED`) | no |  |
| `name` | string | yes |  |
| `readOnly` | boolean | yes |  |
| `ruleLabel` | string | yes |  |
| `ruleStatus` | enum (`NOT_EVALUATED`, `PASSING`, `NEEDS_ATTENTION`, `FAILING`) | yes |  |
| `ruleTemplateName` | string | yes |  |
| `schedule` | string | no |  |
| `scheduleTimezone` | [`TimeZoneDto`](#schema-timezonedto) | no |  |
| `slackChannels` | array<[`AlertingHookDto`](#schema-alertinghookdto)> | no |  |
| `sourcePlatform` | enum (`SIFFLET`, `DBT`) | yes |  |
| `supportAsCodeYAMLConversion` | boolean | yes |  |
| `tags` | array<[`TagDto`](#schema-tagdto)> | no |  |
| `unresolvedIncidents` | integer (int32) | yes |  |
| `workspace` | [`WorkspaceSummaryDto`](#schema-workspacesummarydto) | no |  |


### `GroupDecryptedValuesDto` {#schema-groupdecryptedvaluesdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `decryptedValues` | object | no |  |


### `RuleRunDto` {#schema-rulerundto}

| Name | Type | Required | Description |
|---|---|---|---|
| `canShowFailingRows` | boolean | yes |  |
| `createdBy` | string | no |  |
| `createdDate` | integer (int64) | no |  |
| `debugSql` | [`ParameterizedQueryDto`](#schema-parameterizedquerydto) | no |  |
| `debuggable` | boolean | yes |  |
| `endDate` | integer (int64) | no |  |
| `hasGraph` | boolean | yes |  |
| `hasGroupBy` | boolean | yes |  |
| `id` | string (uuid) | yes |  |
| `incidentIssue` | integer (int32) | no |  |
| `incidentName` | string | no |  |
| `incidentStatus` | enum (`OPEN`, `IN_PROGRESS`, `CLOSED`) | no |  |
| `result` | string | no |  |
| `ruleId` | string (uuid) | no |  |
| `startDate` | integer (int64) | no |  |
| `status` | enum (`PENDING`, `RUNNING`, `SUCCESS`, `REQUIRES_YOUR_ATTENTION`, `TECHNICAL_ERROR`, `FAILED`) | no |  |
| `type` | enum (`MANUAL`, `SCHEDULED`, `DBT`) | no |  |
| `values` | [`RuleRunValuesDto`](#schema-rulerunvaluesdto) | no |  |


### `AsCodeMonitorDto` {#schema-ascodemonitordto}

| Name | Type | Required | Description |
|---|---|---|---|
| `connection` | [`AsCodeConnectionParamsOverrideDto`](#schema-ascodeconnectionparamsoverridedto) | no |  |
| `customMetadataEntries` | array<[`AsCodeCustomMetadataEntryReferenceDto`](#schema-ascodecustommetadataentryreferencedto)> | no |  |
| `datasets` | array<[`AsCodeDatasetReferenceDto`](#schema-ascodedatasetreferencedto)> | no |  |
| `description` | string | no |  |
| `friendlyId` | string | no |  |
| `id` | string (uuid) | no |  |
| `incident` | [`AsCodeIncidentDto`](#schema-ascodeincidentdto) | yes |  |
| `joins` | array<[`AsCodeJoinDto`](#schema-ascodejoindto)> | yes |  |
| `kind` | enum (`Workspace`, `Monitor`, `Asset`, `Source`, `Lineage`) | no |  |
| `name` | string | yes |  |
| `notifications` | array<[`AsCodeAlertingHookNotificationDto`](#schema-ascodealertinghooknotificationdto) or [`AsCodeJiraNotificationDto`](#schema-ascodejiranotificationdto) or [`AsCodeServiceNowNotificationDto`](#schema-ascodeservicenownotificationdto)> | no |  |
| `overrideNotificationRules` | boolean | no |  |
| `parameters` | [`AsCodeCompletenessMonitorParamsDto`](#schema-ascodecompletenessmonitorparamsdto) or [`AsCodeConditionalMonitorParamsDto`](#schema-ascodeconditionalmonitorparamsdto) or [`AsCodeCorrelatedMetricsMonitorParamsDto`](#schema-ascodecorrelatedmetricsmonitorparamsdto) or [`AsCodeCustomMetricsMonitorParamsDtoV1`](#schema-ascodecustommetricsmonitorparamsdtov1) or [`AsCodeCustomMetricsMonitorParamsDtoV2`](#schema-ascodecustommetricsmonitorparamsdtov2) or [`AsCodeDistributionMonitorParamsDto`](#schema-ascodedistributionmonitorparamsdto) or [`AsCodeDuplicatesMonitorParamsDto`](#schema-ascodeduplicatesmonitorparamsdto) or [`AsCodeDynamicFieldProfilingMonitorParamsDto`](#schema-ascodedynamicfieldprofilingmonitorparamsdto) or [`AsCodeDynamicMetricMonitorParamsDto`](#schema-ascodedynamicmetricmonitorparamsdto) or [`AsCodeFieldDuplicatesMonitorParamsDto`](#schema-ascodefieldduplicatesmonitorparamsdto) or [`AsCodeFieldFormatMonitorParamsDtoV1`](#schema-ascodefieldformatmonitorparamsdtov1) or [`AsCodeFieldFormatMonitorParamsDtoV2`](#schema-ascodefieldformatmonitorparamsdtov2) or [`AsCodeFieldInListConstraintMonitorParamsDtoV1`](#schema-ascodefieldinlistconstraintmonitorparamsdtov1) or [`AsCodeFieldInListConstraintMonitorParamsDtoV2`](#schema-ascodefieldinlistconstraintmonitorparamsdtov2) or [`AsCodeFieldNullsMonitorParamsDto`](#schema-ascodefieldnullsmonitorparamsdto) or [`AsCodeFieldUniquenessMonitorParamsDto`](#schema-ascodefielduniquenessmonitorparamsdto) or [`AsCodeFreshnessMonitorParamsDtoV1`](#schema-ascodefreshnessmonitorparamsdtov1) or [`AsCodeFreshnessMonitorParamsDtoV2`](#schema-ascodefreshnessmonitorparamsdtov2) or [`AsCodeMetadataFreshnessMonitorParamsDtoV1`](#schema-ascodemetadatafreshnessmonitorparamsdtov1) or [`AsCodeMetadataFreshnessMonitorParamsDtoV2`](#schema-ascodemetadatafreshnessmonitorparamsdtov2) or [`AsCodeMetricsMonitorParamsDto`](#schema-ascodemetricsmonitorparamsdto) or [`AsCodeReferentialIntegrityMonitorParamsDtoV1`](#schema-ascodereferentialintegritymonitorparamsdtov1) or [`AsCodeReferentialIntegrityMonitorParamsDtoV2`](#schema-ascodereferentialintegritymonitorparamsdtov2) or [`AsCodeRowDuplicatesMonitorParamsDto`](#schema-ascoderowduplicatesmonitorparamsdto) or [`AsCodeSchemaChangeMonitorParamsDto`](#schema-ascodeschemachangemonitorparamsdto) or [`AsCodeSqlConditionMonitorParamsDto`](#schema-ascodesqlconditionmonitorparamsdto) or [`AsCodeSqlMonitorParamsDto`](#schema-ascodesqlmonitorparamsdto) or [`AsCodeStaticCompletenessMonitorParamsDto`](#schema-ascodestaticcompletenessmonitorparamsdto) or [`AsCodeStaticFieldProfilingMonitorParamsDto`](#schema-ascodestaticfieldprofilingmonitorparamsdto) or [`AsCodeStaticMetricMonitorParamsDto`](#schema-ascodestaticmetricmonitorparamsdto) or [`AsCodeValueRangeMonitorParamsDto`](#schema-ascodevaluerangemonitorparamsdto) or [`AsCodeVolumeMonitorParamsDto`](#schema-ascodevolumemonitorparamsdto) | yes |  |
| `schedule` | string | no |  |
| `scheduleTimezone` | string | no |  |
| `tags` | array<[`AsCodeTagReferenceDto`](#schema-ascodetagreferencedto)> | no |  |
| `terms` | array<[`AsCodeReferenceByIdOrNameDtoImpl`](#schema-ascodereferencebyidornamedtoimpl)> | no |  |
| `version` | integer (int32) | yes |  |


### `RuleOverviewDto` {#schema-ruleoverviewdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no |  |


### `SearchCollectionRuleRunDto` {#schema-searchcollectionrulerundto}

| Name | Type | Required | Description |
|---|---|---|---|
| `data` | array<[`RuleRunDto`](#schema-rulerundto)> | yes |  |
| `totalElements` | integer (int64) | no |  |


### `MonitoringSearchDto` {#schema-monitoringsearchdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `catalogFilters` | array<[`CatalogFilterDto`](#schema-catalogfilterdto)> | yes |  |
| `searchRules` | [`SearchCollectionRuleCatalogAssetDto`](#schema-searchcollectionrulecatalogassetdto) | yes |  |


### `RuleDetailsDto` {#schema-ruledetailsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `createdBy` | string | no |  |
| `createdByProvider` | [`AccessTokenProviderDto`](#schema-accesstokenproviderdto) or [`DatasourceProviderDto`](#schema-datasourceproviderdto) or [`GenericProviderDto`](#schema-genericproviderdto) or [`UserProviderDto`](#schema-userproviderdto) | yes |  |
| `createdDate` | integer (int64) | no |  |
| `jiraTemplateName` | string | no |  |
| `lastModifiedDate` | integer (int64) | no |  |
| `mails` | array<[`AlertingHookDto`](#schema-alertinghookdto)> | yes |  |
| `modifiedBy` | string | no |  |
| `modifiedByProvider` | [`AccessTokenProviderDto`](#schema-accesstokenproviderdto) or [`DatasourceProviderDto`](#schema-datasourceproviderdto) or [`GenericProviderDto`](#schema-genericproviderdto) or [`UserProviderDto`](#schema-userproviderdto) | yes |  |
| `msTeams` | array<[`AlertingHookDto`](#schema-alertinghookdto)> | yes |  |
| `provider` | [`AccessTokenProviderDto`](#schema-accesstokenproviderdto) or [`DatasourceProviderDto`](#schema-datasourceproviderdto) or [`GenericProviderDto`](#schema-genericproviderdto) or [`UserProviderDto`](#schema-userproviderdto) | yes |  |
| `ruleParams` | [`JsonNode`](#schema-jsonnode) | no |  |
| `serviceNowTemplateName` | string | no |  |
| `slackChannels` | array<[`AlertingHookDto`](#schema-alertinghookdto)> | yes |  |
| `tags` | array<[`TagDto`](#schema-tagdto)> | yes |  |
| `terms` | array<[`TagDto`](#schema-tagdto)> | yes |  |
| `webhooks` | array<[`AlertingHookDto`](#schema-alertinghookdto)> | yes |  |


### `EntityCustomMetadataDto` {#schema-entitycustommetadatadto}

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no |  |
| `entries` | array<[`EntityCustomMetadataEntryLabelDto`](#schema-entitycustommetadataentrylabeldto) or [`EntityCustomMetadataEntryStringDto`](#schema-entitycustommetadataentrystringdto) or [`EntityCustomMetadataEntryTeamDto`](#schema-entitycustommetadataentryteamdto) or [`EntityCustomMetadataEntryUserDto`](#schema-entitycustommetadataentryuserdto)> | yes |  |
| `id` | string (uuid) | yes |  |
| `lineagePlatform` | enum (`ATHENA`, `BIGQUERY`, `FIREBOLT`, `PRESTO`, `REDSHIFT`, `SNOWFLAKE`, `DATABRICKS`, `DATABRICKS_JOBS`, `ADF`, `MSSQL`, `MYSQL`, `SYNAPSE`, … 449 more — full list in `openapi.json`) | no |  |
| `name` | string | yes |  |
| `type` | enum (`LABEL`, `USER`, `STRING`, `TEAM`) | yes |  |


### `AlertingHookDto` {#schema-alertinghookdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `createdBy` | string | no |  |
| `createdDate` | integer (int64) | no |  |
| `externalHook` | string | yes |  |
| `id` | string (uuid) | yes |  |
| `lastModifiedDate` | integer (int64) | no |  |
| `modifiedBy` | string | no |  |
| `name` | string | yes |  |
| `params` | [`DefaultWebhookParams`](#schema-defaultwebhookparams) or [`GoogleChatWebhookParams`](#schema-googlechatwebhookparams) | no |  |
| `type` | enum (`SLACK`, `MAIL`, `MS_TEAMS`, `WEBHOOK`) | yes |  |


### `TagDto` {#schema-tagdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `createdBy` | string | no |  |
| `createdDate` | integer (int64) | no |  |
| `description` | string | no |  |
| `editable` | boolean | no |  |
| `id` | string (uuid) | yes |  |
| `lastModifiedDate` | integer (int64) | no |  |
| `modifiedBy` | string | no |  |
| `name` | string | yes |  |
| `type` | enum (`GENERIC`, `HIDDEN_DATA_CLASSIFICATION`, `VISIBLE_DATA_CLASSIFICATION`, `TERM`, `ATLAN_EXTERNAL_TERM`, `ALATION_EXTERNAL_TERM`, `AMUNDSEN_EXTERNAL_TERM`, `APACHE_ATLAS_EXTERNAL_TERM`, `CASTOR_DOC_EXTERNAL_TERM`, `COLLIBRA_EXTERNAL_TERM`, `DATAGALAXY_EXTERNAL_TERM`, `INFORMATICA_EXTERNAL_TERM`, … 19 more — full list in `openapi.json`) | yes |  |


### `TimeZoneDto` {#schema-timezonedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `timezone` | string | yes |  |
| `utcOffset` | string | yes |  |


### `DatasetBriefDto` {#schema-datasetbriefdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `datasourceName` | string | yes |  |
| `datasourceType` | string | yes |  |
| `id` | string (uuid) | yes |  |
| `name` | string | yes |  |
| `urn` | string | yes |  |


### `WorkspaceSummaryDto` {#schema-workspacesummarydto}

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no |  |
| `id` | string (uuid) | no |  |
| `name` | string | no |  |


### `IncidentLightDto` {#schema-incidentlightdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `collaborationToolItems` | array<[`GetCollaborationToolItemDto`](#schema-getcollaborationtoolitemdto)> | yes |  |
| `compromisedAssets` | integer (int32) | yes |  |
| `criticality` | integer (int32) | yes |  |
| `datasets` | array<[`DatasetBriefDto`](#schema-datasetbriefdto)> | yes |  |
| `id` | string (uuid) | yes |  |
| `isMutedIndefinitely` | boolean | yes |  |
| `issueNo` | integer (int32) | yes |  |
| `lastModifiedDate` | integer (int64) | no |  |
| `lastOccurredDate` | integer (int64) | yes |  |
| `mutedUntil` | integer (int64) | no |  |
| `name` | string | yes |  |
| `owners` | array<[`UserDto`](#schema-userdto)> | yes |  |
| `qualification` | enum (`FIXED`, `FALSE_POSITIVE`, `NO_ACTION_NEEDED`, `DUPLICATE`, `AUTOMATIC`, `QUALIFIED_MONITORS_REVIEWED`, `QUALIFIED_MONITORS_NO_ACTION_NEEDED`, `QUALIFIED_MONITORS_FALSE_POSITIVE`) | no |  |
| `status` | enum (`OPEN`, `IN_PROGRESS`, `CLOSED`) | yes |  |
| `teams` | array<[`IncidentTeamDto`](#schema-incidentteamdto)> | yes |  |
| `triggerTime` | integer (int64) | yes |  |


### `RuleRunValuesDto` {#schema-rulerunvaluesdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `actual` | number (float) | no |  |
| `expected` | [`RuleRunExpectedValuesDto`](#schema-rulerunexpectedvaluesdto) | no |  |


### `ParameterizedQueryDto` {#schema-parameterizedquerydto}

| Name | Type | Required | Description |
|---|---|---|---|
| `positionalParameters` | array<[`PositionalParameterDto`](#schema-positionalparameterdto)> | yes |  |
| `query` | string | yes |  |


### `AsCodeCustomMetadataEntryReferenceDto` {#schema-ascodecustommetadataentryreferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no |  |
| `value` | [`AsCodeCustomMetadataEntryLabelValueReferenceDto`](#schema-ascodecustommetadataentrylabelvaluereferencedto) or [`AsCodeCustomMetadataEntryStringValueReferenceDto`](#schema-ascodecustommetadataentrystringvaluereferencedto) or [`AsCodeCustomMetadataEntryTeamValueReferenceDto`](#schema-ascodecustommetadataentryteamvaluereferencedto) or [`AsCodeCustomMetadataEntryUserValueReferenceDto`](#schema-ascodecustommetadataentryuservaluereferencedto) | no |  |


### `AsCodeDynamicMetricMonitorParamsDto` {#schema-ascodedynamicmetricmonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `aggregation` | [`AsCodeAggregationClauseDtoV1`](#schema-ascodeaggregationclausedtov1) or [`AsCodeQuantileAggregationClauseDtoV1`](#schema-ascodequantileaggregationclausedtov1) | no |  |
| `field` | string | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV1`](#schema-ascodedynamicthresholddtov1) | no |  |
| `timeWindow` | [`AsCodeTimeWindowWithOffsetFrequencyAndRollingClauseDto`](#schema-ascodetimewindowwithoffsetfrequencyandrollingclausedto) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeFieldDuplicatesMonitorParamsDto` {#schema-ascodefieldduplicatesmonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `field` | array<[`AsCodeFieldReferenceDto`](#schema-ascodefieldreferencedto)> | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV2`](#schema-ascodedynamicthresholddtov2) or [`AsCodeStaticThresholdDtoV2`](#schema-ascodestaticthresholddtov2) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV2`](#schema-ascodetimewindowclausedtov2) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeSqlConditionMonitorParamsDto` {#schema-ascodesqlconditionmonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `sql` | string | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV2`](#schema-ascodedynamicthresholddtov2) or [`AsCodeStaticThresholdDtoV2`](#schema-ascodestaticthresholddtov2) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV2`](#schema-ascodetimewindowclausedtov2) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeSqlMonitorParamsDto` {#schema-ascodesqlmonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `sql` | string | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV2`](#schema-ascodedynamicthresholddtov2) or [`AsCodeStaticThresholdDtoV2`](#schema-ascodestaticthresholddtov2) | no |  |


### `AsCodeFieldInListConstraintMonitorParamsDtoV2` {#schema-ascodefieldinlistconstraintmonitorparamsdtov2}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `field` | [`AsCodeFieldReferenceDto`](#schema-ascodefieldreferencedto) | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV2`](#schema-ascodedynamicthresholddtov2) or [`AsCodeStaticThresholdDtoV2`](#schema-ascodestaticthresholddtov2) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV2`](#schema-ascodetimewindowclausedtov2) | no |  |
| `values` | array<string> | no |  |
| `whereStatement` | string | no |  |


### `AsCodeConnectionParamsOverrideDto` {#schema-ascodeconnectionparamsoverridedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `credentials` | string | yes |  |


### `AsCodeCorrelatedMetricsMonitorParamsDto` {#schema-ascodecorrelatedmetricsmonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `metadataBased` | boolean | no |  |
| `metrics` | array<[`AsCodeMetricClauseDto`](#schema-ascodemetricclausedto)> | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV2`](#schema-ascodedynamicthresholddtov2) or [`AsCodeStaticThresholdDtoV2`](#schema-ascodestaticthresholddtov2) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseWithoutFieldDtoV2`](#schema-ascodetimewindowclausewithoutfielddtov2) | no |  |


### `AsCodeReferentialIntegrityMonitorParamsDtoV1` {#schema-ascodereferentialintegritymonitorparamsdtov1}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `left` | [`AsCodeReferentialIntegrityLeftDtoV1`](#schema-ascodereferentialintegrityleftdtov1) | no |  |
| `matchType` | enum (`Full`, `LeftOnRight`, `RightOnLeft`) | no |  |
| `right` | [`AsCodeReferentialIntegrityRightDto`](#schema-ascodereferentialintegrityrightdto) | no |  |


### `AsCodeDynamicFieldProfilingMonitorParamsDto` {#schema-ascodedynamicfieldprofilingmonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `field` | array<string> | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `profiling` | [`AsCodeFieldProfilingClauseDto`](#schema-ascodefieldprofilingclausedto) or [`AsCodeNullFieldProfilingClauseDto`](#schema-ascodenullfieldprofilingclausedto) | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV1`](#schema-ascodedynamicthresholddtov1) | no |  |
| `timeWindow` | [`AsCodeTimeWindowWithOffsetFrequencyAndRollingClauseDto`](#schema-ascodetimewindowwithoffsetfrequencyandrollingclausedto) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeFieldInListConstraintMonitorParamsDtoV1` {#schema-ascodefieldinlistconstraintmonitorparamsdtov1}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `field` | string | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV1`](#schema-ascodetimewindowclausedtov1) | no |  |
| `values` | array<string> | no |  |
| `whereStatement` | string | no |  |


### `AsCodeConditionalMonitorParamsDto` {#schema-ascodeconditionalmonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `condition` | [`AsCodeConditionGroupDto`](#schema-ascodeconditiongroupdto) or [`AsCodeDateConditionDto`](#schema-ascodedateconditiondto) or [`AsCodeNumericComparisonConditionDto`](#schema-ascodenumericcomparisonconditiondto) or [`AsCodeStringConditionDto`](#schema-ascodestringconditiondto) or [`AsCodeUnaryConditionDto`](#schema-ascodeunaryconditiondto) | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV2`](#schema-ascodedynamicthresholddtov2) or [`AsCodeStaticThresholdDtoV2`](#schema-ascodestaticthresholddtov2) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV2`](#schema-ascodetimewindowclausedtov2) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeCompletenessMonitorParamsDto` {#schema-ascodecompletenessmonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV1`](#schema-ascodedynamicthresholddtov1) | no |  |
| `timeWindow` | [`AsCodeTimeWindowWithOffsetFrequencyAndRollingClauseDto`](#schema-ascodetimewindowwithoffsetfrequencyandrollingclausedto) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeFreshnessMonitorParamsDtoV1` {#schema-ascodefreshnessmonitorparamsdtov1}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `threshold` | [`AsCodeFreshnessThresholdDto`](#schema-ascodefreshnessthresholddto) or [`AsCodeDynamicFreshnessThresholdDto`](#schema-ascodedynamicfreshnessthresholddto) or [`AsCodeStaticFreshnessThresholdDto`](#schema-ascodestaticfreshnessthresholddto) | no |  |
| `timeWindow` | [`AsCodeTimeWindowWithOffsetFrequencyAndRollingClauseDto`](#schema-ascodetimewindowwithoffsetfrequencyandrollingclausedto) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeIncidentDto` {#schema-ascodeincidentdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `createOnFailure` | boolean | no |  |
| `customEmailSubject` | string | no |  |
| `message` | string | no |  |
| `severity` | enum (`Low`, `Moderate`, `High`, `Critical`) | yes |  |


### `AsCodeCustomMetricsMonitorParamsDtoV1` {#schema-ascodecustommetricsmonitorparamsdtov1}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `sql` | string | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV1`](#schema-ascodedynamicthresholddtov1) | no |  |
| `timeWindow` | [`AsCodeTimeWindowOffsetClauseDto`](#schema-ascodetimewindowoffsetclausedto) | no |  |


### `AsCodeDatasetReferenceDto` {#schema-ascodedatasetreferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `datasource` | [`AsCodeReferenceByIdOrNameDtoImpl`](#schema-ascodereferencebyidornamedtoimpl) | no |  |
| `id` | string (uuid) | no |  |
| `name` | string | no |  |
| `uri` | string | no |  |


### `AsCodeDistributionMonitorParamsDto` {#schema-ascodedistributionmonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `field` | array<[`AsCodeFieldReferenceDto`](#schema-ascodefieldreferencedto)> | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `onAddedCategory` | boolean | no |  |
| `onRemovedCategory` | boolean | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `reference` | [`AsCodeFixedDistributionReferenceDto`](#schema-ascodefixeddistributionreferencedto) or [`AsCodeRollingDistributionReferenceDto`](#schema-ascoderollingdistributionreferencedto) | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV2`](#schema-ascodedynamicthresholddtov2) or [`AsCodeStaticThresholdDtoV2`](#schema-ascodestaticthresholddtov2) | no |  |
| `timeWindow` | [`AsCodeDistributionChangeTimeWindowClauseDtoV2`](#schema-ascodedistributionchangetimewindowclausedtov2) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeStaticCompletenessMonitorParamsDto` {#schema-ascodestaticcompletenessmonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `threshold` | [`AsCodeStaticThresholdWithComparisonModeDto`](#schema-ascodestaticthresholdwithcomparisonmodedto) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV1`](#schema-ascodetimewindowclausedtov1) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeTagReferenceDto` {#schema-ascodetagreferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no |  |
| `kind` | enum (`Tag`, `Classification`) | no |  |
| `name` | string | no |  |


### `AsCodeFreshnessMonitorParamsDtoV2` {#schema-ascodefreshnessmonitorparamsdtov2}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV2`](#schema-ascodedynamicthresholddtov2) or [`AsCodeStaticThresholdDtoV2`](#schema-ascodestaticthresholddtov2) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV2`](#schema-ascodetimewindowclausedtov2) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeReferenceByIdOrNameDtoImpl` {#schema-ascodereferencebyidornamedtoimpl}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no |  |
| `name` | string | no |  |


### `AsCodeCustomMetricsMonitorParamsDtoV2` {#schema-ascodecustommetricsmonitorparamsdtov2}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `emptyMeansZero` | boolean | no |  |
| `sql` | string | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV2`](#schema-ascodedynamicthresholddtov2) or [`AsCodeStaticThresholdDtoV2`](#schema-ascodestaticthresholddtov2) | no |  |
| `timeWindow` | [`AsCodeCustomMetricsTimeWindowDto`](#schema-ascodecustommetricstimewindowdto) | no |  |


### `AsCodeMetricsMonitorParamsDto` {#schema-ascodemetricsmonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `aggregation` | [`AsCodeAggregationClauseDtoV2`](#schema-ascodeaggregationclausedtov2) or [`AsCodeCustomAggregationClauseDtoV2`](#schema-ascodecustomaggregationclausedtov2) or [`AsCodeQuantileAggregationClauseDtoV2`](#schema-ascodequantileaggregationclausedtov2) | no |  |
| `field` | [`AsCodeFieldReferenceDto`](#schema-ascodefieldreferencedto) | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV2`](#schema-ascodedynamicthresholddtov2) or [`AsCodeStaticThresholdDtoV2`](#schema-ascodestaticthresholddtov2) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV2`](#schema-ascodetimewindowclausedtov2) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeJiraNotificationDto` {#schema-ascodejiranotificationdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Slack`, `Email`, `MicrosoftTeams`, `Jira`, `ServiceNow`, `Webhook`) | yes |  |
| `issueTypeId` | integer (int64) | no |  |
| `projectKey` | string | no |  |
| `templateName` | string | no |  |


### `AsCodeSchemaChangeMonitorParamsDto` {#schema-ascodeschemachangemonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |


### `AsCodeMetadataFreshnessMonitorParamsDtoV2` {#schema-ascodemetadatafreshnessmonitorparamsdtov2}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV2`](#schema-ascodedynamicthresholddtov2) or [`AsCodeStaticThresholdDtoV2`](#schema-ascodestaticthresholddtov2) | no |  |


### `AsCodeReferentialIntegrityMonitorParamsDtoV2` {#schema-ascodereferentialintegritymonitorparamsdtov2}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `left` | [`AsCodeReferentialIntegrityLeftDtoV2`](#schema-ascodereferentialintegrityleftdtov2) | no |  |
| `matchType` | enum (`Full`, `LeftOnRight`, `RightOnLeft`) | no |  |
| `right` | [`AsCodeReferentialIntegrityRightDto`](#schema-ascodereferentialintegrityrightdto) | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV2`](#schema-ascodedynamicthresholddtov2) or [`AsCodeStaticThresholdDtoV2`](#schema-ascodestaticthresholddtov2) | no |  |


### `AsCodeValueRangeMonitorParamsDto` {#schema-ascodevaluerangemonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `field` | [`AsCodeFieldReferenceDto`](#schema-ascodefieldreferencedto) | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `range` | [`AsCodeRangeDto`](#schema-ascoderangedto) | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV2`](#schema-ascodedynamicthresholddtov2) or [`AsCodeStaticThresholdDtoV2`](#schema-ascodestaticthresholddtov2) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV2`](#schema-ascodetimewindowclausedtov2) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeServiceNowNotificationDto` {#schema-ascodeservicenownotificationdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Slack`, `Email`, `MicrosoftTeams`, `Jira`, `ServiceNow`, `Webhook`) | yes |  |
| `templateName` | string | no |  |


### `AsCodeRowDuplicatesMonitorParamsDto` {#schema-ascoderowduplicatesmonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV2`](#schema-ascodedynamicthresholddtov2) or [`AsCodeStaticThresholdDtoV2`](#schema-ascodestaticthresholddtov2) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV2`](#schema-ascodetimewindowclausedtov2) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeDuplicatesMonitorParamsDto` {#schema-ascodeduplicatesmonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV1`](#schema-ascodedynamicthresholddtov1) | no |  |
| `timeWindow` | [`AsCodeTimeWindowWithOffsetAndFrequencyClauseDto`](#schema-ascodetimewindowwithoffsetandfrequencyclausedto) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeFieldUniquenessMonitorParamsDto` {#schema-ascodefielduniquenessmonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `field` | array<string> | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV1`](#schema-ascodetimewindowclausedtov1) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeFieldNullsMonitorParamsDto` {#schema-ascodefieldnullsmonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `field` | [`AsCodeFieldReferenceDto`](#schema-ascodefieldreferencedto) | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `nullValues` | enum (`Null`, `NullAndEmpty`, `NullEmptyAndWhitespaces`) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV2`](#schema-ascodedynamicthresholddtov2) or [`AsCodeStaticThresholdDtoV2`](#schema-ascodestaticthresholddtov2) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV2`](#schema-ascodetimewindowclausedtov2) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeAlertingHookNotificationDto` {#schema-ascodealertinghooknotificationdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Slack`, `Email`, `MicrosoftTeams`, `Jira`, `ServiceNow`, `Webhook`) | yes |  |
| `id` | string (uuid) | no |  |
| `name` | string | no |  |


### `AsCodeVolumeMonitorParamsDto` {#schema-ascodevolumemonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `metadataBased` | boolean | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV2`](#schema-ascodedynamicthresholddtov2) or [`AsCodeStaticThresholdDtoV2`](#schema-ascodestaticthresholddtov2) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV2`](#schema-ascodetimewindowclausedtov2) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeJoinDto` {#schema-ascodejoindto}

| Name | Type | Required | Description |
|---|---|---|---|
| `dataset` | [`AsCodeDatasetReferenceDto`](#schema-ascodedatasetreferencedto) | yes |  |
| `joinCondition` | [`AsCodeEqualityJoinConditionDto`](#schema-ascodeequalityjoinconditiondto) | yes |  |
| `joinType` | enum (`Inner`, `Left`, `Right`, `Outer`) | yes |  |


### `AsCodeStaticFieldProfilingMonitorParamsDto` {#schema-ascodestaticfieldprofilingmonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `field` | array<string> | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `profiling` | [`AsCodeFieldProfilingClauseDto`](#schema-ascodefieldprofilingclausedto) or [`AsCodeNullFieldProfilingClauseDto`](#schema-ascodenullfieldprofilingclausedto) | no |  |
| `threshold` | [`AsCodeStaticFieldProfilingThresholdDto`](#schema-ascodestaticfieldprofilingthresholddto) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV1`](#schema-ascodetimewindowclausedtov1) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeMetadataFreshnessMonitorParamsDtoV1` {#schema-ascodemetadatafreshnessmonitorparamsdtov1}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `threshold` | [`AsCodeDynamicFreshnessThresholdDto`](#schema-ascodedynamicfreshnessthresholddto) | no |  |


### `AsCodeFieldFormatMonitorParamsDtoV2` {#schema-ascodefieldformatmonitorparamsdtov2}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `field` | [`AsCodeFieldReferenceDto`](#schema-ascodefieldreferencedto) | no |  |
| `format` | [`AsCodeFieldFormatValidationClauseDto`](#schema-ascodefieldformatvalidationclausedto) or [`AsCodeRegexFieldFormatValidationClauseDto`](#schema-ascoderegexfieldformatvalidationclausedto) | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `threshold` | [`AsCodeDynamicThresholdDtoV2`](#schema-ascodedynamicthresholddtov2) or [`AsCodeStaticThresholdDtoV2`](#schema-ascodestaticthresholddtov2) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV2`](#schema-ascodetimewindowclausedtov2) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeStaticMetricMonitorParamsDto` {#schema-ascodestaticmetricmonitorparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `aggregation` | [`AsCodeAggregationClauseDtoV1`](#schema-ascodeaggregationclausedtov1) or [`AsCodeQuantileAggregationClauseDtoV1`](#schema-ascodequantileaggregationclausedtov1) | no |  |
| `field` | string | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `threshold` | [`AsCodeStaticThresholdDtoV1`](#schema-ascodestaticthresholddtov1) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV1`](#schema-ascodetimewindowclausedtov1) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeFieldFormatMonitorParamsDtoV1` {#schema-ascodefieldformatmonitorparamsdtov1}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Metrics`, `Freshness`, `RowDuplicates`, `FieldUniqueness`, `SchemaChange`, `Sql`, `Conditional`, `SqlCondition`, `CorrelatedMetrics`, `Distribution`, `CustomMetrics`, `FieldFormat`, … 14 more — full list in `openapi.json`) | no |  |
| `field` | string | no |  |
| `format` | [`AsCodeFieldFormatValidationClauseDto`](#schema-ascodefieldformatvalidationclausedto) or [`AsCodeRegexFieldFormatValidationClauseDto`](#schema-ascoderegexfieldformatvalidationclausedto) | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV1`](#schema-ascodetimewindowclausedtov1) | no |  |
| `whereStatement` | string | no |  |


### `CatalogFilterDto` {#schema-catalogfilterdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `children` | array<[`FilterElementDto`](#schema-filterelementdto)> | no |  |
| `id` | string | no |  |
| `name` | string | no |  |
| `query` | string | no |  |


### `SearchCollectionRuleCatalogAssetDto` {#schema-searchcollectionrulecatalogassetdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `data` | array<[`RuleCatalogAssetDto`](#schema-rulecatalogassetdto)> | yes |  |
| `totalElements` | integer (int64) | no |  |


### `GenericProviderDto` {#schema-genericproviderdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`GENERIC`, `DATASOURCE`, `USER`, `ACCESS_TOKEN`) | no |  |
| `createdBy` | string | no |  |


### `UserProviderDto` {#schema-userproviderdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`GENERIC`, `DATASOURCE`, `USER`, `ACCESS_TOKEN`) | no |  |
| `name` | string | no |  |


### `DatasourceProviderDto` {#schema-datasourceproviderdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`GENERIC`, `DATASOURCE`, `USER`, `ACCESS_TOKEN`) | no |  |
| `id` | string (uuid) | no |  |
| `name` | string | no |  |


### `AccessTokenProviderDto` {#schema-accesstokenproviderdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`GENERIC`, `DATASOURCE`, `USER`, `ACCESS_TOKEN`) | no |  |
| `name` | string | no |  |


### `JsonNode` {#schema-jsonnode}

_No fields._


### `EntityCustomMetadataEntryStringDto` {#schema-entitycustommetadataentrystringdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | yes |  |
| `type` | enum (`LABEL`, `USER`, `STRING`, `TEAM`) | yes |  |
| `value` | string | no |  |


### `EntityCustomMetadataEntryLabelDto` {#schema-entitycustommetadataentrylabeldto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | yes |  |
| `type` | enum (`LABEL`, `USER`, `STRING`, `TEAM`) | yes |  |
| `value` | string | no |  |


### `EntityCustomMetadataEntryTeamDto` {#schema-entitycustommetadataentryteamdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | yes |  |
| `type` | enum (`LABEL`, `USER`, `STRING`, `TEAM`) | yes |  |
| `name` | string | no |  |
| `teamId` | string (uuid) | no |  |


### `EntityCustomMetadataEntryUserDto` {#schema-entitycustommetadataentryuserdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | yes |  |
| `type` | enum (`LABEL`, `USER`, `STRING`, `TEAM`) | yes |  |
| `login` | string | no |  |
| `name` | string | no |  |
| `userId` | string (uuid) | no |  |


### `DefaultWebhookParams` {#schema-defaultwebhookparams}

| Name | Type | Required | Description |
|---|---|---|---|
| `scope` | enum (`ALL_EVENTS`, `LINKED_EVENTS`) | yes |  |
| `type` | enum (`DEFAULT`, `GOOGLE_CHAT`) | yes |  |
| `headers` | array<[`CustomHeader`](#schema-customheader)> | no |  |


### `GoogleChatWebhookParams` {#schema-googlechatwebhookparams}

| Name | Type | Required | Description |
|---|---|---|---|
| `scope` | enum (`ALL_EVENTS`, `LINKED_EVENTS`) | yes |  |
| `type` | enum (`DEFAULT`, `GOOGLE_CHAT`) | yes |  |


### `UserDto` {#schema-userdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no |  |
| `login` | string | no |  |
| `name` | string | no |  |


### `GetCollaborationToolItemDto` {#schema-getcollaborationtoolitemdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no |  |
| `itemKey` | string | yes |  |
| `itemUrl` | string | no |  |
| `type` | enum (`JIRA`, `SERVICENOW`) | yes |  |


### `IncidentTeamDto` {#schema-incidentteamdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | yes |  |
| `name` | string | yes |  |


### `RuleRunExpectedValuesDto` {#schema-rulerunexpectedvaluesdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `max` | number (float) | no |  |
| `min` | number (float) | no |  |


### `PositionalParameterDto` {#schema-positionalparameterdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `value` | object | no |  |


### `AsCodeCustomMetadataEntryUserValueReferenceDto` {#schema-ascodecustommetadataentryuservaluereferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `customMetadataName` | string | no |  |
| `kind` | enum (`Label`, `String`, `User`, `Team`) | yes |  |
| `email` | string | no |  |


### `AsCodeCustomMetadataEntryTeamValueReferenceDto` {#schema-ascodecustommetadataentryteamvaluereferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `customMetadataName` | string | no |  |
| `kind` | enum (`Label`, `String`, `User`, `Team`) | yes |  |
| `name` | string | no |  |


### `AsCodeCustomMetadataEntryLabelValueReferenceDto` {#schema-ascodecustommetadataentrylabelvaluereferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `customMetadataName` | string | no |  |
| `kind` | enum (`Label`, `String`, `User`, `Team`) | yes |  |
| `labelValue` | string | no |  |


### `AsCodeCustomMetadataEntryStringValueReferenceDto` {#schema-ascodecustommetadataentrystringvaluereferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `customMetadataName` | string | no |  |
| `kind` | enum (`Label`, `String`, `User`, `Team`) | yes |  |
| `stringValue` | string | no |  |


### `AsCodeGroupByClauseDto` {#schema-ascodegroupbyclausedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `field` | array<[`AsCodeFieldReferenceDto`](#schema-ascodefieldreferencedto)> | yes |  |


### `AsCodeIntegerRangePartitionClauseDto` {#schema-ascodeintegerrangepartitionclausedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`IngestionTime`, `IntegerRange`, `TimeUnitColumn`) | no |  |
| `field` | [`AsCodeFieldReferenceDto`](#schema-ascodefieldreferencedto) | no |  |
| `max` | integer (int32) | no |  |
| `min` | integer (int32) | no |  |


### `AsCodeTimeWindowWithOffsetFrequencyAndRollingClauseDto` {#schema-ascodetimewindowwithoffsetfrequencyandrollingclausedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `deltaQuerying` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `disableDeltaQuerying` | boolean | no |  |
| `duration` | [`SimpleDuration`](#schema-simpleduration) | yes |  |
| `field` | string | yes |  |
| `frequency` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `offset` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `rollingTimeWindow` | [`SimpleDuration`](#schema-simpleduration) | no |  |


### `AsCodeQuantileAggregationClauseDtoV1` {#schema-ascodequantileaggregationclausedtov1}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Average`, `NormalizedAverage`, `Count`, `DistinctCount`, `Sum`, `Max`, `Min`, `Quantile`, `Range`, `StandardDeviation`, `Variance`) | yes |  |
| `quantile` | number (float) | no |  |


### `AsCodeDynamicThresholdDtoV1` {#schema-ascodedynamicthresholddtov1}

| Name | Type | Required | Description |
|---|---|---|---|
| `bounds` | enum (`MinAndMax`, `Min`, `Max`) | no |  |
| `excludedDates` | array<[`AsCodeCalendarReferenceDto`](#schema-ascodecalendarreferencedto)> | no |  |
| `sensitivity` | integer (int32) | no |  |


### `AsCodeIngestionTimePartitionClauseDto` {#schema-ascodeingestiontimepartitionclausedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`IngestionTime`, `IntegerRange`, `TimeUnitColumn`) | no |  |
| `interval` | [`SimpleDuration`](#schema-simpleduration) | no |  |


### `AsCodeAggregationClauseDtoV1` {#schema-ascodeaggregationclausedtov1}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Average`, `NormalizedAverage`, `Count`, `DistinctCount`, `Sum`, `Max`, `Min`, `Quantile`, `Range`, `StandardDeviation`, `Variance`) | yes |  |


### `AsCodeTimeUnitColumnPartitionClauseDto` {#schema-ascodetimeunitcolumnpartitionclausedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`IngestionTime`, `IntegerRange`, `TimeUnitColumn`) | no |  |
| `field` | [`AsCodeFieldReferenceDto`](#schema-ascodefieldreferencedto) | no |  |
| `interval` | [`SimpleDuration`](#schema-simpleduration) | no |  |


### `AsCodeStaticThresholdDtoV2` {#schema-ascodestaticthresholddtov2}

| Name | Type | Required | Description |
|---|---|---|---|
| `excludedDates` | array<[`AsCodeCalendarReferenceDto`](#schema-ascodecalendarreferencedto)> | no |  |
| `kind` | enum (`Static`, `Dynamic`) | yes |  |
| `valueMode` | enum (`Count`, `Percentage`) | no |  |
| `comparisonMode` | enum (`Absolute`, `Relative`, `RelativePercentage`) | no |  |
| `isMaxInclusive` | boolean | no |  |
| `isMinInclusive` | boolean | no |  |
| `max` | [`NumberOrPercentageDto`](#schema-numberorpercentagedto) | no |  |
| `min` | [`NumberOrPercentageDto`](#schema-numberorpercentagedto) | no |  |


### `AsCodeDynamicThresholdDtoV2` {#schema-ascodedynamicthresholddtov2}

| Name | Type | Required | Description |
|---|---|---|---|
| `excludedDates` | array<[`AsCodeCalendarReferenceDto`](#schema-ascodecalendarreferencedto)> | no |  |
| `kind` | enum (`Static`, `Dynamic`) | yes |  |
| `valueMode` | enum (`Count`, `Percentage`) | no |  |
| `bounds` | enum (`MinAndMax`, `Min`, `Max`) | no |  |
| `sensitivity` | integer (int32) | no |  |


### `AsCodeFieldReferenceDto` {#schema-ascodefieldreferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `dataset` | [`AsCodeDatasetReferenceDto`](#schema-ascodedatasetreferencedto) | no |  |
| `name` | string | yes |  |


### `AsCodeTimeWindowClauseDtoV2` {#schema-ascodetimewindowclausedtov2}

| Name | Type | Required | Description |
|---|---|---|---|
| `deltaQuerying` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `field` | [`AsCodeFieldReferenceDto`](#schema-ascodefieldreferencedto) | yes |  |
| `firstRun` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `frequency` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `offset` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `offsetPeriods` | integer (int32) | no |  |
| `rollingTimeWindow` | [`SimpleDuration`](#schema-simpleduration) | no |  |


### `AsCodeMetricClauseDto` {#schema-ascodemetricclausedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `aggregation` | [`AsCodeAggregationClauseDtoV2`](#schema-ascodeaggregationclausedtov2) or [`AsCodeCustomAggregationClauseDtoV2`](#schema-ascodecustomaggregationclausedtov2) or [`AsCodeQuantileAggregationClauseDtoV2`](#schema-ascodequantileaggregationclausedtov2) | yes |  |
| `field` | string | no |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `name` | string | yes |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `timeWindowField` | string | no |  |
| `whereStatement` | string | no |  |


### `AsCodeTimeWindowClauseWithoutFieldDtoV2` {#schema-ascodetimewindowclausewithoutfielddtov2}

| Name | Type | Required | Description |
|---|---|---|---|
| `deltaQuerying` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `firstRun` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `frequency` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `offset` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `offsetPeriods` | integer (int32) | no |  |
| `rollingTimeWindow` | [`SimpleDuration`](#schema-simpleduration) | no |  |


### `AsCodeReferentialIntegrityLeftDtoV1` {#schema-ascodereferentialintegrityleftdtov1}

| Name | Type | Required | Description |
|---|---|---|---|
| `field` | array<string> | yes |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `timeWindow` | [`AsCodeTimeWindowWithOffsetAndFrequencyClauseDto`](#schema-ascodetimewindowwithoffsetandfrequencyclausedto) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeReferentialIntegrityRightDto` {#schema-ascodereferentialintegrityrightdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `field` | array<string> | yes |  |
| `whereStatement` | string | no |  |


### `AsCodeFieldProfilingClauseDto` {#schema-ascodefieldprofilingclausedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`DuplicatePercentage`, `DuplicateCount`, `NullPercentage`, `NullCount`) | yes |  |


### `AsCodeNullFieldProfilingClauseDto` {#schema-ascodenullfieldprofilingclausedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`DuplicatePercentage`, `DuplicateCount`, `NullPercentage`, `NullCount`) | yes |  |
| `nullValues` | enum (`Null`, `NullAndEmpty`, `NullEmptyAndWhitespaces`) | no |  |


### `AsCodeTimeWindowClauseDtoV1` {#schema-ascodetimewindowclausedtov1}

| Name | Type | Required | Description |
|---|---|---|---|
| `duration` | [`SimpleDuration`](#schema-simpleduration) | yes |  |
| `field` | string | yes |  |


### `AsCodeConditionGroupDto` {#schema-ascodeconditiongroupdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`andGroup`, `orGroup`, `equals`, `notEquals`, `greaterThan`, `greaterThanOrEquals`, `lessThan`, `lessThanOrEquals`, `isNull`, `isNotNull`, `contains`, `notContains`, … 4 more — full list in `openapi.json`) | yes |  |
| `conditions` | array<[`AsCodeConditionGroupDto`](#schema-ascodeconditiongroupdto) or [`AsCodeDateConditionDto`](#schema-ascodedateconditiondto) or [`AsCodeNumericComparisonConditionDto`](#schema-ascodenumericcomparisonconditiondto) or [`AsCodeStringConditionDto`](#schema-ascodestringconditiondto) or [`AsCodeUnaryConditionDto`](#schema-ascodeunaryconditiondto)> | no |  |


### `AsCodeUnaryConditionDto` {#schema-ascodeunaryconditiondto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`andGroup`, `orGroup`, `equals`, `notEquals`, `greaterThan`, `greaterThanOrEquals`, `lessThan`, `lessThanOrEquals`, `isNull`, `isNotNull`, `contains`, `notContains`, … 4 more — full list in `openapi.json`) | yes |  |
| `expression` | [`AsCodeFieldExpressionDto`](#schema-ascodefieldexpressiondto) | no |  |


### `AsCodeNumericComparisonConditionDto` {#schema-ascodenumericcomparisonconditiondto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`andGroup`, `orGroup`, `equals`, `notEquals`, `greaterThan`, `greaterThanOrEquals`, `lessThan`, `lessThanOrEquals`, `isNull`, `isNotNull`, `contains`, `notContains`, … 4 more — full list in `openapi.json`) | yes |  |
| `leftExpression` | [`AsCodeFieldExpressionDto`](#schema-ascodefieldexpressiondto) | no |  |
| `rightExpression` | [`AsCodeFieldExpressionDto`](#schema-ascodefieldexpressiondto) or [`AsCodeValueExpressionDto`](#schema-ascodevalueexpressiondto) | no |  |


### `AsCodeStringConditionDto` {#schema-ascodestringconditiondto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`andGroup`, `orGroup`, `equals`, `notEquals`, `greaterThan`, `greaterThanOrEquals`, `lessThan`, `lessThanOrEquals`, `isNull`, `isNotNull`, `contains`, `notContains`, … 4 more — full list in `openapi.json`) | yes |  |
| `leftExpression` | [`AsCodeFieldExpressionDto`](#schema-ascodefieldexpressiondto) | no |  |
| `rightExpression` | [`AsCodeFieldExpressionDto`](#schema-ascodefieldexpressiondto) or [`AsCodeValueExpressionDto`](#schema-ascodevalueexpressiondto) | no |  |


### `AsCodeDateConditionDto` {#schema-ascodedateconditiondto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`andGroup`, `orGroup`, `equals`, `notEquals`, `greaterThan`, `greaterThanOrEquals`, `lessThan`, `lessThanOrEquals`, `isNull`, `isNotNull`, `contains`, `notContains`, … 4 more — full list in `openapi.json`) | yes |  |
| `dateExpression` | [`AsCodeFieldExpressionDto`](#schema-ascodefieldexpressiondto) | no |  |
| `duration` | [`AsCodeDurationDto`](#schema-ascodedurationdto) | no |  |


### `AsCodeFreshnessThresholdDto` {#schema-ascodefreshnessthresholddto}

| Name | Type | Required | Description |
|---|---|---|---|
| `excludedDates` | array<[`AsCodeCalendarReferenceDto`](#schema-ascodecalendarreferencedto)> | no |  |
| `kind` | enum (`Dynamic`, `Static`) | yes |  |


### `AsCodeDynamicFreshnessThresholdDto` {#schema-ascodedynamicfreshnessthresholddto}

| Name | Type | Required | Description |
|---|---|---|---|
| `excludedDates` | array<[`AsCodeCalendarReferenceDto`](#schema-ascodecalendarreferencedto)> | no |  |
| `kind` | enum (`Dynamic`, `Static`) | yes |  |
| `sensitivity` | integer (int32) | no |  |


### `AsCodeStaticFreshnessThresholdDto` {#schema-ascodestaticfreshnessthresholddto}

| Name | Type | Required | Description |
|---|---|---|---|
| `excludedDates` | array<[`AsCodeCalendarReferenceDto`](#schema-ascodecalendarreferencedto)> | no |  |
| `kind` | enum (`Dynamic`, `Static`) | yes |  |


### `AsCodeTimeWindowOffsetClauseDto` {#schema-ascodetimewindowoffsetclausedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `offset` | [`SimpleDuration`](#schema-simpleduration) | no |  |


### `AsCodeRollingDistributionReferenceDto` {#schema-ascoderollingdistributionreferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Rolling`, `Fixed`) | yes |  |
| `delay` | [`SimpleDuration`](#schema-simpleduration) | no |  |


### `AsCodeDistributionChangeTimeWindowClauseDtoV2` {#schema-ascodedistributionchangetimewindowclausedtov2}

| Name | Type | Required | Description |
|---|---|---|---|
| `deltaQuerying` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `duration` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `field` | [`AsCodeFieldReferenceDto`](#schema-ascodefieldreferencedto) | yes |  |
| `firstRun` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `frequency` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `offset` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `offsetPeriods` | integer (int32) | no |  |
| `rollingTimeWindow` | [`SimpleDuration`](#schema-simpleduration) | no |  |


### `AsCodeFixedDistributionReferenceDto` {#schema-ascodefixeddistributionreferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Rolling`, `Fixed`) | yes |  |
| `timestamp` | string | no |  |


### `AsCodeStaticThresholdWithComparisonModeDto` {#schema-ascodestaticthresholdwithcomparisonmodedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `comparisonMode` | enum (`Absolute`, `Difference`, `PercentageDifference`) | no |  |
| `excludedDates` | array<[`AsCodeCalendarReferenceDto`](#schema-ascodecalendarreferencedto)> | no |  |
| `isMaxInclusive` | boolean | no |  |
| `isMinInclusive` | boolean | no |  |
| `max` | [`NumberOrPercentageDto`](#schema-numberorpercentagedto) | no |  |
| `min` | [`NumberOrPercentageDto`](#schema-numberorpercentagedto) | no |  |


### `AsCodeCustomMetricsTimeWindowDto` {#schema-ascodecustommetricstimewindowdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `offset` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `offsetPeriods` | integer (int32) | no |  |


### `AsCodeAggregationClauseDtoV2` {#schema-ascodeaggregationclausedtov2}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Average`, `NormalizedAverage`, `Count`, `CountAllRows`, `DistinctCount`, `Sum`, `Max`, `Min`, `Quantile`, `StandardDeviation`, `Variance`, `CustomAggregation`) | yes |  |


### `AsCodeCustomAggregationClauseDtoV2` {#schema-ascodecustomaggregationclausedtov2}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Average`, `NormalizedAverage`, `Count`, `CountAllRows`, `DistinctCount`, `Sum`, `Max`, `Min`, `Quantile`, `StandardDeviation`, `Variance`, `CustomAggregation`) | yes |  |
| `sql` | string | no |  |


### `AsCodeQuantileAggregationClauseDtoV2` {#schema-ascodequantileaggregationclausedtov2}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Average`, `NormalizedAverage`, `Count`, `CountAllRows`, `DistinctCount`, `Sum`, `Max`, `Min`, `Quantile`, `StandardDeviation`, `Variance`, `CustomAggregation`) | yes |  |
| `quantile` | number (float) | no |  |


### `AsCodeReferentialIntegrityLeftDtoV2` {#schema-ascodereferentialintegrityleftdtov2}

| Name | Type | Required | Description |
|---|---|---|---|
| `field` | array<string> | yes |  |
| `groupBy` | [`AsCodeGroupByClauseDto`](#schema-ascodegroupbyclausedto) | no |  |
| `partition` | [`AsCodeIngestionTimePartitionClauseDto`](#schema-ascodeingestiontimepartitionclausedto) or [`AsCodeIntegerRangePartitionClauseDto`](#schema-ascodeintegerrangepartitionclausedto) or [`AsCodeTimeUnitColumnPartitionClauseDto`](#schema-ascodetimeunitcolumnpartitionclausedto) | no |  |
| `timeWindow` | [`AsCodeTimeWindowClauseDtoV2`](#schema-ascodetimewindowclausedtov2) | no |  |
| `whereStatement` | string | no |  |


### `AsCodeRangeDto` {#schema-ascoderangedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `isMaxInclusive` | boolean | no |  |
| `isMinInclusive` | boolean | no |  |
| `max` | [`NumberDto`](#schema-numberdto) | no |  |
| `min` | [`NumberDto`](#schema-numberdto) | no |  |


### `AsCodeTimeWindowWithOffsetAndFrequencyClauseDto` {#schema-ascodetimewindowwithoffsetandfrequencyclausedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `deltaQuerying` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `disableDeltaQuerying` | boolean | no |  |
| `duration` | [`SimpleDuration`](#schema-simpleduration) | yes |  |
| `field` | string | yes |  |
| `frequency` | [`SimpleDuration`](#schema-simpleduration) | no |  |
| `offset` | [`SimpleDuration`](#schema-simpleduration) | no |  |


### `AsCodeEqualityJoinConditionDto` {#schema-ascodeequalityjoinconditiondto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Equality`) | yes |  |
| `fieldPairs` | array<[`AsCodeJoinFieldPairDto`](#schema-ascodejoinfieldpairdto)> | no |  |


### `AsCodeStaticFieldProfilingThresholdDto` {#schema-ascodestaticfieldprofilingthresholddto}

| Name | Type | Required | Description |
|---|---|---|---|
| `excludedDates` | array<[`AsCodeCalendarReferenceDto`](#schema-ascodecalendarreferencedto)> | no |  |
| `max` | [`NumberOrPercentageDto`](#schema-numberorpercentagedto) | yes |  |


### `AsCodeFieldFormatValidationClauseDto` {#schema-ascodefieldformatvalidationclausedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Email`, `Phone`, `UUID`, `Regex`) | yes |  |


### `AsCodeRegexFieldFormatValidationClauseDto` {#schema-ascoderegexfieldformatvalidationclausedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`Email`, `Phone`, `UUID`, `Regex`) | yes |  |
| `regex` | string | no |  |


### `AsCodeStaticThresholdDtoV1` {#schema-ascodestaticthresholddtov1}

| Name | Type | Required | Description |
|---|---|---|---|
| `excludedDates` | array<[`AsCodeCalendarReferenceDto`](#schema-ascodecalendarreferencedto)> | no |  |
| `isMaxInclusive` | boolean | no |  |
| `isMinInclusive` | boolean | no |  |
| `max` | [`NumberOrPercentageDto`](#schema-numberorpercentagedto) | no |  |
| `min` | [`NumberOrPercentageDto`](#schema-numberorpercentagedto) | no |  |


### `FilterElementDto` {#schema-filterelementdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | no |  |
| `name` | string | yes |  |
| `results` | integer (int32) | no |  |


### `RuleCatalogAssetDto` {#schema-rulecatalogassetdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `canManuallyRun` | boolean | yes |  |
| `createdBy` | [`UserDto`](#schema-userdto) | no |  |
| `criticality` | integer (int32) | yes |  |
| `datasetFieldNames` | array<string> | yes |  |
| `datasets` | array<[`DatasetBriefWithUriDto`](#schema-datasetbriefwithuridto)> | yes |  |
| `description` | string | no |  |
| `hasAiRecommendations` | boolean | yes |  |
| `id` | string (uuid) | yes |  |
| `lastRunId` | string (uuid) | no |  |
| `lastRunStatus` | [`LastRunStatusDto`](#schema-lastrunstatusdto) | no |  |
| `lastWeekStatuses` | array<[`LastRunStatusDto`](#schema-lastrunstatusdto)> | yes |  |
| `mails` | array<[`AlertingHookDto`](#schema-alertinghookdto)> | yes |  |
| `msTeams` | array<[`AlertingHookDto`](#schema-alertinghookdto)> | yes |  |
| `multiDimensional` | boolean | yes |  |
| `name` | string | yes |  |
| `provider` | [`AccessTokenProviderDto`](#schema-accesstokenproviderdto) or [`DatasourceProviderDto`](#schema-datasourceproviderdto) or [`GenericProviderDto`](#schema-genericproviderdto) or [`UserProviderDto`](#schema-userproviderdto) | no |  |
| `readOnly` | boolean | yes |  |
| `ruleLabel` | string | no |  |
| `ruleStatus` | [`RuleStatusDto`](#schema-rulestatusdto) | yes |  |
| `ruleType` | enum (`AUTOMATIC_RULE`, `CUSTOM_RULE`, `SIFFLET_RULE`) | yes |  |
| `schedule` | string | no |  |
| `selectable` | boolean | yes |  |
| `slackChannels` | array<[`AlertingHookDto`](#schema-alertinghookdto)> | yes |  |
| `sourcePlatform` | enum (`SIFFLET`, `DBT`) | yes |  |
| `supportAsCodeYAMLConversion` | boolean | yes |  |
| `tags` | array<[`TagDto`](#schema-tagdto)> | yes |  |
| `terms` | array<[`TagDto`](#schema-tagdto)> | yes |  |


### `CustomHeader` {#schema-customheader}

| Name | Type | Required | Description |
|---|---|---|---|
| `key` | string | no |  |
| `value` | string | no |  |


### `SimpleDuration` {#schema-simpleduration}

| Name | Type | Required | Description |
|---|---|---|---|
| `unit` | enum (`SECONDS`, `MINUTES`, `HOURS`, `DAYS`, `WEEKS`, `MONTHS`, `YEARS`) | no |  |
| `value` | integer (int32) | no |  |


### `AsCodeCalendarReferenceDto` {#schema-ascodecalendarreferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no |  |
| `name` | string | no |  |
| `standardCalendar` | enum (`US_PUBLIC_HOLIDAYS`, `FRANCE_PUBLIC_HOLIDAYS`, `UK_PUBLIC_HOLIDAYS`, `BELGIUM_PUBLIC_HOLIDAYS`, `SPAIN_PUBLIC_HOLIDAYS`, `GERMANY_PUBLIC_HOLIDAYS`, `NETHERLANDS_PUBLIC_HOLIDAYS`, `SUNDAYS`, `WEEKENDS`) | no |  |


### `NumberOrPercentageDto` {#schema-numberorpercentagedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `floatValue` | number (float) | no |  |
| `integer` | boolean | no |  |
| `integerValue` | integer (int32) | no |  |
| `percentage` | boolean | no |  |
| `zero` | boolean | no |  |


### `AsCodeFieldExpressionDto` {#schema-ascodefieldexpressiondto}

| Name | Type | Required | Description |
|---|---|---|---|
| `field` | [`AsCodeFieldReferenceDto`](#schema-ascodefieldreferencedto) | yes |  |
| `kind` | enum (`field`, `value`) | yes |  |


### `AsCodeValueExpressionDto` {#schema-ascodevalueexpressiondto}

| Name | Type | Required | Description |
|---|---|---|---|
| `kind` | enum (`field`, `value`) | yes |  |
| `value` | string | no |  |


### `AsCodeDurationDto` {#schema-ascodedurationdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `timeUnit` | enum (`days`, `hours`, `minutes`) | yes |  |
| `value` | integer (int32) | yes |  |


### `NumberDto` {#schema-numberdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `floatValue` | number (float) | no |  |
| `integer` | boolean | no |  |
| `integerValue` | integer (int32) | no |  |
| `zero` | boolean | no |  |


### `AsCodeJoinFieldPairDto` {#schema-ascodejoinfieldpairdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `leftField` | [`AsCodeFieldReferenceDto`](#schema-ascodefieldreferencedto) | yes |  |
| `rightField` | [`AsCodeFieldReferenceDto`](#schema-ascodefieldreferencedto) | yes |  |


### `DatasetBriefWithUriDto` {#schema-datasetbriefwithuridto}

| Name | Type | Required | Description |
|---|---|---|---|
| `datasourceName` | string | yes |  |
| `datasourceType` | string | yes |  |
| `id` | string (uuid) | yes |  |
| `name` | string | yes |  |
| `qualifiedName` | string | no |  |
| `uri` | string | no |  |
| `urn` | string | yes |  |


### `LastRunStatusDto` {#schema-lastrunstatusdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `result` | string | no |  |
| `status` | enum (`PENDING`, `RUNNING`, `SUCCESS`, `REQUIRES_YOUR_ATTENTION`, `TECHNICAL_ERROR`, `FAILED`) | yes |  |
| `timestamp` | integer (int64) | yes |  |


### `RuleStatusDto` {#schema-rulestatusdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `latestRunDate` | integer (int64) | no |  |
| `ruleStatus` | enum (`NOT_EVALUATED`, `PASSING`, `NEEDS_ATTENTION`, `FAILING`) | yes |  |

