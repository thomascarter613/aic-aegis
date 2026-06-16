---
title: ADR-0010 — Headless/API-first MVP
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
adr: ADR-0010
last_updated: 2026-06-16
---

# ADR-0010 — Headless/API-first MVP

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.


## Status

Proposed

## Date

2026-06-16

## Context

Aegis is a headless, API-first control plane. A UI may exist later, but the core platform must be governed through APIs, commands, queries, schemas, events, and evidence artifacts.

If UI behavior becomes authoritative, Aegis risks becoming a dashboard rather than a control plane.

## Decision

Build MVP-A as headless and API-first.

MVP-A capabilities must be exposed through application commands/queries and at least one machine-usable interface, such as HTTP API or CLI.

A UI is optional and must not bypass governed APIs or application use cases.

## Rationale

The headless/API-first posture reinforces that Aegis is the control plane, not a presentation layer.

This keeps core governance usable by scripts, tests, future workers, future UI, and future integrations.

## Consequences

Positive consequences:

- use cases are testable without UI;
- future UI can consume the same governed APIs;
- evidence artifacts remain primary;
- CLI/demo flows can prove MVP-A locally;
- API contracts can drive implementation.

Negative consequences:

- early user experience may be less polished;
- UI demonstration is deferred or minimal;
- more attention is needed on API/schema quality.

## Alternatives Considered

### Alternative 1 — UI-first MVP

Rejected. A UI-first MVP risks hiding control-plane semantics behind screens and local state.

### Alternative 2 — CLI-only with no API design

Partially rejected. A CLI is acceptable, but it should map to application commands/queries and not become the only architecture boundary.

### Alternative 3 — API plus UI from day one

Deferred. A thin UI may be useful later, but it is not necessary for MVP-A.

## Doctrine Alignment

This decision preserves headless doctrine, API-first doctrine, Clean Architecture interface boundary, evidence-first behavior, and the rule that UI must not bypass governing boundaries.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| API becomes too broad | Implement only MVP-A proof-loop endpoints. |
| CLI diverges from API | Both must call the same application use cases. |
| UI bypasses controls later | UI must consume governed API/application layer. |
| Evidence hidden from users | Provide Evidence Pack and Timeline retrieval. |

## Related

- `docs/planning/work-packets/WP-E0-004-mvp-system-boundaries.md`
- `docs/architecture/architecture-doctrine.md`
- `docs/architecture/aegis-laws.md`
- `docs/product/product-charter.md`
