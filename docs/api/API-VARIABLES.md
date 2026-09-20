# API Variables

## 1. Path variables

VC-001 has no path variables.

| Variable | Type | Required | Constraints |
|---|---|---:|---|
| None | — | — | — |

## 2. Query variables

VC-001 has no query parameters.

| Variable | Type | Required | Constraints |
|---|---|---:|---|
| None | — | — | — |

No pagination, filtering, or sorting parameters are supported.

## 3. Headers

| Header | Direction | Required | Type | Constraints |
|---|---|---:|---|---|
| `Origin` | Request | Browser-generated | string | Must match configured production CORS origin |
| `Content-Type` | Request | No | media type | Not required; VC-001 has no request body |
| `Accept` | Request | Recommended | media type | `application/json` |
| `X-Request-ID` | Request | No | UUID string | UUID v4 when present |
| `Content-Type` | Response | Yes | media type | `application/json` |

## 4. Body variables

VC-001 has no request body.

| Variable | Type | Required | Nullable | Constraints |
|---|---|---:|---:|---|
| None | — | — | — | No request body |

## 5. Response variables

### Success

| Variable | Type | Required | Nullable | Constraints |
|---|---|---:|---:|---|
| `count` | integer | Yes | No | >= 0 |

### Error

| Variable | Type | Required | Nullable | Constraints |
|---|---|---:|---:|---|
| `error.code` | string | Yes | No | Uppercase identifier, 3–64 chars |
| `error.message` | string | Yes | No | 1–256 chars |
| `error.requestId` | UUID v4 string | Yes | No | UUID |
| `error.details` | object | No | No | Implementation-safe metadata only |
| `error.details.timestamp` | RFC 3339 date-time | No | No | UTC |

## 6. Identifier rules

- API request IDs: UUID v4.
- Cosmos DB `PartitionKey` and `RowKey`: internal implementation identifiers; not public API fields.
- No visitor/user identifier is defined by v1.
