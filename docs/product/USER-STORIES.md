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
