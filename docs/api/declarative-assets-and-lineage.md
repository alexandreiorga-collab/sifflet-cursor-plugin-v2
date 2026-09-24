# Declarative Assets and Lineage (Workspace sync)

Push declarative assets/lineage and delete the resulting workspace.

[← Back to API index](README.md)

## `POST /v1/assets/sync`

**Sync a workspace**

- **operationId**: `publicSyncAssets`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `dryRun (query)` | boolean | no |  |

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `assets` | array<[`PublicDeclarativeAssetDto`](#schema-publicdeclarativeassetdto)> | no | Use this parameter to declare assets and their associated links. It is recommended to use the `lineages` object of the `assets` array of objects rather than the `lineages` array of objects for cases where you want to declare assets and their corresponding lineage links. |
| `lineages` | array<[`PublicDeclarativeLineageDto`](#schema-publicdeclarativelineagedto)> | no | Use this parameter to declare lineage links between assets. It is recommended to use the `lineages` arrays of objects object rather than the `lineages` object of the `assets` array of objects for cases where you want to declare lineage links between existing assets. |
| `sources` | array<[`PublicDeclarativeSourceDto`](#schema-publicdeclarativesourcedto)> | no | Declaring sources is optional. Declaring a source is useful if you want to attach it specific metadata (e.g. a name, a description, etc.). If no source is declared, Sifflet automatically adds declared assets to sources using declared assets URIs. |
| `workspace` | string | yes | Name of the workspace containing declared assets and sources. <a href="https://docs.siffletdata.com/docs/declarative-assets#workspaces">[Read more about workspaces]</a> |

**Response**

- `200` — Successfully applied workspace: [`WorkspaceApplyResponseDto`](#schema-workspaceapplyresponsedto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v1/assets/sync" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "workspace": "string"
}'
```

Example `200` response:

```json
{
  "changes": [
    {
      "change": {
        "from": "...",
        "fromWorkspaceId": "...",
        "to": "...",
        "toWorkspaceId": "..."
      },
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "kind": "string",
      "logs": [
        "..."
      ]
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
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `DELETE /v1/assets/{name}`

**Delete workspace by name**

- **operationId**: `publicDeleteWorkspace`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `name (path)` | string | yes |  |
| `dryRun (query)` | boolean | no |  |

**Response**

- `200` — Successfully deleted workspace: [`WorkspaceApplyResponseDto`](#schema-workspaceapplyresponsedto)

**Example call**

```bash
curl -X DELETE \
  "https://{tenant}.siffletdata.com/api/v1/assets/{name}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "changes": [
    {
      "change": {
        "from": "...",
        "fromWorkspaceId": "...",
        "to": "...",
        "toWorkspaceId": "..."
      },
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "kind": "string",
      "logs": [
        "..."
      ]
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

## Referenced object schemas

### `PublicDeclarativeLineageDto` {#schema-publicdeclarativelineagedto}

Use this parameter to declare lineage links between assets. It is recommended to use the `lineages` arrays of objects object rather than the `lineages` object of the `assets` array of objects for cases where you want to declare lineage links between existing assets.

| Name | Type | Required | Description |
|---|---|---|---|
| `from` | string | yes | URI string identifying the upstream asset of the lineage. <a href="https://docs.siffletdata.com/docs/uri">[Read more about URIs]</a> |
| `to` | string | yes | URI string identifying the downstream asset of the lineage. <a href="https://docs.siffletdata.com/docs/uri">[Read more about URIs]</a> |


### `PublicDeclarativeAssetDto` {#schema-publicdeclarativeassetdto}

Use this parameter to declare assets and their associated links. It is recommended to use the `lineages` object of the `assets` array of objects rather than the `lineages` array of objects for cases where you want to declare assets and their corresponding lineage links.

| Name | Type | Required | Description |
|---|---|---|---|
| `customMetadataValues` | array<[`PublicCustomMetadataEntryLabelReferenceDto`](#schema-publiccustommetadataentrylabelreferencedto) or [`PublicCustomMetadataEntryStringReferenceDto`](#schema-publiccustommetadataentrystringreferencedto) or [`PublicCustomMetadataEntryTeamReferenceDto`](#schema-publiccustommetadataentryteamreferencedto) or [`PublicCustomMetadataEntryUserReferenceDto`](#schema-publiccustommetadataentryuserreferencedto)> | no | Custom metadata entries to be associated with the declared asset |
| `description` | string | no | Description of the declared asset |
| `href` | string | no | External link to be associated with the declared asset (e.g. link to your actual BI dashboard, ML model, etc.). This link will show up as a button on your asset page. |
| `lineages` | [`PublicDeclarativeLineageListDto`](#schema-publicdeclarativelineagelistdto) | no | Lineage links to be created for the declared asset |
| `name` | string | no | Display name of the declared asset |
| `owners` | array<[`PublicReferenceByIdOrEmailDto`](#schema-publicreferencebyidoremaildto)> | no | Owners to be associated with the declared asset |
| `subType` | string | no | Secondary type of the declared asset. Shows up in the Data Catalog as an additional metadata giving more details about the asset type (e.g. "type": "Dataset", "subType": "View"). "type": "Generic" declared assets will have their subType value added to the Asset type filter category of the Data Catalog. |
| `tags` | array<[`PublicTagReferenceDto`](#schema-publictagreferencedto)> | no | Tags to be associated with the declared asset |
| `terms` | array<[`PublicReferenceByIdOrNameDto`](#schema-publicreferencebyidornamedto)> | no | Business terms to be associated with the declared asset. Business terms can be referenced either through their `id`, their `name`, or both. |
| `type` | enum (`Dataset`, `Dashboard`, `Pipeline`, `MlModel`, `Generic`) | yes | Primary type of the declared asset, indicating the overall category the asset falls in. Utilized to know which value the declared asset should be nested in in the Asset type filter category of the Data Catalog. Selecting Generic will result in the subType value being added as a value of this Asset type filter category. |
| `uri` | string | yes | URI string identifying the declared asset. <a href="https://docs.siffletdata.com/docs/uri">[Read more about URIs]</a> |


### `WorkspaceApplyResponseDto` {#schema-workspaceapplyresponsedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `changes` | array<[`WorkspaceApplyObjectResponseDto`](#schema-workspaceapplyobjectresponsedto)> | no |  |


### `PublicDeclarativeSourceDto` {#schema-publicdeclarativesourcedto}

Declaring sources is optional. Declaring a source is useful if you want to attach it specific metadata (e.g. a name, a description, etc.). If no source is declared, Sifflet automatically adds declared assets to sources using declared assets URIs.

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no | Description of the declared source |
| `name` | string | yes | Display name of the declared source |
| `tags` | array<[`PublicTagReferenceDto`](#schema-publictagreferencedto)> | no | Tags to be associated with the declared source |
| `uri` | string | yes | URI string identifying the declared source. <a href="https://docs.siffletdata.com/docs/uri">[Read more about URIs]</a> |


### `PublicCustomMetadataEntryTeamReferenceDto` {#schema-publiccustommetadataentryteamreferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `customMetadataName` | string | yes | Name of the referenced custom metadata |
| `type` | enum (`LABEL`, `STRING`, `USER`, `TEAM`) | yes |  |
| `name` | string | no | Value of the referenced custom metadata team name |


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


### `PublicReferenceByIdOrEmailDto` {#schema-publicreferencebyidoremaildto}

Id or email reference to an owner

| Name | Type | Required | Description |
|---|---|---|---|
| `email` | string | no | Email of the referenced owner |
| `id` | string (uuid) | no | Id of the referenced owner |


### `PublicCustomMetadataEntryUserReferenceDto` {#schema-publiccustommetadataentryuserreferencedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `customMetadataName` | string | yes | Name of the referenced custom metadata |
| `type` | enum (`LABEL`, `STRING`, `USER`, `TEAM`) | yes |  |
| `email` | string | no | Value of the referenced custom metadata user email |


### `PublicDeclarativeLineageListDto` {#schema-publicdeclarativelineagelistdto}

Lineage links to be created for the declared asset

| Name | Type | Required | Description |
|---|---|---|---|
| `from` | array<string> | no | URI strings identifying the upstream assets. <a href="https://docs.siffletdata.com/docs/uri">[Read more about URIs]</a> |
| `to` | array<string> | no | URI strings identifying the downstream assets. <a href="https://docs.siffletdata.com/docs/uri">[Read more about URIs]</a> |


### `PublicTagReferenceDto` {#schema-publictagreferencedto}

Tags of the source. A tag can either be referenced by its id or its name or its name and kind.

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string (uuid) | no | Id of the referenced object |
| `kind` | enum (`TAG`, `CLASSIFICATION`) | no | Type of the referenced tag |
| `name` | string | no | Name of the referenced object |


### `WorkspaceApplyObjectResponseDto` {#schema-workspaceapplyobjectresponsedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `change` | [`ChangeDto`](#schema-changedto) | no |  |
| `id` | string (uuid) | no |  |
| `kind` | string | no |  |
| `logs` | array<[`LogDto`](#schema-logdto)> | no |  |
| `status` | enum (`OK`, `Error`, `Fatal`) | no |  |
| `subStatus` | enum (`Success`, `Skipped`, `ValidationError`, `DeserializationError`, `Unauthorized`, `InternalServerError`) | no |  |


### `ChangeDto` {#schema-changedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `from` | [`JsonNode`](#schema-jsonnode) | no |  |
| `fromWorkspaceId` | string (uuid) | no |  |
| `to` | [`JsonNode`](#schema-jsonnode) | no |  |
| `toWorkspaceId` | string (uuid) | no |  |
| `type` | enum (`None`, `Create`, `CreateIfMissing`, `Move`, `MoveAndUpdate`, `Update`, `Delete`) | no |  |


### `LogDto` {#schema-logdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `level` | enum (`Info`, `Warning`, `Error`, `Fatal`) | no |  |
| `message` | string | no |  |


### `JsonNode` {#schema-jsonnode}

_No fields._

