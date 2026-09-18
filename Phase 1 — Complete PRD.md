// PRD.md

# Product Requirements Document

## 1. Document Control

| Field | Value |
|---|---|
| Product | Cloud Resume Challenge — Azure |
| Status | Requirements baseline drafted; high-impact decisions explicitly open |
| Primary users | Recruiters, hiring managers, technical interviewers |
| Secondary users | General public visitors |
| Target platform | Microsoft Azure |
| Target region | East US |
| Cost constraint | Zero/near-zero cost where technically feasible |
| Frontend repository | `s1xte3n/sixteen-frontend` |
| Backend repository | `s1xte3n/sixteen-backend` |
| Development branch | `develop` |
| Production branch | `main` |

## 2. Purpose

Provide a public, production-style personal resume website demonstrating practical Azure cloud engineering, backend development, Infrastructure as Code, automated testing, source control, and CI/CD capabilities.

The product is intended to provide recruiters, hiring managers, and technical interviewers with concrete evidence of the project owner's engineering capabilities.

## 3. Confirmed Requirements

The following requirements are confirmed project requirements.

1. A public personal resume website is required.
2. Primary audiences are recruiters, hiring managers, and technical interviewers.
3. The frontend uses HTML, CSS, and JavaScript.
4. Azure Storage static website hosting is required.
5. HTTPS is required.
6. CDN capability is part of the approved delivery direction.
7. A public hostname/DNS solution is required.
8. Paid domain purchase is explicitly out of scope unless separately approved.
9. A JavaScript visitor counter is required.
10. Visitor-counter persistence uses Azure Cosmos DB Table API.
11. Browser JavaScript must not communicate directly with Cosmos DB.
12. Backend compute uses Python on Azure Functions.
13. Automated Python tests are required.
14. Azure infrastructure uses ARM templates.
15. Frontend and backend use separate GitHub repositories.
16. Backend CI/CD runs tests before deployment.
17. Frontend CI/CD automatically publishes website changes.
18. Azure credentials and secrets must not be committed to source control.
19. Free or consumption-based options are preferred.
20. East US is the target Azure region.
21. `develop` is the development/integration branch.
22. `main` is the production branch.
23. A short project-learning blog post must be linked from the resume.
24. AZ-900 is explicitly excluded from this project.
25. The supplied CV is the source material for resume content, subject to final public-content approval.

## 4. Assumptions

The following are assumptions and must not be treated as confirmed implementation decisions:

1. The existing Azure subscription can provision all required resources.
2. Required services can operate within the zero/near-zero-cost constraint.
3. A technically suitable free public hostname/subdomain is available.
4. The supplied CV is sufficient for the initial resume content.
5. The project owner will approve unavoidable costs before commitment.
6. Required Azure services remain available and suitable when implementation begins.
7. The required HTTPS/CDN configuration can satisfy the cost constraint.
8. A blog platform can be selected without changing the core product.
9. Required GitHub Actions deployment authentication can be established securely.

## 5. Actors

| Actor | Responsibility |
|---|---|
| Public Visitor | Reads resume and interacts with visitor counter |
| Recruiter | Reviews experience, skills, certifications, and projects |
| Hiring Manager | Reviews qualifications and engineering evidence |
| Technical Interviewer | Reviews technical implementation evidence |
| Project Owner | Owns content, scope, costs, repositories, and releases |
| GitHub Actions | Executes automated CI/CD workflows |
| Azure Services | Host, deliver, execute, and persist product behavior |

## 6. Product Permissions

- Resume content is publicly readable.
- Visitor-counter functionality is publicly callable only to the extent required by the approved API contract.
- Database access is not public/browser-facing.
- Project-owner controls cover content, scope, costs, repositories, and production release.
- CI/CD deployment identities must have only the permissions required for their deployment responsibilities.
- Secrets must be handled through secure mechanisms and never committed to source control.

# 7. MVP Requirements

## CR-AZ-MVP-001 — Public Resume Content

### Problem / User Story

As a recruiter, hiring manager, or technical interviewer, I need a public resume so I can evaluate the project owner's professional background.

### Actors

- Public Visitor
- Recruiter
- Hiring Manager
- Technical Interviewer
- Project Owner

### Preconditions

- Approved resume content exists.
- Public deployment exists.

### Trigger

A visitor requests the public resume.

### Inputs

- Approved CV-derived content.

### Business Rules

- Public resume content must be based on the supplied CV or explicitly approved additions.
- Final public content requires owner review.
- AZ-900 is not a project requirement.

### Success State

Approved resume content is publicly readable.

### Failure States

- Site unavailable.
- Incomplete content.
- Unapproved or private content is exposed.

### Permissions

- Public read.
- Project owner controls content.

### Edge Cases

- CV changes.
- Content disclosure restrictions.
- Narrow/mobile viewport.

### Dependencies

- CR-AZ-MVP-002
- CR-AZ-MVP-003
- CR-AZ-MVP-004
- CR-AZ-MVP-005
- CR-AZ-MVP-006

### Acceptance Criteria

See `AC-001` in `docs/product/ACCEPTANCE-CRITERIA.md`.

### Non-Functional Requirements

- Publicly available.
- Readable.
- Must not expose private or unapproved information.

### Out of Scope

- Visitor editing.
- User accounts.
- CMS functionality.

---

## CR-AZ-MVP-002 — HTML Resume

### Problem / User Story

As a technical interviewer, I need the resume implemented as HTML to demonstrate web fundamentals.

### Actors

- Public Visitor
- Technical Interviewer

### Preconditions

Approved resume content exists.

### Trigger

The resume is published.

### Inputs

Resume content.

### Business Rules

- Resume must be delivered as an HTML webpage.
- The product must not consist only of Word/PDF documents.

### Success State

A modern browser renders the resume as an HTML webpage.

### Failure States

- Only document-download formats are provided.
- HTML fails to render.

### Permissions

Public read.

### Edge Cases

- Missing markup.
- Malformed HTML.
- Browser rendering differences.

### Dependencies

- CR-AZ-MVP-001
- CR-AZ-MVP-003

### Acceptance Criteria

See `AC-002`.

### Non-Functional Requirements

- Browser-renderable.
- Readable.

### Out of Scope

- PDF generation.
- Word document generation.

---

## CR-AZ-MVP-003 — CSS Styling

### Problem / User Story

As a visitor, I need intentional styling so the resume is presented as a website rather than raw HTML.

### Actors

Public Visitor.

### Preconditions

HTML resume exists.

### Trigger

Resume loads.

### Inputs

HTML and CSS.

### Business Rules

- CSS styling is required.
- Elaborate design is not required.

### Success State

The resume is intentionally styled and readable.

