# Azure Cloud Resume Challenge — Unresolved Questions

> **Source of truth:** `docs/product/OPEN-REQUIREMENTS.md`
>
> This document is the project-level working view of the unresolved requirements recorded in the authoritative open-requirements register. It must not introduce new unresolved questions, silently resolve an open requirement, or mark an open requirement as closed.
>
> **Current status:** Requirements closure is **CLOSED**. OR-001 through OR-013 are resolved at the requirements-definition level. Final service selection/validation, owner content approval, infrastructure deployment, and production evidence remain implementation/production-acceptance gates.

## 1. Reconciliation Rules

The two documents have distinct roles:

- `docs/product/OPEN-REQUIREMENTS.md` is the authoritative product-level register.
- `docs/project/UNRESOLVED-QUESTIONS.md` mirrors every currently open requirement and provides project-facing context.
- IDs and status values in this document must remain aligned with the authoritative register.
- Implementation details that are not themselves unresolved product requirements belong in implementation/design documentation, not in this unresolved-questions register.
- Deliberate decisions such as AI-901, FreeDNS provider selection, repository names, region, and deployment count are not unresolved unless the authoritative register explicitly reopens them.

---

## 2. P1 Decisions

These items must be resolved before affected MVP acceptance and before requirements closure.

**Resolved P1 decisions:** OR-001 through OR-005. OR-004 is resolved at capability level; OR-005 is resolved at content-definition level.

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

**Decision:** Set the MVP hard ceiling to **R100/month recurring Azure/cloud cost**.

**Cost policy:**
- R0/month is preferred.
- R0–R100/month recurring is allowed.
- >R100/month recurring is blocked.
- Exclude personal internet access, existing equipment, optional paid domain registration, and one-time purchases explicitly approved later.
- Paid domain registration is out of MVP.
- Any unexpected charge must be investigated before project work continues.

**Acceptance rule:** Current measured or forecast recurring Azure/cloud cost attributable to the MVP must be `<= R100/month` for production acceptance.

---

### OR-004 — HTTPS/CDN Configuration

**Affected requirements:** MVP-005, MVP-015  
**Status:** Resolved at capability level; selected service validation remains an implementation gate

**Decision:** Use **Azure-managed HTTPS/CDN delivery layer** in front of the Azure Storage static website.

**Approved delivery path:**

```text
FreeDNS public hostname
        |
        v
Azure-managed HTTPS/CDN delivery layer
        |
        v
Azure Storage Static Website
```

**HTTPS:** Use an Azure-managed TLS certificate on the Front Door custom domain and redirect HTTP to HTTPS.

**CDN/delivery:** Azure-managed HTTPS/CDN delivery layer provides the required edge/CDN delivery layer.

**Cost basis:** Microsoft's current published Front Door pricing lists a $35/month Standard base fee, plus usage-based request and data-transfer charges. The project's total recurring Azure/cloud ceiling is R100/month.

**Production validation:** Deployment evidence must verify the actual Front Door SKU, hostname, HTTPS certificate, origin, and total estimated/observed billing remain within the approved ceiling.

**Alternatives rejected:**

- Front Door Premium — unnecessary for the MVP and materially higher base cost.
- Front Door Classic — retiring and not appropriate for new onboarding.
- Direct Storage delivery — does not satisfy the required CDN/delivery architecture.

---

### OR-005 — Public Resume Content

**Affected requirements:** MVP-001, MVP-015  
**Status:** Resolved at content-definition level; final owner approval remains a production acceptance gate

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

## 3. Resolved P2 Decisions

All P2 decisions listed here are resolved. Their implementation and acceptance evidence remains governed by the requirements, architecture, API contract, and release gates.

### OR-006 — Backend/API Contract

**Affected requirements:** MVP-009, MVP-010  
**Status:** Resolved

The visitor API has exactly one MVP responsibility: `GET /api/visitors`.

The successful response contains the current visitor count.

The browser has no Cosmos DB credentials and no direct Cosmos DB access. Azure Functions remains the backend/API boundary.

---

### OR-007 — Persistence Behavior

