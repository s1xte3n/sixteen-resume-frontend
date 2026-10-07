# Phase 5 — Frontend Configuration Security Review

| Finding | Status |
|---|---|
| Browser Azure/Cosmos credentials | PASS — none required or exposed |
| GitHub deployment authentication | PASS — OIDC, no client secret |
| Storage authorization | PASS — Entra identity + Storage Blob Data Contributor |
| Static artifact credential scanning | PASS |
| OIDC identifiers stored as GitHub secrets | PASS — identifiers are documented as protected production environment variables; no client secret is used |
| Frontend UAMI / GitHub production binding | BLOCKER — `AZURE_FRONTEND_IDENTITY_NAME` is missing and the approved UAMI name was not found in the tested resource group. Current reported client ID is `d3363a85-4425-4916-a90a-5b8494015450`, but its resource-type/name binding is unverified. |
| Public hostname | TBD / configuration gate |
| HTTPS edge service | TBD / configuration gate |
| CORS origin | TBD / configuration gate |
| Production cost evidence | TBD / configuration gate |
| API base URL variable | PASS — not approved; same-origin /api/visitors is authoritative |


## Live OIDC evidence — 2026-10-07

The controlled verification stopped at frontend production configuration validation because `AZURE_FRONTEND_IDENTITY_NAME` was absent. Direct Azure checks also returned `ResourceNotFound` for `sixteen-resume-frontend-github` in `rg-sixteen-resume-prod`. Therefore the frontend OIDC gate remains open. The reported client ID `d3363a85-4425-4916-a90a-5b8494015450` must first be correlated to an actual UAMI resource; do not infer the resource type from the UUID alone.