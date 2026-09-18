# Product Requirements Document

## 1. Document Control

| Field | Value |
|---|---|
| Product | Cloud Resume Challenge — Azure |
| Document status | Complete requirements draft; PRD closure pending explicit P1 decisions |
| Primary users | Recruiters, hiring managers, technical interviewers |
| Secondary users | Public visitors |
| Product owner | Project Owner |
| Target platform | Microsoft Azure |
| Target region | East US |
| Deployment environments | One |
| Frontend repository | `s1xte3n/sixteen-resume-frontend` |
| Backend repository | `s1xte3n/sixteen-resume-backend` |
| Development/integration branch | `develop` |
| Production branch | `main` |
| Cost direction | Zero/R0 where possible; otherwise lowest-cost viable option, subject to explicit approval |
| Target completion | 30 September 2026 |

## 2. Product Purpose

Provide a public personal resume website that demonstrates practical Azure cloud engineering, serverless development, backend development, Infrastructure as Code, automated testing, source control, CI/CD, secure cloud deployment, and practical software engineering.

The product is intentionally a focused Cloud Resume Challenge implementation rather than a general-purpose portfolio platform.

## 3. Confirmed Requirements

The following are confirmed project requirements and must not be silently changed:

1. A public personal resume website is required.
2. Primary audiences are recruiters, hiring managers, and technical interviewers.
3. Frontend technology is plain HTML, CSS, and JavaScript.
4. Azure Storage static website hosting is required.
5. HTTPS is required.
6. CDN/delivery capability is part of the approved delivery direction.
7. A public hostname/DNS solution is required.
8. Paid domain purchase is excluded unless separately approved.
9. A JavaScript visitor counter is required.
10. Counter persistence uses Azure Cosmos DB Table API.
11. Browser JavaScript must not access Cosmos DB directly.
12. Backend compute uses Python on Azure Functions.
13. Automated Python tests are required.
14. Azure infrastructure uses ARM templates.
15. Frontend and backend use separate GitHub repositories.
16. Backend CI/CD must run tests before deployment.
17. Frontend CI/CD must automatically publish website changes.
18. Azure credentials and secrets must never be committed to source control.
19. Free or consumption-based options are preferred.
20. East US is the target Azure region.
21. `develop` is the development/integration branch.
22. `main` represents production.
23. A short project-learning article must be linked from the resume.
24. The project intentionally excludes AZ-900; AI-901 may be displayed as an existing certification.
25. The supplied CV is the source material for resume content, subject to final public-content approval.
26. The project will publish project-learning content on Dev.to and Hashnode, as established in the approved project state.
27. The project uses one deployment environment.
28. The existing Azure subscription is the intended subscription; its identifier is not stored in project documentation.

## 4. Assumptions — Not Confirmed Requirements

1. The existing Azure subscription can provision every required service.
2. Required services and relevant free allowances remain available when implementation starts.
3. The required delivery architecture can remain within the eventual numeric cost ceiling.
4. A suitable free hostname/subdomain can satisfy the approved interpretation of the DNS requirement.
5. GitHub Actions can be configured with secure deployment authentication.
6. The supplied CV contains sufficient material for the initial public resume.
7. The public blog platforms can host the required article without introducing product scope or cost changes.
8. Exact resource names, template parameters, API details, and runtime configuration can be selected without changing product behavior.

Assumptions are not acceptance criteria and cannot be treated as confirmed decisions.

## 5. Actors and Permissions

| Actor | Responsibilities / Permissions |
|---|---|
| Public Visitor | Publicly reads the resume, uses the public counter, and follows the project-learning link. No administrative access. |
| Recruiter | Public visitor who evaluates professional background and qualifications. |
| Hiring Manager | Public visitor who evaluates qualifications and engineering evidence. |
| Technical Interviewer | Public visitor who evaluates technical implementation evidence. |
| Project Owner | Owns scope, content approval, costs, repositories, infrastructure changes, and production release decisions. |
| GitHub Actions | Executes approved CI/CD workflows using restricted deployment credentials. |
| Azure Services | Host, deliver, execute, and persist the product's approved behavior. |

