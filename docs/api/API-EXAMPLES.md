# API Examples

## 1. Successful counter operation

### Request

```http
POST /api/v1/visitor-count HTTP/1.1
Host: api.example.invalid
Origin: https://resume.example.invalid
Content-Type: application/json
Accept: application/json
X-Request-ID: 7d3f4a22-1b4f-4d7b-9c0d-7f1c4a8b2d10

{}
```

### Response

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "count": 42
}
```

## 2. Invalid request body

### Request

```http
POST /api/v1/visitor-count HTTP/1.1
Content-Type: application/json

{"visitorId":"abc"}
```

### Response

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "error": {
    "code": "BAD_REQUEST",
    "message": "The request body is invalid.",
    "requestId": "7d3f4a22-1b4f-4d7b-9c0d-7f1c4a8b2d10"
  }
}
```

## 3. Unsupported method

### Request

```http
GET /api/v1/visitor-count HTTP/1.1
Accept: application/json
```

### Response

```http
HTTP/1.1 405 Method Not Allowed
Content-Type: application/json

{
  "error": {
    "code": "METHOD_NOT_ALLOWED",
    "message": "The requested method is not supported.",
    "requestId": "9b2a9e1f-1f9c-4a70-8a73-7c1d2d2a6a50"
  }
}
```

## 4. Persistence dependency unavailable

### Response

```http
HTTP/1.1 503 Service Unavailable
Content-Type: application/json

{
  "error": {
    "code": "DEPENDENCY_UNAVAILABLE",
    "message": "The visitor counter is temporarily unavailable.",
    "requestId": "c1a7f9d8-5a0e-4f1d-8f4c-5c9d1f0c3a21"
  }
}
```

## 5. Timeout

```http
HTTP/1.1 504 Gateway Timeout
Content-Type: application/json

{
  "error": {
    "code": "DEPENDENCY_TIMEOUT",
    "message": "The visitor counter timed out.",
    "requestId": "e2c7d0f5-0a5e-4c6e-bc55-4f8b0d4d6e19"
  }
}
```

## Example constraints

Examples use reserved `.invalid` hostnames and synthetic UUIDs. They are documentation examples only.

The response count is illustrative; exact increment behavior remains blocked by OR-001.
