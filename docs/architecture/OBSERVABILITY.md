```markdown
# Azure Cloud Resume Challenge — Observability Architecture

## 1. Purpose

Provide sufficient operational visibility to determine whether the approved system is:

- Deploying successfully.
- Serving the resume.
- Processing visitor-counter requests.
- Persisting counter state.
- Failing safely.

The requirements do not mandate a specific observability platform or dashboard design. Therefore this document defines the minimum operational signals without introducing additional application functionality.

---

# 2. Observability Boundaries

```text
Frontend
   |
   +--> Browser/network evidence
   |
   v
Azure Function
   |
   +--> Function logs
   |
   v
Cosmos DB
   |
   +--> Persistence failures

CI/CD
   |
   +--> Workflow results
   |
   +--> Test results
   +--> Deployment results
3. Logging
Azure Function

Logs should provide sufficient information to diagnose:

Request processing failure.
Validation failure.
Cosmos DB operation failure.
Unexpected runtime failure.

Logs must not contain:

Secrets.
Connection strings.
Access keys.
Tokens.
Unnecessary personal visitor data.
4. Log Levels

Where supported:

Information
Normal counter operation.
Successful dependency operation.
Warning
Recoverable dependency issue.
Unexpected but handled condition.
Error
Failed database operation.
Function execution failure.
Deployment-independent runtime failure.
5. Metrics

Relevant operational signals include:

Function invocation count.
Function failure count.
Function execution duration.
HTTP response status distribution.
Database operation failures.
CI test failures.
CI deployment failures.
Frontend publication failures.

The visitor count itself is application data, not an operational health metric.

6. Tracing

Distributed tracing is not a separate product requirement.

Where Azure Functions/platform capabilities provide request correlation or tracing without adding unnecessary architecture, those capabilities may be used.

No additional tracing platform is introduced solely for this project.

7. Frontend Operational Signals

The frontend must allow diagnosis of:

Static asset failures.
API request failures.
Invalid counter responses.
Delivery/cache problems.

Browser developer tools are an acceptable validation mechanism for the acceptance tests.

8. CI/CD Observability

GitHub Actions must expose:

Backend
Test execution result.
ARM deployment result.
Function deployment result.
Verification result.
Frontend
Frontend validation result.
Storage publication result.
Cache invalidation result where applicable.
Production endpoint verification result where implemented.
9. Dashboards

A dedicated Azure dashboard is not an approved product requirement.

Therefore no dashboard resource is required by the architecture.

If operational visualization is needed during implementation, native Azure/GitHub operational views should be used before introducing additional infrastructure.

10. Alerts

No specific production alerting SLO is defined in the approved requirements.

Therefore the architecture does not invent a mandatory alert threshold.

The minimum operational expectation is that deployment and CI failures are visible through GitHub Actions and runtime failures are diagnosable through Azure Function/platform logs.

11. Failure Signals
Failure	Signal
Frontend deployment failure	GitHub Actions failure
Backend test failure	GitHub Actions test failure
ARM failure	GitHub Actions deployment failure
Function runtime failure	Azure Function logs/metrics
API failure	HTTP response + frontend network evidence
Cosmos DB failure	Function logs + controlled API error
HTTPS failure	Endpoint/browser/TLS verification
DNS failure	DNS resolution verification
Stale CDN content	Production content verification
12. Security of Observability

Logs and operational telemetry must not become a secret-exfiltration path.

Do not log:

Credentials.
Tokens.
Connection strings.
Secrets.
Full request headers where unnecessary.
Personal visitor information.
13. Acceptance Evidence

Observability-related evidence includes:

Passing GitHub Actions test run.
Passing deployment workflow.
Function runtime evidence.
Browser API/network evidence.
Production HTTPS evidence.
DNS resolution evidence.

Primary verification IDs:

T-AZ-005
T-AZ-007
T-AZ-009
T-AZ-010
T-AZ-011
T-AZ-013
T-AZ-014
T-AZ-015
T-SEC-001
T-SEC-002

---
