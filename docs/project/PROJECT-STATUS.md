// PROJECT-STATUS.md

# Azure Cloud Resume Challenge — Project Status

## Overall Status

**Implementation gate closed for MVP design/implementation — implementation not yet started**

The project requirements, scope, technology stack, constraints, repositories, resume source material, certification situation, and deployment target have been established.

## Discovery Status

| Area               | Status   | Notes                                            |
| ------------------ | -------- | ------------------------------------------------ |
| Project purpose    | Complete | Personal resume/portfolio                        |
| Target users       | Complete | Recruiters, hiring managers, technical reviewers |
| MVP                | Complete | All challenge requirements                       |
| Scope boundaries   | Complete | Strict challenge scope                           |
| Existing assets    | Complete | Current CV supplied                              |
| Technology stack   | Complete | Azure challenge stack confirmed                  |
| Azure subscription | Complete | Existing subscription                            |
| Azure region       | Complete | East US                                          |
| Deployment count   | Complete | One deployment                                   |
| Cost constraint    | Complete | R100/month recurring Azure/cloud ceiling; R0/month preferred; paid domain excluded |
| Security baseline  | Complete | Secrets, HTTPS, least privilege, API separation  |
| Git workflow       | Complete | feature → PR → CI → develop → production release → main |
| Repository plan    | Complete | Two repositories                                 |
| DNS approach       | Complete | FreeDNS selected initially                       |
| Certification      | Complete | AI-901 held; AZ-900 deviation documented         |
| Resume content     | Complete | Public HTML candidate exists; content-definition decision resolved; final owner approval remains a production acceptance gate |
| Resume positioning | Complete | 4+ years hands-on development; Gijima role separately identified |
| Blog platforms     | Complete | Dev.to + Hashnode                                |
| Deadline           | Complete | 30 September 2026                                |

## Current Technical State

| Component                  | Status      |
| -------------------------- | ----------- |
| Frontend repository        | Exists      |
| Backend repository         | Not started |
| HTML resume                | Candidate exists |
| CSS                        | Not started |
| JavaScript visitor counter | Not started |
| Azure Storage              | Not started |
| Azure HTTPS/CDN delivery layer | Capability architecture resolved; service selection pending implementation validation |
| DNS hostname               | Not started |
| Cosmos DB                  | Not started |
| Azure Function             | Not started |
| Python implementation      | Not started |
| Python tests               | Not started |
| ARM template               | Not started |
| Backend GitHub Actions     | Not started |
| Frontend GitHub Actions    | Not started |
| Blog — Dev.to              | Not started |
| Blog — Hashnode            | Not started |
| Production deployment      | Not started |

## Repository Plan

### Frontend

**Repository:** `sixteen-resume-frontend`

Status: **Created**

### Backend

**Repository:** `sixteen-resume-backend`

Status: **Not created**

## Resume Status

### Source Material

Status: **Available**

A complete CV has been supplied.

### Public Content Definition

Status: **Resolved — owner approval pending**

The public resume content policy and editorial positioning are defined by OR-005. The candidate HTML is stored at `docs/product/public-resume-content.html` and is governed by `docs/product/PUBLIC-RESUME-CONTENT-APPROVAL.md`.

The candidate must:


* Present the user as a Software Engineer / Backend Developer / Cloud Engineer.
* State **4+ years of hands-on software development experience**.
* Avoid implying that all four-plus years were professional software-engineering employment.
* Clearly identify **IT Operator — Gijima Holdings | June 2022–Present** as professional employment.
* Highlight relevant Azure, AWS, backend, serverless, CI/CD, and IaC experience.
* Include the Cloud Resume Challenge project.
* Display **Microsoft Certified: Azure AI Fundamentals (AI-901)**.
* Include only explicitly approved public links and contact information.
* Exclude private information not intended for public publication.

### Acceptance Gate

**REQ-AZ-001: Pending owner approval**

The candidate HTML content has been prepared, but final acceptance cannot pass until the owner explicitly approves the complete public HTML resume content.

## Certification Status

**Current certification:**

Microsoft Certified: Azure AI Fundamentals (AI-901)

Status: **Completed — July 2026**

### Challenge Deviation

The challenge specifies AZ-900.

The project currently uses AI-901 instead.

Status: **Documented deviation**

## DNS Status

**Provider:** FreeDNS / afraid.org

Status: **Provider selected; hostname not yet created**

The initial implementation will use a free hosted hostname/subdomain approach. A conventional paid domain can be introduced later if the website is moved toward a production personal-brand deployment.

## Blog Status

Platforms selected:

* Dev.to
* Hashnode

Status: **Not started**

The blog will cover both technical lessons and the overall project journey.

## Cost Status

Target:

**R0 where possible**

Fallback:

**Lowest possible cost**

The project should prioritize free allowances and serverless/pay-per-use services.

## Security Status

Security requirements established:

* No committed credentials.
* No secrets in source control.
* Secure GitHub Actions credentials.
* Least privilege.
* HTTPS.
* Browser cannot directly access Cosmos DB.
* Azure Function provides the database API boundary.

Implementation status: **Not started**

## Deadline

**30 September 2026**

Status: **Active project target**

## Next Project Phase

The discovery phase is complete.

The next phase is implementation: repository/bootstrap work followed by incremental implementation and validation of each challenge requirement. The final public resume content approval remains a production acceptance gate, not a requirements-definition blocker.


## OR-006–OR-009 Resolution Status

The following implementation-governing decisions are now resolved:

| ID | Resolution |
|---|---|
| OR-006 | Visitor API is `GET /api/visitors`; successful response contains the current visitor count; browser has no Cosmos DB credentials or direct database access. |
| OR-007 | One logical counter record; backend performs a concurrency-safe atomic logical increment and returns the resulting persisted count. |
| OR-008 | GitHub Actions is the deployment authority; backend and frontend pipelines must pass their defined validation/deployment gates before deployment. |
| OR-009 | `main` represents production; feature branches flow through PR and CI into `develop`, followed by the production release into `main`. |

The repository contains a `develop` branch created from `main`. Gate closure has been recorded in the project documentation; implementation remains not started.