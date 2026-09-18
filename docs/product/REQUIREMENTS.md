# Requirements Matrix

## 1. Purpose

This document is the canonical traceable requirements baseline for the Azure Cloud Resume Challenge.

It converts the approved PRD into uniquely identified, prioritized, dependency-aware, testable requirements.

### Requirement status values

| Status               | Meaning                                                                        |
| -------------------- | ------------------------------------------------------------------------------ |
| `BASELINED`          | Requirement is sufficiently defined for implementation/verification planning   |
| `BLOCKED`            | Requirement contains an unresolved P0/P1 ambiguity or contradiction            |
| `DEFERRED`           | Requirement is valid but a lower-priority implementation decision remains open |
| `ACCEPTED-DEVIATION` | Deliberately differs from the original Cloud Resume Challenge                  |
| `CLOSED`             | Requirement has implementation and verification evidence                       |

### Priority

| Priority | Meaning                                                                            |
| -------- | ---------------------------------------------------------------------------------- |
| P0       | Critical; blocks safe/product-valid progress                                       |
| P1       | High impact; must be resolved before affected MVP acceptance                       |
| P2       | Important; can be resolved during implementation without invalidating the baseline |
| P3       | Minor refinement                                                                   |

---

# 2. Canonical Requirements

| ID         | Requirement                                                                                                                                                                     | Priority | Status    | Dependencies                                               | Affected Components                                    | Acceptance Criteria | Verification |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------: | --------- | ---------------------------------------------------------- | ------------------------------------------------------ | ------------------- | ------------ |
| REQ-AZ-001 | Approved CV-derived resume content must be publicly readable without exposing rejected/private information.                                                                     |       P1 | BLOCKED   | REQ-AZ-002..006                                            | Resume content, HTML, production site                  | AC-001              | T-AZ-001     |
| REQ-AZ-002 | The resume must be delivered as an HTML webpage rather than requiring Word/PDF viewing.                                                                                         |       P1 | BASELINED | REQ-AZ-001, REQ-AZ-003                                     | HTML resume                                            | AC-002              | T-AZ-002     |
| REQ-AZ-003 | The HTML resume must have intentional CSS styling and remain readable on mobile and desktop viewports.                                                                          |       P1 | BASELINED | REQ-AZ-002                                                 | CSS, HTML                                              | AC-003              | T-AZ-003     |
| REQ-AZ-004 | The production static website must use Azure Storage static website hosting.                                                                                                    |       P1 | BASELINED | REQ-AZ-002, REQ-AZ-003                                     | Azure Storage, frontend repository                     | AC-004              | T-AZ-004     |
| REQ-AZ-005 | Production delivery must provide HTTPS through the approved CDN/delivery architecture while satisfying the approved cost constraint.                                            |       P1 | BLOCKED   | REQ-AZ-004, REQ-AZ-006                                     | CDN/delivery, certificate, Azure Storage               | AC-005              | T-AZ-005     |
| REQ-AZ-006 | The production website must have a public hostname/DNS solution resolving to the intended delivery endpoint.                                                                    |       P1 | BLOCKED   | REQ-AZ-005                                                 | DNS, CDN/delivery                                      | AC-006              | T-AZ-006     |
| REQ-AZ-007 | Browser JavaScript must request and display the approved visitor-counter result without directly accessing Cosmos DB.                                                           |       P1 | BLOCKED   | REQ-AZ-008..010                                            | JavaScript, API                                        | AC-007              | T-AZ-007     |
| REQ-AZ-008 | Visitor-counter state must persist in Azure Cosmos DB Table API and survive normal frontend/backend deployments.                                                                |       P1 | BLOCKED   | REQ-AZ-009, REQ-AZ-010                                     | Cosmos DB, Azure Function                              | AC-008              | T-AZ-008     |
| REQ-AZ-009 | The browser must communicate with the visitor counter through an Azure Function HTTP API rather than directly with Cosmos DB.                                                   |       P1 | BLOCKED   | REQ-AZ-008, REQ-AZ-010                                     | API, JavaScript, Azure Function                        | AC-009              | T-AZ-009     |
| REQ-AZ-010 | Visitor-counter API processing must run on Python Azure Functions with only required data-access permissions.                                                                   |       P1 | BASELINED | REQ-AZ-008, REQ-AZ-009, REQ-AZ-011                         | Azure Function, Python                                 | AC-010              | T-AZ-010     |
| REQ-AZ-011 | Automated Python tests must execute before production backend deployment and their results must be visible in CI.                                                               |       P1 | DEFERRED  | REQ-AZ-010, REQ-AZ-013                                     | Python tests, GitHub Actions                           | AC-011              | T-AZ-011     |
| REQ-AZ-012 | Required Azure infrastructure must be represented in source-controlled ARM templates and provisionable without undocumented manual production configuration.                    |       P1 | BASELINED | REQ-AZ-004, REQ-AZ-005, REQ-AZ-008, REQ-AZ-010, REQ-AZ-013 | ARM, Azure resources                                   | AC-012              | T-AZ-012     |
| REQ-AZ-013 | Backend code and infrastructure must use a dedicated GitHub repository and CI/CD workflow that tests before production deployment.                                              |       P1 | BLOCKED   | REQ-AZ-011, REQ-AZ-012                                     | Backend repository, GitHub Actions, Azure              | AC-013              | T-AZ-013     |
| REQ-AZ-014 | Frontend code must use a dedicated GitHub repository and CI/CD workflow that publishes approved production changes to Azure Storage.                                            |       P1 | BLOCKED   | REQ-AZ-004, REQ-AZ-005, repository-name decision           | Frontend repository, GitHub Actions, Azure Storage/CDN | AC-014              | T-AZ-014     |
| REQ-AZ-015 | A publicly accessible production deployment must integrate the approved resume, HTTPS delivery, hostname, visitor counter, IaC, security controls, and approved cost threshold. |       P0 | BLOCKED   | REQ-AZ-001..014                                            | Entire product                                         | AC-015              | T-AZ-015     |
| REQ-AZ-016 | The resume must link to a publicly reachable project-learning article describing lessons learned from the project.                                                              |       P2 | BLOCKED   | REQ-AZ-001                                                 | Resume, external blog                                  | AC-016              | T-AZ-016     |

