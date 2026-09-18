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