Public access does not grant database, infrastructure, repository, or deployment privileges. Browser clients must never receive Cosmos DB credentials or equivalent database access.

## 6. Product Boundaries

### In Scope

- Public resume content.
- HTML, CSS, and JavaScript website.
- Azure Storage static website hosting.
- HTTPS and approved CDN/delivery layer.
- Public hostname/DNS solution.
- Visitor counter and persistent counter state.
- Python Azure Function API.
- Automated Python tests.
- ARM Infrastructure as Code.
- Separate frontend/backend GitHub repositories.
- Backend and frontend GitHub Actions CI/CD.
- Public production deployment.
- Project-learning article(s) required by the approved project state.

### Explicitly Out of Scope

- Authentication and visitor accounts.
- Admin dashboards.
- Public resume editing.
- CMS functionality.
- Contact forms.
- E-commerce and payments.
- Unrelated analytics or personal tracking.
- General-purpose blogging platform functionality.
- Multiple deployment environments.
- Additional cloud providers.
- Frontend frameworks replacing plain HTML/CSS/JavaScript without scope approval.
- Replacing Python/Azure Functions, Cosmos DB Table API, or ARM without scope approval.
- Paid domain purchase unless separately approved.
- AZ-900 as a project requirement.

## 7. MVP Requirements

Each requirement below is independently specified. Acceptance criteria are maintained in `docs/product/ACCEPTANCE-CRITERIA.md` and use verification IDs beginning with `VT-`.

---

## CR-AZ-MVP-001 — Public Resume Content

**Problem / User Story**  
As a recruiter, hiring manager, or technical interviewer, I need a public resume so I can evaluate the Project Owner's professional background and engineering evidence.

**Actors**  
Public Visitor, Recruiter, Hiring Manager, Technical Interviewer, Project Owner.

**Preconditions**  
Approved public resume content exists; the production website is available.

**Trigger**  
A visitor requests the public resume.

**Inputs**  
Owner-approved CV-derived content and explicitly approved additions.

**Business Rules**  
- Public content must be traceable to the supplied CV or an explicitly approved addition.
- Private or rejected information must not be published.
- The project must not falsely claim AZ-900 compliance.
- Final public content requires Project Owner approval.

**Success State**  
The approved resume content is publicly readable.

**Failure States**  
Unavailable site; incomplete content; unapproved/private information exposed; materially incorrect resume information.

**Permissions**  
Public read; Project Owner controls publication content.

**Edge Cases**  
CV changes; disclosure restrictions; long or narrow viewports; missing optional resume information.

**Dependencies**  
MVP-002, MVP-003, MVP-004, MVP-005, MVP-006, OR-005.

**Acceptance Criteria**  
See AC-001; verification VT-001.

**Non-Functional Requirements**  
Publicly readable, mobile/desktop readable, privacy-preserving, content traceable to approved source.

**Out of Scope**  
Accounts, CMS, visitor editing, resume administration.

---

## CR-AZ-MVP-002 — HTML Resume

**Problem / User Story**  
As a technical interviewer, I need the resume implemented as HTML so the project demonstrates direct web fundamentals.

**Actors**  
Public Visitor, Technical Interviewer.

**Preconditions**  
Approved resume content exists.

**Trigger**  
The public page is requested.

**Inputs**  
HTML document and approved resume content.

**Business Rules**  
- Normal resume viewing must use HTML.
- Word/PDF documents must not be required for normal viewing.

**Success State**  
A supported browser renders the resume as an HTML webpage.

**Failure States**  
HTML unavailable, malformed, or dependent on a document viewer.

**Permissions**  
Public read.

**Edge Cases**  
Malformed markup; browser differences; missing optional assets.

**Dependencies**  
MVP-001, MVP-003.

**Acceptance Criteria**  
See AC-002; verification VT-002.

**Non-Functional Requirements**  
Browser-renderable and readable without proprietary document software.

