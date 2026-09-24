# Test Strategy

## 1. Document Control

| Field | Value |
|---|---|
| System | Azure Cloud Resume Challenge |
| Test Strategy | Complete |
| Test Design Status | Complete |
| Execution Status | Pending implementation |
| Frontend Repository | `s1xte3n/sixteen-resume-frontend` |
| Backend Repository | `s1xte3n/sixteen-resume-backend` |
| Production Branch | `main` |
| Integration Branch | `develop` |
| Target Cloud | Microsoft Azure |
| Target Region | East US |
| Primary API | `GET /api/visitors` |
| API Contract | v1.0.0 |
| Persistence | Azure Cosmos DB Table API |
| Backend | Python Azure Functions |
| IaC | ARM |
| CI/CD | GitHub Actions |

---

# 2. Purpose

This strategy defines how the Azure Cloud Resume Challenge is verified before merge,
deployment, and production release.

The strategy verifies:

- functional correctness;
- requirement compliance;
- API contract compliance;
- persistence correctness;
- concurrency correctness;
- security boundaries;
- frontend behavior;
- Azure infrastructure;
- Infrastructure as Code;
- CI/CD sequencing;
- deployment behavior;
- DNS and HTTPS;
- cost constraints;
- failure handling;
- regression behavior.

A successful HTTP status alone is never sufficient evidence of a passing test.

Every applicable test must assert the complete behavior required by the associated
requirement.

---

# 3. Quality Principles

## 3.1 Requirement Traceability

Every requirement must map to one or more verification tests.

Every P0/P1 requirement must have executable or objectively verifiable evidence.

## 3.2 Business Behavior Over Transport Status

A `2xx` response is not automatically a pass.

Tests must validate:

- status;
- response shape;
- field types;
- field values;
- headers;
- persistence;
- state transitions;
- security behavior;
- side effects;
- error semantics.

## 3.3 No False Positives

A test must fail when the implementation violates the requirement even if the
endpoint remains reachable.

Examples:

- `200` with an invalid response schema = FAIL.
- `200` without incrementing the counter = FAIL.
- `200` while exposing database credentials = FAIL.
- `200` after an invalid request that should return `400` = FAIL.
- `200` after persistence failure = FAIL.

## 3.4 Production Isolation

Automated tests must never mutate production counter state unless the test is
explicitly classified as a controlled production smoke test.

Default automated integration and persistence tests use isolated synthetic state.

## 3.5 Synthetic Data Only

No private resume information, production credentials, Azure keys, Cosmos
connection strings, access tokens, or personal secrets may exist in committed
test fixtures.

## 3.6 Security by Default

Tests verify that:

- browser code cannot access Cosmos DB;
- secrets are not committed;
- API errors do not disclose internal information;
- deployment identities are least privileged;
- production uses HTTPS;
- CORS follows the approved origin policy.

---

# 4. Test Levels

## 4.1 Static Analysis

Validates source and configuration without executing the complete system.

Examples:

- secret scanning;
- JSON validation;
- OpenAPI validation;
- ARM template validation;
- repository structure;
- dependency checks.

## 4.2 Unit Tests

Primary location:

`sixteen-resume-backend`

Validate:

- request validation;
- UUID validation;
- response construction;
- error mapping;
- counter business rules;
- persistence update logic;
- concurrency handling;
- exception handling.

## 4.3 API Contract Tests

Primary tool:

Postman.

Validate:

- HTTP method;
- endpoint;
- status;
- response schema;
- request validation;
- error envelope;
- request ID;
- CORS-related behavior where externally testable;
- absence of internal data.

## 4.4 Integration Tests

Validate:

- Azure Function -> Cosmos DB;
- Function identity;
- persistence;
- ARM provisioning;
- CI test-before-deployment behavior;
- frontend publication.

## 4.5 Browser Tests

Validate:

- HTML rendering;
- CSS;
- responsive behavior;
- JavaScript execution;
- visitor counter;
- failure UX;
- no direct Cosmos DB access.

## 4.6 End-to-End Tests

Validate the complete production flow:

DNS
-> HTTPS/CDN
-> Azure Storage
-> HTML/CSS/JS
-> Azure Function
-> Cosmos DB.

## 4.7 Regression Tests

Regression testing is required after changes to:

- requirements;
- API contract;
- visitor-counter code;
- persistence code;
- ARM templates;
- GitHub Actions;
- frontend JavaScript;
- CSS affecting layout;
- delivery/CDN configuration.

---

# 5. Requirement Coverage

The canonical MVP requirements are:

| Requirement | Priority |
|---|---:|
| REQ-AZ-001 | P1 |
| REQ-AZ-002 | P1 |
| REQ-AZ-003 | P1 |
| REQ-AZ-004 | P1 |
| REQ-AZ-005 | P1 |
| REQ-AZ-006 | P1 |
| REQ-AZ-007 | P1 |
| REQ-AZ-008 | P1 |
| REQ-AZ-009 | P1 |
| REQ-AZ-010 | P1 |
| REQ-AZ-011 | P1 |
| REQ-AZ-012 | P1 |
| REQ-AZ-013 | P1 |
| REQ-AZ-014 | P1 |
| REQ-AZ-015 | P0 |
| REQ-AZ-016 | P2 |

Cross-cutting requirements:

- REQ-AZ-SEC-001
- REQ-AZ-SEC-002
- REQ-AZ-SEC-003
- REQ-AZ-SEC-004
- REQ-AZ-COST-001
- REQ-AZ-REG-001
- REQ-AZ-GIT-001
- REQ-AZ-DEV-001
- REQ-AZ-DEV-002

Every requirement must have traceable verification evidence.

---

# 6. Test Types

The following test dimensions are applied where relevant.

| Test Type | Purpose |
|---|---|
| Positive | Valid behavior |
| Negative | Invalid behavior |
| Validation | Input/schema validation |
| Authentication | Authentication boundary |
| Authorization | Permission enforcement |
| Isolation | Data/resource isolation |
| State | State transitions |
| Boundary | Limits and edge values |
| Persistence | Durable state |
| Contract | API/interface compliance |
| Integration | Component interaction |
| Regression | Existing behavior after change |
| Security | Confidentiality/integrity/access controls |
| Failure | Dependency/runtime failure behavior |
| Concurrency | Atomicity/lost-update protection |
| Deployment | CI/CD behavior |
| Infrastructure | IaC/resource correctness |
| Browser | UI/runtime behavior |
| Compatibility | Browser/device support |

---

# 7. API Testing Strategy

API operation:

`GET /api/visitors`

Success:

```json
{
  "count": 42
}
