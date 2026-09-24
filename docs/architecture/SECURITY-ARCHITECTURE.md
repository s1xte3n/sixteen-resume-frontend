# Azure Cloud Resume Challenge — Security Architecture

## 1. Security Objectives

The security architecture protects:

- Public resume content.
- Azure infrastructure.
- Visitor-counter persistence.
- CI/CD credentials.
- Deployment operations.

The architecture follows the approved requirements without introducing authentication or other out-of-scope security features.

---

# 2. Trust Boundaries

```text
                UNTRUSTED
                   |
                   v
          +----------------+
          | Public Browser |
          +-------+--------+
                  |
             HTTPS/API
                  |
                  v
          +----------------+
          | Azure Function |
          +-------+--------+
                  |
          backend access
                  |
                  v
          +----------------+
          | Cosmos DB      |
          +----------------+


          PRIVILEGED CONTROL PLANE

          GitHub Actions
                |
                v
       Azure deployment APIs
                |
        +-------+--------+
        |                |
   Azure Storage     Azure Function
                       |
                   Cosmos DB
3. Public Browser Boundary

The browser is untrusted.

It may:

Download public resume content.
Execute public JavaScript.
Call the approved visitor-counter API.

It must not:

Access Cosmos DB.
Receive Cosmos credentials.
Receive Azure deployment credentials.
Access administrative endpoints.
Access internal infrastructure APIs.
4. API Security Boundary

The Azure Function is the server-side security boundary between the public browser and Cosmos DB.

Responsibilities:

Validate requests.
Reject malformed input.
Limit operations to approved counter behavior.
Handle downstream failures safely.
Avoid exposing secrets.
Avoid exposing stack traces or internal implementation details.
5. Database Security

Cosmos DB must not be publicly exposed as a browser-facing application interface.

The Azure Function is the only application component authorized to access the counter data.

Database credentials/access configuration must be stored using secure Azure configuration mechanisms.

They must never be committed to Git.

6. Authentication

The public resume does not require user authentication.

The visitor-counter API is publicly callable only to the extent required by the approved API contract.

No login system, user account system, or authentication workflow is introduced.

CI/CD identities are authenticated separately from public users.

7. Authorization

Authorization is responsibility-based.

Frontend deployment identity

May:

Publish approved frontend artifacts.
Perform only required delivery-cache operations.

Must not:

Modify Cosmos DB.
Modify unrelated Azure resources.
Backend deployment identity

May:

Deploy required ARM infrastructure.
Deploy the required Function application.

Permissions must be limited to the required deployment scope.

Function runtime identity

May:

Read/update the visitor-counter data.

Must not:

Modify unrelated Azure resources.
Modify infrastructure.
Access unrelated data.
8. Secrets Management

Secrets must never be stored in:

Git source files.
JavaScript.
HTML.
CSS.
ARM templates as plaintext secrets.
Documentation.
Test fixtures.

CI/CD secrets must be injected through secure GitHub/Azure mechanisms.

GitHub Actions authentication is frozen as OIDC workload identity federation with a dedicated Entra user-assigned managed identity, as recorded in ADR-005.

9. HTTPS

All public production traffic must use HTTPS.

The selected delivery layer must provide:

TLS termination.
Valid certificate handling.
Public HTTPS access.

The exact service remains subject to ADR-006 capability validation.

10. CORS

The browser-to-function boundary requires a controlled CORS configuration if the selected Azure Function hosting/API configuration requires it.

The final allowed origin should be restricted to the approved production frontend hostname rather than allowing unrestricted origins unless required by the final architecture.

The exact CORS configuration depends on the final hostname decision.

11. Input Validation

The API must validate:

HTTP method.
Request shape.
Required inputs.
Data types where applicable.

Invalid input must result in a controlled error.

The function must not execute arbitrary database operations supplied by the browser.

12. Error Handling

Public responses must not disclose:

Stack traces.
Connection strings.
Access keys.
Internal resource names where unnecessary.
Database implementation details.

Operational details belong in server-side logs.

13. Source-Control Security

The following must be checked in CI:

Secret scanning where available.
Repository review.
No Azure credentials.
No Cosmos DB credentials.
No deployment tokens.
No private configuration files containing secrets.
14. Threat Considerations
Threat: Credential exposure

Control:

No secrets in frontend.
Secure CI secrets.
Least privilege.
Secret scanning.
Threat: Direct database access

Control:

Browser has no Cosmos DB endpoint/credentials.
Azure Function is the database boundary.
Threat: Malformed API input

Control:

Input validation.
Controlled errors.
Threat: Excessive deployment permissions

Control:

Dedicated deployment identities.
Least-privilege roles/scopes.
Threat: Stale or compromised frontend deployment

Control:

Protected production branch.
Required CI.
Automated deployment from approved source.
No direct manual production publication as normal workflow.
Threat: Accidental secret commit

Control:

CI secret scanning.
Repository review.
Secure secret storage.
15. Privacy

The approved visitor counter does not authorize unrelated visitor tracking.

The architecture does not intentionally persist:

IP addresses.
User profiles.
Device fingerprints.
Demographics.
Session histories.
Marketing analytics.
16. Security Verification
Control	Verification
No committed credentials	T-SEC-001
No browser-to-Cosmos access	T-SEC-002
Least-privilege deployment	T-SEC-003
Production HTTPS	T-SEC-004
17. Security Decisions Requiring Implementation Validation

Before production:

Final hostname and CORS origin must be provisioned and validated.
OIDC deployment identities and Azure RBAC scopes must be provisioned and tested.
Function managed identity and Cosmos DB for Table data-plane RBAC must be provisioned and tested.
The selected HTTPS/CDN service must pass ADR-006 capability, lifecycle, hostname, certificate, origin, IaC, and cost validation.

These are implementation evidence gates, not unresolved requirements-definition decisions.


---
