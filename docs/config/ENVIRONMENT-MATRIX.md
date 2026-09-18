# Environment Matrix

## Model

There is one actual Azure deployment environment: **Production**. Local, dev, test, and staging are controlled execution/validation contexts and do not imply additional Azure environments.

| Requirement | Local | Dev | Test | Staging | Prod |
|---|---|---|---|---|---|
| Azure deployment | No | No | No | No | **Yes** |
| Purpose | Developer execution | Integration/Git context | Automated verification | Optional pre-release validation context | Public service |
| Public hostname | No | No | No | No | Required |
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

## Promotion gates

1. Python tests pass.
2. ARM/IaC validation passes.
3. Secret scanning passes.
4. Frontend validation passes.
5. API contract validation passes where applicable.
6. No unresolved P1 decision is silently overridden.
7. Production configuration exists in the secure deployment context.
8. Hostname/CORS/CDN decisions are approved.
9. Public resume content is approved.

Environment differences must be configuration, not code forks. Production values must not be copied into test data.
