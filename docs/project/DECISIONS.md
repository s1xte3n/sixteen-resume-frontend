// DECISIONS.md

# Azure Cloud Resume Challenge — Decisions

## D-001 — Project Purpose

**Decision:** Build a personal cloud resume and portfolio website.

**Reason:** The project is intended to demonstrate practical software engineering, Azure, serverless, IaC, testing, and CI/CD skills while serving as the user's personal online resume.

---

## D-002 — Target Audience

**Decision:** Target both recruiters/hiring managers and technical reviewers.

**Reason:** The resume must communicate professional value quickly while the implementation must also provide enough technical evidence for engineering reviewers.

---

## D-003 — MVP Scope

**Decision:** The MVP is the complete Azure Cloud Resume Challenge.

**Reason:** The user explicitly wants to follow the challenge requirements without adding unrelated features.

---

## D-004 — Scope Discipline

**Decision:** Do not add functionality beyond the challenge unless explicitly requested later.

**Reason:** Prevent scope creep and keep the project focused on demonstrating the required Azure capabilities.

---

## D-005 — Certification

**Decision:** Display the existing Microsoft Certified: Azure AI Fundamentals (AI-901) certification.

**Reason:** AI-901 is the Azure certification currently held by the user.

**Deviation:** The challenge specifically requires AZ-900. AI-901 does not satisfy that literal requirement.

**Documentation rule:** The project must describe this as a deviation and must not claim AZ-900 compliance.

---

## D-006 — Resume Experience Positioning

**Decision:** Describe the user as having **4+ years of hands-on software development experience**.

**Reason:** The user graduated in May 2022 and has continuously worked on substantial personal software projects since then.

**Important distinction:** Professional employment remains represented separately as IT Operator at Gijima Holdings from June 2022 to present.

The resume must not imply four-plus years of professional software-engineering employment.

---

## D-007 — Frontend Technology

**Decision:** Use plain HTML, CSS, and JavaScript.

**Reason:** These technologies are explicitly required by the challenge and demonstrate the underlying web fundamentals without introducing unnecessary frontend framework complexity.

---

## D-008 — Static Website Hosting

**Decision:** Use Azure Storage static website hosting.

**Reason:** Azure Storage is explicitly required by the challenge.

---

## D-009 — HTTPS

**Decision:** Use Azure CDN to provide HTTPS for the static website.

**Reason:** HTTPS through Azure CDN is explicitly required by the challenge.

---

## D-010 — DNS

**Decision:** Use FreeDNS / afraid.org for the initial zero-cost DNS/hostname implementation.

**Reason:** The user requested a free solution where possible.

**Constraint:** This provides a free hosted hostname/subdomain approach rather than ownership of a conventional registrable domain.

**Future option:** A paid custom domain can replace this when the project is productionized.

---

## D-011 — Visitor Counter

**Decision:** Implement the visitor counter using frontend JavaScript calling an Azure Function HTTP API.

**Reason:** The challenge requires a JavaScript visitor counter and explicitly prohibits direct browser communication with Cosmos DB.

---

## D-012 — Database

**Decision:** Use Azure Cosmos DB Table API with serverless capacity.

**Reason:** This is the database approach recommended by the challenge and minimizes cost for the project's expected workload.

---

## D-013 — API

**Decision:** Use an Azure Function with an HTTP trigger as the API between the website and Cosmos DB.

**Reason:** This satisfies the challenge requirement and keeps database credentials/access outside browser-side JavaScript.

---

## D-014 — Backend Language

**Decision:** Use Python for the Azure Function.

**Reason:** Python is explicitly required/recommended by the challenge and provides an opportunity to demonstrate Python backend development and Azure SDK usage.

---

## D-015 — Testing

**Decision:** Include automated tests for the Python backend.

**Reason:** Testing is an explicit challenge requirement and provides validation before deployment.

---

## D-016 — Infrastructure as Code

**Decision:** Use an Azure Resource Manager (ARM) template.

**Reason:** The challenge explicitly requires ARM-based infrastructure as code and prohibits relying on manual Azure Portal configuration as the source of truth.

---

## D-017 — Azure Functions Hosting Plan

