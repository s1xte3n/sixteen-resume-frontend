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

**BLOCKED — frontend UAMI and GitHub production configuration are not yet live-verified.**


## Current live blocker — 2026-10-07

- `AZURE_FRONTEND_IDENTITY_NAME` is required and currently missing from the GitHub `production` environment.
- Approved value: `sixteen-resume-frontend-github`.
- Current reported client ID: `d3363a85-4425-4916-a90a-5b8494015450`.
- Azure verification of that client ID as the approved UAMI is still required; the named UAMI lookup returned `ResourceNotFound`.
- Do not introduce a client secret or change the workflow to use long-lived credentials.