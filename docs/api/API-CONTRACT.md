# API / Interface Contract

## 1. Document Control

| Field | Value |
|---|---|
| Contract | Azure Cloud Resume Challenge — API / Interface Contract |
| Contract version | 1.1.0 |
| API contract revision | v1 |
| Status | **Implementation-ready; production evidence pending** |
| Public application operation | VC-001 — `GET /api/visitors` |
| Runtime | Azure Functions Flex Consumption (FC1), Linux, Functions v4, Python 3.12 |
| Persistence | Azure Cosmos DB Table API, serverless |
| Public caller | Resume browser JavaScript |
| Public API authentication | None |
| Public API authorization | Public counter invocation; no user/tenant ownership model |
| Source requirements | REQ-AZ-007..010, REQ-AZ-SEC-002..003 |
| Verification | VT-007..010, VT-SEC-002..003 |
| Architecture | ADR-002, ADR-003, ADR-005, ADR-007, DATA-MODEL.md, SECURITY-ARCHITECTURE.md |
| Decision sources | D-032, D-036, D-037 |

This document is the authoritative wire/interface contract for Phase 4. It does not define controller/service implementation code.

## 2. Scope

The approved application has one public application endpoint:

`GET /api/visitors`

The endpoint performs the approved visitor-counter operation and returns the resulting persisted count.

Architecturally significant non-public interfaces are also frozen here:

- DB-001 — Azure Function to Cosmos DB Table API counter persistence.
- DEP-001 — Frontend GitHub Actions to Azure Storage/static delivery publication.
- DEP-002 — Backend GitHub Actions to ARM/Azure Function/Cosmos infrastructure and application deployment.
- DNS-001 — Public FreeDNS hostname to the approved HTTPS/edge delivery endpoint.

No additional public application endpoint is introduced.

## 3. Frozen Cross-Component Flow

```
Top-level resume page load
        |
        | exactly one counter request
        v
Frontend JavaScript
        |
        | HTTPS GET /api/visitors
        v
Azure Function HTTP trigger
        |
        | authenticated backend data-plane access
        v
Cosmos DB Table API
        |
        | persisted counter result
        v
Azure Function
        |
        | HTTP 200 JSON
        v
Frontend JavaScript
        |
        | display returned count
        v
Visitor sees current committed count
```

Rules:

1. The browser never accesses Cosmos DB directly.
2. One top-level resume page load causes exactly one counter request.
3. A refresh is another page load and therefore another counter operation.
4. Each successfully committed operation increments the persisted count by exactly one.
5. Failed operations do not increment persisted state.
6. Concurrent successful operations must not lose increments.
7. The browser does not identify unique humans, sessions, IP addresses, devices, or users.
8. No API credential, Cosmos credential, token, connection string, or internal database identifier is exposed to the browser.

## 4. Contract Conventions

### 4.1 Naming

- HTTP paths: lowercase.
- JSON properties: lower camel case.
- HTTP header names: conventional HTTP casing; matching is case-insensitive.
- Error codes: uppercase snake case.
- Identifiers exposed by the API: UUID v4 only where an identifier is required.
- Cosmos `PartitionKey` and `RowKey` are internal and are not public API fields.

### 4.2 Media types

- Success response: `application/json`.
- Error response: `application/json`.
- VC-001 has no request body and therefore does not require `Content-Type`.

### 4.3 Date/time

The success response contains no date/time field.

If an error includes `error.details.timestamp`, it is RFC 3339/ISO 8601 UTC. Clients must not depend on the field being present.

### 4.4 Nullability

No success field is nullable.

Optional error metadata may be absent; present fields are non-null.

### 4.5 Compatibility

The MVP public route is fixed as `/api/visitors`.

Within the approved v1 contract:

- `count` remains required and remains a non-negative JSON integer.
- Existing fields cannot be renamed, removed, or change type without an approved contract change.
- New required request fields are not permitted for this bodyless operation without an approved contract change.
- Additive response metadata is compatible only if it does not change the meaning of existing fields and is separately reviewed.
- Any breaking change must update the contract and affected tests before dependent implementation changes.
- The current project does not introduce a second public endpoint or alternate versioned route.

