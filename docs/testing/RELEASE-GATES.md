# Release Gates

## Merge: feature -> develop
- P0/P1 applicable tests pass.
- Static checks and secret scan pass.
- Changed API contract tests pass.
- No P0/P1 defect remains open.
- Traceability is updated for behavior changes.
- No credential is committed.

## Integration: develop
- Full P0/P1 regression passes.
- Python tests pass for backend changes.
- ARM validation passes for IaC changes.
- Postman/contract suite passes for API changes.
- Browser smoke passes for frontend changes.
- Evidence is captured.

## Production deployment: main
1. Merge gates pass.
2. CI proves tests precede deployment.
3. Production source is main.
4. Secure deployment authentication is configured.
5. IaC is source controlled.
6. Secret scanning passes.
7. No P1 ambiguity is silently overridden.
8. Final public resume content approval exists.
9. HTTPS/CDN/hostname/CORS decisions are validated.

## Production acceptance
AC-001..016 applicable checks pass, including content approval, HTML/CSS, Azure Storage, HTTPS/CDN, FreeDNS hostname interpretation, counter/API/persistence/concurrency, Python Function, CI test-before-deploy, ARM reproducibility, CI/CD, and article link.

Also required: recurring Azure/cloud cost <=R100/month; R0 preferred; unexpected charges investigated; no secrets; no browser-to-Cosmos access; least privilege; production represented by main.

## Automatic blockers
Failed P0; failed required P1; secret detected; direct browser-to-Cosmos access; lost counter increments; incorrect schema/business state despite 2xx; deployment after failed required tests; invalid HTTPS; cost >R100/month; unapproved content; non-reproducible production infrastructure; production not from main.

## Evidence
Record repository, branch, commit SHA, environment, test IDs, result, timestamp, CI/deployment run, and sanitized evidence. Never attach secrets.

## Override
Only an explicitly recorded requirement-level deviation may change a release condition. A failed test cannot be relabeled as passed.
