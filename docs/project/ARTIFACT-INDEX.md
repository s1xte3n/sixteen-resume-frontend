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
| `docs/product/PRD.md` | Complete product requirements and feature specifications | Complete; requirements-definition closure complete | Yes |
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
| `docs/api/API-CONTRACT.md` | Canonical visitor-counter HTTP interface contract | Frozen MVP interface; implementation evidence pending | Yes |
| `docs/api/API-ENDPOINTS.md` | Public endpoint inventory | Current | Yes |
| `docs/api/API-SCHEMAS.md` | Reusable request/response/error schemas | Current | Yes |
| `docs/api/API-ERRORS.md` | Canonical HTTP/error-code contract | Current | Yes |
| `docs/api/API-VARIABLES.md` | Path/query/header/body variable definitions | Current | Yes |
| `docs/api/API-EXAMPLES.md` | Representative HTTP examples | Current | Yes |
| `docs/api/API-CHANGELOG.md` | API contract decisions and version history | Current | Yes |
| `docs/api/openapi.yaml` | Machine-readable OpenAPI 3.0.3 contract | Current | Yes |

## 5. Configuration and Test Data Documentation

| Artifact | Purpose | Status |
|---|---|---|
| `docs/config/ENVIRONMENT-VARIABLES.md` | Canonical non-secret environment/configuration inventory | Complete |
| `docs/config/ENVIRONMENT-MATRIX.md` | Local/dev/test/staging/prod context requirements | Complete |
| `docs/config/SECRETS-MANAGEMENT.md` | Secret names, sources, rotation, ownership, and handling rules | Complete; values excluded |
| `docs/config/TEST-DATA.md` | Synthetic API/database test state and lifecycle | Complete |
| `tests/postman/sixteen-resume-environment-template.json` | Non-secret Postman environment template | Complete |
| `docs/ci-cd/OIDC-SETUP.md` | Frontend GitHub Actions → Azure OIDC configuration and verification procedure | Complete |
| `docs/ci-cd/CI-CD-READINESS.md` | Frontend CI/CD operational readiness and evidence gate | Complete |
| `.github/workflows/verify-azure-oidc.yml` | Manual production-environment OIDC and Storage RBAC verification workflow | Implemented; execution evidence **BLOCKED** |
| `.github/workflows/deploy-frontend.yml` | Production frontend deployment via OIDC to Azure Storage with HTTPS smoke test | Implemented; live execution/evidence **BLOCKED** |

## 6. Architecture Documentation

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
| `docs/architecture/ADR-006.md` | HTTPS/CDN architecture | Accepted at capability level; service validation pending |
| `docs/architecture/ADR-007.md` | Visitor-count semantics | Accepted |

## 7. Canonical Repository Names

| Repository | Purpose | Status |
|---|---|---|
| `s1xte3n/sixteen-resume-frontend` | Frontend resume application and documentation | Exists |
| `s1xte3n/sixteen-resume-backend` | Backend/API/IaC application | Exists; Phase 7.2 persistence and Phase 7.3 core ARM IaC implemented on feature branch; Azure deployment/OIDC evidence pending |

Historical names `sixteen-frontend` and `sixteen-backend` are obsolete and must not be used in new requirements.

## 8. Requirements System Status

**Status: Requirements-definition baseline CLOSED; Phase 7 implementation evidence pending.**

Coverage includes:

- 16 canonical MVP requirements.
- Cross-cutting security, cost, region, Git and IaC requirements.
- Unique priority and status for each requirement.
- Dependencies and affected components.
- Acceptance criteria.
- Verification IDs.
- Requirement-to-contract/UI/test/implementation/release traceability.
- Deliberate challenge deviations.
- Explicit implementation and production-acceptance gates.

### Requirements-definition decisions

| Decision | Status |
|---|---|
| Visitor semantics | Resolved |
| Public hostname interpretation | Resolved |
| R100/month recurring cost ceiling | Resolved |
| HTTPS/CDN capability architecture | Resolved at capability level |
| Public resume content definition | Resolved; final owner approval remains acceptance evidence |
| API contract | Resolved |
| Persistence/concurrency semantics | Resolved |
| CI/CD authority | Resolved |
| Production branch authority | Resolved |
| Browser baseline | Resolved |
| DNS acceptance | Resolved |

