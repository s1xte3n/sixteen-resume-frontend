# Requirement Gap Register

## 1. Purpose

This register contains unresolved, vague, contradictory, duplicated, deferred, or objectively unverifiable requirements derived from the approved PRD. These items are not silently resolved and do not become implementation tasks until their required decisions are closed.

## 2. P1 Blocking Gaps

| ID | Source | Classification | Affected requirements | Status | Required resolution |
|---|---|---|---|---|---|
| GAP-AZ-001 | OR-001 | Ambiguous / unverifiable | REQ-AZ-007..009, REQ-AZ-015 | OPEN | Define the counting unit: page load, API request, session, unique visitor, or another explicit unit. |
| GAP-AZ-002 | OR-002 / IC-001 | Contradictory | REQ-AZ-006, REQ-AZ-015 | OPEN | Explicitly approve free hostname/subdomain as a project deviation or change scope. |
| GAP-AZ-003 | OR-003 | Unverifiable (resolved) | REQ-AZ-005, REQ-AZ-006, REQ-AZ-012, REQ-AZ-015 | CLOSED | Cost ceiling fixed at USD $40/month recurring Azure/cloud cost; R0/month preferred; explicit exclusions and unexpected-charge investigation rule recorded. |
| GAP-AZ-004 | OR-004 / IC-003 | Unresolved architecture requirement | REQ-AZ-005, REQ-AZ-006, REQ-AZ-014, REQ-AZ-015 | OPEN | Validate delivery service availability, HTTPS/certificate support, DNS compatibility, Storage compatibility, cache behavior, and cost. |
| GAP-AZ-005 | OR-005 | Content approval | REQ-AZ-001, REQ-AZ-015 | OPEN | Approve the exact public CV-derived content and identifying information. |
| GAP-AZ-006 | Repository naming/state | Contradictory | REQ-AZ-013, REQ-AZ-014, REQ-AZ-GIT-001 | OPEN | Normalize canonical repository names and branch model against actual GitHub state. |

## 3. P2 Gaps

| ID | Source | Classification | Affected requirements | Status | Required resolution |
|---|---|---|---|---|---|
| GAP-AZ-007 | OR-008 | Ambiguous | REQ-AZ-007..010 | OPEN | Define method, endpoint, inputs, success/error responses, status codes, counter semantics, and CORS behavior. |
| GAP-AZ-008 | OR-009 | Ambiguous | REQ-AZ-007, REQ-AZ-009 | OPEN | Define visitor-visible counter failure behavior. |
| GAP-AZ-009 | OR-006 | Deferred | REQ-AZ-011, REQ-AZ-013 | DEFERRED | Select and document the Python test framework before final CI acceptance. |
| GAP-AZ-010 | OR-007 | Documentation contradiction | REQ-AZ-016 | OPEN | Normalize whether Dev.to and Hashnode are both required, either is acceptable, or one is primary/other optional. |
| GAP-AZ-011 | OR-010 | Unverifiable | REQ-AZ-001, REQ-AZ-003, REQ-AZ-015 | OPEN | Define supported browser/version baseline. |
| GAP-AZ-012 | OR-011 | Unspecified | REQ-AZ-015 | OPEN | Define whether a formal availability target is required. |
| GAP-AZ-013 | OR-012 | Unverifiable | REQ-AZ-006, REQ-AZ-015 | OPEN | Define acceptable DNS propagation/stability expectations. |

## 4. P3 Gap

| ID | Source | Classification | Affected requirement | Status |
|---|---|---|---|---|
| GAP-AZ-014 | OR-013 | Minor UX ambiguity | REQ-AZ-016 | OPEN |

Blog link tab behavior is not defined. It does not block the core product baseline.

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

## 9. Gap Closure Rule

A gap closes only when:

1. The decision or correction is explicitly recorded.
2. Affected requirements are updated.
3. Acceptance criteria are updated if behavior changes.
4. Traceability is synchronized.
5. Dependencies are recalculated.
6. The backlog is updated only after the requirement becomes implementation-ready.
