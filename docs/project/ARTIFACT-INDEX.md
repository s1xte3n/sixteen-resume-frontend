# Artifact Index

## 1. Purpose

This document identifies authoritative project documentation, product requirements artifacts, implementation artifacts, and their current status.

## 2. Project Documentation

| Artifact | Purpose | Status | Source of Truth |
|---|---|---|---|
| `docs/project/PROJECT-OVERVIEW.md` | Project purpose, users, scope, constraints, technology, deployment, and goals | Current | Yes |
| `docs/project/PROJECT-STATUS.md` | Current implementation state and project status | Current | Yes |
| `docs/project/DECISIONS.md` | Confirmed decisions and rationale | Current | Yes |
| `docs/project/UNRESOLVED-QUESTIONS.md` | Discovery/project-level unresolved questions | Current; synchronize with product gaps | Yes |
| `docs/project/ARTIFACT-INDEX.md` | Documentation governance and artifact inventory | Updated | Yes |

## 3. Product Documentation

| Artifact | Purpose | Status | Source of Truth |
|---|---|---|---|
| `docs/product/PRD.md` | Complete product requirements and feature specifications | Complete draft; closure pending P1 decisions | Yes |
| `docs/product/USER-STORIES.md` | User stories and use cases mapped to requirements | Current | Yes |
| `docs/product/ACCEPTANCE-CRITERIA.md` | Testable acceptance criteria and verification IDs | Current | Yes |
| `docs/product/SCOPE.md` | MVP, P1/P2/P3 scope, exclusions, constraints | Current | Yes |
| `docs/product/OPEN-REQUIREMENTS.md` | Unresolved decisions and ambiguities | Current | Yes |
| `docs/product/REQUIREMENTS.md` | Canonical requirement matrix | Current | Yes |
| `docs/product/TRACEABILITY-MATRIX.md` | Requirement → contract/UI → acceptance/test → implementation → release evidence | Current | Yes |
| `docs/product/FEATURE-BACKLOG.md` | Executable implementation-ready backlog only | Current; blocked work excluded | Yes |
| `docs/product/DEPENDENCY-MATRIX.md` | Requirement dependencies and sequencing | Current | Yes |
| `docs/product/REQUIREMENT-GAPS.md` | Vague, contradictory, deferred, or unverifiable requirements | Current | Yes |

## 4. API Documentation

| Artifact | Purpose | Status | Source of Truth |
|---|---|---|---|
| `docs/api/API-CONTRACT.md` | Canonical visitor-counter HTTP interface contract | Draft; implementation-ready wire contract, acceptance blocked by OR-001 | Yes |
| `docs/api/API-ENDPOINTS.md` | Public endpoint inventory | Current | Yes |
| `docs/api/API-SCHEMAS.md` | Reusable request/response/error schemas | Current | Yes |
| `docs/api/API-ERRORS.md` | Canonical HTTP/error-code contract | Current | Yes |
| `docs/api/API-VARIABLES.md` | Path/query/header/body variable definitions | Current | Yes |
| `docs/api/API-EXAMPLES.md` | Representative HTTP examples | Current | Yes |
| `docs/api/API-CHANGELOG.md` | API contract decisions and version history | Current | Yes |
| `docs/api/openapi.yaml` | Machine-readable OpenAPI 3.0.3 contract | Current | Yes |

## 5. Architecture Documentation

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

## 6. Canonical Repository Names

| Repository | Purpose | Status |
|---|---|---|
| `s1xte3n/sixteen-resume-frontend` | Frontend resume application and documentation | Exists |
| `s1xte3n/sixteen-resume-backend` | Backend/API/IaC application | Exists; implementation state must be verified |

Historical names `sixteen-frontend` and `sixteen-backend` are obsolete and must not be used in new requirements.

## 7. Requirements System Status

**Status: Traceability baseline complete; requirements closure pending.**

Coverage now includes:

