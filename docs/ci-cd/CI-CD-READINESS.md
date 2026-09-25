# Frontend CI/CD Readiness

## Gate

**Environment configuration definition: COMPLETE**

**Production environment readiness: NOT YET VERIFIED**

**Frontend OIDC operational verification: PENDING EXECUTION**

The distinction is deliberate:

- The environment gate requires every runtime dependency to have a known configuration source and prohibits hardcoded secrets.
- OIDC/Azure resource verification is implementation/delivery evidence and cannot be claimed until the verification workflow has actually succeeded.

## Required production configuration

The production deployment workflow is now present at `.github/workflows/deploy-frontend.yml`. It is intentionally fail-closed until `site/index.html` and the production Azure Storage resource exist.

### GitHub environment: `production`

Secrets:

- `AZURE_CLIENT_ID`
- `AZURE_TENANT_ID`
- `AZURE_SUBSCRIPTION_ID`

Variables:

- `AZURE_STORAGE_ACCOUNT_NAME`
- `PUBLIC_SITE_URL`
- `PUBLIC_API_BASE_URL`
- `PUBLIC_API_PATH`

### Azure

- Dedicated user-assigned managed identity.
- GitHub OIDC federated credential.
- Immutable repository/environment subject.
- `api://AzureADTokenExchange` audience.
- Storage Blob Data Contributor scoped to the frontend storage account.
- No frontend access to Cosmos DB or Function administration.

## Verification evidence

Workflow:

`.github/workflows/verify-azure-oidc.yml`

Evidence required before marking OIDC operational:

| Evidence | Required result |
|---|---|
| GitHub production environment exists | Pass |
| Three OIDC identifier secrets exist | Pass |
| Azure federated credential exists | Pass |
| OIDC login | Pass |
| Azure subscription context | Pass |
| Storage account lookup | Pass |
| Blob data-plane access using Entra login | Pass |
| No long-lived Azure credential used | Pass |

The workflow intentionally does not print secret values.

## What is not required

The following do not block the environment configuration gate:

- A production website already being deployed.
- A CDN purge configuration before the CDN service is selected.
- A Function implementation.
- A Cosmos DB implementation.
- Production DNS.
- A final resume deployment.

Those belong to later implementation/release gates.

## Release dependency

Frontend production deployment remains blocked until the frontend implementation and Azure Storage infrastructure exist. This is an implementation state, not an environment-variable definition gap.