**Decision:** Use the Consumption plan.

**Reason:** The challenge explicitly requires a Consumption plan and it is appropriate for the project's low-volume workload and cost objective.

---

## D-018 — Backend Repository

**Decision:** Create a dedicated GitHub repository named:

`	sixteen-resume-backend`

**Reason:** The challenge requires a separate backend repository.

---

## D-019 — Frontend Repository

**Decision:** Create a dedicated GitHub repository named:

`	sixteen-resume-frontend`

**Reason:** The challenge requires a separate website repository.

---

## D-020 — CI/CD

**Decision:** Use GitHub Actions for both repositories.

**Backend workflow:**

```text
Push / Pull Request
        ↓
Python tests
        ↓
Build/package
        ↓
Deploy infrastructure/application
```

Deployment should only proceed when the required checks pass.

**Frontend workflow:**

```text
Push
 ↓
Validate/build if applicable
 ↓
Upload website to Azure Storage
 ↓
Purge CDN cache if required
```

---

## D-021 — Git Workflow

**Decision:** Use:

```text
develop → feature/* → PR → CI → merge → main
```

**Reason:** The user wants a structured Git workflow with protected branches and CI validation.

---

## D-022 — Deployment Environments

**Decision:** Use one deployment environment.

**Reason:** The user explicitly requested one deployment and the challenge does not require multiple environments.

---

## D-023 — Azure Region

**Decision:** Use East US.

**Reason:** The user selected East US as the target Azure region.

---

## D-024 — Cost Strategy

**Decision:** Prefer R0/free services and allowances.

If a requirement cannot be fulfilled for free, use the lowest-cost viable option.

**Reason:** Cost minimization is a project constraint.

---

## D-025 — Security

**Decision:** Apply the following baseline:

* No credentials in source control.
* Secrets stored through appropriate GitHub/Azure mechanisms.
* Least-privilege access.
* HTTPS.
* Cosmos DB accessed through the backend API rather than browser JavaScript.
* Infrastructure and deployment configuration maintained in source control.

**Reason:** These controls are necessary for a responsible public cloud portfolio project.

---

## D-026 — Blog Platforms

**Decision:** Publish project-related content on both Dev.to and Hashnode.

**Reason:** The user wants both platforms used.

The content will document:

* Technical lessons.
* Implementation decisions.
* Problems and solutions.
* The overall project journey.

---

## D-027 — Existing AWS Cloud Resume Challenge

**Decision:** Treat the existing AWS Cloud Resume Challenge project as prior experience and source material, not as a replacement for this Azure project.

**Reason:** The Azure challenge must be implemented independently to demonstrate Azure-specific capabilities.

---

## D-028 — Project Deadline

**Decision:** Target completion by 30 September 2026.

---

## D-029 — Production Intent

**Decision:** Build the MVP as a portfolio/learning project while keeping the resulting website suitable for eventual use as the user's production personal website.

**Reason:** This allows the project to remain within challenge scope while providing a practical long-term outcome.


---

## D-030 — Visitor Counter API Contract

**Status:** Superseded by D-036 / OR-006.

The earlier draft defined `POST /api/v1/visitor-count`. The approved MVP contract is now `GET /api/visitors`, with a successful response containing the current visitor count.
---

## D-031 — OR-002 Public Hostname Interpretation

**Decision:** Resolve OR-002 by accepting the selected FreeDNS/afraid.org hosted hostname/subdomain for the MVP.

**Reason:** The project explicitly excludes paid domain registration while requiring a public hostname. The FreeDNS approach satisfies the scoped MVP hostname requirement without claiming ownership of a conventional registrable custom domain.

**Required wording:**

> Public hostname: FreeDNS hosted hostname/subdomain.

**Deviation:** The original challenge describes pointing a custom DNS domain to the CDN endpoint. The MVP uses a hosted subdomain instead and records this as a deliberate deviation from the literal custom-domain wording.

**Acceptance rule:** The approved hostname must resolve publicly to the approved Azure delivery endpoint, serve the resume over HTTPS through the approved delivery architecture, and require no paid domain registration.


---

## D-032 — OR-001 Visitor Semantics