### Failure States

- Only raw/default browser presentation is provided.
- CSS prevents meaningful access to the resume.

### Permissions

Public read.

### Edge Cases

- CSS fails to load.
- Narrow/mobile viewport.

### Dependencies

CR-AZ-MVP-002.

### Acceptance Criteria

See `AC-003`.

### Non-Functional Requirements

- Readability.
- Responsive presentation.

### Out of Scope

- Frontend frameworks.
- Advanced animation.
- Design systems.

---

## CR-AZ-MVP-004 — Azure Storage Static Website

### Problem / User Story

As the project owner, I need Azure Storage hosting so the project demonstrates Azure static website hosting.

### Actors

- Public Visitor
- Project Owner
- Azure

### Preconditions

Frontend artifacts exist.

### Trigger

Production publication occurs.

### Inputs

- HTML
- CSS
- JavaScript

### Business Rules

Azure Storage is the primary static website hosting platform.

### Success State

The public website is served from Azure Storage.

### Failure States

- Website is hosted only by another provider.
- Required content is unavailable.

### Permissions

- Public read.
- Deployment write access is restricted.

### Edge Cases

- Partial publication.
- Missing files.
- Endpoint outage.

### Dependencies

- CR-AZ-MVP-002
- CR-AZ-MVP-003
- CR-AZ-MVP-005

### Acceptance Criteria

See `AC-004`.

### Non-Functional Requirements

- Public availability.
- Cost-conscious configuration.

### Out of Scope

Replacing Azure Storage as the primary host.

---

## CR-AZ-MVP-005 — HTTPS/CDN Delivery

### Problem / User Story

As a visitor, I need HTTPS delivery so communication with the public resume uses secure transport.

### Actors

- Public Visitor
- Azure delivery layer

### Preconditions

Azure Storage hosting exists.

### Trigger

A public request is made.

### Inputs

HTTPS request.

### Business Rules

- HTTPS is mandatory.
- CDN capability is part of the approved delivery direction.
- Exact service/configuration must be validated against current availability and cost.

### Success State

The public resume is accessible through HTTPS using the approved delivery path.

### Failure States

- HTTP-only service.
- Certificate/configuration failure.
- Delivery unavailable.
- Cost exceeds the approved constraint.

### Permissions

- Public read.
- Delivery configuration restricted.

### Edge Cases

- Stale cache.
- Certificate lifecycle issues.
- Pricing changes.

### Dependencies

- CR-AZ-MVP-004
- CR-AZ-MVP-006

### Acceptance Criteria

See `AC-005`.

### Non-Functional Requirements

- Secure transport.
- Approved cost compliance.

### Out of Scope

Unapproved paid delivery services.

---

## CR-AZ-MVP-006 — Public Hostname/DNS

### Problem / User Story

As a visitor, I need a stable public hostname so I can access and share the resume.

### Actors

- Public Visitor
- Project Owner
- DNS/hostname provider

### Preconditions

Public delivery endpoint exists.

### Trigger

A visitor resolves the hostname.

### Inputs

Public hostname.

### Business Rules

- A public hostname is required.
- Paid domain purchase is currently excluded.
- A free hostname/subdomain is the current direction.
- Exact DNS/hostname solution remains unresolved.

### Success State

The hostname resolves to the intended production website.

### Failure States

- DNS resolution failure.
- Hostname unavailable.
- Unapproved payment required.

### Permissions

- Public DNS resolution.
- Owner controls configuration.

### Edge Cases

- DNS propagation delay.
- Provider restrictions.
- Hostname change.

### Dependencies

CR-AZ-MVP-005.

### Acceptance Criteria

See `AC-006`.

### Non-Functional Requirements

- Publicly resolvable.
- Cost compliant.

### Out of Scope

Paid domain purchase unless scope changes.

---

## CR-AZ-MVP-007 — JavaScript Visitor Counter

### Problem / User Story

As a visitor, I need to see a visitor count so the website demonstrates dynamic client-side behavior.

### Actors

- Public Visitor
- JavaScript client

### Preconditions

Website and API exist.

### Trigger

Resume loads.

### Inputs

Counter API response.

### Business Rules

- JavaScript retrieves and displays the counter.
- Browser must not access Cosmos DB directly.
- Counting semantics must be explicitly defined before final acceptance.

### Success State

The count is displayed when the counter service succeeds.

### Failure States

- API unavailable.
- Invalid response.
- Count cannot be displayed.

### Permissions

Public operation only as required by the approved API contract.

### Edge Cases

- Page refreshes.
- Concurrent requests.
- Timeouts.
- Duplicate requests.

### Dependencies

- CR-AZ-MVP-008
- CR-AZ-MVP-009
- CR-AZ-MVP-010

### Acceptance Criteria

See `AC-007`.

### Non-Functional Requirements

- Graceful failure.
- No database credentials exposed.

### Out of Scope

- User accounts.
- Demographic analytics.
- Unrelated visitor tracking.

---

## CR-AZ-MVP-008 — Visitor Counter Persistence

### Problem / User Story

As the project owner, I need visitor-counter state persisted so it survives page reloads and normal deployments.

### Actors

- Azure Function
- Cosmos DB Table API

### Preconditions

Database exists and backend has required access.

### Trigger

A valid counter operation occurs.

### Inputs

Counter operation/state.

### Business Rules

- Cosmos DB Table API is the approved persistence direction.
- Counter state must survive normal backend redeployments.

### Success State

Counter state is retrieved and updated persistently according to approved semantics.

### Failure States

- Database unavailable.
- Persistence failure.
- Invalid data response.

### Permissions

Backend access only as required.

### Edge Cases

- First record.
- Missing record.
- Concurrent updates.
- Transient failure.

### Dependencies

- CR-AZ-MVP-009
- CR-AZ-MVP-010

### Acceptance Criteria

See `AC-008`.

### Non-Functional Requirements

- Persistent state.
- No browser database access.

### Out of Scope

General-purpose database functionality.

---

## CR-AZ-MVP-009 — Visitor Counter API

### Problem / User Story

As the website client, I need an API between the browser and database so database access is not exposed directly.

### Actors

- Public Visitor
- JavaScript client
- Azure Function

### Preconditions

Function is deployed.

### Trigger

Frontend requests visitor-counter information.

### Inputs

HTTP request.

### Business Rules

- Browser communicates with the API.
- Browser must not communicate directly with Cosmos DB.

### Success State

The API returns the required counter result.

### Failure States

- Invalid request.
- Backend unavailable.
- Database failure.
- Server error.

### Permissions

Public access only to the required API operation.

### Edge Cases

- Repeated requests.
- Malformed requests.
- Downstream outage.

