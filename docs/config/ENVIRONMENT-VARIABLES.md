# Phase 5 — Frontend Environment & Configuration Inventory

Status: **Phase 5 baseline — implementation-ready; live production values pending**

The frontend is a static HTML/CSS/JavaScript application. Its approved runtime API call is same-origin `/api/visitors`. It does not use a browser-configured API base URL.

## Frontend configuration

| ID | Name | Type | Context | Required | Source/owner | Consumer | Constraints | Secret | Commit |
|---|---|---|---|---|---|---|---|---|---|
| FE-CFG-001 | PUBLIC_HOSTNAME | hostname | production/deployment | Yes | DNS/delivery owner | GitHub deployment workflow | Approved hostname; exact value TBD until edge/DNS path is accepted | No | Name only; deployment value external |
| FE-CFG-002 | VERIFY_PUBLIC_ENDPOINT | boolean | production CI | Yes | Release owner | deploy-frontend.yml | false until approved edge/DNS exists; true only after acceptance | No | Yes |
| FE-CFG-003 | AZURE_RESOURCE_GROUP_NAME | string | production CI | Yes | Azure/IaC owner | deployment + OIDC verification | Approved production RG | No | Value is deployment metadata |
| FE-CFG-004 | AZURE_STORAGE_ACCOUNT_NAME | string | production CI | Yes | IaC/Azure | deployment + OIDC verification | Must resolve to frontend Storage account | No | Deployment-specific |
| FE-CFG-005 | AZURE_FRONTEND_IDENTITY_NAME | string | production CI | Yes | Azure identity owner | OIDC verification | Dedicated frontend UAMI | No | Deployment-specific |
| FE-CFG-006 | AZURE_FRONTEND_IDENTITY_RESOURCE_GROUP | string | production CI | Yes | Azure identity owner | OIDC verification | RG containing frontend UAMI | No | Deployment-specific |
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

`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, and `AZURE_SUBSCRIPTION_ID` are non-secret OIDC identifiers. They belong in protected GitHub production environment variables, not GitHub Secrets. No client secret is required.

## Production configuration gate

`PUBLIC_HOSTNAME` and the final CORS origin remain unresolved until the approved HTTPS/edge/DNS path is finalized. No guessed hostname is permitted.
