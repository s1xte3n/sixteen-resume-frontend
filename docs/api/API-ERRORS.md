# API Errors and Error Taxonomy

## 1. Canonical envelope

All application-generated VC-001 errors use:

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

Required:

- `error.code`
- `error.message`
- `error.requestId`

Optional:

- `error.details`
- `error.details.timestamp`

Clients must use `error.code` for machine behavior and must not parse `message`.

## 2. Error taxonomy

| Code | HTTP | Meaning | Trigger | Client behavior | Server behavior | Logging | Related requirements/tests |
|---|---:|---|---|---|---|---|---|
| `BAD_REQUEST` | 400 | Request violates contract | Invalid method-specific input, invalid UUID, unsupported query/body | Do not retry unchanged request | No state mutation | Log validation category + requestId; never sensitive input | REQ-AZ-009 / VT-009 |
| `METHOD_NOT_ALLOWED` | 405 | Method unsupported | Non-GET method | Do not retry | No state mutation | Log method/status | REQ-AZ-009 / VT-009 |
| `RATE_LIMITED` | 429 | Platform/runtime throttling | Provider or approved runtime limit | Do not blindly retry; no client retry is mandated | No successful count claim | Log throttling status + requestId | REQ-AZ-007, REQ-AZ-010 / VT-007, VT-010 |
| `INTERNAL_ERROR` | 500 | Unexpected/internal failure | Runtime defect, configuration error, backend authorization failure | Treat counter unavailable; continue page | Safe response; no unconfirmed count | Error log with requestId; no secrets | REQ-AZ-009, REQ-AZ-010 / VT-009, VT-010 |
| `DEPENDENCY_UNAVAILABLE` | 503 | Required dependency unavailable | Cosmos/service unavailable before commit | Treat counter unavailable | No successful count claim | Dependency failure + requestId | REQ-AZ-008..010 / VT-008..010 |
| `DEPENDENCY_TIMEOUT` | 504 | Required dependency timed out | Dependency exceeds configured boundary | Treat result as unknown; do not automatically retry | Do not return unconfirmed count | Timeout + requestId + duration if safe | REQ-AZ-008..010 / VT-008..010 |

## 3. Authentication failures

There is no end-user authentication.

Therefore:

- Missing user credentials: not an error; the endpoint is public.
- Invalid user credentials: no authentication scheme exists, so clients must not send them.
- Function-to-Cosmos authentication failure: internal server-side configuration/security failure; map safely to `500 INTERNAL_ERROR` and log the actual authorization failure server-side.

## 4. Authorization failures

Public caller authorization is intentionally not user-based.

A caller cannot request arbitrary database state.

A Function identity authorization failure against Cosmos is internal and must not disclose Cosmos authorization details. Public mapping: `500 INTERNAL_ERROR`.

## 5. CORS failures

CORS failures are enforced by the browser/platform boundary.

They are not represented as a guaranteed application JSON error because a browser may block access to the response before JavaScript can read it.

Production configuration must use the final approved resume origin and must not use wildcard origin.

## 6. Safe error exposure

Never return:

- stack traces;
- exception messages containing secrets;
- access keys;
- tokens;
- connection strings;
- Cosmos credentials;
- raw database errors;
- internal resource names where unnecessary.

## 7. Retry semantics

### Client

No automatic retry is defined for VC-001. This is deliberate because the operation is non-idempotent and an unknown-outcome request may already have incremented the counter.

### Server

Only safe, known optimistic-concurrency conflicts may be retried before a successful commit is confirmed. The server must not blindly repeat an operation after an ambiguous write outcome.

Exact retry counts/backoff are Phase 5 configuration, not public wire behavior.

## 8. Error consistency rules

Every application-generated error must:

1. use the canonical envelope;
2. use one canonical code;
3. include a UUID requestId;
4. use a contract-defined HTTP status;
5. avoid sensitive details;
6. preserve the counter invariant by never claiming an unconfirmed commit.