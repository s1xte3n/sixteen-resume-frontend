# Test Data Plan

## 1. Purpose

Define safe synthetic data, fixtures, accounts, test state, setup, isolation, and cleanup.

No production secrets or private production data are permitted.

---

# 2. Data Classes

| Class | Example | Persistent? | Secret? |
|---|---|---:|---:|
| API input | empty GET request | No | No |
| Request ID | UUID v4 | No | No |
| Counter state | synthetic integer | Test-only | No |
| Error fixture | canonical error envelope | No | No |
| Resume fixture | approved/synthetic content | Test-only | No |
| API URL | test endpoint | No | No |
| Azure credential | GitHub/Azure secret | Yes | YES |
| Cosmos credential | managed identity/config | Yes | YES |

Secrets are never committed to fixtures.

---

# 3. Counter Fixtures

## Fixture A — Initial State

```json
{
  "partitionKey": "visitor-counter-test",
  "rowKey": "global",
  "count": 0
}