**Affected requirements:** MVP-008, MVP-009  
**Status:** Resolved

Use one logical visitor-counter record.

For each successful counter operation, the backend reads the current count, atomically increments it, persists it, and returns the resulting count.

The implementation must protect against concurrent lost updates.

---

### OR-008 — CI/CD Deployment Authority

**Affected requirements:** MVP-013, MVP-014  
**Status:** Resolved

GitHub Actions is the deployment mechanism. Production deployment from a developer laptop is not a valid production release.

The backend pipeline is:

`checkout → install dependencies → run tests → validate infrastructure → deploy`

The frontend pipeline is:

`checkout → validate website → publish to Azure Storage → purge/invalidate edge cache when required`

---

### OR-009 — Production Release

**Affected requirements:** MVP-013, MVP-014, MVP-015  
**Status:** Resolved

`main` represents production.

The intended workflow is:

`feature/* → Pull Request → CI → develop → production release → main`

---

### OR-010 — Browser Support

**Affected requirements:** MVP-001, MVP-003, MVP-015  
**Status:** Resolved

The MVP browser baseline is the latest stable release and immediately preceding major release of Chrome, Edge, Firefox, and Safari available at test execution; viewports are 375x667, 390x844, 768x1024, and 1440x900 CSS pixels.

---

### OR-011 — Availability Target

**Affected requirements:** MVP-015  
**Status:** Resolved

No formal production availability SLO is part of the MVP. Acceptance uses the defined functional, security, deployment, DNS, HTTPS, and cost criteria.

---

### OR-012 — DNS Propagation

**Affected requirements:** MVP-006, MVP-015  
**Status:** Resolved

A DNS change is accepted when the authoritative FreeDNS nameserver returns the intended record and independent public recursive resolvers return the intended record within the provider's documented default TTL window of 1 hour.

---

## 4. Resolved P3 Decision

### OR-013 — Blog Link Behavior

**Status:** Resolved

Project-learning links open in a new browser tab/window using `target="_blank"` with `rel="noopener noreferrer"`.

---

## 5. Related Contradictions and Dependencies

### IC-001 — Custom Domain vs Free Hostname

The original challenge describes a custom DNS domain. The approved project excludes paid domain purchase and selects FreeDNS/afraid.org as the DNS direction. This is tracked by OR-002.

### IC-002 — AZ-900

The original challenge specifies AZ-900 or an advanced Azure certification. The approved project explicitly excludes AZ-900 and documents AI-901 as the existing certification. This is a deliberate project deviation, not an unresolved ambiguity.

### IC-003 — CDN/HTTPS vs Zero/Near-Zero Cost

HTTPS/CDN delivery is required while the project targets R0/free where possible and lowest-cost viable otherwise. The numeric ceiling is resolved at R100/month; HTTPS/CDN configuration validation remains tracked by OR-004.

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

**Current closure status: CLOSED for requirements definition.** Final production acceptance still requires implementation evidence, selected edge-service validation, and explicit owner approval of the final public HTML resume content.

---

## 7. Resolved Context — Not Open Questions

These are retained only to prevent accidental reopening of already-decided project context. They are **not** unresolved requirements.

| Item | Current decision/context |
|---|---|
| DNS provider | FreeDNS / afraid.org selected initially; hostname must be provisioned and verified against the OR-002 acceptance rule. |
| Delivery service | Unresolved; Azure-managed HTTPS/CDN delivery layer required, exact service pending OR-004 validation. |
| HTTPS certificate | Subject to the selected delivery service and OR-004 validation. |
| Cost ceiling | R100/month recurring Azure cost; USD $0 one-time domain/infrastructure purchase required by MVP. |
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
| Cost strategy | R0/free where possible; hard ceiling R100/month recurring Azure/cloud cost. OR-003 resolved. |
| Visual design | No predefined preference; simple professional implementation is an implementation direction, not an unresolved product requirement. |
| Deadline | 30 September 2026. |
| Project scope | Strictly aligned with the Cloud Resume Challenge; unrelated feature expansion remains out of scope. |
