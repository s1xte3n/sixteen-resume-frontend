# Phase 5 — Frontend Environment & Configuration Inventory

Status: **Phase 5 baseline — configuration model complete; live OIDC verification blocked on RBAC/client-ID synchronization**

The frontend is a static HTML/CSS/JavaScript application. Its approved runtime API call is same-origin `/api/visitors`. It does not use a browser-configured API base URL.

## Frontend configuration

| ID | Name | Type | Context | Required | Source/owner | Consumer | Constraints | Secret | Commit |
|---|---|---|---|---|---|---|---|---|---|
| FE-CFG-001 | PUBLIC_HOSTNAME | hostname | production/deployment | Yes | DNS/delivery owner | GitHub deployment workflow | Approved hostname; exact value TBD until edge/DNS path is accepted | No | Name only; deployment value external |
| FE-CFG-002 | VERIFY_PUBLIC_ENDPOINT | boolean | production CI | Yes | Release owner | deploy-frontend.yml / verify-azure-oidc.yml | false until approved edge/DNS exists; true only after acceptance | No | Yes |
| FE-CFG-003 | AZURE_RESOURCE_GROUP_NAME | string | production CI | Yes | Azure/IaC owner | frontend deployment + OIDC verification | `rg-sixteen-resume-prod` | No | Deployment metadata |
| FE-CFG-004 | AZURE_STORAGE_ACCOUNT_NAME | string | production CI | Yes | IaC/Azure | frontend deployment + OIDC verification | `st16resumeweb` | No | Deployment metadata |
| FE-CFG-005 | AZURE_FRONTEND_IDENTITY_NAME | string | production CI | Yes | Azure identity owner | OIDC verification | Approved UAMI name: `sixteen-resume-frontend-github`; live existence currently **BLOCKED**. Current reported OIDC client ID is `d3363a85-4425-4916-a90a-5b8494015450`, but the Azure resource-type/name binding is not yet verified. | No | Deployment metadata |
| FE-CFG-006 | AZURE_FRONTEND_IDENTITY_RESOURCE_GROUP | string | production CI | Yes | Azure identity owner | OIDC verification | Current approved resource-group boundary: `rg-sixteen-resume-prod` | No | Deployment metadata |
| FE-CFG-007 | AZURE_CLIENT_ID | OIDC identifier | production CI | Yes | GitHub/Azure identity owner | azure/login | Must match frontend UAMI client ID | No — identifier only | GitHub production environment variable |
| FE-CFG-008 | AZURE_TENANT_ID | OIDC identifier | production CI | Yes | Azure tenant owner | azure/login | Approved tenant UUID | No — identifier only | GitHub production environment variable |
| FE-CFG-009 | AZURE_SUBSCRIPTION_ID | OIDC identifier | production CI | Yes | Azure subscription owner | azure/login | Approved subscription UUID | No — identifier only | GitHub production environment variable |
| FE-CFG-010 | API path | fixed contract value | runtime | Yes | API contract | browser JavaScript | Exactly `/api/visitors` | No | Frozen in contract/source; not an env variable |
| FE-CFG-011 | API base URL | none | none | No | — | — | Do not introduce; current browser uses same-origin | N/A | N/A |
| FE-CFG-012 | Cosmos credentials | none | all | No | — | — | Browser must never have them | N/A | Must not exist |

## Important correction

The previous frontend configuration documentation listed `PUBLIC_API_BASE_URL`, `PUBLIC_API_PATH`, and `API_VERSION` as application variables. That did not match the approved frontend implementation: `site/script.js` constructs the same-origin `/api/visitors` endpoint. Those variables are therefore **removed from the Phase 5 frontend configuration contract** rather than introduced into the application.

The canonical API path remains the Phase 4 contract value `GET /api/visitors`.

## OIDC identifier classification

`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, and `AZURE_SUBSCRIPTION_ID` are non-secret OIDC identifiers. They belong in the protected GitHub `production` environment, not source files. No client secret is required.

## Current live blocker

The controlled live check reported:

`(ResourceNotFound) ... userAssignedIdentities/sixteen-resume-frontend-github ... rg-sixteen-resume-prod`

The frontend OIDC verification cannot pass until the approved UAMI exists. The missing GitHub variable `AZURE_FRONTEND_IDENTITY_NAME` is a separate GitHub production-environment configuration defect and must also be corrected.

## Production configuration gate

`PUBLIC_HOSTNAME` and the final CORS origin remain unresolved until the approved HTTPS/edge/DNS path is finalized. No guessed hostname is permitted.


## Current OIDC identity record — 2026-10-07

- `AZURE_FRONTEND_IDENTITY_NAME` must be the GitHub production environment variable `sixteen-resume-frontend-github`.
- Previous reported frontend OIDC client ID `d3363a85-4425-4916-a90a-5b8494015450` is superseded by the newly provisioned UAMI client ID `2d19e037-cc57-462c-a950-862f9b8a80e6`.
- Newly provisioned UAMI principal ID: `200b60d9-b05a-4733-81f4-1053834de5c3`.
- The approved UAMI `sixteen-resume-frontend-github` now exists in `rg-sixteen-resume-prod`.
- Its federated credential `github-production` was recreated with the exact production subject `repo:s1xte3n@39813590/sixteen-resume-frontend@1373840239:environment:production` and audience `api://AzureADTokenExchange`.
- GitHub production `AZURE_CLIENT_ID` must now be synchronized to `2d19e037-cc57-462c-a950-862f9b8a80e6`; leaving the old `d3363a85-4425-4916-a90a-5b8494015450` value would make the verifier fail the identity/client-ID equality check.
- Storage Blob Data Contributor for principal `200b60d9-b05a-4733-81f4-1053834de5c3` on `st16resumeweb` is still **unverified/blocked** because local `az role assignment` calls returned `MissingSubscription`.
- Phase 5 remains **NOT PASSED** until client-ID synchronization and Storage RBAC are live-verified.

## Live OIDC subject correction — 2026-10-07

The production GitHub OIDC assertion observed during controlled verification uses the exact subject `repo:s1xte3n@39813590/sixteen-resume-frontend@1373840239:environment:production`. The frontend verifier now derives this form from GitHub owner/repository IDs. The Azure UAMI federated credential must use this exact immutable subject.

Current frontend UAMI: `sixteen-resume-frontend-github`; client ID `2d19e037-cc57-462c-a950-862f9b8a80e6`; principal ID `200b60d9-b05a-4733-81f4-1053834de5c3`.

## 2026-10-07 controlled verification correction

The failed run exposed two separate issues that must not be conflated:

1. **OIDC federation:** the Azure federated credential must exactly match the immutable GitHub subject observed in the live assertion: `repo:s1xte3n@39813590/sixteen-resume-frontend@1373840239:environment:production`.
2. **RBAC verification:** `Storage Blob Data Contributor` authorizes blob data operations but does not grant `Microsoft.Storage/storageAccounts/read`. Therefore `az storage account show` is not a valid least-privilege verification step for the frontend deployment identity. The verification workflow now proves the authenticated client through `az account show` and tests Storage through Entra-authenticated data-plane operations instead.

The frontend deployment workflow was likewise changed to verify static website service properties and the published `$web/index.html` through Entra-authenticated Storage data-plane calls. It no longer requires management-plane Reader access solely for deployment verification.

This is a verification/RBAC-boundary correction only. No API route, frontend runtime contract, persistence model, or authentication architecture changed.