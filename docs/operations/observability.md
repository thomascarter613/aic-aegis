# Observability

## Required telemetry

- run started/completed/failed
- model call latency/cost/tokens
- tool call status
- policy decision status
- memory retrieval/write status
- eval scores
- evidence pack generation
- approval latency

## Trace identity

Every event should propagate:

- tenant_id
- user_id
- agent_id
- run_id
- trace_id
- evidence_pack_id
