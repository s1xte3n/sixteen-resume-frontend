# API Examples

## 1. Successful visitor operation

Request:

```http
GET /api/visitors HTTP/1.1
Host: api.example.invalid
Origin: https://resume.example.invalid
Accept: application/json
X-Request-ID: 7d3f4a22-1b4f-4d7b-9c0d-7f1c4a8b2d10
```

Response:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"count":42}
```

## 2. Unsupported method

```http
POST /api/visitors HTTP/1.1
Host: api.example.invalid
Accept: application/json
```

Response:

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

## 3. Invalid request

```http
GET /api/visitors?unexpected=value HTTP/1.1
Host: api.example.invalid
Accept: application/json
```

Response:

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "error": {
    "code": "BAD_REQUEST",
    "message": "The request is invalid.",
    "requestId": "a0c6e9d3-6b4d-4f2f-9b18-0a8d7e6c5b41"
  }
}
```

## 4. Dependency unavailable

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

## 5. Dependency timeout

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

## 6. Internal failure

```http
HTTP/1.1 500 Internal Server Error
Content-Type: application/json

{
  "error": {
    "code": "INTERNAL_ERROR",
    "message": "The visitor counter is temporarily unavailable.",
    "requestId": "4c9a6f10-3b3d-4e6b-8c1a-2f5e7d9b0a11"
  }
}
```

All hostnames are documentation placeholders. UUIDs are synthetic examples.