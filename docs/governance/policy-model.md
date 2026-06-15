# Policy Model

Policy must be enforced at runtime, not merely documented.

## Decision types

- allow
- deny
- require_approval
- sanitize
- redact
- escalate
- defer

## Required policy checkpoints

1. Before context retrieval
2. Before prompt assembly
3. Before model call
4. Before tool call
5. Before durable memory write
6. Before final output/action release

## Policy record

Every policy decision should record:

- input
- decision
- reason
- policy ID
- policy version
- run ID
- actor
- timestamp
