# Security Policy

This project handles AI workflow governance, tool execution, memory, policy decisions, and evidence records. Treat all production data as sensitive.

## Security principles

- Models do not receive raw credentials.
- Models do not execute tools directly.
- Durable memory writes are gated.
- Tool calls are brokered and audited.
- Policy checks happen at runtime.
- Evidence packs may contain sensitive metadata and must be protected.
- Human approval is required for high-risk actions.

## Out-of-scope for MVP

- PCI workloads
- HIPAA workloads
- fully autonomous destructive infrastructure changes
- production legal/medical/financial advice automation