**Out of Scope**  
PDF/Word generation as the primary resume experience.

---

## CR-AZ-MVP-003 — CSS Styling

**Problem / User Story**  
As a visitor, I need intentional styling so the resume is presented as a professional website rather than raw HTML.

**Actors**  
Public Visitor.

**Preconditions**  
HTML resume exists.

**Trigger**  
Resume loads.

**Inputs**  
HTML and CSS assets.

**Business Rules**  
- CSS styling is mandatory.
- The design should remain simple and professional.
- Design complexity is not an MVP goal.

**Success State**  
The resume is intentionally styled and remains readable.

**Failure States**  
Raw/default presentation only; styling makes content unusable; CSS errors materially obstruct access.

**Permissions**  
Public read.

**Edge Cases**  
CSS unavailable; narrow viewport; large text; differing browser rendering.

**Dependencies**  
MVP-002.

**Acceptance Criteria**  
See AC-003; verification VT-003.

**Non-Functional Requirements**  
Readable across common desktop and mobile viewports; graceful degradation when styling fails.

**Out of Scope**  
Frontend frameworks, advanced animation, design systems, or elaborate interaction design.

---

## CR-AZ-MVP-004 — Azure Storage Static Website

**Problem / User Story**  
As the Project Owner, I need Azure Storage hosting so the project demonstrates Azure static website hosting.

**Actors**  
Public Visitor, Project Owner, Azure Services.

**Preconditions**  
Frontend artifacts exist and the approved Azure subscription is available.

**Trigger**  
A production frontend publication occurs.

**Inputs**  
HTML, CSS, JavaScript, and other approved static assets.

**Business Rules**  
- Azure Storage is the primary static website host.
- Production publication must result from the approved source-controlled workflow.

**Success State**  
Required website assets are served through Azure Storage and are available to the approved delivery path.

**Failure States**  
Wrong host; missing assets; partial publication; inaccessible Storage content.

**Permissions**  
Public read; restricted deployment write access.

**Edge Cases**  
Missing file; partial upload; endpoint/service outage.

**Dependencies**  
MVP-002, MVP-003, MVP-005, MVP-014.

**Acceptance Criteria**  
See AC-004; verification VT-004.

**Non-Functional Requirements**  
Repeatable publication, cost-conscious configuration, no public deployment credentials.

**Out of Scope**  
Replacing Azure Storage with a different primary host.

---

## CR-AZ-MVP-005 — HTTPS/CDN Delivery

**Problem / User Story**  
As a visitor, I need secure HTTPS delivery of the public resume.

**Actors**  
Public Visitor, Azure delivery services, Project Owner.

**Preconditions**  
Azure Storage hosting exists; approved delivery configuration exists.

**Trigger**  
A visitor requests the public site.

**Inputs**  
HTTPS request and hostname.

**Business Rules**  
- HTTPS is mandatory.
- CDN/delivery capability is required by the approved project direction.
- The exact service/configuration must satisfy the final approved cost ceiling.
- Current service suitability must be validated before production acceptance.

**Success State**  
The public resume is delivered through HTTPS using the approved delivery path.

**Failure States**  
HTTP-only delivery; certificate failure; invalid hostname configuration; delivery outage; cost outside approved limit.

**Permissions**  
Public read; delivery configuration restricted to authorized project/deployment identities.

**Edge Cases**  
Certificate lifecycle; cache staleness; service/pricing changes; origin failure.

**Dependencies**  
MVP-004, MVP-006, OR-003, OR-004.

**Acceptance Criteria**  
See AC-005; verification VT-005.

**Non-Functional Requirements**  
Secure transport, approved cost compliance, documented delivery configuration.

**Out of Scope**  
Unapproved paid delivery services or architecture substitutions.

---

## CR-AZ-MVP-006 — Public Hostname/DNS

**Problem / User Story**  
As a visitor, I need a stable public hostname so I can access and share the resume.

**Actors**  
Public Visitor, Project Owner, DNS/hostname provider.

