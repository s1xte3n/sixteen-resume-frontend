# Data Integrity Review

## Document Control

| Field | Value |
|---|---|
| Phase | Phase 8 — Security, Reliability & Quality |
| Scope | VisitorCounter persistence and Cosmos Table infrastructure |
| Data model | PartitionKey=VisitorCounter, RowKey=Global |
| Evidence level | Source/configuration review; live persistence evidence pending |

## 1. Executive Result

**Data-integrity review status: PASS WITH LIVE PERSISTENCE EVIDENCE PENDING**

The implementation uses one logical counter entity and protects updates with ETag conditional replacement.

## 2. Integrity Controls

| Control | Result | Evidence |
|---|---|---|
| Single logical counter | PASS | `VisitorCounter/Global` is the canonical entity |
| Non-negative count | PASS | Persisted count is validated before increment |
| Atomic logical increment | PASS | ETag + IfNotModified conditional replacement |
| Concurrent creation handling | PASS | ResourceExistsError causes retry |
| Duplicate lost-update protection | PASS | ResourceModifiedError causes retry |
| Table ownership | PASS | ARM provisions the single VisitorCounter table |
| Browser isolation | PASS | Browser has no direct Cosmos access |
| Production persistence | PENDING | Requires deployed Azure verification |
| Backup/recovery evidence | PENDING | Requires approved Azure recovery evidence |

## 3. Data Model

The approved counter record is:

| Field | Value |
|---|---|
| PartitionKey | `VisitorCounter` |
| RowKey | `Global` |
| Count | Non-negative integer |

The browser does not control the partition key, row key, or database operation.

## 4. Failure Handling

Invalid persisted count state raises a dependency error rather than producing an incorrect counter value.

Conditional update conflicts are retried.

Repeated concurrency conflicts eventually produce a controlled dependency failure instead of an unbounded loop.

## 5. Remaining Evidence

The data-integrity gate remains open until:

1. Cosmos Table infrastructure is deployed.
2. The Function identity can read/update the table.
3. A successful increment is persisted.
4. The persisted value survives Function restart/deployment.
5. Controlled concurrent operations demonstrate no lost successful increments.
6. Recovery/backup expectations are documented and verified where applicable.
