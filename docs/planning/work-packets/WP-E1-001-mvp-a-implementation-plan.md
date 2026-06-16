---
title: WP-E1-001 — MVP-A Implementation Plan
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
work_packet: WP-E1-001
epic: E1
phase: MVP-A Proof Loop
depends_on:
  - WP-E0-001
  - WP-E0-002
  - WP-E0-003A
  - WP-E0-003
  - WP-E0-004
  - WP-E0-005
last_updated: 2026-06-16
---

# WP-E1-001 — MVP-A Implementation Plan

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Work Packet Summary

WP-E1-001 is the first implementation planning packet for the AIC Aegis MVP-A Proof Loop.

It translates the accepted doctrine, system boundaries, and initial ADR baseline into a coding-ready plan for the smallest coherent product slice:

```text
create Run
  -> record events
  -> mock model proposes Tool Action
  -> Proposal is captured
  -> Tool Broker receives Proposal
  -> Policy Check evaluates action
  -> platform Disposition is applied
  -> safe action is mocked / risky action is blocked or approval-gated
  -> Evidence Pack is generated
  -> Run Timeline is visible
```

This packet is implementation-facing, but it still preserves the Aegis doctrine: the model proposes; the platform disposes.

## 2. Objective

Define the implementation plan for MVP-A so a coding agent or human developer can begin work without reopening product scope.

This packet defines:

- implementation sequence;
- recommended local-first service shape;
- package/module boundaries;
- MVP-A command/query set;
- API contract;
- schema catalog;
- persistence model;
- mock model and mock tool behavior;
- policy fixture behavior;
- Evidence Pack shape;
- Timeline shape;
- acceptance tests;
- Codex execution handoff.

## 3. Implementation Posture

### 3.1 Repository-Aware Default

The current repository should be treated as planning-first and contract-first unless code inspection proves otherwise.

Default implementation posture:

- local-first;
- modular monolith;
- headless/API-first;
- mock-safe external behavior;
- file-backed or SQLite-backed persistence for MVP-A;
- deterministic mock model;
- deterministic mock tools;
- small local policy evaluator or OPA/Rego adapter where already present;
- no real customer data;
- no real external side effects.

### 3.2 Stack Selection Rule

Before writing code, inspect the repository and use the existing service/tooling conventions when they are clear.

If the repository does not already contain an active MVP-A service scaffold, the recommended default is:

```text
services/aegis-control-plane/
```

with a local API service and clean internal layers.

The exact language/framework may be finalized by a small implementation ADR if needed. Do not select a stack in a way that violates the architecture doctrine.

## 4. MVP-A Scope

### 4.1 Included

MVP-A includes:

1. Run creation;
2. Actor attribution;
3. Run Event recording;
4. deterministic mock model proposal;
5. Tool Action Proposal capture;
6. Tool Broker orchestration;
7. Policy Check before tool effect;
8. allow/mock/block/approval-required Disposition;
9. simulated Approval Gate;
10. mock Tool Action execution;
11. Evidence Pack manifest generation;
12. Timeline reconstruction;
13. local demo command or script;
14. unit and integration tests for the proof loop.

### 4.2 Excluded

MVP-A excludes:

- governed memory retrieval;
- Memory Candidate proposal;
- Memory Admission Gate;
- Feedback Event capture;
- Eval Result recording;
- Business Outcome Event recording;
- production email sending;
- real CRM mutation;
- real customer data;
- enterprise authentication;
- billing;
- Kubernetes;
- full microservices;
- full event sourcing;
- large connector ecosystem;
- compliance claims.

## 5. Recommended Repository Additions

If no equivalent structure already exists, add:

```text
services/aegis-control-plane/
  src/
    domain/
    application/
    adapters/
    interfaces/
  tests/
    unit/
    integration/
  README.md
```

Documentation additions from this packet:

