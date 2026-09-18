# API Contract Changelog

## 1.0.0 — 2026-09-18

### Added

- Defined v1 public visitor-counter interface.
- Defined `POST /api/v1/visitor-count`.
- Defined empty request body.
- Frozen success response field `count`.
- Frozen canonical error envelope and error codes.
- Frozen UUID v4 request correlation ID format.
- Defined CORS contract without production hostname hardcoding.
- Defined versioning and backward-compatibility rules.
- Added representative HTTP examples.
- Added machine-readable OpenAPI 3.0 contract.

### Explicitly not resolved

- OR-001: exact definition of a visitor and increment/duplicate semantics.
- OR-002: free hostname/subdomain interpretation versus literal custom-domain requirement.
- OR-004: final HTTPS/CDN configuration and production origin.
- OR-009: final visitor-counter failure UX where client behavior is affected.

These are documented blockers and are not silently resolved by this contract.

## Decision record

| Decision | Requirement/architecture addressed | Decision |
|---|---|---|
| API boundary | REQ-AZ-009, ADR-002 | Azure Function is the sole browser-to-database application boundary |
| API versioning | Compatibility governance | URL version `v1` |
| State-changing operation | REQ-AZ-007..009 | `POST /api/v1/visitor-count` |
| Error envelope | VT-009 | Stable `code/message/requestId` structure |
| Correlation ID | Observability/security architecture | UUID v4 request correlation |
| Public auth | REQ-AZ-007 | No end-user authentication |
| CORS | REQ-AZ-007, REQ-AZ-SEC-002 | Production origin allowlist; no wildcard |
| Semantics | ADR-007 | Explicitly left pending OR-001 |

## Compatibility policy

Any future breaking wire-contract change requires a new API major version. Additive compatible changes may be released within v1 under the compatibility rules in `API-CONTRACT.md`.
