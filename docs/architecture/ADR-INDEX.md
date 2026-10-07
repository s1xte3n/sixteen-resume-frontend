# Architecture Decision Record Index

## 1. Purpose

This index identifies the architecture decisions governing the Azure Cloud Resume Challenge.

## 2. ADR Catalogue

| ADR | Decision | Status | Requirements |
|---|---|---|---|
| ADR-001 | Static HTML/CSS/JS frontend on Azure Storage | Accepted | REQ-AZ-001..004 |
| ADR-002 | Azure Function as API/database boundary | Accepted | REQ-AZ-007..010 |
| ADR-003 | Cosmos DB Table API for counter persistence | Accepted | REQ-AZ-008 |
| ADR-004 | ARM + GitHub Actions deployment architecture | Accepted | REQ-AZ-011..014 |
| ADR-005 | Least-privilege secure CI/CD authentication | Accepted in principle | REQ-AZ-SEC-001..003 |
| ADR-006 | Capability-based HTTPS/CDN delivery architecture; exact edge service selected during implementation validation | Accepted at capability level; implementation validation pending | REQ-AZ-005, REQ-AZ-006, REQ-AZ-015 |
| ADR-007 | Visitor-count semantics | **Accepted** | REQ-AZ-007..009 |
| ADR-008 | Azure Functions Flex Consumption hosting | Accepted — current | REQ-AZ-010..013, REQ-AZ-SEC-003, REQ-AZ-COST-001 |

## 3. ADR Status Definitions

### Accepted

Architecture direction is approved and may be implemented.

### Accepted in principle

Requirement direction is approved, but implementation-specific details remain open.

### Pending validation

The requirement is approved, but current service/configuration feasibility must be validated.

### Pending approval

A product decision has not yet been approved. No affected implementation may treat it as frozen.

## 4. Architecture Freeze / Implementation Validation

- ADR-007 visitor semantics is resolved and must be treated as frozen.
- ADR-006 remains a capability-level architecture decision; exact edge-service selection is an implementation validation gate constrained by HTTPS, hostname, Storage origin, IaC and R100/month conditions.
- Repository naming, cost ceiling and hostname interpretation are already resolved in the requirements/decision baseline.
