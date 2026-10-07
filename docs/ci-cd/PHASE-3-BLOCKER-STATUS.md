# Phase 3 Blocker Status

## Scope

This document records only the frontend Phase 3 deployment-verification blocker. It does not change the approved static-hosting architecture, deployment workflow, or GitHub OIDC authentication model.

## Frontend blocker — federated identity recreation

The production workflow already uses GitHub Actions OIDC with the protected `production` environment. No workflow authentication change is required.

The dedicated user-assigned managed identity must be recreated or corrected so that its federated identity credential exactly matches the immutable GitHub production subject:

- Issuer: `https://token.actions.githubusercontent.com`
- Subject: `repo:s1xte3n@39813590/sixteen-resume-frontend@1373840239:environment:production`
- Audience: `api://AzureADTokenExchange`

No wildcard subject, branch-wide subject, pull-request subject, client secret, publish profile, storage key, SAS token, or connection string is permitted.

## Azure-side remediation

Recreate the dedicated user-assigned managed identity if the existing identity is not trusted with the exact subject.

The recreated identity must:

1. contain exactly the production GitHub federated credential above;
2. have `Storage Blob Data Contributor` scoped only to the production frontend storage account;
3. have no Cosmos DB permissions;
4. have no Function App deployment permissions;
5. have no subscription Owner or Contributor role;
6. have no resource-group-wide Contributor role unless separately approved.

Update the GitHub `production` environment's `AZURE_CLIENT_ID` to the recreated identity's client ID. Keep `AZURE_TENANT_ID` and `AZURE_SUBSCRIPTION_ID` unchanged.

## Verification gate

Phase 3 remains **BLOCKED** until the existing `.github/workflows/verify-azure-oidc.yml` workflow succeeds against the recreated identity and confirms:

- GitHub OIDC token issuance;
- Azure federated authentication;
- expected subscription context;
- frontend storage access using Microsoft Entra authorization;
- absence of storage keys/connection strings from the deployment path.

No frontend source-code, API-contract, hosting, or CDN change is part of this blocker remediation.
