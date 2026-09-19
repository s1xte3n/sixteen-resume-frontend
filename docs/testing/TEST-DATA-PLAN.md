# Test Data Plan

## Principles
All data is synthetic, disposable, isolated, and non-sensitive. Production visitor data is never copied into tests.

## Canonical fixtures
| Fixture | Value/rule | Purpose |
|---|---|---|
| Counter | PartitionKey=TEST, RowKey=VISITOR_COUNTER, Count=0 | Baseline |
| Counter N | Same key, Count=N, N>=0 | State transitions |
| Concurrent K | K=2,10,25 | Concurrency |
| Valid request | Empty body | Contract |
| Request ID | UUID v4 | Correlation |
| Invalid request ID | not-a-uuid | Validation |
| Unknown field | unexpected=true | Schema rejection |
| Malformed JSON | { | 400 |
| Error fixture | Canonical error envelope | Error contract |
| Resume fixture | Approved/synthetic public-safe content | UI/content |

## Setup
Create unique test-run state, set known baseline, record baseline, execute, assert API and persistence, then clean up only state created by the run.

## Failure injection
Use mocks/test seams for dependency unavailable, timeout, conditional update conflict, and unexpected exception. Do not disable production controls.

## Cleanup
Local and CI fixtures are disposable. Remote synthetic state is isolated and deleted/restored after tests. Production data is never modified by automated tests.

## Secrets
No Azure keys, connection strings, tokens, passwords, private keys, or private resume information in fixtures, Postman files, logs, or committed environment files.
