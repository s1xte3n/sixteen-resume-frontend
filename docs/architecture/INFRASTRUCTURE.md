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
    +-- Azure-managed HTTPS/CDN delivery layer
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

The exact resource names and ARM properties are implementation decisions.

## 4. Azure Storage

Purpose:

Static website hosting.

Required artifacts:

HTML.  
CSS.  
JavaScript.

Access model:

Public read through the Front Door delivery path.  
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

## 6. DNS/Hostname

The project uses FreeDNS/free hostname functionality.

Required relationship:

```text
FreeDNS Public Hostname
      |
      v
Azure-managed HTTPS/CDN delivery layer
      |
      v
Azure Storage Static Website
```

DNS must provide the records required by Azure Front Door to validate and associate the hostname.

HTTPS must use the Azure-managed Front Door certificate.

No paid domain registration is required.

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
- Azure-managed HTTPS/CDN delivery layer profile, endpoint, origin group, origin, route, and custom domain.
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
6. Verify delivery endpoint, custom hostname, and HTTPS.

Frontend deployment order:

1. Validate frontend artifacts.
2. Publish to Azure Storage.
3. Invalidate Front Door cache if required.
4. Verify public endpoint over HTTPS.

## 12. Dependency Ordering

Infrastructure dependencies:

```text
Storage
  |
  v
Azure-managed HTTPS/CDN delivery layer
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
- delivery endpoint hostname.
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

Front Door must use HTTPS for public delivery.

The project does not add a separate WAF resource for the MVP unless the selected delivery architecture requires it and the addition is explicitly approved within the cost ceiling.

## 15. Cost Controls

The approved recurring Azure cost ceiling is:

**R100/month.**

One-time domain/infrastructure purchase cost required by the MVP:

**USD $0.**

The infrastructure intentionally avoids:

- Dedicated always-on compute.
- Multiple environments.
- Unnecessary managed services.
- Containers.
- Kubernetes.
- Multi-region resources.
- Additional analytics systems.
- Front Door Premium.
- Front Door Classic.

Azure-managed HTTPS/CDN delivery layer has a published base fee of $35/month, billed hourly, plus usage-based request and data-transfer charges. The remaining $5/month budget covers the project's other Azure resource and delivery usage.

The final resource SKUs and delivery service must be validated against the approved **R100/month recurring Azure/cloud cost ceiling** before production. R0/month is the preferred target. Personal internet access, existing equipment, optional paid domain registration, and one-time purchases explicitly approved later are excluded from the recurring ceiling. Any unexpected Azure/cloud charge must be investigated before continuing project work. A recurring cost above R100/month blocks production.

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
```
