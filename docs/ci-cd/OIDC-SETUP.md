# Frontend Azure OIDC Setup

## Status

**OIDC RESOLVED — verified by frontend production run #33 on 2026-10-07.**

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

The successful production run presented exactly this subject:

`repo:s1xte3n@39813590/sixteen-resume-frontend@1373840239:environment:production`

The Azure federated credential must contain this exact subject. The workflow itself is already aligned and does not require a code change.

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

## Manual Azure-side recreation procedure

If the existing frontend deployment identity is being removed, **do not create a normal app registration with `az ad app create` for the frontend workflow**. The approved frontend identity is a **user-assigned managed identity**. Recreate that identity and attach the federated credential to it.

Run from an authenticated Azure administrative shell:

```bash
SUBSCRIPTION_ID="aab5f649-b686-4f86-95cc-aa72ae71f03b"
TENANT_ID="936720d3-5742-4aa8-a632-b7731b0f24ff"
RESOURCE_GROUP="rg-sixteen-resume-prod"
LOCATION="eastus"
IDENTITY_NAME="sixteen-resume-frontend-github"

az account set --subscription "$SUBSCRIPTION_ID"

az account show \
  --query "{subscriptionId:id,tenantId:tenantId,name:name,state:state}" \
  --output table
```

If the old identity has already been deleted, create the replacement:

```bash
az identity create \
  --name "$IDENTITY_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --location "$LOCATION"

CLIENT_ID="$(az identity show \
  --resource-group "$RESOURCE_GROUP" \
  --name "$IDENTITY_NAME" \
  --query clientId -o tsv)"

PRINCIPAL_ID="$(az identity show \
  --resource-group "$RESOURCE_GROUP" \
  --name "$IDENTITY_NAME" \
  --query principalId -o tsv)"

echo "Frontend managed identity client ID: $CLIENT_ID"
echo "Frontend managed identity principal ID: $PRINCIPAL_ID"
```

Create exactly one production federated credential:

```bash
az identity federated-credential create \
  --identity-name "$IDENTITY_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --name "github-frontend-production" \
  --issuer "https://token.actions.githubusercontent.com" \
  --subject "repo:s1xte3n@39813590/sixteen-resume-frontend@1373840239:environment:production" \
  --audiences "api://AzureADTokenExchange"
```

Verify the credential before touching GitHub:

```bash
az identity federated-credential list \
  --identity-name "$IDENTITY_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --output table
```

The row must show exactly:

- issuer: `https://token.actions.githubusercontent.com`
- subject: `repo:s1xte3n@39813590/sixteen-resume-frontend@1373840239:environment:production`
- audience: `api://AzureADTokenExchange`

Then restore only the approved storage data-plane role:

```bash
STORAGE_ID="$(az storage account show \
  --resource-group "$RESOURCE_GROUP" \
  --name "<STORAGE_ACCOUNT_NAME>" \
  --query id -o tsv)"

az role assignment create \
  --assignee-object-id "$PRINCIPAL_ID" \
  --assignee-principal-type ServicePrincipal \
  --role "Storage Blob Data Contributor" \
  --scope "$STORAGE_ID"
```

Finally update the GitHub `production` environment:

- `AZURE_CLIENT_ID` = the **new frontend managed identity client ID**
- `AZURE_TENANT_ID` = `936720d3-5742-4aa8-a632-b7731b0f24ff`
- `AZURE_SUBSCRIPTION_ID` = `aab5f649-b686-4f86-95cc-aa72ae71f03b`

Do not add a client secret or publish profile.

## Backend app-registration recreation impact

The backend identity is a separate deployment identity from the frontend managed identity. If the backend app registration is recreated, the new backend application/client ID must replace the old value in the backend repository's protected `production` GitHub environment secret `AZURE_CLIENT_ID`.

The backend federated credential must use the backend repository's own immutable production subject. Do not reuse the frontend subject.

The new backend service principal must retain only the approved deployment permissions required by the backend pipeline. Existing resource-provider managed-identity permissions in the ARM template are separate from the GitHub deployment identity.

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

Production run #33 is the required operational evidence: Azure OIDC login succeeded with the exact immutable subject and the subsequent Storage upload succeeded with Microsoft Entra authorization. The remaining Phase 3 frontend blocker is public HTTPS/DNS delivery, not OIDC.

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
