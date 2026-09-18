# API Errors and HTTP Status Contract

## 1. Canonical error envelope

Every application-generated error uses:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Safe client-facing message.",
    "requestId": "UUID-V4",
    "details": {
      "timestamp": "2026-09-18T12:00:00Z"
    }
  }
}
```

`details` is optional. Clients must not depend on fields inside `details`.

## 2. Status contract

| HTTP status | Error code | When used | Retry guidance |
|---:|---|---|---|
| 400 | `BAD_REQUEST` | Invalid/malformed request | Do not retry unchanged request |
| 405 | `METHOD_NOT_ALLOWED` | Unsupported HTTP method | Do not retry |
| 415 | `UNSUPPORTED_MEDIA_TYPE` | Unsupported content type | Do not retry unchanged request |
| 429 | `RATE_LIMITED` | Platform/application throttling | Retry only according to platform/client backoff policy |
| 500 | `INTERNAL_ERROR` | Unexpected server failure | Client may retry cautiously |
| 503 | `DEPENDENCY_UNAVAILABLE` | Cosmos DB or required backend dependency unavailable | Retry with bounded backoff |
| 504 | `DEPENDENCY_TIMEOUT` | Dependency timeout | Retry with bounded backoff |

The API does not expose 401/403 for normal public counter invocation because no end-user authentication/authorization is required. CORS rejection is handled at the browser/platform boundary and is not an application JSON error contract.

## 3. Error message rules

Messages must:

- Be safe for public clients.
- Explain the failure category without exposing internal implementation.
- Never contain secrets, credentials, tokens, stack traces, database connection information, or sensitive infrastructure details.
- Remain stable enough for human debugging but are not machine-parsed; clients must use `error.code`.

## 4. Correlation

`error.requestId` identifies the request in application telemetry.

If the caller supplies `X-Request-ID`, the value may be reused only after UUID v4 validation. Otherwise the server generates a UUID v4.

## 5. Unknown/unspecified failures

Unexpected failures map to `500 INTERNAL_ERROR`.

A confirmed downstream dependency outage maps to `503 DEPENDENCY_UNAVAILABLE`.

A confirmed downstream timeout maps to `504 DEPENDENCY_TIMEOUT`.

The implementation must not leak the raw downstream error.
