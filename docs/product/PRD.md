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