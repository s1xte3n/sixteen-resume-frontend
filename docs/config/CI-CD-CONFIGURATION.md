# Phase 5 — Frontend CI/CD Configuration

## Production workflow

`.github/workflows/deploy-frontend.yml`

Protected OIDC inputs (non-secret identifiers supplied as protected GitHub `production` environment variables; they are not repository secrets):
- AZURE_CLIENT_ID
- AZURE_TENANT_ID
- AZURE_SUBSCRIPTION_ID

Production variables:
- AZURE_RESOURCE_GROUP_NAME
- AZURE_STORAGE_ACCOUNT_NAME
- AZURE_FRONTEND_IDENTITY_NAME
- AZURE_FRONTEND_IDENTITY_RESOURCE_GROUP
- PUBLIC_HOSTNAME
- VERIFY_PUBLIC_ENDPOINT

The frontend repository uses `AZURE_RESOURCE_GROUP_NAME` as its canonical resource-group variable. No second resource-group variable name is approved.

Sequence: validate configuration → validate/scan static artifacts → build → OIDC login → upload `$web` using Entra authorization → verify Storage endpoint → optionally verify approved public HTTPS endpoint → publish evidence.

No Storage key, SAS, connection string, Cosmos credential, or client secret is permitted.

## OIDC verification

`.github/workflows/verify-azure-oidc.yml`

The verification workflow uses the same protected production environment identifiers for:
- AZURE_CLIENT_ID
- AZURE_TENANT_ID
- AZURE_SUBSCRIPTION_ID

It additionally requires:
- AZURE_RESOURCE_GROUP_NAME
- AZURE_STORAGE_ACCOUNT_NAME
- AZURE_FRONTEND_IDENTITY_NAME
- AZURE_FRONTEND_IDENTITY_RESOURCE_GROUP
- VERIFY_PUBLIC_ENDPOINT
- PUBLIC_HOSTNAME when VERIFY_PUBLIC_ENDPOINT=true

The workflow validates:
1. Required production environment variables exist.
2. GitHub Actions can exchange its OIDC token for an Azure session.
3. The Azure subscription/tenant context is correct.
4. The configured Storage account exists in the configured resource group.
5. The configured frontend user-assigned managed identity exists and its client ID matches AZURE_CLIENT_ID.
6. Exactly one federated credential matches the approved GitHub production subject, issuer `https://token.actions.githubusercontent.com`, and audience `api://AzureADTokenExchange`.
7. Blob data-plane access works through Entra login without a Storage key/SAS.
8. The configured public hostname serves HTTPS content when edge verification is enabled.

The workflow's successful execution is the live evidence. A committed workflow file alone is not evidence.

## Current gate status

**BLOCKED — frontend UAMI and federated credential are provisioned, but the protected GitHub client ID and Storage RBAC still require live verification.**


## Current live correction — 2026-10-07

- `AZURE_FRONTEND_IDENTITY_NAME` is now configured as `sixteen-resume-frontend-github` in the GitHub `production` environment.
- The approved UAMI now exists in `rg-sixteen-resume-prod`.
- Current UAMI client ID: `2d19e037-cc57-462c-a950-862f9b8a80e6`.
- GitHub production `AZURE_CLIENT_ID` must be synchronized to that client ID; the prior `d3363a85-4425-4916-a90a-5b8494015450` value is superseded.
- Federated credential is corrected to the exact production subject and audience.
- Storage Blob Data Contributor remains unverified because local `az role assignment` operations return `MissingSubscription`.
- Do not introduce a client secret, Storage key, SAS token, or alternate authentication mechanism.

## Live OIDC subject correction — 2026-10-07

The production GitHub OIDC assertion observed during controlled verification uses the exact subject `repo:s1xte3n@39813590/sixteen-resume-frontend@1373840239:environment:production`. The frontend verifier now derives this form from GitHub owner/repository IDs. The Azure UAMI federated credential must use this exact subject.

Current frontend UAMI: `sixteen-resume-frontend-github`; client ID `2d19e037-cc57-462c-a950-862f9b8a80e6`; principal ID `200b60d9-b05a-4733-81f4-1053834de5c3`.

## 2026-10-07 controlled verification correction

The failed run exposed two separate issues that must not be conflated:

1. **OIDC federation:** the Azure federated credential must exactly match the immutable GitHub subject observed in the live assertion: `repo:s1xte3n@39813590/sixteen-resume-frontend@1373840239:environment:production`.
2. **RBAC verification:** `Storage Blob Data Contributor` authorizes blob data operations but does not grant `Microsoft.Storage/storageAccounts/read`. Therefore `az storage account show` is not a valid least-privilege verification step for the frontend deployment identity. The verification workflow now proves the authenticated client through `az account show` and tests Storage through Entra-authenticated data-plane operations instead.

The frontend deployment workflow was likewise changed to verify static website service properties and the published `$web/index.html` through Entra-authenticated Storage data-plane calls. It no longer requires management-plane Reader access solely for deployment verification.

This is a verification/RBAC-boundary correction only. No API route, frontend runtime contract, persistence model, or authentication architecture changed.