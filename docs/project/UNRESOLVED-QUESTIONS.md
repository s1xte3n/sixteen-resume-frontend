# Azure Cloud Resume Challenge — Unresolved Questions

> **Source of truth:** `docs/product/OPEN-REQUIREMENTS.md`
>
> This document is the project-level working view of the unresolved requirements recorded in the authoritative open-requirements register. It must not introduce new unresolved questions, silently resolve an open requirement, or mark an open requirement as closed.
>
> **Current status:** Requirements closure is **NOT CLOSED**. OR-004 and OR-005 are P1 closure blockers; OR-001, OR-002, and OR-003 are resolved.

## 1. Reconciliation Rules

The two documents have distinct roles:

- `docs/product/OPEN-REQUIREMENTS.md` is the authoritative product-level register.
- `docs/project/UNRESOLVED-QUESTIONS.md` mirrors every currently open requirement and provides project-facing context.
- IDs and status values in this document must remain aligned with the authoritative register.
- Implementation details that are not themselves unresolved product requirements belong in implementation/design documentation, not in this unresolved-questions register.
- Deliberate decisions such as AI-901, FreeDNS provider selection, repository names, region, and deployment count are not unresolved unless the authoritative register explicitly reopens them.

---

## 2. P1 Open Decisions

These items must be resolved before affected MVP acceptance and before requirements closure.

**Resolved P1 decisions:** OR-001, OR-002, and OR-003. The remaining P1 closure blockers are OR-004 and OR-005.

### OR-001 — Visitor Definition

**Affected requirements:** MVP-007, MVP-008, MVP-009  
**Status:** Resolved

**Decision:** A visitor is one successfully committed visitor-counter API operation initiated by a top-level resume page load.

**Counting semantics:**
- The frontend performs exactly one counter request per top-level resume page load.
- A refresh is a new page load and therefore counts as another visit.
- The counter does not identify unique humans, browsers, sessions, IP addresses, devices, or users.
- A successfully committed operation increments the persisted total by exactly one.
- Failed API/database operations do not increment the persisted count.
- Duplicate HTTP requests are separate operations unless a future requirement explicitly introduces idempotency.

**Concurrency rule:** The backend must perform an atomic/concurrency-safe increment so concurrent successful requests cannot overwrite each other.

**Acceptance invariant:** If the persisted value is N, then K successfully committed counter operations result in N + K.

---

### OR-002 — Free Hostname vs Custom Domain

**Affected requirements:** MVP-006, MVP-015  
**Status:** Resolved

**Decision:** Accept the selected FreeDNS/afraid.org hosted hostname/subdomain for the MVP as the project's scoped public-hostname/DNS interpretation.

**Project constraint:** The MVP must not require paid domain registration.

---

### OR-003 — Numeric Cost Ceiling

**Affected requirements:** MVP-005, MVP-006, MVP-012, MVP-015  
**Status:** Resolved

**Decision:** Set the MVP hard ceiling to **USD $40/month recurring Azure/cloud cost**.

**Cost policy:**
- R0/month is preferred.
- R0–USD $40/month recurring is allowed.
- >USD $40/month recurring is blocked.
- Exclude personal internet access, existing equipment, optional paid domain registration, and one-time purchases explicitly approved later.
- Paid domain registration is out of MVP.
- Any unexpected charge must be investigated before project work continues.

**Acceptance rule:** Current measured or forecast recurring Azure/cloud cost attributable to the MVP must be `<= USD $40/month` for production acceptance.

---

### OR-004 — HTTPS/CDN Configuration

**Affected requirements:** MVP-005, MVP-015  
**Status:** Open

**Decision:** Use **Azure Front Door Standard** in front of the Azure Storage static website.

**Approved delivery path:**

```text
FreeDNS public hostname
        |
        v
Azure Front Door Standard
        |
        v
Azure Storage Static Website
```

**HTTPS:** Use an Azure-managed TLS certificate on the Front Door custom domain and redirect HTTP to HTTPS.

**CDN/delivery:** Azure Front Door Standard provides the required edge/CDN delivery layer.

**Cost basis:** Microsoft's current published Front Door pricing lists a $35/month Standard base fee, plus usage-based request and data-transfer charges. The project's total recurring Azure ceiling is $40/month.

**Production validation:** Deployment evidence must verify the actual Front Door SKU, hostname, HTTPS certificate, origin, and total estimated/observed billing remain within the approved ceiling.

**Alternatives rejected:**

- Front Door Premium — unnecessary for the MVP and materially higher base cost.
- Front Door Classic — retiring and not appropriate for new onboarding.
- Direct Storage delivery — does not satisfy the required CDN/delivery architecture.

---

### OR-005 — Public Resume Content

**Affected requirements:** MVP-001, MVP-015  
**Status:** Open pending Project Owner approval

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

---

## 3. P2 Open Requirements

These remain open in the authoritative register and may be resolved during implementation only where doing so does not bypass an affected acceptance or closure requirement.

### OR-006 — Python Testing Framework

**Affected requirements:** MVP-011, MVP-013  
**Status:** Intentionally deferred until test implementation is prepared.

The approved requirement requires automated Python tests but does not select a framework. Final acceptance requires a documented framework and repeatable CI execution.

---

### OR-007 — Blog Platform Normalization

**Affected requirements:** MVP-016  
**Status:** Open documentation inconsistency.

