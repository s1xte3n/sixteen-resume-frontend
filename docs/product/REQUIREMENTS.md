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

> **Step 7 status rule:** `BASELINED` means the requirement is unblocked and sufficiently defined for implementation. It does **not** mean implemented or accepted. Final acceptance still requires the applicable acceptance/verification evidence and any explicitly retained implementation gate.

| Priority | Meaning |
|---|---|
| P0 | Critical product/security requirement. |
| P1 | Core MVP requirement; must be resolved before affected acceptance. |
| P2 | Important requirement or lower-priority decision that does not invalidate the baseline. |
| P3 | Minor refinement. |

## 3. Canonical MVP Requirements

| ID | Requirement | Priority | Status | Dependencies | Affected components | Acceptance | Verification |
|---|---|---:|---|---|---|---|---|
| REQ-AZ-001 | Approved CV-derived resume content must be publicly readable without exposing rejected/private information. | P1 | BASELINED | REQ-AZ-002..006; OR-005 | Resume content, HTML, production site | AC-001 | VT-001 |
| REQ-AZ-002 | Resume must be delivered as an HTML webpage without requiring Word/PDF viewing. | P1 | BASELINED | REQ-AZ-001, REQ-AZ-003 | HTML resume | AC-002 | VT-002 |
| REQ-AZ-003 | HTML resume must have intentional CSS styling and remain readable on mobile and desktop. | P1 | BASELINED | REQ-AZ-002 | HTML, CSS, UI | AC-003 | VT-003 |
| REQ-AZ-004 | Production static website must use Azure Storage static website hosting. | P1 | BASELINED | REQ-AZ-002, REQ-AZ-003 | Azure Storage, frontend | AC-004 | VT-004 |
| REQ-AZ-005 | Production delivery must provide HTTPS through the approved CDN/delivery architecture within the approved cost ceiling. | P1 | BASELINED | REQ-AZ-004, REQ-AZ-006; OR-004 | CDN/delivery, certificate, Storage | AC-005 | VT-005 |
| REQ-AZ-006 | Production website must have an approved public hostname/DNS solution resolving to the intended delivery endpoint. | P1 | BASELINED | REQ-AZ-005; OR-002 | DNS, delivery | AC-006 | VT-006 |
| REQ-AZ-007 | Browser JavaScript must request and display the approved visitor-counter result without direct Cosmos DB access. | P1 | BASELINED | REQ-AZ-008..010; OR-008, OR-009 | JavaScript, API | AC-007 | VT-007 |
| REQ-AZ-008 | Visitor-counter state must persist in Azure Cosmos DB Table API and survive normal frontend/backend deployments. | P1 | BASELINED | REQ-AZ-009, REQ-AZ-010; OR-008 | Cosmos DB, Function | AC-008 | VT-008 |
| REQ-AZ-009 | Browser must communicate with the visitor counter through an Azure Function HTTP API rather than directly with Cosmos DB. | P1 | BASELINED | REQ-AZ-008, REQ-AZ-010; OR-008 | API, JavaScript, Function | AC-009 | VT-009 |
| REQ-AZ-010 | Visitor-counter processing must run on Python Azure Functions with only required data-access permissions. | P1 | BASELINED | REQ-AZ-008, REQ-AZ-009 | Function, Python | AC-010 | VT-010 |
| REQ-AZ-011 | Automated Python tests must execute before production backend deployment and results must be visible in CI. | P1 | BASELINED | REQ-AZ-010, REQ-AZ-013; OR-006 | Tests, GitHub Actions | AC-011 | VT-011 |
| REQ-AZ-012 | Required Azure infrastructure must be represented in source-controlled ARM templates and provisionable without undocumented manual production configuration. | P1 | BASELINED | REQ-AZ-004, REQ-AZ-005, REQ-AZ-008, REQ-AZ-010 | ARM, Azure resources | AC-012 | VT-012 |
| REQ-AZ-013 | Backend code and infrastructure must use the canonical dedicated GitHub repository and CI/CD workflow that tests before production deployment. | P1 | BASELINED | REQ-AZ-011, REQ-AZ-012; repository state/authentication | Backend repo, Actions, Azure | AC-013 | VT-013 |
| REQ-AZ-014 | Frontend code must use the canonical dedicated GitHub repository and CI/CD workflow that publishes approved production changes to Azure Storage. | P1 | BASELINED | REQ-AZ-004, REQ-AZ-005; repository/delivery configuration | Frontend repo, Actions, Storage/CDN | AC-014 | VT-014 |
| REQ-AZ-015 | Public production deployment must integrate approved resume, HTTPS, hostname, counter, IaC, security controls, and cost constraint. | P0 | BASELINED | REQ-AZ-001..014; OR-001, OR-002, OR-004, OR-005 | Entire product | AC-015 | VT-015 |
| REQ-AZ-016 | Resume must link to a publicly reachable project-learning article describing lessons learned. | P2 | BASELINED | REQ-AZ-001; OR-007 | Resume, external article | AC-016 | VT-016 |