---

# 3. Cross-Cutting Requirements

| ID              | Requirement                                                                                     | Priority | Status    | Verification |
| --------------- | ----------------------------------------------------------------------------------------------- | -------: | --------- | ------------ |
| REQ-AZ-SEC-001  | Azure credentials and secrets must never be committed to source control.                        |       P0 | BASELINED | T-SEC-001    |
| REQ-AZ-SEC-002  | Browser JavaScript must never directly access Cosmos DB.                                        |       P0 | BASELINED | T-SEC-002    |
| REQ-AZ-SEC-003  | Deployment identities must use only permissions required for their deployment responsibilities. |       P1 | BASELINED | T-SEC-003    |
| REQ-AZ-SEC-004  | Public production traffic must use HTTPS.                                                       |       P0 | BLOCKED   | T-SEC-004    |
| REQ-AZ-COST-001 | Infrastructure and services must remain within the explicitly approved project cost ceiling.    |       P1 | BLOCKED   | T-COST-001   |
| REQ-AZ-REG-001  | Azure resources must target East US unless an approved change is recorded.                      |       P2 | BASELINED | T-REG-001    |
| REQ-AZ-GIT-001  | `develop` is the development/integration branch and `main` is the production branch.            |       P1 | BLOCKED   | T-GIT-001    |
| REQ-AZ-DEV-001  | Production infrastructure must be reproducible from source-controlled IaC.                      |       P1 | BASELINED | T-IAC-001    |

---

# 4. Deliberate Challenge Deviation

| ID             | Requirement                                                         | Priority | Status             | Verification |
| -------------- | ------------------------------------------------------------------- | -------: | ------------------ | ------------ |
| REQ-AZ-DEV-002 | The project displays AI-901 rather than claiming AZ-900 compliance. |       P1 | ACCEPTED-DEVIATION | T-CERT-001   |

The approved project state explicitly documents AI-901 as the currently held certification and AZ-900 as a deliberate deviation.

The project must not represent AI-901 as equivalent to literal AZ-900 compliance.

---

# 5. Requirement Quality Findings

## QF-001 — Visitor Semantics

Affected requirements: REQ-AZ-007, REQ-AZ-008, REQ-AZ-009.

The term "visitor" is not objectively defined.

**Required before acceptance:** define whether counting represents page loads, API calls, sessions, unique visitors, or another unit.

## QF-002 — DNS Interpretation

Affected requirements: REQ-AZ-006 and REQ-AZ-015.

The original challenge specifies a custom domain, while the approved project state excludes paid domain purchase and selects FreeDNS.

**Required before acceptance:** explicitly approve whether the free hostname/subdomain interpretation satisfies project scope.

## QF-003 — Cost Constraint

Affected requirements: REQ-AZ-005, REQ-AZ-006, REQ-AZ-012, REQ-AZ-015.

"Zero/near-zero" and "R0 where possible" are not objectively testable.

**Required before acceptance:** define a numeric maximum.

## QF-004 — CDN Configuration

Affected requirements: REQ-AZ-005 and REQ-AZ-015.

The exact Azure HTTPS/CDN configuration has not been finalized.

**Required before acceptance:** validate service availability, certificate behavior, DNS behavior, and cost.

## QF-005 — Public Content Approval

Affected requirements: REQ-AZ-001 and REQ-AZ-015.

The CV is available, but the final public subset has not yet been approved.

## QF-006 — Repository Naming

The documentation contains both:

* `sixteen-frontend` / `sixteen-backend`
* `sixteen-resume-frontend` / `sixteen-resume-backend`

The actual repository requested for this requirements work is `sixteen-resume-frontend`.

This must be normalized before CI/CD requirements are considered closed.

## QF-007 — Blog Platform

Project-state documentation selects Dev.to and Hashnode, while the open-requirements document treats the platform as unresolved.

This must be normalized before REQ-AZ-016 is closed.

## QF-008 — Artifact Index Naming

The Artifact Index references `OPEN-QUESTIONS.md`, while the repository contains `UNRESOLVED-QUESTIONS.md`.

This is a documentation consistency defect.

---

# 6. Requirement Closure Rule

A requirement may move from `BLOCKED` or `DEFERRED` to `BASELINED` only when its unresolved decision is explicitly recorded in the appropriate project/product decision artifact.

A requirement may move to `CLOSED` only when:

1. Its acceptance criteria pass.
2. Its verification/test ID has evidence.
3. Its dependencies are satisfied.
4. Required implementation evidence exists.
5. Required CI/release evidence exists.
6. No unresolved higher-priority ambiguity invalidates the result.
