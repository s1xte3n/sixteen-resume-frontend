# Architecture Decision Record Index

## 1. Purpose

This index identifies the architecture decisions governing the Azure Cloud Resume Challenge.

---

## 2. ADR Catalogue

| ADR | Decision | Status | Requirements |
|---|---|---|---|
| ADR-001 | Static HTML/CSS/JS frontend on Azure Storage | Accepted | REQ-AZ-001..004 |
| ADR-002 | Azure Function as API/database boundary | Accepted | REQ-AZ-007..010 |
| ADR-003 | Cosmos DB Table API for counter persistence | Accepted | REQ-AZ-008 |
| ADR-004 | ARM + GitHub Actions deployment architecture | Accepted | REQ-AZ-011..014 |
| ADR-005 | Least-privilege secure CI/CD authentication | Accepted in principle | REQ-AZ-SEC-001..003 |
| ADR-006 | Capability-based HTTPS/CDN delivery architecture; exact edge service selected during implementation validation | Accepted | REQ-AZ-005, REQ-AZ-006, REQ-AZ-015 |
| ADR-007 | Visitor-count semantics | **Pending approval** | REQ-AZ-007..009 |

---

## 3. ADR Status Definitions

### Accepted

Architecture direction is approved and may be implemented.

### Accepted in principle

Requirement direction is approved, but implementation-specific details remain open.

### Pending validation

The requirement is approved, but current service/configuration feasibility must be validated.

### Pending approval

A product requirement must be explicitly decided before architecture can be frozen.

---

## 4. Architecture Freeze Gate

Before implementation of affected components:

- ADR-006 must be implemented against its frozen acceptance conditions.
- ADR-007 must be resolved.
- Repository naming must be normalized.
- Cost ceiling must be defined.
- Hostname interpretation must be approved.
