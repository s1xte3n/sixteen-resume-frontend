# Phase 5 — Frontend CI/CD Configuration

## Production workflow
`.github/workflows/deploy-frontend.yml`

Protected OIDC inputs (non-secret identifiers supplied as production environment variables):
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
`.github/workflows/verify-azure-oidc.yml`

The verification workflow uses the same protected production **environment variables** as the deployment workflow for AZURE_CLIENT_ID, AZURE_TENANT_ID, and AZURE_SUBSCRIPTION_ID. These are identifiers, not secrets.

The workflow validates:
1. Required production environment variables exist.
2. GitHub Actions can exchange its OIDC token for an Azure session.
3. The Azure subscription/tenant context is available.
4. The configured Storage account exists in the configured resource group.
5. The configured frontend user-assigned managed identity client ID matches AZURE_CLIENT_ID.
6. Exactly one federated credential matches issuer `https://token.actions.githubusercontent.com`, subject `repo:<owner>/<repo>:environment:production`, and audience `api://AzureADTokenExchange`.
7. Blob data-plane access works through Entra login without a Storage key/SAS.
8. The configured public hostname serves HTTPS content.

The workflow's successful execution is the live evidence. A committed workflow file alone is not evidence.
