# Requirements Traceability — API / Interface Contract

## 1. Public API traceability

| Requirement ID | Contract ID | Operation/interface | Acceptance | Test/verification |
|---|---|---|---|---|
| REQ-AZ-007 | VC-001 | GET /api/visitors | AC-007 | VT-007 |
| REQ-AZ-008 | VC-001, DB-001 | Counter persistence | AC-008 | VT-008 |
| REQ-AZ-009 | VC-001 | GET /api/visitors | AC-009 | VT-009 |
| REQ-AZ-010 | VC-001, DB-001 | Python Function + persistence | AC-010 | VT-010 |
| REQ-AZ-SEC-002 | VC-001, DB-001 | Browser/API/Cosmos boundary | Global security acceptance | VT-SEC-002 |
| REQ-AZ-SEC-003 | DB-001, DEP-001, DEP-002 | Least-privilege identities | Security acceptance | VT-SEC-003 |

## 2. Deployment/interface traceability

| Requirement ID | Contract ID | Interface | Acceptance | Test/verification |
|---|---|---|---|---|
| REQ-AZ-004 | DEP-001 | Frontend publication to Azure Storage | AC-004 | VT-004 |
| REQ-AZ-005 | DNS-001, DEP-001 | HTTPS/edge delivery | AC-005 | VT-005 |
| REQ-AZ-006 | DNS-001 | Public hostname resolution | AC-006 | VT-006 |
| REQ-AZ-011 | DEP-002 | Backend CI test gate | AC-011 | VT-011 |
| REQ-AZ-012 | DEP-002 | ARM infrastructure deployment | AC-012 | VT-012 |
| REQ-AZ-013 | DEP-002 | Backend CI/CD | AC-013 | VT-013 |
| REQ-AZ-014 | DEP-001 | Frontend CI/CD publication | AC-014 | VT-014 |
| REQ-AZ-015 | VC-001, DEP-001, DEP-002, DNS-001 | Production integration | AC-015 | VT-015 |
| REQ-AZ-DEV-001 | DEP-002 | Source-controlled IaC | — | VT-IAC-001 |
| REQ-AZ-REG-001 | DEP-002 | Azure resource location | — | VT-REG-001 |
| REQ-AZ-GIT-001 | DEP-001, DEP-002 | develop/main workflow | — | VT-GIT-001 |
| REQ-AZ-COST-001 | DEP-001, DEP-002, DNS-001 | Cost-constrained deployment | — | VT-COST-001 |

## 3. Flex traceability

| Requirement ID | Contract ID | Interface | Acceptance | Test |
|---|---|---|---|---|
| REQ-AZ-FLEX-001 | DEP-002 | Function hosting | AC-FLEX-001 | VT-FLEX-001 |
| REQ-AZ-FLEX-002 | DEP-002 | Function runtime | AC-FLEX-002 | VT-FLEX-002 |
| REQ-AZ-FLEX-003 | DEP-002 | Scale configuration | AC-FLEX-003 | VT-FLEX-003 |
| REQ-AZ-FLEX-004 | DEP-002 | Blob-container deployment | AC-FLEX-004 | VT-FLEX-004 |
| REQ-AZ-FLEX-005 | DEP-002 | Deployment identity/storage | AC-FLEX-005 | VT-FLEX-005 |
| REQ-AZ-FLEX-006 | DEP-002 | Runtime storage | AC-FLEX-006 | VT-FLEX-006 |
| REQ-AZ-FLEX-007 | DB-001 | Function identity/Cosmos | AC-FLEX-007 | VT-FLEX-007 |
| REQ-AZ-FLEX-008 | DEP-002 | Flex CI/CD | AC-FLEX-008 | VT-FLEX-008 |
| REQ-AZ-FLEX-009 | DEP-002 | ARM functionAppConfig | AC-FLEX-009 | VT-FLEX-009 |
| REQ-AZ-FLEX-010 | DEP-002 | East US capacity | AC-FLEX-010 | VT-FLEX-010 |
| REQ-AZ-FLEX-011 | VC-001 | API unchanged | AC-FLEX-011 | VT-FLEX-011 |
| REQ-AZ-FLEX-012 | DEP-002 | Deployment failure gate | AC-FLEX-012 | VT-FLEX-012 |
| REQ-AZ-FLEX-013 | DEP-002 | Cost-constrained Flex deployment | AC-FLEX-013 | VT-FLEX-013 |

## 4. Acceptance mapping

| Contract | Required acceptance set |
|---|---|
| VC-001 | AC-007, AC-008, AC-009, AC-010 |
| DB-001 | AC-008, AC-010, AC-FLEX-007 |
| DEP-001 | AC-004, AC-005, AC-014 |
| DEP-002 | AC-010..013, AC-FLEX-001..013 |
| DNS-001 | AC-006, AC-015 |

## 5. Traceability status

The contract-to-requirement mapping is complete for all requirements affected by API/runtime/deployment interfaces.

Implementation, execution, CI and production evidence remain separate gates and are not claimed by this document.