**Preconditions**  
Approved delivery endpoint exists.

**Trigger**  
Visitor resolves the public hostname.

**Inputs**  
Public hostname/DNS records.

**Business Rules**  
- A public hostname is required.
- Paid domain purchase is currently excluded.
- The current project direction is a free hostname/subdomain.
- The interpretation of the original custom-domain requirement must be explicitly documented.

**Success State**  
The approved hostname resolves to the intended production delivery endpoint.

**Failure States**  
DNS resolution failure; unavailable hostname; configuration mismatch; unapproved paid-domain dependency.

**Permissions**  
Public DNS resolution; owner controls DNS configuration.

**Edge Cases**  
Propagation delay; provider restrictions; hostname change; certificate/hostname mismatch.

**Dependencies**  
MVP-005, MVP-015, OR-002.

**Acceptance Criteria**  
See AC-006; verification VT-006.

**Non-Functional Requirements**  
Publicly resolvable, stable enough for production use, cost compliant.

**Out of Scope**  
Paid domain purchase unless separately approved.

---

## CR-AZ-MVP-007 — JavaScript Visitor Counter

**Problem / User Story**  
As a public visitor, I want a visitor count so the site demonstrates dynamic client-side behavior.

**Actors**  
Public Visitor, Browser JavaScript.

**Preconditions**  
Website and approved counter API are available.

**Trigger**  
The resume page loads and initializes counter behavior.

**Inputs**  
Counter API request and response.

**Business Rules**  
- JavaScript must retrieve/display the counter through the approved API.
- Browser JavaScript must not access Cosmos DB directly.
- The exact visitor-counting unit must be explicitly defined before final acceptance.

**Success State**  
The approved counter result is displayed when the counter service succeeds.

**Failure States**  
API unavailable; invalid response; persistence failure; counter cannot be displayed.

**Permissions**  
Public invocation only to the extent required by the approved API contract.

**Edge Cases**  
Refreshes; duplicate requests; concurrent requests; timeouts; malformed API response.

**Dependencies**  
MVP-008, MVP-009, MVP-010, OR-001, OR-008, OR-009.

**Acceptance Criteria**  
See AC-007; verification VT-007.

**Non-Functional Requirements**  
Counter failure must not prevent resume reading; no database credentials exposed; semantics must be objectively testable.

**Out of Scope**  
Accounts, demographic tracking, unrelated analytics, or personal tracking.

---

## CR-AZ-MVP-008 — Visitor Counter Persistence

**Problem / User Story**  
As the Project Owner, I need counter state persisted so normal reloads and redeployments do not reset the counter.

**Actors**  
Azure Function, Cosmos DB Table API.

**Preconditions**  
Approved database resource exists; backend has required restricted access.

**Trigger**  
A valid counter operation is processed.

**Inputs**  
Counter state/operation according to the approved semantics and API contract.

**Business Rules**  
- Cosmos DB Table API is the approved persistence technology.
- State must survive normal backend and frontend redeployment.
- Database access is backend-only.

**Success State**  
Persistent counter state is read/updated according to the approved semantics.

**Failure States**  
Database unavailable; write/read failure; invalid state; concurrency conflict not safely handled.

**Permissions**  
Backend identity only; no browser database access.

**Edge Cases**  
First record; missing record; concurrent updates; transient failure; retry/duplicate operation.

**Dependencies**  
MVP-009, MVP-010, OR-001, OR-008.

**Acceptance Criteria**  
See AC-008; verification VT-008.

**Non-Functional Requirements**  
Persistence across normal deployments, controlled failures, least-privileged access.

**Out of Scope**  
General-purpose database functionality or unrelated analytics.

---

## CR-AZ-MVP-009 — Visitor Counter API

**Problem / User Story**  
As the website client, I need an API boundary between browser and database so database credentials and direct database access are not exposed.

**Actors**  
Browser JavaScript, Azure Function, Cosmos DB Table API.

**Preconditions**  
Function and persistence layer exist; API contract is approved.

**Trigger**  
Browser JavaScript sends the counter request.

