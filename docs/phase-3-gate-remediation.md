# Phase 3 Gate Remediation

## Current Phase 3 blocker

The frontend Azure Storage publication RBAC blocker is **resolved**. The remaining blocker is the **public HTTPS edge/DNS path**: the latest failure is a 20-second connection timeout from public-host verification. Storage publication is therefore not the failing step.

## Remediation applied

The frontend GitHub Actions service principal has Storage Blob Data Contributor scoped only to `st16resumeweb`; the previous resource-group-wide assignment was removed. The workflow continues to use Microsoft Entra/OIDC authorization.

The public endpoint must remain a hard verification gate; do not mask the timeout by weakening the check.

The previous required assignment was:

`/subscriptions/<subscription-id>/resourceGroups/rg-sixteen-resume-prod/providers/Microsoft.Storage/storageAccounts/st16resumeweb`

Do not switch the workflow to account keys or other secret-based authentication.

## Verification

After the assignment propagates, rerun the production frontend workflow and retain evidence that:

- Azure OIDC login succeeds.
- `az storage blob upload-batch --auth-mode login` succeeds.
- The Azure Storage static website endpoint is reachable.
- The approved public hostname resolves to the approved edge service and HTTPS serves the published resume.
- The selected edge implementation is represented by approved IaC and remains within the R100/month recurring cost ceiling.

## Gate status

**BLOCKED — storage publication is fixed; public HTTPS edge/DNS architecture remains unresolved.**
