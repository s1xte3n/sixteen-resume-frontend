# Canonical Test Matrix

| Requirement | Test IDs | Priority |
|---|---|---|
| REQ-AZ-001 | T-001-P, T-001-N, T-001-SEC, T-001-R | P1 |
| REQ-AZ-002 | T-002-P, T-002-V, T-002-R | P1 |
| REQ-AZ-003 | T-003-P, T-003-B, T-003-F, T-003-R | P1 |
| REQ-AZ-004 | T-004-P, T-004-G, T-004-R | P1 |
| REQ-AZ-005 | T-005-P, T-005-SEC, T-005-G, T-005-B | P0 |
| REQ-AZ-006 | T-006-P, T-006-V, T-006-G, T-006-F | P1 |
| REQ-AZ-007 | T-007-P, T-007-N, T-007-V, T-007-I, T-007-S, T-007-SEC, T-007-R | P1 |
| REQ-AZ-008 | T-008-P, T-008-S, T-008-D, T-DATA-001, T-DATA-002, T-008-F | P0 |
| REQ-AZ-009 | T-009-P, T-009-N, T-009-V, T-009-A, T-009-Z, T-009-C, T-009-G, T-009-SEC, T-009-F | P1 |
| REQ-AZ-010 | T-010-P, T-010-Z, T-010-F, T-010-SEC | P1 |
| REQ-AZ-011 | T-011-P, T-011-N, T-011-G, T-011-R | P1 |
| REQ-AZ-012 | T-012-P, T-012-N, T-012-G, T-012-R | P1 |
| REQ-AZ-013 | T-013-P, T-013-N, T-013-SEC, T-013-G | P1 |
| REQ-AZ-014 | T-014-P, T-014-N, T-014-SEC, T-014-G | P1 |
| REQ-AZ-015 | T-015-E2E, T-015-SEC, T-015-COST, T-REL-001 | P0 |
| REQ-AZ-016 | T-016-P, T-016-V, T-016-R | P2 |
| REQ-AZ-SEC-001 | T-SEC-001, T-SEC-001-R | P0 |
| REQ-AZ-SEC-002 | T-SEC-002, T-007-SEC | P0 |
| REQ-AZ-SEC-003 | T-SEC-003, T-010-Z, T-013-SEC | P0 |
| REQ-AZ-SEC-004 | T-SEC-004, T-005-SEC | P0 |
| REQ-AZ-COST-001 | T-COST-001, T-005-B, T-015-COST | P0 |
| REQ-AZ-REG-001 | T-REG-001 | P2 |
| REQ-AZ-GIT-001 | T-GIT-001, T-013-G, T-014-G | P1 |
| REQ-AZ-DEV-001 | T-IAC-001, T-012-G | P1 |
| REQ-AZ-DEV-002 | T-CERT-001 | P1 |

## Coverage
Positive, negative, validation, state, persistence, contract, integration, regression, security, and failure are represented. Authentication is N/A for public VC-001 but applies to deployment/service identities. Authorization is covered by T-009-Z, T-010-Z, and T-SEC-003. Isolation is covered by T-007-I and T-SEC-002.

Every listed ID is detailed in TEST-CASES.md. A requirement is not closed merely because an endpoint returned 2xx.