---

## 9. Current Implementation / Acceptance Gates

These are implementation or production-acceptance gates rather than unresolved requirements:

1. Select and validate the exact Azure HTTPS/CDN delivery service.
2. Provision the approved FreeDNS hostname.
3. Implement Azure Storage.
4. Implement Cosmos DB Table API.
5. Implement Python Azure Function.
6. Implement concurrency-safe counter persistence.
7. Implement ARM infrastructure — core Azure resources now represented in the backend ARM template; live Azure validation and the ADR-006 edge-service resource remain pending.
8. Implement backend GitHub Actions.
9. Complete frontend GitHub Actions deployment workflow — implementation complete; live execution evidence remains BLOCKED.
10. Implement frontend visitor-counter JavaScript — implementation complete; live API/production verification remains BLOCKED.
11. Execute API, persistence, concurrency, browser, security and deployment tests.
12. Obtain final public HTML resume owner approval.
13. Validate complete MVP recurring cost <= R100/month.

---

## 10. Testing Artifacts

| Artifact | Status |
|---|---|
| `docs/testing/TEST-STRATEGY.md` | Complete — execution evidence pending implementation |
| `docs/testing/TEST-MATRIX.md` | Complete |
| `docs/testing/TEST-DATA-PLAN.md` | Complete |
| `docs/testing/TEST-CASES.md` | Complete — execution pending implementation |
| `docs/testing/TEST-PRIORITIES.md` | Complete |
| `docs/testing/RELEASE-GATES.md` | Complete |
| `tests/postman/sixteen-resume-API.postman_collection.json` | Complete — execution pending backend implementation |
| `tests/postman/sixteen-resume-environment-template.json` | Complete |

No API test is considered passed until the backend exists and the assertions verify status, schema, business behavior, persistence and security as applicable.

---

## 11. Implementation Artifact Status

| Artifact | Status |
|---|---|
| HTML resume | Candidate exists; implementation/approval pending |
| CSS | Not started |
| JavaScript visitor counter | Not started |
| Azure Storage | ARM-defined backend resource; live deployment verification **BLOCKED** |
| HTTPS/CDN | Architecture capability resolved; service selection pending implementation |
| DNS hostname | Provider selected; hostname provisioning pending |
| Cosmos DB | ARM-defined serverless Table API; live deployment/RBAC verification **BLOCKED** |
| Azure Function | ARM-defined Python Linux Consumption app; live runtime verification **BLOCKED** |
| Python implementation | Phase 7.1 foundation implemented; local HTTP contract and persistence tests present |
| Python tests | Phase 7.1 unit, persistence, concurrency and HTTP contract tests implemented |
| ARM template | Phase 7.3 core ARM infrastructure implemented in `s1xte3n/sixteen-resume-backend/infra/azure/azuredeploy.json`; Azure validation/deployment pending |
| Backend GitHub Actions | Phase 7.1 workflow implemented and extended with ARM structural validation; execution/deployment evidence pending |
| Frontend GitHub Actions | PR CI `validate` and production deployment workflow implemented; live execution evidence **BLOCKED** |
| Production deployment | **BLOCKED** — live Azure deployment/runtime evidence unavailable in current environment |
| Blog content | Not started |
| Public resume owner approval | Pending |
| API contract | Frozen v1 |
| OpenAPI specification | Current |
| Architecture | Implementation-ready with edge-service validation gate |

---

## 12. Repository Status

| Repository | Status |
|---|---|
| `s1xte3n/sixteen-resume-frontend` | Exists |
| `s1xte3n/sixteen-resume-backend` | Exists; Phase 7.1 backend foundation implemented; later IaC/deployment work pending |

The backend repository is not considered implementation-complete merely because the GitHub repository exists. Phase 7.3 core ARM artifacts are implemented, but live Azure validation/deployment and production evidence remain required.

