# Open Requirements

## 1. Purpose

This document is the authoritative product-level register of unresolved decisions, ambiguities, contradictions, hidden dependencies, missing requirements, and requirements that are not yet objectively testable.

No ambiguity listed here may be silently resolved during implementation.

## 2. Priority Definitions

| Priority | Meaning |
|---|---|
| P0 | Critical; blocks safe or product-valid progress. |
| P1 | High impact; must be resolved before affected MVP acceptance. |
| P2 | Important; may be resolved during implementation if it does not block acceptance. |
| P3 | Minor refinement. |

## 3. P1 Open Decisions

| ID | Decision / ambiguity | Affected requirements | Status |
|---|---|---|---|
| OR-002 | FreeDNS/afraid.org hosted hostname/subdomain is accepted for the MVP as the project's scoped DNS/public-hostname interpretation, with an explicit deviation from the challenge's conventional custom-domain wording. | MVP-006, MVP-015 | Resolved |

| OR-003 | Define the numeric maximum acceptable project cost. | MVP-005, MVP-006, MVP-012, MVP-015 | Open |
| OR-004 | Validate the exact HTTPS/CDN delivery configuration and current cost suitability. | MVP-005, MVP-015 | Open |
| OR-005 | Approve the exact public resume content derived from the supplied CV. | MVP-001, MVP-015 | Open |

### OR-001 — Visitor Definition

**Decision:** A visitor is one successfully committed visitor-counter operation initiated by a top-level resume page load.

**Counting semantics:**
- The frontend performs exactly one counter request per top-level resume page load.
- A browser refresh is a new page load and therefore counts as another visitor-counter operation.
- The counter does not identify or attempt to distinguish unique humans, browsers, sessions, IP addresses, devices, or users.
- Every successfully committed counter operation increments the persisted total by exactly one.
- A failed API operation or failed database operation does not increment the persisted total.
- Duplicate HTTP requests are separate counter operations unless a future requirement explicitly introduces idempotency semantics.

**Concurrency rule:** The backend must perform a concurrency-safe atomic logical increment. Concurrent successful operations must not overwrite one another. The implementation should use conditional entity updates/ETags with retry-on-conflict behavior so each successfully committed operation contributes exactly one increment.

**Acceptance invariant:** If the persisted count is N before K successfully committed counter operations, the resulting persisted count is N + K.

**Privacy rationale:** This definition is deterministic and avoids cookies, authentication, fingerprinting, IP tracking, or other identity-based visitor tracking.

**Affected:** MVP-007, MVP-008, MVP-009.

**Status:** Resolved.

### OR-002 — Free Hostname vs Custom Domain

**Decision:** Accept the selected FreeDNS/afraid.org hosted hostname/subdomain for the MVP as the project's scoped public-hostname/DNS interpretation.

**Original challenge requirement:** The challenge describes pointing a custom DNS domain to the CDN endpoint.

**Project constraint:** The MVP must not require paid domain registration.

**Deviation:** The MVP does **not** claim ownership of a conventional registrable custom domain. Documentation must use the term **public hostname: FreeDNS hosted hostname/subdomain**.

**Production acceptance rule:**
- The approved FreeDNS hostname resolves publicly.
- The hostname resolves to the approved Azure delivery endpoint.
- The resume is served through that hostname.
- The hostname supports HTTPS through the approved delivery architecture.
- No paid domain registration is required.
- The project documentation explicitly records this as a scoped deviation from the literal custom-domain wording.

**Status:** Resolved.

### OR-003 — Numeric Cost Ceiling

**Question:** What exact maximum project cost is acceptable?

The current direction is R0/free where possible and the lowest-cost viable option otherwise, but this is not objectively testable without a numeric threshold.

**Decision required:** Define a maximum such as `$0`, `$X/month`, `$X/year`, or another explicit measurable limit, and state whether one-time costs are included.

**Affected:** MVP-005, MVP-006, MVP-012, MVP-015.

**Status:** Open.

