# Threat Model

## Initial threats

- Prompt injection
- Tool injection
- Data exfiltration
- Unsafe tool use
- Insecure output handling
- Memory poisoning
- Policy bypass
- Evidence tampering
- Credential exposure
- Over-broad tool permissions
- Retrieval of unauthorized context

## MVP mitigations

- Tool broker
- Runtime policy checks
- Memory Admission Gate
- Evidence pack immutability target
- Scoped credentials
- Schema validation
- Approval gates
- Trace IDs
