# Phase 5 — Frontend Configuration Change Log

## 2026-10-07
- Re-baselined frontend configuration against the approved implementation and Phase 4 contract.
- Removed PUBLIC_API_BASE_URL, PUBLIC_API_PATH, and API_VERSION from the runtime configuration contract because the approved frontend uses same-origin /api/visitors and the API path is frozen by VC-001.
- Documented OIDC identifiers, Storage deployment inputs, test-state separation, validation rules, and security gates.
- Kept final hostname, HTTPS edge, CORS origin, live OIDC/RBAC evidence, and cost evidence as explicit gates.

- Corrected OIDC identifier classification: `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, and `AZURE_SUBSCRIPTION_ID` are consumed from protected GitHub production environment variables rather than GitHub Secrets. No credential model change was introduced.
