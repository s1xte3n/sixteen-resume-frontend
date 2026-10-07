# Phase 5 — Configuration Change Log

| Date | Repository | Change | Reason | Impact |
|---|---|---|---|---|
| 2026-10-07 | frontend | Classified Azure OIDC identifiers as protected production environment variables | Align configuration model with OIDC architecture and deployment workflow | No API/runtime behavior change |
| 2026-10-07 | frontend | Corrected OIDC verification workflow to consume AZURE_CLIENT_ID, AZURE_TENANT_ID, and AZURE_SUBSCRIPTION_ID from `vars.*`, matching the deployment workflow and Phase 5 secret model | Prevent false configuration failures caused by reading identifiers from `secrets.*` | Verification-only; no credential model change |
| 2026-10-07 | frontend | Added controlled live OIDC/Azure verification procedure | Separate configuration readiness from live Azure/GitHub evidence | No product behavior change |

| 2026-10-07 | frontend | Corrected OIDC subject handling and recorded the live blocker for missing AZURE_FRONTEND_IDENTITY_NAME | Align Phase 5 artifacts with the protected-variable workflow and approved immutable production subject | Configuration-only; no API or runtime behavior change |