## 4. Cross-Cutting Requirements

| ID | Requirement | Priority | Status | Dependencies | Affected components | Verification |
|---|---|---:|---|---|---|---|
| REQ-AZ-SEC-001 | Azure credentials and secrets must never be committed to source control. | P0 | BASELINED | CI/CD configuration | Git repositories, Actions | VT-SEC-001 |
| REQ-AZ-SEC-002 | Browser JavaScript must never directly access Cosmos DB. | P0 | BASELINED | REQ-AZ-009 | Browser, API, Cosmos DB | VT-SEC-002 |
| REQ-AZ-SEC-003 | Deployment identities must use only permissions required for their responsibilities. | P1 | BASELINED | REQ-AZ-012, REQ-AZ-013, REQ-AZ-014 | GitHub Actions, Azure IAM | VT-SEC-003 |
| REQ-AZ-SEC-004 | Public production traffic must use HTTPS. | P0 | BASELINED | REQ-AZ-005; OR-004 | Delivery layer | VT-SEC-004 |
| REQ-AZ-COST-001 | Services and infrastructure must remain within the approved numeric project cost ceiling of R100/month recurring Azure/cloud cost; R0/month is preferred and approved exclusions apply. | P1 | BASELINED | OR-003 (resolved) | Azure services, delivery | VT-COST-001 |
| REQ-AZ-REG-001 | Azure resources must target East US unless an approved change is recorded. | P2 | BASELINED | ARM configuration | Azure resources | VT-REG-001 |
| REQ-AZ-GIT-001 | `develop` is development/integration and `main` is production. | P1 | BASELINED | Repository state normalization | GitHub repositories | VT-GIT-001 |
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
| QF-004 | Exact HTTPS/CDN service/SKU and cost suitability require implementation validation against resolved OR-004 capability conditions. | REQ-AZ-005, REQ-AZ-015 | IMPLEMENTATION GATE |
| QF-005 | Public content definition is resolved; final owner approval of the complete HTML artifact remains a production acceptance gate. | REQ-AZ-001, REQ-AZ-015 | ACCEPTANCE GATE |
| QF-006 | Historical repository names are normalized to canonical `sixteen-resume-frontend` and `sixteen-resume-backend`. | REQ-AZ-013, REQ-AZ-014 | RESOLVED |
| QF-007 | Blog-platform direction is normalized to Dev.to + Hashnode. | REQ-AZ-016 | RESOLVED |
| QF-008 | Artifact-index filename references use `UNRESOLVED-QUESTIONS.md`. | Documentation | RESOLVED |

## 7. Requirement Rules

- No requirement with unresolved P0/P1 ambiguity may enter the executable backlog.
- `BASELINED` requirements are implementation-ready; unresolved implementation validation or acceptance gates must remain explicitly documented and must not be represented as implementation completion.
- A requirement is not `CLOSED` merely because its implementation exists; acceptance and verification evidence are required.
- Acceptance criteria remain the source of behavioral pass/fail conditions.
- `VT-*` verification IDs are the canonical verification IDs for this requirements phase.
- Changes to a requirement must be synchronized with PRD, acceptance criteria, traceability, dependency, gaps, and artifact-index documentation.


# Phase 1 — Flex Consumption PRD Re-Baseline

## Baseline authority

Phase 0 hosting-model change is merged to `main` in both canonical repositories. The current Azure Functions hosting requirement is **Azure Functions Flex Consumption (FC1), Linux, Functions runtime v4, Python 3.12**. Linux Consumption/Y1 is historical/superseded and must not be used as a current requirement or deployment baseline.

