# Acceptance Criteria

## 1. Purpose

This document defines objective acceptance criteria and verification IDs for every MVP requirement in `docs/product/PRD.md`.

A checkbox is only considered passed when the stated evidence exists in the final approved configuration. An unresolved P1 decision blocks acceptance of the affected requirement; it is not silently assumed.

## 2. Global Acceptance Conditions

- Production is the state represented by `main`.
- Final public resume content must be explicitly approved by the Project Owner.
- No credentials, secrets, tokens, connection strings, or equivalent sensitive deployment material may be committed to source control.
- Acceptance uses the final approved configuration and public delivery path.
- Browser-to-Cosmos DB direct access must not exist.
- A requirement with an unresolved high-impact dependency cannot be marked fully accepted.

---

## AC-001 — Public Resume Content

**Requirement:** CR-AZ-MVP-001  
**Verification:** VT-001 — Public content review

- [ ] The approved public resume URL opens successfully.
- [ ] The page displays the exact owner-approved resume content.
- [ ] Every material resume section is traceable to the supplied CV or an explicitly approved addition.
- [ ] Private/rejected information identified during content review is absent from production.
- [ ] The resume does not falsely represent AZ-900 as held or as a project requirement.
- [ ] Owner approval is recorded before production acceptance.

**Blocking dependency:** OR-005.

## AC-002 — HTML Resume

**Requirement:** CR-AZ-MVP-002  
**Verification:** VT-002 — HTML delivery/rendering test

- [ ] The public resume is delivered as an HTML webpage.
- [ ] A supported modern browser renders the core resume without requiring a Word/PDF viewer.
- [ ] Core resume content exists in HTML rather than only as a downloadable document.
- [ ] Normal resume viewing does not depend on PDF or Word generation.

## AC-003 — CSS Styling

**Requirement:** CR-AZ-MVP-003  
**Verification:** VT-003 — Responsive/style test

- [ ] The resume has intentional CSS styling beyond browser-default raw HTML presentation.
- [ ] Core content remains readable at the approved mobile viewport baseline.
- [ ] Core content remains readable at the approved desktop viewport baseline.
- [ ] CSS failure does not make the underlying resume content inaccessible.
- [ ] No unapproved frontend framework is required for the MVP styling.

**Blocking dependency:** OR-010 for the final browser/viewport baseline.

## AC-004 — Azure Storage Static Website

**Requirement:** CR-AZ-MVP-004  
**Verification:** VT-004 — Hosting/source verification

- [ ] Production static website hosting uses Azure Storage.
- [ ] The production HTML is served through the Azure Storage-backed delivery path.
- [ ] CSS assets load successfully.
- [ ] JavaScript assets load successfully.
- [ ] A successful frontend publication produces the expected website content.
- [ ] The primary hosting requirement is not satisfied solely by a third-party static host.

## AC-005 — HTTPS/CDN Delivery

**Requirement:** CR-AZ-MVP-005  
**Verification:** VT-005 — HTTPS/delivery/cost validation

- [ ] The approved public hostname serves the resume over HTTPS.
- [ ] The final production path contains the approved CDN/delivery layer.
- [ ] Certificate handling is operational for the public hostname.
- [ ] HTTP-to-HTTPS behavior, if used, is documented and verified.
- [ ] The actual deployed configuration matches the approved architecture.
- [ ] Current service cost is within the approved numeric cost ceiling.

**Blocking dependency:** None. Final verification must confirm the deployed configuration remains within the US$5/month ceiling and matches ADR-006.

## AC-006 — Public Hostname/DNS

**Requirement:** CR-AZ-MVP-006  
**Verification:** VT-006 — DNS/hostname resolution test

- [ ] The approved public hostname resolves successfully from an external network.
- [ ] DNS resolves to the intended production delivery endpoint.
- [ ] The resume loads through the approved hostname.
- [ ] The hostname does not require an unapproved paid domain purchase.
- [ ] The project-owner interpretation is recorded as: **Public hostname: FreeDNS hosted hostname/subdomain**.
- [ ] The documentation explicitly states that this is not ownership of a conventional registrable custom domain.
- [ ] The implementation does not require paid domain registration.

**Blocking dependency:** None for the resolved hostname interpretation. Final acceptance verifies FreeDNS/Cloudflare/Azure Storage hostname compatibility.

