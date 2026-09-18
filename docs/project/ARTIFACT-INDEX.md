# Artifact Index

## 1\. Purpose

This document identifies the project's authoritative documentation and current artifact status.

\---

# 2\. Project Documentation

|Artifact|Purpose|Status|Source of Truth|
|-|-|-|-|
|`docs/project/PROJECT-OVERVIEW.md`|Project purpose, users, goals, scope, constraints, stack, deployment, dependencies, assumptions, and risks|Current|Yes|
|`docs/project/PROJECT-STATUS.md`|Current project state, completed/incomplete work, blockers, next gate, and evidence|Current|Yes|
|`docs/project/DECISIONS.md`|Confirmed decisions, rationale, alternatives, consequences, and open decisions|Current|Yes|
|`docs/project/OPEN-QUESTIONS.md`|Discovery-stage unresolved questions, priorities, owners, and decision status|Current|Yes|
|`docs/project/PROJECT-CHARTER.md`|Project scope, MVP, stakeholders, milestones, success criteria, and Definition of Done|Current|Yes|
|`docs/project/ARTIFACT-INDEX.md`|Project artifact index and documentation governance|Updated|Yes|

\---

# 3\. Product Documentation

|Artifact|Purpose|Status|Source of Truth|
|-|-|-|-|
|`docs/product/PRD.md`|Complete product requirements and feature-level requirements|Created|Yes|
|`docs/product/USER-STORIES.md`|User stories and use cases mapped to requirement IDs|Created|Yes|
|`docs/product/ACCEPTANCE-CRITERIA.md`|Testable acceptance criteria for every MVP requirement|Created|Yes|
|`docs/product/SCOPE.md`|MVP, P1/P2/P3 scope, explicit exclusions, and future ideas|Created|Yes|
|`docs/product/OPEN-REQUIREMENTS.md`|Unresolved product decisions, ambiguities, contradictions, hidden dependencies, and untestable requirements|Created|Yes|

\---

# 4\. Source Requirements

|Artifact|Purpose|Status|
|-|-|-|
|Cloud Resume Challenge — Azure requirements|Original challenge requirements baseline|Current|
|Project owner's CV|Resume-content source|Current|
|Approved project state|Project-specific requirements and decisions|Current|

\---

# 5\. Source Code Repositories

|Repository|Purpose|Status|
|-|-|-|
|`github.com/s1xte3n/sixteen-frontend`|Frontend resume application|Exists; empty|
|`github.com/s1xte3n/sixteen-backend`|Backend/API application|Exists; empty|

\---

# 6\. Current Implementation Artifacts

|Artifact|Status|
|-|-|
|Frontend source code|Not started|
|Backend source code|Not started|
|ARM templates|Not started|
|Python tests|Not started|
|GitHub Actions frontend workflow|Not started|
|GitHub Actions backend workflow|Not started|
|Azure project resources|No project resources confirmed|
|Public deployment|Not started|
|Public hostname|Not selected|
|Blog post|Not created|

\---

# 7\. Branch Model

|Branch|Intended Role|Current Status|
|-|-|-|
|`develop`|Development/integration|Intended|
|`main`|Production|Intended|

The repositories are currently empty, so actual branch implementation/state still needs to be established.

\---

# 8\. External Artifacts

## Resume Content

The supplied CV is the current source material for the public resume.

Before production deployment, final public content must be reviewed and approved by the project owner.

**Status:** Awaiting final public-content approval.

## Blog Post

A project-learning blog post is required by the approved MVP scope.

**Status:** Not created.

**Platform:** Undecided.

\---

# 9\. Product Requirements Artifacts

## PRD

**Path:** `docs/product/PRD.md`

**Status:** Created.

**Purpose:** Defines the product purpose, actors, confirmed requirements, assumptions, MVP requirements, non-functional requirements, contradictions, and completion gate.

## User Stories

**Path:** `docs/product/USER-STORIES.md`

**Status:** Created.

**Purpose:** Maps user stories and use cases to product requirement IDs.

## Acceptance Criteria

**Path:** `docs/product/ACCEPTANCE-CRITERIA.md`

**Status:** Created.

**Purpose:** Provides testable acceptance criteria for every MVP requirement.

## Scope

**Path:** `docs/product/SCOPE.md`

**Status:** Created.

**Purpose:** Defines MVP, P1, P2, P3, explicit exclusions, and scope governance.

## Open Requirements

**Path:** `docs/product/OPEN-REQUIREMENTS.md`

**Status:** Created.

**Purpose:** Tracks unresolved decisions, ambiguities, contradictions, hidden dependencies, missing requirements, and requirements that cannot yet be objectively tested.

\---

# 10\. Product Phase Status

**Requirements documentation:** Created.

**MVP acceptance coverage:** Complete.

**PRD closure:** Pending explicit resolution of P1 product decisions.

Current P1 open items:

1. Visitor-count semantics.
2. Free hostname/subdomain versus original custom-domain interpretation.
3. Numeric cost ceiling.
4. HTTPS/CDN service suitability and cost validation.
5. Final public resume-content approval.

No implementation tasks are defined by these product documents.

\---

# 11\. Artifact Governance

When a requirement, decision, or project state changes:

1. Update the affected product or project document.
2. Record significant confirmed decisions in `docs/project/DECISIONS.md`.
3. Record unresolved decisions in `docs/product/OPEN-REQUIREMENTS.md` or `docs/project/OPEN-QUESTIONS.md`, depending on whether they are product or project-level.
4. Update `docs/project/PROJECT-STATUS.md` when implementation state changes.
5. Synchronize this artifact index.
6. Do not silently change confirmed requirements.
7. Do not mark unresolved requirements as complete without explicit evidence.

\---

# 12\. PRD Closure Rule

The requirements phase is complete only when:

* Every MVP feature has testable acceptance criteria.
* No high-impact ambiguity is hidden.
* All P0/P1 requirements are explicitly resolved or formally accepted as a documented deviation.
* The final scope is reflected consistently across the product and project documentation.

