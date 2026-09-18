# Feature Backlog

## 1. Backlog Governance

This backlog contains only implementation-ready work.

Requirements that remain ambiguous, contradictory, or unverifiable are intentionally excluded and tracked in `REQUIREMENT-GAPS.md`.

No implementation task should be created from a blocked requirement until its blocking decision is resolved.

---

# 2. P0 — Critical

## BL-AZ-001 — Establish Production Security Baseline

**Requirement:** REQ-AZ-SEC-001, REQ-AZ-SEC-002

**Dependencies:** None

**Affected components:**

* Git repositories
* Frontend JavaScript
* Backend API
* Azure configuration

**Acceptance evidence:**

* No credentials committed.
* Browser has no Cosmos DB credentials or direct database access.
* Security review passes.

**Verification:** T-SEC-001, T-SEC-002

---

## BL-AZ-002 — Establish Production Acceptance Gate

**Requirement:** REQ-AZ-015

**Status:** BLOCKED — planning only; no implementation task until P1 dependencies are resolved.

**Blocking dependencies:**

* DNS interpretation
* CDN/HTTPS configuration
* visitor semantics
* cost ceiling
* public resume approval
* CI/CD
* API contract

**Verification:** T-AZ-015

---

# 3. P1 — Core Resume

## BL-AZ-003 — Prepare HTML Resume Structure

**Requirement:** REQ-AZ-002

**Dependencies:** REQ-AZ-001

**Affected components:**

* Frontend repository
* HTML resume

**Acceptance:**

* Resume is delivered as HTML.
* Browser renders core resume content without PDF/Word dependency.

**Verification:** T-AZ-002

---

## BL-AZ-004 — Implement Resume CSS

**Requirement:** REQ-AZ-003

**Dependencies:** BL-AZ-003

**Affected components:**

* CSS
* HTML

**Acceptance:**

* Intentional styling.
* Mobile readability.
* Desktop readability.
* CSS failure does not eliminate underlying content.

**Verification:** T-AZ-003

---

# 4. P1 — Azure Static Hosting

## BL-AZ-005 — Define Azure Storage Static Website IaC Boundary

**Requirement:** REQ-AZ-004, REQ-AZ-012

**Dependencies:** BL-AZ-003

**Affected components:**

* Azure Storage
* ARM templates

**Acceptance:**

* Static website resource is represented in source-controlled infrastructure.
* Production assets can be served through Azure Storage.

**Verification:** T-AZ-004, T-AZ-012

---

# 5. P1 — Backend Foundation

## BL-AZ-006 — Establish Python Azure Function Foundation

**Requirement:** REQ-AZ-010

**Dependencies:** None

**Affected components:**

* Azure Functions
* Python
* Backend repository

**Acceptance:**

* Function runtime is Python.
* HTTP-triggered backend can execute.
* Required data-access boundary can be represented.

**Verification:** T-AZ-010

---

## BL-AZ-007 — Establish ARM Backend Resource Definitions

**Requirement:** REQ-AZ-012

**Dependencies:** BL-AZ-006

**Affected components:**

* ARM
* Azure Function
* Function hosting plan
* Required backend resources

**Acceptance:**

* Required backend infrastructure is source controlled.
* Consumption-plan direction is represented.
* Normal provisioning does not depend on undocumented manual configuration.

**Verification:** T-AZ-012

---

# 6. P1 — CI/CD Foundation

## BL-AZ-008 — Establish Backend Repository Workflow

**Requirement:** REQ-AZ-013

**Dependencies:** REQ-AZ-011, REQ-AZ-012

**Status:** BLOCKED until repository naming is normalized and testing framework is selected.

**Verification:** T-AZ-013

---

## BL-AZ-009 — Establish Frontend Repository Workflow

**Requirement:** REQ-AZ-014

**Dependencies:** REQ-AZ-004

**Status:** BLOCKED until repository naming and delivery configuration are normalized.

**Verification:** T-AZ-014

---

# 7. P2 — Deferred Decisions

The following are **not implementation tasks**.

| Requirement | Reason excluded from executable backlog     |
| ----------- | ------------------------------------------- |
| REQ-AZ-007  | Visitor semantics unresolved                |
| REQ-AZ-008  | Visitor semantics unresolved                |
| REQ-AZ-009  | API contract unresolved                     |
| REQ-AZ-011  | Testing framework unresolved                |
| REQ-AZ-016  | Blog platform/content definition unresolved |

---

# 8. Explicitly Blocked Work

The following must remain in the requirements-gap process:

1. Final HTTPS/CDN implementation.
2. Final DNS implementation.
3. Visitor-counter implementation semantics.
4. Final visitor-counter API contract.
5. Production cost validation.
6. Final public resume content.
7. Final repository-name normalization.
8. Blog platform normalization.
9. Production acceptance.

These are not implementation tasks until their blocking requirements are resolved.

---

# 9. Backlog Entry Rule

A requirement enters the executable backlog only when:

* It has a stable requirement ID.
* Required inputs are known.
* Acceptance criteria are objectively testable.
* Dependencies are known.
* No unresolved P0/P1 decision changes the implementation shape.
* A verification ID exists.

Otherwise it belongs in `REQUIREMENT-GAPS.md`.
