---
title: ADR-0002 — Clean Architecture package boundaries
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
adr: ADR-0002
last_updated: 2026-06-16
---

# ADR-0002 — Clean Architecture package boundaries

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.


## Status

Proposed

## Date

2026-06-16

## Context

Aegis must keep the domain of governed AI work independent from frameworks, databases, model SDKs, external tools, and transport details.

Without explicit package boundaries, implementation can easily drift into a framework-shaped application where controllers, persistence, policy, model calls, and tool execution are tangled together.

## Decision

Use Clean Architecture package boundaries for MVP-A.

Required logical layers:

```text
domain/
application/
adapters/
interfaces/
```

The exact language-specific directory structure may vary, but responsibilities must remain stable.

## Rationale

Clean Architecture is already part of the Aegis doctrine. MVP-A needs it not for ceremony, but to enforce the core law.

The Tool Broker, Policy Check, Evidence Pack, and Timeline cannot be reliably governed if framework handlers or tool adapters can bypass application use cases.

## Consequences

Positive consequences:

- domain remains stable;
- business vocabulary remains explicit;
- infrastructure can change without rewriting core rules;
- application use cases become testable;
- architecture fitness checks become possible.

Negative consequences:

- more initial files and boundaries than a quick prototype;
- contributors must understand the layering;
- some simple operations may require explicit command/query plumbing.

## Alternatives Considered

### Alternative 1 — Framework-first structure

Rejected. A framework-first structure risks placing policy, evidence, and tool execution in controllers or handlers.

### Alternative 2 — Hexagonal-only naming

Not rejected, but folded into Clean Architecture. Ports and adapters remain central.

### Alternative 3 — Single flat package

Rejected. A flat package makes boundary violations harder to detect.

## Doctrine Alignment

This decision directly implements the architecture doctrine: domain independence, application-owned use cases, adapters as replaceable infrastructure, and interfaces as entry points.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Boundary becomes ceremonial | Add fitness checks and code review rules. |
| Too much abstraction too early | Define only MVP-A ports needed by the proof loop. |
| Application layer becomes anemic | Keep orchestration in use cases, not controllers. |
| Adapters leak infrastructure language | Map adapter details into Aegis domain terms. |

## Related

- `docs/planning/work-packets/WP-E0-004-mvp-system-boundaries.md`
- `docs/architecture/architecture-doctrine.md`
- `docs/architecture/aegis-laws.md`
- `docs/glossary/system-glossary.md`
