# Detailed Test Cases

All tests require the applicable requirement, environment, synthetic data, and build SHA. Record status, evidence, and cleanup result.

## Frontend
- T-001-P: Compare approved public resume with owner-approved content. Expected exact approved content and no private/unapproved material.
- T-001-N: Search rendered HTML/assets for rejected/private markers. Expected absent.
- T-001-SEC: Inspect public assets for secrets/private data. Expected none.
- T-001-R: Re-run content comparison after changes. Expected no unintended material changes.
- T-002-P: Fetch page and inspect HTML/content type. Expected core resume in HTML.
- T-002-V: Load without Office/PDF viewer. Expected readable resume.
- T-002-R: Repeat HTML structural check after markup changes. Expected core sections remain.
- T-003-P: Load normal CSS. Expected intentional styling.
- T-003-B: Test approved mobile/desktop baselines. Expected no blocking clipping/overlap.
- T-003-F: Block CSS. Expected semantic HTML remains readable.
- T-003-R: Repeat responsive smoke after style changes.

## Hosting/DNS
- T-004-P: Verify Azure Storage static website is primary origin. Expected configuration evidence.
- T-004-G: Publish approved change through CI and fetch it. Expected source/production consistency.
- T-004-R: Repeat hosting evidence after deployment changes.
- T-005-P: Resolve hostname and connect HTTPS. Expected valid TLS and approved delivery path.
- T-005-SEC: Probe insecure HTTP behavior. Expected production policy prevents insecure application access.
- T-005-G: Fetch HTML/CSS/JS through public endpoint. Expected approved delivery path.
- T-005-B: Review recurring cost. Expected <=R100/month; R0 preferred.
- T-006-P: Resolve public hostname externally. Expected intended production endpoint.
- T-006-V: Inspect DNS mapping. Expected correct/stable mapping.
- T-006-G: Trace hostname through DNS to delivery. Expected correct chain.
- T-006-F: Validate unavailable/unpropagated DNS evidence. Expected controlled failure, no readiness claim.

## Counter/API
- T-007-P: Open page once and inspect network/UI. Expected exactly one successful GET /api/visitors and displayed committed count.
- T-007-N: Make API unavailable. Expected resume remains readable and approved failure UX.
- T-007-V: Baseline N, refresh once. Expected exactly one additional successful operation and N+1.
- T-007-I: Inspect cookies/storage/network. Expected no identity-based counting.
- T-007-S: Observe one load. Expected no duplicate counter operation.
- T-007-SEC: Inspect built assets/network. Expected no Cosmos endpoint, token, key, or direct request.
- T-007-R: Repeat counter smoke after frontend changes.
- T-008-P: Initialize isolated counter. Expected one logical entity and correct result.
- T-008-S: Baseline N, perform K successes. Expected persisted N+K.
- T-008-D: Record count, deploy normally, verify. Expected state survives.
- T-DATA-001: Run K concurrent successes. Expected N+K with no lost increments.
- T-DATA-002: Fail dependency before commit. Expected 503/504 and unchanged state.
- T-008-F: Force conditional conflict. Expected safe retry or controlled failure, no lost increment.
- T-009-P: GET /api/visitors. Expected 200, exact schema, count integer >=0, and state transition confirmed.
- T-009-N: Unsupported method/query/path/malformed request. Expected canonical 400/405 and no unintended mutation.
- T-009-V: Invalid X-Request-ID/unsupported content type. Expected 400/415 and no mutation.
- T-009-A: Invoke without end-user credentials. Expected public counter is allowed; service auth remains server-side.
- T-009-Z: Attempt reset/admin/arbitrary partition operation. Expected unavailable/blocked.
- T-009-C: Run Postman contract suite. Expected status/schema/header/requestId/error assertions pass.
- T-009-G: Inject dependency unavailable/timeout/unexpected error. Expected 503/504/500 mapping and no false success.
- T-009-SEC: Trigger errors. Expected no stack trace, secret, token, connection string, or unnecessary internal detail.
- T-009-F: Exercise applicable throttling. Expected 429 and no unintended mutation.

## Backend/CI/IaC
- T-010-P: Verify deployed Python Function handles request/persistence.
- T-010-Z: Review Function identity and attempt unrelated access. Expected least privilege.
- T-010-F: Force runtime/dependency failure. Expected canonical safe error.
- T-010-SEC: Inspect code/config/logs. Expected no plaintext credentials.
- T-011-P: Run backend workflow. Expected Python tests execute and are visible.
- T-011-N: Introduce deliberate required-behavior failure in isolated run. Expected deployment skipped.
- T-011-G: Inspect workflow ordering. Expected tests pass before deployment.
- T-011-R: Repeat after pipeline changes. Expected gate remains.
- T-012-P: Validate ARM and required resources. Expected all required infrastructure represented.
- T-012-N: Provision isolated target from ARM. Expected no undocumented manual configuration.
- T-012-G: Apply ARM and compare resulting resources/config. Expected source parity.
- T-012-R: Repeat validation after template changes.
- T-013-P: Run backend change. Expected tests then deployment.
- T-013-N: Force deployment failure. Expected visible failure and no false success.
- T-013-SEC: Scan backend source/workflows/artifacts. Expected no secrets.
- T-013-G: Inspect branch triggers/source. Expected develop integration and main production.
- T-014-P: Run frontend change. Expected Azure Storage publication.
- T-014-N: Force publication failure. Expected workflow failure.
- T-014-SEC: Scan frontend source/build artifacts. Expected no deployment/database secrets.
- T-014-G: Publish changed asset and fetch through delivery layer. Expected current asset after required invalidation.

## Release/cross-cutting
- T-015-E2E: Verify hostname, HTTPS, content, counter, CI, IaC, security, cost. Expected all AC-015 conditions pass.
- T-015-SEC: Review secret scan, network, TLS, permissions. Expected no critical security failure.
- T-015-COST: Capture recurring cost. Expected <=R100/month and unexpected charges investigated.
- T-016-P: Open production article link externally. Expected public and required learning topics.
- T-016-V: Verify article URL/platform against current project docs. Expected evidence recorded and inconsistency not hidden.
- T-016-R: Re-check article after deployment. Expected reachable.
- T-SEC-001: Run secret scanner. Expected no credentials/tokens/keys.
- T-SEC-001-R: Repeat after config/dependency changes. Expected clean.
- T-SEC-002: Inspect source/build/network. Expected no browser-to-Cosmos access.
- T-SEC-003: Review deployment/runtime identities. Expected only required permissions.
- T-SEC-004: Probe production TLS. Expected valid HTTPS and approved insecure-traffic behavior.
- T-COST-001: Review billing/forecast/config evidence. Expected <=R100/month; R0 preferred.
- T-REG-001: Inspect resource locations. Expected East US unless approved change.
- T-GIT-001: Inspect branches/workflows. Expected develop integration; main production.
- T-IAC-001: Provision isolated target from committed ARM only. Expected reproducible infrastructure.
- T-CERT-001: Inspect certification wording. Expected no false AZ-900 claim; AI-901 may be displayed if approved.
- T-REL-001: Run P0 suite on release candidate. Expected all P0 checks pass.
