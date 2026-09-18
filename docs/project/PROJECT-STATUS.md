// PROJECT-STATUS.md

# Azure Cloud Resume Challenge — Project Status

## Overall Status

**Discovery complete — implementation not started**

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
| Cost constraint    | Complete | R0 preferred; lowest possible cost               |
| Security baseline  | Complete | Secrets, HTTPS, least privilege, API separation  |
| Git workflow       | Complete | develop → feature → PR → CI → merge              |
| Repository plan    | Complete | Two repositories                                 |
| DNS approach       | Complete | FreeDNS selected initially                       |
| Certification      | Complete | AI-901 held; AZ-900 deviation documented         |
| Resume content     | Complete | Source CV supplied                               |
| Resume positioning | Complete | 4+ years hands-on development                    |
| Blog platforms     | Complete | Dev.to + Hashnode                                |
| Deadline           | Complete | 30 September 2026                                |

## Current Technical State

| Component                  | Status      |
| -------------------------- | ----------- |
| Frontend repository        | Not started |
| Backend repository         | Not started |
| HTML resume                | Not started |
| CSS                        | Not started |
| JavaScript visitor counter | Not started |
| Azure Storage              | Not started |
| Azure CDN                  | Not started |
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

Status: **Not created**

### Backend

**Repository:** `sixteen-resume-backend`

Status: **Not created**

## Resume Status

### Source Material

Status: **Available**

A complete CV has been supplied.

### Required Editorial Changes

The resume should:

* Present the user as a Software Engineer / Backend Developer / Cloud Engineer.
* State **4+ years of hands-on software development experience**.
* Avoid implying that all four-plus years were professional software-engineering employment.
* Clearly identify Gijima Holdings employment as IT Operations.
* Highlight relevant Azure, AWS, backend, serverless, CI/CD, and IaC experience.
* Include the Cloud Resume Challenge project.
* Include AI-901.
* Include links to GitHub and the published blog content.

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

The next phase is implementation planning and repository/bootstrap work, followed by incremental implementation and validation of each challenge requirement.
