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

## Flex traceability
| Requirement | User story/use case | Acceptance | Verification | Component | Dependency |
| REQ-AZ-FLEX-001 | US-009 / UC-002 | AC-FLEX-001 | VT-FLEX-001 | Function plan | East US Flex availability |
| REQ-AZ-FLEX-002 | US-009 / UC-002 | AC-FLEX-002 | VT-FLEX-002 | Function runtime | Python 3.12 / Functions v4 |
| REQ-AZ-FLEX-003 | US-009 / UC-002 | AC-FLEX-003 | VT-FLEX-003 | Scale config | Flex scale model |
| REQ-AZ-FLEX-004 | US-012 / UC-003 | AC-FLEX-004 | VT-FLEX-004 | Deployment storage/package | Storage |
| REQ-AZ-FLEX-005 | US-012 / UC-003 | AC-FLEX-005 | VT-FLEX-005 | Managed identity/Storage | Storage authorization |
| REQ-AZ-FLEX-006 | US-012 / UC-003 | AC-FLEX-006 | VT-FLEX-006 | Runtime storage | Flex storage model |
| REQ-AZ-FLEX-007 | US-008/US-009 / UC-002 | AC-FLEX-007 | VT-FLEX-007 | Function identity/Cosmos | Cosmos authorization |
| REQ-AZ-FLEX-008 | US-012 / UC-003 | AC-FLEX-008 | VT-FLEX-008 | Backend CI/CD | OIDC/package deployment |
| REQ-AZ-FLEX-009 | US-011 / UC-003 | AC-FLEX-009 | VT-FLEX-009 | ARM | Flex resource model |
| REQ-AZ-FLEX-010 | US-012 / UC-003 | AC-FLEX-010 | VT-FLEX-010 | Azure subscription | Flex capacity |
| REQ-AZ-FLEX-011 | US-008/US-009 / UC-002 | AC-FLEX-011 | VT-FLEX-011 | API/frontend/backend | Existing API contract |
| REQ-AZ-FLEX-012 | US-012 / UC-003 | AC-FLEX-012 | VT-FLEX-012 | GitHub Actions | ARM/package deployment |
| REQ-AZ-FLEX-013 | US-012/US-014 | AC-FLEX-013 | VT-FLEX-013 | Azure resources | Cost policy |
Verification catalogue: VT-FLEX-001 plan/OS; 002 runtime; 003 scale/always-ready; 004 deployment storage/package; 005 Storage identity; 006 runtime storage; 007 Cosmos identity; 008 CI/CD; 009 ARM; 010 regional capacity; 011 API regression; 012 failure gates; 013 cost.
