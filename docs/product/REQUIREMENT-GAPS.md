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
| GAP-AZ-009 | OR-006 | Implementation detail | REQ-AZ-011, REQ-AZ-013 | CLOSED | Backend Python tests use pytest; CI must execute pytest before deployment. |
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

The source requirements intentionally do not provide formal measurable targets for accessibility, performance, cache freshness, rollback, monitoring/alerting, article length, or minimum resume section count. These must not be invented as product requirements. Availability, DNS acceptance, browser baseline, API contract, and counter failure behavior are already defined elsewhere in the canonical requirements and acceptance artifacts.

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
**Status:** CLOSED — the canonical artifact is `docs/project/UNRESOLVED-QUESTIONS.md`; remaining historical references must be treated as documentation cleanup only.

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
