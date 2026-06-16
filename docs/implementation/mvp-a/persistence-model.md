---
title: MVP-A Persistence Model
project: AIC Aegis
status: Proposed
last_updated: 2026-06-16
---

# MVP-A Persistence Model

> **Core law:** The model proposes; the platform disposes.

## 1. Persistence Principle

MVP-A persistence may be local and simple, but it must support evidence and timeline reconstruction.

Persistence is not incidental logging.

## 2. Minimum Tables or Collections

| Record | Key Fields |
|---|---|
| runs | run_id, workflow, purpose, actor_id, status, created_at, updated_at |
| run_events | event_id, run_id, sequence, event_type, payload, schema_version, created_at |
| proposals | proposal_id, run_id, actor_id, proposal_type, raw_source_ref, payload, created_at |
| tool_actions | tool_action_id, run_id, proposal_id, tool_name, operation, status, payload, created_at |
| policy_checks | policy_check_id, run_id, proposal_id, tool_action_id, disposition, risk_level, controls, rationale, created_at |
| tool_broker_decisions | decision_id, run_id, tool_action_id, policy_check_id, disposition, status, created_at |
| approval_requests | approval_request_id, run_id, proposal_id, tool_action_id, status, requested_by, rationale, created_at |
| approval_decisions | approval_decision_id, approval_request_id, decision, approver_actor_id, rationale, created_at |
| evidence_packs | evidence_pack_id, run_id, manifest_path, schema_version, created_at |
| evidence_artifacts | artifact_id, evidence_pack_id, artifact_type, path, hash, schema_version, created_at |

## 3. Relationship Rules

- A Run has many Run Events.
- A Run has many Proposals.
- A Proposal may produce one Tool Action in MVP-A.
- A Tool Action must have a Policy Check before mock execution.
- A Tool Broker Decision references the Tool Action and Policy Check.
- An Approval Request references the Tool Action when disposition is `approval_required`.
- An Evidence Pack references Run records, events, proposal, policy, broker decision, approvals, and timeline.

## 4. Local Storage Options

Acceptable MVP-A options:

- in-memory persistence for unit tests;
- file-backed JSON persistence for demos;
- SQLite for local integration tests;
- local Postgres only if already available in repo setup.

Do not require managed cloud infrastructure for MVP-A.

## 5. Evidence Path

Recommended evidence path:

```text
.aic/runtime/evidence/{run_id}/{evidence_pack_id}/
  manifest.json
  run.json
  events.json
  proposal.json
  tool-action.json
  policy-check.json
  tool-broker-decision.json
  approval.json
  timeline.json
```
