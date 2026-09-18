# Requirement Gaps

## 1. Purpose

This document contains vague, contradictory, duplicated, deferred, or objectively unverifiable requirements.

These items are deliberately excluded from the executable feature backlog until resolved.

---

# 2. P1 Gaps

## GAP-AZ-001 — Visitor Definition

**Source:** OR-001

**Affected requirements:**

* REQ-AZ-007
* REQ-AZ-008
* REQ-AZ-009
* REQ-AZ-015

**Problem:**

"Visitor" is undefined.

Possible interpretations include:

* Page load
* API request
* Browser session
* Unique visitor
* Another explicit unit

**Why it matters:**

The counter cannot be objectively tested until the counting unit is defined.

**Classification:** Ambiguous / unverifiable

**Status:** OPEN

**No implementation task:** Correct. Do not implement counting semantics until resolved.

---

## GAP-AZ-002 — FreeDNS vs Custom Domain

**Source:** OR-002 / IC-001

**Affected requirements:**

* REQ-AZ-006
* REQ-AZ-015

**Problem:**

The original challenge specifies a custom DNS domain, while project documentation excludes paid domain purchase and selects FreeDNS/free hostname/subdomain.

**Classification:** Contradictory

**Status:** OPEN

**Required resolution:**

Explicitly state that the free hostname/subdomain is an approved project deviation from the original custom-domain interpretation, or change the scope.

**No implementation task:** Correct. DNS implementation remains blocked.

---

## GAP-AZ-003 — Numeric Cost Ceiling

**Source:** OR-003 / NTR-001

**Affected requirements:**

* REQ-AZ-005
* REQ-AZ-006
* REQ-AZ-012
* REQ-AZ-015

**Problem:**

"Zero/near-zero", "R0 where possible", and "lowest possible cost" do not define an objectively testable threshold.

**Classification:** Unverifiable

**Status:** OPEN

**Required resolution:**

Define a maximum cost, for example a monthly or annual amount.

**No implementation task:** Correct.

---

## GAP-AZ-004 — HTTPS/CDN Configuration

**Source:** OR-004 / IC-003

**Affected requirements:**

* REQ-AZ-005
* REQ-AZ-006
* REQ-AZ-014
* REQ-AZ-015

**Problem:**

The project direction requires Azure Storage, HTTPS, CDN capability, public hostname, and low cost, but the exact delivery service/configuration has not been validated.

**Classification:** Unresolved architecture requirement

**Status:** OPEN

**Required evidence:**

* Service availability
* HTTPS/certificate support
* DNS compatibility
* Azure Storage compatibility
* Current pricing
* Cache behavior

**No implementation task:** Correct.

---

## GAP-AZ-005 — Final Public Resume Content

**Source:** OR-005

**Affected requirements:**

* REQ-AZ-001
* REQ-AZ-015

**Problem:**

The CV is available, but the final public subset has not been explicitly approved.

**Classification:** Content approval gap

**Status:** OPEN

**Required resolution:**

Owner approval of:

* Personal information
* Contact information
* Employment history
* Skills
* Certifications
* Education
* Projects
* External links

**No implementation task:** Do not treat content publication as complete.

---

## GAP-AZ-006 — Repository Naming

**Source:** PRD/project-state inconsistency

**Problem:**

Documentation contains:

* `sixteen-frontend`
* `sixteen-backend`

and:

* `sixteen-resume-frontend`
* `sixteen-resume-backend`

The actual requested repository is `sixteen-resume-frontend`.

**Classification:** Contradictory

**Status:** OPEN

**Impact:**

Backend and frontend CI/CD traceability, repository evidence, and artifact references.

---

# 3. P2 Gaps

## GAP-AZ-007 — Visitor API Contract

**Source:** OR-008

**Affected requirements:**

* REQ-AZ-009
* REQ-AZ-010

The following remain undefined:

* HTTP method
* Endpoint
* Request inputs
* Optional/required parameters
* Success response
* Error responses
* Status codes
* CORS behavior
* Counter semantics

**Classification:** Ambiguous

**Status:** OPEN

---

## GAP-AZ-008 — Counter Failure UX

**Source:** OR-009

**Affected requirements:**

* REQ-AZ-007
* REQ-AZ-009

Undefined behavior when API/database fails.

Potential behaviors documented by the source material include:

* Hide counter
* Display unavailable state
* Display last known value
* Another approved fallback

**Classification:** Ambiguous

**Status:** OPEN

---

## GAP-AZ-009 — Python Test Framework

**Source:** OR-006

**Affected requirements:**

* REQ-AZ-011
* REQ-AZ-013

The testing requirement is confirmed, but framework selection is intentionally deferred.

**Classification:** Deferred implementation decision

**Status:** DEFERRED

---

## GAP-AZ-010 — Blog Platform

**Source:** OR-007

**Problem:**

Project-state documentation says Dev.to and Hashnode are selected, while the open-requirements documentation says the blog platform remains unresolved.

**Classification:** Contradictory documentation

**Status:** OPEN

**Required resolution:**

Normalize whether:

1. Both platforms are mandatory;
2. Either platform is acceptable;
3. One is primary and the other optional.

---

## GAP-AZ-011 — Browser Support

**Source:** OR-010 / NTR-005

No browser/version baseline is defined.

**Classification:** Unverifiable

**Status:** OPEN

---

## GAP-AZ-012 — Availability Target

**Source:** OR-011

No explicit production availability target exists.

**Classification:** Unspecified

**Status:** OPEN

---

## GAP-AZ-013 — DNS Propagation

**Source:** OR-012

No acceptable propagation/stability expectation is defined.

**Classification:** Unverifiable

**Status:** OPEN

---

# 4. P3 Gaps

## GAP-AZ-014 — Blog Link Behavior

**Source:** OR-013

Undefined whether the blog link opens in the same tab or a new tab.

**Classification:** Minor UX ambiguity

**Status:** OPEN

This does not block the core implementation.

---

# 5. Missing Non-Functional Requirements

The approved requirements do not objectively specify:

* Accessibility target
* Performance target
* Cache freshness target
* Availability SLO
* DNS propagation SLA
* Rollback expectation
* Monitoring/alerting requirement
* Exact blog article length
* Exact resume section minimum
* Counter failure UX

These must not be silently invented.

---

# 6. Deliberate Deviation

## GAP-AZ-015 — AZ-900

The original challenge calls for AZ-900 or an advanced Azure certification.

The approved project state intentionally uses AI-901.

**Classification:** Deliberate deviation

**Status:** ACCEPTED-DEVIATION

The project must not claim literal AZ-900 compliance unless AZ-900 is subsequently obtained.

---

# 7. Documentation Consistency Gap

## GAP-AZ-016 — Artifact Index Filename

The current Artifact Index references:

`docs/project/OPEN-QUESTIONS.md`

The repository currently contains:

`docs/project/UNRESOLVED-QUESTIONS.md`

**Classification:** Documentation inconsistency

**Status:** OPEN

**Required action:** Normalize the filename references.

---

# 8. Gap Closure Rule

A gap is closed only when:

1. The decision is explicitly recorded.
2. Affected requirements are updated.
3. Acceptance criteria are updated if necessary.
4. Traceability is updated.
5. Dependencies are recalculated.
6. The executable backlog is updated only after the requirement becomes implementation-ready.

No gap should be silently resolved through implementation assumptions.
