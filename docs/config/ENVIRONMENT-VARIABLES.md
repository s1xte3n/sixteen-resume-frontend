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
| PUBLIC_HOSTNAME | Non-secret | hostname | production | DNS/delivery | Valid approved FreeDNS hosted hostname; provisioned during implementation | Placeholder only |
| CORS_ALLOWED_ORIGIN | Non-secret | origin URL | backend CI/prod | deployment config | Exact approved frontend origin; never * in prod | Placeholder only |
| AZURE_RESOURCE_GROUP_NAME | Non-secret | string | Azure contexts | ARM | Azure naming rules | Yes if approved |
| AZURE_STORAGE_ACCOUNT_NAME | Non-secret | string | Azure contexts | ARM output; GitHub production environment variable after provisioning | Azure naming rules; must resolve to the approved production Storage account | Yes as a variable name; value is deployment-specific |
| AZURE_RESOURCE_GROUP_NAME | Non-secret | string | CI/CD | ARM output; GitHub production environment variable | Must resolve to the approved production resource group | Yes as a variable name; value is deployment-specific |
| AZURE_FRONTEND_IDENTITY_NAME | Non-secret | string | CI/CD | ARM output; GitHub production environment variable | Must resolve to the dedicated frontend user-assigned managed identity | Yes as a variable name; value is deployment-specific |
| AZURE_FRONTEND_IDENTITY_RESOURCE_GROUP | Non-secret | string | CI/CD | ARM output; GitHub production environment variable | Must resolve to the resource group containing the frontend managed identity | Yes as a variable name; value is deployment-specific |
| AZURE_FUNCTION_APP_NAME | Non-secret | string | Azure contexts | ARM/output | Azure naming rules | Yes if approved |
| AZURE_COSMOS_ACCOUNT_NAME | Non-secret | string | Azure contexts | ARM/output | Azure naming rules | Yes if approved |
| AZURE_COSMOS_TABLE_NAME | Non-secret | string | backend | ARM/application | Valid Table API name | Yes if approved |
| COSMOS_PARTITION_KEY | Non-secret | string | backend/tests | data model | Internal value; never client supplied | Yes if approved |
| COSMOS_ROW_KEY | Non-secret | string | backend/tests | data model | Internal value; never client supplied | Yes if approved |
| COSMOS_ENDPOINT | Non-secret | URL | backend | Azure output | HTTPS Cosmos endpoint | Yes if appropriate |
| FUNCTIONS_WORKER_RUNTIME | Non-secret | string | backend | Azure Functions | python | Yes |
| FUNCTIONS_EXTENSION_VERSION | Non-secret | string | backend | Azure Functions | ~4 unless platform decision changes | Yes |
| LOG_LEVEL | Non-secret | enum | all | app config | DEBUG/INFO/WARNING/ERROR; default INFO | Yes |
| AZURE_SUBSCRIPTION_ID | Identifier | UUID | CI/CD | GitHub production environment secret for OIDC | Must equal the approved Azure subscription UUID | Secret value: no |
| AZURE_TENANT_ID | Identifier | UUID | CI/CD | GitHub production environment secret for OIDC | Must equal the Azure tenant UUID | Secret value: no |
| AZURE_CLIENT_ID | Identifier | UUID | CI/CD | GitHub production environment secret for OIDC | Must equal the dedicated frontend user-assigned managed identity client ID | Secret value: no |
| AZURE_CLIENT_SECRET | Secret | N/A | None | Not used; OIDC is required | Must not exist | **No** |
| COSMOS_CONNECTION_STRING | Secret | N/A | None | Not used; Function managed identity + Cosmos RBAC | Must not exist | **No** |
| COSMOS_ACCOUNT_KEY | Secret | N/A | None | Not used; Function managed identity + Cosmos RBAC | Must not exist | **No** |
| AZURE_STORAGE_CONNECTION_STRING | Secret | N/A | None | Not used; frontend CI uses federated Azure identity | Must not exist | **No** |

## Naming relationship: application configuration vs Postman

`PUBLIC_API_BASE_URL` is the canonical application/runtime configuration variable used by the frontend. It identifies the API origin/base URL.

The committed Postman environment uses `apiBaseUrl` for the same conceptual value because Postman environment variables follow the client's lower-camel-case naming convention. It is **not a second API configuration concept**.

| Consumer | Variable | Meaning |
|---|---|---|
| Frontend/application configuration | `PUBLIC_API_BASE_URL` | Canonical API base/origin used by application code |
| Postman environment | `apiBaseUrl` | Postman representation of `PUBLIC_API_BASE_URL` |
| Postman environment | `apiPath` | Postman representation of `PUBLIC_API_PATH` |

When adding or changing API-base configuration, update the canonical application variable first and then keep the Postman mapping synchronized. Do not introduce another API-base variable without updating this inventory.

## Contract constraints

VC-001 is GET /api/visitors, accepts no request body or query/path parameters, and returns a JSON object containing a non-negative integer `count`. The request does not require `Content-Type`. `Accept: application/json` is recommended. `X-Request-ID` is optional and, when supplied, must be UUID v4. Production CORS is restricted to the approved resume origin. Browser artifacts must never contain Azure/Cosmos credentials.

## Authentication note

ADR-005 is frozen: GitHub Actions uses OIDC workload identity federation with a dedicated Entra user-assigned managed identity; the Function uses its managed identity with Cosmos DB for Table native data-plane RBAC. `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, and `AZURE_SUBSCRIPTION_ID` are identifiers required by the OIDC login configuration and are not secrets. Long-lived client secrets, Cosmos keys, and Storage connection strings are not part of the approved runtime path.

## Ownership

Frontend configuration: frontend owner. Backend runtime configuration: backend owner. Azure resource configuration: ARM/IaC owner. CI/CD credentials: repository/environment administrator. Rotation follows the selected identity mechanism.

## Validation

CI must fail on missing required context variables, non-HTTPS production URLs, wildcard production CORS, API-path drift, unresolved production placeholders, mismatched Azure resource identifiers, OIDC identity/federated-credential mismatch, or secrets in tracked/frontend artifacts.
