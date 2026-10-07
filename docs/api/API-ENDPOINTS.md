# API Endpoint Inventory

## Public application endpoints

| Contract ID | Method | Path | Authentication | Authorization | Priority | Status | Requirements |
|---|---|---|---|---|---:|---|---|
| VC-001 | GET | `/api/visitors` | None | Public counter invocation only | P1 | Implementation-ready | REQ-AZ-007..010 |

## Public non-endpoints

The v1 public API intentionally exposes no:

- authentication/login endpoint;
- admin endpoint;
- reset/delete endpoint;
- analytics endpoint;
- user/profile endpoint;
- health endpoint;
- pagination/filtering/sorting endpoint;
- Cosmos DB endpoint.

Operational health and Azure management interfaces remain platform/control-plane concerns and are not public application APIs.

## Architecturally significant internal interfaces

| Contract ID | Interface | Direction | Requirements |
|---|---|---|---|
| DB-001 | VisitorCounter persistence | Azure Function → Cosmos DB Table API | REQ-AZ-008, REQ-AZ-010, REQ-AZ-SEC-003 |
| DEP-001 | Frontend production publication | GitHub Actions → Azure Storage/edge delivery | REQ-AZ-004, REQ-AZ-005, REQ-AZ-014 |
| DEP-002 | Backend production deployment | GitHub Actions → ARM/Function/Cosmos | REQ-AZ-010..013, REQ-AZ-DEV-001, REQ-AZ-FLEX-001..013 |
| DNS-001 | Public hostname resolution | FreeDNS → approved edge endpoint | REQ-AZ-006, REQ-AZ-015 |

## Governance

- VC-001 is the sole public application operation.
- Cosmos DB is never a public browser interface.
- Any new public endpoint requires an approved requirements and contract change.
- No implementation may invent a second contract for the same operation.