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

## D-009 — HTTPS/CDN Delivery

**Decision:** Use Cloudflare Free proxy/CDN to provide the public HTTPS/CDN delivery layer in front of the Azure Storage static website.

**Reason:** Azure Front Door Standard has a current US$35/month base fee, while Azure CDN from Microsoft (classic) no longer accepts new profiles/domains. Cloudflare Free provides CDN and Universal SSL at no recurring plan charge.

**Deviation:** The delivery/CDN provider is not Azure CDN. Azure Storage remains the required static website origin.

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

**Decision:** Prefer R0/free services and allowances, with a measurable MVP ceiling of **US$5/month for recurring cloud/service costs**.

Planned one-time domain registration cost is **US$0** because the MVP uses the approved free-hostname/subdomain interpretation. Any future paid service or domain outside these limits requires an explicit project decision.

**Reason:** Cost minimization is a project constraint and must be objectively testable.

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

**Decision:** Define a versioned public HTTP API as `POST /api/v1/visitor-count` with an empty JSON request and a JSON response containing the persisted `count`.

**Reason:** The browser requires an explicit API boundary to the Python Azure Function, while the API must not expose Cosmos DB access or unrelated application functionality.

**Contract controls:**

- No end-user authentication.
- Production CORS uses an explicit resume-origin allowlist.
- Success response field: `count`, non-negative integer.
- Canonical errors use `code`, `message`, and UUID v4 `requestId`.
- v1 has no pagination, filtering, sorting, reset, delete, admin, or analytics operations.
- Breaking wire changes require a new API major version.

**Requirement Addressed:** REQ-AZ-007, REQ-AZ-008, REQ-AZ-009, REQ-AZ-010.

**Architecture Addressed:** ADR-002, ADR-003, ADR-007.

**Constraint:** Visitor semantics are resolved under OR-001. Duplicate HTTP requests are separate counter operations unless a future requirement explicitly introduces idempotency semantics; concurrent successful operations must not lose increments.


---

## D-031 — OR-002 Public Hostname Interpretation

**Decision:** Resolve OR-002 by accepting the selected FreeDNS/afraid.org hosted hostname/subdomain for the MVP.

**Reason:** The project explicitly excludes paid domain registration while requiring a public hostname. The FreeDNS approach satisfies the scoped MVP hostname requirement without claiming ownership of a conventional registrable custom domain.

**Required wording:**

> Public hostname: FreeDNS hosted hostname/subdomain.

**Deviation:** The original challenge describes pointing a custom DNS domain to the CDN endpoint. The MVP uses a hosted subdomain instead and records this as a deliberate deviation from the literal custom-domain wording.

**Acceptance rule:** The approved hostname must resolve publicly through the approved Cloudflare delivery path to the Azure Storage static website, serve the resume over HTTPS, and require no paid domain registration.
