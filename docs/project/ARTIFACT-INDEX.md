# Artifact Index

## 1. Purpose

This document identifies authoritative project documentation, product requirements artifacts, implementation artifacts, and their current status.

## 2. Project Documentation

| Artifact | Purpose | Status | Source of Truth |
|---|---|---|---|
| `docs/project/PROJECT-OVERVIEW.md` | Project purpose, users, scope, constraints, technology, deployment, and goals | Current | Yes |
| `docs/project/PROJECT-STATUS.md` | Current implementation state and project status | Current | Yes |
| `docs/project/DECISIONS.md` | Confirmed decisions and rationale | Current | Yes |
| `docs/project/UNRESOLVED-QUESTIONS.md` | Discovery/project-level unresolved questions | Current; must remain synchronized with product blockers | Yes |
| `docs/project/ARTIFACT-INDEX.md` | Documentation governance and artifact inventory | Updated | Yes |

## 3. Product Documentation

| Artifact | Purpose | Status | Source of Truth |
|---|---|---|---|
| `docs/product/PRD.md` | Complete product requirements and feature-level specifications | Complete draft; closure pending | Yes |
| `docs/product/USER-STORIES.md` | User stories and use cases mapped to requirement IDs | Updated | Yes |
| `docs/product/ACCEPTANCE-CRITERIA.md` | Testable acceptance criteria and verification IDs for every MVP requirement | Updated | Yes |
| `docs/product/SCOPE.md` | MVP, P1/P2/P3 scope, exclusions, constraints, and scope governance | Updated | Yes |
| `docs/product/OPEN-REQUIREMENTS.md` | Unresolved product decisions, contradictions, hidden dependencies, and untestable requirements | Updated | Yes |
| `docs/product/REQUIREMENTS.md` | Canonical traceable requirement matrix | Downstream artifact; must reflect updated PRD | Yes |
| `docs/product/TRACEABILITY-MATRIX.md` | Requirement-to-test/implementation/release traceability | Downstream artifact | Yes |
| `docs/product/FEATURE-BACKLOG.md` | Implementation-ready backlog | Downstream artifact; no blocked P1 implementation tasks | Yes |
| `docs/product/DEPENDENCY-MATRIX.md` | Requirement sequencing and dependency relationships | Downstream artifact | Yes |
| `docs/product/REQUIREMENT-GAPS.md` | Ambiguous, contradictory, unverifiable, and missing requirements | Downstream artifact | Yes |

## 4. Architecture Documentation

| Artifact | Purpose | Status |
|---|---|---|
| `docs/architecture/ARCHITECTURE.md` | Logical/system architecture | Proposed; not frozen |
| `docs/architecture/DATA-MODEL.md` | Persistent data model | Proposed |
| `docs/architecture/SECURITY-ARCHITECTURE.md` | Security boundaries and controls | Proposed |
| `docs/architecture/INFRASTRUCTURE.md` | Azure resource/environment architecture | Proposed |
| `docs/architecture/OBSERVABILITY.md` | Operational telemetry and failure signals | Proposed |
| `docs/architecture/ADR-INDEX.md` | Architecture decision catalogue | Proposed |
| `docs/architecture/ADR-001.md` | Static frontend architecture | Accepted |
| `docs/architecture/ADR-002.md` | Function/API boundary | Accepted |
| `docs/architecture/ADR-003.md` | Cosmos DB persistence | Accepted |
| `docs/architecture/ADR-004.md` | ARM and CI/CD architecture | Accepted |
| `docs/architecture/ADR-005.md` | CI/CD security/authentication | Accepted in principle |
| `docs/architecture/ADR-006.md` | HTTPS/CDN architecture | Pending validation |
| `docs/architecture/ADR-007.md` | Visitor-count semantics | Pending approval |

## 5. Source Requirements

| Source | Purpose | Status |
|---|---|---|
| Azure Cloud Resume Challenge requirements | Original challenge baseline | Current |
| Approved project state | Project-specific constraints and decisions | Current |
| `docs/product/PRD.md` | Canonical project-specific product requirements | Current |
| Supplied CV | Resume-content source | Current |

## 6. Canonical Repository Names

| Repository | Purpose | Status |
|---|---|---|
| `s1xte3n/sixteen-resume-frontend` | Frontend resume application and documentation | Exists |
| `s1xte3n/sixteen-resume-backend` | Backend/API/IaC application | Exists / implementation state must be verified |

Historical references to `sixteen-frontend` and `sixteen-backend` are obsolete and must not be used in new product requirements or acceptance criteria.

