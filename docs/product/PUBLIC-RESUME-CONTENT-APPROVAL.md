# Public Resume Content Approval Record

## Purpose

This document records the owner-approval gate for OR-005 and REQ-AZ-001.

OR-005 is resolved at the content-definition level. Production acceptance remains blocked until the owner explicitly approves the final public HTML resume content.

## Authoritative Public Content

The candidate public HTML resume is:

`docs/product/public-resume-content.html`

The candidate is intentionally limited to the currently approved public contact/link surface: GitHub and LinkedIn. Phone and email details remain excluded until explicitly approved.

It is derived from the supplied CV and the approved project editorial decisions.

## Approved Editorial Rules

The public resume must:

- contain only professionally relevant information derived from the supplied CV;
- contain only explicitly approved project information;
- contain only explicitly approved public links and contact information;
- exclude private information not intended for public publication;
- state **4+ years of hands-on software development experience**;
- separately identify **IT Operator — Gijima Holdings | June 2022–Present**;
- avoid implying that the full four-plus-year period represents professional software-engineering employment;
- display **Microsoft Certified: Azure AI Fundamentals (AI-901)**;
- never represent AI-901 as AZ-900.

## Current Content Verification

The current candidate HTML contains the required positioning and certification wording:

- Professional summary: **4+ years of hands-on software development experience**.
- Professional experience: **IT Operator — Gijima Holdings**, **June 2022 – Present**.
- Certification: **Microsoft Certified: Azure AI Fundamentals (AI-901)**.
- GitHub and LinkedIn links are explicitly present.
- No phone number or email address is published in the candidate HTML because those contact details are not explicitly approved by the current content decision.
- The document contains no AZ-900 claim.
- Project content is presented as technical-project experience rather than professional employment.

## Owner Approval Gate

**Status: PENDING EXPLICIT OWNER APPROVAL**

The owner must review the complete rendered/public HTML content and explicitly approve it before REQ-AZ-001 and the corresponding production acceptance gate can pass.

### Approval Statement

When the content has been reviewed and is approved for public publication, record:

- **Decision:** Approved
- **Approved artifact:** `docs/product/public-resume-content.html`
- **Owner:** Project owner
- **Approval date:** YYYY-MM-DD
- **Approval note:** The owner explicitly approves the complete public HTML resume content for publication.

Until that statement is recorded, the content remains a candidate/draft for acceptance purposes.

## Traceability

| Item | Status |
|---|---|
| OR-005 content-definition decision | Resolved |
| Public HTML candidate exists | Complete |
| Editorial positioning implemented | Complete |
| AI-901 wording implemented | Complete |
| Final owner review | Pending |
| Explicit owner approval | Pending |
| REQ-AZ-001 final acceptance | Blocked pending owner approval |