- 16 canonical MVP requirements.
- Cross-cutting security, cost, region, Git, and IaC requirements.
- Unique priority and status for each requirement.
- Dependencies and affected components.
- Acceptance-criteria mapping.
- Verification IDs (`VT-*`).
- Requirement-to-contract/UI-to-test-to-implementation-to-release traceability.
- Executable backlog containing only implementation-ready items.
- Explicit gap register for unresolved requirements.

## 8. Current P1 Blockers

1. OR-001 — Visitor-count semantics.
2. OR-002 — Free hostname versus custom-domain interpretation.
3. OR-003 — Numeric cost ceiling.
4. OR-004 — HTTPS/CDN configuration and cost validation.
5. OR-005 — Final public resume-content approval.
6. Repository/branch state normalization where it affects CI/CD evidence.

## 9. Current P2/P3 Decisions

- OR-006 — Python test framework, intentionally deferred.
- OR-007 — Blog-platform interpretation/normalization.
- OR-008 — Visitor API contract: **resolved by API v1 contract; acceptance remains blocked by OR-001**.
- OR-009 — Counter failure UX.
- OR-010 — Browser support baseline.
- OR-011 — Availability target.
- OR-012 — DNS propagation/stability expectation.
- OR-013 — Blog link tab behavior.

## 10. Implementation Artifact Status

| Artifact | Status |
|---|---|
| HTML resume | Not started |
| CSS | Not started |
| JavaScript visitor counter | Blocked by visitor semantics/API contract/failure UX |
| Azure Storage | Not started |
| HTTPS/CDN | Blocked by cost and delivery validation |
| DNS hostname | Blocked by hostname interpretation |
| Cosmos DB | Not started |
| Azure Function | Not started |
| Python implementation | Not started |
| Python tests | Blocked by test-framework decision |
| ARM templates | Not started |
| Backend GitHub Actions | Blocked by CI/repository/authentication decisions |
| Frontend GitHub Actions | Blocked by delivery/repository decisions |
| Production deployment | Blocked by P1 requirements |
| Blog content | Not started |
| Public resume content approval | Pending OR-005 |
| API contract | Draft; wire contract frozen for v1; acceptance blocked by OR-001 |\n| OpenAPI specification | Current; synchronized with API v1 |\n| Architecture | Proposed; not frozen |

## 11. Governance Rules

When a requirement or decision changes:

1. Update `PRD.md`.
2. Update `OPEN-REQUIREMENTS.md` / `REQUIREMENT-GAPS.md` as applicable.
3. Update `SCOPE.md` when scope changes.
4. Synchronize `USER-STORIES.md` and `ACCEPTANCE-CRITERIA.md` when behavior/acceptance changes.
5. Synchronize `REQUIREMENTS.md`, `TRACEABILITY-MATRIX.md`, and `DEPENDENCY-MATRIX.md`.
6. Update `FEATURE-BACKLOG.md` only when implementation becomes ready.
7. Record significant decisions in `DECISIONS.md`.
8. Update `PROJECT-STATUS.md` for implementation-state changes.
9. Never claim completion without evidence.

## 12. Gate Status

### PRD Gate

**NOT CLOSED.** Every MVP requirement now has acceptance criteria and a verification path, but P1 decisions remain unresolved.

### Requirements Gate

**NOT CLOSED.** The traceability system is established, but the following prevent requirements closure: unresolved P1 product decisions, unresolved P2 API/testing/blog decisions where they affect acceptance, and repository/branch-state evidence that must match the canonical Git model.

### Architecture Gate

**NOT FROZEN.** Architecture depends on unresolved visitor semantics, hostname interpretation, cost ceiling, HTTPS/CDN validation, API contract, and related decisions.

## 13. No-Task Rule

No implementation task is created for a requirement that remains ambiguous, contradictory, or objectively unverifiable. Such requirements remain in `REQUIREMENT-GAPS.md` until formally resolved.
