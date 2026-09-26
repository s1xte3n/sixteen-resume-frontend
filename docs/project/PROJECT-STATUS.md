// PROJECT-STATUS.md

# Azure Cloud Resume Challenge — Project Status

## Overall Status

**Phase 8 quality review in progress — Phase 7.3 Azure core IaC implemented; production infrastructure evidence pending**

The project requirements, scope, technology stack, constraints, repositories, resume source material, certification situation, and deployment target have been established.

## Discovery Status

| Area | Status | Notes |
|---|---|---|
| Project purpose | Complete | Personal resume/portfolio |
| Target users | Complete | Recruiters, hiring managers, technical reviewers |
| MVP | Complete | All challenge requirements |
| Scope boundaries | Complete | Strict challenge scope |
| Existing assets | Complete | Current CV supplied |
| Technology stack | Complete | Azure challenge stack confirmed |
| Azure subscription | Complete | Existing subscription |
| Azure region | Complete | East US |
| Deployment count | Complete | One deployment |
| Cost constraint | Complete | R100/month recurring Azure/cloud ceiling; R0/month preferred; paid domain excluded |
| Security baseline | Complete | Secrets, HTTPS, least privilege, API separation |
| Git workflow | Complete | feature → PR → CI → develop → production release → main |
| Repository plan | Complete | Two repositories |
| DNS approach | Complete | FreeDNS selected initially |
| Certification | Complete | AI-901 held; AZ-900 deviation documented |
| Resume content | Complete | Public HTML candidate exists; final owner approval remains a production acceptance gate |
| Resume positioning | Complete | 4+ years hands-on development; Gijima role separately identified |
| Blog platforms | Complete | Dev.to + Hashnode |
| Deadline | Complete | 30 September 2026 |

## Current Technical State

| Component | Status |
|---|---|
| Frontend repository | Exists |
| Backend repository | Exists — Phase 7.2 persistence and Phase 7.3 core ARM IaC implemented; production evidence pending |
| HTML resume | Candidate exists |
| CSS | Not started |
| JavaScript visitor counter | Not started |
| Azure Storage | ARM-defined; Azure deployment pending |
| Azure HTTPS/CDN delivery layer | Architecture resolved; exact service pending implementation validation |
| DNS hostname | Provider selected; hostname not provisioned |
| Cosmos DB | ARM-defined as serverless Table API; deployment/RBAC verification pending |
| Azure Function | ARM-defined for Python Linux Consumption; deployment/runtime verification pending |
| Python implementation | Phase 7.2 persistence implementation complete; production verification pending |
| Python tests | Implemented; execution evidence pending |
| ARM template | Phase 7.3 core infrastructure implemented; Azure validation/deployment pending |
| Backend GitHub Actions | Implemented with ARM structural validation; OIDC/deployment evidence pending |
| Frontend GitHub Actions | OIDC/deployment workflow artifacts exist; production execution pending |
| Production deployment | Not started |
| Phase 8 quality review | Source review complete; live evidence pending |
| Phase 8 quality gate | Not passed |

## Resume Status

### Public Content Definition

Status: **Resolved — owner approval pending**

The candidate HTML is governed by the approved public resume content documentation.

### Acceptance Gate

**REQ-AZ-001: Pending owner approval**

Final acceptance cannot pass until the complete public HTML resume content is explicitly approved.

## Certification Status

**Microsoft Certified: Azure AI Fundamentals (AI-901)**

Status: **Completed — July 2026**

The challenge specifies AZ-900; the project records AI-901 as a documented deviation and does not claim AZ-900 compliance.

## DNS Status

**Provider:** FreeDNS / afraid.org

Status: **Provider selected; hostname not yet created**

## Blog Status

Platforms selected:

* Dev.to
* Hashnode

Status: **Not started**

## Cost Status

Approved recurring Azure/cloud ceiling:

**R100/month**

Preferred target:

**R0/month**

The previous USD $40/month wording is obsolete for the current MVP baseline.

## Security Status

