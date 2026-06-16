---
title: ADR-0006 — Evidence Pack as MVP-A artifact
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
adr: ADR-0006
last_updated: 2026-06-16
---

# ADR-0006 — Evidence Pack as MVP-A artifact

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.


## Status

Proposed

## Date

2026-06-16

## Context

Aegis claims that AI work should be provable. That claim cannot wait until later platform maturity.

MVP-A must generate an Evidence Pack that lets a reviewer inspect what happened during a Run.

## Decision

Generate an Evidence Pack as a required MVP-A product artifact.

For MVP-A, the Evidence Pack must include or reference Run metadata, Actor attribution, Run Events, Proposal, Tool Action, Policy Check, Disposition, Approval records if applicable, mock Tool Action result if applicable, Timeline export, and Evidence Pack manifest.

## Rationale

Evidence is not an audit-log afterthought. It is a core product primitive and the basis for Aegis trust claims.

This decision makes the MVP demonstrably different from a chatbot, agent demo, or observability dashboard.

## Consequences

Positive consequences:

- MVP-A can demonstrate provable AI work;
- Timeline and evidence reinforce each other;
- policy and tool decisions become inspectable;
- future eval, feedback, and outcome records can extend the pack.

Negative consequences:

- evidence schema and artifact writing must be implemented early;
- demo flow must include evidence generation;
- incomplete records become visible.

## Alternatives Considered

### Alternative 1 — Use logs as evidence

Rejected. Logs may support operations, but logs are not a structured product artifact.

### Alternative 2 — Defer evidence packs until later

Rejected. Without Evidence Pack generation, MVP-A does not prove Aegis.

### Alternative 3 — Generate only a model summary

Rejected. A model summary is not authoritative evidence.

## Doctrine Alignment

This decision preserves Law 7, Law 8, CTRL-006, CTRL-007, and MVP-A Trust Ladder Level 5.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Evidence pack too large for MVP | Use manifest plus references to local JSON artifacts. |
| Evidence generated after missing records | Require proposal, policy, disposition, and tool records first. |
| Evidence treated as logs | Use explicit Evidence Pack schema and use case. |
| Evidence lacks timeline | Include Timeline export/reference. |

## Related

- `docs/planning/work-packets/WP-E0-004-mvp-system-boundaries.md`
- `docs/architecture/architecture-doctrine.md`
- `docs/architecture/aegis-laws.md`
- `docs/product/trust-ladder.md`
