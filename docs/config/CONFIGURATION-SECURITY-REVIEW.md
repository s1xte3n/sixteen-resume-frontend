# Phase 5 — Frontend Configuration Security Review

| Finding | Status |
|---|---|
| Browser Azure/Cosmos credentials | PASS — none required or exposed |
| GitHub deployment authentication | PASS — OIDC, no client secret |
| Storage authorization | PASS — Entra identity + Storage Blob Data Contributor |
| Static artifact credential scanning | PASS |
| OIDC identifiers stored as GitHub secrets | PASS — identifiers are documented as protected production environment variables; no client secret is used |
| Frontend UAMI / GitHub production binding | WARNING — approved UAMI now exists and its production federated credential is configured; GitHub `AZURE_CLIENT_ID` must be synchronized to the new client ID before the controlled workflow can pass. |
| Public hostname | TBD / configuration gate |
| HTTPS edge service | TBD / configuration gate |
| CORS origin | TBD / configuration gate |
| Production cost evidence | TBD / configuration gate |
| API base URL variable | PASS — not approved; same-origin /api/visitors is authoritative |


## Live OIDC evidence — 2026-10-07

- UAMI created: `sixteen-resume-frontend-github`.
- Client ID: `2d19e037-cc57-462c-a950-862f9b8a80e6`.
- Principal ID: `200b60d9-b05a-4733-81f4-1053834de5c3`.
- Federated credential subject corrected to `repo:s1xte3n/sixteen-resume-frontend:environment:production`.
- GitHub `AZURE_FRONTEND_IDENTITY_NAME` has been configured.
- Storage Blob Data Contributor remains unverified because local RBAC CLI calls return `MissingSubscription`.
- Phase 5 remains blocked until the new client ID is synchronized and Storage RBAC is verified.

The controlled verification stopped at frontend production configuration validation because `AZURE_FRONTEND_IDENTITY_NAME` was absent. Direct Azure checks also returned `ResourceNotFound` for `sixteen-resume-frontend-github` in `rg-sixteen-resume-prod`. Therefore the frontend OIDC gate remains open. The reported client ID `d3363a85-4425-4916-a90a-5b8494015450` must first be correlated to an actual UAMI resource; do not infer the resource type from the UUID alone.

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