The previous Y1 deployment failed because the subscription's Y1 VM quota was 0 and the attempted increase to 1 was unsuccessful. No further Y1 quota increase is permitted.

## Flex-specific requirement classification

| ID | Classification | Requirement |
|---|---|---|
| REQ-AZ-FLEX-001 | NEW | The production Function App must use Azure Functions Flex Consumption with FC1 on Linux. |
| REQ-AZ-FLEX-002 | NEW | The production Function App must use Functions runtime v4 and Python 3.12. Runtime v4 is a platform/runtime requirement; the obsolete `FUNCTIONS_EXTENSION_VERSION` app-setting mechanism must not be required for Flex. |
| REQ-AZ-FLEX-003 | NEW | The MVP Function App must support serverless scale-to-zero and configure zero always-ready instances. |
| REQ-AZ-FLEX-004 | NEW | Flex deployment must use a configured blob-container deployment source and Flex-compatible package deployment. The deployment storage account/container must exist as required by the approved IaC design. Exact resource names and provider properties remain architecture/implementation details. |
| REQ-AZ-FLEX-005 | NEW | Flex deployment-storage access must use the Function App's system-assigned managed identity rather than a long-lived storage credential. The identity must have only the permissions required for deployment-package access. |
| REQ-AZ-FLEX-006 | NEW | Flex runtime host storage must use the provider-supported identity-based configuration; obsolete Y1 Azure Files/content-share settings must not be required by the current architecture. |
| REQ-AZ-FLEX-007 | NEW | Function App system-assigned managed identity must remain the runtime identity for Cosmos DB Table API access, with least-privilege data-plane authorization scoped to the VisitorCounter table. |
| REQ-AZ-FLEX-008 | CHANGED | Backend deployment must use a Flex-compatible package deployment mechanism. Existing generic ZIP packaging may be retained only where it satisfies the Flex deployment contract; the implementation must not rely on the superseded Y1 deployment assumptions. |
| REQ-AZ-FLEX-009 | CHANGED | ARM IaC must represent the Flex resource model through `functionAppConfig`, including deployment source and runtime/scale configuration applicable to the approved MVP. |
| REQ-AZ-FLEX-010 | NEW | Flex regional availability/quota must be validated for East US before production deployment. A Y1 quota request is neither a dependency nor an approved fallback. |
| REQ-AZ-FLEX-011 | UNCHANGED | The API contract remains `GET /api/visitors`; the hosting-model change does not alter request/response semantics, visitor semantics, persistence semantics, or browser/database isolation. |
| REQ-AZ-FLEX-012 | NEW | Flex-specific deployment failures must fail the CI/CD deployment gate and must not be represented as successful production releases. |
| REQ-AZ-FLEX-013 | NEW | The Flex implementation must preserve the approved R100/month recurring Azure/cloud ceiling; Flex pricing/availability is an implementation validation dependency, not an invented price requirement. |

## Flex abstraction boundary

The following are **not fixed product requirements** unless later promoted by an approved change:

- exact deployment storage account/container names;
- exact `functionAppConfig` API version;
- exact instance memory size;
- exact maximum instance count;
- exact HTTP per-instance concurrency;
- exact site-update strategy;
- exact deployment package build tooling;
- separate Application Insights resource;
- exact Storage RBAC role name where the selected IaC design can prove least-privilege access by capability.

These remain architecture/implementation decisions constrained by the requirements above.

## Historical/superseded Y1 material

Y1/Linux Consumption may remain only in explicit historical decision evidence explaining the failed deployment and supersession. It must not appear as the current hosting architecture, current requirement, current CI/CD target, or current acceptance criterion.

## API preservation

The visitor API is explicitly **UNCHANGED**. No Flex-driven API redesign has been identified.

## Official platform evidence

Current Microsoft documentation describes Flex-specific ARM configuration through `functionAppConfig`, including deployment source, runtime, scale/concurrency, and always-ready settings; it also documents managed-identity deployment storage and package deployment behavior. Flex runs on runtime v4, and Python 3.12 is supported. citeturn0search0turn0search2turn1search1
