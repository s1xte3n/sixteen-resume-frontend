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
| `docs/api/API-CONSISTENCY-REVIEW.md` | Phase 4 contract consistency, ambiguity, security and QA review | Current | Yes |

## 5. Configuration and Test Data Documentation

| Artifact | Purpose | Status |
|---|---|---|
| `docs/config/ENVIRONMENT-VARIABLES.md` | Canonical frontend configuration inventory aligned to the approved implementation | Updated — Phase 5 |
| `docs/config/ENVIRONMENT-MATRIX.md` | Local/test/CI/deployment/production context matrix | Updated — Phase 5 |
| `docs/config/SECRETS-MANAGEMENT.md` | OIDC identifiers, prohibited credentials, and handling rules | Updated — Phase 5 |
| `docs/config/TEST-DATA.md` | Synthetic frontend test data and lifecycle | Updated — Phase 5 |
| `docs/config/CI-CD-CONFIGURATION.md` | Frontend deployment/OIDC configuration matrix | Added — Phase 5 |
| `docs/config/CONFIGURATION-VALIDATION-RULES.md` | Configuration validation rules | Added — Phase 5 |
| `docs/config/CONFIGURATION-SECURITY-REVIEW.md` | Configuration security findings | Added — Phase 5 |
| `docs/config/CONFIGURATION-CHANGE-LOG.md` | Phase 5 configuration changes | Added — Phase 5 |
| `tests/postman/sixteen-resume-environment-template.json` | Non-secret API-client environment template | Current |

### Phase 5 correction

The frontend runtime does **not** consume `PUBLIC_API_BASE_URL`, `PUBLIC_API_PATH`, or `API_VERSION`. The approved JavaScript uses the same-origin frozen path `/api/visitors`. Those variables are therefore not part of the frontend configuration contract.

Final hostname, HTTPS edge service, final CORS origin, live OIDC/RBAC evidence, and cost evidence remain configuration/acceptance gates.

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
| `docs/architecture/ADR-006.md` | HTTPS/CDN architecture | **Blocked — cost/service feasibility conflict; decision reopened** |
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


## Phase 4 continuation — Flex maximum instance requirement — 2026-10-07

The latest controlled backend deployment advanced to the Function App resource and Azure rejected an empty Flex `maximumInstanceCount`. Azure requires an explicit value in the range 1–1000. The backend correction sets `maximumInstanceCount: 1`, the lowest provider-permitted active-instance ceiling, while retaining `instanceMemoryMB: 512` and `alwaysReady: []`. This is a provider-required configuration correction and does not change the frontend API contract, browser/Cosmos isolation, credentials, CDN/cache architecture, or frontend deployment mechanism.

Frontend production acceptance remains **BLOCKED**. No frontend implementation change is required for this backend infrastructure correction. A fresh successful backend production workflow from `main` remains mandatory before end-to-end frontend/API, CORS, security, and cost evidence can be accepted.


## Phase 4 continuation — Flex worker runtime setting correction — 2026-10-07

Backend production verification identified a provider-level Flex configuration defect: `FUNCTIONS_WORKER_RUNTIME` is invalid for Flex Consumption. The backend ARM template removes that app setting and retains Python 3.12 in `functionAppConfig.runtime`.

No frontend artifact or architecture requires modification for this backend-only correction. Frontend production evidence remains blocked pending a fresh successful backend production workflow and the defined end-to-end acceptance evidence.


## Phase 4 continuation — Cosmos Table RBAC scope correction — 2026-10-07

Backend IaC has been corrected for the current Azure Cosmos DB for Table RBAC provider contract: `tableRoleAssignments.properties.scope` now uses the Cosmos account resource ID rather than the rejected full `/tables/VisitorCounter` resource path. The frontend has no implementation change for this backend-only provider correction. Frontend live deployment, API, browser isolation, CORS, security, and cost evidence remain **BLOCKED** until a fresh successful backend production workflow provides the required dependency evidence.


## Phase 4 continuation — 2026-10-07 — Static website provider correction

The frontend production deployment remains blocked by the shared Azure Storage static website infrastructure owned by the backend ARM deployment. The latest controlled deployment reached the frontend Storage account and Azure rejected the static website request with `InvalidRequestParameters: properties.staticWebsiteEnabled`.

The backend IaC correction is to use the supported `Microsoft.Storage/storageAccounts/blobServices@2025-08-01` API for the static website resource. The approved frontend hosting model is unchanged: Azure Storage static website, public website content, and no CDN/cache-purge service selection beyond the approved project scope.

Frontend application code and deployment credentials are unchanged. A fresh production frontend deployment verification must wait until the backend infrastructure correction is merged and the production workflow proves the static website resource is successfully provisioned.

**Frontend Phase 4 status: BLOCKED — infrastructure dependency.**


## Phase 3 blocker update — 2026-10-07

The Phase 3 architecture deliverables remain aligned with the approved design. Operational blockers are recorded as implementation verification blockers, not architecture changes:

