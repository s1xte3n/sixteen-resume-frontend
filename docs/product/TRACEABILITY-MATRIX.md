# Requirements Traceability Matrix

## 1. Purpose

Trace each canonical requirement from user need through contract/UI, acceptance criteria, verification, implementation area, and CI/release evidence. This document records planned evidence paths; it does not claim evidence exists before implementation.

## 2. MVP Traceability

| Requirement | User story / use case | Contract / UI | Acceptance | Verification | Implementation area | CI / release evidence |
|---|---|---|---|---|---|---|
| REQ-AZ-001 | US-001 / UC-001 | Resume page/content | AC-001 | VT-001 | Approved resume content + HTML | Production URL + owner content approval |
| REQ-AZ-002 | US-001, US-003 / UC-001 | HTML document | AC-002 | VT-002 | `index.html` / markup | Frontend validation + production fetch |
| REQ-AZ-003 | US-002, US-003 / UC-001 | CSS/UI | AC-003 | VT-003 | CSS assets | Frontend CI + browser validation |
| REQ-AZ-004 | US-001 / UC-001 | Static site delivery | AC-004 | VT-004 | Azure Storage static website | Frontend deployment run + endpoint evidence |
| REQ-AZ-005 | US-004 / UC-001 | HTTPS/CDN delivery | AC-005 | VT-005 | Approved delivery configuration | Deployment configuration + HTTPS probe + cost evidence |
| REQ-AZ-006 | US-005 / UC-001 | Public hostname/DNS | AC-006 | VT-006 | DNS + delivery endpoint | DNS resolution + production URL evidence |
| REQ-AZ-007 | US-003, US-006 / UC-002 | Counter UI + one operation per top-level page load | AC-007 | VT-007 | Browser JavaScript | Browser network + UI evidence |
| REQ-AZ-008 | US-007 / UC-002 | Counter persistence + concurrency-safe increment | AC-008 | VT-008 | Cosmos DB Table API + Function service layer | Backend tests + persistence evidence |
| REQ-AZ-009 | US-008 / UC-002 | Visitor API contract | AC-009 | VT-009 | Azure Function HTTP endpoint | API test evidence |
| REQ-AZ-010 | US-009 / UC-002 | Function runtime | AC-010 | VT-010 | Python Azure Function | Backend CI + deployed Function evidence |
| REQ-AZ-011 | US-010 / UC-003 | Test suite / CI gate | AC-011 | VT-011 | Python tests + GitHub Actions | Passing test-gated workflow run |
| REQ-AZ-012 | US-011 / UC-003 | ARM resource definitions | AC-012 | VT-012 | ARM templates | IaC deployment evidence |
| REQ-AZ-013 | US-012 / UC-003 | Backend CI/CD workflow | AC-013 | VT-013 | Backend repository + workflows | Successful test-gated backend deployment |
| REQ-AZ-014 | US-013 / UC-004 | Frontend CI/CD workflow | AC-014 | VT-014 | Frontend repository + workflow | Successful frontend publication |
| REQ-AZ-015 | US-014 / UC-001, UC-004 | Production URL / end-to-end behavior | AC-015 | VT-015 | Entire system | Production release + end-to-end evidence |
| REQ-AZ-016 | US-015 / UC-005 | Blog/article link | AC-016 | VT-016 | Resume external link | Public article + production link evidence |

## 3. Cross-Cutting Traceability

| Requirement | Acceptance / verification | Evidence path |
|---|---|---|
| REQ-AZ-SEC-001 | VT-SEC-001 | Secret scan + repository review |
| REQ-AZ-SEC-002 | VT-SEC-002 | Browser network inspection |
| REQ-AZ-SEC-003 | VT-SEC-003 | GitHub/Azure permission review |
| REQ-AZ-SEC-004 | VT-SEC-004 | Production HTTPS probe |
| REQ-AZ-COST-001 | VT-COST-001 | Azure billing/configuration evidence against the approved R100/month recurring ceiling; R0/month preferred and approved exclusions applied |
| REQ-AZ-REG-001 | VT-REG-001 | ARM resource-location review |
| REQ-AZ-GIT-001 | VT-GIT-001 | Repository branch evidence |
| REQ-AZ-DEV-001 | VT-IAC-001 | ARM deployment/reproducibility evidence |
| REQ-AZ-DEV-002 | VT-CERT-001 | Public resume content review |

## 4. Verification Catalogue

| ID | Objective | Type | Requirement |
|---|---|---|---|
| VT-001 | Verify approved resume content only is public. | Content/acceptance | REQ-AZ-001 |
| VT-002 | Verify browser-renderable HTML resume. | Structural/browser | REQ-AZ-002 |
| VT-003 | Verify intentional responsive CSS presentation. | Browser/UI | REQ-AZ-003 |
| VT-004 | Verify production assets are served by Azure Storage. | Integration | REQ-AZ-004 |
| VT-005 | Verify approved HTTPS/CDN configuration and cost compliance. | Integration/configuration | REQ-AZ-005 |
| VT-006 | Verify public hostname resolves to production delivery. | DNS/integration | REQ-AZ-006 |
| VT-007 | Verify browser uses API and displays approved counter behavior. | Browser/integration | REQ-AZ-007 |
| VT-008 | Verify counter persistence and deployment survival. | Backend/integration | REQ-AZ-008 |
| VT-009 | Verify API request, response, validation, and error behavior. | API | REQ-AZ-009 |
| VT-010 | Verify Python Function behavior and restricted permissions. | Backend/security | REQ-AZ-010 |
| VT-011 | Verify tests execute and gate deployment. | CI | REQ-AZ-011 |
| VT-012 | Verify ARM reproducibility and required resource coverage. | IaC/integration | REQ-AZ-012 |
| VT-013 | Verify backend CI/CD tests before deployment. | CI/CD | REQ-AZ-013 |
| VT-014 | Verify frontend CI/CD publication. | CI/CD | REQ-AZ-014 |
| VT-015 | Verify complete production acceptance. | End-to-end | REQ-AZ-015 |
| VT-016 | Verify public article and production link. | Content/link | REQ-AZ-016 |
| VT-SEC-001 | Verify no committed credentials/secrets. | Security | REQ-AZ-SEC-001 |
| VT-SEC-002 | Verify browser has no direct Cosmos DB access. | Security/network | REQ-AZ-SEC-002 |
| VT-SEC-003 | Verify deployment identities are least privilege. | Security/configuration | REQ-AZ-SEC-003 |
| VT-SEC-004 | Verify production traffic uses HTTPS. | Security/network | REQ-AZ-SEC-004 |
| VT-COST-001 | Verify recurring Azure/cloud cost is <= R100/month, with R0/month preferred, approved exclusions applied, and unexpected charges investigated. | Governance | REQ-AZ-COST-001 |
| VT-REG-001 | Verify Azure resources target East US. | IaC/configuration | REQ-AZ-REG-001 |
| VT-GIT-001 | Verify branch model and production branch. | Repository governance | REQ-AZ-GIT-001 |
| VT-IAC-001 | Verify production infrastructure is source-defined. | IaC | REQ-AZ-DEV-001 |
| VT-CERT-001 | Verify AI-901 representation without AZ-900 claim. | Content | REQ-AZ-DEV-002 |

## 5. Traceability Status

All canonical requirements have IDs, priorities, dependencies, affected components, acceptance criteria, and verification IDs. Implementation and release evidence are intentionally pending because implementation has not been completed.

Requirements unblocked by Step 7 are now implementation-ready. This does not claim implementation, verification evidence, or production acceptance; those remain pending.


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