### OR-004 — HTTPS/CDN Configuration

**Question:** Which current Azure delivery configuration satisfies Azure Storage hosting, HTTPS, CDN/delivery capability, public hostname requirements, and the approved cost ceiling?

**Why it matters:** The selected service/configuration determines architecture, pricing, DNS, certificate handling, caching, and acceptance evidence.

**Decision required:** Validate the exact production delivery configuration and record the applicable cost assumptions.

**Affected:** MVP-005, MVP-015.

**Status:** Open.

### OR-005 — Public Resume Content

**Question:** Which exact CV-derived information is approved for public publication?

**Decision review must cover:**
- Personal information.
- Contact information.
- Professional history.
- Skills.
- Certifications.
- Education.
- Projects.
- External links.
- Any other identifying information.

**Why it matters:** A supplied CV is source material, not automatic authorization to publish every field publicly.

**Affected:** MVP-001, MVP-015.

**Status:** Open pending Project Owner approval.

## 4. P2 Open Requirements

| ID | Requirement / ambiguity | Affected requirements | Status |
|---|---|---|---|
| OR-006 | Select Python testing framework. | MVP-011, MVP-013 | Intentionally deferred until test implementation is prepared. |
| OR-007 | Normalize the blog platform requirement across product/project documents. Approved project state says Dev.to + Hashnode; older product docs said undecided. | MVP-016 | Open documentation inconsistency. |
| OR-008 | Define visitor-counter API method, endpoint purpose, request/response, status codes, error contract, semantics, and CORS. | MVP-009, MVP-010 | Open |
| OR-009 | Define user-visible behavior when counter API/database fails. | MVP-007, MVP-009 | Open |
| OR-010 | Define supported browser/version and viewport baseline. | MVP-001, MVP-003, MVP-015 | Open |
| OR-011 | Define whether a formal production availability/SLO target is required. | MVP-015 | Open |
| OR-012 | Define DNS propagation/stability expectation for acceptance. | MVP-006, MVP-015 | Open |

### OR-006 — Python Testing Framework

The approved requirement requires automated Python tests but does not select a framework. The choice remains intentionally deferred. Final acceptance requires a documented framework and repeatable CI execution.

### OR-007 — Blog Platform Normalization

The approved project state specifies both Dev.to and Hashnode and describes the content scope as technical lessons, implementation, problems, solutions/decisions, and the broader project journey. Earlier product documentation treated the platform as undecided. The approved project-state decision must be reflected consistently in product documentation before final acceptance.

### OR-008 — Visitor API Contract

The final contract must define at minimum:

- HTTP method(s).
- Endpoint purpose/path.
- Request inputs and required/optional fields.
- Successful response schema.
- Error response schema.
- HTTP status behavior.
- Counter semantics.
- CORS behavior.

This is not silently specified here because the approved sources do not provide the final contract.

### OR-009 — Counter Failure UX

Possible behaviors already identified are hiding the counter, displaying an unavailable state, displaying a last-known value, or another approved fallback. No option is selected.

The chosen behavior must not prevent access to the resume.

### OR-010 — Browser Support

The requirements say supported modern browsers/common desktop and mobile viewports but do not provide a version matrix. A final compatibility test baseline is required before objective acceptance.

### OR-011 — Availability Target

No formal availability SLO is currently approved. The product must not claim an uptime target that is not defined by the project.

### OR-012 — DNS Propagation

DNS acceptance needs a defined expectation for propagation/stability if timing is to be tested objectively.

## 5. P3 Open Requirements

### OR-013 — Blog Link Behavior

The project has not specified whether the project-learning link opens in the same tab or a new tab. This is a minor UX detail and does not block requirements closure unless explicitly promoted.

## 6. Contradictions

### IC-001 — Custom Domain vs Free Hostname

The original challenge describes a custom DNS domain. The approved project excludes paid domain purchase and currently selects FreeDNS/afraid.org as the DNS direction. This is a genuine interpretation conflict and is tracked as OR-002.

