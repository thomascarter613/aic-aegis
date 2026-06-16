---
title: WP-E1-003 — MVP-A Code Skeleton and Local Proof Loop
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
work_packet: WP-E1-003
phase: E1
depends_on:
  - WP-E0-001
  - WP-E0-002
  - WP-E0-003A
  - WP-E0-003
  - WP-E0-004
  - WP-E0-005
  - WP-E1-001
  - WP-E1-002
next_work_packet: WP-E1-004
last_updated: 2026-06-16
---

# WP-E1-003 — MVP-A Code Skeleton and Local Proof Loop

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Work Packet Summary

WP-E1-003 creates the first executable MVP-A code skeleton for AIC Aegis.

This work packet implements a local, mock-safe Proof Loop that demonstrates:

1. Run creation;
2. Actor attribution;
3. Run Event recording;
4. mock model Tool Action Proposal;
5. Proposal capture;
6. Tool Broker enforcement;
7. Policy Check before effect;
8. platform Disposition;
9. Approval Gate for high-risk work;
10. mock-safe tool execution;
11. Evidence Pack generation;
12. Timeline reconstruction.

The result is not a production service. It is a local proof-loop skeleton that gives future work packets a working implementation baseline.

## 2. Objective

Create a small, executable MVP-A runtime skeleton under:

```text
services/runtime/aegis_mvp_a/
```

The skeleton must preserve Clean Architecture responsibilities:

- domain objects and invariants;
- application use cases;
- mock/local adapters;
- CLI/demo interface;
- local tests.

## 3. In Scope

This packet includes:

- Python stdlib-only MVP-A runtime package;
- domain dataclasses and enums;
- in-memory repositories;
- local policy evaluator;
- deterministic mock model adapter;
- mock-safe tool executor;
- evidence writer;
- timeline query;
- CLI/demo runner;
- unit tests for MVP-A invariants;
- docs and Codex handoff.

## 4. Out of Scope

This packet does not include:

- real LLM calls;
- real email sending;
- real CRM updates;
- production connectors;
- database migrations;
- external queue;
- web API server;
- UI;
- Kubernetes;
- enterprise auth;
- billing;
- governed memory;
- evals;
- feedback;
- business outcomes.

## 5. Implementation Shape

The code is placed under:

```text
services/runtime/aegis_mvp_a/
  __init__.py
  __main__.py
  application.py
  cli.py
  domain.py
  serialization.py
  README.md

services/runtime/tests/
  test_mvp_a_proof_loop.py

scripts/
  mvp-a-demo.sh
  test-mvp-a.sh
```

## 6. Runtime Behavior

The local demo supports three scenarios:

| Scenario | Expected Disposition | Expected Result |
|---|---|---|
| `safe` | `mock` | Mock tool action executes and evidence is generated. |
| `risky` | `approval_required` | Approval request is created; optional approval can resume mock execution. |
| `blocked` | `block` | Tool action is blocked and evidence is generated. |

## 7. Acceptance Criteria

WP-E1-003 is accepted when:

- the local package imports successfully;
- the safe demo creates a Run, Proposal, Policy Check, mock Tool Action result, Evidence Pack, and Timeline;
- the risky demo creates an Approval Request and does not execute until approved;
- the blocked demo blocks the Tool Action;
- tests prove Proposal-before-disposition;
- tests prove Policy Check before mock execution;
- tests prove Evidence Pack contains key records;
- tests prove Timeline is reconstructable;
- no MVP-B Memory, Feedback, Eval, or Business Outcome implementation is required.

## 8. Done Means

WP-E1-003 is done when a developer or coding agent can run:

```bash
bash scripts/test-mvp-a.sh
bash scripts/mvp-a-demo.sh safe
bash scripts/mvp-a-demo.sh risky --approve
bash scripts/mvp-a-demo.sh blocked
```

and inspect local evidence output under:

```text
.aic/runtime/evidence/
```

## 9. Handoff to WP-E1-004

Recommended next packet:

**WP-E1-004 — MVP-A HTTP API and Contract Validation**

Likely scope:

- expose CreateRun, SubmitProposal, BrokerToolAction, GenerateEvidencePack, and GetTimeline through HTTP or CLI/API boundary;
- add schema validation against `contracts/schemas/mvp-a`;
- add OpenAPI contract for MVP-A endpoints;
- ensure the API calls application use cases instead of bypassing governance.
