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

| OR-003 | Numeric MVP recurring Azure/cloud cost ceiling is fixed at R100/month, with R0/month preferred and explicit exclusions. | MVP-005, MVP-006, MVP-012, MVP-015 | Resolved |
| OR-004 | Freeze the HTTPS/CDN architecture at capability level; exact edge service remains an implementation choice subject to fixed acceptance conditions. | MVP-005, MVP-015 | Resolved |
| OR-005 | Approve the public resume content policy and editorial positioning derived from the supplied CV. | MVP-001, MVP-015 | Resolved |

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

**Decision:** The MVP hard ceiling is **R100/month recurring Azure/cloud cost**, with **R0/month** as the preferred target.

**Cost policy:**
- **R0/month:** Preferred where viable.
- **R0–R100/month recurring:** Allowed.
- **>R100/month recurring:** Blocked.
- The ceiling applies to recurring Azure/cloud costs attributable to the project.
- The ceiling excludes personal internet access, existing equipment, optional paid domain registration, and one-time purchases explicitly approved later.
- Paid domain registration is out of MVP.
- Any unexpected Azure/cloud charge must be investigated before project work continues.
- Cost acceptance must use current billing/pricing evidence and verify the deployed configuration remains within the ceiling.

**Acceptance invariant:** The measured recurring Azure/cloud cost attributable to the MVP must be <= R100/month for production acceptance. A forecast or estimate above R100/month blocks production. An unexpected charge triggers investigation before continuing project work.

**Affected:** MVP-005, MVP-006, MVP-012, MVP-015.

**Status:** Resolved.

### OR-004 — HTTPS/CDN Configuration

**Decision:** Resolve OR-004 by freezing the HTTPS/CDN architecture at capability level while deliberately leaving the exact Azure edge service as an implementation choice.

Required architecture:

```text
Browser
   |
   | HTTPS
   v
Public Hostname
   |
   v
Azure CDN / approved Azure edge-delivery service
   |
   v
Azure Storage Static Website
```

The selected implementation must satisfy all of these acceptance conditions:

- HTTPS is supported.
- Certificate management is supported.
- The public hostname can resolve to the edge endpoint.
- Azure Storage remains the origin.
- Configuration can be represented in IaC where applicable.
- Recurring Azure/cloud cost remains <= R100/month for the complete MVP.
- The service is available and suitable for the required deployment architecture.

The exact Azure service/SKU is therefore not architecture-locked. It is selected during implementation validation against these frozen conditions.

**Status:** Resolved.

**Required delivery capability:**
- Azure-managed HTTPS/CDN delivery in front of Azure Storage static website hosting.
- Public delivery through the approved FreeDNS hostname/subdomain.
- HTTPS with appropriate certificate management.
- Required CDN/edge delivery behavior.
- Source-controlled/IaC representation where supported.
- Total recurring Azure/cloud cost within the **R100/month** ceiling.

**Important status rule:** Azure Front Door Standard is a **candidate only**, not an approved implementation decision. Existing ADR-006 and infrastructure documentation must not describe Front Door Standard as selected, approved, architecture-locked, or deployed.

**Validation evidence must establish:**
1. Current service availability/lifecycle.
2. HTTPS and certificate support.
3. FreeDNS hostname compatibility.
4. Azure Storage static website origin compatibility.
5. Required CDN/edge behavior.
6. ARM/IaC support.
7. Current pricing and projected billing for the complete MVP.
8. Compliance with the R100/month ceiling.

**Affected:** MVP-005, MVP-015.

### OR-005 — Public Resume Content

**Decision:** The public resume will contain only:
- Professionally relevant information derived from the supplied CV.
- Explicitly approved project information.
- Explicitly approved links/contact information.
- No private information that is not intended for public publication.

**Approved positioning:**
- The resume may state **4+ years of hands-on software development experience**.
- Professional employment is separately identified as **IT Operator — Gijima Holdings | June 2022–Present**.
- The resume must not imply that the full four-plus-year period represents professional software-engineering employment.

**Approved certification display:**
- **Microsoft Certified: Azure AI Fundamentals (AI-901)**.
- The resume must not represent AI-901 as AZ-900.
- AZ-900 remains a documented deviation from the original challenge requirement.

**Acceptance rule:** OR-005 is resolved as a content-authorization decision. Final production acceptance still requires the owner to explicitly approve the final public HTML resume content and verify that the published content conforms to this decision.

**Affected:** MVP-001, MVP-015.

**Status:** Resolved.

## 4. P2 Requirements

