---
title: ADR-0009 — Mock model and mock tools for MVP-A
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
adr: ADR-0009
last_updated: 2026-06-16
---

# ADR-0009 — Mock model and mock tools for MVP-A

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.


## Status

Proposed

## Date

2026-06-16

## Context

MVP-A must demonstrate governed AI work without real customer data, production email sending, real CRM mutation, or external side effects.

Using live models and real tools too early would increase safety, privacy, cost, and integration risks before the control plane is proven.

## Decision

Use a deterministic mock model and mock tool adapters for MVP-A.

The mock model may generate fixed or scenario-driven Tool Action Proposals.

The mock tools may simulate actions such as sending a follow-up email, creating a CRM note, creating a task, or updating follow-up status.

No real external side effects are allowed in MVP-A.

## Rationale

The purpose of MVP-A is to prove platform disposition, not model quality or connector breadth.

Mocking keeps the demo safe while still exercising Proposal capture, Policy Check, Tool Broker, Approval Gate, Evidence Pack, and Timeline.

## Consequences

Positive consequences:

- local demos are safe and repeatable;
- no external credentials are required;
- policy and evidence behavior can be tested deterministically;
- real customer data is avoided;
- cost and integration complexity stay low.

Negative consequences:

- MVP-A does not prove real connector reliability;
- model variability is not tested;
- production readiness is not claimed.

## Alternatives Considered

### Alternative 1 — Use live LLM from the start

Deferred. A live model can be added later, but MVP-A does not require it.

### Alternative 2 — Use real email/CRM tools

Rejected for MVP-A. Real external effects are unnecessary and increase risk.

### Alternative 3 — No model boundary at all

Rejected. MVP-A must still demonstrate model-like Proposal generation.

## Doctrine Alignment

This decision preserves local-first doctrine, Mock-Safe Execution control, no external effect without governed boundary, MVP thin-slice discipline, and evidence-first demonstration.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Mock hides real integration problems | Document real integrations as deferred. |
| Mock model too unrealistic | Use scenario-driven proposals with risk variation. |
| Mock tool bypasses broker | Mock tools still execute only through Tool Broker. |
| Users think MVP is production-ready | Clearly label mock-safe behavior. |

## Related

- `docs/planning/work-packets/WP-E0-004-mvp-system-boundaries.md`
- `docs/architecture/architecture-doctrine.md`
- `docs/architecture/aegis-laws.md`
- `docs/governance/control-catalog.md`
