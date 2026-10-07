# Phase 5 — Frontend Environment & Configuration Inventory

Status: **Phase 5 baseline — configuration model complete; live OIDC provisioning blocked**

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
- Current reported frontend OIDC client ID: `d3363a85-4425-4916-a90a-5b8494015450`.
- The tested Azure command `az identity show --name sixteen-resume-frontend-github --resource-group rg-sixteen-resume-prod` returned `ResourceNotFound`; therefore the reported client ID is **not** sufficient evidence that the required UAMI exists under the approved name/resource group.
- Before creating a second identity, search Azure for the reported client ID and confirm its resource type. If it is not the required UAMI, provision the approved UAMI and bind the new client ID instead.
- Phase 5 remains **NOT PASSED**.