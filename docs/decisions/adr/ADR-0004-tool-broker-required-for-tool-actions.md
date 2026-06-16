---
title: ADR-0004 — Tool Broker required for tool actions
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
adr: ADR-0004
last_updated: 2026-06-16
---

# ADR-0004 — Tool Broker required for tool actions

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.


## Status

Proposed

## Date

2026-06-16

## Context

Aegis must govern tool actions because tool actions create external or externally meaningful effects.

The highest-risk architecture failure is direct model-to-tool execution. If a model or model adapter can call a tool directly, Aegis becomes an agent framework rather than a control plane.

## Decision

All Tool Actions must pass through the Tool Broker.

For MVP-A, the Tool Broker must receive a Tool Action Proposal, validate schema, request a Policy Check, apply Disposition, route to Approval Gate if required, execute only mock-safe tool behavior when allowed, record the decision, and attach evidence.

## Rationale

The Tool Broker is the central enforcement boundary for the MVP-A Proof Loop. It ensures that model proposals do not become actions without policy, approval, disposition, and evidence.

## Consequences

Positive consequences:

- no direct model-to-tool path;
- policy decisions become enforceable;
- tool execution can be mocked safely;
- approval requirements can block execution;
- evidence can include complete tool decision records.

Negative consequences:

- tool integrations require broker adapters;
- quick direct tool calls are not allowed;
- implementation must route even simple tools through the broker.

## Alternatives Considered

### Alternative 1 — Let model adapter execute tools

Rejected. This is a direct violation of the core law.

### Alternative 2 — Tool broker only for risky tools

Rejected for MVP-A. All tool actions must establish the governed path.

### Alternative 3 — Policy wrapper around tools without broker

Rejected. Policy wrappers alone do not provide proposal capture, approval routing, evidence, and timeline semantics.

## Doctrine Alignment

This decision preserves Law 2, Law 5, CTRL-002 Tool Broker Enforcement, RISK-001 mitigation, Evidence Pack requirements, and Timeline requirements.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Developers bypass broker for convenience | Fitness checks and tests must forbid direct tool execution. |
| Broker becomes too broad | MVP-A supports only mock-safe tool actions. |
| Policy logic leaks into broker adapter | Keep policy behind Policy Engine port. |
| Tool result lacks evidence | Tool Broker records decision and result for Evidence Pack. |

## Related

- `docs/planning/work-packets/WP-E0-004-mvp-system-boundaries.md`
- `docs/architecture/architecture-doctrine.md`
- `docs/architecture/aegis-laws.md`
- `docs/governance/risk-register.md`
