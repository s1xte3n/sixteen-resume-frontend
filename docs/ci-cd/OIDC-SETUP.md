# Frontend Azure OIDC Setup

## Status

**Configuration defined; operational verification requires one controlled GitHub Actions run.**

This document is the source of truth for the frontend repository's GitHub Actions → Azure authentication.

The approved model is GitHub Actions OpenID Connect (OIDC) workload identity federation using a dedicated Microsoft Entra user-assigned managed identity. No Azure client secret, storage account key, SAS token, or connection string is part of the approved frontend deployment path.

## Repository

- Repository: `s1xte3n/sixteen-resume-frontend`
- Repository ID: `1373840239`
- Owner: `s1xte3n`
- Owner ID: `39813590`
- Production GitHub environment: `production`
- Production branch: `main`

Because this repository was created after 15 July 2026, GitHub uses immutable OIDC subjects by default. The expected production-environment subject is:

`repo:s1xte3n@39813590/sixteen-resume-frontend@1373840239:environment:production`

Verify the actual subject in the GitHub Actions OIDC token if GitHub changes or customizes the repository OIDC subject format before provisioning the Azure federated credential.

## Azure identity

Create or use a **dedicated user-assigned managed identity** for frontend deployment.

The identity must have:

1. A federated identity credential trusting this repository and the `production` GitHub environment.
2. The GitHub OIDC issuer:
   `https://token.actions.githubusercontent.com`
3. Audience:
   `api://AzureADTokenExchange`
4. The exact production subject defined above.
5. Azure RBAC limited to the frontend resources required for deployment.

The frontend identity must not have:

- Cosmos DB permissions.
- Function deployment permissions.
- Subscription Owner.
- Subscription Contributor.
- Resource-group-wide Contributor unless explicitly required and justified.

## Required GitHub production environment secrets

Configure these under:

**Repository → Settings → Environments → production → Environment secrets**

| Name | Type | Value |
|---|---|---|
| `AZURE_CLIENT_ID` | Secret | Client ID of the dedicated user-assigned managed identity |
| `AZURE_TENANT_ID` | Secret | Azure tenant/directory ID |
| `AZURE_SUBSCRIPTION_ID` | Secret | Target Azure subscription ID |

These are identifiers rather than passwords, but they remain environment-scoped secrets so that production deployment configuration is not exposed unnecessarily.

Do **not** create:

- `AZURE_CLIENT_SECRET`
- `AZURE_CREDENTIALS`
- `AZURE_STORAGE_CONNECTION_STRING`
- `AZURE_STORAGE_KEY`
- `AZURE_STORAGE_SAS_TOKEN`

for the frontend deployment path.

## Required GitHub production environment variables

Configure these under:

**Repository → Settings → Environments → production → Environment variables**

| Name | Purpose |
|---|---|
| `AZURE_STORAGE_ACCOUNT_NAME` | Storage account receiving the static website artifacts |
| `PUBLIC_SITE_URL` | Approved public HTTPS resume URL |
| `PUBLIC_API_BASE_URL` | Approved visitor-counter API origin |
| `PUBLIC_API_PATH` | Frozen API path: `/api/visitors` |

Only non-secret values belong here.

## Azure RBAC

The frontend deployment identity needs Blob data-plane write access to the production storage account.

Preferred role:

`Storage Blob Data Contributor`

Scope:

**the production storage account only**

Do not grant the identity a subscription-wide role merely to make the workflow work.

If the final CDN/edge service requires a cache purge operation, add only the provider-specific purge role at the narrowest applicable resource scope after ADR-006 is implemented. Do not add a purge permission now for an unselected service.

## Federated credential creation

The Azure federated credential must match:

- Issuer: `https://token.actions.githubusercontent.com`
- Subject: `repo:s1xte3n@39813590/sixteen-resume-frontend@1373840239:environment:production`
- Audience: `api://AzureADTokenExchange`

Do not use a wildcard subject.

Do not trust every branch of the repository.

Do not trust every repository owned by `s1xte3n`.

Do not create a credential for `pull_request` or feature branches with production permissions.

## Azure CLI setup

Run these commands from an authenticated administrative Azure shell. Replace only local shell variables; do not put resulting credentials into Git.

```bash
az login

SUBSCRIPTION_ID="$(az account show --query id -o tsv)"
TENANT_ID="$(az account show --query tenantId -o tsv)"

az account set --subscription "$SUBSCRIPTION_ID"

az identity create \
  --name "sixteen-resume-frontend-github" \
  --resource-group "<RESOURCE_GROUP>" \
  --location "eastus"

CLIENT_ID="$(az identity show \
  --resource-group "<RESOURCE_GROUP>" \
  --name "sixteen-resume-frontend-github" \
  --query clientId -o tsv)"

PRINCIPAL_ID="$(az identity show \
  --resource-group "<RESOURCE_GROUP>" \
  --name "sixteen-resume-frontend-github" \
  --query principalId -o tsv)"
```

Create the federated credential using the Microsoft Entra workload identity federation command appropriate to the current Azure CLI version. The immutable subject above must be used exactly.

Then assign the storage data role:

```bash
STORAGE_ID="$(az storage account show \
  --resource-group "<RESOURCE_GROUP>" \
  --name "<STORAGE_ACCOUNT_NAME>" \
  --query id -o tsv)"

az role assignment create \
  --assignee-object-id "$PRINCIPAL_ID" \
  --assignee-principal-type ServicePrincipal \
  --role "Storage Blob Data Contributor" \
  --scope "$STORAGE_ID"
```

Azure RBAC propagation can take several minutes.

## Verification workflow

The repository contains:

`.github/workflows/verify-azure-oidc.yml`

Run it manually from the GitHub Actions UI against `main`.

The workflow verifies:

1. The three required production environment secrets exist.
2. GitHub can issue an OIDC token.
3. Azure accepts the federated identity.
4. The workflow receives the expected Azure subscription context.
5. The production storage account exists.
6. The deployment identity can access Blob data using Microsoft Entra login.
7. No storage key or connection string is required.

A successful run is the required operational evidence for frontend OIDC readiness.

## Security verification

The following conditions must remain true:

- `permissions.id-token: write` exists only in workflows that actually need OIDC.
- Production deployment jobs reference the `production` environment.
- Azure federated trust is restricted to this repository and environment.
- Storage data access uses `--auth-mode login`.
- No storage account key is passed to GitHub Actions.
- No Azure client secret exists for this deployment.
- OIDC failures stop the workflow.
- Production deployment is impossible without the protected GitHub environment configuration.

## Relationship to frontend deployment

This document establishes the authentication/control-plane prerequisite.

The repository now contains `.github/workflows/deploy-frontend.yml`. It must be enabled operationally only after the frontend implementation and Storage infrastructure exist.

The frontend deployment workflow:

1. Validate the frontend build/static artifacts.
2. Log into Azure with the same OIDC identity.
3. Upload the approved static website artifacts to the Storage static website container.
4. Purge the selected delivery-layer cache when the final ADR-006 service requires it.
5. Execute a non-destructive HTTPS smoke test.
6. Fail the release when any post-deployment check fails.

The CDN purge step must not be implemented against an unselected service.
