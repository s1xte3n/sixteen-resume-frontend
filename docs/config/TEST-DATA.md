# Phase 5 — Frontend Test Data

Frontend tests use synthetic data and configuration only.

| ID | Data/config | Purpose | Cleanup |
|---|---|---|---|
| FE-TEST-001 | Synthetic UUID v4 request ID | X-Request-ID contract testing | Request-scoped |
| FE-TEST-002 | Synthetic count such as 0, 1, 42 | Rendering/validation | Fixture-scoped |
| FE-TEST-003 | Malformed/non-UUID request ID | API validation testing | Fixture-scoped |
| FE-TEST-004 | Synthetic API error response | Graceful counter failure behavior | Fixture-scoped |
| FE-TEST-005 | Synthetic publicOrigin/apiBaseUrl only in API-client test environment where required | Cross-component contract testing | Untracked local environment |

No real personal information or Azure credentials are needed.

The frontend must not create production state solely to support testing.
