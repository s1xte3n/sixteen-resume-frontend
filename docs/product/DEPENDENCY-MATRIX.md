# Requirement Dependency Matrix

## 1. Purpose

This matrix defines requirement-to-requirement dependencies, blocking decisions, and sequencing. It is derived from the canonical requirements baseline and prevents downstream work from being treated as complete while upstream behavior remains unresolved.

## 2. Canonical Dependency Matrix

| Requirement | Depends on | Dependency type | Blocking? | Sequence |
|---|---|---|---|---:|
| REQ-AZ-001 | OR-005; REQ-AZ-002..006 | Content/product | Yes | 1 |
| REQ-AZ-002 | REQ-AZ-001 | Content/UI | Yes | 2 |
| REQ-AZ-003 | REQ-AZ-002 | UI | Yes | 3 |
| REQ-AZ-004 | REQ-AZ-002, REQ-AZ-003 | Hosting | Yes | 4 |
| REQ-AZ-005 | REQ-AZ-004, REQ-AZ-006 | Delivery/cost | Yes | 7 |
| REQ-AZ-006 | REQ-AZ-005 | DNS/delivery | Yes | 6 |
| REQ-AZ-007 | REQ-AZ-008..010; OR-001, OR-008, OR-009 | Application | Yes | 12 |
| REQ-AZ-008 | REQ-AZ-009, REQ-AZ-010; OR-001, OR-008 | Persistence/API | Yes | 11 |
| REQ-AZ-009 | REQ-AZ-010; OR-008 | API | Yes | 10 |
| REQ-AZ-010 | REQ-AZ-011 | Backend/test governance | No for foundation; yes for final CI-gated acceptance | 9 |
| REQ-AZ-011 | REQ-AZ-010, REQ-AZ-013; OR-006 | Test/CI | Yes | 13 |
| REQ-AZ-012 | REQ-AZ-004, REQ-AZ-008, REQ-AZ-010; approved architecture | IaC | Yes | 14 |
| REQ-AZ-013 | REQ-AZ-011, REQ-AZ-012; repository/authentication state | Backend CI/CD | Yes | 15 |
| REQ-AZ-014 | REQ-AZ-004, REQ-AZ-005; repository/delivery state | Frontend CI/CD | Yes | 16 |
| REQ-AZ-015 | REQ-AZ-001..014; OR-001..OR-005 | End-to-end | Yes | 18 |
| REQ-AZ-016 | REQ-AZ-001; OR-007 | Content/external | No | 17 |

## 3. Cross-Cutting Dependencies

| Requirement | Depends on | Reason |
|---|---|---|
| REQ-AZ-SEC-001 | CI/CD and repository configuration | Secrets must be injected securely, not committed. |
| REQ-AZ-SEC-002 | REQ-AZ-009 | The API is the database security boundary. |
| REQ-AZ-SEC-003 | REQ-AZ-012..014 | Least privilege depends on actual resource and deployment architecture. |
| REQ-AZ-SEC-004 | REQ-AZ-005 | HTTPS depends on final delivery configuration. |
| REQ-AZ-COST-001 | Approved US$5/month recurring cloud/service ceiling | Cost acceptance is objectively testable against the approved threshold. |
| REQ-AZ-REG-001 | REQ-AZ-012 | Resource locations are validated from IaC. |
| REQ-AZ-GIT-001 | Repository/branch normalization | Branch model must match actual canonical repositories. |
| REQ-AZ-DEV-001 | REQ-AZ-012 | Reproducibility depends on ARM coverage. |
| REQ-AZ-DEV-002 | OR-005 | Certification representation is part of final public-content approval. |

## 4. Blocking Decisions

| Decision | Blocks |
|---|---|
| OR-001 Visitor semantics | REQ-AZ-007, REQ-AZ-008, REQ-AZ-009, REQ-AZ-015 |
| OR-005 Public resume approval | REQ-AZ-001, REQ-AZ-015 |
| OR-006 Test framework | REQ-AZ-011, REQ-AZ-013 |
| OR-007 Blog publication interpretation | REQ-AZ-016 |
| OR-008 API contract | REQ-AZ-007..010 |
| OR-009 Counter failure UX | REQ-AZ-007, REQ-AZ-009 |
| Repository naming/state normalization | REQ-AZ-013, REQ-AZ-014 |

## 5. Recommended Sequencing

### Phase A — Requirements closure
1. Resolve OR-001 through OR-005.
2. Resolve OR-008 and OR-009 sufficiently for objective counter acceptance.
3. Resolve repository/branch naming and actual repository state.
4. Normalize OR-007 against the approved Dev.to/Hashnode decision.
5. Resolve OR-006 before final CI acceptance.

### Phase B — Frontend foundation
6. REQ-AZ-002.
7. REQ-AZ-003.
8. REQ-AZ-004.
9. REQ-AZ-014 when delivery/repository prerequisites are stable.

### Phase C — Backend foundation
10. REQ-AZ-010.
11. REQ-AZ-008.
12. REQ-AZ-009.
13. REQ-AZ-011.
14. REQ-AZ-012.
15. REQ-AZ-013.

### Phase D — Delivery and integration
16. REQ-AZ-005.
17. REQ-AZ-006.
18. REQ-AZ-007.
19. REQ-AZ-015.

### Phase E — Content completion
20. REQ-AZ-016.

## 6. Dependency Rule

A downstream requirement must not be marked complete when an upstream requirement materially determines its behavior and remains unresolved. Parallel preparation is permitted only when the unresolved dependency cannot change the interface, acceptance criteria, security boundary, cost, or architecture.
