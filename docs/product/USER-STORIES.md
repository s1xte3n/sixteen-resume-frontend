# User Stories and Use Cases

## 1. Purpose

This document defines the product personas, user stories, and use cases for the requirements in `docs/product/PRD.md`. Every MVP requirement is mapped to at least one story or use case.

## 2. Personas

| Persona | Need |
|---|---|
| USR-001 Recruiter | Quickly understand professional background, experience, skills, certifications, and projects. |
| USR-002 Hiring Manager | Evaluate qualifications and practical engineering evidence. |
| USR-003 Technical Interviewer | Inspect evidence of software engineering, Azure/cloud, serverless development, IaC, testing, and CI/CD. |
| USR-004 Public Visitor | Access the public resume, use the visitor counter, and follow project-learning links. |
| USR-005 Project Owner | Control content, scope, costs, repositories, infrastructure, and production releases. |

## 3. User Stories

| ID | User Story | Requirement IDs |
|---|---|---|
| US-001 | As a recruiter, I want to open a public resume so I can review professional qualifications. | MVP-001, MVP-002, MVP-004, MVP-005, MVP-006, MVP-015 |
| US-002 | As a visitor, I want intentional styling so the resume is readable as a professional website. | MVP-003 |
| US-003 | As a technical interviewer, I want the resume implemented with HTML, CSS, and JavaScript so I can see direct web fundamentals. | MVP-002, MVP-003, MVP-007 |
| US-004 | As a visitor, I want HTTPS delivery so the public site uses secure transport. | MVP-005 |
| US-005 | As a visitor, I want a stable public hostname so I can access and share the resume. | MVP-006 |
| US-006 | As a visitor, I want a visitor counter so the site demonstrates dynamic behavior. | MVP-007 |
| US-007 | As the Project Owner, I want counter state persisted so normal page reloads and redeployments do not reset it. | MVP-008 |
| US-008 | As the website client, I want an API between the browser and database so database access is not exposed directly. | MVP-009 |
| US-009 | As a technical interviewer, I want Python on Azure Functions so the project demonstrates serverless Python development. | MVP-010 |
| US-010 | As the Project Owner, I want automated backend tests so changes can be validated before deployment. | MVP-011 |
| US-011 | As a technical interviewer, I want ARM Infrastructure as Code so Azure resources are reproducible and source controlled. | MVP-012 |
| US-012 | As the Project Owner, I want backend changes tested and deployed through GitHub Actions so production releases are automated. | MVP-013 |
| US-013 | As the Project Owner, I want frontend changes automatically published so website releases are repeatable. | MVP-014 |
| US-014 | As a recruiter, hiring manager, or technical interviewer, I want a public production URL so I can access the resume without local setup. | MVP-015 |
| US-015 | As a technical interviewer, I want a linked project-learning article so I can understand lessons learned and project decisions. | MVP-016 |

## 4. Use Cases

### UC-001 — View Resume

**Primary actor:** Public Visitor  
**Supporting actors:** DNS/hostname provider, Azure delivery layer, Azure Storage.

**Preconditions**
- Approved public resume content exists.
- Production deployment exists.
- Public hostname and HTTPS delivery are operational.

**Trigger**

Visitor opens the public resume URL.

**Main flow**
1. Visitor requests the public hostname.
2. DNS resolves the hostname.
3. HTTPS connection is established.
4. Delivery layer retrieves/serves the static website content.
5. HTML renders.
6. CSS styles the resume.
7. JavaScript initializes the counter behavior.

**Success**

The approved resume is publicly readable.

**Failure conditions**

DNS failure, HTTPS failure, missing assets, rendering failure, or unapproved content exposure.

**Related requirements:** MVP-001 through MVP-007, MVP-015.

### UC-002 — Count Visitor

**Primary actor:** Public Visitor  
**Supporting actors:** Browser JavaScript, Azure Function, Cosmos DB Table API.

**Preconditions**
- Frontend exists.
- Approved API exists.
- Function and database exist.
- Required backend permissions exist.

**Trigger**