### Dependencies

- CR-AZ-MVP-008
- CR-AZ-MVP-010

### Acceptance Criteria

See `AC-009`.

### Non-Functional Requirements

- Controlled errors.
- Secure secrets.
- No database credentials exposed.

### Out of Scope

General API platform functionality.

---

## CR-AZ-MVP-010 — Python Azure Function

### Problem / User Story

As a technical interviewer, I need the backend implemented in Python on Azure Functions so the project demonstrates serverless Python development.

### Actors

- Azure Function
- Technical Interviewer

### Preconditions

API behavior is defined.

### Trigger

An API request occurs.

### Inputs

HTTP request.

### Business Rules

- Python is the backend language.
- Azure Functions is the compute platform.
- Function must use only required data-access permissions.

### Success State

The function handles required counter behavior.

### Failure States

- Function unavailable.
- Runtime error.
- Dependency error.
- Configuration error.

### Permissions

Least privilege for required data access.

### Edge Cases

- Cold start.
- Malformed input.
- Database outage.

### Dependencies

- CR-AZ-MVP-008
- CR-AZ-MVP-009
- CR-AZ-MVP-011

### Acceptance Criteria

See `AC-010`.

### Non-Functional Requirements

- Serverless operation.
- Least privilege.
- Safe errors.

### Out of Scope

Non-Python backend implementation.

---

## CR-AZ-MVP-011 — Automated Python Tests

### Problem / User Story

As the project owner, I need automated tests so backend changes can be validated before deployment.

### Actors

- GitHub Actions
- Python test suite

### Preconditions

Backend code exists.

### Trigger

Backend CI workflow runs.

### Inputs

Backend code and tests.

### Business Rules

- Automated tests are required.
- Tests must execute before production backend deployment.
- Test framework selection remains intentionally deferred.

### Success State

Tests execute and results are reported.

### Failure States

- Test failure.
- Test execution failure.
- Missing required tests.

### Permissions

CI may execute tests without unnecessary production-secret exposure.

### Edge Cases

- Dependency failure.
- Environment differences.
- Flaky tests.

### Dependencies

- CR-AZ-MVP-010
- CR-AZ-MVP-013

### Acceptance Criteria

See `AC-011`.

### Non-Functional Requirements

- Repeatable.
- Observable CI results.

### Out of Scope

Final test-framework selection within this PRD.

---

## CR-AZ-MVP-012 — ARM Infrastructure as Code

### Problem / User Story

As a technical interviewer, I need Azure infrastructure represented as source-controlled IaC so the environment is reproducible.

### Actors

- Project Owner
- GitHub
- Azure deployment process

### Preconditions

Required resources are identified.

### Trigger

Provisioning or infrastructure change occurs.

### Inputs

ARM templates and approved parameters.

### Business Rules

- ARM is the approved IaC format.
- Production infrastructure must not depend on undocumented manual configuration.
- Backend resources use the Consumption-plan direction.

### Success State

Required infrastructure can be represented and provisioned from source-controlled ARM definitions.

### Failure States

- Missing resource definition.
- Deployment failure.
- Undocumented manual-only configuration.

### Permissions

Deployment identity has only required permissions.

### Edge Cases

- Parameter differences.
- Azure service changes.
- Configuration drift.

### Dependencies

- CR-AZ-MVP-004
- CR-AZ-MVP-005
- CR-AZ-MVP-008
- CR-AZ-MVP-010
- CR-AZ-MVP-013

### Acceptance Criteria

See `AC-012`.

### Non-Functional Requirements

- Reproducibility.
- Source control.
- Cost-consciousness.

### Out of Scope

Terraform/Bicep substitution unless scope changes.

---

## CR-AZ-MVP-013 — Backend GitHub Repository and CI/CD

### Problem / User Story

As the project owner, I need backend changes tested and deployed automatically so production releases do not depend on manual laptop deployment.

### Actors

- Project Owner
- GitHub
- GitHub Actions
- Azure

### Preconditions

Backend repository exists.

### Trigger

An approved backend/IaC change enters the workflow.

### Inputs

- Python code.
- Tests.
- ARM templates.
- Secure deployment configuration.

### Business Rules

- Repository: `s1xte3n/sixteen-backend`.
- Tests must run before deployment.
- Failed tests block production deployment.
- No credentials may be committed.
- `main` represents production.

### Success State

Validated backend changes deploy through automation.

### Failure States

- Tests fail.
- Deployment fails.
- Credentials/configuration are invalid.

### Permissions

CI identity is limited to required deployment operations.

### Edge Cases

- Partial deployment.
- Concurrent workflows.
- Incorrect branch.

### Dependencies

- CR-AZ-MVP-011
- CR-AZ-MVP-012

### Acceptance Criteria

See `AC-013`.

### Non-Functional Requirements

- Repeatable.
- Secure.
- Observable.

### Out of Scope

Manual production deployment as the normal workflow.

---

## CR-AZ-MVP-014 — Frontend GitHub Repository and CI/CD

### Problem / User Story

As the project owner, I need frontend changes automatically published so website releases are repeatable.

### Actors

- Project Owner
- GitHub
- GitHub Actions
- Azure Storage/CDN

### Preconditions

Frontend repository exists.

### Trigger

An approved frontend change enters the workflow.

### Inputs

- HTML.
- CSS.
- JavaScript.
- Secure deployment configuration.

### Business Rules

- Repository: `s1xte3n/sixteen-frontend`.
- Production publication follows the approved branch model.
- Secrets are not committed.
- Cache invalidation is performed when required.

### Success State

Frontend changes are automatically published.

### Failure States

- Workflow failure.
- Upload failure.
- Invalid deployment credentials.
- Stale cache remains unresolved.

### Permissions

CI identity has only required publication permissions.

### Edge Cases

- Partial upload.
- Cache delay.
- Workflow rerun.

### Dependencies

- CR-AZ-MVP-004
- CR-AZ-MVP-005
- CR-AZ-MVP-006

### Acceptance Criteria

See `AC-014`.

### Non-Functional Requirements

- Repeatability.
- Security.
- Observable failures.

### Out of Scope

Routine manual production deployment.

---

## CR-AZ-MVP-015 — Public Production Deployment

### Problem / User Story

As a recruiter, hiring manager, or technical interviewer, I need a stable public resume URL without local setup.

### Actors

- Public Visitor
- Project Owner
- Azure

### Preconditions

All MVP capabilities are implemented and validated.

### Trigger

Production release occurs.

### Inputs

Approved frontend, backend, infrastructure, and content.

### Business Rules

- Production corresponds to `main`.
- Public deployment must satisfy security and cost constraints.

### Success State

