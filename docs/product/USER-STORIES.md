# User Stories and Use Cases

## 1. Purpose

This document maps user stories and use cases to the product requirements defined in `docs/product/PRD.md`.

---

# 2. Personas

## USR-001 — Recruiter

Needs to quickly understand the project owner's professional background, experience, skills, certifications, and projects.

## USR-002 — Hiring Manager

Needs to evaluate technical qualifications and practical engineering evidence.

## USR-003 — Technical Interviewer

Needs to inspect evidence of software engineering, cloud engineering, serverless development, Infrastructure as Code, testing, and CI/CD practices.

## USR-004 — Public Visitor

Needs to access the public resume and interact with the visitor counter.

## USR-005 — Project Owner

Needs to control resume content, scope, costs, repositories, infrastructure, and production releases.

---

# 3. User Stories

| Story ID | User Story | Requirement IDs |
|---|---|---|
| US-001 | As a recruiter, I want to open a public resume so I can review professional qualifications. | CR-AZ-MVP-001, CR-AZ-MVP-002, CR-AZ-MVP-004, CR-AZ-MVP-005, CR-AZ-MVP-006 |
| US-002 | As a visitor, I want intentional styling so the resume is readable as a professional website. | CR-AZ-MVP-003 |
| US-003 | As a technical interviewer, I want the resume implemented with HTML, CSS, and JavaScript so I can see direct web-development fundamentals. | CR-AZ-MVP-002, CR-AZ-MVP-003, CR-AZ-MVP-007 |
| US-004 | As a visitor, I want HTTPS delivery so the public site uses secure transport. | CR-AZ-MVP-005 |
| US-005 | As a visitor, I want a stable public hostname so I can access and share the resume. | CR-AZ-MVP-006 |
| US-006 | As a visitor, I want a visitor counter so the website demonstrates dynamic behavior. | CR-AZ-MVP-007 |
| US-007 | As the project owner, I want counter state persisted so page reloads and normal redeployments do not reset the count. | CR-AZ-MVP-008 |
| US-008 | As the website client, I want an API between the browser and database so database access is not exposed directly. | CR-AZ-MVP-009 |
| US-009 | As a technical interviewer, I want Python and Azure Functions so the project demonstrates serverless Python development. | CR-AZ-MVP-010 |
| US-010 | As the project owner, I want automated backend tests so changes can be validated before deployment. | CR-AZ-MVP-011 |
| US-011 | As a technical interviewer, I want ARM infrastructure as code so Azure resources are reproducible and source controlled. | CR-AZ-MVP-012 |
| US-012 | As the project owner, I want backend changes tested and deployed through GitHub Actions so production deployment is automated. | CR-AZ-MVP-013 |
| US-013 | As the project owner, I want frontend changes automatically published so website releases are repeatable. | CR-AZ-MVP-014 |
| US-014 | As a recruiter, I want a public production URL so I can access the resume without local setup. | CR-AZ-MVP-015 |
| US-015 | As a technical interviewer, I want a linked project-learning article so I can understand lessons learned from the project. | CR-AZ-MVP-016 |

---

# 4. Use Cases

## UC-001 — View Resume

### Actor

Public Visitor

### Preconditions

- Public deployment exists.
- Public hostname resolves.
- HTTPS delivery is available.

### Trigger

Visitor opens the public resume URL.

### Main Flow

1. Visitor requests the public hostname.
2. DNS resolves the hostname.
3. HTTPS connection is established.
4. Website assets are delivered.
5. HTML resume renders.
6. CSS styles the content.
7. JavaScript initializes visitor-counter behavior.

### Success

The approved resume is publicly readable.

### Failure Conditions

- DNS resolution fails.
- HTTPS delivery fails.
- Website assets are unavailable.
- HTML cannot render.
- Unapproved content is displayed.

### Related Requirements

- CR-AZ-MVP-001
- CR-AZ-MVP-002
- CR-AZ-MVP-003
- CR-AZ-MVP-004
- CR-AZ-MVP-005
- CR-AZ-MVP-006
- CR-AZ-MVP-007

---

## UC-002 — Count Visitor

### Actor

Public Visitor

### Supporting Actors

- JavaScript client
- Azure Function
- Cosmos DB Table API

### Preconditions

