# Azure Cloud Resume Challenge — System Architecture

## 1. Document Control

| Field | Value |
|---|---|
| System | Azure Cloud Resume Challenge |
| Architecture Status | Proposed — implementation not started |
| Requirements Source | `docs/product/REQUIREMENTS.md` |
| Acceptance Source | `docs/product/ACCEPTANCE-CRITERIA.md` |
| Dependency Source | `docs/product/DEPENDENCY-MATRIX.md` |
| Target Cloud | Microsoft Azure |
| Target Region | East US |
| Deployment Environments | One |
| Frontend Repository | `s1xte3n/sixteen-resume-frontend` |
| Backend Repository | `s1xte3n/sixteen-resume-backend` |
| Production Branch | `main` |
| Development Branch | `develop` |

---

# 2. Architecture Scope

This architecture covers only the approved Cloud Resume Challenge requirements.

The system provides:

1. A public HTML/CSS/JavaScript resume.
2. Azure Storage static website hosting.
3. HTTPS through the approved Azure delivery/CDN architecture.
4. A public hostname/DNS solution.
5. A JavaScript visitor counter.
6. An Azure Function HTTP API.
7. Persistent visitor-counter state in Azure Cosmos DB Table API.
8. Python serverless backend processing.
9. Automated Python tests.
10. ARM-based infrastructure as code.
11. Separate frontend/backend repositories.
12. GitHub Actions CI/CD.
13. A publicly linked project-learning article.

The architecture does not introduce:

- Authentication.
- User accounts.
- Admin functionality.
- CMS functionality.
- Contact forms.
- Additional analytics.
- Additional APIs.
- Additional cloud providers.
- Multiple application environments.
- E-commerce.
- Payments.

---

# 3. Architectural Principles

## 3.1 Requirements First

The architecture implements only requirements represented in the approved requirements baseline.

No implementation decision may silently convert an unresolved requirement into an assumed requirement.

## 3.2 Static Frontend

The resume is a static website implemented with:

- HTML
- CSS
- JavaScript

No frontend framework is required.

## 3.3 API as Database Boundary

Browser JavaScript communicates with the visitor-counter API.

Browser JavaScript never communicates directly with Cosmos DB.

## 3.4 Serverless Backend

Visitor-counter processing runs in Python on Azure Functions.

The function uses only the permissions required to perform its persistence operation.

## 3.5 Infrastructure as Code

Required Azure infrastructure is represented by ARM templates.

Manual Azure Portal configuration must not become the production source of truth.

## 3.6 Automated Delivery

Production deployment is performed through GitHub Actions.

Normal production deployment must not depend on manual laptop deployment.

## 3.7 Least Privilege

Each deployment/runtime identity receives only the permissions required for its responsibility.

## 3.8 Cost Consciousness

The architecture prefers free, serverless, or consumption-based services.

The numeric cost ceiling remains an unresolved requirement and must be frozen before final production acceptance.

---

# 4. Logical Architecture

```text
                         PUBLIC INTERNET
                               |
                               v
                    +----------------------+
                    | Public Hostname / DNS|
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | HTTPS / CDN /        |
                    | Delivery Layer       |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Azure Storage Static |
                    | Website              |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | HTML / CSS / JS      |
                    | Resume               |
                    +----------+-----------+
                               |
                               | HTTPS API request
                               v
                    +----------------------+
                    | Azure Function       |
                    | Python HTTP API      |
                    +----------+-----------+
                               |
                               | Table API
                               v
                    +----------------------+
                    | Azure Cosmos DB       |
                    | Table API             |
                    +----------------------+

The deployment/control plane is separate:

Frontend Repository
        |
        v
GitHub Actions
        |
        +--------------------> Azure Storage
        |
        +--------------------> Delivery cache invalidation
        

Backend Repository
        |
        v
GitHub Actions
        |
        +--> Python tests
        |
        +--> ARM deployment
        |
        +--> Azure Function deployment
        |
        +--> Cosmos DB infrastructure
```
# 5. Component Architecture
## 5.1 Public Resume

Responsibilities:

Render approved resume content.
Load CSS.
Execute visitor-counter JavaScript.
Link to the approved project-learning article.

Technology:

HTML
CSS
JavaScript

Repository:

s1xte3n/sixteen-resume-frontend

## 5.2 Azure Storage Static Website

Responsibilities:

Store static frontend artifacts.
Serve HTML.
Serve CSS.
Serve JavaScript.

It is the authoritative runtime host for the frontend content.

Deployment write access is restricted to CI/CD.

## 5.3 HTTPS/CDN Delivery Layer

Responsibilities:

Provide the approved public delivery path.
Provide HTTPS.
Provide CDN/delivery capability required by the approved requirements.
Deliver cached static content where supported.

The exact Azure service/configuration remains subject to ADR-006 validation.

## 5.4 Public DNS/Hostname

Responsibilities:

Resolve the approved public hostname.
Point the hostname to the approved delivery endpoint.

The project currently directs implementation toward a FreeDNS/free-hostname solution.

