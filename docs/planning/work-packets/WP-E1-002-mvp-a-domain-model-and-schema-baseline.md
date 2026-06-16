---
title: WP-E1-002 — MVP-A Domain Model and Schema Baseline
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
work_packet: WP-E1-002
phase: E1
depends_on:
  - WP-E0-001
  - WP-E0-002
  - WP-E0-003A
  - WP-E0-003
  - WP-E0-004
  - WP-E0-005
  - WP-E1-001
next_work_packet: WP-E1-003
last_updated: 2026-06-16
---

# WP-E1-002 — MVP-A Domain Model and Schema Baseline

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Work Packet Summary

WP-E1-002 defines the initial MVP-A domain model and schema baseline for AIC Aegis.

This packet translates the MVP-A implementation plan into concrete domain objects, invariants, event names, command/query names, and versioned JSON schema contracts.

The objective is to give implementation agents a stable target before code generation begins.

## 2. Objective

Define the minimum MVP-A domain and schema baseline required to implement the Proof Loop:

1. create Run;
2. identify Actor;
3. record Run Events;
4. capture Tool Action Proposal;
5. evaluate Policy Check;
6. apply Disposition;
7. broker mock-safe Tool Action;
8. route high-risk proposals to Approval Gate;
9. generate Evidence Pack;
10. reconstruct Timeline.

## 3. Scope

### 3.1 In Scope

This packet defines:

- MVP-A aggregate/entity/value-object model;
- MVP-A domain invariants;
- MVP-A enum values;
- MVP-A command and query catalog;
- MVP-A event catalog;
- MVP-A JSON schema files;
- schema naming and versioning rules;
- implementation acceptance criteria.

### 3.2 Out of Scope

This packet does not implement:

- application code;
- API routes;
- database migrations;
- queue/worker runtime;
- production tool connectors;
- real email sending;
- real CRM updates;
- governed memory;
- evals;
- feedback;
- business outcome records;
- UI.

## 4. MVP-A Domain Objects

MVP-A includes these domain objects:

| Object | Type | Purpose |
|---|---|---|
| Actor | Entity/reference | Identifies who or what initiated, proposed, approved, or executed work. |
| Run | Aggregate root | Bounded unit of governed AI work. |
| Run Event | Entity/record | Ordered record of what happened during a Run. |
| Proposal | Entity | Captured model/mock-model suggestion before disposition. |
| Tool Action | Entity | Proposed or mock-executed external-effect-like action. |
| Policy Check | Entity | Explicit evaluation against controls and risk. |
| Disposition | Value object/enum | Platform decision: allow, mock, block, approval_required, etc. |
| Approval Request | Entity | Gate for high-risk or ambiguous proposed work. |
| Approval Decision | Entity | Human/system decision on an approval request. |
| Evidence Pack | Entity/artifact manifest | Evidence bundle for a Run. |
| Evidence Artifact | Value object/entity | Individual evidence item referenced by the pack. |
| Timeline Item | Read model item | Ordered explanation of a Run. |

## 5. MVP-A Required Invariants

The implementation must preserve these invariants:

1. A Run must exist before any Run Event, Proposal, Policy Check, Tool Action, Approval Request, Evidence Pack, or Timeline can be associated with it.
2. A Proposal must exist before a Tool Action can be dispositioned.
3. A Tool Action Proposal must pass through the Tool Broker before mock execution.
4. A Policy Check must exist before a Tool Action can be allowed, mocked, blocked, or approval-gated.
5. A high-risk Tool Action must not be executed unless approved.
6. MVP-A tool execution must be mock-safe only.
7. Evidence Pack generation must include or reference Run, Proposal, Policy Check, Disposition, Tool Action, Approval, and Timeline records where applicable.
8. Timeline must be reconstructable from Run Events and related records.
9. MVP-A must not require Memory, Feedback, Eval, or Business Outcome records.
10. Domain objects must not depend on infrastructure frameworks or adapters.

## 6. Schema Baseline

Schema files are emitted under:

```text
contracts/schemas/mvp-a/
```

All MVP-A schemas use:

- JSON Schema draft 2020-12;
- stable `$id` values under `https://aic-aegis.local/schemas/mvp-a/`;
- `schema_version`;
- explicit required fields;
- Aegis domain vocabulary.

## 7. Deliverables

This work packet emits:

- `docs/planning/work-packets/WP-E1-002-mvp-a-domain-model-and-schema-baseline.md`
- `docs/implementation/mvp-a/domain-model.md`
- `docs/implementation/mvp-a/domain-invariants.md`
- `docs/implementation/mvp-a/event-catalog.md`
- `docs/implementation/mvp-a/command-query-catalog.md`
- `contracts/schemas/mvp-a/README.md`
- `contracts/schemas/mvp-a/actor.schema.json`
- `contracts/schemas/mvp-a/run.schema.json`
- `contracts/schemas/mvp-a/run-event.schema.json`
- `contracts/schemas/mvp-a/proposal.schema.json`
- `contracts/schemas/mvp-a/tool-action.schema.json`
- `contracts/schemas/mvp-a/policy-check.schema.json`
- `contracts/schemas/mvp-a/approval.schema.json`
- `contracts/schemas/mvp-a/evidence-pack.schema.json`
- `contracts/schemas/mvp-a/timeline.schema.json`
- `contracts/schemas/mvp-a/enums.schema.json`
- `docs/planning/codex-handoffs/WP-E1-002-codex-handoff.md`

## 8. Acceptance Criteria

WP-E1-002 is accepted when:

- MVP-A domain objects are named and scoped;
- MVP-A invariants are explicit;
- command/query names are defined;
- event names are defined;
- schemas exist for all MVP-A records;
- schemas preserve Proposal before Disposition;
- schemas preserve Policy Check before effect;
- schemas support Evidence Pack and Timeline reconstruction;
- schemas do not introduce MVP-B memory/eval/feedback/outcome dependencies;
- the next implementation packet can begin code scaffolding.

## 9. Done Means

WP-E1-002 is done when a coding agent can use these files to generate the MVP-A domain/application skeleton without reopening product scope or inventing domain language.

## 10. Handoff to WP-E1-003

Recommended next packet:

**WP-E1-003 — MVP-A Code Skeleton and Local Proof Loop**

Likely scope:

- create package/module layout;
- implement domain types;
- implement application commands and queries;
- implement in-memory repositories;
- implement mock model adapter;
- implement mock tool executor;
- implement local policy evaluator;
- implement evidence writer;
- implement timeline query;
- wire a local demo runner;
- add tests for the Proof Loop invariants.
