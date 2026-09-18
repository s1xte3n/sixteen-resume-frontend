```markdown
# Azure Cloud Resume Challenge — Data Model

## 1. Purpose

Define the persistent data required by the approved visitor-counter functionality.

The model intentionally contains no user accounts, profiles, analytics, contact records, or unrelated application data.

---

# 2. Persistence Technology

| Property | Decision |
|---|---|
| Database | Azure Cosmos DB |
| API | Table API |
| Capacity direction | Serverless |
| Region | East US |
| Access | Azure Function only |
| Browser access | Prohibited |
| Infrastructure | ARM |

---

# 3. Entities

## 3.1 Visitor Counter

The application requires a persistent counter representing the visitor-count state.

Conceptual entity:

| Property | Purpose |
|---|---|
| `PartitionKey` | Cosmos DB Table partition identifier |
| `RowKey` | Unique entity identifier |
| `Count` | Current counter value |

Additional fields must not be introduced unless required by the approved counter semantics.

---

# 4. Entity Lifecycle

## Initialization

If the counter entity does not exist:

1. Azure Function detects missing state.
2. Function initializes the counter according to the approved semantics.
3. Entity is persisted.
4. Result is returned to the browser.

## Normal Operation

1. Function reads the counter.
2. Function applies the approved counting operation.
3. Function persists the new state.
4. Function returns the resulting count.

## Deployment

Frontend or backend deployment must not delete or recreate counter state.

## Deletion

Counter deletion is not part of the approved product behavior.

Any deletion/reset operation requires explicit scope approval.

---

# 5. Relationships

The approved application contains one persistent entity.

```text
Azure Function
      |
      | reads/updates
      v
VisitorCounter

There are no relationships to:

Users
Sessions
Accounts
Profiles
Analytics events
Other application entities
6. Constraints
Counter

Count must:

Represent the approved visitor-count unit.
Be persisted between requests.
Survive frontend/backend deployments.
Be readable by the Azure Function.
Be writable only through the backend application boundary.
Browser

The browser must never receive:

Cosmos DB credentials.
Cosmos DB connection strings.
Backend database access tokens.
Internal database identifiers that are not required by the API contract.
7. Concurrency

Concurrent counter updates are an important data-integrity concern.

The implementation must use a Cosmos DB Table API operation appropriate to the selected concurrency model.

The final mechanism must ensure that concurrent valid counter operations do not silently overwrite one another.

The exact concurrency implementation is an implementation decision and must not change the approved external API behavior.

8. Indexing

The application requires lookup of the single counter entity.

The data model should use the Table API's partition/key model rather than introducing an additional indexing subsystem.

No custom indexing service is required.

9. Access Ownership
Data	Owner	Read	Write
Visitor counter	Backend application	Azure Function	Azure Function
Resume content	Frontend repository	Public	CI/CD
Infrastructure state	Azure deployment	CI/CD/project owner	CI/CD
10. Data Protection

The counter is not intended to contain personal information.

The application must not expand the counter schema into visitor-identifying information without a new approved requirement.

11. Data Flow
Browser
  |
  | HTTPS
  v
Azure Function
  |
  | authenticated backend access
  v
Cosmos DB Table API
  |
  v
VisitorCounter entity
12. Recovery Requirements

Counter state must survive:

Frontend deployment.
Backend deployment.
Normal application restart.
Function cold starts.

A deployment must not reset the counter.

13. Open Data Decisions

The following must be resolved before the data model is implementation-locked:

What exactly constitutes a visitor?
Is counting based on page loads, API operations, sessions, or another approved unit?
What should happen if the counter entity does not yet exist?
What concurrency behavior is required by the selected semantics?

The first item is P1 and blocks final counter acceptance.


---