The resume is publicly available over HTTPS and the visitor counter works through the approved flow.

### Failure States

- Site unavailable.
- API unavailable.
- Counter broken.
- Cost constraint violated.
- Production contains unapproved content.

### Permissions

- Public read.
- Production release restricted.

### Edge Cases

- DNS propagation.
- CDN cache.
- Function cold start.
- Temporary dependency outage.

### Dependencies

CR-AZ-MVP-001 through CR-AZ-MVP-014.

### Acceptance Criteria

See `AC-015`.

### Non-Functional Requirements

- Availability.
- HTTPS.
- Security.
- Cost compliance.
- Reproducibility.

### Out of Scope

Unapproved multi-environment platform expansion.

---

## CR-AZ-MVP-016 — Project-Learning Blog Post

### Problem / User Story

As a technical interviewer, I need a linked project-learning article so I can understand lessons learned from the project.

### Actors

- Public Visitor
- Project Owner

### Preconditions

Article is publicly published.

### Trigger

Visitor selects the project-learning link.

### Inputs

Article and public URL.

### Business Rules

- Resume must link to the article.
- Blog platform remains undecided.

### Success State

The article opens through a working public link.

### Failure States

- Missing article.
- Broken link.
- Private article.
- Deleted article.

### Permissions

- Public read.
- Owner controls publication.

### Edge Cases

- Blog platform changes.
- Article URL changes.

### Dependencies

- CR-AZ-MVP-001
- CR-AZ-MVP-014
- CR-AZ-MVP-015

### Acceptance Criteria

See `AC-016`.

### Non-Functional Requirements

Article must be publicly reachable at acceptance.

### Out of Scope

A full blog platform or multiple articles.

# 8. Cross-Cutting Non-Functional Requirements

## Security

- No credentials or secrets in source control.
- No direct browser-to-Cosmos DB access.
- CI/CD authentication must use secure mechanisms.
- API errors must not disclose secrets.
- Deployment identities must follow least privilege.

## Cost

- Zero/near-zero cost is the approved constraint.
- Any unavoidable cost requires explicit approval.
- Current Azure pricing and service suitability must be validated before production.

## Reliability

- Counter state survives normal page reloads and normal backend redeployment.
- CI/CD failures are observable.
- Deployments are repeatable.

## Maintainability

- Frontend and backend remain separate repositories.
- Infrastructure remains source-controlled.
- Documentation reflects approved requirements and final state.

## Compatibility

- Resume renders in supported modern browsers.
- Resume remains readable across common desktop and mobile viewports.

## Privacy

- Public resume content requires owner approval.
- Visitor-counter functionality does not authorize unrelated personal tracking.

# 9. Contradictions

## C-001 — Custom Domain vs Free Hostname

The original challenge describes a custom DNS domain. The approved project state excludes paid-domain purchase and prefers a free hostname/subdomain.

This must not be silently reconciled.

See `OR-002` in `OPEN-REQUIREMENTS.md`.

## C-002 — AZ-900

The original challenge requires AZ-900 or an advanced Azure certification.

The approved project explicitly removes AZ-900.

This is a deliberate project deviation.

## C-003 — CDN/HTTPS vs Zero Cost

HTTPS/CDN is required while the project has a zero/near-zero-cost constraint.

The exact service configuration and cost must be validated.

See `OR-004`.

# 10. Requirements Not Yet Fully Testable

The following requirements require decisions before their final acceptance criteria can be considered fully closed:

1. Visitor-count semantics.
2. Public hostname/custom-domain interpretation.
3. Numeric definition of zero/near-zero cost.
4. HTTPS/CDN service configuration and pricing.
5. Final public resume content approval.
6. Python testing framework selection.
7. Blog platform selection.
8. API request/response contract.
9. Visitor-counter failure UX.
10. Supported browser/version baseline.
11. Availability target.
12. Cache freshness target.
13. DNS propagation expectation.

# 11. Product Completion Gate

The MVP is complete only when:

1. Every MVP requirement has passing acceptance criteria.
2. No P0 ambiguity remains.
3. No P1 ambiguity remains hidden.
4. Explicit deviations from the original challenge are documented.
5. Production configuration satisfies the approved cost constraint.
6. Final public resume content has been approved.

// USER-STORIES.md

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

// ACCEPTANCE-CRITERIA.md

# Acceptance Criteria

## 1. Purpose

This document defines testable acceptance criteria for every MVP requirement in `docs/product/PRD.md`.

## 2. Global Acceptance Conditions

- Production means the state represented by `main`.
- Final public resume content must be approved by the project owner.
- No credentials or secrets may be committed to source control.
- Acceptance testing must use the final approved configuration.
- A requirement blocked by an unresolved high-impact decision cannot be considered fully accepted.

---

# AC-001 — Public Resume Content

**Requirement:** CR-AZ-MVP-001

### Acceptance Criteria

- [ ] The public resume URL opens successfully.
- [ ] The page displays the approved resume content.
- [ ] Public resume content can be traced to the supplied CV or explicitly approved additions.
- [ ] AZ-900 is not falsely represented as a project requirement or completed certification.
- [ ] Rejected or private content is absent from production.

---

# AC-002 — HTML Resume

**Requirement:** CR-AZ-MVP-002

### Acceptance Criteria

- [ ] The public resume is delivered as an HTML webpage.
- [ ] A supported modern browser renders the resume without requiring a Word/PDF viewer.
- [ ] The core resume content is available in HTML.
- [ ] The product is not dependent on a PDF or Word document for normal resume viewing.

---

# AC-003 — CSS Styling

**Requirement:** CR-AZ-MVP-003

### Acceptance Criteria

- [ ] The resume has intentional styling beyond browser-default raw HTML.
- [ ] Resume content remains readable on a common mobile viewport.
- [ ] Resume content remains readable on a common desktop viewport.
- [ ] CSS failure does not prevent access to the underlying resume content.

---

# AC-004 — Azure Storage Static Website

**Requirement:** CR-AZ-MVP-004

### Acceptance Criteria

- [ ] Production static website hosting uses Azure Storage.
- [ ] HTML files are served from Azure Storage.
- [ ] CSS assets are served successfully.
- [ ] JavaScript assets are served successfully.
- [ ] A successful frontend deployment results in the expected production website content being available.

---

# AC-005 — HTTPS/CDN Delivery

**Requirement:** CR-AZ-MVP-005

### Acceptance Criteria

- [ ] The approved public hostname serves the resume over HTTPS.
- [ ] The final production delivery configuration contains the approved CDN/delivery layer.
- [ ] HTTPS certificate handling is operational.
- [ ] The selected configuration has been validated against the approved cost constraint.
- [ ] Any required HTTP-to-HTTPS behavior is documented and verified.

