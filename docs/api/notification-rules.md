# Notification Rules

Rules that route monitor/incident notifications.

[← Back to API index](README.md)

## `GET /v1/notification-rules`

**Get list of notification rules**

- **operationId**: `publicGetNotificationRules`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `domainId (query)` | string (uuid) | no | Domain of the notification rules |
| `page (query)` | integer (int32) | no | The page number to retrieve. Starts at 0. |
| `itemsPerPage (query)` | integer (int32) | no | The number of elements to be returned inside the page. |

**Response**

- `200` — Notification Rules retrieved: [`PublicPageDtoPublicGetNotificationRuleDto`](#schema-publicpagedtopublicgetnotificationruledto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/notification-rules" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "data": [
    {
      "ticketingDestinations": [
        "..."
      ],
      "name": "string",
      "domainId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "scope": {
        "monitorScope": "...",
        "assetScope": "..."
      },
      "notificationDestinations": [
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
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `POST /v1/notification-rules`

**Create a notification rule**

- **operationId**: `publicCreateNotificationRule`

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no | Description of the notification rule |
| `domainId` | string (uuid) | yes | Domain of the notification rule |
| `name` | string | yes | Name of the notification rule |
| `notificationDestinations` | array<[`PublicMailNotificationDestinationReferenceDto`](#schema-publicmailnotificationdestinationreferencedto) or [`PublicMsTeamsNotificationDestinationReferenceDto`](#schema-publicmsteamsnotificationdestinationreferencedto) or [`PublicSlackNotificationDestinationReferenceDto`](#schema-publicslacknotificationdestinationreferencedto) or [`PublicWebhookNotificationDestinationReferenceDto`](#schema-publicwebhooknotificationdestinationreferencedto)> | no | Notification destination of the notification rule, like Slack or emails |
| `scope` | [`PublicNotificationRuleScopeDto`](#schema-publicnotificationrulescopedto) | yes | Definition of the monitors bound to the notification rule |
| `ticketingDestinations` | array<[`PublicJiraTicketingDestinationParamsDto`](#schema-publicjiraticketingdestinationparamsdto) or [`PublicServiceNowTicketingDestinationParamsDto`](#schema-publicservicenowticketingdestinationparamsdto)> | no | Ticketing destination of the notification rule, like Jira or ServiceNow |

**Response**

- `201` — Notification Rule created: [`PublicGetNotificationRuleDto`](#schema-publicgetnotificationruledto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v1/notification-rules" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "domainId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "name": "string",
  "scope": {
    "monitorScope": {},
    "assetScope": {}
  }
}'
```

Example `201` response:

```json
{
  "ticketingDestinations": [
    {}
  ],
  "name": "string",
  "domainId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "scope": {
    "monitorScope": {},
    "assetScope": {}
  },
  "notificationDestinations": [
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
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `DELETE /v1/notification-rules/{id}`

**Delete a notification rule**

- **operationId**: `publicDeleteNotificationRule`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `204` — Notification Rule deleted (no body)

**Example call**

```bash
curl -X DELETE \
  "https://{tenant}.siffletdata.com/api/v1/notification-rules/{id}" \
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

## `GET /v1/notification-rules/{id}`

**Get a notification rule by id**

- **operationId**: `publicGetNotificationRule`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `200` — Notification Rule retrieved: [`PublicGetNotificationRuleDto`](#schema-publicgetnotificationruledto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/notification-rules/{id}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "ticketingDestinations": [
    {}
  ],
  "name": "string",
  "domainId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "scope": {
    "monitorScope": {},
    "assetScope": {}
  },
  "notificationDestinations": [
    {}
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

## `PATCH /v1/notification-rules/{id}`

**Update a notification rule**

- **operationId**: `publicUpdateNotificationRule`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no | Description of the notification rule |
| `name` | string | yes | Name of the notification rule |
| `notificationDestinations` | array<[`PublicMailNotificationDestinationReferenceDto`](#schema-publicmailnotificationdestinationreferencedto) or [`PublicMsTeamsNotificationDestinationReferenceDto`](#schema-publicmsteamsnotificationdestinationreferencedto) or [`PublicSlackNotificationDestinationReferenceDto`](#schema-publicslacknotificationdestinationreferencedto) or [`PublicWebhookNotificationDestinationReferenceDto`](#schema-publicwebhooknotificationdestinationreferencedto)> | no | Notification destination of the notification rule, like Slack or emails |
| `scope` | [`PublicNotificationRuleScopeDto`](#schema-publicnotificationrulescopedto) | yes | Definition of the monitors bound to the notification rule |
| `ticketingDestinations` | array<[`PublicJiraTicketingDestinationParamsDto`](#schema-publicjiraticketingdestinationparamsdto) or [`PublicServiceNowTicketingDestinationParamsDto`](#schema-publicservicenowticketingdestinationparamsdto)> | no | Ticketing destination of the notification rule, like Jira or ServiceNow |

**Response**

- `200` — Notification Rule updated: [`PublicGetNotificationRuleDto`](#schema-publicgetnotificationruledto)

**Example call**

```bash
curl -X PATCH \
  "https://{tenant}.siffletdata.com/api/v1/notification-rules/{id}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "scope": {
    "monitorScope": {},
    "assetScope": {}
  }
}'
```

Example `200` response:

```json
{
  "ticketingDestinations": [
    {}
  ],
  "name": "string",
  "domainId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "scope": {
    "monitorScope": {},
    "assetScope": {}
  },
  "notificationDestinations": [
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
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## Referenced object schemas

### `PublicMsTeamsNotificationDestinationReferenceDto` {#schema-publicmsteamsnotificationdestinationreferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`SLACK`, `MAIL`, `MS_TEAMS`, `WEBHOOK`) | yes |  |
| `msTeamsName` | string | no | Name of the referenced microsoft teams channel |


### `PublicWebhookNotificationDestinationReferenceDto` {#schema-publicwebhooknotificationdestinationreferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`SLACK`, `MAIL`, `MS_TEAMS`, `WEBHOOK`) | yes |  |
| `webhookName` | string | no | Name of the referenced webhook |


### `PublicSlackNotificationDestinationReferenceDto` {#schema-publicslacknotificationdestinationreferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`SLACK`, `MAIL`, `MS_TEAMS`, `WEBHOOK`) | yes |  |
| `channelName` | string | no | Name of the referenced slack channel |


### `PublicNotificationRuleScopeDto` {#schema-publicnotificationrulescopedto}

Definition of the monitors bound to the notification rule

| Name | Type | Required | Description |
|---|---|---|---|
| `assetScope` | [`PublicAllNotificationRuleAssetScopeDto`](#schema-publicallnotificationruleassetscopedto) or [`PublicDynamicNotificationRuleAssetScopeDto`](#schema-publicdynamicnotificationruleassetscopedto) or [`PublicStaticNotificationRuleAssetScopeDto`](#schema-publicstaticnotificationruleassetscopedto) | yes |  |
| `monitorScope` | [`PublicAllNotificationRuleMonitorScopeDto`](#schema-publicallnotificationrulemonitorscopedto) or [`PublicFilteredNotificationRuleMonitorScopeDto`](#schema-publicfilterednotificationrulemonitorscopedto) | yes |  |


### `PublicPageDtoPublicGetNotificationRuleDto` {#schema-publicpagedtopublicgetnotificationruledto}

| Name | Type | Required | Description |
|---|---|---|---|
| `data` | array<[`PublicGetNotificationRuleDto`](#schema-publicgetnotificationruledto)> | yes |  |
| `totalCount` | integer (int64) | no |  |


### `PublicGetNotificationRuleDto` {#schema-publicgetnotificationruledto}

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no | Description of the notification rule |
| `domainId` | string (uuid) | yes | Domain of the notification rule |
| `id` | string (uuid) | yes |  |
| `name` | string | yes | Name of the notification rule |
| `notificationDestinations` | array<[`PublicMailNotificationDestinationReferenceDto`](#schema-publicmailnotificationdestinationreferencedto) or [`PublicMsTeamsNotificationDestinationReferenceDto`](#schema-publicmsteamsnotificationdestinationreferencedto) or [`PublicSlackNotificationDestinationReferenceDto`](#schema-publicslacknotificationdestinationreferencedto) or [`PublicWebhookNotificationDestinationReferenceDto`](#schema-publicwebhooknotificationdestinationreferencedto)> | yes | Notification destination of the notification rule, like Slack or emails |
| `scope` | [`PublicNotificationRuleScopeDto`](#schema-publicnotificationrulescopedto) | yes | Definition of the monitors bound to the notification rule |
| `ticketingDestinations` | array<[`PublicJiraTicketingDestinationParamsDto`](#schema-publicjiraticketingdestinationparamsdto) or [`PublicServiceNowTicketingDestinationParamsDto`](#schema-publicservicenowticketingdestinationparamsdto)> | yes | Ticketing destination of the notification rule, like Jira or ServiceNow |


### `PublicMailNotificationDestinationReferenceDto` {#schema-publicmailnotificationdestinationreferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`SLACK`, `MAIL`, `MS_TEAMS`, `WEBHOOK`) | yes |  |
| `email` | string | no | Referenced email destination address |


### `PublicServiceNowTicketingDestinationParamsDto` {#schema-publicservicenowticketingdestinationparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `templateName` | string | yes | Name of the referenced template |
| `type` | enum (`JIRA`, `SERVICENOW`) | yes |  |
| `fields` | array<[`PublicServiceNowTemplateFieldDto`](#schema-publicservicenowtemplatefielddto)> | no | Custom fields for service now template |


### `PublicJiraTicketingDestinationParamsDto` {#schema-publicjiraticketingdestinationparamsdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `templateName` | string | yes | Name of the referenced template |
| `type` | enum (`JIRA`, `SERVICENOW`) | yes |  |
| `fields` | array<[`PublicJiraTemplateFieldDto`](#schema-publicjiratemplatefielddto)> | no | Custom fields for jira template |


### `PublicAllNotificationRuleAssetScopeDto` {#schema-publicallnotificationruleassetscopedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ALL`, `STATIC`, `DYNAMIC`) | yes | Type of the notification rule asset scope |


### `PublicAllNotificationRuleMonitorScopeDto` {#schema-publicallnotificationrulemonitorscopedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ALL`, `FILTERED`) | yes | Type of the notification rule monitor scope |


### `PublicStaticNotificationRuleAssetScopeDto` {#schema-publicstaticnotificationruleassetscopedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ALL`, `STATIC`, `DYNAMIC`) | yes | Type of the notification rule asset scope |
| `assets` | array<string> | no | List of the assets in the scope of the notification rule |


### `PublicFilteredNotificationRuleMonitorScopeDto` {#schema-publicfilterednotificationrulemonitorscopedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ALL`, `FILTERED`) | yes | Type of the notification rule monitor scope |
| `monitorTemplates` | array<enum (`COMPLETENESS`, `ROW_LEVEL_DUPLICATES`, `FRESHNESS`, `SCHEMA_CHANGE`, `FRESHNESS_UPDATE_TIME_GAP`, `NUMERICAL_TRANSFORMATION`, `CORRELATED_METRICS`, `CUSTOM_METRICS`, `DISTRIBUTION`, `UNIQUE`, `REFERENTIAL_INTEGRITY`, `NOT_IN_LIST`, … 11 more — full list in `openapi.json`)> | no | List of monitor templates in the scope of the notification rule |


### `PublicDynamicNotificationRuleAssetScopeDto` {#schema-publicdynamicnotificationruleassetscopedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`ALL`, `STATIC`, `DYNAMIC`) | yes | Type of the notification rule asset scope |
| `conditions` | array<[`PublicSourceFilterNotificationRuleAssetScopeConditionDto`](#schema-publicsourcefilternotificationruleassetscopeconditiondto) or [`PublicTagFilterNotificationRuleAssetScopeConditionDto`](#schema-publictagfilternotificationruleassetscopeconditiondto)> | no | List of the conditions defining asset scope of the notification rule |
| `filterLogicalOperator` | enum (`AND`, `OR`) | no | Logical operator to use between conditions |


### `PublicServiceNowTemplateFieldDto` {#schema-publicservicenowtemplatefielddto}

Custom fields for service now template

| Name | Type | Required | Description |
|---|---|---|---|
| `key` | string | yes |  |
| `value` | string | no |  |


### `PublicJiraTemplateFieldDto` {#schema-publicjiratemplatefielddto}

Custom fields for jira template

| Name | Type | Required | Description |
|---|---|---|---|
| `key` | string | yes |  |
| `type` | string | yes |  |
| `value` | string | no |  |


### `PublicTagFilterNotificationRuleAssetScopeConditionDto` {#schema-publictagfilternotificationruleassetscopeconditiondto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`SOURCE`, `TAG`) | yes | Type of the condition |
| `operator` | enum (`IS`, `IS_NOT`) | no | Operator of the condition |
| `tags` | array<[`PublicExternalTagReferenceDto`](#schema-publicexternaltagreferencedto)> | no | List of the tags references in the condition |


### `PublicSourceFilterNotificationRuleAssetScopeConditionDto` {#schema-publicsourcefilternotificationruleassetscopeconditiondto}

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | enum (`SOURCE`, `TAG`) | yes | Type of the condition |
| `operator` | enum (`IS`, `IS_NOT`) | no | Operator of the condition |
| `sources` | array<string> | no | List of the sources in the condition in URI format. <a href="https://docs.siffletdata.com/docs/uri">[Read more about URIs]</a> |


### `PublicExternalTagReferenceDto` {#schema-publicexternaltagreferencedto}

Asset tag from external providers.

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | Id of the referenced object |
| `kind` | enum (`BIGQUERY_EXTERNAL`, `SNOWFLAKE_EXTERNAL`, `DBT_EXTERNAL`, `DATABRICKS_EXTERNAL`, `ADF_EXTERNAL`, `ATLAN_EXTERNAL`, `ALATION_EXTERNAL`, `AMUNDSEN_EXTERNAL`, `APACHE_ATLAS_EXTERNAL`, `CASTOR_DOC_EXTERNAL`, `COLLIBRA_EXTERNAL`, `DATAGALAXY_EXTERNAL`, … 4 more — full list in `openapi.json`) | no | Type of the referenced tag |
| `name` | string | no | Name of the referenced object |

