```markdown
# Azure Cloud Resume Challenge — Infrastructure Architecture

## 1. Infrastructure Objectives

Infrastructure must:

- Run in Azure.
- Target East US.
- Support the approved resume application.
- Support the visitor counter.
- Be represented by ARM templates.
- Be reproducible.
- Minimize cost.
- Avoid undocumented manual production configuration.

---

# 2. Environment Model

There is one Azure deployment environment:

```text
Production

No additional Azure environments are introduced.

3. Azure Resource Topology
Azure Subscription
|
+-- Resource Group
    |
    +-- Storage Account
    |     |
    |     +-- Static Website
    |
    +-- Delivery/CDN Resource
    |
    +-- Function App
    |     |
    |     +-- Consumption Plan
    |     +-- Python Runtime
    |
    +-- Cosmos DB Account
          |
          +-- Table API
          |
          +-- Visitor Counter Table

The exact resource names and ARM properties are implementation decisions.

4. Azure Storage

Purpose:

Static website hosting.

Required artifacts:

HTML.
CSS.
JavaScript.

Access model:

Public read through approved delivery path.
CI/CD write.
No general-purpose deployment credentials exposed to browser users.
5. Delivery/CDN Layer

Purpose:

HTTPS.
CDN/delivery capability.
Public delivery endpoint.
Cache behavior.

The delivery architecture is fixed by ADR-006 as Cloudflare Free proxy/CDN → Azure Storage Static Website. Cloudflare is an external delivery dependency; Azure Storage remains the required origin.

See:

ADR-006.md

6. DNS/Hostname

The project uses the approved FreeDNS/afraid.org hosted hostname/subdomain. The final hostname must be verified for Cloudflare delegation/proxying and HTTPS compatibility before production acceptance.

Required relationship:

Public Hostname
      |
      v
Approved Delivery Endpoint
      |
      v
Azure Storage

The exact hostname and whether it is accepted as the project's interpretation of the custom-domain requirement must be formally recorded before production acceptance.

7. Azure Function

Configuration direction:

Property	Requirement
Platform	Azure Functions
Language	Python
Trigger	HTTP
Hosting	Consumption
Region	East US
Purpose	Visitor-counter API
Database access	Cosmos DB Table API
Public API	Only approved counter operation
8. Cosmos DB

Configuration direction:

Property	Requirement
Service	Azure Cosmos DB
API	Table API
Capacity	Serverless
Region	East US
Data	Visitor counter
Browser access	No
Application access	Azure Function
9. ARM Infrastructure

The backend repository contains the authoritative ARM infrastructure.

The template should represent the required resources and configuration necessary for the production architecture.

The template must avoid storing plaintext secrets.

Sensitive configuration should be supplied through secure deployment mechanisms.

10. Resource Ownership
Resource	Owning repository
HTML/CSS/JS	s1xte3n/sixteen-resume-frontend
Storage publication	Frontend CI/CD
Delivery configuration	Infrastructure/backend ownership
Function code	s1xte3n/sixteen-resume-backend
Cosmos DB infrastructure	Backend ARM
ARM templates	s1xte3n/sixteen-resume-backend
Backend CI/CD	Backend repository
Frontend CI/CD	Frontend repository
11. Infrastructure Deployment

Backend deployment order:

1. Validate Python tests
2. Validate ARM
3. Deploy/update Azure infrastructure
4. Deploy Function application
5. Verify API

Frontend deployment order:

1. Validate frontend artifacts
2. Publish to Azure Storage
3. Invalidate delivery cache if required
4. Verify public endpoint
12. Dependency Ordering

Infrastructure dependencies:

Storage
  |
  v
Delivery
  |
  v
DNS

Cosmos DB
  |
  v
Function
  |
  v
Frontend JavaScript

The public counter cannot be considered operational until:

Cosmos DB exists.
Function exists.
API contract exists.
Frontend API integration exists.
13. Configuration

Configuration values must be classified as:

Non-secret

Examples:

Azure region.
Resource names.
API hostname.
Table/partition identifiers.

These may be represented through approved IaC parameters.

Secret

Examples:

Deployment credentials.
Database secrets if the selected authentication model requires them.
GitHub deployment secrets.

These must not be committed.

14. Infrastructure Security

ARM deployment must use a dedicated deployment identity with only the permissions required to manage the project's infrastructure.

Runtime application permissions must be narrower than infrastructure deployment permissions.

15. Cost Controls

The infrastructure intentionally avoids:

Dedicated always-on compute.
Multiple environments.
Unnecessary managed services.
Containers.
Kubernetes.
Multi-region resources.
Additional analytics systems.

The final Azure resource SKUs must remain within the approved US$5/month recurring cloud/service ceiling before production acceptance.

16. Infrastructure Failure

If infrastructure deployment fails:

GitHub Actions reports failure.
Production promotion must not be treated as successful.
The last known-good production infrastructure should remain the recovery target.

Infrastructure drift must be corrected through ARM rather than becoming permanent manual configuration.

17. Infrastructure Verification

Primary verification:

T-AZ-004
T-AZ-005
T-AZ-008
T-AZ-010
T-AZ-012
T-SEC-003
T-COST-001
T-REG-001
T-IAC-001

---
