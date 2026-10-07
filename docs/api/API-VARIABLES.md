# API Variables

## 1. Public endpoint

### VC-001 — GET /api/visitors

### Path parameters

None.

### Query parameters

None.

### Request headers

| Header | Direction | Required | Type | Validation |
|---|---|---:|---|---|
| `Origin` | Request | Browser-generated | string | Must match production CORS allowlist |
| `Accept` | Request | Recommended | media type | Should permit `application/json` |
| `Content-Type` | Request | No | media type | No body is defined; not required |
| `X-Request-ID` | Request | No | UUID string | UUID v4 when present |

### Response headers

| Header | Direction | Required | Rule |
|---|---|---:|---|
| `Content-Type` | Response | Yes | `application/json` |
| `X-Request-ID` | Response | Yes | UUID v4; preserves valid caller value or returns a generated UUID v4 |

### Request body

None.

### Success response

| Field | Type | Required | Nullable | Constraint |
|---|---|---:|---:|---|
| `count` | integer | Yes | No | >= 0 |

### Error response

| Field | Type | Required | Nullable | Constraint |
|---|---|---:|---:|---|
| `error.code` | string | Yes | No | uppercase identifier, 3–64 chars |
| `error.message` | string | Yes | No | 1–256 chars |
| `error.requestId` | UUID string | Yes | No | UUID v4 |
| `error.details` | object | No | No | Safe metadata only |
| `error.details.timestamp` | date-time | No | No | RFC 3339 UTC |

## 2. Internal DB-001 variables

| Variable | Type | Public | Rule |
|---|---|---:|---|
| `PartitionKey` | string | No | Stable internal logical partition |
| `RowKey` | string | No | Stable internal counter entity |
| `Count` | integer | No | >= 0 |
| Entity version/ETag | provider-specific | No | Used for concurrency control where supported |

## 3. Deployment interfaces

DEP-001 and DEP-002 use workflow/control-plane inputs rather than public API fields.

They may include:

- repository/ref;
- approved non-secret configuration;
- deployment resource identifiers;
- secure identity context.

Secret values are never API/interface fields and are supplied through approved secret/OIDC mechanisms.

## 4. Identifier rules

- `X-Request-ID`: UUID v4.
- No visitor/user identifier.
- No session identifier.
- No IP address field.
- No Cosmos `PartitionKey` or `RowKey` exposed publicly.
