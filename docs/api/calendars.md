# Calendars

Maintenance-window calendars used by monitor schedules.

[← Back to API index](README.md)

## `GET /v1/calendars`

**Get list of calendars**

- **operationId**: `publicGetCalendars`

**Response**

- `200` — Calendars retrieved: [`PublicPageDtoPublicCalendarGetDto`](#schema-publicpagedtopubliccalendargetdto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/calendars" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "data": [
    {
      "timeslots": [
        "..."
      ],
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
| `404` | Resource not found |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `POST /v1/calendars`

**Create a calendar**

- **operationId**: `publicCreateCalendar`

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no |  |
| `name` | string | yes |  |
| `timeslots` | array<[`CalendarTimeslot`](#schema-calendartimeslot)> | yes |  |

**Response**

- `201` — Calendar created: [`PublicCalendarGetDto`](#schema-publiccalendargetdto)

**Example call**

```bash
curl -X POST \
  "https://{tenant}.siffletdata.com/api/v1/calendars" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "timeslots": [
    {
      "date": "2024-01-01T00:00:00Z"
    }
  ],
  "name": "string"
}'
```

Example `201` response:

```json
{
  "timeslots": [
    {
      "date": "2024-01-01T00:00:00Z"
    }
  ],
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
| `409` | Conflict |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## `DELETE /v1/calendars/{id}`

**Delete a calendar**

- **operationId**: `publicDeleteCalendar`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `204` — Calendar deleted (no body)

**Example call**

```bash
curl -X DELETE \
  "https://{tenant}.siffletdata.com/api/v1/calendars/{id}" \
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

## `GET /v1/calendars/{id}`

**Get a calendar by id**

- **operationId**: `publicGetCalendar`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Response**

- `200` — Calendar retrieved: [`PublicCalendarGetDto`](#schema-publiccalendargetdto)

**Example call**

```bash
curl -X GET \
  "https://{tenant}.siffletdata.com/api/v1/calendars/{id}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN"
```

Example `200` response:

```json
{
  "timeslots": [
    {
      "date": "2024-01-01T00:00:00Z"
    }
  ],
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

## `PATCH /v1/calendars/{id}`

**Update a calendar**

- **operationId**: `publicUpdateCalendar`

**Parameters**

| Name | Type | Required | Description |
|---|---|---|---|
| `id (path)` | string (uuid) | yes |  |

**Request body** (required, `application/json`)

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no |  |
| `name` | string | yes |  |
| `timeslots` | array<[`CalendarTimeslot`](#schema-calendartimeslot)> | yes |  |

**Response**

- `200` — Calendar updated: [`PublicCalendarGetDto`](#schema-publiccalendargetdto)

**Example call**

```bash
curl -X PATCH \
  "https://{tenant}.siffletdata.com/api/v1/calendars/{id}" \
  -H "Authorization: Bearer $SIFFLET_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "timeslots": [
    {
      "date": "2024-01-01T00:00:00Z"
    }
  ],
  "name": "string"
}'
```

Example `200` response:

```json
{
  "timeslots": [
    {
      "date": "2024-01-01T00:00:00Z"
    }
  ],
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
| `409` | Conflict |
| `500` | Internal server error |

Error bodies follow the standard [`ApiProblemSchema`](README.md#standard-error-format) shape (`application/problem+json`).

---

## Referenced object schemas

### `CalendarTimeslot` {#schema-calendartimeslot}

| Name | Type | Required | Description |
|---|---|---|---|
| `date` | string (date) | yes |  |
| `description` | string | no |  |


### `PublicCalendarGetDto` {#schema-publiccalendargetdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | no |  |
| `editable` | boolean | no |  |
| `id` | string (uuid) | yes |  |
| `name` | string | yes |  |
| `standardCalendar` | enum (`US_PUBLIC_HOLIDAYS`, `FRANCE_PUBLIC_HOLIDAYS`, `UK_PUBLIC_HOLIDAYS`, `BELGIUM_PUBLIC_HOLIDAYS`, `SPAIN_PUBLIC_HOLIDAYS`, `GERMANY_PUBLIC_HOLIDAYS`, `NETHERLANDS_PUBLIC_HOLIDAYS`, `SUNDAYS`, `WEEKENDS`) | no |  |
| `timeslots` | array<[`CalendarTimeslot`](#schema-calendartimeslot)> | yes |  |


### `PublicPageDtoPublicCalendarGetDto` {#schema-publicpagedtopubliccalendargetdto}

| Name | Type | Required | Description |
|---|---|---|---|
| `data` | array<[`PublicCalendarGetDto`](#schema-publiccalendargetdto)> | yes |  |
| `totalCount` | integer (int64) | no |  |

