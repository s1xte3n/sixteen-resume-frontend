# Product Scope

## 1. Purpose

This document defines the product scope for the Cloud Resume Challenge — Azure and separates confirmed MVP scope from future priorities and explicit exclusions.

---

# 2. MVP Scope

The MVP consists of the following requirements:

1. Public resume content.
2. HTML resume.
3. CSS styling.
4. Azure Storage static website hosting.
5. HTTPS/CDN delivery.
6. Public hostname/DNS.
7. JavaScript visitor counter.
8. Cosmos DB Table API persistence.
9. Visitor-counter API.
10. Python Azure Function.
11. Automated Python tests.
12. ARM infrastructure as code.
13. Backend GitHub repository and CI/CD.
14. Frontend GitHub repository and CI/CD.
15. Public production deployment.
16. Project-learning blog post.

Each MVP requirement has a corresponding requirement ID in `PRD.md` and acceptance criteria in `ACCEPTANCE-CRITERIA.md`.

---

# 3. P1 Scope

P1 represents potential post-MVP improvements that are related to the product purpose but are not required for MVP completion.

Potential P1 scope:

- Enhanced resume presentation within the existing product purpose.
- Additional approved project evidence.
- Additional public project links.
- Defined user-facing visitor-counter failure messaging.
- Improved documentation of operational behavior.
- Additional resume sections if justified by the final resume-content review.

P1 features require explicit approval before entering the implementation scope.

---

# 4. P2 Scope

Potential P2 scope:

- Additional public content sections.
- Additional project-learning articles.
- Non-identifying website analytics.
- Additional deployment environments.
- Additional operational reporting.
- Expanded technical project documentation.
- Additional cloud-service demonstrations.

These are future possibilities and are not MVP commitments.

---

# 5. P3 / Future Ideas

Potential P3/future ideas include:

- General portfolio/CMS functionality.
- Resume administration interface.
- Visitor analytics dashboard.
- Multiple resume versions.
- Internationalized resume content.
- Additional interactive website functionality.
- Public content-management workflows.
- Automated content publishing.

These ideas must not be introduced into MVP without an explicit scope decision.

---

# 6. Explicit Exclusions

The following are explicitly outside the current product scope:

- AZ-900 certification.
- Paid domain purchase unless separately approved.
- Unrelated application or portfolio features.
- Unapproved recurring or one-time costs.
- Direct browser-to-Cosmos DB access.
- Manual production infrastructure configuration as the intended workflow.
- Visitor accounts.
- Public resume editing.
- General CMS functionality.
- Unrelated personal analytics or tracking.
- Replacing HTML/CSS/JavaScript with a frontend framework without a scope change.
- Replacing Python/Azure Functions without a scope change.
- Replacing Cosmos DB Table API without a scope change.
- Replacing ARM IaC without a scope change.
- A general-purpose blog platform as part of this application.

---

# 7. Scope Constraints

## Cost

The project is intended to remain at zero or near-zero cost.

A numeric cost ceiling has not yet been defined.

Any unavoidable cost requires explicit approval.

## Certification

AZ-900 is not part of this project.

The existing AI-901 certification may appear on the resume where appropriate but does not become a substitute project requirement.

## Technology

The approved technology direction is:

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- Python
- Azure Functions

### Database

- Azure Cosmos DB
- Table API

### Infrastructure

- ARM templates

### Hosting

- Azure Storage static website

### Delivery

- HTTPS
- CDN
- Public hostname/DNS

### Source Control

- GitHub
- Separate frontend/backend repositories

### CI/CD

- GitHub Actions

---

# 8. Scope Change Rules

A proposed feature is a scope change if it:

- introduces a new product capability;
- changes an approved technology requirement;
- introduces a new recurring cost;
- changes the intended target audience;
- changes the visitor-counter purpose;
- changes the public deployment model;
- removes an approved MVP requirement.

Scope changes must identify:

1. User value.
2. Affected requirements.
3. Cost impact.
4. Security/privacy impact.
5. Dependencies.
6. Acceptance criteria.
7. Impact on MVP completion.

No feature becomes part of the product solely because it is technically useful.

---

# 9. Current Scope Boundary

The product is a focused Cloud Resume Challenge implementation.

It is not currently a general-purpose personal portfolio platform.

The project should prioritize evidence of:

- Azure cloud engineering.
- Serverless development.
- Backend development.
- Infrastructure as Code.
- Automated testing.
- CI/CD.
- Secure cloud deployment.
- Practical software engineering.

Features unrelated to those objectives require explicit scope approval.

---

# 10. Scope Completion

MVP scope is considered complete when:

- Every MVP requirement is implemented.
- Every MVP requirement has passing acceptance criteria.
- No P0/P1 ambiguity remains hidden.
- Approved production constraints are satisfied.
- Public deployment is operational.
- Documentation accurately represents the final scope.