# Phase 5 — Frontend Secrets Management

## Approved authentication model

Frontend deployment uses GitHub Actions OIDC → dedicated Azure user-assigned managed identity → Storage Blob Data Contributor on the frontend Storage account.

The browser has no Azure credentials.

## Inventory

| ID | Reference | Classification | Storage | Consumer | Injection | Rotation/replacement |
|---|---|---|---|---|---|---|
| FE-SEC-001 | AZURE_CLIENT_ID | OIDC identifier | GitHub production environment secret in current workflow | azure/login + verification | GitHub Actions OIDC | Replace when UAMI changes |
| FE-SEC-002 | AZURE_TENANT_ID | OIDC identifier | GitHub production environment secret in current workflow | azure/login | GitHub Actions OIDC | Change only if tenant changes |
| FE-SEC-003 | AZURE_SUBSCRIPTION_ID | OIDC identifier | GitHub production environment secret in current workflow | azure/login | GitHub Actions OIDC | Change only if subscription changes |
| FE-SEC-004 | Azure client secret | prohibited | None | None | None | Must never be created |
| FE-SEC-005 | Storage account key | prohibited | None | None | None | Must never be created |
| FE-SEC-006 | Storage SAS token | prohibited | None | None | None | Must never be created |
| FE-SEC-007 | Cosmos credential | prohibited | None | None | None | Must never exist in frontend |

The OIDC values are identifiers, not client secrets. They are protected as GitHub Environment Secrets because the current workflow consumes them there; this does not change the underlying credential model.

## Exposure rules

Never place credentials in:
- site HTML/CSS/JavaScript;
- committed `.env` files;
- Postman environments;
- build artifacts;
- screenshots/evidence;
- workflow logs;
- API responses.

If credential material is exposed, revoke/replace it and inspect Git history separately.
