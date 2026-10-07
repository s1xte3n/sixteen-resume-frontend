# Phase 5 — Controlled Live OIDC/Azure Verification

## Purpose

This artifact defines the controlled production verification required to close the Phase 5 live OIDC/Azure configuration gate.

The verification workflow is intentionally manual (`workflow_dispatch`) and is bound to the protected GitHub `production` environment. It does not deploy application changes or modify Azure resources.

## Required GitHub production environment configuration

Non-secret protected environment variables:

- `AZURE_CLIENT_ID`
- `AZURE_TENANT_ID`
- `AZURE_SUBSCRIPTION_ID`
- `AZURE_RESOURCE_GROUP_NAME`
- `AZURE_STORAGE_ACCOUNT_NAME`
- `AZURE_FRONTEND_IDENTITY_NAME`
- `AZURE_FRONTEND_IDENTITY_RESOURCE_GROUP`
- `PUBLIC_HOSTNAME`
- `VERIFY_PUBLIC_ENDPOINT`

No Azure client secret is required.

## Controlled execution

1. Open the frontend repository's GitHub Actions page.
2. Select **Verify Azure OIDC**.
3. Select **Run workflow** against `main`.
4. Confirm the workflow is using the protected `production` environment.
5. Do not modify workflow inputs or secrets during the run.
6. Record the run URL, commit SHA, run conclusion, and each verification step result.
7. If any step fails, do not mark Phase 5 ready. Record the exact failing step and remediate the external configuration before rerunning.

## Acceptance evidence

The live gate passes only when the run proves all of the following:

| Check | Required result |
|---|---|
| GitHub production environment variables | Present |
| OIDC login | Success |
| Azure subscription/tenant context | Matches configured identifiers |
| Storage account scope | Configured account exists in configured RG |
| Frontend UAMI client ID | Matches AZURE_CLIENT_ID |
| Federated credential issuer | `https://token.actions.githubusercontent.com` |
| Federated credential subject | `repo:s1xte3n@39813590/sixteen-resume-frontend@1373840239:environment:production` |
| Federated credential audience | `api://AzureADTokenExchange` |
| Federated credential count | Exactly one matching credential |
| Storage data-plane access | Success with `--auth-mode login` |
| Public hostname HTTPS | Success only if the approved public edge/DNS path exists |

## Security constraints

- Never print Azure credentials.
- Never add a client secret to make the check pass.
- Never use a Storage key/SAS to bypass OIDC or RBAC failure.
- Never expose Cosmos credentials to the browser.
- Never convert OIDC identifiers into long-lived credentials.
- Never treat workflow-file existence as live evidence.

## Current gate status

**BLOCKED — frontend UAMI exists and federation is configured, but GitHub client-ID synchronization and Storage RBAC remain unverified.**

The latest controlled verification failed during configuration validation because `AZURE_FRONTEND_IDENTITY_NAME` is missing from the GitHub `production` environment. Azure login was not reached.

The workflow is prepared for controlled execution, but this environment cannot independently dispatch a `workflow_dispatch` run or inspect Azure tenant-side RBAC/federated-credential state. Therefore no live pass is claimed here.

## Failure interpretation

- Missing `vars.*`: GitHub production environment configuration defect.
- Azure login failure: OIDC trust/tenant/subscription/client-ID configuration defect.
- Federated credential mismatch: Azure identity federation defect.
- Storage scope failure: Azure resource/configuration mismatch.
- Blob authorization failure: frontend UAMI Storage RBAC defect.
- Public hostname failure: approved edge/DNS/HTTPS path remains unresolved; do not bypass it with a different public URL.


## Current live correction — 2026-10-07

- The approved UAMI `sixteen-resume-frontend-github` now exists in `rg-sixteen-resume-prod` with client ID `2d19e037-cc57-462c-a950-862f9b8a80e6` and principal ID `200b60d9-b05a-4733-81f4-1053834de5c3`.
- The federated credential `github-production` now has issuer `https://token.actions.githubusercontent.com`, subject `repo:s1xte3n/sixteen-resume-frontend:environment:production`, and audience `api://AzureADTokenExchange`.
- `AZURE_FRONTEND_IDENTITY_NAME` has been added to the GitHub `production` environment with value `sixteen-resume-frontend-github`.
- `AZURE_CLIENT_ID` must be updated to `2d19e037-cc57-462c-a950-862f9b8a80e6` before verification; the previously reported `d3363a85-4425-4916-a90a-5b8494015450` is superseded.
- Storage Blob Data Contributor on `st16resumeweb` remains unverified because local Azure CLI RBAC commands return `MissingSubscription`.
- Do not add a client secret, Storage key, SAS token, or alternate identity type.