The term "v1" identifies this frozen contract revision; it does not authorize adding a different route or versioning scheme.

---

# 5. Interface VC-001 — Visitor Counter HTTP Operation

## 5.1 Contract identity

| Item | Contract |
|---|---|
| Contract ID | VC-001 |
| Operation | Perform visitor-counter operation |
| Method | GET |
| Path | `/api/visitors` |
| Purpose | Atomically commit one visitor-counter increment and return the resulting persisted count |
| Caller | Public resume browser JavaScript |
| Server | Azure Function HTTP trigger |
| Priority | P1 |
| Requirements | REQ-AZ-007, REQ-AZ-008, REQ-AZ-009, REQ-AZ-010 |
| Acceptance | AC-007, AC-008, AC-009, AC-010 |
| Verification | VT-007, VT-008, VT-009, VT-010 |

## 5.2 Architecture components involved

- Frontend HTML/CSS/JavaScript.
- Azure Storage static website.
- Approved HTTPS/CDN/edge delivery path for the public website.
- Azure Function Flex Consumption FC1.
- Python 3.12 Function runtime.
- Azure Function system-assigned managed identity.
- Azure Cosmos DB Table API, serverless.
- GitHub Actions deployment control plane.

The edge service remains subject to ADR-006 implementation validation; this does not alter VC-001's route or payload.

## 5.3 Authentication

### Browser caller

No end-user authentication is required or permitted by the approved MVP.

The browser must not send:

- Bearer tokens.
- API keys.
- Client secrets.
- Cosmos credentials.
- Azure credentials.

### Function-to-Cosmos

The Function authenticates to Cosmos DB using its approved managed identity/data-plane authorization.

No Cosmos connection string, account key, SAS token, or equivalent secret is part of the public contract.

## 5.4 Authorization

The public operation is intentionally callable without an end-user identity.

Authorization boundaries are:

1. The browser may invoke only the public counter operation.
2. The browser cannot select a database entity, partition, row, or arbitrary operation.
3. The Function identity may access only the approved visitor-counter data operation.
4. Deployment identities are separate from the runtime Function identity.
5. There is no user/tenant ownership model for the counter.

A backend Cosmos authorization failure is an internal configuration/security failure and must never be exposed as a public database authorization detail.

## 5.5 CORS

Production browser access:

- Allowed origin: the final approved resume origin.
- Allowed method: `GET`.
- Allowed request headers, if supplied: `Accept`, `X-Request-ID`; `Content-Type` may be permitted by platform configuration but is not required by VC-001.
- Credentials: not allowed.
- Wildcard production origin: prohibited.

The exact origin value is deployment configuration derived from the approved public hostname. It is not hardcoded in this contract because the final hostname/edge deployment evidence is an implementation gate.

A browser-origin/CORS rejection is a browser/platform boundary failure, not a VC-001 application JSON error. The browser must not treat a CORS failure as proof of a particular backend status.

## 5.6 Path parameters

None.

## 5.7 Query parameters

None.

Any query parameter is outside the VC-001 contract. The implementation may reject such requests as `400 BAD_REQUEST`; it must not use query parameters to select database state or alter counter semantics.

## 5.8 Required headers

| Header | Required | Rule |
|---|---:|---|
| `Origin` | Browser-generated | Must match the configured production CORS origin |
| `Accept` | Recommended | `application/json` |
| `Content-Type` | No | No request body is defined |

## 5.9 Optional headers

| Header | Rule |
|---|---|
| `X-Request-ID` | Optional UUID v4 correlation identifier. If absent, server generates one for error correlation/logging. If present and invalid, return `400 BAD_REQUEST`. |

No authentication or idempotency header is supported.

## 5.10 Request body

**No request body.**

The request is bodyless:

```http
GET /api/visitors HTTP/1.1
Accept: application/json
```

A client must not send a JSON request object as part of the normal operation.

Malformed or unsupported request data is not used to modify counter behavior.