Whether this satisfies the original challenge's custom-domain interpretation must remain explicitly documented as a project deviation if approved.

## 5.5 Visitor Counter JavaScript

Responsibilities:

Request the counter through the public API.
Render the returned value.
Fail gracefully if the API is unavailable.
Never contain Cosmos DB credentials.
Never connect directly to Cosmos DB.

The precise counting semantics remain subject to ADR-007.

## 5.6 Azure Function

Responsibilities:

Accept the approved visitor-counter HTTP request.
Validate the request.
Read/update counter state.
Return the approved response.
Return controlled errors.
Avoid exposing implementation details or secrets.

Runtime:

Azure Functions
Python
Consumption plan

## 5.7 Cosmos DB Table API

Responsibilities:

Persist visitor-counter state.
Maintain state across frontend and backend deployments.
Provide the persistence boundary for the Azure Function.

Only the backend should access this persistence layer.

## 5.8 GitHub Actions
Frontend
main
 |
 v
Frontend CI/CD
 |
 +--> validation
 |
 +--> publish static files
 |
 +--> invalidate delivery cache where required
Backend
main
 |
 v
Backend CI/CD
 |
 +--> Python tests
 |
 +--> package/application validation
 |
 +--> ARM deployment
 |
 +--> Function deployment

A failing required test must prevent backend production deployment.

# 6. Application Boundaries
Boundary A — Public Web Boundary

Contains:

HTML
CSS
JavaScript
public resume content

Trust level:

Untrusted public client

No secrets may exist here.

Boundary B — API Boundary

Contains:

Azure Function
HTTP endpoint
request validation
counter business logic

Trust level:

Server-side application

This is the only application boundary between browser code and Cosmos DB.

Boundary C — Persistence Boundary

Contains:

Cosmos DB Table API
visitor-counter state

Trust level:

Private backend persistence

No browser access.

Boundary D — Deployment Boundary

Contains:

GitHub Actions
Azure deployment credentials/identity
ARM templates

Trust level:

Privileged automation

Deployment identities must be least privileged.

# 7. Request Flow

## 7.1 Resume Request
1. Visitor requests public hostname.
2. DNS resolves hostname.
3. HTTPS delivery layer receives request.
4. Delivery layer retrieves static content.
5. Azure Storage provides static assets.
6. Browser renders HTML/CSS.

## 7.2 Visitor Counter Request
1. Resume JavaScript executes.
2. JavaScript sends HTTPS request to Azure Function.
3. Azure Function validates request.
4. Function reads current counter state.
5. Function updates counter according to approved semantics.
6. Function returns counter result.
7. JavaScript validates response.
8. JavaScript renders counter.

## 7.3 Counter Failure Flow
Browser
   |
   v
Azure Function
   |
   X
Cosmos DB unavailable
   |
   v
Controlled API failure
   |
   v
JavaScript fallback behavior

The exact user-visible fallback remains an open P2 requirement.

The resume itself must remain readable when the counter fails.

# 8. Deployment Flow

## 8.1 Backend
Developer
   |
