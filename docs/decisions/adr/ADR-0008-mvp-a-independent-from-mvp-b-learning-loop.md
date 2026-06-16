---
title: ADR-0008 — MVP-A independent from MVP-B Learning Loop
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
adr: ADR-0008
last_updated: 2026-06-16
---

# ADR-0008 — MVP-A independent from MVP-B Learning Loop

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.


## Status

Proposed

## Date

2026-06-16

## Context

The MVP strategy separates MVP-A Proof Loop from MVP-B Learning Loop.

A common product risk is mixing governed memory, feedback, evals, and outcomes into MVP-A before proposal-to-evidence governance works.

## Decision

MVP-A must be implemented and accepted without requiring MVP-B learning-loop capabilities.

MVP-A must not require governed memory retrieval, Memory Candidate proposal, Memory Admission Gate, Feedback Event capture, Eval Result recording, or Business Outcome Event recording.

MVP-B may later reuse MVP-A primitives, including Runs, Events, Proposals, Policy Checks, Evidence Packs, and Timelines.

## Rationale

Aegis must first prove that it can govern proposed AI work. Learning is valuable, but learning without the proof loop creates ungoverned memory and outcome overclaiming risks.

## Consequences

Positive consequences:

- MVP-A remains smaller;
- implementation can focus on Proof Loop controls;
- memory/eval/outcome designs can build on evidence;
- acceptance criteria are clearer.

Negative consequences:

- MVP-A will not yet show governed learning;
- feedback and outcome value is deferred;
- memory-related demos must wait until MVP-B.

## Alternatives Considered

### Alternative 1 — Include memory in MVP-A

Rejected. Memory introduces admission and provenance concerns that belong to MVP-B.

### Alternative 2 — Include evals in MVP-A

Rejected. Eval records are useful but not required to prove proposal-to-evidence governance.

### Alternative 3 — Build learning loop first

Rejected. Learning without governed action/evidence risks amplifying untrusted model output.

## Doctrine Alignment

This decision preserves MVP Strategy, Maturity Model M1 before M2, MVP-A/MVP-B separation, RISK-004 mitigation, and RISK-010 mitigation.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| MVP-A grows too broad | Reject features that depend on memory/eval/outcome. |
| Placeholder interfaces create confusion | Mark them deferred and non-blocking. |
| MVP-B has to redo MVP-A | Design MVP-A primitives for reuse. |
| Outcome value delayed | Capture product rationale but defer implementation. |

## Related

- `docs/planning/work-packets/WP-E0-004-mvp-system-boundaries.md`
- `docs/architecture/architecture-doctrine.md`
- `docs/architecture/aegis-laws.md`
- `docs/product/mvp-strategy.md`
- `docs/product/maturity-model.md`
