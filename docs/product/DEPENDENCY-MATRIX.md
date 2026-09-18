# Requirement Dependency Matrix

## 1. Purpose

This document defines the sequencing relationships between requirements and prevents implementation from proceeding against unresolved prerequisites.

---

# 2. Requirement Dependency Matrix

| Requirement | Depends On                                                 | Dependency Type  | Blocking? | Sequence |
| ----------- | ---------------------------------------------------------- | ---------------- | --------- | -------: |
| REQ-AZ-001  | REQ-AZ-002..006                                            | Product/content  | Yes       |        1 |
| REQ-AZ-002  | REQ-AZ-001, REQ-AZ-003                                     | Content/UI       | Yes       |        2 |
| REQ-AZ-003  | REQ-AZ-002                                                 | UI               | Yes       |        3 |
| REQ-AZ-004  | REQ-AZ-002, REQ-AZ-003                                     | Hosting          | Yes       |        4 |
| REQ-AZ-005  | REQ-AZ-004, REQ-AZ-006                                     | Delivery         | Yes       |        6 |
| REQ-AZ-006  | REQ-AZ-005                                                 | DNS/delivery     | Yes       |        5 |
| REQ-AZ-007  | REQ-AZ-008..010                                            | Application      | Yes       |       10 |
| REQ-AZ-008  | REQ-AZ-009, REQ-AZ-010                                     | Persistence      | Yes       |        9 |
| REQ-AZ-009  | REQ-AZ-008, REQ-AZ-010                                     | API              | Yes       |        8 |
| REQ-AZ-010  | REQ-AZ-008, REQ-AZ-009, REQ-AZ-011                         | Backend          | Yes       |        7 |
| REQ-AZ-011  | REQ-AZ-010, REQ-AZ-013                                     | CI/test          | Yes       |       11 |
| REQ-AZ-012  | REQ-AZ-004, REQ-AZ-005, REQ-AZ-008, REQ-AZ-010, REQ-AZ-013 | IaC              | Yes       |       12 |
| REQ-AZ-013  | REQ-AZ-011, REQ-AZ-012                                     | Backend CI/CD    | Yes       |       13 |
| REQ-AZ-014  | REQ-AZ-004, REQ-AZ-005                                     | Frontend CI/CD   | Yes       |       14 |
| REQ-AZ-015  | REQ-AZ-001..014                                            | End-to-end       | Yes       |       16 |
| REQ-AZ-016  | REQ-AZ-001                                                 | Content/external | No        |       15 |

---

# 3. Security Dependencies

| Requirement    | Depends On                         | Reason                                                        |
| -------------- | ---------------------------------- | ------------------------------------------------------------- |
| REQ-AZ-SEC-001 | CI/CD configuration                | Credentials must be securely injected rather than committed   |
| REQ-AZ-SEC-002 | REQ-AZ-009                         | API must be the database boundary                             |
| REQ-AZ-SEC-003 | REQ-AZ-012, REQ-AZ-013, REQ-AZ-014 | Deployment permissions depend on actual resource architecture |
| REQ-AZ-SEC-004 | REQ-AZ-005                         | HTTPS delivery depends on final delivery architecture         |

---

# 4. Governance Dependencies

| Requirement     | Dependency                             |
| --------------- | -------------------------------------- |
| REQ-AZ-COST-001 | Numeric cost ceiling decision          |
| REQ-AZ-REG-001  | ARM deployment configuration           |
| REQ-AZ-GIT-001  | Repository/branch naming normalization |
| REQ-AZ-DEV-001  | ARM resource coverage                  |
| REQ-AZ-DEV-002  | Final resume-content review            |

---

# 5. Blocking Decisions

| Decision                     | Blocks                                         |
| ---------------------------- | ---------------------------------------------- |
| Visitor-count semantics      | REQ-AZ-007, REQ-AZ-008, REQ-AZ-009, REQ-AZ-015 |
| Free hostname interpretation | REQ-AZ-006, REQ-AZ-015                         |
| Numeric cost ceiling         | REQ-AZ-005, REQ-AZ-006, REQ-AZ-012, REQ-AZ-015 |
| CDN/HTTPS architecture       | REQ-AZ-005, REQ-AZ-006, REQ-AZ-014, REQ-AZ-015 |
| Public resume approval       | REQ-AZ-001, REQ-AZ-015                         |
| API contract                 | REQ-AZ-009, REQ-AZ-010                         |
| Test framework               | REQ-AZ-011, REQ-AZ-013                         |
| Repository naming            | REQ-AZ-013, REQ-AZ-014                         |
| Blog platform                | REQ-AZ-016                                     |

---

# 6. Recommended Dependency Sequence

### Phase A — Requirements closure

1. Normalize repository names.
2. Define visitor semantics.
3. Define numeric cost ceiling.
4. Resolve free-hostname interpretation.
5. Validate HTTPS/CDN architecture.
6. Approve final public resume content.
7. Define API contract.
8. Select testing framework.
9. Normalize blog-platform decision.

### Phase B — Frontend foundation

10. HTML resume.
11. CSS styling.
12. Azure Storage hosting boundary.
13. Frontend CI/CD.

### Phase C — Backend foundation

14. Python Azure Function.
15. Cosmos DB persistence boundary.
16. API contract implementation.
17. Python tests.
18. ARM infrastructure.
19. Backend CI/CD.

### Phase D — Delivery

20. CDN/HTTPS.
21. DNS hostname.
22. Visitor counter integration.
23. Production end-to-end validation.

### Phase E — Content completion

24. Blog article.
25. Resume blog link.
26. Final production acceptance.

---

# 7. Dependency Rule

A downstream requirement must not be marked complete when an upstream requirement that materially determines its behavior remains unresolved.

An implementation may proceed in parallel only when the unresolved dependency cannot change its interface, acceptance criteria, security boundary, or architecture.