## 5.11 Field-level validation

| Input | Validation |
|---|---|
| HTTP method | Must be GET |
| Path | Must exactly match `/api/visitors` |
| Query string | No application query parameters accepted |
| Request body | Not defined; must not be required |
| Origin | Production browser origin must pass CORS policy |
| Accept | If supplied, should permit `application/json` |
| X-Request-ID | If supplied, must be UUID v4 |
| Authentication fields | None accepted |
| Database fields | None accepted |
| Response count | Integer >= 0 |

The Function must not execute arbitrary database operations based on caller-supplied fields.

## 5.12 Request example

```http
GET /api/visitors HTTP/1.1
Host: api.example.invalid
Origin: https://resume.example.invalid
Accept: application/json
X-Request-ID: 7d3f4a22-1b4f-4d7b-9c0d-7f1c4a8b2d10
```

The hostnames above are documentation placeholders only.

## 5.13 Success response

### Status

`200 OK`

### Headers

```
Content-Type: application/json
```

### Schema

```json
{
  "count": 42
}
```

Rules:

- `count` is required.
- `count` is a JSON integer.
- `count >= 0`.
- `count` is the persisted count after the current operation has been successfully committed.
- The server must not return a value that it has not confirmed as successfully persisted.

### Success example

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"count":42}
```

## 5.14 Expected errors

| Status | Code | Contract meaning |
|---:|---|---|
| 400 | `BAD_REQUEST` | Request is malformed or violates the request contract |
| 405 | `METHOD_NOT_ALLOWED` | HTTP method is not supported |
| 429 | `RATE_LIMITED` | Platform or approved runtime throttling rejects the request |
| 500 | `INTERNAL_ERROR` | Unexpected server/runtime/configuration failure |
| 503 | `DEPENDENCY_UNAVAILABLE` | Required downstream dependency is unavailable |
| 504 | `DEPENDENCY_TIMEOUT` | Required downstream dependency exceeded its configured time boundary |

The contract does not require a 401/403 response for public browser invocation because no end-user authentication/authorization exists.

A Cosmos 401/403 caused by backend identity/RBAC configuration is an internal server-side failure and must map to a safe public error, normally `500 INTERNAL_ERROR`, with the authorization failure recorded server-side.

A CORS rejection is not represented by this JSON error envelope.

## 5.15 Error semantics

### 400 — BAD_REQUEST

Use when the request itself violates the interface.

Client behavior: do not retry unchanged input.

Server behavior: do not mutate counter state.

### 405 — METHOD_NOT_ALLOWED

Use when a method other than GET reaches the endpoint.

Client behavior: do not retry using the same unsupported method.

Server behavior: do not mutate counter state.

### 429 — RATE_LIMITED

Use only when throttling is actually applied by the platform/runtime.

Client behavior: no automatic retry policy is mandated by this contract because VC-001 is non-idempotent. If a future client retry is approved, it must use bounded backoff and an explicit duplicate-counting decision.

Server behavior: do not claim a committed increment.

### 500 — INTERNAL_ERROR

Use for unexpected application/runtime/configuration failures.

Client behavior: treat the counter as unavailable; continue displaying the resume.

Server behavior: log the failure with correlation ID; do not expose internal details.

### 503 — DEPENDENCY_UNAVAILABLE

Use when a required dependency is confirmed unavailable before a successful counter commit.

Client behavior: treat the counter as unavailable. No automatic retry is required.

Server behavior: log dependency failure and do not claim a new count.

### 504 — DEPENDENCY_TIMEOUT

Use when a required dependency exceeds the configured timeout boundary before the Function can confirm successful completion.

Client behavior: treat the counter result as unknown/unavailable. The frontend must not automatically retry because a timed-out operation may have committed.

Server behavior: log the timeout and preserve safe error exposure. The server must not report a new count unless persistence success is confirmed.

## 5.16 Error schema

All application-generated errors use:

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

Required fields:

- `error.code`
- `error.message`
- `error.requestId`

Optional:

- `error.details`
- `error.details.timestamp`

Messages must not contain:

- Stack traces.
- Secrets.
- Credentials.
- Tokens.
- Connection strings.
- Raw Cosmos errors.
- Internal resource names unless explicitly necessary for safe operations.

## 5.17 Error examples

### Invalid request

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "error": {
    "code": "BAD_REQUEST",
    "message": "The request is invalid.",
    "requestId": "9b2a9e1f-1f9c-4a70-8a73-7c1d2d2a6a50"
  }
}
```