### Open Dependency

The exact CDN/HTTPS service configuration remains unresolved.

See `OR-004`.

---

# AC-006 — Public Hostname/DNS

**Requirement:** CR-AZ-MVP-006

### Acceptance Criteria

- [ ] The approved public hostname resolves successfully.
- [ ] The hostname resolves to the intended production delivery endpoint.
- [ ] The resume loads through the hostname.
- [ ] The hostname solution does not introduce an unapproved paid domain.
- [ ] The free-hostname/subdomain interpretation has been explicitly approved before final acceptance.

### Open Dependency

The exact hostname/DNS solution remains unresolved.

See `OR-002`.

---

# AC-007 — JavaScript Visitor Counter

**Requirement:** CR-AZ-MVP-007

### Acceptance Criteria

- [ ] When the counter service is healthy, JavaScript displays the returned counter value.
- [ ] The counter request is initiated by the website JavaScript.
- [ ] Browser network inspection confirms that JavaScript communicates with the approved API rather than directly with Cosmos DB.
- [ ] API failure does not prevent the visitor from reading the resume.
- [ ] API failure does not expose database credentials.
- [ ] A normal reload returns a value based on persisted counter state.

### Open Dependency

The exact definition of a visitor is unresolved.

See `OR-001`.

---

# AC-008 — Visitor Counter Persistence

**Requirement:** CR-AZ-MVP-008

### Acceptance Criteria

- [ ] A valid initial counter operation creates or initializes the required persistent state.
- [ ] A subsequent valid operation reflects the prior state according to the approved counting semantics.
- [ ] Counter state survives normal backend redeployment.
- [ ] Counter state survives normal frontend redeployment.
- [ ] Browser network inspection shows no direct Cosmos DB access.
- [ ] Database failure produces a controlled failure state.

---

# AC-009 — Visitor Counter API

**Requirement:** CR-AZ-MVP-009

### Acceptance Criteria

- [ ] A valid frontend counter request reaches the approved API.
- [ ] The API returns the required counter result for a valid request.
- [ ] Invalid requests return a defined controlled error.
- [ ] Database failure returns a defined controlled API failure.
- [ ] The API does not expose database credentials.
- [ ] The browser does not connect directly to Cosmos DB.

### Open Dependency

The exact API request/response contract remains unresolved.

See `OR-008`.

---

# AC-010 — Python Azure Function

**Requirement:** CR-AZ-MVP-010

### Acceptance Criteria

- [ ] API request handling is performed by Azure Functions.
- [ ] Backend implementation uses Python.
- [ ] The function can communicate with the required persistence layer.
- [ ] Function permissions are limited to required operations.
- [ ] Runtime errors return controlled responses.
- [ ] Error responses do not disclose secrets.

---

# AC-011 — Automated Python Tests

**Requirement:** CR-AZ-MVP-011

### Acceptance Criteria

- [ ] Backend CI automatically executes the Python test suite.
- [ ] A deliberately broken required behavior causes the test workflow to fail.
- [ ] Passing tests produce a successful test result.
- [ ] Test execution results are visible in the CI workflow.
- [ ] Tests can execute repeatedly in the CI environment.
- [ ] The selected testing framework is documented before final acceptance.

### Open Dependency

The Python testing framework is intentionally deferred.

See `OR-006`.

---

# AC-012 — ARM Infrastructure as Code

**Requirement:** CR-AZ-MVP-012

### Acceptance Criteria

- [ ] Required Azure project infrastructure is represented by ARM templates.
- [ ] ARM templates are stored in source control.
- [ ] Required infrastructure can be provisioned/configured through the approved IaC process.
- [ ] No undocumented manual production configuration is required for normal provisioning.
- [ ] Backend resources use the approved Consumption-plan direction.
- [ ] Infrastructure changes are represented as source-controlled changes.

---

# AC-013 — Backend GitHub Repository and CI/CD

**Requirement:** CR-AZ-MVP-013

### Acceptance Criteria

- [ ] The backend repository is `s1xte3n/sixteen-backend`.
- [ ] Approved backend changes trigger the intended workflow.
- [ ] Automated tests execute before production deployment.
- [ ] A failing required test prevents production deployment.
- [ ] Passing tests allow deployment when deployment prerequisites are valid.
- [ ] Deployment failures are reported by the workflow.
- [ ] No Azure credentials are committed to the repository.
- [ ] Production deployment represents the approved `main` branch.

---

# AC-014 — Frontend GitHub Repository and CI/CD

**Requirement:** CR-AZ-MVP-014

### Acceptance Criteria

- [ ] The frontend repository is `s1xte3n/sixteen-frontend`.
- [ ] Approved frontend production changes trigger the intended workflow.
- [ ] Frontend files are automatically published to Azure Storage.
- [ ] Publication failure causes the workflow to report failure.
- [ ] Required CDN cache invalidation is handled where applicable.
- [ ] No Azure credentials are committed to the repository.
- [ ] Production publication represents the approved `main` branch.

---

# AC-015 — Public Production Deployment

**Requirement:** CR-AZ-MVP-015

### Acceptance Criteria

- [ ] The public hostname resolves successfully.
- [ ] The resume loads over HTTPS.
- [ ] The resume content is the approved production content.
- [ ] The visitor counter can complete the approved frontend → API → persistence flow.
- [ ] Production corresponds to the approved `main` state.
- [ ] Cost validation passes the approved cost threshold.
- [ ] Repository review confirms that no Azure credentials or secrets are committed.
- [ ] Required Azure infrastructure is represented in source-controlled IaC.

---

# AC-016 — Project-Learning Blog Post

**Requirement:** CR-AZ-MVP-016

### Acceptance Criteria

- [ ] The resume contains a project-learning article link.
- [ ] The link opens from an external browser session.
- [ ] The article is publicly reachable.
- [ ] The article describes lessons learned from the project.
- [ ] The final article URL is recorded in project documentation.
- [ ] The final publishing platform is documented.

### Open Dependency

The blog platform remains unresolved.

See `OR-007`.

---

# 3. MVP Acceptance Gate

The MVP cannot be declared fully accepted until:

- [ ] All 16 MVP requirements have passing acceptance criteria.
- [ ] Visitor-count semantics are explicitly defined.
- [ ] Public hostname interpretation is explicitly defined.
- [ ] Numeric cost ceiling is explicitly defined.
- [ ] HTTPS/CDN configuration and cost have been validated.
- [ ] Final public resume content has been approved.
- [ ] No P0/P1 ambiguity remains hidden.

// SCOPE.md

# Product Scope

## 1. Purpose

