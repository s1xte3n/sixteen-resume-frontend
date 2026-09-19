# Test Strategy

## Purpose
Canonical QA strategy derived from the approved PRD, requirements matrix, architecture, API contract, acceptance criteria, and test-data configuration.

**Core rule:** a 2xx response alone never constitutes a pass. API tests must assert status, response shape, business behavior, persistence/state, security, and side effects where applicable.

## Scope
Covers REQ-AZ-001..016, REQ-AZ-SEC-001..004, REQ-AZ-COST-001, REQ-AZ-REG-001, REQ-AZ-GIT-001, REQ-AZ-DEV-001..002 and their AC/VT evidence.

Out of scope: authentication/user accounts, visitor identity tracking, IP/device fingerprinting, analytics, counter reset/delete/admin APIs, additional entities, and production data as test data.

## Test levels
| Level | Purpose | Gate |
|---|---|---|
| Static/structural | HTML, schema, secret scan, ARM/config checks | PR |
| Unit | Validation, state transitions, error mapping, retry logic | PR |
| API/contract | VC-001 method/status/schema/error/header behavior | PR/integration |
| Integration | Function-Cosmos, IaC, CI/CD, permissions | integration/release |
| Browser/E2E | Resume rendering, counter flow, failure isolation | pre-release |
| Security | Secrets, direct DB access, least privilege, HTTPS | PR/release |
| Resilience | 500/503/504, throttling, concurrency | integration/release |
| Regression | P0/P1 smoke and changed-area regression | merge/release |

## Test principles
1. Requirements are the coverage source; acceptance criteria are pass/fail.
2. Every P0/P1 requirement has executable or evidence-based verification.
3. Tests are deterministic, synthetic, isolated, and repeatable.
4. Negative paths are first-class.
5. Stateful tests prove both API result and persisted state.
6. Security tests prove absence of forbidden access.
7. Production data is never copied into tests.
8. Unresolved requirements are blockers, not assumptions.
9. Evidence identifies environment, commit, test ID, timestamp, and relevant artifact.

## Authentication and authorization
Public VC-001 has no end-user authentication by approved contract. Authentication/authorization testing applies to CI/CD identities and the Function-to-Cosmos boundary. Public API authorization is constrained by the absence of privileged operations, CORS, and server-side access controls.

## Environments
Local uses unit/static tests and synthetic fixtures. Dev is the develop Git context; no dedicated Azure dev environment is approved. Test uses isolated synthetic state. Staging is optional and not permanent. Production is for final acceptance only.

## Entry criteria
Baselined requirement/contract; available test data; secure configuration; reproducible build; no silently overridden P0/P1 decision.

## Exit criteria
### Merge
P0/P1 tests pass; secret scan passes; changed contract tests pass; no P0/P1 defect; traceability updated.

### Production
AC-001..016 applicable checks pass; P0/P1 regression passes; HTTPS/DNS/CORS/cost evidence passes; CI proves tests precede deployment; no secrets; content approval exists.

## Risk focus
Highest risk: counter atomicity/concurrency, browser-to-Cosmos isolation, API error/schema mapping, HTTPS/CORS, secret exposure, test-before-deploy ordering, IaC reproducibility, and public content correctness.

## Evidence rule
Never record a test as passed from a status code alone. Capture response schema, state transition, persistence, security, and integration evidence when required by the test case.
