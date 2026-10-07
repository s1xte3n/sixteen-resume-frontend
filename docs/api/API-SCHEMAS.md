# API Schemas

## 1. Schema conventions

- JSON property names use lower camel case.
- Unknown request properties are not part of the VC-001 contract.
- No success property is nullable.
- `count` is a JSON integer >= 0.
- Public identifiers are UUID v4 only where defined.
- Error timestamps, when present, are RFC 3339 UTC.
- Internal Cosmos fields are never public API fields.

## 2. VC-001 request

VC-001 is bodyless.

There is **no request JSON schema** and no request body is required.

Canonical request:

```http
GET /api/visitors HTTP/1.1
Accept: application/json
```

A JSON object such as `{}` is not required and is not part of the wire contract.

## 3. VC-001 success — VisitorCountResponse

```yaml
type: object
additionalProperties: false
required:
  - count
properties:
  count:
    type: integer
    minimum: 0
```

Example:

```json
{"count":42}
```

## 4. ErrorResponse

```yaml
type: object
additionalProperties: false
required:
  - error
properties:
  error:
    type: object
    additionalProperties: false
    required:
      - code
      - message
      - requestId
    properties:
      code:
        type: string
        pattern: '^[A-Z][A-Z0-9_]{2,63}$'
      message:
        type: string
        minLength: 1
        maxLength: 256
      requestId:
        type: string
        format: uuid
      details:
        type: object
        additionalProperties: false
        properties:
          timestamp:
            type: string
            format: date-time
```

## 5. Error code enum

The canonical application error codes are:

- `BAD_REQUEST`
- `METHOD_NOT_ALLOWED`
- `RATE_LIMITED`
- `INTERNAL_ERROR`
- `DEPENDENCY_UNAVAILABLE`
- `DEPENDENCY_TIMEOUT`

## 6. Internal persistence schema

The single logical Cosmos DB Table entity contains:

| Field | Type | Constraint |
|---|---|---|
| `PartitionKey` | string | Stable internal key |
| `RowKey` | string | Stable internal key |
| `Count` | integer | >= 0 |

The actual key values are internal and are not exposed through VC-001.

## 7. Deployment interface payloads

DEP-001 and DEP-002 do not define public JSON request/response payloads. Their contract is workflow/control-plane behavior:

- authenticated workflow identity;
- approved repository state;
- required validation gates;
- Azure resource/deployment operations;
- explicit success/failure status.

No deployment credential or secret value is a contract field.