### Dependency unavailable

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

### Dependency timeout

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

### Unexpected failure

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

## 5.18 Rate limiting/throttling

No application-specific rate limit or quota is approved as a product requirement.

If Azure Functions/platform throttling occurs:

- The public contract may surface `429 RATE_LIMITED`.
- The response must use the canonical error envelope.
- No increment may be claimed unless the operation was successfully committed.
- Throttling telemetry must be visible to operations.
- The exact provider limit is not part of the application contract.

## 5.19 Idempotency and state behavior

VC-001 is intentionally **non-idempotent**.

A successful request represents one successfully committed visitor-counter operation.

Therefore:

- Two successful requests represent two operations and increment by two.
- A page refresh represents another operation.
- No `Idempotency-Key` is defined.
- The frontend performs exactly one request per top-level page load.
- The frontend must not automatically retry a request after timeout or unknown outcome.
- The server may retry a known optimistic-concurrency conflict before a commit is confirmed, but must not blindly repeat an operation whose previous persistence outcome is unknown.

This preserves the approved invariant:

> If persisted count is N before K successfully committed operations, the resulting persisted count is N + K.

## 5.20 Persistence/data interaction

VC-001 maps to DB-001.

The successful request must:

1. Read the single logical visitor-counter entity.
2. Increment the persisted count by exactly one.
3. Commit the update using a concurrency-safe mechanism.
4. Return the resulting persisted count.

If the entity is missing:

1. Treat it as initialization of the single logical counter.
2. The first successfully committed operation produces count 1.
3. Concurrent initialization must not create a second logical counter or lose an increment.

No reset/delete operation exists.

## 5.21 Dependency interactions

Required dependency chain:

```
Browser
  -> Azure Function HTTP trigger
  -> Cosmos DB Table API
  -> Azure Function response
  -> Browser display
```

The Function is the only application boundary permitted to access Cosmos DB.

## 5.22 Timeout/failure behavior

The exact numeric dependency timeout is not fixed by Phase 0–3 requirements and therefore is intentionally not invented here.

The interface requirement is semantic:

- Dependency waits must be bounded by the runtime's approved configuration.
- A confirmed dependency timeout maps to 504.
- An unknown outcome must not be retried automatically by the browser.
- The Function must not return a new count unless the persistence result is known.
- Failed operations must not intentionally mutate state.

The numeric timeout value is a Phase 5 configuration decision and must be recorded before production implementation acceptance.

## 5.23 Security requirements

- HTTPS for production public traffic.
- No browser-to-Cosmos connectivity.
- No Cosmos credentials in browser artifacts.
- No Azure deployment credentials in browser artifacts.
- Managed identity for Function-to-Cosmos access.
- Least-privilege data-plane authorization.
- No arbitrary database operation inputs.
- Controlled error responses.
- No secrets or tokens in logs.
- No unnecessary visitor-identifying data.
- CORS restricted to the approved production origin.
- No end-user authentication feature introduced.

## 5.24 Logging/audit requirements

The Function should produce structured operational logs sufficient to correlate:

- Request outcome.
- HTTP status.
- Request/correlation ID.
- Validation failures.
- Dependency failures.
- Dependency timeouts.
- Unexpected runtime failures.
- Concurrency conflicts/retries where observable.

Do not log:

- Credentials.
- Tokens.
- Connection strings.
- Full sensitive headers.
- IP addresses or visitor-identifying data.
- Raw Cosmos error payloads if they contain internal details.

No separate audit-log product is required by the approved architecture.

## 5.25 Observability

Minimum operational signals:

- Function invocation count.
- Function failure count.
- HTTP status distribution.
- Function duration.
- Cosmos operation failures.
- CI test/deployment failures.
- Frontend API request failures as observable in browser diagnostics.

The visitor count itself is application data, not an operational metric.

## 5.26 Test/verification IDs

| Requirement | Tests |
|---|---|
| REQ-AZ-007 | VT-007 |
| REQ-AZ-008 | VT-008 |
| REQ-AZ-009 | VT-009 |
| REQ-AZ-010 | VT-010 |
| REQ-AZ-SEC-002 | VT-SEC-002 |
| REQ-AZ-SEC-003 | VT-SEC-003 |

The later Phase 6 test strategy must expand these into positive, negative, validation, concurrency, persistence, failure, contract and security cases.

## 5.27 Acceptance criteria

VC-001 is accepted when all applicable AC-007 through AC-010 conditions are satisfied, including:

- exactly one counter request per top-level page load;
- successful operation returns the resulting persisted count;
- failed operations do not increment state;
- concurrent successful operations do not lose increments;
- browser has no direct Cosmos DB access;
- API request/response/error behavior matches this contract;
- CORS matches the approved production origin;
- Function uses the approved Python/Azure Functions runtime and restricted data access;
- public error responses are safe.

---

# 6. Interface DB-001 — Function to Cosmos DB Counter Persistence

## 6.1 Contract identity

| Item | Value |
|---|---|
| Contract ID | DB-001 |
| Interface | VisitorCounter persistence operation |
| Caller | Azure Function runtime |
| Callee | Azure Cosmos DB Table API |
| Requirements | REQ-AZ-008, REQ-AZ-010, REQ-AZ-SEC-003 |
| Verification | VT-008, VT-010, VT-SEC-003 |

This is an internal data-plane interface, not a public HTTP endpoint.

## 6.2 Purpose

Persist the single logical counter while guaranteeing that concurrent successful operations do not silently overwrite one another.

## 6.3 Authentication

Function system-assigned managed identity using the approved Cosmos DB Table data-plane authorization.

No browser credential is involved.

## 6.4 Authorization

The Function identity may read/update the approved visitor-counter data only.

It must not:

- administer the Cosmos account;
- alter unrelated tables;
- receive arbitrary entity/table names from the browser;
- expose database access to the browser.

## 6.5 Logical entity schema

| Field | Type | Public? | Rule |
|---|---|---:|---|
| `PartitionKey` | string | No | Stable internal partition identifier |
| `RowKey` | string | No | Stable internal entity identifier |
| `Count` | integer | No | Non-negative persisted count |

The exact key values are internal implementation/configuration values and are not part of the public HTTP contract.

## 6.6 Operation behavior

Logical operation:

```
read current entity
  -> increment Count by 1
  -> conditional/concurrency-safe write
  -> return committed Count
```

Missing entity behavior:

- Initialize the single logical entity.
- First successful operation produces Count = 1.
- A concurrent create/update race must be resolved without losing an increment.

## 6.7 Concurrency

The implementation must use the provider-supported concurrency mechanism, such as conditional entity version/ETag handling, to prevent lost updates.

Known conditional conflicts may be retried before the operation is committed.

The exact retry count/backoff is not part of the external contract and must be documented in Phase 5 configuration.

## 6.8 Failure mapping

| Internal condition | Public mapping |
|---|---|
| Entity missing and initialization succeeds | 200 |
| Conditional concurrency conflict, safely retried and committed | 200 |
| Dependency unavailable | 503 |
| Dependency timeout | 504 |
| Authentication/authorization misconfiguration | 500 |
| Unexpected SDK/runtime failure | 500 |
| Throttling | 429 where surfaced by the approved platform behavior |

A failed persistence operation must not be reported as successful.

## 6.9 Retry rules

- Retry known optimistic-concurrency conflicts only when the previous write attempt is known not to have committed.
- Do not blindly retry an operation after an ambiguous write outcome.
- Do not create a client-visible retry mechanism.
- Do not use retries to convert a single page load into multiple intended counter operations.