**Inputs**  
Request defined by the approved API contract.

**Business Rules**  
- The API is the only application boundary between browser and Cosmos DB.
- Request validation and controlled error behavior are required.
- CORS behavior must be explicitly defined.
- Database credentials/secrets must remain server-side.

**Success State**  
A valid request produces the approved counter result.

**Failure States**  
Invalid request; unauthorized database access attempt; database failure; function failure; malformed response.

**Permissions**  
Public API invocation as required by the counter; backend database permissions restricted.

**Edge Cases**  
Malformed payload; unexpected method; repeated requests; origin mismatch; transient database failure.

**Dependencies**  
MVP-008, MVP-010, OR-008, OR-009.

**Acceptance Criteria**  
See AC-009; verification VT-009.

**Non-Functional Requirements**  
No direct browser-to-Cosmos path; controlled errors; no secret disclosure; defined CORS/security behavior.

**Out of Scope**  
Additional APIs unrelated to the visitor counter.

---

## CR-AZ-MVP-010 — Python Azure Function

**Problem / User Story**  
As a technical interviewer, I need the API implemented with Python on Azure Functions so the project demonstrates serverless backend development.

**Actors**  
Azure Function, Project Owner, Technical Interviewer.

**Preconditions**  
Function resource and runtime configuration exist.

**Trigger**  
A valid API request is received.

**Inputs**  
Approved API request and persistence operation.

**Business Rules**  
- Backend API compute uses Azure Functions.
- Application code uses Python.
- Function access to persistence is restricted to required operations.

**Success State**  
The Function handles approved counter requests and returns controlled results.

**Failure States**  
Runtime error; dependency failure; invalid input; unavailable persistence.

**Permissions**  
Function identity receives only required backend permissions.

**Edge Cases**  
Cold start; malformed request; downstream timeout; unexpected exception.

**Dependencies**  
MVP-008, MVP-009, MVP-011, MVP-012.

**Acceptance Criteria**  
See AC-010; verification VT-010.

**Non-Functional Requirements**  
Controlled errors, no secret disclosure, least privilege, repeatable deployment.

**Out of Scope**  
Non-counter APIs and replacement backend platforms.

---

## CR-AZ-MVP-011 — Automated Python Tests

**Problem / User Story**  
As the Project Owner, I need automated backend tests so changes can be validated before deployment.

**Actors**  
Project Owner, GitHub Actions.

**Preconditions**  
Backend test suite exists and CI can execute it.

**Trigger**  
A backend/infrastructure change enters the CI workflow.

**Inputs**  
Source code, test suite, and CI environment.

**Business Rules**  
- Required tests execute automatically.
- A failing required test must block production deployment.
- The test framework is currently deferred as OR-006 and must be selected before final acceptance.

**Success State**  
Tests execute repeatedly and produce a visible pass/fail result; passing required tests permit the deployment stage to proceed.

**Failure States**  
Test failure; test execution failure; missing dependency; CI cannot reproduce test execution.

**Permissions**  
CI test execution does not require production database privileges unless a separately approved test requires them.

**Edge Cases**  
Flaky test; missing dependency; environment-specific failure; deliberately broken behavior.

**Dependencies**  
MVP-010, MVP-013, OR-006.

**Acceptance Criteria**  
See AC-011; verification VT-011.

**Non-Functional Requirements**  
Repeatable, visible, automated, and deployment-gating.

**Out of Scope**  
A specific testing framework until OR-006 is resolved.

---

## CR-AZ-MVP-012 — ARM Infrastructure as Code

**Problem / User Story**  
As a technical interviewer, I need Azure infrastructure represented as code so the environment is reproducible and source controlled.

**Actors**  
Project Owner, GitHub Actions, Azure Resource Manager.

**Preconditions**  
Required Azure resources and their intended configuration are defined.

**Trigger**  
Infrastructure is provisioned or changed through the approved workflow.

**Inputs**  
Source-controlled ARM templates and approved parameters.

