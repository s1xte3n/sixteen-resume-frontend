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
| `docs/architecture/ARCHITECTURE.md` | Logical/system architecture | Implementation-aligned; live Azure verification pending |
| `docs/architecture/DATA-MODEL.md` | Persistent data model | Proposed |
| `docs/architecture/SECURITY-ARCHITECTURE.md` | Security boundaries and controls | Flex identity/RBAC alignment documented; live verification pending |
| `docs/architecture/INFRASTRUCTURE.md` | Azure resource/environment architecture | Flex implementation-aligned; live Azure verification pending |
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
| `s1xte3n/sixteen-resume-backend` | Backend/API/IaC application | Exists; Phase 2 Flex Consumption IaC, RBAC, package deployment workflow and validation tests implemented on feature branch; Azure/OIDC execution evidence pending |

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

## Phase 1 artifacts
| Artifact | Status |
| docs/product/PRD.md | Flex re-baselined |
| docs/product/REQUIREMENTS.md | REQ-AZ-FLEX-001..013 added |
| docs/product/ACCEPTANCE-CRITERIA.md | AC-FLEX-001..013 added |
| docs/product/DEPENDENCY-MATRIX.md | Flex dependencies added |
| docs/product/TRACEABILITY-MATRIX.md | Flex traceability added |
| docs/product/REQUIREMENT-GAPS.md | Flex gaps classified/closed/deferred |
| docs/product/SCOPE.md | Flex hosting scope updated |
| docs/product/USER-STORIES.md | Flex story mapping added |
| docs/project/PROJECT-STATUS.md | Phase 1 status updated |
Backend infra/azure/azuredeploy.json remains the superseded Y1 implementation and is not a Phase 1 implementation artifact. Phase 2 must replace it.
Backend tests containing Y1 assertions are stale implementation evidence and must be replaced in Phase 2. Phase 1 does not modify application/test implementation.


## Phase 2 Implementation Artifacts

| Artifact | Status |
|---|---|
| Backend Flex ARM template | Implemented on phase-2/flex-consumption-infrastructure branch |
| Backend Flex ARM structural tests | Implemented; execution evidence pending |
| Backend Flex deployment workflow | Implemented; live OIDC/Azure evidence pending |
| Backend Flex validation documentation | Implemented |
| Backend package deployment | Implemented using supported Flex package-deployment tooling |
| Runtime managed identity/RBAC | Defined in ARM; live Azure verification pending |
| Deployment storage managed identity/RBAC | Defined in ARM; live Azure verification pending |
| Runtime identity-based host storage | Defined in ARM; live Azure verification pending |
| API contract | Unchanged — GET /api/visitors |

The backend Phase 2 branch is the implementation candidate. No Phase 2 artifact is considered production-proven until authenticated Azure evidence exists.


## Phase 4 continuation — 2026-10-07

Backend Phase 4 verification has advanced past the ARM template validation defects. The backend ARM template now validates successfully against the approved production resource group and parameters. Production deployment/runtime evidence remains blocked by the unresolved GitHub Actions OIDC subscription authorization result.

Frontend artifacts remain implementation-aligned but production acceptance is still gated on authenticated backend deployment, live API verification, browser/API isolation, CORS, security, and cost evidence. No frontend architecture or API contract change was made as part of the Phase 4 ARM correction.


## Phase 4 continuation — 2026-10-07

Backend ARM validation defects are resolved and the current production blocker is now deployment-identity RBAC: the GitHub Actions service principal reaches ARM but lacks `Microsoft.Authorization/roleAssignments/write` at `rg-sixteen-resume-prod`. Frontend production acceptance remains blocked and no frontend implementation change is authorized for this blocker.

Required next evidence remains a fresh successful backend production workflow execution followed by the defined end-to-end frontend verification. Documentation must not mark production deployment, API, persistence, isolation, CORS, security, or cost as passed before direct evidence exists.

## Phase 4 continuation — FC1 instance memory requirement — 2026-10-07

The latest controlled backend production deployment reached the Function App resource but Azure rejected the Flex `functionAppConfig.scaleAndConcurrency` configuration because `instanceMemoryMB` was not explicitly set. Azure reported the supported values as 512, 2048, and 4096 MB.

The backend correction sets `instanceMemoryMB` to **512 MB**, the lowest provider-supported value, while retaining `alwaysReady: []` for zero always-ready instances and scale-to-zero. No frontend architecture, API contract, credentials, direct Cosmos access, CDN/cache path, or deployment mechanism changes as a result.

Frontend production acceptance remains **BLOCKED** until the corrected backend passes CI and a fresh production workflow from `main` completes the required deployment, runtime, API, persistence/concurrency, isolation, CORS, security, observability, and cost evidence.
