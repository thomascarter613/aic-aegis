---
title: ADR-0003 — Model output as Proposal records
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
adr: ADR-0003
last_updated: 2026-06-16
---

# ADR-0003 — Model output as Proposal records

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.


## Status

Proposed

## Date

2026-06-16

## Context

The core law says the model proposes and the platform disposes. This requires an explicit record of model-originated suggestions before any platform decision or external effect can occur.

If model output is treated as a command, decision, or direct tool invocation, Aegis loses its central governance boundary.

## Decision

Represent important model-originated output as Proposal records.

For MVP-A, the required Proposal type is a Tool Action Proposal.

A Proposal must be recorded before policy evaluation, tool brokerage, approval routing, mock execution, blocking, evidence pack generation, and timeline reconstruction.

## Rationale

A Proposal record creates the handoff point between model behavior and platform governance. It makes model output inspectable, policy-checkable, approval-gatable, evidencable, and replayable.

This decision prevents model output from being silently converted into action.

## Consequences

Positive consequences:

- proposals can be audited;
- policy checks can reference stable proposal IDs;
- tool broker decisions can be traced;
- approval requests can reference proposed action;
- evidence packs can explain what was suggested;
- timeline can distinguish proposal from disposition.

Negative consequences:

- every important model suggestion requires schema and persistence;
- raw model output may need normalization;
- proposal versioning becomes important.

## Alternatives Considered

### Alternative 1 — Treat model output as direct command

Rejected. This violates the core law and allows the model to become operationally authoritative.

### Alternative 2 — Store only raw transcript/log

Rejected. Logs are not enough. Aegis needs typed Proposal records.

### Alternative 3 — Capture proposals only after policy

Rejected. Policy must evaluate a stable proposal record.

## Doctrine Alignment

This decision preserves Law 1, Law 3, Proposal Capture control, Evidence-first doctrine, and Timeline reconstruction.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Proposal schema too broad | Start with Tool Action Proposal only for MVP-A. |
| Raw model output lost | Store normalized proposal and optional raw source reference. |
| Proposal confused with Disposition | Use separate record types and IDs. |
| Proposal capture bypassed | Enforce through Tool Broker use-case tests. |

## Related

- `docs/planning/work-packets/WP-E0-004-mvp-system-boundaries.md`
- `docs/architecture/architecture-doctrine.md`
- `docs/architecture/aegis-laws.md`
- `docs/governance/control-catalog.md`
