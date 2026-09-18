# Requirements Traceability Matrix

## 1. Purpose

This document provides bidirectional traceability from product requirements through user stories, acceptance criteria, verification tests, implementation areas, and CI/release evidence.

No requirement is considered fully traceable until it has at least one verification ID.

---

## 2. Traceability Matrix

| Requirement | User Story / Use Case   | Contract / UI            | Acceptance | Verification | Implementation Area                 | CI / Release Evidence                         |
| ----------- | ----------------------- | ------------------------ | ---------- | ------------ | ----------------------------------- | --------------------------------------------- |
| REQ-AZ-001  | US-001 / UC-001         | Resume content/page      | AC-001     | T-AZ-001     | Resume HTML/content                 | Frontend production URL + content review      |
| REQ-AZ-002  | US-001, US-003 / UC-001 | HTML document            | AC-002     | T-AZ-002     | `index.html` / resume markup        | Frontend CI validation                        |
| REQ-AZ-003  | US-002, US-003 / UC-001 | CSS/UI presentation      | AC-003     | T-AZ-003     | CSS assets                          | Frontend CI + browser validation              |
| REQ-AZ-004  | US-001 / UC-001         | Static website delivery  | AC-004     | T-AZ-004     | Azure Storage                       | Frontend deployment workflow + Azure endpoint |
| REQ-AZ-005  | US-004 / UC-001         | HTTPS/CDN delivery       | AC-005     | T-AZ-005     | CDN/delivery configuration          | Deployment configuration + HTTPS probe        |
| REQ-AZ-006  | US-005 / UC-001         | Public hostname/DNS      | AC-006     | T-AZ-006     | DNS + delivery endpoint             | DNS resolution evidence                       |
| REQ-AZ-007  | US-003, US-006 / UC-002 | Counter UI + API call    | AC-007     | T-AZ-007     | JavaScript counter client           | Browser network evidence                      |
| REQ-AZ-008  | US-007 / UC-002         | Persistence behavior     | AC-008     | T-AZ-008     | Cosmos DB Table API + service layer | Backend test + persistence evidence           |
| REQ-AZ-009  | US-008 / UC-002         | HTTP API contract        | AC-009     | T-AZ-009     | Azure Function HTTP endpoint        | API test evidence                             |
| REQ-AZ-010  | US-009 / UC-002         | Function runtime         | AC-010     | T-AZ-010     | Python Azure Function               | Backend CI + deployed function evidence       |
| REQ-AZ-011  | US-010 / UC-003         | Test suite / CI gate     | AC-011     | T-AZ-011     | Python test suite + workflow        | Passing GitHub Actions run                    |
| REQ-AZ-012  | US-011 / UC-003         | ARM resource definitions | AC-012     | T-AZ-012     | ARM templates                       | ARM deployment evidence                       |
| REQ-AZ-013  | US-012 / UC-003         | Backend CI/CD workflow   | AC-013     | T-AZ-013     | Backend repository/workflows        | Successful backend deployment run             |
| REQ-AZ-014  | US-013 / UC-004         | Frontend CI/CD workflow  | AC-014     | T-AZ-014     | Frontend repository/workflow        | Successful frontend deployment run            |
| REQ-AZ-015  | US-014 / UC-001, UC-004 | Production URL           | AC-015     | T-AZ-015     | Full system                         | Production release evidence                   |
| REQ-AZ-016  | US-015 / UC-005         | Blog/article link        | AC-016     | T-AZ-016     | Resume external link                | Public article + production link              |

---

## 3. Security Traceability

| Requirement    | Verification | Evidence                                          |
| -------------- | ------------ | ------------------------------------------------- |
| REQ-AZ-SEC-001 | T-SEC-001    | Repository secret scan + manual repository review |
| REQ-AZ-SEC-002 | T-SEC-002    | Browser network inspection                        |
| REQ-AZ-SEC-003 | T-SEC-003    | Azure/GitHub deployment permission review         |
| REQ-AZ-SEC-004 | T-SEC-004    | HTTPS production probe                            |

---