- Frontend exists.
- API exists.
- Azure Function exists.
- Database exists.
- Required backend permissions exist.

### Trigger

Resume page loads.

### Main Flow

1. JavaScript initializes.
2. JavaScript sends a request to the approved visitor-counter API.
3. Azure Function receives the request.
4. Function validates the request.
5. Function reads/upserts the counter through Cosmos DB Table API.
6. Function returns the approved counter response.
7. JavaScript displays the counter.

### Success

The approved visitor-count result is displayed and persisted.

### Failure Conditions

- API unavailable.
- Function unavailable.
- Database unavailable.
- Invalid API response.
- Persistence failure.

### Important Open Requirement

The exact definition of a "visitor" is unresolved.

See `OR-001`.

### Related Requirements

- CR-AZ-MVP-007
- CR-AZ-MVP-008
- CR-AZ-MVP-009
- CR-AZ-MVP-010

---

## UC-003 — Backend CI/CD

### Actor

Project Owner / GitHub Actions

### Preconditions

- Backend repository exists.
- CI/CD workflow exists.
- Required secure deployment credentials/configuration exist.

### Trigger

An approved backend or infrastructure change enters the production workflow.

### Main Flow

1. Workflow starts.
2. Backend dependencies are prepared.
3. Automated tests execute.
4. Test results are evaluated.
5. If tests fail, deployment stops.
6. If tests pass, deployment proceeds.
7. Azure deployment executes.
8. Workflow reports success/failure.

### Success

Validated backend changes are deployed automatically.

### Failure

- Tests fail.
- Workflow fails.
- Deployment fails.
- Secure authentication fails.

### Related Requirements

- CR-AZ-MVP-011
- CR-AZ-MVP-012
- CR-AZ-MVP-013

---

## UC-004 — Frontend CI/CD

### Actor

Project Owner / GitHub Actions

### Preconditions

- Frontend repository exists.
- Frontend deployment workflow exists.
- Secure deployment configuration exists.

### Trigger

Approved frontend production change enters the workflow.

### Main Flow

1. Workflow starts.
2. Frontend files are validated.
3. Website artifacts are published.
4. Required cache invalidation occurs.
5. Workflow reports the result.

### Success

The production website reflects the approved frontend change.

### Failure

- Workflow failure.
- Upload failure.
- Authentication failure.
- CDN/cache continues serving stale content.

### Related Requirements

- CR-AZ-MVP-014
- CR-AZ-MVP-015

---

## UC-005 — Review Project Learning

### Actor

Recruiter, Hiring Manager, or Technical Interviewer

### Preconditions

- Blog post is published.
- Resume contains the correct link.

### Trigger

Visitor selects the project-learning link.

### Main Flow

1. Visitor reads the resume.
2. Visitor selects the project-learning link.
3. Public article opens.
4. Visitor reads the project-learning content.

### Success

The article is publicly reachable.

### Failure

- Link is broken.
- Article is private.
- Article has been deleted.
- URL has changed.

### Related Requirements

CR-AZ-MVP-016.

---

# 5. Story Traceability

Every MVP requirement must have at least one user story or use case.

| Requirement | Story / Use Case |
|---|---|
| CR-AZ-MVP-001 | US-001, UC-001 |
| CR-AZ-MVP-002 | US-001, US-003, UC-001 |
| CR-AZ-MVP-003 | US-002, US-003, UC-001 |
| CR-AZ-MVP-004 | US-001, UC-001 |
| CR-AZ-MVP-005 | US-001, US-004, UC-001 |
| CR-AZ-MVP-006 | US-001, US-005, UC-001 |
| CR-AZ-MVP-007 | US-003, US-006, UC-002 |
| CR-AZ-MVP-008 | US-007, UC-002 |
| CR-AZ-MVP-009 | US-008, UC-002 |
| CR-AZ-MVP-010 | US-009, UC-002 |
| CR-AZ-MVP-011 | US-010, UC-003 |
| CR-AZ-MVP-012 | US-011, UC-003 |
| CR-AZ-MVP-013 | US-012, UC-003 |
| CR-AZ-MVP-014 | US-013, UC-004 |
| CR-AZ-MVP-015 | US-014, UC-001, UC-004 |
| CR-AZ-MVP-016 | US-015, UC-005 |