## AC-007 — JavaScript Visitor Counter

**Requirement:** CR-AZ-MVP-007  
**Verification:** VT-007 — Counter browser-flow test

- [ ] On a healthy counter service, JavaScript initiates the approved counter operation.
- [ ] The browser receives the approved counter result through the API.
- [ ] Browser network inspection confirms no direct Cosmos DB request occurs.
- [ ] The displayed value follows the approved semantics: one successfully committed counter operation per top-level resume page load.
- [ ] A normal reload produces exactly one additional counter operation and the displayed result reflects the committed persisted state.
- [ ] Refreshing the page is treated as a new counter operation.
- [ ] The implementation does not use cookies, authentication, fingerprinting, IP tracking, or user identification to determine whether to count the operation.
- [ ] Counter/API failure does not prevent the visitor from reading the resume.
- [ ] Failure behavior matches the approved counter failure UX once OR-009 is resolved.

**Blocking dependencies:** OR-008, OR-009.

## AC-008 — Visitor Counter Persistence

**Requirement:** CR-AZ-MVP-008  
**Verification:** VT-008 — Persistence/state test

- [ ] A valid initial counter operation creates or initializes persistent state according to the approved model.
- [ ] A subsequent valid operation produces the expected state transition according to the approved counting semantics.
- [ ] Counter state survives a normal backend redeployment.
- [ ] Counter state survives a normal frontend redeployment.
- [ ] Browser inspection shows no direct database access.
- [ ] Database failure produces the approved controlled failure state and does not increment persisted state.
- [ ] Concurrent successful operations do not overwrite one another.
- [ ] If the persisted value is N, then K successfully committed operations result in N + K.
- [ ] Failed API/database operations do not change the persisted count.
- [ ] Conditional update conflicts are retried safely or otherwise resolved without lost increments.

**Blocking dependency:** OR-008.

## AC-009 — Visitor Counter API

**Requirement:** CR-AZ-MVP-009  
**Verification:** VT-009 — API contract/security test

- [ ] A valid frontend request reaches the approved API endpoint.
- [ ] The endpoint uses the approved HTTP method and request contract.
- [ ] A valid request returns the approved success response and status behavior.
- [ ] Invalid requests return the approved controlled error and status behavior.
- [ ] Database failure returns the approved controlled API failure and does not increment persisted state.
- [ ] CORS behavior matches the approved contract.
- [ ] Database credentials/secrets are not returned to the browser.
- [ ] Browser requests do not directly target Cosmos DB.

**Blocking dependencies:** OR-008 and OR-009.

## AC-010 — Python Azure Function

**Requirement:** CR-AZ-MVP-010  
**Verification:** VT-010 — Function/runtime/security test

- [ ] Approved counter API handling executes in Azure Functions.
- [ ] Backend application code is Python.
- [ ] The Function can perform the required persistence operation through its backend access path.
- [ ] Function access is limited to required operations.
- [ ] Runtime and downstream failures return controlled responses.
- [ ] Error responses do not disclose secrets or sensitive infrastructure information.

## AC-011 — Automated Python Tests

**Requirement:** CR-AZ-MVP-011  
**Verification:** VT-011 — CI test-gate test

- [ ] The backend CI workflow automatically executes the required Python test suite.
- [ ] A deliberately broken required behavior causes the required test stage to fail.
- [ ] Passing tests produce a visible successful result.
- [ ] Test results are visible in the CI workflow.
- [ ] Tests can execute repeatedly in the CI environment.
- [ ] The selected testing framework is documented before final acceptance.

**Blocking dependency:** OR-006.

## AC-012 — ARM Infrastructure as Code

**Requirement:** CR-AZ-MVP-012  
**Verification:** VT-012 — IaC provisioning/source-control test

- [ ] Required project Azure infrastructure is represented by ARM templates.
- [ ] ARM templates are stored in source control.
- [ ] The approved provisioning workflow can apply the required infrastructure from source-controlled definitions.
- [ ] Normal production provisioning does not require undocumented manual configuration.
- [ ] Backend resources use the approved Consumption-plan direction.
- [ ] Infrastructure changes are represented as source-controlled changes.
- [ ] Deployed configuration remains within the approved cost ceiling.

