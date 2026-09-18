# Canonical Requirements Matrix

## 1. Purpose

This is the canonical traceability baseline derived from `docs/product/PRD.md`. It assigns every confirmed requirement a unique ID, priority, status, dependencies, affected components, acceptance criterion, and verification ID.

## 2. Status and Priority

| Status | Meaning |
|---|---|
| `BASELINED` | Sufficiently defined for implementation planning; no unresolved decision changes its required behavior. |
| `BLOCKED` | A P0/P1 ambiguity, contradiction, or required approval prevents implementation/acceptance. |
| `DEFERRED` | Requirement is confirmed but a lower-priority decision remains open. |
| `ACCEPTED-DEVIATION` | Deliberate project deviation from the original challenge. |
| `CLOSED` | Implementation and verification evidence demonstrate acceptance. |

| Priority | Meaning |
|---|---|
| P0 | Critical product/security requirement. |
| P1 | Core MVP requirement; must be resolved before affected acceptance. |
| P2 | Important requirement or lower-priority decision that does not invalidate the baseline. |
| P3 | Minor refinement. |

## 3. Canonical MVP Requirements

| ID | Requirement | Priority | Status | Dependencies | Affected components | Acceptance | Verification |
|---|---|---:|---|---|---|---|---|
| REQ-AZ-001 | Approved CV-derived resume content must be publicly readable without exposing rejected/private information. | P1 | BLOCKED | REQ-AZ-002..006; OR-005 | Resume content, HTML, production site | AC-001 | VT-001 |
| REQ-AZ-002 | Resume must be delivered as an HTML webpage without requiring Word/PDF viewing. | P1 | BASELINED | REQ-AZ-001, REQ-AZ-003 | HTML resume | AC-002 | VT-002 |
| REQ-AZ-003 | HTML resume must have intentional CSS styling and remain readable on mobile and desktop. | P1 | BASELINED | REQ-AZ-002 | HTML, CSS, UI | AC-003 | VT-003 |
| REQ-AZ-004 | Production static website must use Azure Storage static website hosting. | P1 | BASELINED | REQ-AZ-002, REQ-AZ-003 | Azure Storage, frontend | AC-004 | VT-004 |
| REQ-AZ-005 | Production delivery must provide HTTPS through the approved CDN/delivery architecture within the approved cost ceiling. | P1 | BLOCKED | REQ-AZ-004, REQ-AZ-006; OR-004 | CDN/delivery, certificate, Storage | AC-005 | VT-005 |
| REQ-AZ-006 | Production website must have an approved public hostname/DNS solution resolving to the intended delivery endpoint. | P1 | BLOCKED | REQ-AZ-005; OR-002 | DNS, delivery | AC-006 | VT-006 |
| REQ-AZ-007 | Browser JavaScript must request and display the approved visitor-counter result without direct Cosmos DB access. | P1 | BLOCKED | REQ-AZ-008..010; OR-008, OR-009 | JavaScript, API | AC-007 | VT-007 |
| REQ-AZ-008 | Visitor-counter state must persist in Azure Cosmos DB Table API and survive normal frontend/backend deployments. | P1 | BLOCKED | REQ-AZ-009, REQ-AZ-010; OR-008 | Cosmos DB, Function | AC-008 | VT-008 |
| REQ-AZ-009 | Browser must communicate with the visitor counter through an Azure Function HTTP API rather than directly with Cosmos DB. | P1 | BLOCKED | REQ-AZ-008, REQ-AZ-010; OR-008 | API, JavaScript, Function | AC-009 | VT-009 |
| REQ-AZ-010 | Visitor-counter processing must run on Python Azure Functions with only required data-access permissions. | P1 | BASELINED | REQ-AZ-008, REQ-AZ-009 | Function, Python | AC-010 | VT-010 |
| REQ-AZ-011 | Automated Python tests must execute before production backend deployment and results must be visible in CI. | P1 | DEFERRED | REQ-AZ-010, REQ-AZ-013; OR-006 | Tests, GitHub Actions | AC-011 | VT-011 |
| REQ-AZ-012 | Required Azure infrastructure must be represented in source-controlled ARM templates and provisionable without undocumented manual production configuration. | P1 | BASELINED | REQ-AZ-004, REQ-AZ-005, REQ-AZ-008, REQ-AZ-010 | ARM, Azure resources | AC-012 | VT-012 |
| REQ-AZ-013 | Backend code and infrastructure must use the canonical dedicated GitHub repository and CI/CD workflow that tests before production deployment. | P1 | BLOCKED | REQ-AZ-011, REQ-AZ-012; repository state/authentication | Backend repo, Actions, Azure | AC-013 | VT-013 |
| REQ-AZ-014 | Frontend code must use the canonical dedicated GitHub repository and CI/CD workflow that publishes approved production changes to Azure Storage. | P1 | BLOCKED | REQ-AZ-004, REQ-AZ-005; repository/delivery configuration | Frontend repo, Actions, Storage/CDN | AC-014 | VT-014 |
| REQ-AZ-015 | Public production deployment must integrate approved resume, HTTPS, hostname, counter, IaC, security controls, and cost constraint. | P0 | BLOCKED | REQ-AZ-001..014; OR-001, OR-002, OR-004, OR-005 | Entire product | AC-015 | VT-015 |
| REQ-AZ-016 | Resume must link to a publicly reachable project-learning article describing lessons learned. | P2 | DEFERRED | REQ-AZ-001; OR-007 | Resume, external article | AC-016 | VT-016 |

