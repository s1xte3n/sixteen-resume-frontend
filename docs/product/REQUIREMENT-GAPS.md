# Requirement Gap Register

## 1. Purpose

This register contains unresolved, vague, contradictory, duplicated, deferred, or objectively unverifiable requirements derived from the approved PRD.

These items are not silently resolved and do not become implementation tasks until their required decisions are closed.

---

## 2. P1 Blocking Gaps

| ID | Source | Classification | Affected requirements | Status | Required resolution |
|---|---|---|---|---|---|
| GAP-AZ-001 | OR-001 | Ambiguous / unverifiable | REQ-AZ-007..009, REQ-AZ-015 | CLOSED | Visitor semantics defined as one successfully committed counter operation per top-level resume page load. |
| GAP-AZ-002 | OR-002 / IC-001 | Contradictory | REQ-AZ-006, REQ-AZ-015 | CLOSED | FreeDNS hosted hostname/subdomain accepted as the MVP public-hostname interpretation and documented as a challenge deviation. |
| GAP-AZ-003 | OR-003 | Unverifiable before numeric constraint | REQ-AZ-005, REQ-AZ-006, REQ-AZ-012, REQ-AZ-015 | CLOSED | Hard recurring Azure/cloud ceiling fixed at R100/month; R0/month preferred; exclusions and unexpected-charge investigation rule recorded. |
| GAP-AZ-004 | OR-004 / IC-003 | Architecture-selection dependency | REQ-AZ-005, REQ-AZ-006, REQ-AZ-014, REQ-AZ-015 | CLOSED — capability level | Azure-managed HTTPS/CDN delivery architecture is frozen. Exact service selection is an implementation validation task against HTTPS, hostname, Storage origin, IaC and R100/month conditions. |
| GAP-AZ-005 | OR-005 | Content approval | REQ-AZ-001, REQ-AZ-015 | CLOSED — content definition | Public resume content policy and positioning are defined. Final owner approval of the actual published HTML remains a production acceptance gate. |
| GAP-AZ-006 | Repository naming/state | Documentation/state inconsistency | REQ-AZ-013, REQ-AZ-014, REQ-AZ-GIT-001 | CLOSED | Canonical repositories are `s1xte3n/sixteen-resume-frontend` and `s1xte3n/sixteen-resume-backend`. Actual repository state must be reflected in project documentation. |

---

## 3. P2 Gaps

| ID | Source | Classification | Affected requirements | Status | Required resolution |
|---|---|---|---|---|---|
| GAP-AZ-007 | OR-006 | API contract definition | REQ-AZ-009, REQ-AZ-010 | CLOSED | `GET /api/visitors`, request validation, response/error schemas, status semantics and CORS boundary are defined by API v1. |
| GAP-AZ-008 | OR-009 | Failure UX definition | REQ-AZ-007, REQ-AZ-009 | CLOSED | Counter failure must not prevent resume rendering; exact presentation remains implementation detail unless promoted to a product requirement. |
| GAP-AZ-009 | OR-006 | Implementation detail | REQ-AZ-011, REQ-AZ-013 | DEFERRED — implementation choice | Select the Python test framework during Phase 7 implementation. This does not block implementation because the test requirement itself is already defined. |
| GAP-AZ-010 | OR-007 | Documentation inconsistency | REQ-AZ-016 | CLOSED | Dev.to and Hashnode are the approved publishing platforms. The project documentation must use this consistently. |
| GAP-AZ-011 | OR-010 | Compatibility baseline | REQ-AZ-001, REQ-AZ-003, REQ-AZ-015 | CLOSED | Browser baseline is latest stable and immediately preceding major release of Chrome, Edge, Firefox and Safari; required viewports are 375x667, 390x844, 768x1024 and 1440x900 CSS pixels. |
| GAP-AZ-012 | OR-011 | Availability requirement | REQ-AZ-015 | CLOSED | No formal production availability SLO is part of the MVP. |
| GAP-AZ-013 | OR-012 | DNS acceptance | REQ-AZ-006, REQ-AZ-015 | CLOSED | DNS acceptance uses authoritative and independent resolver evidence within the documented provider TTL window. |

---

## 4. P3 Gap

| ID | Source | Classification | Affected requirement | Status |
|---|---|---|---|---|
| GAP-AZ-014 | OR-013 | Minor UX | REQ-AZ-016 | CLOSED |

Blog links use:

```html
target="_blank"
rel="noopener noreferrer"

## 5. Missing / Weakly Testable Requirements

The source requirements do not currently provide measurable definitions for:

- Accessibility target.
- Performance target.
- Cache freshness target.
- Availability SLO.
- DNS propagation SLA.
- Rollback expectation.
- Monitoring/alerting requirement.
- Exact blog article minimum content/length.
- Exact minimum resume sections.
- Counter failure UX.

These are recorded rather than invented.

## 6. Deliberate Deviation

### GAP-AZ-015 — AZ-900

The original challenge calls for AZ-900 or an advanced Azure certification. The approved project intentionally excludes AZ-900 and permits AI-901 to be displayed as an existing certification.

**Classification:** Accepted project deviation.
**Status:** ACCEPTED-DEVIATION
**Constraint:** The project must not claim literal AZ-900 compliance unless AZ-900 is subsequently obtained.

## 7. Documentation Consistency

### GAP-AZ-016 — Artifact Index Filename

Historical documentation referenced `docs/project/OPEN-QUESTIONS.md`, while the canonical project artifact is `docs/project/UNRESOLVED-QUESTIONS.md`.

**Classification:** Documentation inconsistency.
**Status:** OPEN until all references are normalized.

## 8. Duplicate / Overlapping Requirement Findings

No duplicate MVP capability has been introduced by the requirements conversion. Some cross-cutting requirements intentionally overlap MVP behavior, especially HTTPS and browser-to-Cosmos isolation; these are governance/security controls, not duplicate product features.

## 9. Step 7 Closure Notes

The P1 decision gaps that previously blocked REQ-AZ-001, REQ-AZ-005..009, and REQ-AZ-013..015 are now closed at the requirements-definition level. Their affected requirements are implementation-ready, but they are not implementation-complete. Final content approval, edge-service/cost validation, hostname provisioning/validation, concurrency-safe persistence evidence, CI/CD implementation, and production deployment evidence remain acceptance or implementation gates as applicable.

## 10. Gap Closure Rule

A gap closes only when:

1. The decision or correction is explicitly recorded.
2. Affected requirements are updated.
3. Acceptance criteria are updated if behavior changes.
4. Traceability is synchronized.
5. Dependencies are recalculated.
6. The backlog is updated only after the requirement becomes implementation-ready.
