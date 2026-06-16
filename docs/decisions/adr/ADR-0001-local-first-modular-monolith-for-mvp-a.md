---
title: ADR-0001 — Local-first modular monolith for MVP-A
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
adr: ADR-0001
last_updated: 2026-06-16
---

# ADR-0001 — Local-first modular monolith for MVP-A

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.


## Status

Proposed

## Date

2026-06-16

## Context

Aegis needs to prove the MVP-A Proof Loop before taking on platform breadth. The MVP must run locally without managed cloud infrastructure while preserving future cloud-native capability.

The major risk is premature distributed architecture: microservices, Kubernetes, queues, and managed services could consume effort before the proof loop works.

## Decision

Build MVP-A as a local-first modular monolith or single local process with explicit module boundaries.

The implementation may expose an HTTP API, CLI, and worker-like entry point, but deployment must not require Kubernetes, cloud services, distributed queues, or multiple independently deployed services.

The code must preserve conceptual service boundaries even if executed in one process.

## Rationale

A modular monolith is the smallest architecture capable of proving the trust loop while preserving Clean Architecture boundaries.

It allows Aegis to implement Run, Proposal, Policy, Tool Broker, Approval, Evidence, and Timeline behavior without premature infrastructure. Future cloud-native deployment remains possible because the application layer will depend on ports rather than infrastructure details.

## Consequences

Positive consequences:

- local setup remains simple;
- MVP-A can be implemented faster;
- domain and application boundaries remain testable;
- future adapters can replace local infrastructure;
- evidence and timeline behavior can be proven before scaling.

Negative consequences:

- deployment topology will not prove distributed operations yet;
- worker behavior may initially be synchronous;
- later extraction may require deliberate refactoring.

## Alternatives Considered

### Alternative 1 — Microservices from the start

Rejected for MVP-A. Microservices would add distributed systems complexity before Aegis proves proposal-to-evidence governance.

### Alternative 2 — Kubernetes-first architecture

Rejected for MVP-A. Kubernetes may be useful later but violates local-first MVP simplicity.

### Alternative 3 — Script-only prototype

Rejected as the main architecture. A script could demonstrate behavior, but it risks losing the boundaries needed for a reliability control plane.

## Doctrine Alignment

This decision preserves local-first doctrine, cloud-native-capable doctrine through ports/adapters, Clean Architecture boundaries, MVP thin-slice discipline, and the rule that local simplicity must not remove governance boundaries.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Modular monolith becomes unstructured | Enforce package boundaries and application ports. |
| Future service extraction becomes difficult | Keep interfaces and adapters isolated. |
| Worker boundary disappears | Model worker behavior as application use cases even if synchronous. |
| Local-first becomes local-only | Use environment-based configuration and replaceable adapters. |

## Related

- `docs/planning/work-packets/WP-E0-004-mvp-system-boundaries.md`
- `docs/architecture/architecture-doctrine.md`
- `docs/architecture/aegis-laws.md`
- `docs/product/mvp-strategy.md`
