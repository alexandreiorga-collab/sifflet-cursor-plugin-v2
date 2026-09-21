# External Catalog

Push external catalog metadata (tags, terms, descriptions) onto assets.

[← Back to API index](README.md)

## `POST /v1/external-catalog/import`

**Push external catalog metadata to Sifflet assets** — Enriches existing Sifflet assets with metadata imported from an external data catalog. Each asset is processed independently. The caller must have "Catalog Editor" or "Domain Editor" permission on each asset's domain.

The HTTP status reflects the aggregate outcome: 200 when every asset succeeds, 207 when some succeed and some fail, 400 when all assets fail.

- **operationId**: `publicImportExternalCatalog`

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `assets` | array<[`PublicAssetImportDto`](#schema-publicassetimportdto)> | yes | Assets to enrich with external catalog metadata |
| `configuration` | [`PublicConfigurationImportDto`](#schema-publicconfigurationimportdto) | yes | Configuration of the import |

**Response**

- `200` — All assets imported successfully: [`PublicExternalCatalogImportResponseDto`](#schema-publicexternalcatalogimportresponsedto)
- `207` — Partial success - some assets imported, some failed: [`PublicExternalCatalogImportResponseDto`](#schema-publicexternalcatalogimportresponsedto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v1/external-catalog/import" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "assets": [
    {
      "uri": "bigquery:project.dataset.table"
    }
  ],
  "configuration": {
    "catalogProvider": "APACHE_ATLAS"
  }
}'
```

Example `200` response:

```json
{
  "detail": {
    "importStatus": "SUCCESS",
    "results": [
      {
        "message": "...",
        "status": "...",
        "uri": "..."
      }
    ]
  },
  "status": 0,
  "title": "string"
}
```

**Errors**

| Status | Description |
|---|---|
| `400` | Either the request failed validation or all assets failed to import  |
| `401` | Unauthorized |
| `403` | Forbidden |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## Referenced object schemas

### `PublicConfigurationImportDto` {#schema-publicconfigurationimportdto}

Configuration of the import

| Name | Type | Required | Description |
|---|---|---|---|
| `catalogProvider` | enum (`ATLAN`, `ALATION`, `AMUNDSEN`, `APACHE_ATLAS`, `CASTOR_DOC`, `COLLIBRA`, `DATAGALAXY`, `INFORMATICA`, `SECODA`, `SELECT_STAR`, `CATALOG_GENERIC`) | yes | Type of external catalog. If not listed, use CATALOG_GENERIC |


### `PublicExternalCatalogImportResponseDto` {#schema-publicexternalcatalogimportresponsedto}

| Name | Type | Required | Description |
|---|---|---|---|
| `detail` | [`PublicExternalCatalogImportResultDto`](#schema-publicexternalcatalogimportresultdto) | no | Detailed import result |
| `status` | integer (int32) | no | HTTP status code |
| `title` | string | no | HTTP status title |


### `PublicAssetImportDto` {#schema-publicassetimportdto}

Assets to enrich with external catalog metadata

| Name | Type | Required | Description |
|---|---|---|---|
| `catalogUrl` | string | no | URL of the asset in the external catalog. Null or empty removes the existing link. |
| `description` | string | no | Description of the asset in the external catalog. Null or empty removes the existing description. |
| `labels` | array<[`PublicLabelExternalMetadataDto`](#schema-publiclabelexternalmetadatadto)> | no | Labels to attach to the asset |
| `strings` | array<[`PublicStringExternalMetadataDto`](#schema-publicstringexternalmetadatadto)> | no | String metadata to attach to the asset |
| `tags` | array<[`PublicNamedElementExternalMetadataDto`](#schema-publicnamedelementexternalmetadatadto)> | no | Tags to attach to the asset |
| `uri` | string | yes | URI of the asset to enrich. <a href="https://docs.siffletdata.com/docs/uri">[Read more about URIs]</a> |


### `PublicExternalCatalogImportResultDto` {#schema-publicexternalcatalogimportresultdto}

Detailed import result

| Name | Type | Required | Description |
|---|---|---|---|
| `importStatus` | enum (`SUCCESS`, `PARTIAL_SUCCESS`, `FAILURE`) | no | Status of the import |
| `results` | array<[`PublicAssetImportResultDto`](#schema-publicassetimportresultdto)> | no | Per-asset import status |


### `PublicNamedElementExternalMetadataDto` {#schema-publicnamedelementexternalmetadatadto}

Tags to attach to the asset

| Name | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | Name to display |


### `PublicStringExternalMetadataDto` {#schema-publicstringexternalmetadatadto}

String metadata to attach to the asset

| Name | Type | Required | Description |
|---|---|---|---|
| `data` | string | yes | Value of the metadata |
| `name` | string | yes | Name of the metadata |
| `showInFilter` | boolean | no | Whether the metadata should be shown as a filter in the catalog |


### `PublicLabelExternalMetadataDto` {#schema-publiclabelexternalmetadatadto}

Labels to attach to the asset

| Name | Type | Required | Description |
|---|---|---|---|
| `data` | array<[`PublicNamedElementExternalMetadataDto`](#schema-publicnamedelementexternalmetadatadto)> | yes | Values of the label |
| `name` | string | yes | Name of the metadata |
| `showInFilter` | boolean | no | Whether the label should be shown as a filter in the catalog |


### `PublicAssetImportResultDto` {#schema-publicassetimportresultdto}

Per-asset import status

| Name | Type | Required | Description |
|---|---|---|---|
| `message` | string | no | Failure message, present only when the asset failed to import |
| `status` | enum (`SUCCESS`, `FAILED`) | no | Import status of the asset |
| `uri` | string | no | URI of the asset |