### IC-002 — AZ-900

The original challenge specifies AZ-900 or an advanced Azure certification. The approved project explicitly excludes AZ-900 and documents AI-901 as the existing certification. This is a deliberate project deviation, not an unresolved ambiguity.

### IC-003 — CDN/HTTPS vs Zero/Near-Zero Cost

HTTPS/CDN delivery is required while the project targets R0/free where possible and lowest-cost viable otherwise. The absence of a numeric ceiling and validated current configuration makes this an open P1 decision (OR-003/OR-004).

### IC-004 — Blog Platform Documentation

Approved project-state documentation specifies Dev.to + Hashnode, while older product documentation marked the platform undecided. The approved project-state decision should be treated as the current direction, but the documents must be normalized before final acceptance.

### IC-005 — Repository Naming in Historical Documentation

Older product artifacts used `sixteen-frontend` and `sixteen-backend`; the approved repository names are `sixteen-resume-frontend` and `sixteen-resume-backend`. The PRD and acceptance criteria now use the approved names. Other project artifacts must be synchronized as part of requirements/documentation governance.

## 7. Hidden Dependencies

1. The Azure subscription must support the required resources.
2. Required Azure services must remain available and suitable.
3. Service pricing must remain within the approved numeric cost ceiling once defined.
4. The selected FreeDNS hostname/subdomain must be provisioned and satisfy the OR-002 production acceptance rule.
5. DNS configuration must support the final delivery architecture.
6. The final delivery configuration must support the selected hostname and HTTPS certificate behavior.
7. GitHub Actions must support secure deployment authentication.
8. Final public resume content requires owner approval.
9. The public article must remain reachable at final acceptance.
10. The backend API must implement the final counter contract consumed by the frontend.
11. Counter semantics determine persistence and concurrency test behavior.
12. The selected test framework determines CI test execution details.

## 8. Missing Requirements

The approved sources do not objectively define:

- Numeric cost ceiling and treatment of one-time versus recurring cost.
- Visitor-count semantics.
- Exact API request/response contract.
- API authentication requirements, if any.
- Exact CORS policy.
- Counter failure UX.
- Browser/version matrix.
- Accessibility target.
- Performance target.
- Cache freshness target.
- Availability/SLO target.
- DNS propagation expectation.
- Minimum measurable article length/content beyond the approved topics.
- Exact required resume section list.
- Formal rollback requirement.
- Monitoring/alerting target.

These omissions are recorded rather than invented.

## 9. Requirements That Are Not Yet Objectively Testable

| ID | Requirement | Why not objectively testable yet |
|---|---|---|
| NTR-001 | Zero/near-zero cost | No numeric ceiling. |
| NTR-002 | Visitor count | Counting unit undefined. |
| NTR-003 | Public hostname | Final hostname is not yet provisioned; the interpretation is resolved under OR-002. |
| NTR-004 | HTTPS/CDN | Exact service/configuration and cost not validated. |
| NTR-005 | Readable resume | No formal accessibility/readability baseline. |
| NTR-006 | Short project-learning article | No measurable length/content minimum beyond topics. |
| NTR-007 | Supported modern browsers | No version matrix. |
| NTR-008 | Production availability | No SLO/target. |
| NTR-009 | DNS stability | No propagation/stability threshold. |

## 10. Requirements Closure Rule

The PRD phase is closed only when:

1. Every MVP feature has testable acceptance criteria and a verification ID.
2. No P0 ambiguity remains.
3. No P1 ambiguity remains hidden.
4. All deliberate deviations from the original challenge are documented.
5. The numeric cost constraint is defined.
6. Public hostname interpretation is defined.
8. HTTPS/CDN configuration is validated.
9. Final public resume content is approved.
10. Product and project documents use the canonical repository names and agree on the approved blog-platform direction.

**Current status: NOT CLOSED.** OR-001 and OR-002 are resolved. OR-003 through OR-005 remain P1 closure blockers.
