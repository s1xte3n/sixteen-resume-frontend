# API / Interface Contract Consistency Review

## 1. Review basis

Reviewed against the approved Phase 0–3 project artifacts in this repository:

- Project state and scope.
- PRD.
- Canonical requirements matrix.
- Acceptance criteria.
- Requirements traceability.
- Architecture.
- Data model.
- Security architecture.
- Infrastructure architecture.
- Observability architecture.
- Architecture decisions.
- Resolved product decisions D-032, D-036 and D-037.

This review does not introduce new product behavior.

## 2. Overall result

**Contract completeness: HIGH / implementation-ready for the approved API boundary.**

The public application interface is sufficiently defined for implementation:

- `GET /api/visitors`
- no end-user authentication;
- public invocation;
- explicit CORS policy;
- bodyless request;
- `200 { "count": integer }` success response;
- canonical error envelope;
- persistence/concurrency invariant;
- safe retry behavior;
- browser/Cosmos isolation.

The contract does not claim production acceptance or live Azure evidence.

## 3. Findings

| ID | Finding | Severity | Classification | Minimum action |
|---|---|---|---|---|
| CR-001 | ADR-INDEX.md previously labelled ADR-007 visitor semantics as “Pending approval” while REQUIREMENTS.md, OPEN-REQUIREMENTS.md, DECISIONS.md and DATA-MODEL.md treat the decision as resolved. | HIGH | Documentation/source-of-truth inconsistency | Synchronize ADR-007 status to Accepted; no product decision change is required. |
| CR-002 | API documents previously described a v1 API while using the fixed non-versioned route `/api/visitors`. | MEDIUM | Versioning ambiguity | Treat “v1” as the current frozen contract revision and require controlled contract change before any breaking modification; do not add a new route in MVP. |
| CR-003 | Production CORS origin depends on the final approved public hostname, which is an implementation/configuration value rather than a contract-definition blocker. | MEDIUM | Deployment configuration gate | Populate the exact origin in environment/configuration before production acceptance and execute CORS verification. |
| CR-004 | Exact dependency timeout duration is not specified in Phase 0–3. | MEDIUM | Runtime configuration ambiguity | Define the numeric timeout in Phase 5 configuration; preserve 504 semantics. |
| CR-005 | Exact concurrency retry count/backoff is not specified in Phase 0–3. | MEDIUM | Runtime configuration ambiguity | Define bounded conflict-retry configuration in Phase 5; preserve the no-lost-increment invariant. |
| CR-006 | Architecture security documentation uses legacy `T-SEC-*` labels while the canonical requirements/traceability use `VT-SEC-*`. | MEDIUM | Verification-ID documentation inconsistency | Normalize to the canonical Phase 2 `VT-SEC-*` IDs in future documentation; do not create duplicate tests. |
| CR-007 | Exact Azure edge/CDN service remains an implementation validation gate under ADR-006. | MEDIUM | Infrastructure implementation gate | Select a service only if it satisfies frozen HTTPS, hostname, Storage-origin, IaC and R100/month conditions. |
| CR-008 | Exact production hostname value is not frozen in the contract artifacts even though the interpretation is resolved as a FreeDNS hosted hostname/subdomain. | LOW | Deployment configuration | Record the final hostname as configuration and use it as the production CORS origin. |

## 4. Requirements consistency

No requirement conflict was found in the approved product behavior for the visitor counter.

The following are mutually consistent:

- REQ-AZ-007 — browser requests/displays counter without direct Cosmos access.
- REQ-AZ-008 — persistent Cosmos Table state.
- REQ-AZ-009 — Azure Function HTTP boundary.
- REQ-AZ-010 — Python Azure Function with required permissions.
- REQ-AZ-SEC-002 — browser-to-Cosmos prohibition.
- REQ-AZ-SEC-003 — least-privilege deployment/runtime identities.
- OR-001/D-032 — visitor semantics.
- OR-006/D-036 — GET /api/visitors.
- OR-007/D-037 — one logical counter and concurrency-safe increment.

## 5. Undefined error states checked

Covered:

- malformed request;
- unsupported method;
- platform throttling;
- dependency unavailable;
- dependency timeout;
- unexpected runtime failure;
- backend authorization/configuration failure;
- CORS rejection;
- concurrency conflict;
- missing initial counter entity;
- ambiguous write outcome.

## 6. Authentication/authorization review

Public API authentication is explicitly none.

No hidden user authorization requirement remains.

The internal Function-to-Cosmos authorization boundary is explicitly managed identity + least privilege.

Deployment identity and runtime identity are separate.

## 7. Persistence review

Defined:

- one logical counter;
- internal `PartitionKey` / `RowKey` / `Count`;
- count >= 0;
- one increment per successfully committed operation;
- deployment survival;
- no reset/delete;
- concurrency-safe conditional update;
- no lost increments;
- no blind retry after unknown write outcome.

## 8. CORS review

Defined:

- production allowlist;
- no wildcard;
- GET only;
- no credentials;
- final hostname supplied through deployment configuration.

Only the exact deployed origin remains a configuration/evidence gate.

## 9. Security review

No public database credential, Azure credential, token, or internal database identifier is part of the interface.

Safe error exposure is defined.

The browser/Cosmos trust boundary is explicit.

## 10. QA testability

The contract is testable at:

- HTTP status;
- JSON schema;
- business invariant;
- persistence state;
- concurrency;
- duplicate/repeated request behavior;
- failure mapping;
- CORS;
- security isolation;
- CI/CD gates.

## 11. Phase 4 exit implications

The contract itself is ready for implementation.

Phase 4 must not be declared fully closed until the documentation inconsistencies CR-001 and CR-006 are synchronized and the contract artifacts are internally consistent. Runtime/configuration items CR-003 through CR-005 and infrastructure gate CR-007 may remain implementation gates without changing the contract.