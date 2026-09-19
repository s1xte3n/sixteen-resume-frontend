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
```

## 3. Azure Resource Topology

```text
Azure Subscription
|
+-- Resource Group
    |
    +-- Storage Account
    |     |
    |     +-- Static Website
    |
    +-- Azure CDN / approved Azure edge-delivery service
    |     |
    |     +-- Endpoint
    |     +-- Origin Group
    |     +-- Storage Static Website Origin
    |     +-- FreeDNS Custom Domain
    |     +-- Managed TLS Certificate
    |     +-- HTTPS Redirect Route
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
```

The exact resource names, SKUs, ARM properties, and edge-delivery service are implementation decisions subject to the approved requirements and cost/availability validation.

## 4. Azure Storage

Purpose:

Static website hosting.

Required artifacts:

HTML.  
CSS.  
JavaScript.

Access model:

Public read through the approved Azure edge-delivery path.  
CI/CD write.  
No general-purpose deployment credentials exposed to browser users.

## 5. Delivery/CDN Layer

**Delivery service: unresolved pending OR-004 validation.**

Purpose:

- HTTPS.
- CDN/edge delivery.
- Public delivery endpoint.
- Managed TLS certificate.
- Cache behavior.
- HTTP-to-HTTPS redirect.

The delivery layer is **not service-locked**; ADR-006 remains pending validation.

The delivery-layer origin is the Azure Storage static website endpoint.

The approved public hostname is the FreeDNS/afraid.org hosted hostname/subdomain defined by OR-002.

The selected service must satisfy all OR-004 acceptance conditions before production:

- HTTPS is supported.
- Certificate management is supported.
- The FreeDNS/afraid.org public hostname can resolve to and be associated with the service.
- Azure Storage remains the origin.
- Configuration can be represented in IaC where applicable.
- Recurring cost remains at or below the approved R100/month ceiling.
- The service is available in the required deployment architecture.

No specific Azure edge/CDN product is authoritative until OR-004 validation is complete.

## 6. DNS/Hostname

The project uses FreeDNS/free hostname functionality.

Required relationship:

```text
FreeDNS Public Hostname
      |
      v
Approved Azure HTTPS/CDN edge-delivery service
      |
      v
Azure Storage Static Website
```

DNS configuration must provide the records required by the **selected and validated** Azure edge-delivery service to associate the public hostname.

HTTPS must use certificate management supported by the selected and validated delivery service.

No paid domain registration is required for the MVP.

The project documentation must describe the hostname as a **FreeDNS hosted hostname/subdomain**, not as ownership of a conventional registrable custom domain.

## 7. Azure Function

Configuration direction:

| Property | Requirement |
|---|---|
| Platform | Azure Functions |
| Language | Python |
| Trigger | HTTP |
| Hosting | Consumption |
| Region | East US |
| Purpose | Visitor-counter API |
| Database access | Cosmos DB Table API |
| Public API | Only approved counter operation |

## 8. Cosmos DB

Configuration direction:

| Property | Requirement |
|---|---|
| Service | Azure Cosmos DB |
| API | Table API |
| Capacity | Serverless |
| Region | East US |
| Data | Visitor counter |
| Browser access | No |
| Application access | Azure Function |

## 9. ARM Infrastructure

The backend repository contains the authoritative ARM infrastructure.

The template must represent:

- Azure Storage static website.
- The selected and validated Azure HTTPS/CDN edge-delivery layer and its required resources.
- HTTPS/certificate configuration supported by the selected and validated delivery service.
- Azure Function Consumption resources.
- Cosmos DB Table API resources.
- Required deployment configuration.

The template must avoid storing plaintext secrets.

Sensitive configuration should be supplied through secure deployment mechanisms.

## 10. Resource Ownership

| Resource | Owning repository |
|---|---|
| HTML/CSS/JS | s1xte3n/sixteen-resume-frontend |
| Storage publication | Frontend CI/CD |
| delivery-layer configuration | s1xte3n/sixteen-resume-backend |
| Function code | s1xte3n/sixteen-resume-backend |
| Cosmos DB infrastructure | Backend ARM |
| ARM templates | s1xte3n/sixteen-resume-backend |
| Backend CI/CD | Backend repository |
| Frontend CI/CD | Frontend repository |

## 11. Infrastructure Deployment

Backend deployment order:

1. Validate Python tests.
2. Validate ARM.
3. Deploy/update Azure infrastructure.
4. Deploy Function application.
5. Verify API.
6. Verify delivery endpoint, public hostname, and HTTPS.

Frontend deployment order:

1. Validate frontend artifacts.
2. Publish to Azure Storage.
3. Invalidate/purge the selected edge-delivery service cache if required.
4. Verify public endpoint over HTTPS.

## 12. Dependency Ordering

Infrastructure dependencies:

```text
Storage
  |
  v
Selected Azure HTTPS/CDN edge-delivery service
  |
  v
DNS / FreeDNS Hostname
```

Counter dependencies:

```text
Cosmos DB
  |
  v
Function
  |
  v
Frontend JavaScript
```

The public counter cannot be considered operational until:

- Cosmos DB exists.
- Function exists.
- API contract exists.
- Frontend API integration exists.

## 13. Configuration

Configuration values must be classified as:

### Non-secret

Examples:

- Azure region.
- Resource names.
- Delivery endpoint hostname.
- Public hostname.
- API hostname.
- Table/partition identifiers.

These may be represented through approved IaC parameters.

### Secret

Examples:

- Deployment credentials.
- Database secrets if the selected authentication model requires them.
- GitHub deployment secrets.

These must not be committed.

## 14. Infrastructure Security

ARM deployment must use a dedicated deployment identity with only the permissions required to manage the project's infrastructure.

Runtime application permissions must be narrower than infrastructure deployment permissions.

The selected and validated delivery service must use HTTPS for public delivery.

The project does not add a separate WAF resource for the MVP unless the selected delivery architecture requires it and the addition is explicitly approved within the cost ceiling.

## 15. Cost Controls

The approved recurring Azure/cloud cost ceiling is:

**R100/month.**

Preferred target:

**R0/month.**

The final resource SKUs and delivery service must be validated against the approved **R100/month recurring Azure/cloud cost ceiling** before production.

The infrastructure should avoid:

- Dedicated always-on compute.
- Multiple environments.
- Unnecessary managed services.
- Containers.
- Kubernetes.
- Multi-region resources.
- Additional analytics systems.
- Any delivery-service SKU that would cause the recurring cost ceiling to be exceeded.

No specific delivery-service base fee or SKU is treated as authoritative in this document until OR-004 validation is completed against current availability and pricing.

Personal internet access, existing equipment, optional paid domain registration, and one-time purchases explicitly approved later are excluded from the recurring ceiling.

Any unexpected Azure/cloud charge must be investigated before continuing project work.

A recurring cost above R100/month blocks production.

## 16. Infrastructure Failure

If infrastructure deployment fails:

- GitHub Actions reports failure.
- Production promotion must not be treated as successful.
- The last known-good production infrastructure should remain the recovery target.

Infrastructure drift must be corrected through ARM rather than becoming permanent manual configuration.

## 17. Infrastructure Verification

Primary verification:

- T-AZ-004
- T-AZ-005
- T-AZ-008
- T-AZ-010
- T-AZ-012
- T-SEC-003
- T-COST-001
- T-REG-001
- T-IAC-001
- OR-004 delivery acceptance evidence

---