---

## 13. Governance Rules

When a requirement changes:

1. Update `docs/product/OPEN-REQUIREMENTS.md`.
2. Update affected requirements.
3. Update acceptance criteria.
4. Update traceability.
5. Update architecture/ADR documentation if necessary.
6. Update test coverage.
7. Update implementation backlog.
8. Update project status.
9. Never claim completion without evidence.

---

## 14. Gate Status

### Project Ready Gate

**CLOSED**

Scope, constraints, repositories, deviations and implementation boundaries are defined.

### PRD Ready Gate

**CLOSED**

All MVP requirements have acceptance criteria and verification paths. No P0/P1 requirement ambiguity remains.

### Requirements Ready Gate

**CLOSED**

Requirements-definition decisions are resolved.

### Architecture Ready Gate

**CLOSED FOR IMPLEMENTATION**

The architecture is frozen at the required capability level. Exact Azure edge-service selection remains an implementation validation task constrained by the approved architecture and R100/month ceiling.

### Test Strategy Ready Gate

**CLOSED**

Test strategy, matrix, data plan, cases, priorities and release gates are defined.

### Phase 7 Entry

**IN PROGRESS — PHASE 7.3**

The backend foundation and executable VC-001 HTTP contract are implemented in `s1xte3n/sixteen-resume-backend`. Local validation is established with pytest, Azurite persistence/concurrency tests, and an HTTP contract suite against the Functions host. Backend CI is implemented and awaits its first GitHub Actions execution/evidence.

Phase 7.1 does not provision production Azure resources, ARM infrastructure, managed-identity RBAC, or production deployment; those remain subsequent implementation work.

---


### Phase 5 — Configuration / Environment Readiness

**NOT YET PASSED — CONFIGURATION DEFINITION COMPLETE; LIVE PRODUCTION EVIDENCE PENDING**

Phase 5 configuration design is complete, but the environment gate is not passed until live production configuration is verified.

### Complete configuration-definition evidence

- docs/config/ENVIRONMENT-VARIABLES.md
- docs/config/ENVIRONMENT-MATRIX.md
- docs/config/SECRETS-MANAGEMENT.md
- docs/config/TEST-DATA.md
- tests/postman/sixteen-resume-environment-template.json
- .github/workflows/verify-azure-oidc.yml

### Remaining gate evidence

| Evidence | Status | Verification source |
|---|---|---|
| Generated-variable classification | Complete | ENVIRONMENT-VARIABLES.md |
| GitHub production environment exists | Pending live verification | GitHub repository settings |
| AZURE_CLIENT_ID exists | Pending live verification | GitHub production environment |
| AZURE_TENANT_ID exists | Pending live verification | GitHub production environment |
| AZURE_SUBSCRIPTION_ID exists | Pending live verification | GitHub production environment |
| Required production repository/environment variables exist | Pending live verification | GitHub production environment |
| OIDC federated credential exists | Pending live verification | Azure managed identity |
| OIDC subject/audience match | Pending live verification | verify-azure-oidc.yml |
| Managed identity resolves to AZURE_CLIENT_ID | Pending live verification | verify-azure-oidc.yml |
| Managed identity has approved Storage RBAC | Pending live verification | verify-azure-oidc.yml / Azure RBAC |
| Postman deployed environment | Blocked until API endpoint exists | Implementation/deployment |
| Successful OIDC verification run | Pending | GitHub Actions |

The committed workflow is validation machinery, not validation evidence. The gate passes only after a successful controlled execution against the actual production GitHub/Azure configuration.

## 15. Phase 7 Rule

Phase 7 implementation must not:

- change approved visitor semantics;
- change the API contract without a controlled contract change;
- exceed the R100/month recurring Azure/cloud ceiling;
- introduce direct browser-to-Cosmos access;
- introduce secrets into source control;
- replace ARM with portal-only infrastructure;
- bypass GitHub Actions for production deployment;
- introduce unrelated product features.

All implementation work must remain traceable to an approved requirement or implementation task.


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
