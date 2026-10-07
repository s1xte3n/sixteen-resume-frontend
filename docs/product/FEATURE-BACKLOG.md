# Feature Backlog

## 1. Purpose and Gate

This is the executable backlog only. A requirement enters this backlog only when its required behavior is stable, acceptance criteria are objectively testable, dependencies are known, and no unresolved P0/P1 decision changes its implementation shape.

Ambiguous or blocked requirements are recorded in `REQUIREMENT-GAPS.md` and are deliberately not represented as implementation tasks.

## 2. Implementation-Ready Items

### BL-AZ-001 — HTML Resume Foundation

**Requirement:** REQ-AZ-002  
**Priority:** P1  
**Dependencies:** REQ-AZ-001 content approval  
**Verification:** VT-002  
**Acceptance:** HTML delivers the approved resume content without requiring a document viewer.

### BL-AZ-002 — CSS Resume Presentation

**Requirement:** REQ-AZ-003  
**Priority:** P1  
**Dependencies:** BL-AZ-001  
**Verification:** VT-003  
**Acceptance:** Intentional styling; readable on agreed mobile/desktop validation viewports; underlying content remains accessible if CSS fails.

### BL-AZ-003 — Azure Storage Hosting Boundary

**Requirement:** REQ-AZ-004  
**Priority:** P1  
**Dependencies:** BL-AZ-001, BL-AZ-002  
**Verification:** VT-004  
**Acceptance:** Required static assets are served from Azure Storage through the approved delivery path.

### BL-AZ-004 — Python Function Foundation

**Requirement:** REQ-AZ-010  
**Priority:** P1  
**Dependencies:** None at product-behavior level  
**Verification:** VT-010  
**Acceptance:** Python Azure Function can execute the approved HTTP-triggered backend behavior and use only required data-access permissions.

### BL-AZ-005 — ARM Infrastructure Boundary

**Requirement:** REQ-AZ-012, REQ-AZ-DEV-001  
**Priority:** P1  
**Dependencies:** BL-AZ-003, BL-AZ-004, final approved architecture  
**Verification:** VT-012, VT-IAC-001  
**Acceptance:** Required infrastructure is represented in source-controlled ARM and normal provisioning does not depend on undocumented manual production configuration.

## 3. Acceptance-Gated Requirements / Implementation Dependencies

| Requirement | Blocking decision/dependency | Status |
|---|---|---|
| REQ-AZ-001 | Final public-content owner approval | ACCEPTANCE GATE |
| REQ-AZ-005 | Edge-service validation and cost evidence | ACCEPTANCE GATE |
| REQ-AZ-006 | Hostname provisioning and delivery validation | ACCEPTANCE GATE |
| REQ-AZ-007 | Implement approved visitor semantics and failure behavior | IMPLEMENTATION |
| REQ-AZ-008 | Implement concurrency-safe persistence | IMPLEMENTATION |
| REQ-AZ-009 | Implement and test frozen API contract | IMPLEMENTATION |
| REQ-AZ-011 | pytest suite and CI execution | IMPLEMENTATION |
| REQ-AZ-013 | Backend GitHub Actions and secure deployment identity | IMPLEMENTATION |
| REQ-AZ-014 | Frontend GitHub Actions and edge-cache publication flow | IMPLEMENTATION |
| REQ-AZ-015 | Complete production integration and acceptance evidence | ACCEPTANCE GATE |
| REQ-AZ-016 | Publish and validate Dev.to/Hashnode learning article | IMPLEMENTATION / ACCEPTANCE |

## 4. Cross-Cutting Controls

REQ-AZ-SEC-001 and REQ-AZ-SEC-002 are mandatory controls for all implementation work. They are not standalone feature tasks; every relevant change must preserve them.

REQ-AZ-015 remains a production acceptance gate. Its implementation dependencies are now defined and may be executed during Phase 7.

## 5. Backlog Entry Rule

A new implementation item requires:

1. Stable canonical requirement ID.
2. Known inputs and dependencies.
3. Objectively testable acceptance criteria.
4. Verification ID.
5. No unresolved P0/P1 ambiguity affecting behavior, interface, security boundary, cost, or architecture.

No implementation task is created for unresolved requirements merely to make the backlog appear complete.