```text
docs/implementation/mvp-a/README.md
docs/implementation/mvp-a/module-boundaries.md
docs/implementation/mvp-a/api-contract.md
docs/implementation/mvp-a/schema-catalog.md
docs/implementation/mvp-a/persistence-model.md
docs/implementation/mvp-a/demo-scenario.md
docs/implementation/mvp-a/test-strategy.md
docs/planning/codex-handoffs/WP-E1-001-codex-handoff.md
```

## 6. MVP-A Modules

### 6.1 Domain

Domain owns pure Aegis concepts:

- Actor;
- Run;
- RunEvent;
- Proposal;
- ToolAction;
- PolicyCheck;
- Disposition;
- ApprovalRequest;
- ApprovalDecision;
- EvidencePack;
- EvidenceArtifact;
- TimelineEntry.

Domain must not depend on web frameworks, databases, queues, model SDKs, cloud SDKs, or tool SDKs.

### 6.2 Application

Application owns commands, queries, use cases, and ports:

Commands:

- CreateRun;
- RecordRunEvent;
- SubmitToolActionProposal;
- BrokerToolAction;
- EvaluatePolicy;
- RequestApproval;
- RecordApprovalDecision;
- GenerateEvidencePack.

Queries:

- GetRun;
- ListRuns;
- ListRunEvents;
- GetProposal;
- GetPolicyCheck;
- GetToolAction;
- GetApprovalRequest;
- GetEvidencePack;
- GetRunTimeline.

Ports:

- RunRepository;
- RunEventStore;
- ProposalRepository;
- ToolActionRepository;
- PolicyCheckRepository;
- PolicyEngine;
- ToolExecutor;
- ApprovalRepository;
- EvidenceWriter;
- EvidenceRepository;
- TimelineReader;
- ModelProposalProvider.

### 6.3 Adapters

Adapters implement ports:

- local persistence adapter;
- local event store adapter;
- deterministic mock model adapter;
- local policy evaluator adapter;
- mock tool executor adapter;
- file-backed evidence writer;
- timeline reader adapter.

### 6.4 Interfaces

Interfaces expose use cases:

- HTTP API;
- CLI or local demo runner;
- optional worker entry point.

Interfaces must not contain policy logic, tool execution logic, persistence mutation logic, or evidence generation logic.

## 7. API Contract Summary

MVP-A should expose at least these capabilities:

| Method | Path | Purpose |
|---|---|---|
| POST | `/runs` | Create a Run |
| GET | `/runs` | List Runs |
| GET | `/runs/{run_id}` | Get Run |
| POST | `/runs/{run_id}/events` | Record Run Event |
| GET | `/runs/{run_id}/events` | List Run Events |
| POST | `/runs/{run_id}/proposals/tool-action` | Submit Tool Action Proposal |
| POST | `/runs/{run_id}/tool-actions/{tool_action_id}/broker` | Broker Tool Action |
| GET | `/runs/{run_id}/policy-checks/{policy_check_id}` | Get Policy Check |
| POST | `/runs/{run_id}/approvals/{approval_request_id}/decisions` | Record Approval Decision |
| POST | `/runs/{run_id}/evidence-packs` | Generate Evidence Pack |
| GET | `/runs/{run_id}/evidence-packs/{evidence_pack_id}` | Get Evidence Pack |
| GET | `/runs/{run_id}/timeline` | Get Run Timeline |
| POST | `/demo/golden-workflow` | Run deterministic MVP-A demo |

The API may be implemented through HTTP, CLI, or both, but the application commands and queries must remain the source of behavior.

## 8. MVP-A Data Records

Minimum records:

- ActorRef;
- Run;
- RunEvent;
- Proposal;
- ToolAction;
- PolicyCheck;
- ToolBrokerDecision;
- ApprovalRequest;
- ApprovalDecision;
- EvidencePack;
- EvidenceArtifact;
- TimelineEntry or reconstructable timeline source.

## 9. Policy Fixture

MVP-A policy should be deterministic.

Required dispositions:

- `allow`;
- `mock`;
- `block`;
- `approval_required`.

Minimum policy scenarios:

