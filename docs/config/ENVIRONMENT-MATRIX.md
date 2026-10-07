# Phase 5 — Frontend Environment Matrix

| Requirement | Local | Automated test | CI | Deployment | Production |
|---|---|---|---|---|---|
| Azure Storage deployment | No | No | No | Yes | Yes |
| PUBLIC_HOSTNAME | Not required | Not required | Optional validation | Required once edge exists | **TBD/configuration gate** |
| VERIFY_PUBLIC_ENDPOINT | false/not used | false | false | false until edge | false until edge acceptance; then true |
| AZURE_RESOURCE_GROUP_NAME | No | No | Production deployment context only | Required | Required |
| AZURE_STORAGE_ACCOUNT_NAME | No | No | Required for deployment workflow | Required | Required |
| AZURE_FRONTEND_IDENTITY_NAME | No | No | OIDC verification | Required for verification | Required |
| AZURE_FRONTEND_IDENTITY_RESOURCE_GROUP | No | No | OIDC verification | Required for verification | Required |
| OIDC identifiers | No | No | Required for deployment job | Required | Required |
| API URL | same-origin | local/mock as applicable | no live API required for static CI | deployed API/edge verification | same-origin /api/visitors |
| Cosmos credentials | Never | Never | Never | Never | Never |
| Real visitor data | Never | Never | Never | Never | Counter only |

There is one Azure deployment environment: production. Local/test/CI are execution contexts, not separate Azure environments.
