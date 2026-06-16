---
title: ADR-0007 — Event-rich records without full event sourcing
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
adr: ADR-0007
last_updated: 2026-06-16
---

# ADR-0007 — Event-rich records without full event sourcing

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.


## Status

Proposed

## Date

2026-06-16

## Context

Aegis requires events to reconstruct what happened during a Run. However, the MVP explicitly defers full event sourcing.

The architecture must capture enough event and record history for Timeline and Evidence Pack behavior without introducing unnecessary event-sourcing infrastructure.

## Decision

Use event-rich records for MVP-A, but do not implement full event sourcing.

MVP-A must record key events such as RunCreated, ProposalSubmitted, ToolActionProposed, PolicyCheckCompleted, ToolActionDispositioned, ApprovalGateRequested, ApprovalDecisionRecorded, ToolActionMockExecuted, ToolActionBlocked, and EvidencePackGenerated.

These events support Timeline reconstruction and Evidence Pack generation, but application state may still be stored in conventional records.

## Rationale

This approach captures the evidence value of events without requiring event replay, aggregate reconstruction, event version migration frameworks, or distributed event brokers in MVP-A.

It preserves the doctrine: event-rich, not prematurely event-sourced.

## Consequences

Positive consequences:

- Timeline reconstruction becomes possible;
- evidence can cite event history;
- implementation remains simpler than event sourcing;
- future event sourcing remains possible if justified.

Negative consequences:

- not every state change is necessarily event-sourced;
- replay is not guaranteed in MVP-A;
- consistency rules must be handled by application use cases.

## Alternatives Considered

### Alternative 1 — Full event sourcing immediately

Rejected for MVP-A. Full event sourcing adds complexity before the proof loop is implemented.

### Alternative 2 — No events, only CRUD records

Rejected. Aegis requires Timeline reconstruction and evidence-grade history.

### Alternative 3 — Observability logs only

Rejected. Logs do not provide governed domain events.

## Doctrine Alignment

This decision preserves event-rich doctrine, selective CQRS doctrine, Law 8, FF-006, and local-first simplicity.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Events become inconsistent | Use versioned event schemas. |
| Events treated as logs | Use domain event names and Run IDs. |
| Future migration is hard | Include schema version and stable IDs. |
| Timeline misses non-event records | Timeline may join events with related records. |

## Related

- `docs/planning/work-packets/WP-E0-004-mvp-system-boundaries.md`
- `docs/architecture/architecture-doctrine.md`
- `docs/architecture/aegis-laws.md`
- `docs/architecture/architecture-fitness-functions.md`