**Blocking dependency:** None. Final verification must confirm the selected resources remain within the approved US$5/month recurring cloud/service ceiling.

## AC-013 — Backend GitHub Repository and CI/CD

**Requirement:** CR-AZ-MVP-013  
**Verification:** VT-013 — Backend CI/CD integration test

- [ ] The canonical backend repository is `s1xte3n/sixteen-resume-backend`.
- [ ] The intended integration workflow uses `develop` and production is represented by `main`.
- [ ] An approved backend/infrastructure change entering the production workflow triggers the intended CI/CD process.
- [ ] Required tests execute before production deployment.
- [ ] A failing required test prevents production deployment.
- [ ] Passing required tests allow deployment to proceed when deployment prerequisites are valid.
- [ ] Deployment failures are reported by the workflow.
- [ ] No Azure credentials or secrets are committed.
- [ ] Production deployment represents the approved `main` state.

**Blocking dependencies:** OR-006 and secure CI/CD authentication configuration.

## AC-014 — Frontend GitHub Repository and CI/CD

**Requirement:** CR-AZ-MVP-014  
**Verification:** VT-014 — Frontend publication integration test

- [ ] The canonical frontend repository is `s1xte3n/sixteen-resume-frontend`.
- [ ] The intended integration workflow uses `develop` and production is represented by `main`.
- [ ] An approved frontend production change triggers the intended workflow.
- [ ] Frontend files are automatically published to Azure Storage.
- [ ] Publication failure causes the workflow to report failure.
- [ ] Required delivery-layer cache invalidation is handled where the final architecture requires it.
- [ ] No Azure credentials or secrets are committed.
- [ ] Production publication represents the approved `main` state.

**Blocking dependency:** None for architecture selection; implementation must handle Cloudflare cache behavior as specified by ADR-006.

## AC-015 — Public Production Deployment

**Requirement:** CR-AZ-MVP-015  
**Verification:** VT-015 — End-to-end production acceptance test

- [ ] The approved public hostname resolves successfully.
- [ ] The resume loads over HTTPS.
- [ ] The public content exactly matches the approved production content.
- [ ] The visitor counter completes the approved frontend → API → persistence flow.
- [ ] Production corresponds to the approved `main` state.
- [ ] The deployed configuration passes the approved numeric cost threshold.
- [ ] Repository review confirms no credentials or secrets are committed.
- [ ] Required infrastructure is represented in source-controlled ARM IaC.
- [ ] Required backend and frontend deployment workflows have passed their applicable acceptance tests.

**Blocking dependencies:** OR-005, plus affected P2 API/test decisions.

## AC-016 — Project-Learning Blog Post

**Requirement:** CR-AZ-MVP-016  
**Verification:** VT-016 — Public article/link test

- [ ] The resume contains the approved project-learning article link(s).
- [ ] Each required link opens from an external browser session.
- [ ] The article is publicly reachable.
- [ ] The article covers technical lessons learned, implementation, problems encountered, solutions/decisions, and the broader project journey.
- [ ] Final article URL(s) are recorded in project documentation.
- [ ] Final publishing platform(s) are documented.
- [ ] No general-purpose blog application is introduced into the product.

**Source-of-truth note:** the approved project state specifies Dev.to and Hashnode; older product documentation marked the platform undecided. This inconsistency must be normalized in `OPEN-REQUIREMENTS.md`/project documentation before final acceptance.

## 3. MVP Acceptance Gate

The MVP cannot be declared fully accepted until:

- [ ] AC-001 through AC-016 all pass.
- [ ] No P0 ambiguity remains.
- [ ] OR-002 is resolved and its deviation from the literal challenge wording is documented.
- [ ] OR-001 through OR-004 are resolved and their implementation verification conditions pass.
- [ ] OR-005 is resolved before full MVP acceptance.
- [ ] All deliberate deviations from the original challenge are documented.
- [ ] The numeric cost ceiling is defined and verified.
- [ ] Visitor-count semantics are verified against the resolved OR-001 definition.
- [ ] Public hostname interpretation is defined as a FreeDNS hosted hostname/subdomain and verified in production.
- [ ] HTTPS/CDN configuration and cost are validated.
- [ ] Final public resume content is approved.
- [ ] No hidden P1 ambiguity remains.