| Scenario | Example Tool Action | Expected Disposition |
|---|---|---|
| Safe follow-up draft | Create a draft follow-up note | `mock` or `allow_mock` |
| Sensitive claim | Send unverified guarantee | `block` |
| Customer-facing send | Send follow-up email | `approval_required` |
| Internal note | Create internal CRM note | `mock` |

MVP-A must not send a real email or mutate a real CRM.

## 10. Evidence Pack Minimum

Evidence Pack manifest must include:

- evidence pack ID;
- Run ID;
- generated timestamp;
- schema version;
- included artifact references;
- Run metadata reference;
- event log reference;
- proposal reference;
- policy check reference;
- tool broker decision reference;
- approval reference if applicable;
- mock tool result reference if applicable;
- timeline export reference.

Artifacts may be JSON files in a local evidence directory.

Recommended local path:

```text
.aic/runtime/evidence/{run_id}/{evidence_pack_id}/
```

## 11. Timeline Minimum

The MVP-A Timeline must reconstruct:

1. Run created;
2. mock model proposal generated;
3. Proposal submitted;
4. Tool Action proposed;
5. Policy Check completed;
6. Disposition applied;
7. Approval requested or skipped;
8. Approval decision recorded when applicable;
9. Tool action mocked, blocked, or deferred;
10. Evidence Pack generated.

The Timeline must be derived from events and related records, not from hidden UI state or model summaries.

## 12. Implementation Sequence

### Step 1 — Repository Inspection

- identify existing service conventions;
- identify existing script entry points;
- identify existing policy/OPA files;
- identify test runner conventions;
- avoid duplicating existing scaffolds.

### Step 2 — Service Skeleton

- create or reuse MVP-A service directory;
- add domain/application/adapters/interfaces folders;
- add README for service;
- wire local config.

### Step 3 — Domain Types

- implement value objects and records for Run, ActorRef, RunEvent, Proposal, ToolAction, PolicyCheck, Disposition, Approval, Evidence, Timeline.

### Step 4 — Application Ports and Use Cases

- define ports;
- implement CreateRun;
- implement RecordRunEvent;
- implement SubmitToolActionProposal;
- implement BrokerToolAction;
- implement GenerateEvidencePack;
- implement GetRunTimeline.

### Step 5 — Local Adapters

- in-memory or local file persistence;
- deterministic mock model;
- deterministic mock tool executor;
- local policy evaluator;
- file evidence writer;
- timeline reader.

### Step 6 — Interfaces

- expose API routes and/or CLI commands;
- add deterministic `/demo/golden-workflow` or equivalent local command.

### Step 7 — Tests

- unit tests for domain invariants;
- unit tests for policy dispositions;
- use-case tests for proposal before disposition;
- integration test for golden workflow;
- evidence pack generation test;
- timeline reconstruction test;
- architecture check for no direct model-to-tool path.

### Step 8 — Documentation and Handoff

- update README if needed;
- add demo instructions;
- update task/check scripts only if necessary;
- record any new implementation ADRs if stack decisions are made.

## 13. Acceptance Criteria

WP-E1-001 is accepted when the implementation plan:

- keeps MVP-A focused on the Proof Loop;
- preserves MVP-B as deferred learning scope;
- defines implementation sequence;
- defines module boundaries;
- defines API surface;
- defines schema families;
- defines persistence records;
- defines policy fixture behavior;
- defines mock model/tool behavior;
- defines Evidence Pack minimum;
- defines Timeline minimum;
- defines test strategy;
- provides a Codex handoff;
- avoids real customer data and real external effects.

## 14. Done Means

This work packet is done when a coding agent can implement MVP-A without asking whether to build memory, evals, outcomes, real connectors, Kubernetes, marketplace, or enterprise controls.

## 15. Handoff to Next Work

After accepting this plan, the next work should begin implementation in thin packets:

1. WP-E1-002 — Run and Event Backbone Implementation;
2. WP-E1-003 — Proposal and Tool Broker Implementation;
3. WP-E1-004 — Policy and Disposition Implementation;
4. WP-E1-005 — Approval and Evidence Implementation;
5. WP-E1-006 — Timeline and Golden Workflow Demo.
