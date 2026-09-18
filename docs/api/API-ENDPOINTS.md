# API Endpoint Inventory

| Contract ID | Method | Path | Auth | Priority | Status | Owning requirements |
|---|---|---|---|---|---|---|
| VC-001 | POST | `/api/v1/visitor-count` | Public; no end-user auth | P1 | Draft; acceptance blocked by OR-001 | REQ-AZ-007, REQ-AZ-008, REQ-AZ-009, REQ-AZ-010 |

## Non-endpoints

The v1 API intentionally exposes no:

- GET counter endpoint.
- Reset/delete endpoint.
- Admin endpoint.
- Health endpoint.
- Authentication endpoint.
- User/profile endpoint.
- Analytics endpoint.
- Pagination/filtering/sorting endpoint.

Operational health checks, if required by Azure infrastructure, are not part of the public application contract and must not expose application or database state.

## Endpoint governance

- Public endpoint is versioned under `/api/v1`.
- Cosmos DB is never a public interface.
- Endpoint behavior is governed by `API-CONTRACT.md`.
- Schemas are governed by `API-SCHEMAS.md`.
- Status/error behavior is governed by `API-ERRORS.md`.
