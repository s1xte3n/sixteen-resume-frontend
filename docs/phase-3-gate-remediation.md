# Phase 3 Gate Remediation

## Confirmed blocker

Frontend CI authenticates with Azure but the storage upload fails under OAuth/RBAC because the GitHub Actions deployment service principal lacks **Storage Blob Data Contributor** on `st16resumeweb`.

## Required remediation

Grant the frontend GitHub Actions service principal Storage Blob Data Contributor at:

`/subscriptions/<subscription-id>/resourceGroups/rg-sixteen-resume-prod/providers/Microsoft.Storage/storageAccounts/st16resumeweb`

Use Azure RBAC with the service principal object ID. Do not switch the workflow to account keys or other secret-based authentication.

## Verification

After the assignment propagates, rerun the production frontend workflow and retain evidence that:

- Azure OIDC login succeeds.
- `az storage blob upload-batch --auth-mode login` succeeds.
- The public HTTPS frontend endpoint is reachable.

## Gate status

**BLOCKED** until fresh production workflow evidence demonstrates successful OAuth/RBAC storage deployment.