## 4. Cost / Governance Traceability

| Requirement     | Verification | Evidence                                                   |
| --------------- | ------------ | ---------------------------------------------------------- |
| REQ-AZ-COST-001 | T-COST-001   | Azure cost/configuration evidence against approved ceiling |
| REQ-AZ-REG-001  | T-REG-001    | ARM resource location review                               |
| REQ-AZ-GIT-001  | T-GIT-001    | Repository branch/settings evidence                        |
| REQ-AZ-DEV-001  | T-IAC-001    | ARM template deployment evidence                           |
| REQ-AZ-DEV-002  | T-CERT-001   | Resume/content review                                      |

---

# 5. Verification Catalogue

| Test ID    | Verification Objective                                | Type                      | Requirement(s)  |
| ---------- | ----------------------------------------------------- | ------------------------- | --------------- |
| T-AZ-001   | Verify only approved public resume content is exposed | Acceptance/content        | REQ-AZ-001      |
| T-AZ-002   | Verify resume is browser-renderable HTML              | Structural/browser        | REQ-AZ-002      |
| T-AZ-003   | Verify intentional responsive CSS presentation        | Browser/UI                | REQ-AZ-003      |
| T-AZ-004   | Verify production assets are served by Azure Storage  | Deployment/integration    | REQ-AZ-004      |
| T-AZ-005   | Verify HTTPS/CDN configuration and cost suitability   | Integration/configuration | REQ-AZ-005      |
| T-AZ-006   | Verify hostname resolves to production delivery       | DNS/integration           | REQ-AZ-006      |
| T-AZ-007   | Verify browser uses API and displays counter          | Browser/integration       | REQ-AZ-007      |
| T-AZ-008   | Verify persistent counter state                       | Backend/integration       | REQ-AZ-008      |
| T-AZ-009   | Verify API request/response/error behavior            | API                       | REQ-AZ-009      |
| T-AZ-010   | Verify Python Azure Function behavior and permissions | Backend                   | REQ-AZ-010      |
| T-AZ-011   | Verify tests execute and gate deployment              | CI                        | REQ-AZ-011      |
| T-AZ-012   | Verify ARM reproducibility                            | IaC/integration           | REQ-AZ-012      |
| T-AZ-013   | Verify backend CI/CD sequence                         | CI/CD                     | REQ-AZ-013      |
| T-AZ-014   | Verify frontend CI/CD publication                     | CI/CD                     | REQ-AZ-014      |
| T-AZ-015   | Verify complete production acceptance                 | End-to-end                | REQ-AZ-015      |
| T-AZ-016   | Verify article link and public article                | Content/link              | REQ-AZ-016      |
| T-SEC-001  | Verify no committed credentials/secrets               | Security                  | REQ-AZ-SEC-001  |
| T-SEC-002  | Verify browser cannot directly access Cosmos DB       | Security/network          | REQ-AZ-SEC-002  |
| T-SEC-003  | Verify deployment permissions are least privilege     | Security/configuration    | REQ-AZ-SEC-003  |
| T-SEC-004  | Verify production HTTPS                               | Security/network          | REQ-AZ-SEC-004  |
| T-COST-001 | Verify cost against approved numeric ceiling          | Governance                | REQ-AZ-COST-001 |
| T-REG-001  | Verify Azure resources use East US                    | IaC/configuration         | REQ-AZ-REG-001  |
| T-GIT-001  | Verify branch model and production branch             | Repository governance     | REQ-AZ-GIT-001  |
| T-IAC-001  | Verify production infrastructure is source-defined    | IaC                       | REQ-AZ-DEV-001  |
| T-CERT-001 | Verify AI-901 is represented without claiming AZ-900  | Content                   | REQ-AZ-DEV-002  |

---

# 6. Traceability Completeness Rule

Every canonical requirement must have:

* Requirement ID
* Priority
* Status
* Dependency relationship
* Affected component
* Acceptance criterion
* Verification/test ID
* Implementation area
* Release evidence

A requirement missing any of these fields is considered **traceability incomplete**.