- Frontend GitHub OIDC: Azure federated credential must exactly match the immutable production environment subject presented by GitHub.
- Backend Flex startup: host storage identity configuration requires the documented empty `AzureWebJobsStorage` setting plus Storage Queue Data Contributor RBAC; tracked in backend PR #36.
- No API, frontend application architecture, browser/Cosmos boundary, or hosting-model redesign was introduced.

## Phase 3 blocker — frontend OIDC federated credential — 2026-10-07

Frontend Phase 3 production verification remains **BLOCKED** by the Azure-side federated identity credential for the production GitHub Actions environment. The approved credential must exactly match the GitHub-issued production subject:

`repo:s1xte3n@39813590/sixteen-resume-frontend@1373840239:environment:production`

with issuer `https://token.actions.githubusercontent.com` and audience `api://AzureADTokenExchange`.

This is an external Azure configuration prerequisite. No application, API, Storage deployment, browser/Cosmos, secret, or alternate authentication artifact is changed. The artifact remains unverified until a fresh production OIDC workflow succeeds.


## Phase 3 blocker-correction artifact

| Artifact | Purpose | Status |
|---|---|---|
| `docs/ci-cd/PHASE-3-FRONTEND-UAMI-RECREATION.md` | Exact frontend UAMI, federated credential, narrow Storage RBAC, GitHub production environment binding, exclusions, and verification gate | Current; Azure/GitHub mutation evidence **BLOCKED** |


## Phase 3 blocker resolution update — 2026-10-07

| Artifact | Status | Evidence |
|---|---|---|
| Frontend OIDC / UAMI binding | **RESOLVED** | Production run #33: Azure OIDC login succeeded with the exact immutable production subject |
| Frontend Storage RBAC | **RESOLVED** | Production run #33: Storage upload succeeded with `--auth-mode login` |
| Frontend public HTTPS endpoint | **BLOCKED** | Production run #33: `https://sixteen-resume.mooo.com/` timed out after 20 seconds |
| Backend OIDC binding | **BLOCKED** | Production run #153: `AADSTS700016`; recreated backend client ID must replace the stale GitHub production `AZURE_CLIENT_ID` |
| Backend deployment RBAC | **PENDING VERIFICATION** | Recreated service principal has User Access Administrator; Contributor deployment permission must be verified |
| API / persistence / end-to-end evidence | **BLOCKED BY BACKEND** | Requires fresh successful backend production deployment |

No frontend application code, API contract, browser/Cosmos boundary, or authentication mechanism is changed by these corrections.


## Phase 3 blocker correction — 2026-10-07

- Frontend OIDC and Storage RBAC are already resolved and are not the current Phase 3 blocker.
- The public HTTPS endpoint timeout is caused by the incomplete edge path and the unresolved edge-service decision.
- Azure Front Door Standard is not production-approved because its current fixed base fee conflicts with the hard R100/month recurring Azure/cloud ceiling.
- No frontend application/API contract/browser-Cosmos architecture change is required.


## Phase 3 blocker remediation — 2026-10-07

| Artifact | Status | Change |
|---|---|---|
| `docs/ci-cd/PHASE-3-BLOCKER-STATUS.md` | Updated | Records the separation of Storage deployment verification from the unresolved public edge/DNS path. |
| Frontend Storage deployment | Corrected verification | Azure Storage upload and Storage website reachability are now independently verified. |
| Public HTTPS verification | Blocked | Custom hostname verification is conditional on `VERIFY_PUBLIC_ENDPOINT=true`; it must remain false until the edge/DNS path is actually provisioned. |

No frontend application, API, authentication, or browser/Cosmos boundary change was introduced.


## Phase 3 blocker correction — 2026-10-07

| Area | Current status | Boundary |
|---|---|---|
| GitHub Actions OIDC | **Resolved** | Production environment federated identity now matches the GitHub-issued subject; no application change required. |
| Storage Blob Data Contributor | **Resolved** | Frontend deployment identity is authorized only against `st16resumeweb`; deployment continues to use `--auth-mode login`. |
| Static website endpoint | **Blocked for verification** | The latest deployment attempt timed out while reaching the Azure Storage website endpoint. This is an infrastructure/network verification issue, not a frontend code defect. |
| Public custom hostname | **Blocked** | `sixteen-resume.mooo.com` remains dependent on the approved HTTPS edge/DNS path. |
| Visitor API integration | **Blocked by backend** | End-to-end verification waits for the backend Function/Cosmos production gate. |

No frontend API contract, browser/Cosmos boundary, credential model, or application architecture was changed for these blockers.


## Phase 3 blocker correction — 2026-10-07

| Artifact | Status | Change |
|---|---|---|
| `docs/ci-cd/PHASE-3-BLOCKER-STATUS.md` | Updated | Records the latest Azure Storage static-site reachability timeout as the current frontend infrastructure blocker. |
| Frontend OIDC | Resolved | Production Azure login is no longer the active blocker. |
| Storage Blob Data Contributor | Resolved | Upload authorization is no longer the active blocker. |
| Static website reachability | Blocked | Latest verification timed out before the public site could be accepted. |
| Public custom hostname | Blocked | Remains dependent on the approved HTTPS/DNS edge path. |

