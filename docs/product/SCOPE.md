# Product Scope

## 1. Purpose

This document defines the approved product boundary for the Cloud Resume Challenge — Azure. It separates committed MVP scope from non-MVP priorities and future ideas. It does not silently resolve unresolved requirements.

## 2. MVP Scope

The MVP contains these 16 requirements:

| ID | MVP capability | Priority |
|---|---|---:|
| CR-AZ-MVP-001 | Public resume content | P1 |
| CR-AZ-MVP-002 | HTML resume | P1 |
| CR-AZ-MVP-003 | CSS styling | P1 |
| CR-AZ-MVP-004 | Azure Storage static website | P1 |
| CR-AZ-MVP-005 | HTTPS/CDN delivery | P1 |
| CR-AZ-MVP-006 | Public hostname/DNS | P1 |
| CR-AZ-MVP-007 | JavaScript visitor counter | P1 |
| CR-AZ-MVP-008 | Cosmos DB Table API persistence | P1 |
| CR-AZ-MVP-009 | Visitor-counter API | P1 |
| CR-AZ-MVP-010 | Python Azure Function | P1 |
| CR-AZ-MVP-011 | Automated Python tests | P1 |
| CR-AZ-MVP-012 | ARM Infrastructure as Code | P1 |
| CR-AZ-MVP-013 | Backend GitHub repository and CI/CD | P1 |
| CR-AZ-MVP-014 | Frontend GitHub repository and CI/CD | P1 |
| CR-AZ-MVP-015 | Public production deployment | P0 |
| CR-AZ-MVP-016 | Project-learning blog post | P2 |

All MVP requirements have detailed specifications in `PRD.md` and acceptance criteria in `ACCEPTANCE-CRITERIA.md`.

## 3. P1 Scope

P1 is the committed MVP-critical scope unless explicitly marked as an unresolved product decision. P1 open decisions must be closed before affected requirements can be accepted.

Current P1 product decisions:

- Visitor-count semantics.
- Free hostname/subdomain versus original custom-domain interpretation.
- HTTPS/CDN service suitability and cost validation.
- Final public resume-content approval.

Potential post-MVP P1 improvements, requiring explicit scope approval, include:

- Enhanced resume presentation within the existing purpose.
- Additional approved project evidence.
- Additional public project links.
- Defined user-facing visitor-counter failure messaging if not already required to close MVP behavior.
- Improved operational documentation.
- Additional resume sections following an approved content review.

## 4. P2 Scope

P2 items are not required to complete the MVP unless explicitly promoted through scope governance.

Potential P2 work includes:

- Additional public content sections.
- Additional project-learning articles.
- Non-identifying website analytics, subject to privacy review and explicit approval.
- Additional operational reporting.
- Expanded technical project documentation.
- Additional cloud-service demonstrations.
- Minor UX refinements such as browser baseline and blog-link behavior.

Current P2 unresolved decisions are tracked in `OPEN-REQUIREMENTS.md`.

## 5. P3 / Future Ideas

Potential future ideas include:

- General portfolio/CMS functionality.
- Resume administration interface.
- Visitor analytics dashboard.
- Multiple resume versions.
- Internationalized resume content.
- Additional interactive website functionality.
- Public content-management workflows.
- Automated content publishing beyond the approved project-learning requirement.

These ideas are explicitly future scope and must not be introduced into MVP implementation without a scope change.

## 6. Explicit Exclusions

- AZ-900 certification as a project requirement.
- Paid domain purchase unless separately approved.
- Unapproved recurring or one-time costs.
- Direct browser-to-Cosmos DB access.
- Visitor accounts/authentication.
- Public resume editing.
- Admin dashboards.
- General CMS functionality.
- Contact forms.
- E-commerce and payments.
- Unrelated personal analytics/tracking.
- Multiple deployment environments.
- Additional cloud providers.
- Frontend frameworks replacing plain HTML/CSS/JavaScript without scope approval.
- Replacing Python/Azure Functions without scope approval.
- Replacing Cosmos DB Table API without scope approval.
- Replacing ARM templates without scope approval.
- A general-purpose blog application.
- Functionality unrelated to demonstrating the approved Cloud Resume Challenge objectives.

## 7. Confirmed Technology Direction

| Area | Approved direction |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Static hosting | Azure Storage static website |
| Delivery | HTTPS + CDN/delivery layer + public hostname/DNS |
| API | Azure Functions HTTP trigger |
| Backend language | Python |
| Persistence | Azure Cosmos DB Table API |
| IaC | ARM templates |
| Source control | GitHub, separate frontend/backend repositories |
| CI/CD | GitHub Actions |
| Azure region | East US |
| Environments | One |
| Cost | R0/month preferred; hard ceiling USD $40/month recurring Azure/cloud cost; >USD $40/month recurring blocked; approved exclusions apply |

## 8. Scope Constraints

### Cost

The project targets **R0/month** recurring Azure/cloud cost where viable and permits up to **USD $40/month recurring Azure/cloud cost** for the MVP. Costs above USD $40/month recurring are blocked. The ceiling excludes personal internet access, existing equipment, optional paid domain registration, and one-time purchases explicitly approved later. Paid domain registration is out of MVP. Any unexpected Azure/cloud charge must be investigated before continuing project work.

### Certification

AI-901 may be displayed as an existing certification. AZ-900 is intentionally excluded and must not be claimed as satisfied.

### Content

The supplied CV is the source material. Final public content requires owner approval.

### Delivery

The project must use Azure Storage static website hosting with HTTPS and the approved CDN/delivery direction. Exact configuration remains subject to OR-004.

### Domain/DNS

A free hostname/subdomain is the current project direction. Whether this satisfies the original challenge's custom-domain intent remains OR-002.

## 9. Scope Governance

A proposal is a scope change if it:

- introduces a new product capability;
- changes an approved technology requirement;
- introduces a new recurring cost;
- changes the intended target audience;
- changes the visitor-counter purpose;
- changes the public deployment model;
- removes an approved MVP requirement.

A scope change must document:

1. User value.
2. Affected requirements.
3. Cost impact.
4. Security/privacy impact.
5. Dependencies.
6. Acceptance criteria.
7. Impact on MVP completion.

Technical usefulness alone does not add a feature to scope.

## 10. MVP Completion Definition

MVP scope is complete only when:

- all 16 MVP requirements are implemented;
- AC-001 through AC-016 pass;
- no P0/P1 ambiguity remains hidden;
- all deliberate challenge deviations are documented;
- approved production constraints are satisfied;
- public deployment is operational;
- final public resume content is approved;
- product/project documentation agrees with the implemented state.

## 11. Current Scope Status

**Status: Scope baseline complete; MVP closure blocked by unresolved product decisions.**

The scope is intentionally not marked fully closed because the approved sources still contain P1 decisions and a product/project documentation inconsistency regarding the blog platform.
