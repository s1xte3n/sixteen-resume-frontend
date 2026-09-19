# Test Priorities and Execution Order

## Definitions
| Priority | Meaning | Failure effect |
|---|---|---|
| P0 | Security, data integrity, production-critical, or release-blocking | Immediate block |
| P1 | Core MVP and mandatory contract/integration | Blocks merge/release |
| P2 | Important supporting/resilience/compatibility behavior | Blocks when acceptance requires it |
| P3 | Refinement or extended evidence | Normally non-blocking |

## Canonical order
1. P0 static/security.
2. P0 data integrity: atomicity, concurrency, no-increment-on-failure.
3. P1 unit validation/state/error tests.
4. P1 API contract tests.
5. P1 integration: Function-Cosmos, IaC, identity, CI ordering.
6. P1 frontend/browser tests.
7. P1 production E2E.
8. P2 resilience/compatibility.
9. P3 extended regression/documentation.

## P0 IDs
T-SEC-001, T-SEC-002, T-SEC-004, T-DATA-001, T-DATA-002, T-REL-001.

A passing smoke test never overrides a failed state, persistence, security, contract, or release-gate assertion.
