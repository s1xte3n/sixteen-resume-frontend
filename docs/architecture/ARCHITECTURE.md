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
