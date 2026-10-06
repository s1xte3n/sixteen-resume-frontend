// PROJECT-STATUS.md

# Azure Cloud Resume Challenge — Project Status

## Overall Status

**Phase 0 re-baseline complete; live Azure deployment verification BLOCKED pending corrected Flex ARM validation and authenticated Azure/production evidence**

The project requirements, scope, technology stack, constraints, repositories, resume source material, certification situation, and deployment target have been established.

## Discovery Status

| Area               | Status   | Notes                                            |
| ------------------ | -------- | ------------------------------------------------ |
| Project purpose    | Complete | Personal resume/portfolio                        |
| Target users       | Complete | Recruiters, hiring managers, technical reviewers |
| MVP                | Complete | All challenge requirements                       |
| Scope boundaries   | Complete | Strict challenge scope                           |
| Existing assets    | Complete | Current CV supplied                              |
| Technology stack   | Complete | Azure challenge stack confirmed                  |
| Azure subscription | Complete | Existing subscription                            |
| Azure region       | Complete | East US                                          |
| Deployment count   | Complete | One deployment                                   |
| Cost constraint    | Complete | R100/month recurring Azure/cloud ceiling; R0/month preferred; paid domain excluded |
| Security baseline  | Complete | Secrets, HTTPS, least privilege, API separation  |
| Git workflow       | Complete | feature → PR → CI → develop → production release → main |
| Repository plan    | Complete | Two repositories                                 |
| DNS approach       | Complete | FreeDNS selected initially                       |
| Certification      | Complete | AI-901 held; AZ-900 deviation documented         |
| Resume content     | Complete | Public HTML candidate exists; content-definition decision resolved; final owner approval remains a production acceptance gate |
| Resume positioning | Complete | 4+ years hands-on development; Gijima role separately identified |
| Blog platforms     | Complete | Dev.to + Hashnode                                |
| Deadline           | Complete | 30 September 2026                                |

## Current Technical State

| Component | Status |
|---|---|
| Frontend repository | Exists |
| Backend repository | Exists — Phase 7.2 persistence implementation and Phase 7.3 Flex ARM IaC implemented; current ARM validation blocker is being corrected; production deployment evidence pending |
| HTML resume | Candidate exists |
| CSS | Implemented in `site/style.css` |
| JavaScript visitor counter | Implemented in `site/script.js`; live API verification pending |
| Azure Storage | ARM-defined; Azure deployment pending |
| Azure HTTPS/CDN delivery layer | Architecture resolved; exact service pending implementation validation |
| DNS hostname | Provider selected; hostname not provisioned |
| Cosmos DB | ARM-defined as serverless Table API; Azure deployment/RBAC verification pending |
| Azure Function | Flex Consumption FC1, Linux, Functions v4, Python 3.12; ARM and deployment workflow implemented on Phase 2 backend branch; authenticated Azure verification pending |
| Python implementation | Phase 7.2 persistence implementation complete; production runtime verification pending |
| Python tests | Implemented; local/CI execution evidence pending |
| ARM template | Flex Consumption implementation completed; role-assignment naming correction prepared; authenticated Azure validation/deployment pending |
| Backend GitHub Actions | Flex-aware validation, ARM deployment, package build/deployment and post-deployment verification implemented; production OIDC federation progressed past the previous blocker; ARM template validation currently blocks deployment |
| Frontend GitHub Actions | Implemented: PR CI `validate` and production deployment workflow; execution evidence pending |
| Blog — Dev.to | Not started |
| Blog — Hashnode | Not started |
| Production deployment | **BLOCKED — live Azure execution/verification evidence unavailable in current environment** |

## Repository Plan

### Frontend

**Repository:** `s1xte3n/sixteen-resume-frontend`

Status: **Created**

### Backend

**Repository:** `s1xte3n/sixteen-resume-backend`

Status: **Created — implementation not started**

## Resume Status

### Source Material

Status: **Available**

A complete CV has been supplied.

### Public Content Definition

Status: **Resolved — owner approval pending**

The public resume content policy and editorial positioning are defined by OR-005. The candidate HTML is stored at `docs/product/public-resume-content.html` and is governed by `docs/product/PUBLIC-RESUME-CONTENT-APPROVAL.md`.

The candidate must:


* Present the user as a Software Engineer / Backend Developer / Cloud Engineer.
* State **4+ years of hands-on software development experience**.
* Avoid implying that all four-plus years were professional software-engineering employment.
* Clearly identify **IT Operator — Gijima Holdings | June 2022–Present** as professional employment.
* Highlight relevant Azure, AWS, backend, serverless, CI/CD, and IaC experience.
* Include the Cloud Resume Challenge project.
* Display **Microsoft Certified: Azure AI Fundamentals (AI-901)**.
* Include only explicitly approved public links and contact information.
* Exclude private information not intended for public publication.

### Acceptance Gate

**REQ-AZ-001: Pending owner approval**

The candidate HTML content has been prepared, but final acceptance cannot pass until the owner explicitly approves the complete public HTML resume content.

## Certification Status

**Current certification:**

Microsoft Certified: Azure AI Fundamentals (AI-901)

Status: **Completed — July 2026**

### Challenge Deviation

The challenge specifies AZ-900.

The project currently uses AI-901 instead.

Status: **Documented deviation**

## DNS Status

**Provider:** FreeDNS / afraid.org

Status: **Provider selected; hostname not yet created**

The initial implementation will use a free hosted hostname/subdomain approach. A conventional paid domain can be introduced later if the website is moved toward a production personal-brand deployment.

## Blog Status

Platforms selected:

* Dev.to
* Hashnode

