# Phase 5 — Frontend CI/CD Configuration

## Production workflow
`.github/workflows/deploy-frontend.yml`

Protected OIDC inputs:
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

Sequence: validate configuration → validate/scan static artifacts → build → OIDC login → upload `$web` using Entra authorization → verify Storage endpoint → optionally verify approved public HTTPS endpoint → publish evidence.

No Storage key, SAS, connection string, Cosmos credential, or client secret is permitted.

## OIDC verification
`.github/workflows/verify-azure-oidc.yml` validates the production OIDC relationship, Storage scope, UAMI client ID, federated credential subject/audience, and keyless Blob access. Workflow existence is not live evidence until it executes successfully.
