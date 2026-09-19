# API Contract

## 1. Document Control

| Field | Value |
|---|---|
| Contract | Visitor Counter HTTP API |
| Contract version | 1.0.0 |
| API version | v1 |
| Status | Frozen MVP interface; OR-001, OR-006 and OR-007 resolved |
| Runtime | Python on Azure Functions |
| Persistence | Azure Cosmos DB Table API |
| Public caller | Resume browser JavaScript |
| Source requirements | REQ-AZ-007, REQ-AZ-008, REQ-AZ-009, REQ-AZ-010 |
| Verification | VT-007, VT-008, VT-009, VT-010 |
| Architecture | ADR-002, ADR-003, ADR-007 |

## 2. Contract Freeze

The following are frozen for implementation:

- API base path: `/api`.
- Counter operation: `GET /api/visitors`.
- Public API requires no end-user authentication.
- Production browser access is restricted by CORS to the approved resume origin; the production origin remains a deployment variable until OR-002/OR-004 are closed.
- The request has no body.
- The request does not require `Content-Type`.
- Successful response is JSON with one required `count` field.
- Error response is JSON with `error.code`, `error.message`, and `error.requestId`; `error.details` is optional.
- `requestId` is UUID v4.
- Error `timestamp` is RFC 3339 UTC when supplied in `details`; clients must not depend on it.
- Count is a non-negative JSON integer.
- Query parameters, path parameters, and request bodies are not accepted.
- No pagination, filtering, or sorting is supported.
- No API operation exposes Cosmos DB identifiers, credentials, connection strings, or tokens.
- No reset, delete, admin, analytics, authentication, or profile operations are part of v1.

### Visitor semantics resolution

OR-001 is resolved. The API operation uses the approved visitor semantics: one successfully committed counter operation caused by a top-level resume page load; a refresh is another operation; no unique-human, browser, session, IP, device, or user identification is performed; failed operations do not increment persisted state; and concurrent successful operations must not lose increments.

## 3. Operation VC-001

### Identity

**Contract ID:** VC-001  
**Method/path:** `GET /api/visitors`  
**Purpose:** Perform the approved visitor-count operation and return the resulting persisted count.

### Authentication

- End-user authentication: none.
- Transport: HTTPS only in production.
- Function-to-Cosmos authentication: server-side Azure-supported credential mechanism; exact mechanism is an infrastructure/security implementation decision.
- Browser must never receive database credentials.

### Authorization

The operation is publicly invocable because the resume visitor counter is public.

Authorization is constrained by:
- CORS allowlist at the HTTP boundary.
- No privileged operations exposed.
- Backend identity has only required Cosmos permissions.
- No client-supplied identity is trusted for ownership.

### Path variables

None.

### Query variables

None.

### Headers

| Header | Required | Value |
|---|---:|---|
| `Origin` | Browser-generated | Production resume origin; validated by CORS |
| `Content-Type` | No | Not required for the bodyless GET request |
| `Accept` | Recommended | `application/json` |
| `X-Request-ID` | No | Client correlation ID; if absent, server generates UUID v4 |

The server must validate `X-Request-ID` as a UUID v4 if it accepts the header. Invalid values produce `400 BAD_REQUEST`.

### Request body

The request has no body. Query parameters and path parameters are not accepted.

### Success

**HTTP 200 OK**

```json
{
  "count": 42
}
```

The returned `count` is the persisted count after the approved counter operation.

### Expected errors

| Status | Code | Meaning |
|---:|---|---|
| 400 | `BAD_REQUEST` | Malformed JSON, invalid request ID, or unsupported request fields |
| 405 | `METHOD_NOT_ALLOWED` | HTTP method is not supported |
| 415 | `UNSUPPORTED_MEDIA_TYPE` | Request content type is unsupported |
| 429 | `RATE_LIMITED` | Request rejected by an applicable platform/rate limit |
| 500 | `INTERNAL_ERROR` | Unexpected backend failure |
| 503 | `DEPENDENCY_UNAVAILABLE` | Required backend dependency is unavailable |
| 504 | `DEPENDENCY_TIMEOUT` | Required backend dependency timed out |

A CORS rejection is handled by the HTTP platform/browser and is not represented as an application error schema.

### Side effects

A successful request may modify the single persistent visitor-counter entity according to the approved visitor semantics.

No other persistent data may be created or modified.

### Idempotency

VC-001 is **not idempotent by default** because a successful operation may change the counter.

No `Idempotency-Key` behavior is defined in v1. Clients must not retry a successful/unknown-outcome request merely to force an increment. Retry behavior must follow the selected visitor semantics and frontend policy.

### Pagination/filtering/sorting

Not applicable.

### Ownership/isolation

There is one application-owned counter. There is no user or tenant isolation model. The caller does not select `PartitionKey`, `RowKey`, or any database identifier.

### Validation

- HTTP method must be GET.
- Production transport must be HTTPS.
- No request body is accepted.
- Request ID, when supplied, must be UUID v4.
- No query/path parameters are accepted.
- Request must not contain database or authentication fields.
- Count returned must be an integer >= 0.

### Failure behavior

The API must not expose stack traces, connection strings, database endpoints, access tokens, internal table names, or platform exception messages.

On persistence failure, the API returns a canonical dependency/server error and does not claim a new count unless the persistence operation was confirmed successful.

## 4. CORS

Production CORS:

- Allow only the final approved resume origin.
- Allow method: `GET`.
- Allow request headers: `Content-Type`, `Accept`, `X-Request-ID`.
- Do not use `*` as the production allowed origin.
- Do not allow credentials unless a new approved requirement introduces authenticated browser behavior.

The final origin is intentionally not frozen until the public hostname/delivery decisions are resolved.

## 5. Versioning and Compatibility

- The MVP endpoint path is fixed as `/api/visitors`.
- The response field `count` and its type are immutable for the MVP.
- Additive response fields may be introduced only as backward-compatible changes and must not alter the meaning of existing fields.
- Existing fields cannot be renamed, removed, or change type in v1.
- New required request fields are not backward compatible and require v2.
- Enum additions are compatible only where clients are specified to tolerate unknown values; v1 has no request enums.
- HTTP status meanings in this document are contractual.
- Breaking changes to the MVP wire contract require an explicit contract update and corresponding verification.
- Documentation-only corrections that do not change wire behavior do not require a version increment.
- Contract version follows semantic versioning; API major version is independent of documentation patch/minor revisions.

## 6. Cross-Reference

| Contract area | Requirements | Architecture |
|---|---|---|
| Public counter call | REQ-AZ-007, REQ-AZ-009 | ADR-002 |
| Persistent count | REQ-AZ-008 | ADR-003 |
| Python Function | REQ-AZ-010 | ADR-002 |
| Security boundary | REQ-AZ-SEC-002, REQ-AZ-SEC-003 | SECURITY-ARCHITECTURE.md |
| Visitor semantics | REQ-AZ-007..009 | ADR-007 / OR-001 |

## 7. Freeze Gates

Before production acceptance, resolve:

1. OR-004 — HTTPS/CDN and final production origin.
2. OR-005 — final public resume content approval.
3. OR-010 — browser support baseline.
4. OR-011 — availability target, if required.
5. OR-012 — DNS propagation/stability expectation.

No unresolved gate may be silently implemented as a new requirement.
