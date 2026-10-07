# Test Matrix

## Requirement ID -> Test ID

| Requirement | Priority | Test IDs | Primary Coverage |
|---|---:|---|---|
| REQ-AZ-001 | P1 | T-001-P, T-001-N, T-001-SEC, T-001-R | content, privacy, regression |
| REQ-AZ-002 | P1 | T-002-P, T-002-V, T-002-R | HTML, rendering |
| REQ-AZ-003 | P1 | T-003-P, T-003-B, T-003-F, T-003-R | CSS, responsive, resilience |
| REQ-AZ-004 | P1 | T-004-P, T-004-G, T-004-R | Azure Storage hosting |
| REQ-AZ-005 | P1 | T-005-P, T-005-SEC, T-005-G, T-005-B | HTTPS, CDN, cost |
| REQ-AZ-006 | P1 | T-006-P, T-006-V, T-006-G, T-006-F | DNS |
| REQ-AZ-007 | P1 | T-007-P, T-007-N, T-007-V, T-007-I, T-007-S, T-007-SEC, T-007-R | counter frontend |
| REQ-AZ-008 | P1 | T-008-P, T-008-S, T-008-D, T-DATA-001, T-DATA-002, T-008-F | persistence |
| REQ-AZ-009 | P1 | T-009-P, T-009-N, T-009-V, T-009-A, T-009-Z, T-009-C, T-009-G, T-009-SEC, T-009-F | API contract |
| REQ-AZ-010 | P1 | T-010-P, T-010-Z, T-010-F, T-010-SEC | Function/security |
| REQ-AZ-011 | P1 | T-011-P, T-011-N, T-011-G, T-011-R | Python CI tests |
| REQ-AZ-012 | P1 | T-012-P, T-012-N, T-012-G, T-012-R | ARM/IaC |
| REQ-AZ-013 | P1 | T-013-P, T-013-N, T-013-SEC, T-013-G | backend CI/CD |
| REQ-AZ-014 | P1 | T-014-P, T-014-N, T-014-SEC, T-014-G | frontend CI/CD |
| REQ-AZ-015 | P0 | T-015-E2E, T-015-SEC, T-015-COST, T-REL-001 | production integration |
| REQ-AZ-016 | P2 | T-016-P, T-016-V, T-016-R | article |
| REQ-AZ-SEC-001 | P0 | T-SEC-001, T-SEC-001-R | secret security |
| REQ-AZ-SEC-002 | P0 | T-SEC-002, T-007-SEC, T-009-SEC | database boundary |
| REQ-AZ-SEC-003 | P1 | T-010-Z, T-SEC-003 | least privilege |
| REQ-AZ-SEC-004 | P0 | T-005-P, T-005-SEC, T-SEC-004 | HTTPS |
| REQ-AZ-COST-001 | P1 | T-005-B, T-COST-001 | cost |
| REQ-AZ-REG-001 | P2 | T-REG-001 | region |
| REQ-AZ-GIT-001 | P1 | T-013-G, T-GIT-001 | branch model |
| REQ-AZ-DEV-001 | P1 | T-012-N, T-IAC-001 | reproducible IaC |
| REQ-AZ-DEV-002 | P1 | T-CERT-001 | certification wording |

---

# Test Category Matrix

| Test ID | Positive | Negative | Validation | Auth | AuthZ | Isolation | State | Boundary | Persistence | Contract | Integration | Regression | Security | Failure |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| T-001-P | X | | | | | X | | | | | | | X | |
| T-002-P | X | | X | | | | | X | | | | X | | |
| T-003-B | X | | | | | | | X | | | | X | | |
| T-004-P | X | | | | X | X | | | | | X | X | X | |
| T-005-P | X | | | | | | | X | | | X | X | X | |
| T-006-P | X | X | | | | | | X | | | X | X | | X |
| T-007-P | X | | X | | | X | X | | X | X | X | X | X | |
| T-DATA-001 | X | | | | | X | X | X | X | | X | X | X | |
| T-DATA-002 | | X | | | | X | X | X | X | | X | X | X | X |
| T-009-P | X | | X | | | X | X | X | X | X | X | X | X | |
| T-009-N | | X | X | | X | X | X | X | X | X | X | X | X | |
| T-009-SEC | | X | | X | X | X | | | | X | X | X | X | X |
| T-010-P | X | | X | X | X | X | X | | X | X | X | X | X | |
| T-011-P | X | | | | X | X | X | | | | X | X | X | X |
| T-012-P | X | | X | X | X | X | | X | | | X | X | X | X |
| T-013-P | X | | | X | X | X | X | | | | X | X | X | X |
| T-014-P | X | | | X | X | X | X | | | | X | X | X | X |
| T-015-E2E | X | X | X | X | X | X | X | X | X | X | X | X | X | X |

---

# Coverage Rule

Every P0/P1 requirement must have:

1. at least one positive test;
2. at least one negative or failure test where applicable;
3. validation testing where inputs exist;
4. security testing where a security boundary exists;
5. persistence testing where state is stored;
6. contract testing for public APIs;
7. integration testing where components interact;
8. regression coverage for change-sensitive behavior.

A missing applicable test dimension is a coverage defect.


## Phase 1 Flex verification rows
| Test ID | Requirement | Scenario | Type |
| T-FLEX-001 | REQ-AZ-FLEX-001 | FC1 Linux hosting | Configuration |
| T-FLEX-002 | REQ-AZ-FLEX-002 | v4/Python 3.12 runtime | Configuration |
| T-FLEX-003 | REQ-AZ-FLEX-003 | scale-to-zero/zero always-ready | Configuration |
| T-FLEX-004 | REQ-AZ-FLEX-004 | deployment storage/package contract | Deployment |
| T-FLEX-005 | REQ-AZ-FLEX-005 | managed-identity Storage access | Security/IAM |
| T-FLEX-006 | REQ-AZ-FLEX-006 | identity-based runtime storage | Configuration/Security |
| T-FLEX-007 | REQ-AZ-FLEX-007 | Cosmos Table identity authorization | Security |
| T-FLEX-008 | REQ-AZ-FLEX-008 | Flex-compatible CI/CD deployment | CI/CD |
| T-FLEX-009 | REQ-AZ-FLEX-009 | functionAppConfig ARM structure | IaC |
| T-FLEX-010 | REQ-AZ-FLEX-010 | East US Flex capacity | Deployment |
| T-FLEX-011 | REQ-AZ-FLEX-011 | GET /api/visitors regression | Contract |
| T-FLEX-012 | REQ-AZ-FLEX-012 | deployment failure blocks release | Failure/CI |
| T-FLEX-013 | REQ-AZ-FLEX-013 | R100/month ceiling | Cost/Governance |
