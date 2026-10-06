# Acceptance Criteria

## 1. Purpose

This document defines objective acceptance criteria and verification IDs for every MVP requirement in `docs/product/PRD.md`.

A checkbox is only considered passed when the stated evidence exists in the final approved configuration. An unresolved P1 decision blocks acceptance of the affected requirement; it is not silently assumed. A resolved capability decision may still have an implementation validation gate.

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

**Acceptance gate:** OR-005 is resolved at the requirements-definition level; final owner approval remains required before production acceptance.

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

**Browser baseline:** latest stable and immediately preceding major release of Chrome, Edge, Firefox, and Safari; viewports 375x667, 390x844, 768x1024, and 1440x900 CSS pixels.

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
- [ ] Current recurring Azure/cloud cost attributable to the MVP is **<= R100/month**.
- [ ] **R0/month** is recorded as the preferred target where viable.
- [ ] The cost calculation excludes personal internet access, existing equipment, optional paid domain registration, and one-time purchases explicitly approved later.
- [ ] No paid domain registration is required for MVP acceptance.
- [ ] Any unexpected Azure/cloud charge identified during validation has been investigated before acceptance continues.
- [ ] A forecast or measured recurring Azure/cloud cost **> R100/month** blocks production acceptance.

**Architecture dependency:** ADR-006 is resolved. Production acceptance additionally requires implementation evidence that the selected edge service satisfies the frozen ADR-006 conditions; OR-003 is resolved.

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

**Blocking dependency:** None for hostname interpretation; final HTTPS/delivery implementation must satisfy the resolved ADR-006 conditions.

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

**Implementation gates:** OR-008 and OR-009 are resolved; implementation must satisfy the approved API contract and counter failure behavior.

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

**Implementation gate:** OR-008 is resolved; implementation must satisfy the approved atomic persistence semantics.

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

**Implementation gates:** OR-008 and OR-009 are resolved; implementation must satisfy the approved API contract and failure behavior.

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

**Implementation gate:** the selected Python test framework must be documented and the CI test stage must execute before deployment.

## AC-012 — ARM Infrastructure as Code

**Requirement:** CR-AZ-MVP-012  
**Verification:** VT-012 — IaC provisioning/source-control test

- [ ] Required project Azure infrastructure is represented by ARM templates.
- [ ] ARM templates are stored in source control.
- [ ] The approved provisioning workflow can apply the required infrastructure from source-controlled definitions.
- [ ] Normal production provisioning does not require undocumented manual configuration.
- [ ] Backend resources use Azure Functions Flex Consumption (FC1), Linux, Functions v4, and Python 3.12.
- [ ] The Function App supports serverless scale-to-zero behavior.
- [ ] The MVP uses zero always-ready instances unless a later approved requirement changes this.
- [ ] Infrastructure changes are represented as source-controlled changes.
- [ ] Deployed configuration remains within the approved cost ceiling.

**Implementation gates:** OR-003 and OR-004 are resolved at the requirements-definition level; final resource selection and delivery validation remain implementation gates.

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

**Implementation/acceptance gates:** secure CI/CD authentication and the selected test framework remain required for final acceptance; the requirement is unblocked for implementation.

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

**Implementation gate:** OR-004 is resolved; final delivery/cache behavior must still be implemented and verified.

## AC-015 — Public Production Deployment

**Requirement:** CR-AZ-MVP-015  
**Verification:** VT-015 — End-to-end production acceptance test

- [ ] The approved public hostname resolves successfully.
- [ ] The resume loads over HTTPS.
- [ ] The public content exactly matches the approved production content.
- [ ] The visitor counter completes the approved frontend → API → persistence flow.
- [ ] Production corresponds to the approved `main` state.
- [ ] The deployed configuration passes the approved **R100/month recurring Azure/cloud cost ceiling**.
- [ ] The cost evidence records R0/month as the preferred target and applies the approved exclusions.
- [ ] Any unexpected Azure/cloud charge has been investigated before acceptance.
- [ ] Repository review confirms no credentials or secrets are committed.
- [ ] Required infrastructure is represented in source-controlled ARM IaC.
- [ ] Required backend and frontend deployment workflows have passed their applicable acceptance tests.

**Acceptance/implementation gates:** OR-004 and OR-005 are resolved at the requirements-definition level; final edge validation, owner content approval, CI/CD implementation, and applicable P2 decisions still require evidence before production acceptance.

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

**Source-of-truth note:** the approved project state specifies Dev.to + Hashnode. External project-learning links open in a new tab/window with `target="_blank"` and `rel="noopener noreferrer"`.

## 3. MVP Acceptance Gate

The MVP cannot be declared fully accepted until:

- [ ] AC-001 through AC-016 all pass.
- [ ] No P0 ambiguity remains.
- [ ] OR-002 is resolved and its deviation from the literal challenge wording is documented.
- [ ] OR-003 through OR-005 are resolved at the requirements-definition level.
- [ ] All deliberate deviations from the original challenge are documented.
- [ ] The numeric cost ceiling is defined and verified.
- [ ] Visitor-count semantics are verified against the resolved OR-001 definition.
- [ ] Public hostname interpretation is defined as a FreeDNS hosted hostname/subdomain and verified in production.
- [ ] HTTPS/CDN configuration and cost are validated.
- [ ] Final public resume content is approved.
- [ ] Browser, availability, DNS, and blog-link baselines are explicitly defined.
- [ ] No hidden P1 ambiguity remains.


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