Status: **Not started**

The blog will cover both technical lessons and the overall project journey.

## Cost Status

Target:

**R0 where possible**

Fallback:

**Lowest possible cost**

The project should prioritize free allowances and serverless/pay-per-use services.

## Security Status

Security requirements established:

* No committed credentials.
* No secrets in source control.
* Secure GitHub Actions credentials.
* Least privilege.
* HTTPS.
* Browser cannot directly access Cosmos DB.
* Azure Function provides the database API boundary.

Implementation status: **Flex infrastructure/security implementation in progress; live Azure verification pending**

## Deadline

**30 September 2026**

Status: **Active project target**

## Next Project Phase

Requirements-definition work is complete.

Architecture and test design are ready for implementation.

**Current phase: Phase 7 — Implementation. Frontend CI/CD and backend core ARM/deployment workflows are implemented; live Azure deployment verification is BLOCKED pending authenticated production evidence.**

Phase 7 continues with incremental implementation and validation of:

1. Azure Storage static website.
2. Azure HTTPS/CDN delivery.
3. FreeDNS hostname.
4. Cosmos DB Table API.
5. Python Azure Function.
6. Counter persistence and concurrency.
7. ARM infrastructure.
8. Backend CI/CD.
9. Frontend CI/CD.
10. Frontend visitor counter.
11. Automated tests.
12. End-to-end validation.

The final public resume approval and production cost evidence remain production acceptance gates.

The approved recurring Azure/cloud cost ceiling is **R100/month**, with **R0/month preferred**.


## OR-006–OR-009 Resolution Status

The following implementation-governing decisions are now resolved:

| ID | Resolution |
|---|---|
| OR-006 | Visitor API is `GET /api/visitors`; successful response contains the current visitor count; browser has no Cosmos DB credentials or direct database access. |
| OR-007 | One logical counter record; backend performs a concurrency-safe atomic logical increment and returns the resulting persisted count. |
| OR-008 | GitHub Actions is the deployment authority; backend and frontend pipelines must pass their defined validation/deployment gates before deployment. |
| OR-009 | `main` represents production; feature branches flow through PR and CI into `develop`, followed by the production release into `main`. |

The repositories contain `develop` branches. Backend persistence and frontend CI/CD implementation exist on `main`. The existing Y1 ARM path is superseded and is no longer the current deployment path. The Phase 2 backend branch contains the Flex ARM implementation, identity/RBAC configuration, package deployment workflow, and Flex validation tests. Live production infrastructure, OIDC execution, runtime logging, HTTPS/edge routing, DNS, persistence and end-to-end evidence remain blocked pending authenticated Azure access and release validation.


# Phase 2 — Flex Consumption Infrastructure Implementation

Status: IMPLEMENTATION COMPLETE ON FEATURE BRANCH — authenticated Azure deployment evidence pending.
Phase 0 PR #50 frontend is merged into main at d75e43eb64c995086e36e89799d09754a1ce1fa7.
Phase 0 PR #18 backend is merged into main at 9dd83933d4341315810aed96117177da8c47cba5.
Current hosting authority: Azure Functions Flex Consumption FC1, Linux, Functions runtime v4, Python 3.12, serverless scale-to-zero, zero always-ready instances, system-assigned managed identity, Cosmos DB Table API serverless, ARM IaC, GitHub Actions and Microsoft Entra OIDC.
Historical Y1 failure: subscription Y1 VM quota was 0; attempted increase to 1 failed; no further Y1 quota increase is authorized.
API contract: UNCHANGED — GET /api/visitors.
Phase 1 added explicit requirements for Flex plan, runtime, scale-to-zero, zero always-ready, deployment storage/package deployment, identity-based storage access, runtime storage, Cosmos authorization, ARM functionAppConfig, regional capacity and CI/CD failure gating.
Phase 2 replaced the superseded Y1 ARM assumptions, updated package/deployment configuration and tests, and added automated Flex availability/runtime validation. No API redesign was performed. Production deployment evidence remains pending.


## Phase 3 — Authenticated Azure Deployment Verification

**Current gate: BLOCKED.**

The previous production OIDC federation blocker was corrected and the backend deployment workflow progressed to Azure ARM template validation. The current blocker is an ARM template defect: role-assignment resource names used reference() to obtain the Function App managed-identity principal ID. ARM does not permit reference() at that location.

The backend correction keeps reference(...).identity.principalId in the role-assignment properties and changes only the resource-name expressions to deterministic guid(...) values based on stable resource identifiers, the Function App name, and role identifiers.

Consequences until the corrected backend branch is validated and released:

- ARM validation remains unproven.
- ARM deployment remains unproven.
- Flex subscription capacity remains unproven.
- Function App, Storage, RBAC, Cosmos, package activation, runtime startup, API, persistence/concurrency, CORS, observability, and cost remain unverified.
- Frontend production deployment remains dependent on the backend release and end-to-end acceptance.

No alternate credential mechanism, manual production repair, or API redesign is authorized.


## Phase 4 continuation — 2026-10-07

The backend ARM template validation blocker is resolved: the current approved template now passes Azure deployment-group validation against the production resource group using the dedicated deployment Storage account/container. The remaining production blocker is authenticated GitHub Actions OIDC execution: the federated credential exists with the approved issuer, audience, and production repository/environment subject, but the deployment workflow still fails to obtain an Azure subscription context.

Frontend production deployment remains BLOCKED and unchanged. No frontend credential, direct Cosmos access, API change, CDN/cache service, or alternative deployment path has been introduced. The frontend may proceed only after the backend production gate has a fresh authenticated execution and the required end-to-end evidence is captured.
