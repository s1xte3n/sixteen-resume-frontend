# Phase 3 Blocker Status

## Scope

This document records the current frontend Phase 3 production blocker. The remediation is limited to Azure Storage data-plane RBAC; no frontend source, API, static-hosting, CDN, or OIDC workflow redesign is required.

## Frontend blocker — missing storage data-plane authorization

The production workflow successfully authenticated to Azure and reached the storage upload step. The upload failed because the deployment identity does not currently have permission to write blobs.

The workflow already uses:

`az storage blob upload-batch --auth-mode login`

Therefore the required fix is an Azure RBAC assignment, not a credential or workflow-authentication change.

### Required correction

Assign **Storage Blob Data Contributor** to the frontend GitHub Actions OIDC service principal at the production frontend Storage account only:

`st16resumeweb`

Do not replace this with storage account keys, SAS tokens, connection strings, client secrets, publish profiles, or broader Owner/Contributor access.

### Command-line correction

```bash
SUBSCRIPTION_ID="aab5f649-b686-4f86-95cc-aa72ae71f03b"
RESOURCE_GROUP="rg-sixteen-resume-prod"
FRONTEND_STORAGE_ACCOUNT="st16resumeweb"

az account set --subscription "$SUBSCRIPTION_ID"

FRONTEND_SP_OBJECT_ID="$(
  az ad sp list     --display-name "sixteen-resume-frontend-github-actions"     --query "[0].id"     --output tsv
)"

test -n "$FRONTEND_SP_OBJECT_ID"

STORAGE_SCOPE="/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Storage/storageAccounts/$FRONTEND_STORAGE_ACCOUNT"

az role assignment create   --assignee-object-id "$FRONTEND_SP_OBJECT_ID"   --assignee-principal-type ServicePrincipal   --role "Storage Blob Data Contributor"   --scope "$STORAGE_SCOPE"
```

Verify:

```bash
az role assignment list   --assignee "$FRONTEND_SP_OBJECT_ID"   --scope "$STORAGE_SCOPE"   --role "Storage Blob Data Contributor"   --output table
```

If role assignment creation itself fails with an authorization error, the administrator performing the assignment must have `Microsoft.Authorization/roleAssignments/write` at the target scope. Do not broaden the GitHub deployment identity to solve that administrator-side permission problem.

### Workflow requirement

No workflow change is required. Keep:

```yaml
az storage blob upload-batch \
  --account-name "${AZURE_STORAGE_ACCOUNT_NAME}" \
  --destination '$web' \
  --source dist \
  --auth-mode login \
  --overwrite
```

## Verification gate

Phase 3 remains **BLOCKED** until a fresh `main` production run proves:

- GitHub OIDC federation succeeds;
- expected Azure subscription context is established;
- blob upload to `$web` succeeds with `--auth-mode login`;
- public HTTPS verification succeeds;
- no storage keys, SAS tokens, connection strings, client secrets, or publish profiles are used.

No frontend implementation change is part of this remediation.
