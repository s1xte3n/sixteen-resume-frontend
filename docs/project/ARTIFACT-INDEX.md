# Artifact Index

## 1. Purpose

This document identifies authoritative project documentation, requirements artifacts, implementation artifacts, and their current status.

---

# 2. Project Documentation

| Artifact                               | Purpose                                                                       | Status  | Source of Truth |
| -------------------------------------- | ----------------------------------------------------------------------------- | ------- | --------------- |
| `docs/project/PROJECT-OVERVIEW.md`     | Project purpose, users, scope, constraints, technology, deployment, and goals | Current | Yes             |
| `docs/project/PROJECT-STATUS.md`       | Current implementation state and project status                               | Current | Yes             |
| `docs/project/DECISIONS.md`            | Confirmed decisions and rationale                                             | Current | Yes             |
| `docs/project/UNRESOLVED-QUESTIONS.md` | Discovery/project-level unresolved questions                                  | Current | Yes             |
| `docs/project/ARTIFACT-INDEX.md`       | Documentation governance and artifact inventory                               | Updated | Yes             |

---

# 3. Product Documentation

| Artifact                              | Purpose                                                          | Status  | Source of Truth |
| ------------------------------------- | ---------------------------------------------------------------- | ------- | --------------- |
| `docs/product/PRD.md`                 | Approved product requirements baseline                           | Current | Yes             |
| `docs/product/USER-STORIES.md`        | User stories and use cases                                       | Current | Yes             |
| `docs/product/ACCEPTANCE-CRITERIA.md` | Testable acceptance criteria                                     | Current | Yes             |
| `docs/product/SCOPE.md`               | Scope and exclusions                                             | Current | Yes             |
| `docs/product/OPEN-REQUIREMENTS.md`   | Existing discovery-stage open requirements                       | Current | Supporting      |
| `docs/product/REQUIREMENTS.md`        | Canonical traceable requirement matrix                           | Create  | Yes             |
| `docs/product/TRACEABILITY-MATRIX.md` | Requirement-to-test/implementation/release traceability          | Create  | Yes             |
| `docs/product/FEATURE-BACKLOG.md`     | Implementation-ready backlog                                     | Create  | Yes             |
| `docs/product/DEPENDENCY-MATRIX.md`   | Requirement sequencing and dependency relationships              | Create  | Yes             |
| `docs/product/REQUIREMENT-GAPS.md`    | Ambiguous, contradictory, unverifiable, and missing requirements | Create  | Yes             |

---

# 4. Requirements Governance

The authoritative relationship between the product artifacts is:

```text
PRD
 ↓
REQUIREMENTS.md
 ↓
REQUIREMENT-GAPS.md
 ↓
DEPENDENCY-MATRIX.md
 ↓
FEATURE-BACKLOG.md
 ↓
TRACEABILITY-MATRIX.md
 ↓
Implementation + Tests + CI/CD Evidence
```

`REQUIREMENTS.md` is the canonical requirement identity and priority source.

`REQUIREMENT-GAPS.md` controls requirements that are not implementation-ready.

`FEATURE-BACKLOG.md` contains only implementation-ready work.

`TRACEABILITY-MATRIX.md` provides evidence linkage.

---

# 5. Source Requirements

| Source                                    | Purpose                                    | Status  |
| ----------------------------------------- | ------------------------------------------ | ------- |
| Azure Cloud Resume Challenge requirements | Original challenge baseline                | Current |
| `docs/product/PRD.md`                     | Approved project-specific requirements     | Current |
| Project state                             | Approved project constraints and decisions | Current |
| Supplied CV                               | Resume content source                      | Current |
| `docs/product/ACCEPTANCE-CRITERIA.md`     | Existing acceptance baseline               | Current |

---

# 6. Repository Documentation

| Repository                        | Purpose                                       | Status                       |
| --------------------------------- | --------------------------------------------- | ---------------------------- |
| `s1xte3n/sixteen-resume-frontend` | Frontend resume application and documentation | Exists                       |
| `s1xte3n/sixteen-resume-backend`  | Backend/API/IaC application                   | Planned/verify current state |

Repository naming must be normalized because some older project documentation refers to `sixteen-frontend` and `sixteen-backend`.

---

# 7. Current Implementation Artifacts

| Artifact                       | Status                                    |
| ------------------------------ | ----------------------------------------- |
| HTML resume                    | Not started                               |
| CSS                            | Not started                               |
| JavaScript visitor counter     | Blocked by visitor semantics/API contract |
| Azure Storage                  | Not started                               |
| HTTPS/CDN                      | Blocked by delivery/cost validation       |
| DNS hostname                   | Blocked by hostname interpretation        |
| Cosmos DB                      | Not started                               |
| Azure Function                 | Not started                               |
| Python implementation          | Not started                               |
| Python tests                   | Blocked by test-framework decision        |
| ARM templates                  | Not started                               |
| Backend GitHub Actions         | Blocked by repository/test decisions      |
| Frontend GitHub Actions        | Blocked by repository/delivery decisions  |
| Production deployment          | Blocked by P1 requirements                |
| Blog — Dev.to                  | Not started                               |
| Blog — Hashnode                | Not started                               |
| Public resume content approval | Pending                                   |

---

# 8. Requirements Phase Status

**Status:** Traceability baseline created.

### Requirement count

* 16 canonical MVP requirements
* 8 cross-cutting requirements
* 1 deliberate certification deviation

### Current P1 blockers

1. Visitor-count semantics
2. Free hostname vs custom-domain interpretation
3. Numeric cost ceiling
4. HTTPS/CDN architecture and cost validation
5. Final public resume content
6. Repository naming normalization

### Current P2 blockers/deferred decisions

1. API contract
2. Counter failure UX
3. Python test framework
4. Blog-platform normalization
5. Browser support baseline
6. Availability target
7. DNS propagation expectations

---

# 9. Artifact Status Rules

When a requirement changes:

1. Update `REQUIREMENTS.md`.
2. Update `REQUIREMENT-GAPS.md` if ambiguity exists.
3. Update `DEPENDENCY-MATRIX.md`.
4. Update `TRACEABILITY-MATRIX.md`.
5. Update `FEATURE-BACKLOG.md` only when implementation becomes ready.
6. Update `PROJECT-STATUS.md` when implementation status changes.
7. Record significant decisions in `DECISIONS.md`.
8. Update this artifact index.

No artifact may claim completion without corresponding evidence.

---

# 10. Naming Consistency Rule

The canonical repository naming must be explicitly normalized before CI/CD traceability is closed.

Current evidence contains both:

* `sixteen-frontend`
* `sixteen-backend`

and:

* `sixteen-resume-frontend`
* `sixteen-resume-backend`

The repository supplied for this documentation review is:

`s1xte3n/sixteen-resume-frontend`

Until the naming decision is normalized, CI/CD requirements remain blocked.

---

# 11. Requirements Closure Rule

The requirements phase is closed only when:

* Every MVP requirement has a unique ID.
* Every requirement has a priority.
* Every requirement has dependencies.
* Every requirement has affected components.
* Every requirement has acceptance criteria.
* Every requirement has at least one verification ID.
* P0/P1 ambiguity is resolved or formally accepted as a deviation.
* Contradictions are explicitly resolved.
* Unverifiable requirements receive measurable definitions.
* Traceability connects requirements to implementation and release evidence.

---

# 12. Next Gate

The next gate is **requirements closure**, not implementation.

No new implementation task should be created for the currently blocked P1 requirements until their corresponding gaps are resolved.
