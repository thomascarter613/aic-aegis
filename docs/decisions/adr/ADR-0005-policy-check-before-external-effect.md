---
title: ADR-0005 — Policy Check before external effect
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
adr: ADR-0005
last_updated: 2026-06-16
---

# ADR-0005 — Policy Check before external effect

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.


## Status

Proposed

## Date

2026-06-16

## Context

Aegis must be policy-enforced. A proposal cannot safely proceed to a tool action, mock action, approval route, or block decision without a recorded policy evaluation.

Even in MVP-A, policy must be explicit and inspectable. It cannot be hidden in controller conditionals or tool adapters.

## Decision

Require a Policy Check before any external effect or mock-safe tool execution.

For MVP-A, Policy Check output must include Policy Check ID, Run ID, Proposal ID, Tool Action ID where applicable, disposition, risk level, matched controls, rationale, timestamp, and schema version.

## Rationale

Policy Check is the bridge between Proposal and Disposition. It allows Aegis to explain why the platform allowed, mocked, blocked, or approval-gated a proposed action.

## Consequences

Positive consequences:

- platform disposition is explainable;
- controls and risks become visible;
- evidence packs can include policy rationale;
- high-risk actions can be reliably approval-gated or blocked.

Negative consequences:

- policy records must be modeled early;
- even mocked actions need policy handling;
- simple demos require policy fixtures.

## Alternatives Considered

### Alternative 1 — Policy as hardcoded controller logic

Rejected. Controller logic is not a durable Policy Check record.

### Alternative 2 — Policy only for high-risk actions

Rejected. MVP-A must prove Policy Check before effect as a universal boundary.

### Alternative 3 — Policy as post-hoc audit annotation

Rejected. Policy must influence disposition before execution.

## Doctrine Alignment

This decision preserves Law 4, CTRL-003, CTRL-004, RISK-002 mitigation, and evidence-first doctrine.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Policy becomes too complex | Use a small local policy evaluator for MVP-A. |
| Policy output too vague | Require disposition, risk, controls, and rationale. |
| Policy bypassed by mock execution | Apply policy before mocked execution too. |
| Policy tied to one engine | Define Policy Engine as application port. |

## Related

- `docs/planning/work-packets/WP-E0-004-mvp-system-boundaries.md`
- `docs/architecture/architecture-doctrine.md`
- `docs/architecture/aegis-laws.md`
- `docs/governance/control-catalog.md`
