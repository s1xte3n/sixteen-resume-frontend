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

**BLOCKED — GitHub production environment configuration is incomplete.**

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

- Current reported frontend OIDC client ID: `d3363a85-4425-4916-a90a-5b8494015450`.
- Approved identity resource name: `sixteen-resume-frontend-github`.
- Approved identity resource group: `rg-sixteen-resume-prod`.
- Direct lookup of the approved UAMI returned `ResourceNotFound`.
- The GitHub production environment is also missing `AZURE_FRONTEND_IDENTITY_NAME`.
- These are two separate blockers. Configure the GitHub variable and verify/provision the actual UAMI before rerunning this workflow.
- Do not treat the reported client ID as proof of UAMI existence or substitute an Entra application/service principal without an approved architecture change.