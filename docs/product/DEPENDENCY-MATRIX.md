# Requirement Dependency Matrix

## 1. Purpose

This matrix defines requirement-to-requirement dependencies, blocking decisions, and sequencing. It is derived from the canonical requirements baseline and prevents downstream work from being treated as complete while upstream behavior remains unresolved.

## 2. Canonical Dependency Matrix

| Requirement | Depends on | Dependency type | Blocking? | Sequence |
|---|---|---|---|---:|
| REQ-AZ-001 | OR-005; REQ-AZ-002..006 | Content/product | No — implementation-ready; owner approval remains an acceptance gate | 1 |
| REQ-AZ-002 | REQ-AZ-001 | Content/UI | Yes | 2 |
| REQ-AZ-003 | REQ-AZ-002 | UI | Yes | 3 |
| REQ-AZ-004 | REQ-AZ-002, REQ-AZ-003 | Hosting | Yes | 4 |
| REQ-AZ-005 | REQ-AZ-004, REQ-AZ-006; OR-004 | No — implementation-ready; edge/cost validation remains | 7 |
| REQ-AZ-006 | REQ-AZ-005; OR-002 | No — implementation-ready; hostname creation/validation remains | 6 |
| REQ-AZ-007 | REQ-AZ-008..010; OR-001, OR-008, OR-009 | No — implementation-ready; atomic persistence evidence remains | 12 |
| REQ-AZ-008 | REQ-AZ-009, REQ-AZ-010; OR-001, OR-008 | No — implementation-ready; atomic persistence evidence remains | 11 |
| REQ-AZ-009 | REQ-AZ-010; OR-008 | No — implementation-ready; approved API contract remains the implementation source | 10 |
| REQ-AZ-010 | REQ-AZ-011 | Backend/test governance | No for foundation; yes for final CI-gated acceptance | 9 |
| REQ-AZ-011 | REQ-AZ-010, REQ-AZ-013; OR-006 | Test/CI | Yes | 13 |
| REQ-AZ-012 | REQ-AZ-004, REQ-AZ-008, REQ-AZ-010; approved architecture | IaC | Yes | 14 |
| REQ-AZ-013 | REQ-AZ-011, REQ-AZ-012; repository/authentication state | No — implementation-ready; CI/CD implementation remains | 15 |
| REQ-AZ-014 | REQ-AZ-004, REQ-AZ-005; repository/delivery state | No — implementation-ready; CI/CD implementation remains | 16 |
| REQ-AZ-015 | REQ-AZ-001..014; OR-001..OR-005 | No — implementation-ready; production deployment remains | 18 |
| REQ-AZ-016 | REQ-AZ-001; OR-007 | Content/external | No | 17 |

## 3. Cross-Cutting Dependencies

| Requirement | Depends on | Reason |
|---|---|---|
| REQ-AZ-SEC-001 | CI/CD and repository configuration | Secrets must be injected securely, not committed. |
| REQ-AZ-SEC-002 | REQ-AZ-009 | The API is the database security boundary. |
| REQ-AZ-SEC-003 | REQ-AZ-012..014 | Least privilege depends on actual resource and deployment architecture. |
| REQ-AZ-SEC-004 | REQ-AZ-005 | HTTPS depends on final delivery configuration. |
| REQ-AZ-COST-001 | Approved cost policy | Numeric ceiling is now fixed at R100/month recurring Azure/cloud cost; R0/month preferred, with documented exclusions. |
| REQ-AZ-REG-001 | REQ-AZ-012 | Resource locations are validated from IaC. |
| REQ-AZ-GIT-001 | Repository/branch normalization | Branch model must match actual canonical repositories. |
| REQ-AZ-DEV-001 | REQ-AZ-012 | Reproducibility depends on ARM coverage. |
| REQ-AZ-DEV-002 | OR-005 | Certification representation is part of final public-content approval. |

## 4. Blocking Decisions

| Decision | Blocks |
|---|---|
| OR-001 Visitor semantics | None — resolved; implementation must still satisfy the defined semantics |
| OR-002 Hostname interpretation | None — resolved; hostname provisioning/validation remains |
| OR-003 Numeric cost ceiling | None — resolved |
| OR-004 HTTPS/CDN configuration | None — resolved; edge-service/cost validation remains |
| OR-005 Public resume approval | None as a requirements-definition blocker; final owner approval remains an acceptance gate |
| OR-006 Test framework | REQ-AZ-011, REQ-AZ-013 |
| OR-007 Blog publication interpretation | REQ-AZ-016 |
| OR-008 API contract | REQ-AZ-007..010 |
| OR-009 Counter failure UX | REQ-AZ-007, REQ-AZ-009 |
| Repository naming/state normalization | REQ-AZ-013, REQ-AZ-014 |

## 5. Recommended Sequencing

### Phase A — Requirements closure
1. OR-001 through OR-005 are resolved at the requirements-definition level; retain their documented implementation/acceptance gates.
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
