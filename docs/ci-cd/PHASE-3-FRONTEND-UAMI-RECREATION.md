# Phase 3 — Frontend UAMI Recreation and OIDC Binding

## Purpose

Record the exact Azure/GitHub correction required to restore frontend production OIDC without changing the approved frontend architecture or deployment mechanism.

## Frozen correction

| Item | Required value |
|---|---|
| Azure identity type | User-assigned managed identity |
| Managed identity name | `sixteen-resume-frontend-github` |
| Federated credential count | Exactly one production credential |
| Federated credential name | `github-frontend-production` |
| Issuer | `https://token.actions.githubusercontent.com` |
| Subject | `repo:s1xte3n@39813590/sixteen-resume-frontend@1373840239:environment:production` |
| Audience | `api://AzureADTokenExchange` |
| Tenant | `936720d3-5742-4aa8-a632-b7731b0f24ff` |
| Subscription | `aab5f649-b686-4f86-95cc-aa72ae71f03b` |
| Storage RBAC | `Storage Blob Data Contributor` |
| Storage RBAC scope | Production frontend Storage account only (`st16resumeweb`) |
| GitHub environment | `production` |
| GitHub environment secret | `AZURE_CLIENT_ID` = replacement managed identity client ID |

## Required exclusions

The correction must not introduce:

- an app registration in place of the user-assigned managed identity;
- a client secret or publish profile;
- subscription-wide Owner or Contributor;
- resource-group-wide Contributor for the frontend identity;
- Cosmos DB permissions;
- Function deployment permissions;
- wildcard or branch-wide federated trust;
- a second production federated credential.

## Verification gate

The correction is **not complete** until all of the following have direct evidence:

1. `sixteen-resume-frontend-github` exists as a user-assigned managed identity.
2. Its single production federated credential has the exact issuer, subject, and audience above.
3. Its principal has only the approved Storage Blob Data Contributor role at the frontend Storage account scope.
4. GitHub production `AZURE_CLIENT_ID` contains the new managed identity client ID.
5. The frontend production OIDC verification workflow succeeds against `main`.

## Current execution status

**BLOCKED.** The current connected tooling does not expose Azure control-plane write access or GitHub protected-environment secret mutation. The target state is documented, but no Azure/GitHub mutation is claimed as completed without direct evidence.

The existing frontend deployment workflow remains unchanged because it already uses `azure/login@v2` with `secrets.AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, and `AZURE_SUBSCRIPTION_ID`, plus `permissions.id-token: write`.
