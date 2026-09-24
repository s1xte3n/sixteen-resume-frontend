# Environment Variables — Canonical Inventory

## Purpose

Canonical configuration inventory for the Azure Cloud Resume Challenge. Values are environment-specific and never stored here. Secret values are never committed. The project has one actual Azure deployment environment: production; local/dev/test/staging are execution or validation contexts.

## Inventory

| Variable | Class | Type | Required contexts | Source | Validation/default | Commit |
|---|---|---|---|---|---|---|
| APP_ENV | Non-secret | enum | all | process/CI | local/dev/test/staging/prod; local default local | Name only |
| AZURE_REGION | Non-secret | string | Azure contexts | ARM | Must be East US | Yes |
| PUBLIC_API_BASE_URL | Non-secret | URL | all | environment/CI | HTTPS outside local; no trailing slash | Placeholder only |
| PUBLIC_API_PATH | Non-secret | path | all | API contract | Must be /api/visitors | Yes |
| API_VERSION | Non-secret | string | all | API contract | v1 | Yes |
| PUBLIC_HOSTNAME | Non-secret | hostname | production | DNS/delivery | Valid approved hostname; currently unresolved | Placeholder only |
| CORS_ALLOWED_ORIGIN | Non-secret | origin URL | backend CI/prod | deployment config | Exact approved frontend origin; never * in prod | Placeholder only |
| AZURE_RESOURCE_GROUP_NAME | Non-secret | string | Azure contexts | ARM | Azure naming rules | Yes if approved |
| AZURE_STORAGE_ACCOUNT_NAME | Non-secret | string | Azure contexts | ARM/output | Azure naming rules | Yes if approved |
| AZURE_FUNCTION_APP_NAME | Non-secret | string | Azure contexts | ARM/output | Azure naming rules | Yes if approved |
| AZURE_COSMOS_ACCOUNT_NAME | Non-secret | string | Azure contexts | ARM/output | Azure naming rules | Yes if approved |
| AZURE_COSMOS_TABLE_NAME | Non-secret | string | backend | ARM/application | Valid Table API name | Yes if approved |
| COSMOS_PARTITION_KEY | Non-secret | string | backend/tests | data model | Internal value; never client supplied | Yes if approved |
| COSMOS_ROW_KEY | Non-secret | string | backend/tests | data model | Internal value; never client supplied | Yes if approved |
| COSMOS_ENDPOINT | Non-secret | URL | backend | Azure output | HTTPS Cosmos endpoint | Yes if appropriate |
| FUNCTIONS_WORKER_RUNTIME | Non-secret | string | backend | Azure Functions | python | Yes |
| FUNCTIONS_EXTENSION_VERSION | Non-secret | string | backend | Azure Functions | ~4 unless platform decision changes | Yes |
| LOG_LEVEL | Non-secret | enum | all | app config | DEBUG/INFO/WARNING/ERROR; default INFO | Yes |
| AZURE_SUBSCRIPTION_ID | Identifier | UUID | CI/CD | GitHub variable/context | Approved subscription UUID | Value no |
| AZURE_TENANT_ID | Identifier | UUID | CI/CD | GitHub variable/context | Tenant UUID | Value no |
| AZURE_CLIENT_ID | Identifier | UUID | CI/CD if selected | GitHub variable/context | Client UUID | Value no |
| AZURE_CLIENT_SECRET | Secret | N/A | None | Not used; OIDC is required | Must not exist | **No** |
| COSMOS_CONNECTION_STRING | Secret | N/A | None | Not used; Function managed identity + Cosmos RBAC | Must not exist | **No** |
| COSMOS_ACCOUNT_KEY | Secret | N/A | None | Not used; Function managed identity + Cosmos RBAC | Must not exist | **No** |
| AZURE_STORAGE_CONNECTION_STRING | Secret | N/A | None | Not used; frontend CI uses federated Azure identity | Must not exist | **No** |

## Contract constraints

VC-001 is GET /api/visitors, accepts no request body or query/path parameters, and returns a JSON object containing a non-negative integer `count`. The request does not require `Content-Type`. `Accept: application/json` is recommended. `X-Request-ID` is optional and, when supplied, must be UUID v4. Production CORS is restricted to the approved resume origin. Browser artifacts must never contain Azure/Cosmos credentials.

## Authentication note

ADR-005 is frozen: GitHub Actions uses OIDC workload identity federation with a dedicated Entra user-assigned managed identity; the Function uses its managed identity with Cosmos DB for Table native data-plane RBAC. `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, and `AZURE_SUBSCRIPTION_ID` are identifiers required by the OIDC login configuration and are not secrets. Long-lived client secrets, Cosmos keys, and Storage connection strings are not part of the approved runtime path.

## Ownership

Frontend configuration: frontend owner. Backend runtime configuration: backend owner. Azure resource configuration: ARM/IaC owner. CI/CD credentials: repository/environment administrator. Rotation follows the selected identity mechanism.

## Validation

CI must fail on missing required context variables, non-HTTPS production URLs, wildcard production CORS, API-path drift, unresolved production placeholders, or secrets in tracked/frontend artifacts.