This document defines the product scope for the Cloud Resume Challenge — Azure and separates confirmed MVP scope from future priorities and explicit exclusions.

---

# 2. MVP Scope

The MVP consists of the following requirements:

1. Public resume content.
2. HTML resume.
3. CSS styling.
4. Azure Storage static website hosting.
5. HTTPS/CDN delivery.
6. Public hostname/DNS.
7. JavaScript visitor counter.
8. Cosmos DB Table API persistence.
9. Visitor-counter API.
10. Python Azure Function.
11. Automated Python tests.
12. ARM infrastructure as code.
13. Backend GitHub repository and CI/CD.
14. Frontend GitHub repository and CI/CD.
15. Public production deployment.
16. Project-learning blog post.

Each MVP requirement has a corresponding requirement ID in `PRD.md` and acceptance criteria in `ACCEPTANCE-CRITERIA.md`.

---

# 3. P1 Scope

P1 represents potential post-MVP improvements that are related to the product purpose but are not required for MVP completion.

Potential P1 scope:

- Enhanced resume presentation within the existing product purpose.
- Additional approved project evidence.
- Additional public project links.
- Defined user-facing visitor-counter failure messaging.
- Improved documentation of operational behavior.
- Additional resume sections if justified by the final resume-content review.

P1 features require explicit approval before entering the implementation scope.

---

# 4. P2 Scope

Potential P2 scope:

- Additional public content sections.
- Additional project-learning articles.
- Non-identifying website analytics.
- Additional deployment environments.
- Additional operational reporting.
- Expanded technical project documentation.
- Additional cloud-service demonstrations.

These are future possibilities and are not MVP commitments.

---

# 5. P3 / Future Ideas

Potential P3/future ideas include:

- General portfolio/CMS functionality.
- Resume administration interface.
- Visitor analytics dashboard.
- Multiple resume versions.
- Internationalized resume content.
- Additional interactive website functionality.
- Public content-management workflows.
- Automated content publishing.

These ideas must not be introduced into MVP without an explicit scope decision.

---

# 6. Explicit Exclusions

The following are explicitly outside the current product scope:

- AZ-900 certification.
- Paid domain purchase unless separately approved.
- Unrelated application or portfolio features.
- Unapproved recurring or one-time costs.
- Direct browser-to-Cosmos DB access.
- Manual production infrastructure configuration as the intended workflow.
- Visitor accounts.
- Public resume editing.
- General CMS functionality.
- Unrelated personal analytics or tracking.
- Replacing HTML/CSS/JavaScript with a frontend framework without a scope change.
- Replacing Python/Azure Functions without a scope change.
- Replacing Cosmos DB Table API without a scope change.
- Replacing ARM IaC without a scope change.
- A general-purpose blog platform as part of this application.

---

# 7. Scope Constraints

## Cost

The project is intended to remain at zero or near-zero cost.

A numeric cost ceiling has not yet been defined.

Any unavoidable cost requires explicit approval.

## Certification

AZ-900 is not part of this project.

The existing AI-901 certification may appear on the resume where appropriate but does not become a substitute project requirement.

## Technology

The approved technology direction is:

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- Python
- Azure Functions

### Database

- Azure Cosmos DB
- Table API

### Infrastructure

- ARM templates

### Hosting

- Azure Storage static website

### Delivery

- HTTPS
- CDN
- Public hostname/DNS

### Source Control

- GitHub
- Separate frontend/backend repositories

### CI/CD

- GitHub Actions

---

# 8. Scope Change Rules

A proposed feature is a scope change if it:

- introduces a new product capability;
- changes an approved technology requirement;
- introduces a new recurring cost;
- changes the intended target audience;
- changes the visitor-counter purpose;
- changes the public deployment model;
- removes an approved MVP requirement.

Scope changes must identify:

1. User value.
2. Affected requirements.
3. Cost impact.
4. Security/privacy impact.
5. Dependencies.
6. Acceptance criteria.
7. Impact on MVP completion.

No feature becomes part of the product solely because it is technically useful.

---

# 9. Current Scope Boundary

The product is a focused Cloud Resume Challenge implementation.

It is not currently a general-purpose personal portfolio platform.

The project should prioritize evidence of:

- Azure cloud engineering.
- Serverless development.
- Backend development.
- Infrastructure as Code.
- Automated testing.
- CI/CD.
- Secure cloud deployment.
- Practical software engineering.

Features unrelated to those objectives require explicit scope approval.

---

# 10. Scope Completion

MVP scope is considered complete when:

- Every MVP requirement is implemented.
- Every MVP requirement has passing acceptance criteria.
- No P0/P1 ambiguity remains hidden.
- Approved production constraints are satisfied.
- Public deployment is operational.
- Documentation accurately represents the final scope.

// OPEN-REQUIREMENTS.md

# Open Requirements

## 1. Purpose

This document records unresolved product decisions, ambiguities, contradictions, hidden dependencies, missing requirements, and requirements that are not yet objectively testable.

No ambiguity in this document should be silently resolved during implementation.

---

# 2. Priority Definitions

| Priority | Meaning |
|---|---|
| P0 | Critical; blocks safe/product-valid progress |
| P1 | High impact; must be resolved before affected MVP acceptance |
| P2 | Important; may be resolved during implementation if it does not block acceptance |
| P3 | Minor refinement |

---

# 3. Open Decisions

| ID | Priority | Decision / Ambiguity | Affected Requirements | Status |
|---|---:|---|---|---|
| OR-001 | P1 | Define what counts as a visitor: page load, request, unique visitor, session, or another unit. | MVP-007, MVP-008, MVP-009 | Open |
| OR-002 | P1 | Confirm whether a free hostname/subdomain satisfies the original challenge's custom-domain/DNS intent. | MVP-006, MVP-015 | Open |
| OR-003 | P1 | Define a numeric maximum acceptable project cost. | MVP-005, MVP-006, MVP-012, MVP-015 | Open |
| OR-004 | P1 | Validate exact HTTPS/CDN service configuration and current cost suitability. | MVP-005, MVP-015 | Open |
| OR-005 | P1 | Approve exact public resume content from the supplied CV. | MVP-001, MVP-015 | Open |
| OR-006 | P2 | Select Python testing framework. | MVP-011, MVP-013 | Intentionally deferred |
| OR-007 | P2 | Select blog platform. | MVP-016 | Open |
| OR-008 | P2 | Define visitor-counter API request/response contract. | MVP-009, MVP-010 | Open |
| OR-009 | P2 | Define user-visible behavior when counter API/database fails. | MVP-007, MVP-009 | Open |
| OR-010 | P2 | Define supported browser/version baseline. | MVP-001, MVP-003, MVP-015 | Open |
| OR-011 | P2 | Define production availability expectation/SLO, if any. | MVP-015 | Open |
| OR-012 | P2 | Define DNS propagation/stability expectation. | MVP-006, MVP-015 | Open |
| OR-013 | P3 | Define whether blog link opens in same tab or new tab. | MVP-016 | Open |

