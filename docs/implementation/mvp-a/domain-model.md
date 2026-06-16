---
title: MVP-A Domain Model
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
work_packet: WP-E1-002
last_updated: 2026-06-16
---

# MVP-A Domain Model

> **Core law:** The model proposes; the platform disposes.

## 1. Purpose

This document defines the initial MVP-A domain model for the AIC Aegis Proof Loop.

The model is intentionally narrow. It supports governed tool-action proposals, policy disposition, approval gating, mock-safe execution, evidence generation, and timeline reconstruction.

## 2. Domain Shape

MVP-A centers on the `Run` aggregate.

A Run is the bounded unit of governed AI work. All MVP-A records attach to a Run directly or indirectly.

```text
Run
├── Actor reference
├── Run Events
├── Proposals
│   └── Tool Action
│       ├── Policy Check
│       ├── Disposition
│       ├── Approval Request / Decision
│       └── Mock Tool Result
├── Evidence Pack
└── Timeline
```

## 3. Actor

An `Actor` identifies a human, model adapter, service, worker, or system component involved in governed work.

Minimum fields:

- `actor_id`
- `actor_type`
- `display_name`
- `external_ref`
- `metadata`

Allowed actor types:

- `human`
- `mock_model`
- `service`
- `worker`
- `system`

## 4. Run

A `Run` is the aggregate root for MVP-A.

Minimum fields:

- `run_id`
- `workflow`
- `purpose`
- `status`
- `initiating_actor_id`
- `created_at`
- `updated_at`
- `metadata`

Allowed statuses:

- `created`
- `running`
- `awaiting_approval`
- `completed`
- `blocked`
- `failed`
- `cancelled`

## 5. Run Event

A `Run Event` records something that happened during a Run.

Minimum fields:

- `event_id`
- `run_id`
- `event_type`
- `event_version`
- `occurred_at`
- `actor_id`
- `correlation_id`
- `causation_id`
- `payload`
- `schema_version`

## 6. Proposal

A `Proposal` is a model-originated or model-like suggestion. A Proposal is not permission.

MVP-A supports:

- `tool_action` proposal type.

Minimum fields:

- `proposal_id`
- `run_id`
- `proposed_by_actor_id`
- `proposal_type`
- `status`
- `created_at`
- `summary`
- `payload`
- `source`

Allowed proposal statuses:

- `submitted`
- `under_policy_review`
- `dispositioned`
- `approval_required`
- `blocked`
- `mock_executed`
- `cancelled`

## 7. Tool Action

A `Tool Action` represents a proposed or mock-executed external-effect-like action.

MVP-A allows mock-safe tool actions only.

Minimum fields:

- `tool_action_id`
- `run_id`
- `proposal_id`
- `tool_name`
- `operation`
- `target`
- `arguments`
- `status`
- `created_at`
- `updated_at`

Allowed tool action statuses:

- `proposed`
- `policy_checked`
- `approval_required`
- `approved`
- `rejected`
- `mock_executed`
- `blocked`
- `failed`

## 8. Policy Check

A `Policy Check` is an explicit evaluation against controls and risk.

Minimum fields:

- `policy_check_id`
- `run_id`
- `proposal_id`
- `tool_action_id`
- `checked_at`
- `policy_engine`
- `input_ref`
- `risk_level`
- `matched_controls`
- `disposition`
- `rationale`

Allowed risk levels:

- `low`
- `medium`
- `high`
- `critical`

Allowed dispositions:

- `allow`
- `mock`
- `block`
- `approval_required`
- `defer`

## 9. Approval Request and Decision

An `Approval Request` records that proposed work requires approval.

Minimum request fields:

- `approval_request_id`
- `run_id`
- `proposal_id`
- `tool_action_id`
- `requested_by_actor_id`
- `status`
- `rationale`
- `created_at`
- `expires_at`

Minimum decision fields:

- `approval_decision_id`
- `approval_request_id`
- `decided_by_actor_id`
- `decision`
- `rationale`
- `decided_at`

Allowed approval statuses:

- `requested`
- `approved`
- `rejected`
- `expired`
- `cancelled`

Allowed approval decisions:

- `approved`
- `rejected`

## 10. Evidence Pack

An `Evidence Pack` is the generated artifact manifest for a Run.

Minimum fields:

- `evidence_pack_id`
- `run_id`
- `generated_at`
- `generated_by_actor_id`
- `manifest_version`
- `artifacts`
- `summary`

## 11. Timeline

A `Timeline` is a query/read-model response that reconstructs the Run.

Minimum fields:

- `run_id`
- `generated_at`
- `items`

Timeline items must include:

- `timeline_item_id`
- `occurred_at`
- `event_type`
- `title`
- `description`
- `record_refs`

## 12. MVP-B Exclusion

The following domain objects are not part of MVP-A implementation:

- Memory
- Memory Candidate
- Memory Admission
- Feedback Event
- Eval Result
- Business Outcome Event

They may be named in docs as deferred objects but must not be required by MVP-A code.
