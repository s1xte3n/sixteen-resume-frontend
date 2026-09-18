# API Schemas

## 1. Common conventions

- Media type: `application/json`.
- JSON property names use lower camel case.
- No JSON property is nullable unless explicitly marked nullable.
- Unknown request properties are rejected.
- Numeric `count` is a JSON integer, not a string.
- IDs use UUID v4.
- No date/time field is required by the v1 success response.
- Error timestamps, when emitted, are RFC 3339 UTC.

## 2. VC-001 Request

### VisitorCountRequest

```json
{}
```

Schema:

```yaml
type: object
additionalProperties: false
maxProperties: 0
```

There are no request fields.

## 3. VC-001 Success

### VisitorCountResponse

```yaml
type: object
required:
  - count
additionalProperties: false
properties:
  count:
    type: integer
    minimum: 0
```

Example:

```json
{
  "count": 42
}
```

## 4. Error

### ErrorResponse

```yaml
type: object
required:
  - error
additionalProperties: false
properties:
  error:
    type: object
    required:
      - code
      - message
      - requestId
    additionalProperties: false
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

Example:

```json
{
  "error": {
    "code": "DEPENDENCY_UNAVAILABLE",
    "message": "The visitor counter is temporarily unavailable.",
    "requestId": "7d3f4a22-1b4f-4d7b-9c0d-7f1c4a8b2d10",
    "details": {
      "timestamp": "2026-09-18T12:00:00Z"
    }
  }
}
```

## 5. Error codes

Canonical codes and status mappings are defined in `API-ERRORS.md`.

## 6. Database schema boundary

The following Cosmos DB Table API fields are internal and are never accepted from or returned to the browser:

- `PartitionKey`
- `RowKey`
- database/table names
- connection strings
- access tokens

The public contract exposes only `count`.