---

# 4. P1 Requirements

## OR-001 — Visitor Definition

### Question

What exactly constitutes a visitor?

Possible interpretations include:

- Every page load.
- Every counter API request.
- Every browser session.
- Every unique visitor.
- Another explicitly defined unit.

### Why It Matters

Without this definition, the visitor counter cannot be objectively tested.

### Affected Requirements

- CR-AZ-MVP-007
- CR-AZ-MVP-008
- CR-AZ-MVP-009

### Status

Open.

---

## OR-002 — Free Hostname vs Custom Domain

### Question

Does the approved free hostname/subdomain satisfy the original challenge requirement for DNS/custom-domain functionality?

### Conflict

The original challenge describes pointing a custom DNS domain to the CDN endpoint.

The approved project state explicitly excludes purchasing a paid domain.

### Why It Matters

The implementation cannot be considered compliant with the approved project interpretation until the intended meaning is documented.

### Affected Requirements

- CR-AZ-MVP-006
- CR-AZ-MVP-015

### Status

Open.

---

## OR-003 — Numeric Cost Ceiling

### Question

What exact maximum cost is acceptable?

The project currently states:

> Zero/near-zero cost.

This is not objectively testable without a numeric threshold.

### Required Decision

Define one of:

- `$0`
- `$X/month`
- `$X/year`
- another explicit threshold.

### Affected Requirements

- CR-AZ-MVP-005
- CR-AZ-MVP-006
- CR-AZ-MVP-012
- CR-AZ-MVP-015

### Status

Open.

---

## OR-004 — HTTPS/CDN Configuration

### Question

Which current Azure delivery configuration satisfies:

- Azure Storage hosting;
- HTTPS;
- CDN/delivery requirement;
- public hostname;
- cost constraint?

### Why It Matters

The exact service configuration affects architecture, pricing, DNS, certificate handling, caching, and acceptance testing.

### Affected Requirements

- CR-AZ-MVP-005
- CR-AZ-MVP-015

### Status

Open.

---

## OR-005 — Public Resume Content

### Question

Which exact information from the supplied CV is approved for public publication?

### Why It Matters

The CV may contain information that should not necessarily become publicly accessible.

### Required Decision

Owner review of:

- Personal information.
- Contact information.
- Professional history.
- Skills.
- Certifications.
- Education.
- Projects.
- External links.
- Any other identifying information.

### Affected Requirements

- CR-AZ-MVP-001
- CR-AZ-MVP-015

### Status

Open.

---

# 5. P2 Requirements

## OR-006 — Python Testing Framework

### Question

Which Python testing framework will be used?

### Status

Intentionally deferred.

### Affected Requirements

- CR-AZ-MVP-011
- CR-AZ-MVP-013

---

## OR-007 — Blog Platform

### Question

Which platform will host the required project-learning article?

### Status

Open.

### Affected Requirement

CR-AZ-MVP-016.

---

## OR-008 — Visitor API Contract

### Question

What is the exact API contract?

At minimum, the final specification must define:

- HTTP method.
- Endpoint purpose.
- Request inputs.
- Required/optional parameters.
- Successful response.
- Error responses.
- HTTP status behavior.
- Counter semantics.
- CORS behavior.

### Status

Open.

---

## OR-009 — Counter Failure UX

### Question

What should the visitor see if the API or database is unavailable?

Possible product behaviors include:

- Hide the counter.
- Display an unavailable state.
- Display the last known value.
- Display another approved fallback.

No option is currently selected.

### Status

Open.

---

## OR-010 — Browser Support

### Question

Which browsers and versions are supported?

### Status

Open.

---

## OR-011 — Availability Target

### Question

Is an explicit availability target required?

Examples could include:

- No formal SLO.
- Monthly availability target.
- Another documented expectation.

### Status

Open.

---

## OR-012 — DNS Propagation

### Question

What DNS propagation/stability behavior is acceptable during deployment?

### Status

Open.

---

# 6. P3 Requirements

## OR-013 — Blog Link Behavior

### Question

Should the project-learning link open in:

- The same browser tab.
- A new browser tab.
- Another explicitly defined behavior?

### Status

Open.

---

# 7. Contradictions

## IC-001 — Custom Domain vs Free Hostname

The original challenge describes a custom DNS domain.

The approved project state excludes paid domain purchase and prefers a free hostname/subdomain.

This is a genuine requirement conflict and must be explicitly interpreted.

---

## IC-002 — AZ-900

The original challenge requires AZ-900 or an advanced Azure certification.

The approved project explicitly excludes AZ-900.

This is a deliberate project deviation rather than an unresolved ambiguity.

---

## IC-003 — CDN/HTTPS vs Zero Cost

The project requires HTTPS/CDN functionality while simultaneously targeting zero/near-zero cost.

The actual current service configuration and pricing must be validated.

---

# 8. Hidden Dependencies

The following dependencies could affect MVP acceptance:

1. Azure subscription must support required resources.
2. Required Azure services must remain available and suitable.
3. Azure service pricing must remain within the approved cost threshold.
4. A suitable free hostname/subdomain mechanism must exist.
5. GitHub Actions must support secure deployment authentication.
6. Public resume content requires owner approval.
7. A public blog platform must be available.
8. DNS configuration must support the chosen delivery architecture.
9. CDN/delivery configuration must support the selected hostname.
10. Backend API must support the frontend's final visitor-counter contract.

---

# 9. Missing Requirements

The current project requirements do not objectively define:

- Visitor-counting semantics.
- API request/response contract.
- API authentication requirements.
- Exact CORS behavior.
- Numeric cost ceiling.
- Browser support matrix.
- Availability target.
- Accessibility target.
- Performance target.
- Cache freshness target.
- DNS propagation expectations.
- Blog article length/content minimum.
- Exact required resume sections.
- Rollback expectations.
- Counter failure UX.
- Monitoring/alerting requirements.

These have intentionally not been invented.

---

# 10. Requirements That Cannot Yet Be Tested Objectively

## NTR-001 — Zero/Near-Zero Cost

No numeric threshold exists.

## NTR-002 — Visitor Count

The counting unit is undefined.

## NTR-003 — Public Hostname

The exact hostname mechanism/provider is not selected.

## NTR-004 — Short Blog Post

No measurable length or content structure is specified.

## NTR-005 — Readable Resume

No explicit accessibility/readability baseline is defined.

## NTR-006 — Production-Style

