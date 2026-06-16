---
title: MVP-A Test Strategy
project: AIC Aegis
status: Proposed
last_updated: 2026-06-16
---

# MVP-A Test Strategy

> **Core law:** The model proposes; the platform disposes.

## 1. Test Principle

Tests must prove governance, not just code coverage.

## 2. Required Test Groups

### 2.1 Domain Tests

- Run requires actor attribution.
- Proposal is distinct from Disposition.
- Tool Action cannot be marked executed without broker decision.
- Approval-required action cannot execute before approval.

### 2.2 Use-Case Tests

- CreateRun records RunCreated event.
- SubmitToolActionProposal records ProposalSubmitted and ToolActionProposed.
- BrokerToolAction always invokes Policy Check.
- BrokerToolAction blocks blocked actions.
- BrokerToolAction creates Approval Request for approval-required actions.
- GenerateEvidencePack includes required artifacts.
- GetRunTimeline reconstructs ordered events.

### 2.3 Policy Tests

- safe internal note returns mock/allow-mock.
- customer-facing send returns approval_required.
- unsafe guarantee returns block.
- policy result includes risk level, controls, and rationale.

### 2.4 Adapter Tests

- mock model produces deterministic Proposal.
- mock tool executor cannot be called directly by interface layer.
- evidence writer creates manifest and artifacts.
- local persistence preserves IDs and timestamps.

### 2.5 Integration Tests

- golden workflow safe variant completes with mock execution and evidence.
- golden workflow approval variant pauses before approval and resumes after approval.
- golden workflow blocked variant records block and still generates evidence.

### 2.6 Fitness Tests

Required MVP-A fitness checks:

- core law visible in docs/API metadata;
- no direct model-to-tool execution;
- Proposal before Disposition;
- Policy Check before mock execution;
- Evidence Pack generated;
- Timeline reconstructable;
- domain independent from framework/database/model SDK;
- MVP-A does not require MVP-B memory/eval/outcome.

## 3. Acceptance Test

A single end-to-end test should execute:

```text
POST /demo/golden-workflow
GET /runs/{run_id}/timeline
GET /runs/{run_id}/evidence-packs/{evidence_pack_id}
```

and assert:

- Run exists;
- Proposal exists;
- Policy Check exists;
- Tool Broker Decision exists;
- Disposition exists;
- Evidence Pack manifest exists;
- Timeline contains ordered proof-loop entries.