The approved project state specifies both Dev.to and Hashnode and describes the content scope as technical lessons, implementation, problems, solutions/decisions, and the broader project journey. Earlier product documentation treated the platform as undecided. The approved project-state decision must be reflected consistently in product documentation before final acceptance.

---

### OR-008 — Visitor API Contract

**Affected requirements:** MVP-009, MVP-010  
**Status:** Open

The final contract must define at minimum:

- HTTP method(s).
- Endpoint purpose/path.
- Request inputs and required/optional fields.
- Successful response schema.
- Error response schema.
- HTTP status behavior.
- Counter semantics.
- CORS behavior.

This must remain aligned with the approved API/interface contract when finalized.

---

### OR-009 — Counter Failure UX

**Affected requirements:** MVP-007, MVP-009  
**Status:** Open

Possible behaviors already identified are hiding the counter, displaying an unavailable state, displaying a last-known value, or another approved fallback. No option is selected.

The chosen behavior must not prevent access to the resume.

---

### OR-010 — Browser Support

**Affected requirements:** MVP-001, MVP-003, MVP-015  
**Status:** Open

The requirements say supported modern browsers/common desktop and mobile viewports but do not provide a version matrix. A final compatibility test baseline is required before objective acceptance.

---

### OR-011 — Availability Target

**Affected requirements:** MVP-015  
**Status:** Open

No formal availability SLO is currently approved. The product must not claim an uptime target that is not defined by the project.

---

### OR-012 — DNS Propagation

**Affected requirements:** MVP-006, MVP-015  
**Status:** Open

DNS acceptance needs a defined expectation for propagation/stability if timing is to be tested objectively.

---

## 4. P3 Open Requirements

### OR-013 — Blog Link Behavior

**Status:** Open

The project has not specified whether the project-learning link opens in the same tab or a new tab. This is a minor UX detail and does not block requirements closure unless explicitly promoted.

---

## 5. Related Contradictions and Dependencies

### IC-001 — Custom Domain vs Free Hostname

The original challenge describes a custom DNS domain. The approved project excludes paid domain purchase and selects FreeDNS/afraid.org as the DNS direction. This is tracked by OR-002.

### IC-002 — AZ-900

The original challenge specifies AZ-900 or an advanced Azure certification. The approved project explicitly excludes AZ-900 and documents AI-901 as the existing certification. This is a deliberate project deviation, not an unresolved ambiguity.

### IC-003 — CDN/HTTPS vs Zero/Near-Zero Cost

HTTPS/CDN delivery is required while the project targets R0/free where possible and lowest-cost viable otherwise. The numeric ceiling is resolved at USD $40/month; HTTPS/CDN configuration validation remains tracked by OR-004.

### IC-004 — Blog Platform Documentation

Approved project-state documentation specifies Dev.to + Hashnode, while older product documentation marked the platform undecided. The approved project-state decision is the current direction, but the documents must be normalized before final acceptance. This is tracked by OR-007.

### IC-005 — Repository Naming in Historical Documentation

Older product artifacts used `sixteen-frontend` and `sixteen-backend`; the approved repository names are `sixteen-resume-frontend` and `sixteen-resume-backend`. The PRD and acceptance criteria now use the approved names. Other project artifacts must be synchronized as part of requirements/documentation governance.

---

## 6. Requirements Closure Blockers

Requirements closure remains blocked until the authoritative closure rule in `OPEN-REQUIREMENTS.md` is satisfied:

1. Every MVP feature has testable acceptance criteria and a verification ID.
2. No P0 ambiguity remains.
3. No P1 ambiguity remains hidden.
4. All deliberate deviations from the original challenge are documented.
5. The numeric cost constraint is defined.
6. Visitor-count semantics are defined.
7. Public hostname interpretation is defined.
8. HTTPS/CDN configuration is validated.
9. Final public resume content is approved.
10. Product and project documents use the canonical repository names and agree on the approved blog-platform direction.

**Current closure status: NOT CLOSED.**

---

## 7. Resolved Context — Not Open Questions

These are retained only to prevent accidental reopening of already-decided project context. They are **not** unresolved requirements.

| Item | Current decision/context |
|---|---|
| DNS provider | FreeDNS / afraid.org selected initially; hostname must be provisioned and verified against the OR-002 acceptance rule. |
| Delivery service | Azure Front Door Standard. |
| HTTPS certificate | Azure-managed TLS certificate on the Front Door custom domain. |
| Cost ceiling | USD $40/month recurring Azure cost; USD $0 one-time domain/infrastructure purchase required by MVP. |
| Azure certification | AI-901 is held and is the documented certification deviation from the literal AZ-900 challenge requirement. |
| Resume source | Complete CV supplied; public publication approval remains OR-005. |
| Resume positioning | 4+ years of hands-on software development experience, with professional employment represented separately as IT Operator — Gijima Holdings. |
| Backend repository | `sixteen-resume-backend`. |
| Frontend repository | `sixteen-resume-frontend`. |
| Blog platforms | Dev.to + Hashnode; documentation normalization remains OR-007. |
| Blog scope | Technical lessons plus the complete project journey. |
| Azure subscription | Existing subscription. |
| Azure region | East US. |
| Deployment count | One deployment environment. |
| Cost strategy | R0/free where possible; hard ceiling USD $40/month recurring Azure/cloud cost. OR-003 resolved. |
| Visual design | No predefined preference; simple professional implementation is an implementation direction, not an unresolved product requirement. |
| Deadline | 30 September 2026. |
| Project scope | Strictly aligned with the Cloud Resume Challenge; unrelated feature expansion remains out of scope. |