"Production-style" is descriptive rather than independently testable.

The product therefore relies on concrete requirements such as:

- IaC.
- Automated testing.
- CI/CD.
- HTTPS.
- Security.
- Public deployment.
- Source control.
- Serverless architecture.

---

# 11. Requirements Closure Rule

The PRD phase is complete only when:

1. Every MVP feature has testable acceptance criteria.
2. No P0 ambiguity remains.
3. No P1 ambiguity is hidden.
4. All deliberate deviations from the original challenge are documented.
5. The numeric cost constraint is defined.
6. Visitor-count semantics are defined.
7. Public hostname interpretation is defined.
8. HTTPS/CDN configuration is validated.
9. Final public resume content is approved.

// ARTIFACT-INDEX.md

# Artifact Index

## 1\. Purpose

This document identifies the project's authoritative documentation and current artifact status.

\---

# 2\. Project Documentation

|Artifact|Purpose|Status|Source of Truth|
|-|-|-|-|
|`docs/project/PROJECT-OVERVIEW.md`|Project purpose, users, goals, scope, constraints, stack, deployment, dependencies, assumptions, and risks|Current|Yes|
|`docs/project/PROJECT-STATUS.md`|Current project state, completed/incomplete work, blockers, next gate, and evidence|Current|Yes|
|`docs/project/DECISIONS.md`|Confirmed decisions, rationale, alternatives, consequences, and open decisions|Current|Yes|
|`docs/project/OPEN-QUESTIONS.md`|Discovery-stage unresolved questions, priorities, owners, and decision status|Current|Yes|
|`docs/project/PROJECT-CHARTER.md`|Project scope, MVP, stakeholders, milestones, success criteria, and Definition of Done|Current|Yes|
|`docs/project/ARTIFACT-INDEX.md`|Project artifact index and documentation governance|Updated|Yes|

\---

# 3\. Product Documentation

|Artifact|Purpose|Status|Source of Truth|
|-|-|-|-|
|`docs/product/PRD.md`|Complete product requirements and feature-level requirements|Created|Yes|
|`docs/product/USER-STORIES.md`|User stories and use cases mapped to requirement IDs|Created|Yes|
|`docs/product/ACCEPTANCE-CRITERIA.md`|Testable acceptance criteria for every MVP requirement|Created|Yes|
|`docs/product/SCOPE.md`|MVP, P1/P2/P3 scope, explicit exclusions, and future ideas|Created|Yes|
|`docs/product/OPEN-REQUIREMENTS.md`|Unresolved product decisions, ambiguities, contradictions, hidden dependencies, and untestable requirements|Created|Yes|

\---

# 4\. Source Requirements

|Artifact|Purpose|Status|
|-|-|-|
|Cloud Resume Challenge — Azure requirements|Original challenge requirements baseline|Current|
|Project owner's CV|Resume-content source|Current|
|Approved project state|Project-specific requirements and decisions|Current|

\---

# 5\. Source Code Repositories

|Repository|Purpose|Status|
|-|-|-|
|`github.com/s1xte3n/sixteen-frontend`|Frontend resume application|Exists; empty|
|`github.com/s1xte3n/sixteen-backend`|Backend/API application|Exists; empty|

\---

# 6\. Current Implementation Artifacts

|Artifact|Status|
|-|-|
|Frontend source code|Not started|
|Backend source code|Not started|
|ARM templates|Not started|
|Python tests|Not started|
|GitHub Actions frontend workflow|Not started|
|GitHub Actions backend workflow|Not started|
|Azure project resources|No project resources confirmed|
|Public deployment|Not started|
|Public hostname|Not selected|
|Blog post|Not created|

\---

# 7\. Branch Model

|Branch|Intended Role|Current Status|
|-|-|-|
|`develop`|Development/integration|Intended|
|`main`|Production|Intended|

The repositories are currently empty, so actual branch implementation/state still needs to be established.

\---

# 8\. External Artifacts

## Resume Content

The supplied CV is the current source material for the public resume.

Before production deployment, final public content must be reviewed and approved by the project owner.

**Status:** Awaiting final public-content approval.

## Blog Post

A project-learning blog post is required by the approved MVP scope.

**Status:** Not created.

**Platform:** Undecided.

\---

# 9\. Product Requirements Artifacts

## PRD

**Path:** `docs/product/PRD.md`

**Status:** Created.

**Purpose:** Defines the product purpose, actors, confirmed requirements, assumptions, MVP requirements, non-functional requirements, contradictions, and completion gate.

## User Stories

**Path:** `docs/product/USER-STORIES.md`

**Status:** Created.

**Purpose:** Maps user stories and use cases to product requirement IDs.

## Acceptance Criteria

**Path:** `docs/product/ACCEPTANCE-CRITERIA.md`

**Status:** Created.

**Purpose:** Provides testable acceptance criteria for every MVP requirement.

## Scope

**Path:** `docs/product/SCOPE.md`

**Status:** Created.

**Purpose:** Defines MVP, P1, P2, P3, explicit exclusions, and scope governance.

## Open Requirements

**Path:** `docs/product/OPEN-REQUIREMENTS.md`

**Status:** Created.

**Purpose:** Tracks unresolved decisions, ambiguities, contradictions, hidden dependencies, missing requirements, and requirements that cannot yet be objectively tested.

\---

# 10\. Product Phase Status

**Requirements documentation:** Created.

**MVP acceptance coverage:** Complete.

**PRD closure:** Pending explicit resolution of P1 product decisions.

Current P1 open items:

1. Visitor-count semantics.
2. Free hostname/subdomain versus original custom-domain interpretation.
3. Numeric cost ceiling.
4. HTTPS/CDN service suitability and cost validation.
5. Final public resume-content approval.

No implementation tasks are defined by these product documents.

\---

# 11\. Artifact Governance

When a requirement, decision, or project state changes:

1. Update the affected product or project document.
2. Record significant confirmed decisions in `docs/project/DECISIONS.md`.
3. Record unresolved decisions in `docs/product/OPEN-REQUIREMENTS.md` or `docs/project/OPEN-QUESTIONS.md`, depending on whether they are product or project-level.
4. Update `docs/project/PROJECT-STATUS.md` when implementation state changes.
5. Synchronize this artifact index.
6. Do not silently change confirmed requirements.
7. Do not mark unresolved requirements as complete without explicit evidence.

\---

# 12\. PRD Closure Rule

The requirements phase is complete only when:

* Every MVP feature has testable acceptance criteria.
* No high-impact ambiguity is hidden.
* All P0/P1 requirements are explicitly resolved or formally accepted as a documented deviation.
* The final scope is reflected consistently across the product and project documentation.

