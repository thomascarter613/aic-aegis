---
title: MVP-A Event Catalog
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
work_packet: WP-E1-002
last_updated: 2026-06-16
---

# MVP-A Event Catalog

> **Core law:** The model proposes; the platform disposes.

## 1. Purpose

This document defines the MVP-A event catalog.

Aegis is event-rich, not fully event-sourced in MVP-A. Events exist to support evidence and timeline reconstruction.

## 2. Event Naming Rules

Events use past-tense domain names.

Use:

- `RunCreated`
- `ProposalSubmitted`
- `PolicyCheckCompleted`

Avoid:

- `AgentDidThing`
- `AIAction`
- `LogEntry`
- `ToolCalledDirectly`

## 3. MVP-A Events

| Event Type | Trigger | Required References |
|---|---|---|
| RunCreated | A Run is created. | `run_id`, `actor_id` |
| RunEventRecorded | A generic Run Event is recorded. | `run_id`, `event_id` |
| ProposalSubmitted | A model/mock-model Proposal is captured. | `run_id`, `proposal_id`, `actor_id` |
| ToolActionProposed | A Tool Action Proposal is recognized. | `run_id`, `proposal_id`, `tool_action_id` |
| PolicyCheckCompleted | Policy evaluation completes. | `run_id`, `proposal_id`, `policy_check_id` |
| ToolActionDispositioned | Platform applies disposition. | `run_id`, `proposal_id`, `tool_action_id`, `policy_check_id` |
| ApprovalGateRequested | Approval is requested. | `run_id`, `proposal_id`, `tool_action_id`, `approval_request_id` |
| ApprovalDecisionRecorded | Approval decision is recorded. | `run_id`, `approval_request_id`, `approval_decision_id` |
| ToolActionMockExecuted | Mock tool execution completes. | `run_id`, `tool_action_id` |
| ToolActionBlocked | Tool action is blocked. | `run_id`, `tool_action_id`, `policy_check_id` |
| EvidencePackGenerated | Evidence Pack is generated. | `run_id`, `evidence_pack_id` |
| TimelineGenerated | Timeline is generated or queried. | `run_id` |

## 4. Event Envelope

Each event should use the common Run Event envelope:

- `event_id`
- `event_type`
- `event_version`
- `schema_version`
- `run_id`
- `actor_id`
- `occurred_at`
- `correlation_id`
- `causation_id`
- `payload`

## 5. MVP-B Deferred Events

Do not require these for MVP-A:

- `GovernedMemoryRetrieved`
- `MemoryCandidateProposed`
- `MemoryAdmissionCompleted`
- `FeedbackCaptured`
- `EvalResultRecorded`
- `BusinessOutcomeRecorded`