## 6.10 Persistence invariants

For persisted count N and K successfully committed operations:

`result = N + K`

The entity survives:

- frontend deployment;
- backend deployment;
- normal Function restart;
- Function cold start.

No reset/delete operation exists.

---

# 7. Interface DEP-001 — Frontend Production Publication

## 7.1 Contract identity

| Item | Value |
|---|---|
| Contract ID | DEP-001 |
| Interface | GitHub Actions → Azure Storage/static delivery |
| Requirements | REQ-AZ-004, REQ-AZ-005, REQ-AZ-014, REQ-AZ-SEC-001, REQ-AZ-SEC-003 |
| Verification | VT-004, VT-005, VT-014, VT-SEC-001, VT-SEC-003 |

## 7.2 Trigger

Approved production frontend changes flow through the approved Git workflow and CI/CD authority. `main` represents production.

## 7.3 Authentication

GitHub Actions uses the approved Microsoft Entra OIDC deployment identity.

No long-lived Azure credential is stored in frontend source.

## 7.4 Authorization

The frontend deployment identity may:

- publish approved static website artifacts to the production Storage account;
- perform only the required edge-cache invalidation operation, if the selected delivery service requires it.

It must not receive Cosmos DB or Function runtime permissions.

## 7.5 Inputs

- Approved `main` repository content.
- HTML.
- CSS.
- JavaScript.
- Other approved static assets.
- Non-secret deployment configuration.

No secret values are part of the source artifact.

## 7.6 Success

A successful deployment results in:

- expected static assets present in Azure Storage;
- approved delivery cache invalidated when required;
- workflow reports success only after its defined validation gates pass.

## 7.7 Failure

- Validation failure blocks publication.
- Storage publication failure blocks successful workflow completion.
- Cache invalidation failure blocks successful completion if invalidation is required by the final delivery architecture.
- No production-success claim may be made from a failed workflow.

## 7.8 Verification

VT-004 and VT-014, plus the applicable security and delivery tests.

---

# 8. Interface DEP-002 — Backend Production Deployment

## 8.1 Contract identity

| Item | Value |
|---|---|
| Contract ID | DEP-002 |
| Interface | GitHub Actions → ARM/Azure Function/Cosmos infrastructure |
| Requirements | REQ-AZ-010..013, REQ-AZ-SEC-001, REQ-AZ-SEC-003, REQ-AZ-DEV-001, REQ-AZ-FLEX-001..013 |
| Verification | VT-010..013, VT-SEC-001, VT-SEC-003, VT-IAC-001, VT-FLEX-001..013 |

## 8.2 Required pipeline sequence

```
checkout
 -> dependency installation
 -> Python tests
 -> package/application validation
 -> ARM validation
 -> infrastructure deployment
 -> Function deployment
 -> post-deployment verification
```

The exact workflow implementation is not part of this wire contract.

## 8.3 Authentication

GitHub Actions uses the approved Microsoft Entra OIDC deployment identity.

The Function runtime uses its separate system-assigned managed identity.

## 8.4 Authorization

Deployment identity permissions are limited to the approved project deployment scope.

Runtime identity permissions are narrower and limited to required Function runtime/data operations.

## 8.5 Success

Production deployment is successful only when:

- required tests pass;
- ARM validation passes;
- infrastructure deployment succeeds;
- Function deployment succeeds;
- required post-deployment checks succeed;
- workflow reports success.

## 8.6 Failure

Any required pre-deployment test or deployment gate failure blocks successful production status.

No manual laptop deployment is a substitute for the approved production workflow.

## 8.7 Verification

VT-011, VT-012, VT-013, VT-IAC-001 and the applicable Flex verification IDs.

---

# 9. Interface DNS-001 — Public Hostname Resolution

## 9.1 Contract identity

| Item | Value |
|---|---|
| Contract ID | DNS-001 |
| Interface | FreeDNS hostname → approved HTTPS/edge delivery endpoint |
| Requirements | REQ-AZ-006, REQ-AZ-015 |
| Verification | VT-006, VT-015 |

## 9.2 Frozen behavior

