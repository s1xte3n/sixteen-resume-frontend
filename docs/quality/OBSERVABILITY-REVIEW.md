# Observability Review

## Document Control

| Field | Value |
|---|---|
| Phase | Phase 8 — Security, Reliability & Quality |
| Scope | Function/API, CI/CD, Azure infrastructure |
| Evidence level | Source/configuration review; live operational telemetry pending |

## 1. Executive Result

**Observability review status: PARTIAL — implementation baseline exists; production evidence pending**

The API has request-ID handling and controlled public errors. CI uploads local runtime logs on failure.

The project still requires live Azure logging/monitoring verification before the observability gate can be closed.

## 2. Current Controls

### Request correlation

The Function generates a UUID request ID when one is not supplied and returns it through the `X-Request-ID` response header.

A supplied request ID must be UUID v4.

### Safe public errors

Public errors use stable error codes and messages and do not return stack traces or dependency credentials.

### CI diagnostics

The backend workflow uploads Azurite and Functions host logs when a local CI execution fails.

## 3. Gaps

| ID | Severity | Gap | Required action | Verification |
|---|---|---|---|---|
| OBS-008-001 | P1 | Live Function log verification pending | Confirm deployed Function logs are available and contain request correlation information without secrets. | Observability smoke |
| OBS-008-002 | P1 | Production health/smoke evidence pending | Execute deployed API smoke tests and retain results. | VT-015 |
| OBS-008-003 | P2 | Alert/dashboard evidence not yet established | Define only the minimum operational signals required by the approved MVP architecture before release. | Observability verification |
| OBS-008-004 | P1 | Failure-path operational evidence pending | Trigger/verify controlled dependency failure behavior and confirm safe public response plus useful server-side telemetry. | Reliability/security tests |

## 4. Logging Hygiene

The implementation must not log:

- Cosmos credentials;
- Azure access tokens;
- connection strings;
- secret values;
- private resume information not required for operations.

Request IDs may be used for correlation.

## 5. Gate

Observability is **not production-closed** until deployed runtime logs, smoke tests, and failure-path evidence are available.