The resume page initializes visitor-counter behavior.

**Main flow**
1. JavaScript starts the counter operation.
2. JavaScript calls the approved counter API.
3. Azure Function validates the request.
4. Function reads/updates counter state through Cosmos DB Table API.
5. Function returns the approved counter response.
6. JavaScript displays the returned value or approved failure state.

**Success**

The counter result is displayed and persistent state is updated according to the approved counting semantics.

**Failure conditions**

API unavailable, function failure, database failure, invalid response, or persistence failure.

**Open dependencies:** OR-001, OR-008, OR-009.

**Related requirements:** MVP-007, MVP-008, MVP-009, MVP-010.

### UC-003 — Backend CI/CD

**Primary actor:** Project Owner / GitHub Actions.

**Preconditions**
- Canonical backend repository exists.
- CI/CD workflow exists.
- Secure deployment authentication is configured.

**Trigger**

An approved backend or infrastructure change enters the workflow.

**Main flow**
1. Workflow starts.
2. Test environment is prepared.
3. Required Python tests execute.
4. Test result is evaluated.
5. If required tests fail, deployment stops.
6. If tests pass, deployment proceeds.
7. Azure deployment executes.
8. Workflow reports the outcome.

**Success**

Validated `main` changes are deployed automatically.

**Failure conditions**

Test failure, workflow failure, authentication failure, or Azure deployment failure.

**Related requirements:** MVP-011, MVP-012, MVP-013.

### UC-004 — Frontend CI/CD

**Primary actor:** Project Owner / GitHub Actions.

**Preconditions**
- Canonical frontend repository exists.
- Frontend workflow exists.
- Secure deployment configuration exists.

**Trigger**

An approved frontend production change enters the workflow.

**Main flow**
1. Workflow starts.
2. Frontend files are validated.
3. Website artifacts are published to Azure Storage.
4. Required delivery-layer cache invalidation occurs where applicable.
5. Workflow reports the outcome.

**Success**

The production website reflects the approved `main` state.

**Failure conditions**

Validation, upload, authentication, cache invalidation, or workflow failure.

**Related requirements:** MVP-014, MVP-015.

### UC-005 — Review Project Learning

**Primary actor:** Recruiter, Hiring Manager, or Technical Interviewer.

**Preconditions**
- Required article is publicly published.
- Resume contains the approved link.

**Trigger**

Visitor selects the project-learning link.

**Main flow**
1. Visitor reads the resume.
2. Visitor selects the project-learning link.
3. Public article opens.
4. Visitor reads the project-learning content.

**Success**

The article is publicly reachable and contains the required project-learning material.

**Failure conditions**

Broken link, private/deleted article, or incomplete article.

**Related requirements:** MVP-016.

## 5. Story Traceability

| Requirement | User Story / Use Case | Verification |
|---|---|---|
| MVP-001 | US-001, UC-001 | VT-001 |
| MVP-002 | US-001, US-003, UC-001 | VT-002 |
| MVP-003 | US-002, US-003, UC-001 | VT-003 |
| MVP-004 | US-001, UC-001 | VT-004 |
| MVP-005 | US-004, UC-001 | VT-005 |
| MVP-006 | US-005, UC-001 | VT-006 |
| MVP-007 | US-003, US-006, UC-002 | VT-007 |
| MVP-008 | US-007, UC-002 | VT-008 |
| MVP-009 | US-008, UC-002 | VT-009 |
| MVP-010 | US-009, UC-002, UC-003 | VT-010 |
| MVP-011 | US-010, UC-003 | VT-011 |
| MVP-012 | US-011, UC-003 | VT-012 |
| MVP-013 | US-012, UC-003 | VT-013 |
| MVP-014 | US-013, UC-004 | VT-014 |
| MVP-015 | US-014, UC-001, UC-004 | VT-015 |
| MVP-016 | US-015, UC-005 | VT-016 |

## 6. Scope Note

These stories describe the approved product behavior. They do not authorize additional functionality, resolve open requirements, or create implementation tasks.


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