The MVP public hostname is a FreeDNS hosted hostname/subdomain.

It must resolve publicly to the approved HTTPS/edge delivery endpoint, which uses Azure Storage as origin.

The project must not claim ownership of a conventional registrable paid domain.

## 9.3 Security

- Public DNS resolution is unauthenticated.
- DNS management is restricted to the project owner/provider account.
- The public hostname must match the certificate/delivery configuration.
- DNS configuration must not expose Azure credentials.

## 9.4 Acceptance

DNS-001 passes only when external resolution, endpoint association, HTTPS and public resume delivery all succeed.

---

# 10. Explicit Non-Interfaces

The following are intentionally not public interfaces:

- Cosmos DB directly from browser.
- Cosmos DB credentials/token endpoint.
- Authentication/login endpoint.
- Admin/reset endpoint.
- Analytics endpoint.
- User/profile endpoint.
- Public health endpoint.
- Pagination/filtering/sorting endpoint.
- Direct Azure management API exposed to browser.

Any new interface requires a controlled requirements/architecture/contract change.

---

# 11. Contract-Level Security Review

| Control | Contract requirement | Verification |
|---|---|---|
| Browser-to-Cosmos isolation | Browser cannot access Cosmos DB | VT-SEC-002 |
| Secret protection | No credentials/tokens in public contract or browser | VT-SEC-001 |
| Least privilege | Function/deployment identities have only required permissions | VT-SEC-003 |
| HTTPS | Public production traffic uses HTTPS | VT-SEC-004 |
| CORS | Production origin allowlist; no wildcard | VT-009 |
| Error safety | No stack traces/secrets/internal database details | VT-009, VT-010 |
| Input validation | No arbitrary database operation inputs | VT-009 |
| Privacy | No identity/analytics fields introduced | VT-007, VT-008 |
| Non-idempotent retry safety | No blind client retries after unknown outcome | VT-007, VT-008 |

---

# 12. Contract-Level QA Review

Required test categories:

- Happy path.
- Request/method validation.
- Error envelope and exact status mapping.
- CORS allow/deny behavior.
- Persistence.
- Initial entity creation.
- Concurrent operations.
- Conditional concurrency conflict.
- Dependency unavailable.
- Dependency timeout.
- Internal authorization/configuration failure.
- Unexpected server failure.
- Rate limiting where platform behavior is exercised.
- Duplicate/repeated requests.
- Timeout/unknown-outcome behavior.
- Response consistency.
- Browser/Cosmos isolation.
- No secret exposure.
- Regression of frontend display behavior.
- CI/CD deployment gating.

The Phase 6 test strategy must map each applicable case to a unique Test ID.

---

# 13. Contract Acceptance Gate

The API/interface contract is implementation-ready when:

1. VC-001 is the only public application endpoint.
2. GET `/api/visitors` is implemented exactly as specified.
3. Request/response/error schemas match this document.
4. Visitor semantics match the approved OR-001/D-032 decision.
5. Persistence and concurrency behavior match OR-007/D-037.
6. Browser-to-Cosmos isolation is preserved.
7. Authentication/authorization boundaries are preserved.
8. CORS uses the final approved production origin.
9. Error responses do not expose sensitive implementation details.
10. Required verification IDs are mapped.
11. No undocumented public interface is introduced.
12. Deployment interfaces remain governed by GitHub Actions and approved identities.

## 13.1 Known implementation gates, not contract ambiguities

- Final HTTPS/CDN service must satisfy ADR-006 capability/cost/availability conditions.
- Final public hostname must be provisioned and verified.
- Exact dependency timeout configuration must be recorded.
- Exact backend concurrency retry/backoff configuration must be recorded.
- Production OIDC/RBAC execution evidence must pass.
- Production API, persistence, CORS, security and end-to-end evidence must pass.

These gates do not authorize changing the API contract.

## 13.2 Contract exit criterion

**CONTRACT READY** means a frontend/backend implementer can build against this document without reading backend source code to discover request, response, error, security, persistence-boundary or deployment-interface behavior.