# API Contract Changelog

## 1.1.0 — Phase 4 contract completion

### Frozen

- Canonical public operation remains `GET /api/visitors`.
- One top-level page load produces exactly one counter request.
- Successful operations increment the single persisted counter by exactly one.
- Concurrent successful operations must not lose increments.
- Browser-to-Cosmos access is prohibited.
- Public endpoint has no end-user authentication.
- Production CORS uses the final approved resume origin and no wildcard origin.
- Canonical error taxonomy is 400/405/429/500/503/504.
- No automatic browser retry is defined for the non-idempotent counter operation.
- Safe server-side retry is limited to known optimistic-concurrency conflicts before commit.
- Internal persistence and deployment interfaces are documented.
- Deployment authority remains GitHub Actions.
- Function-to-Cosmos access remains managed-identity based.
- Flex Consumption hosting does not change the public API.

### Corrected documentation drift

- Removed stale references treating OR-001 as unresolved.
- Removed stale references treating OR-006/OR-007 as unresolved.
- Clarified that the API path is `/api/visitors`; no new versioned route is introduced.
- Clarified that VC-001 has no request body.
- Clarified that 401/403 are not public end-user errors.
- Added explicit internal deployment/runtime interfaces.
- Added contract-level consistency and ambiguity review.

## 1.0.0 — 2026-09-18

Initial frozen visitor-counter contract based on the approved `GET /api/visitors` decision.

Earlier `POST /api/v1/visitor-count` drafts are superseded and are not authoritative.