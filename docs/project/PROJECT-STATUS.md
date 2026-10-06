// PROJECT-STATUS.md

# Azure Cloud Resume Challenge — Project Status

## Overall Status

**Phase 0 re-baseline complete after approved hosting-model change; live Azure deployment verification BLOCKED pending Flex ARM update and authenticated Azure/production evidence**

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
| Backend repository | Exists — Phase 7.2 persistence implementation and Phase 7.3 core ARM IaC implemented; production deployment evidence pending |
| HTML resume | Candidate exists |
| CSS | Implemented in `site/style.css` |
| JavaScript visitor counter | Implemented in `site/script.js`; live API verification pending |
| Azure Storage | ARM-defined; Azure deployment pending |
| Azure HTTPS/CDN delivery layer | Architecture resolved; exact service pending implementation validation |
| DNS hostname | Provider selected; hostname not provisioned |
| Cosmos DB | ARM-defined as serverless Table API; Azure deployment/RBAC verification pending |
| Azure Function | Current target: Flex Consumption (FC1), Linux, Functions v4, Python 3.12; ARM implementation update required before deployment |
| Python implementation | Phase 7.2 persistence implementation complete; production runtime verification pending |
| Python tests | Implemented; local/CI execution evidence pending |
| ARM template | Phase 7.3 historical core infrastructure implemented in backend repository; current Flex ARM update required before Azure validation/deployment |
| Backend GitHub Actions | Implemented with ARM structural validation; production OIDC/deployment evidence pending |
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

Implementation status: **Not started**

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

The repositories contain `develop` branches. Backend persistence and frontend CI/CD implementation exist on `main`. The existing backend ARM template is historical/superseded because it encodes Linux Consumption/Y1. Live production infrastructure, OIDC execution, HTTPS/edge routing, DNS, persistence, runtime logging, and end-to-end evidence remain blocked pending the Flex ARM update and authenticated Azure access.


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