**Business Rules**  
- Required project infrastructure must be represented by ARM templates.
- Backend resources follow the approved Consumption-plan direction.
- Normal production provisioning must not depend on undocumented manual configuration.

**Success State**  
Required infrastructure can be provisioned/configured from source-controlled ARM definitions.

**Failure States**  
Missing resource definition; template failure; undocumented manual dependency; configuration outside approved constraints.

**Permissions**  
Deployment identity receives only required resource-management permissions.

**Edge Cases**  
Existing resource state; parameter mismatch; partial deployment; deployment rollback/failure.

**Dependencies**  
MVP-004, MVP-005, MVP-006, MVP-008, MVP-010, MVP-013, OR-003, OR-004.

**Acceptance Criteria**  
See AC-012; verification VT-012.

**Non-Functional Requirements**  
Reproducible, source controlled, reviewable, least privileged, cost compliant.

**Out of Scope**  
Manual-only production infrastructure and non-ARM IaC substitutions.

---

## CR-AZ-MVP-013 — Backend GitHub Repository and CI/CD

**Problem / User Story**  
As the Project Owner, I need backend changes tested and deployed through GitHub Actions so production releases are automated and repeatable.

**Actors**  
Project Owner, GitHub Actions, Azure.

**Preconditions**  
Canonical backend repository exists; secure CI/CD authentication is configured.

**Trigger**  
An approved backend or infrastructure change enters the production workflow.

**Inputs**  
Backend source, tests, ARM templates, workflow configuration, and secure deployment credentials/configuration.

**Business Rules**  
- Canonical backend repository is `s1xte3n/sixteen-resume-backend`.
- `develop` is the integration branch; `main` represents production.
- Tests execute before production deployment.
- A failing required test blocks deployment.
- Secrets are not committed.

**Success State**  
A validated `main` change is deployed through the automated workflow.

**Failure States**  
Test failure; workflow failure; authentication failure; deployment failure; invalid infrastructure.

**Permissions**  
CI/CD uses restricted deployment identities; repository write/merge permissions remain owner-controlled.

**Edge Cases**  
Failed deployment; rerun; concurrent change; stale artifact; revoked credential.

**Dependencies**  
MVP-011, MVP-012, MVP-010, OR-006.

**Acceptance Criteria**  
See AC-013; verification VT-013.

**Non-Functional Requirements**  
Automated, auditable, secure, repeatable, deployment-gating.

**Out of Scope**  
Manual production deployment as the intended release path.

---

## CR-AZ-MVP-014 — Frontend GitHub Repository and CI/CD

**Problem / User Story**  
As the Project Owner, I need frontend changes automatically published so website releases are repeatable.

**Actors**  
Project Owner, GitHub Actions, Azure Storage, approved delivery layer.

**Preconditions**  
Canonical frontend repository exists; secure deployment configuration exists.

**Trigger**  
An approved frontend production change enters the workflow.

**Inputs**  
HTML, CSS, JavaScript, workflow configuration, and secure deployment credentials/configuration.

**Business Rules**  
- Canonical frontend repository is `s1xte3n/sixteen-resume-frontend`.
- `develop` is the integration branch; `main` represents production.
- Successful workflow publication updates Azure Storage.
- Required cache invalidation is handled where the approved delivery architecture requires it.
- Secrets are never committed.

**Success State**  
The production website reflects the approved `main` state after successful publication.

**Failure States**  
Validation failure; upload failure; authentication failure; stale cache; workflow failure.

**Permissions**  
Restricted deployment write access to Azure Storage/delivery resources.

**Edge Cases**  
Partial publication; stale cache; repeated deployment; failed cache purge.

**Dependencies**  
MVP-004, MVP-005, MVP-013, MVP-015, OR-004.

**Acceptance Criteria**  
See AC-014; verification VT-014.

**Non-Functional Requirements**  
Automated, repeatable, secure, observable publication.

**Out of Scope**  
Manual production publication as the intended workflow.

---

## CR-AZ-MVP-015 — Public Production Deployment