## 4. Cross-Cutting Requirements

| ID | Requirement | Priority | Status | Dependencies | Affected components | Verification |
|---|---|---:|---|---|---|---|
| REQ-AZ-SEC-001 | Azure credentials and secrets must never be committed to source control. | P0 | BASELINED | CI/CD configuration | Git repositories, Actions | VT-SEC-001 |
| REQ-AZ-SEC-002 | Browser JavaScript must never directly access Cosmos DB. | P0 | BASELINED | REQ-AZ-009 | Browser, API, Cosmos DB | VT-SEC-002 |
| REQ-AZ-SEC-003 | Deployment identities must use only permissions required for their responsibilities. | P1 | BASELINED | REQ-AZ-012, REQ-AZ-013, REQ-AZ-014 | GitHub Actions, Azure IAM | VT-SEC-003 |
| REQ-AZ-SEC-004 | Public production traffic must use HTTPS. | P0 | BLOCKED | REQ-AZ-005; OR-004 | Delivery layer | VT-SEC-004 |
| REQ-AZ-COST-001 | Services and infrastructure must remain within the approved numeric project cost ceiling of USD $40/month recurring Azure/cloud cost; R0/month is preferred and approved exclusions apply. | P1 | BASELINED | OR-003 (resolved) | Azure services, delivery | VT-COST-001 |
| REQ-AZ-REG-001 | Azure resources must target East US unless an approved change is recorded. | P2 | BASELINED | ARM configuration | Azure resources | VT-REG-001 |
| REQ-AZ-GIT-001 | `develop` is development/integration and `main` is production. | P1 | BLOCKED | Repository state normalization | GitHub repositories | VT-GIT-001 |
| REQ-AZ-DEV-001 | Production infrastructure must be reproducible from source-controlled IaC. | P1 | BASELINED | REQ-AZ-012 | ARM, Azure | VT-IAC-001 |

## 5. Deliberate Deviation

| ID | Requirement | Priority | Status | Verification |
|---|---|---:|---|---|
| REQ-AZ-DEV-002 | The project may display AI-901 as an existing certification but must not claim AZ-900 compliance. | P1 | ACCEPTED-DEVIATION | VT-CERT-001 |

## 6. Quality Findings / Gaps

| ID | Classification | Affected requirements | Status |
|---|---|---|---|
| QF-001 | Visitor semantics resolved: one successfully committed counter operation per top-level resume page load, with concurrency-safe increments. | REQ-AZ-007..009, REQ-AZ-015 | RESOLVED / OR-001 |
| QF-002 | Free hostname versus original custom-domain interpretation is a deliberate scoped deviation. | REQ-AZ-006, REQ-AZ-015 | RESOLVED / OR-002 |
| QF-003 | Numeric cost ceiling was previously undefined. | REQ-AZ-005, REQ-AZ-006, REQ-AZ-012, REQ-AZ-015 | RESOLVED / OR-003 |
| QF-004 | Exact HTTPS/CDN configuration and cost suitability are unvalidated. | REQ-AZ-005, REQ-AZ-015 | OPEN / OR-004 |
| QF-005 | Final public CV subset is not approved. | REQ-AZ-001, REQ-AZ-015 | OPEN / OR-005 |
| QF-006 | Historical repository names conflict with canonical names. | REQ-AZ-013, REQ-AZ-014 | OPEN |
| QF-007 | Blog-platform documentation requires normalization. | REQ-AZ-016 | OPEN / OR-007 |
| QF-008 | Artifact-index filename references must use `UNRESOLVED-QUESTIONS.md`. | Documentation | OPEN |

## 7. Requirement Rules

- No requirement with unresolved P0/P1 ambiguity may enter the executable backlog.
- A requirement is not `CLOSED` merely because its implementation exists; acceptance and verification evidence are required.
- Acceptance criteria remain the source of behavioral pass/fail conditions.
- `VT-*` verification IDs are the canonical verification IDs for this requirements phase.
- Changes to a requirement must be synchronized with PRD, acceptance criteria, traceability, dependency, gaps, and artifact-index documentation.
