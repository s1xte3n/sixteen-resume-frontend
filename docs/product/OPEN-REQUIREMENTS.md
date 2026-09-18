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