## 7. Current Implementation Artifacts

| Artifact | Status |
|---|---|
| HTML resume | Not started |
| CSS | Not started |
| JavaScript visitor counter | Blocked by OR-001/OR-008/OR-009 |
| Azure Storage | Not started |
| HTTPS/CDN | Blocked by OR-003/OR-004 |
| DNS hostname | Blocked by OR-002 |
| Cosmos DB | Not started |
| Azure Function | Not started |
| Python implementation | Not started |
| Python tests | Blocked by OR-006 |
| ARM templates | Not started |
| Backend GitHub Actions | Blocked by test/auth/repository-state dependencies |
| Frontend GitHub Actions | Blocked by delivery/repository-state dependencies |
| Production deployment | Blocked by P1 requirements |
| Blog — Dev.to | Not started |
| Blog — Hashnode | Not started |
| Public resume content approval | Pending OR-005 |
| System architecture | Proposed |
| Data model | Proposed |
| Security architecture | Proposed |
| Infrastructure architecture | Proposed |
| Observability architecture | Proposed |
| Production implementation | Not started |

## 8. Requirements Phase Status

**Status: PRD requirements baseline updated; closure pending.**

### Requirement coverage

- 16 canonical MVP requirements.
- Every MVP requirement has a detailed PRD specification.
- Every MVP requirement has acceptance criteria.
- Every MVP requirement has a verification ID (`VT-001` through `VT-016`).
- P0/P1 blockers remain explicitly visible in `OPEN-REQUIREMENTS.md`.

### Current P1 blockers

1. OR-001 — Visitor-count semantics.
2. OR-002 — Free hostname versus custom-domain interpretation.
3. OR-003 — Numeric cost ceiling.
4. OR-004 — HTTPS/CDN configuration and cost validation.
5. OR-005 — Final public resume-content approval.

### Current P2/P3 decisions

- OR-006 — Python test framework, intentionally deferred.
- OR-007 — Blog-platform documentation normalization; approved project state specifies Dev.to + Hashnode.
- OR-008 — Visitor API contract.
- OR-009 — Counter failure UX.
- OR-010 — Browser support baseline.
- OR-011 — Availability target.
- OR-012 — DNS propagation/stability expectation.
- OR-013 — Blog link tab behavior.

## 9. Requirements Governance

The authoritative relationship is:

```text
Approved Project State
        ↓
      PRD
        ↓
 User Stories + Acceptance Criteria
        ↓
 Open Requirements / Scope
        ↓
 Requirements Matrix + Traceability + Dependencies
        ↓
 Architecture
        ↓
 Implementation + Tests + CI/CD Evidence
```

The product documents must not create implementation tasks for unresolved P1 decisions.

## 10. Artifact Status Rules

When a requirement or decision changes:

1. Update `docs/product/PRD.md`.
2. Update `docs/product/OPEN-REQUIREMENTS.md` when ambiguity exists.
3. Update `docs/product/SCOPE.md` when scope changes.
4. Update `docs/product/USER-STORIES.md` and `docs/product/ACCEPTANCE-CRITERIA.md` when behavior or acceptance changes.
5. Synchronize downstream requirement/traceability/dependency artifacts.
6. Record significant confirmed decisions in `docs/project/DECISIONS.md`.
7. Update `docs/project/PROJECT-STATUS.md` when implementation state changes.
8. Update this artifact index.
9. Never mark a blocked requirement complete without evidence.

## 11. Architecture Gate

Architecture is **proposed, not frozen**.

The architecture must not be considered implementation-frozen until the material product decisions affecting architecture are resolved, including visitor semantics, hostname interpretation, numeric cost ceiling, HTTPS/CDN configuration, final public content, and the API contract where it changes system boundaries.

## 12. PRD Closure Gate

The PRD phase is closed only when:

- every MVP requirement has a unique ID, priority, dependencies, acceptance criteria, and verification path;
- no P0/P1 ambiguity remains hidden;
- contradictions are explicitly resolved or documented as deviations;
- untestable requirements receive measurable definitions;
- final scope is synchronized across product/project documentation;
- the numeric cost ceiling is defined;
- visitor-count semantics are defined;
- hostname interpretation is defined;
- HTTPS/CDN configuration is validated;
- final public resume content is approved.

**Current gate result: NOT CLOSED.** The requested product artifacts have been updated, but the five P1 decisions above remain unresolved and therefore the project must not claim PRD closure yet.

## 13. Next Gate

The next action is **P1 product-decision closure**, not implementation. No implementation task is created by this artifact index.
