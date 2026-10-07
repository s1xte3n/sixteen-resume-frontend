# Phase 5 — Configuration Change Log

## 2026-10-07 — Frontend UAMI recreation and OIDC correction

- Recreated the approved user-assigned managed identity `sixteen-resume-frontend-github` in `rg-sixteen-resume-prod`.
- New client ID: `2d19e037-cc57-462c-a950-862f9b8a80e6`.
- New principal ID: `200b60d9-b05a-4733-81f4-1053834de5c3`.
- Corrected the federated credential subject to `repo:s1xte3n/sixteen-resume-frontend:environment:production`.
- Added GitHub production `AZURE_FRONTEND_IDENTITY_NAME`.
- Required next correction: set GitHub production `AZURE_CLIENT_ID` to the new UAMI client ID and verify `Storage Blob Data Contributor` on `st16resumeweb`.
- No application code, API contract, browser/Cosmos boundary, or credential model changed.

| Date | Repository | Change | Reason | Impact |
|---|---|---|---|---|
| 2026-10-07 | frontend | Classified Azure OIDC identifiers as protected production environment variables | Align configuration model with OIDC architecture and deployment workflow | No API/runtime behavior change |
| 2026-10-07 | frontend | Corrected OIDC verification workflow to consume AZURE_CLIENT_ID, AZURE_TENANT_ID, and AZURE_SUBSCRIPTION_ID from `vars.*`, matching the deployment workflow and Phase 5 secret model | Prevent false configuration failures caused by reading identifiers from `secrets.*` | Verification-only; no credential model change |
| 2026-10-07 | frontend | Added controlled live OIDC/Azure verification procedure | Separate configuration readiness from live Azure/GitHub evidence | No product behavior change |

| 2026-10-07 | frontend | Corrected OIDC subject handling and recorded the live blocker for missing AZURE_FRONTEND_IDENTITY_NAME | Align Phase 5 artifacts with the protected-variable workflow and approved immutable production subject | Configuration-only; no API or runtime behavior change |


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