| ID | Requirement / ambiguity | Affected requirements | Status |
|---|---|---|---|
| OR-006 | Define the backend/API contract for the visitor counter. | MVP-009, MVP-010 | Resolved |
| OR-007 | Define persistence behavior for the single logical visitor counter, including concurrency-safe increment semantics. | MVP-008, MVP-009 | Resolved |
| OR-008 | Define GitHub Actions as the CI/CD deployment authority and required backend/frontend pipeline gates. | MVP-013, MVP-014 | Resolved |
| OR-009 | Define the production release workflow and branch authority: feature/* → PR → CI → develop → production release → main. | MVP-013, MVP-014, MVP-015 | Resolved |
| OR-010 | Define supported browser/version and viewport baseline. | MVP-001, MVP-003, MVP-015 | Resolved |
| OR-011 | Define whether a formal production availability/SLO target is required. | MVP-015 | Resolved |
| OR-012 | Define DNS propagation/stability expectation for acceptance. | MVP-006, MVP-015 | Resolved |

### OR-006 — Backend/API Contract

**Decision:** The visitor API has exactly one MVP responsibility: `GET /api/visitors`.

The successful response contains the current visitor count.

The browser has no Cosmos DB credentials and no direct Cosmos DB access. Azure Functions remains the backend/API boundary.

**Status:** Resolved.

### OR-007 — Persistence Behavior

**Decision:** Use one logical visitor-counter record.

For each successful counter operation, the backend:

```
read current count
→ atomically increment
→ persist
→ return resulting count
```

The implementation must protect against concurrent lost updates. The persisted result must therefore reflect every successfully committed increment.

**Status:** Resolved.

### OR-008 — CI/CD Deployment Authority

**Decision:** GitHub Actions is the deployment mechanism. A production deployment performed directly from a developer laptop is not a valid production release.

**Backend pipeline:**

```
checkout
→ install dependencies
→ run tests
→ validate infrastructure
→ deploy
```

**Frontend pipeline:**

```
checkout
→ validate website
→ publish to Azure Storage
→ purge/invalidate edge cache when required
```

**Status:** Resolved.

### OR-009 — Production Release

**Decision:** `main` represents production.

The intended workflow is:

```
feature/*
    ↓
Pull Request
    ↓
CI
    ↓
develop
    ↓
production release
    ↓
main
```

The project repository workflow is therefore feature branches into `develop`, followed by the production release into `main`.

**Status:** Resolved.

### OR-010 — Browser Support

**Decision:** The MVP browser baseline is the latest stable release and immediately preceding major release of Chrome, Edge, Firefox, and Safari available at test execution. Viewports: 375x667, 390x844, 768x1024, and 1440x900 CSS pixels.

**Status:** Resolved.

### OR-011 — Availability Target

**Decision:** No formal production uptime SLO is part of the MVP. The project must not publish an uptime claim; acceptance uses the defined functional, security, deployment, DNS, HTTPS, and cost criteria.

**Status:** Resolved.

### OR-012 — DNS Propagation

**Decision:** A DNS change is accepted when the authoritative FreeDNS nameserver returns the intended record and independent public recursive resolvers return the intended record within the provider's documented default TTL window of 1 hour. Validation records resolver evidence. FreeDNS documents a default 3600-second TTL and cache expiry behavior.

**Status:** Resolved.

## 5. P3 Requirements

### OR-013 — Blog Link Behavior

**Decision:** Project-learning links open in a new browser tab/window using `target="_blank"` with `rel="noopener noreferrer"`.

**Status:** Resolved.

## 6. Contradictions

### IC-001 — Custom Domain vs Free Hostname

The original challenge describes a custom DNS domain. The approved project excludes paid domain purchase and selects FreeDNS/afraid.org as the DNS direction. This is a deliberate scoped deviation tracked by OR-002.

### IC-002 — AZ-900

The original challenge specifies AZ-900 or an advanced Azure certification. The approved project explicitly excludes AZ-900 and documents AI-901 as the existing certification. This is a deliberate project deviation, not an unresolved ambiguity.

### IC-003 — CDN/HTTPS vs Zero/Near-Zero Cost

HTTPS/CDN delivery is required while the project targets R0/free where possible and lowest-cost viable otherwise. The numeric ceiling is resolved at R100/month; the exact edge service remains an implementation selection governed by the resolved OR-004 acceptance conditions.

### IC-004 — Blog Platform Documentation

Approved project-state documentation specifies Dev.to + Hashnode, while older product documentation marked the platform undecided. The approved project-state decision should be treated as the current direction, but the documents must be normalized before final acceptance.

### IC-005 — Repository Naming in Historical Documentation

Older product artifacts used `sixteen-frontend` and `sixteen-backend`; the approved repository names are `sixteen-resume-frontend` and `sixteen-resume-backend`. The PRD and acceptance criteria now use the approved names. Other project artifacts must be synchronized as part of requirements/documentation governance.

## 7. Hidden Dependencies

1. The Azure subscription must support the required resources.
2. Required Azure services must remain available and suitable.
3. Service pricing must remain within the approved R100/month recurring Azure/cloud cost ceiling.
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
| NTR-002 | Visitor count | Counting semantics are resolved; final API/implementation evidence remains required. |
| NTR-003 | Public hostname | Final hostname is not yet provisioned; the interpretation is resolved under OR-002. |
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
5. The numeric cost constraint is defined as R100/month recurring, with R0/month preferred and explicit exclusions.
6. Public hostname interpretation is defined.
7. HTTPS/CDN capability architecture is resolved and the selected implementation is validated against its fixed acceptance conditions.
8. The public resume content policy and editorial positioning are approved, and the final public HTML content is explicitly approved before production acceptance.
9. Product and project documents use the canonical repository names and agree on the approved blog-platform direction.

**Current status: OR-001 through OR-013 are resolved at the requirements-definition level. Final public HTML owner approval, selected edge-service validation, and implementation evidence remain production acceptance gates.**
