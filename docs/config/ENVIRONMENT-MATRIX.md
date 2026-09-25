# Environment Matrix

## Model

There is one actual Azure deployment environment: **Production**. Local, dev, test, and staging are controlled execution/validation contexts and do not imply additional Azure environments.

| Requirement | Local | Dev | Test | Staging | Prod |
|---|---|---|---|---|---|
| Azure deployment | No | No | No | No | **Yes** |
| Purpose | Developer execution | Integration/Git context | Automated verification | Optional pre-release validation context | Public service |
| Public hostname (`PUBLIC_HOSTNAME`) | No | No | No | No | Required (FreeDNS hosted hostname) |
| HTTPS | Optional | N/A | N/A | If exercised | Required |
| Exact production CORS | No | No | No | If API exercised | Required |
| Visitor API | Local/mocked | Optional integration | Required for contract tests | If exercised | Required |
| Cosmos DB | Mock/test seam preferred | No dedicated env | Synthetic isolated state | No dedicated env | Required |
| Azure Storage | No | No | No | No | Required |
| CDN/delivery | No | No | No | No | Required |
| DNS | No | No | No | No | Required |
| ARM validation | Recommended | Required | Required | Required if used | Required |
| Python tests | Required before PR | Required | Required | Required if used | Must pass CI |
| Secrets | Local secure store only | CI secure context | Prefer none | No production secrets | Secure GitHub/Azure mechanism |
| Real visitor data | Never | Never | Never | Never | Approved counter only |
| Deployment source | Local | Git/CI | CI | CI if used | GitHub Actions |
| Cost | None | None | None | None | Approved ceiling only |

## Context rules

### Local
No production credentials. Synthetic data only. Secret-bearing .env files remain untracked. Do not copy production CORS or credentials into fixtures.

### Dev
No dedicated Azure dev environment is approved. Dev refers to the development/integration Git context and CI validation.

### Test
Tests are deterministic and synthetic. Unit tests should mock persistence. No production Cosmos entity or credential may be used.

### Staging
No staging Azure environment is approved. A future staging deployment requires explicit scope approval and must not silently become permanent.

### Production
East US; public HTTPS; approved hostname; exact CORS origin; Azure Storage static website; Azure Function Consumption direction; Cosmos DB Table API serverless direction; CI/CD-only deployment; no plaintext secrets; ARM as source of truth.

## Production configuration evidence gate

**Status: NOT YET VERIFIED.**

The matrix defines the required configuration, but production is not environment-ready until live evidence exists for:

1. GitHub production environment.
2. AZURE_CLIENT_ID, AZURE_TENANT_ID, AZURE_SUBSCRIPTION_ID.
3. Production environment variables required by the verification workflow.
4. Azure federated identity credential.
5. Managed identity ↔ GitHub OIDC relationship.
6. Managed identity ↔ production Storage RBAC relationship.
7. Successful .github/workflows/verify-azure-oidc.yml execution.
8. Deployed API endpoint for Postman environment configuration.

A repository workflow can validate these conditions, but the presence of the workflow is not evidence that the conditions have passed.

## Postman deployed-environment rule

tests/postman/sixteen-resume-environment-template.json is the safe committed template and remains local-by-default.

After the API is deployed:
- create/update a local, uncommitted deployed environment;
- set apiBaseUrl to the actual deployed API origin;
- keep apiPath=/api/visitors;
- set `publicOrigin` to `https://<PUBLIC_HOSTNAME>` for the approved frontend origin;
- use a UUID-v4 requestId when testing request correlation;
- never add Azure credentials, Cosmos credentials, Function keys, or connection strings;
- execute the API collection against the deployed endpoint and retain the run as implementation evidence.

The deployed Postman environment is generated operational state, not a committed repository artifact.

## Promotion gates

1. Python tests pass.
2. ARM/IaC validation passes.
3. Secret scanning passes.
4. Frontend validation passes.
5. API contract validation passes where applicable.
6. No unresolved P1 decision is silently overridden.
7. Production configuration exists in the secure deployment context.
8. Hostname/CORS/CDN capability decisions are approved and the selected delivery service passes implementation validation.
9. Public resume content definition is resolved; final owner approval is required before production acceptance.
10. OIDC deployment identity and Function managed-identity/RBAC configuration are validated.

Environment differences must be configuration, not code forks. Production values must not be copied into test data.
