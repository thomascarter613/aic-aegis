---
title: MVP-A Domain Invariants
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
work_packet: WP-E1-002
last_updated: 2026-06-16
---

# MVP-A Domain Invariants

> **Core law:** The model proposes; the platform disposes.

## 1. Purpose

This document defines invariant rules that MVP-A implementation must enforce or test.

## 2. Required Invariants

| ID | Invariant | Enforcement Point |
|---|---|---|
| INV-A-001 | A Run must exist before related records are created. | Application use cases / repositories |
| INV-A-002 | Actor attribution is required for Run creation, proposal submission, approval decisions, and evidence generation. | Commands / schema validation |
| INV-A-003 | A Proposal must be recorded before Tool Broker disposition. | `SubmitProposal`, `BrokerToolAction` |
| INV-A-004 | A Tool Action must reference a Proposal. | Tool Action schema / application use case |
| INV-A-005 | A Policy Check must exist before allow/mock/block/approval disposition. | Tool Broker use case |
| INV-A-006 | High-risk proposals cannot execute without approval. | Policy + Approval Gate |
| INV-A-007 | MVP-A execution must be mock-safe only. | Tool Executor adapter |
| INV-A-008 | Evidence Pack generation requires Run, Proposal, Policy Check, Disposition, and Timeline source data. | Evidence use case |
| INV-A-009 | Timeline must be reconstructable from events and related records. | Timeline query |
| INV-A-010 | MVP-A must not require memory/eval/feedback/outcome records. | Package boundary / tests |

## 3. Failure Behavior

Invariant failure should result in one of:

- validation error;
- blocked disposition;
- failed command result;
- test failure;
- rejected implementation change.

Invariant failure must not be silently logged and ignored.

## 4. Test Expectations

Each invariant should eventually have at least one test.

Minimum early tests:

1. cannot broker tool action without Proposal;
2. cannot mock execute without Policy Check;
3. high-risk action results in approval_required or block;
4. evidence pack includes proposal and policy result references;
5. timeline includes proposal, policy, disposition, and evidence events.