Security requirements established:

* No committed credentials.
* No secrets in source control.
* Secure GitHub Actions credentials.
* Least privilege.
* HTTPS.
* Browser cannot directly access Cosmos DB.
* Azure Function provides the database API boundary.

Phase 8 source review found no unresolved P0 security defect. Live OIDC, RBAC, CORS, HTTPS, secret-scanning and production telemetry evidence remain pending.

## Reliability / Data Integrity Status

The backend source review confirms:

* ETag-based conditional counter updates.
* Retry handling for concurrent modifications.
* Concurrent initial-entity creation handling.
* Controlled timeout/dependency failures.
* Validation of persisted counter state.

Live Cosmos persistence, concurrency, recovery and production smoke evidence remain pending.

## Deadline

**30 September 2026**

Status: **Active project target**

## Phase Status

Requirements-definition work is complete.

Architecture and test design are ready for implementation.

**Current phase: Phase 8 — Security, Reliability & Quality.**

Phase 7.3 core Azure IaC is implemented in the backend repository. Phase 8 review artifacts are present in `docs/quality/`.

The Phase 8 quality gate is **NOT PASSED** because production evidence remains pending.

## Phase 7.3 / Production Validation Gates

1. Azure Storage static website deployment.
2. Azure HTTPS/CDN service selection and validation.
3. FreeDNS hostname provisioning.
4. Cosmos DB Table API deployment.
5. Python Azure Function deployment.
6. Managed identity and table-scoped RBAC verification.
7. Backend OIDC deployment identity verification.
8. Backend CI execution evidence.
9. Frontend CI/CD execution evidence.
10. Visitor-counter browser integration.
11. API, persistence, concurrency, browser and security tests.
12. Production smoke tests.
13. Complete recurring cost evidence <= R100/month.
14. Final public resume owner approval.
15. Blog article publication and link verification.

## Linux Consumption Lifecycle

The approved MVP architecture uses Azure Functions Linux Consumption (`Y1` / Dynamic).

Microsoft has announced retirement of Linux Consumption hosting on **30 September 2028**. The project therefore treats Linux Consumption as the currently approved MVP implementation while retaining migration to Flex Consumption as a future lifecycle requirement.

This lifecycle constraint does not change the current Phase 7.3 implementation baseline.

## OR-006–OR-009 Resolution Status

| ID | Resolution |
|---|---|
| OR-006 | Visitor API is `GET /api/visitors`; successful response contains the current visitor count; browser has no Cosmos DB credentials or direct database access. |
| OR-007 | One logical counter record; backend performs a concurrency-safe atomic logical increment and returns the resulting persisted count. |
| OR-008 | GitHub Actions is the deployment authority; backend and frontend pipelines must pass their defined validation/deployment gates before deployment. |
| OR-009 | `main` represents production; feature branches flow through PR and CI into `develop`, followed by the production release into `main`. |

The repositories contain `develop` branches created from `main`. Phase 7.1/7.2 backend implementation and Phase 7.3 core ARM infrastructure are implemented; production infrastructure validation, edge-service selection, OIDC deployment evidence, and release acceptance remain pending.

## Phase 8 Quality Artifacts

| Artifact | Status |
|---|---|
| `docs/quality/SECURITY-REVIEW.md` | Complete — live evidence pending |
| `docs/quality/RELIABILITY-REVIEW.md` | Complete — live evidence pending |
| `docs/quality/DATA-INTEGRITY-REVIEW.md` | Complete — live evidence pending |
| `docs/quality/OBSERVABILITY-REVIEW.md` | Complete — live telemetry evidence pending |
| `docs/quality/QUALITY-GATE.md` | Complete — gate not passed |

## Quality Gate Decision

**NOT PASSED**

No unresolved P0 security/reliability defect was identified from source-controlled evidence.

The project must not be declared production-ready until the documented Azure deployment, identity/RBAC, HTTPS, DNS, persistence, concurrency, smoke-test, observability and cost evidence gates are satisfied.