**Decision:** Define a visitor as one successfully committed visitor-counter API operation caused by a top-level resume page load.

**Rules:**
- The frontend performs exactly one counter request per top-level resume page load.
- A refresh counts as another visit.
- The counter does not identify unique humans, browsers, sessions, IP addresses, devices, or users.
- Failed API/database operations do not increment the persisted count.
- Concurrent successful operations must not overwrite one another.
- If the persisted value is N, then K successfully committed counter operations result in N + K.

**Reason:** This provides deterministic, privacy-preserving, static-site-compatible, and testable visitor semantics.

---

## D-033 — OR-002 Public Hostname Interpretation

**Decision:** Use the selected FreeDNS/afraid.org hosted hostname/subdomain for the MVP.

**Required wording:** **Public hostname: FreeDNS hosted hostname/subdomain.**

**Constraint:** The project must not claim ownership of a conventional registrable custom domain and must not require paid domain registration.

**Acceptance:** The hostname must resolve publicly to the approved Azure delivery endpoint, serve the resume, support HTTPS through the approved delivery architecture, and require no paid domain registration.

---

## D-034 — OR-003 Cost Ceiling

**Decision:** Set the MVP hard ceiling to **R100/month recurring Azure/cloud cost**, with **R0/month** as the preferred target where viable.

**Cost policy:**

| Cost | Decision |
|---|---|
| R0/month | Preferred |
| R0–R100/month recurring | Allowed |
| >R100/month recurring | Blocked |
| Paid domain | Out of MVP |
| Unexpected charge | Investigate before continuing |

**Exclusions:** Personal internet access, existing equipment, optional paid domain registration, and one-time purchases explicitly approved later are excluded from the recurring Azure/cloud ceiling.

**Reason:** The numeric ceiling must be objectively testable while leaving room for the approved Azure delivery architecture and its usage charges.


---

## D-035 — OR-004 HTTPS/CDN Architecture Resolution

**Decision:** Freeze the HTTPS/CDN architecture at capability level while leaving the exact Azure edge service/SKU as an implementation choice.

**Required path:**

```text
Browser
   |
   | HTTPS
   v
Public Hostname
   |
   v
Azure CDN / approved Azure edge-delivery service
   |
   v
Azure Storage Static Website
```

**Implementation acceptance conditions:**

- HTTPS is supported.
- Certificate management is supported.
- The public hostname can resolve to the selected edge endpoint.
- Azure Storage remains the origin.
- Configuration can be represented in IaC where applicable.
- Recurring Azure/cloud cost remains <= R100/month for the complete MVP.
- The selected service is available and suitable for the required deployment architecture.

**Reason:** This resolves OR-004 without prematurely locking the project to a specific Azure edge service whose current availability, lifecycle, pricing, or hostname compatibility may change.

**Requirement:** REQ-AZ-005, REQ-AZ-006, REQ-AZ-015.

**Constraint:** A specific service may only be selected after validating it against these frozen conditions.

---

## D-036 — OR-006 Visitor API Contract

**Decision:** The visitor API has exactly one MVP responsibility: `GET /api/visitors`.

The successful response contains the current visitor count.

The browser has no Cosmos DB credentials and no direct Cosmos DB access. Azure Functions remains the application/API boundary.

---

## D-037 — OR-007 Counter Persistence Behavior

**Decision:** Use one logical counter record. For each successful counter operation, the backend reads the current count, atomically increments it, persists it, and returns the resulting count.

The implementation must prevent concurrent lost updates.

---

## D-038 — OR-008 CI/CD Deployment Authority

**Decision:** GitHub Actions is the deployment mechanism. Production deployment from a developer laptop is not a valid production release.

**Backend:** checkout → install dependencies → run tests → validate infrastructure → deploy.

**Frontend:** checkout → validate website → publish to Azure Storage → purge/invalidate edge cache when required.

---

## D-039 — OR-009 Production Release Workflow

**Decision:** `main` represents production.

**Workflow:**

```
feature/*
    ↓
Pull Request
    ↓
CI
    ↓
develop
    ↓
production release
    ↓
main
```

The frontend repository now has a `develop` branch created from `main` to establish the approved development/production branch model.