# Phase 5 — Frontend Configuration Validation Rules

| ID | Rule | Severity |
|---|---|---|
| FE-VAL-001 | Required production variables must exist before deployment. | BLOCKER |
| FE-VAL-002 | PUBLIC_HOSTNAME must be a valid non-placeholder hostname. | BLOCKER |
| FE-VAL-003 | Public verification must use HTTPS. | BLOCKER |
| FE-VAL-004 | Static artifacts must contain no credentials, .env files, keys, certificates, connection strings, SAS tokens, or client secrets. | BLOCKER |
| FE-VAL-005 | Azure deployment must use GitHub OIDC. | BLOCKER |
| FE-VAL-006 | Storage uploads must use Entra authorization, not storage keys. | BLOCKER |
| FE-VAL-007 | Browser code must contain no Azure/Cosmos credentials. | BLOCKER |
| FE-VAL-008 | API path remains exactly /api/visitors; no independent runtime URL variable may be invented. | BLOCKER |
| FE-VAL-009 | VERIFY_PUBLIC_ENDPOINT remains false until edge/DNS acceptance. | BLOCKER |
| FE-VAL-010 | Backend CORS origin must equal the final approved frontend origin. | BLOCKER |

| FE-VAL-011 | OIDC identifiers must be stored as protected production environment variables, not GitHub Secrets; no client secret may be introduced. | BLOCKER |
