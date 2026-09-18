# Test Data

## Purpose

Safe synthetic data for local development, automated tests, API contract tests, and deployment validation. Production visitor data is never required.

## Synthetic counter fixture

| Field | Rule |
|---|---|
| PartitionKey | TEST |
| RowKey | VISITOR_COUNTER |
| Count | Integer >= 0; initialize to 0 |
| Purpose | Isolated test state |
| Production use | Forbidden |

Production key values come only from the finalized data model.

## API fixtures

Request:

```json
{}
```

Optional request ID:

```
X-Request-ID: 7d3f4a22-1b4f-4d7b-9c0d-7f1c4a8b2d10
```

Success:

```json
{"count":1}
```

Dependency failure:

```json
{"error":{"code":"DEPENDENCY_UNAVAILABLE","message":"The visitor counter is temporarily unavailable.","requestId":"7d3f4a22-1b4f-4d7b-9c0d-7f1c4a8b2d10"}}
```

## Required negative cases

- malformed JSON -> 400
- unsupported request property -> 400
- invalid X-Request-ID -> 400
- wrong method -> 405
- unsupported content type -> 415
- applicable rate limit -> 429
- unexpected failure -> 500
- dependency unavailable -> 503
- dependency timeout -> 504
- count remains a non-negative integer

Exact increment and duplicate semantics remain blocked by OR-001 and must not be invented in tests.

## Test accounts

None. The product has no authentication, admin accounts, profiles, or account lifecycle.

## Resume fixtures

Use synthetic or already-approved public content. Do not place private contact information, internal employer information, or unapproved personal data in fixtures.

## Lifecycle

Local and CI fixtures are disposable. Remote synthetic state must be isolated and cleaned up. Production data must never be copied into tests or used as a test oracle.