**Problem / User Story**  
As a recruiter, hiring manager, or technical interviewer, I need a working public production URL so I can evaluate the resume without local setup.

**Actors**  
Public Visitor, Project Owner, GitHub Actions, Azure services.

**Preconditions**  
All required MVP components have passed their applicable acceptance criteria; final public content is approved; production configuration satisfies the approved cost ceiling.

**Trigger**  
The approved production release is published.

**Inputs**  
Approved `main` state, deployed infrastructure, public hostname, website, API, persistence, and delivery configuration.

**Business Rules**  
- Production corresponds to `main`.
- Public hostname resolves.
- Resume loads over HTTPS.
- Counter follows the approved frontend → API → persistence path.
- No secrets are committed.
- Required infrastructure is source-controlled through IaC.
- Cost must satisfy the approved numeric threshold.

**Success State**  
A public visitor can access the approved resume at the production hostname over HTTPS and the required counter behavior operates according to its approved semantics.

**Failure States**  
DNS failure; HTTPS failure; stale/incorrect content; counter flow failure; deployment mismatch; cost non-compliance; secret exposure.

**Permissions**  
Public read; deployment and infrastructure changes restricted to authorized identities.

**Edge Cases**  
DNS propagation; CDN cache staleness; partial release; backend unavailable; certificate issue.

**Dependencies**  
MVP-001 through MVP-014, MVP-016, OR-001 through OR-005, and any required P2 contract decisions.

**Acceptance Criteria**  
See AC-015; verification VT-015.

**Non-Functional Requirements**  
Secure, publicly reachable, reproducible, cost compliant, and consistent with approved source state.

**Out of Scope**  
Multiple production environments, high-scale availability commitments, or unrelated operational services.

---

## CR-AZ-MVP-016 — Project-Learning Blog Post

**Problem / User Story**  
As a technical interviewer, I need a linked project-learning article so I can understand lessons learned, implementation decisions, and the project journey.

**Actors**  
Recruiter, Hiring Manager, Technical Interviewer, Public Visitor, Project Owner.

**Preconditions**  
The required project-learning article is publicly published; final URL is known.

**Trigger**  
A visitor selects the project-learning link from the resume.

**Inputs**  
Public article URL and article content.

**Business Rules**  
- The resume must contain a working link to project-learning content.
- Approved project state calls for publication on Dev.to and Hashnode.
- Article scope covers technical lessons, implementation, problems, solutions/decisions, and broader project journey.
- A general-purpose blogging application is not part of the product.

**Success State**  
The linked article is publicly reachable and contains project-learning content.

**Failure States**  
Broken link; private article; deleted article; incomplete required content.

**Permissions**  
Public read; Project Owner controls article publication.

**Edge Cases**  
URL changes; one platform unavailable; duplicate publication; article updated after resume publication.

**Dependencies**  
MVP-001, MVP-014, MVP-015; project-state blog decision.

**Acceptance Criteria**  
See AC-016; verification VT-016.

**Non-Functional Requirements**  
Public reachability, stable link at acceptance, content consistent with the project.

**Out of Scope**  
Blog CMS, comments, subscriptions, analytics dashboard, or multiple unrelated articles.

## 8. Cross-Cutting Non-Functional Requirements

### Security

- No Azure credentials or secrets in source control.
- Browser JavaScript must never connect directly to Cosmos DB.
- Deployment identities must use least privilege.
- API errors must not disclose secrets or sensitive infrastructure information.
- Public resume content requires owner approval.

### Cost

- Project direction is R0/free where possible and lowest-cost viable where free service is unavailable.
- A numeric maximum cost is still required before final production acceptance (OR-003).
- Any unavoidable cost requires explicit approval.

### Reliability

- Counter state survives normal frontend and backend redeployments.
- CI/CD failures are observable through workflow results.
- Deployments are repeatable.
- No formal availability SLO is currently committed (OR-011).

### Compatibility

- Resume must render in supported modern browsers.
- Resume must remain readable across common desktop and mobile viewports.
- Exact browser/version baseline remains open (OR-010).

