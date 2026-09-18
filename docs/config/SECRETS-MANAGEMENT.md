# Secrets Management

## Purpose

Canonical inventory and handling rules. **No secret values are stored here.**

## Secret inventory

| Logical secret | Status | Source | Consumer | Rotation/owner | Commit |
|---|---|---|---|---|---|
| AZURE_CLIENT_SECRET | Conditional | GitHub Actions secret/Azure secure mechanism | CI/CD if client-secret auth selected | Identity/deployment owner | **Never** |
| COSMOS_CONNECTION_STRING | Conditional | Azure/GitHub secure store | Function/integration tests if selected | Database owner | **Never** |
| COSMOS_ACCOUNT_KEY | Conditional | Azure/GitHub secure store | Function/integration tests if selected | Database owner; rotate on exposure | **Never** |
| AZURE_STORAGE_CONNECTION_STRING | Conditional | GitHub Actions secret | Frontend CI if selected | Frontend deployment owner | **Never** |
| Azure Function platform secrets | Platform-managed | Azure | Function runtime | Azure/resource owner | **Never** |
| Future deployment token | Conditional | GitHub/Azure secure store | CI/CD only | Deployment owner | **Never** |

The authentication mechanism is not yet frozen. Do not create credentials merely because a conditional name is listed.

## Non-secret identifiers

AZURE_SUBSCRIPTION_ID, AZURE_TENANT_ID, AZURE_CLIENT_ID, Azure resource names, Cosmos endpoint, API hostname, and production origin are identifiers/configuration, not passwords or keys. They still must not be hardcoded into client bundles when avoidable.

## Storage rules

Secrets may be stored only in GitHub encrypted secrets/environment secrets and/or Azure-supported secure configuration/identity mechanisms selected by the final security decision.

Never store secrets in source files, committed .env files, HTML/CSS/JavaScript, ARM plaintext, Postman environments, test fixtures, docs, PR comments, logs, or build artifacts.

## CI/CD rules

Read secrets only when required; use least privilege; mask values; never echo them; never place them in frontend artifacts; fail closed when required credentials are absent; prefer short-lived/federated authentication where supported; run secret scanning.

## Rotation

After suspected exposure: revoke/rotate, inspect repository/workflow history, remove exposed material, rerun secret scanning, validate the replacement, and record the event. Removing a secret from the latest commit is not rotation.

## Review rule

Any connection string, access key, bearer token, client secret, private certificate, or credential-like file blocks release until removed and rotated if exposed.

Production must have zero plaintext credentials in source control. The browser never receives Azure management or Cosmos credentials.