No frontend application, API contract, browser/Cosmos boundary, or authentication architecture change was introduced.


## Phase 5 controlled live OIDC verification — 2026-10-07

| Artifact | Status | Purpose |
|---|---|---|
| `docs/config/OIDC-AZURE-LIVE-VERIFICATION.md` | Added — pending live evidence | Controlled manual verification procedure for GitHub → Azure OIDC, frontend UAMI federation, Storage RBAC, and public HTTPS evidence |
| `.github/workflows/verify-azure-oidc.yml` | Corrected — pending execution | Uses protected production environment variables for OIDC identifiers and performs non-deploying Azure verification |

The Phase 5 gate remains **NOT PASSED** until the controlled workflow is executed successfully against the actual protected GitHub production environment and Azure tenant. Workflow existence is not live evidence.


## Phase 5 live OIDC remediation — 2026-10-07

- `docs/config/ENVIRONMENT-VARIABLES.md` — **BLOCKED / live OIDC provisioning pending**; frontend UAMI requirement and missing GitHub environment variable are recorded.
- `docs/config/CI-CD-CONFIGURATION.md` — canonical frontend production variable names recorded.
- `.github/workflows/deploy-frontend.yml` — resource-group variable aligned to `AZURE_RESOURCE_GROUP_NAME`.
- Phase 5 configuration model remains authoritative; no API or browser/Cosmos boundary changed.


## Phase 5 live OIDC correction — 2026-10-07

| Artifact | Status | Change |
|---|---|---|
| `docs/config/ENVIRONMENT-VARIABLES.md` | Updated | Records the current reported frontend client ID `d3363a85-4425-4916-a90a-5b8494015450` and keeps the approved UAMI name explicit. |
| `docs/config/CI-CD-CONFIGURATION.md` | Updated | Clarifies that OIDC identifiers are protected production environment variables and records the missing `AZURE_FRONTEND_IDENTITY_NAME` blocker. |
| `docs/config/OIDC-AZURE-LIVE-VERIFICATION.md` | Updated | Records current live evidence and separates the GitHub-variable blocker from the Azure UAMI blocker. |
| `docs/config/CONFIGURATION-SECURITY-REVIEW.md` | Updated | Keeps frontend OIDC/UAMI binding as a BLOCKER until live evidence passes. |
| Phase 5 gate | **NOT PASSED** | The approved frontend UAMI and GitHub production configuration are not live-verified. |

No frontend application code, API contract, browser/Cosmos boundary, or credential model was changed.

## Phase 5 live OIDC correction — 2026-10-07

| Artifact | Status | Evidence / change |
|---|---|---|
| `docs/config/ENVIRONMENT-VARIABLES.md` | Updated | Records recreated frontend UAMI client/principal IDs and the remaining client-ID/RBAC gate. |
| `docs/config/CI-CD-CONFIGURATION.md` | Updated | Records current protected production variables and the remaining verification blocker. |
| `docs/config/OIDC-AZURE-LIVE-VERIFICATION.md` | Updated | Records corrected federated credential and controlled verification prerequisites. |
| `docs/config/CONFIGURATION-SECURITY-REVIEW.md` | Updated | UAMI provisioning is no longer a blocker; client-ID synchronization and Storage RBAC remain open. |
| `docs/config/CONFIGURATION-CHANGE-LOG.md` | Updated | Records the identity recreation and OIDC correction. |
| Phase 5 gate | **NOT PASSED** | Controlled frontend OIDC workflow must still prove client-ID equality and Storage Blob Data Contributor access. |



## Phase 5 live OIDC correction — 2026-10-07

The controlled run reached Azure login and failed with **AADSTS700213** because Azure had the federated credential subject `repo:s1xte3n/sixteen-resume-frontend:environment:production`, while GitHub presented the immutable subject:

`repo:s1xte3n@39813590/sixteen-resume-frontend@1373840239:environment:production`

This is the authoritative subject observed in the live GitHub OIDC assertion. The verification workflow has been corrected to derive that subject from the GitHub repository owner/repository IDs. The Azure federated credential must be recreated with the exact observed subject before the next verification run.

Current frontend identity evidence:
- UAMI: `sixteen-resume-frontend-github`
- Client ID: `2d19e037-cc57-462c-a950-862f9b8a80e6`
- Principal ID: `200b60d9-b05a-4733-81f4-1053834de5c3`
- GitHub production `AZURE_FRONTEND_IDENTITY_NAME`: configured
- GitHub production `AZURE_CLIENT_ID`: set to the UAMI client ID
- Storage Blob Data Contributor: assigned at `st16resumeweb` scope

**Phase 5 remains NOT PASSED** until a fresh controlled workflow run succeeds through OIDC login, identity matching, federated-credential validation, and Storage data-plane access.