### Performance and caching

- The site should provide normal static-site response behavior appropriate to the selected delivery architecture.
- Exact performance and cache-freshness targets are not currently defined and must not be invented.

### Privacy

- Only approved resume information is public.
- Visitor counter does not authorize unrelated personal tracking.

### Accessibility

- Readability is required, but no formal accessibility target has yet been approved.

## 9. Confirmed Deviations from Original Challenge

### Certification

The original challenge calls for AZ-900 or an advanced Azure certification. The approved project explicitly excludes AZ-900 and uses the existing AI-901 certification as the displayed certification where appropriate. The project must not claim literal AZ-900 compliance unless that certification is subsequently obtained.

### Domain

The original challenge describes a custom DNS domain. The approved project excludes paid domain purchase and currently directs the project toward a free hostname/subdomain. The exact interpretation is still recorded as OR-002 and must be explicitly closed.

## 10. Contradictions and Ambiguities

| ID | Issue | Impact | Status |
|---|---|---|---|
| OR-001 | Visitor unit is undefined. | Counter behavior and tests cannot be final. | Open P1 |
| OR-002 | Original custom-domain wording conflicts with free-hostname direction. | DNS and production acceptance cannot be final. | Open P1 |
| OR-003 | Zero/near-zero has no numeric threshold. | Cost acceptance cannot be objective. | Open P1 |
| OR-004 | Exact current HTTPS/CDN configuration and cost suitability are not validated. | Delivery architecture and acceptance cannot be final. | Open P1 |
| OR-005 | Exact public CV content has not received final owner approval. | Public-content acceptance cannot be final. | Open P1 |
| OR-006 | Python test framework is unspecified. | Test implementation details remain open. | Open P2 |
| OR-007 | Blog platform is inconsistent between product docs and approved project state. | MVP-016 documentation is inconsistent. | Open P2; project state indicates Dev.to + Hashnode |
| OR-008 | Counter API contract is unspecified. | API acceptance cannot be fully concrete. | Open P2 |
| OR-009 | Counter failure UX is unspecified. | Failure-state acceptance is incomplete. | Open P2 |
| OR-010 | Browser baseline is unspecified. | Compatibility testing lacks a fixed matrix. | Open P2 |
| OR-011 | Availability target is unspecified. | No objective uptime acceptance target exists. | Open P2 |
| OR-012 | DNS propagation expectation is unspecified. | DNS deployment acceptance lacks timing boundary. | Open P2 |
| OR-013 | Blog link tab behavior is unspecified. | Minor UX detail is untestable. | Open P3 |

## 11. Missing / Not Objectively Testable Requirements

The following remain intentionally unspecified because the approved sources do not define them:

- Numeric cost ceiling.
- Visitor-count unit.
- Exact API request/response and CORS contract.
- API authentication requirement, if any.
- Counter failure UX.
- Browser/version matrix.
- Formal availability SLO.
- Accessibility target.
- Performance target.
- Cache freshness target.
- DNS propagation/stability target.
- Minimum measurable blog length/content beyond the approved topic scope.
- Exact required resume section list.
- Formal rollback requirement.
- Monitoring/alerting target.

These are tracked in `OPEN-REQUIREMENTS.md`; they are not silently resolved here.

## 12. Requirement Completion / PRD Closure Gate

The PRD is **not closed yet**. The requirements baseline is complete enough to expose the full product boundary, but the closure gate remains blocked until the following are explicitly resolved or formally accepted as documented deviations:

1. Every MVP requirement has testable acceptance criteria and verification IDs.
2. No P0 ambiguity remains.
3. No P1 ambiguity remains hidden.
4. All deliberate deviations from the original challenge are documented.
5. A numeric cost ceiling is defined.
6. Visitor-count semantics are defined.
7. Public hostname interpretation is defined.
8. HTTPS/CDN configuration and cost are validated.
9. Final public resume content is approved.

No implementation task is created by this PRD. Blocking decisions remain product decisions until explicitly closed.