feature/*
   |
Pull Request
   |
CI
   |
Python tests
   |
merge to develop
   |
production promotion
   |
main
   |
GitHub Actions
   |
ARM deployment
   |
Function deployment

Production deployment is allowed only after required validation succeeds.

## 8.2 Frontend
Developer
   |
feature/*
   |
Pull Request
   |
CI
   |
merge to develop
   |
production promotion
   |
main
   |
GitHub Actions
   |
Azure Storage publication
   |
CDN cache invalidation where required

# 9. Data Flow

Only one persistent business datum is required:

Visitor Counter
      |
      v
Azure Function
      |
      v
Cosmos DB Table API

The browser receives only the approved counter result.

No visitor profile, demographic profile, account, or unrelated analytics dataset is introduced.

# 10. Data Model Summary

The minimum persistence model is one counter entity.

Conceptually:

Counter
├── PartitionKey
├── RowKey
└── Count

Exact property names and concurrency strategy are defined in:

docs/architecture/DATA-MODEL.md

# 11. Security Architecture Summary

Security controls include:

HTTPS.
No browser-to-Cosmos DB access.
No credentials in source control.
Secure CI/CD authentication.
Least-privilege deployment permissions.
Least-privilege runtime database permissions.
Controlled API errors.
Public content approval.
Source-controlled infrastructure.

Detailed controls are defined in:

docs/architecture/SECURITY-ARCHITECTURE.md

# 12. Infrastructure Summary

The target architecture contains:

Azure Storage static website.
Azure HTTPS/CDN delivery layer.
Public DNS/hostname.
Azure Function App.
Consumption hosting plan.
Cosmos DB account with Table API.
Required Cosmos DB table.
Application/runtime configuration.
CI/CD deployment configuration.

All required Azure resources must be represented in ARM.

Detailed infrastructure is defined in:

docs/architecture/INFRASTRUCTURE.md

# 13. Environment Strategy

There is one deployment environment:

Production

The project does not introduce separate:

Development Azure environment
Test Azure environment
Staging Azure environment

Local development and CI validation are not considered additional Azure deployment environments.

# 14. Availability

The requirements do not define a numeric production availability SLO.

Therefore this architecture does not invent one.

The system should be designed around the selected serverless/static services and should fail gracefully when the visitor-counter dependency is unavailable.

The static resume and visitor-counter service are separate failure domains at the application level:

Resume delivery can remain available if the counter API fails.
Counter persistence failure must not prevent resume rendering.

# 15. Failure Handling

Frontend failure

If CSS fails:

HTML remains available.
Resume content remains readable.

If JavaScript fails:

Resume remains readable.
Counter may be unavailable.
Delivery failure

If CDN/delivery configuration fails:

Public website may become unavailable.

This is a production infrastructure failure and must be detected through deployment and endpoint validation.

Function failure

If Azure Function fails:

Resume remains available.
Counter displays the approved failure state.
Database failure

If Cosmos DB fails:

Function returns controlled failure.
No database credentials are exposed.
Resume remains usable.
Deployment failure

A failed deployment must:

Report failure in GitHub Actions.
Prevent successful release status.
Preserve the previous successfully deployed production state where the deployment mechanism supports atomic/rollback-safe behavior.

The project does not introduce an additional deployment platform solely for rollback.

# 16. Recovery Strategy

Static Website

Recovery source:

Git repository
Azure Storage deployment workflow

Recovery mechanism:

Identify last known-good main commit.
Redeploy frontend through GitHub Actions.
Invalidate delivery cache if required.
Backend

Recovery source:

Backend repository.
ARM templates.
Python source.
Git history.

Recovery mechanism:

Identify last known-good commit.
Restore/redeploy ARM state.
Redeploy Python Function.
Verify API.
Verify persistence.
Database

Counter state is persistent infrastructure data.

Backend/frontend redeployment must not recreate or reset the counter state.

Database recovery details must remain limited to the approved persistence requirement; no additional backup platform is introduced unless required by Azure service configuration or explicitly approved.

# 17. Scalability

The system is intentionally small-scale.

Primary scaling characteristics:

Static frontend scales through the Azure delivery/storage architecture.
Azure Functions scales serverlessly according to platform behavior.
Cosmos DB uses the approved serverless capacity direction.

The architecture does not introduce:

Load balancers.
Kubernetes.
Container orchestration.
Application gateways.
Additional caching services.
Multi-region deployment.

Those would exceed the approved scope.

# 18. Cost Architecture

The cost strategy is:

Prefer free allowances.
Prefer serverless/consumption services.
Minimize persistent resource usage.
Avoid unnecessary services.
Validate current pricing before production.

The numeric cost ceiling is not yet frozen.

Therefore the architecture must not claim final cost compliance until that decision is recorded.

# 19. Major Technology Decisions

ADR	Decision	Requirement(s)
ADR-001	HTML/CSS/JS static frontend on Azure Storage	REQ-AZ-001..004
ADR-002	Azure Function is the API/database boundary	REQ-AZ-007..010
ADR-003	Cosmos DB Table API persistence	REQ-AZ-008
ADR-004	ARM + GitHub Actions deployment	REQ-AZ-011..014
ADR-005	Least-privilege secure CI/CD authentication	REQ-AZ-SEC-001..003
ADR-006	HTTPS/CDN delivery architecture	REQ-AZ-005/006/015
ADR-007	Visitor counting semantics	REQ-AZ-007..009

# 20. Decisions That Must Be Frozen Before Implementation

The following decisions materially affect architecture or acceptance and must be explicitly resolved:

P1
Visitor-count semantics.
Free hostname/subdomain versus custom-domain interpretation.
Numeric project cost ceiling.
Exact HTTPS/CDN architecture and pricing.
Final public resume content.
Repository naming normalization.
P2
Visitor-counter API contract.
Counter failure UX.
Python testing framework.
Blog-platform interpretation.
Supported browser baseline.
Availability target, if one is required.
DNS propagation expectation.

These correspond to the requirement-quality findings in the canonical requirements matrix.

# 21. Architecture Constraints

The following are hard constraints:

Azure remains the cloud provider.
East US remains the target region unless formally changed.
Azure Storage remains the frontend host.
Azure Functions remains the backend compute platform.
Python remains the backend language.
Cosmos DB Table API remains the visitor-counter persistence technology.
ARM remains the IaC format.
GitHub Actions remains the CI/CD platform.
Frontend and backend remain separate repositories.
Browser JavaScript cannot access Cosmos DB.
Secrets cannot be committed.
No additional application features may be introduced without scope approval.

# 22. Architecture Validation Gate

Architecture is considered implementation-ready only when:

All P0 architecture/security requirements are baselined.
P1 architecture decisions are explicitly resolved.
The CDN/HTTPS architecture is validated.
The hostname model is approved.
The cost ceiling is numeric.
Visitor semantics are defined.
API contract is defined.
Repository names are normalized.
Public resume content is approved.

Until then, affected components may be designed at the boundary level but must not be treated as implementation-locked.


---
