# Phase 3 Blocker Status

## Scope

This document records the current frontend Phase 3 production blocker. No frontend source, API, static-hosting, CDN, or OIDC workflow redesign is required.

## Frontend blocker — missing storage data-plane authorization

The production workflow successfully authenticated to Azure and reached the storage upload step. The upload failed because the deployment identity does not currently have permission to write blobs.

Required correction:

- **Storage Blob Data Contributor**
- Scope: production frontend Storage account only: `st16resumeweb`
- Authentication: Microsoft Entra/OIDC via `azure/login` and `az storage blob upload-batch --auth-mode login`

Do not replace this with storage account keys, SAS, connection strings, client secrets, publish profiles, or broader Contributor/Owner access.

### Azure-side correction

Assign `Storage Blob Data Contributor` to the existing frontend production OIDC principal at the storage-account scope only.

The exact principal must be the identity configured in the GitHub `production` environment as `AZURE_CLIENT_ID`.

### Command-line correction

Run as an administrator authorized to assign storage data-plane RBAC:

```bash
SUBSCRIPTION_ID="aab5b649-b686-4f86-95cc-aa72ae71f03b"
RESOURCE_GROUP="rg-sixteen-resume-prod"
FRONTEND_STORAGE_ACCOUNT="st16resumeweb"
FRONTEND_DEPLOYMENT_PRINCIPAL_OBJECT_ID="<frontend-oidc-principal-object-id>"

az account set --subscription "$SUBSCRIPTION_ID"

STORAGE_SCOPE="/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Storage/storageAccounts/$FRONTEND_STORAGE_ACCOUNT"

az role assignment create \
  --assignee-object-id "$FRONTEND_DEPLOYMENT_PRINCIPAL_OBJECT_ID" \
  --assignee-principal-type ServicePrincipal \
  --role "Storage Blob Data Contributor" \
  --scope "$STORAGE_SCOPE"
```

## Verification gate

Phase 3 remains **BLOCKED** until a fresh `main` production run proves:

- GitHub OIDC federation succeeds;
- expected Azure subscription context is established;
- blob upload to `$web` succeeds with `--auth-mode login`;
- public HTTPS verification succeeds;
- no storage keys or connection strings are used.

No frontend implementation change is part of this remediation.
