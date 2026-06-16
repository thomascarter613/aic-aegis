---
title: Architecture Decision Records
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
last_updated: 2026-06-16
---

# Architecture Decision Records

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Purpose

This directory contains Architecture Decision Records for AIC Aegis.

ADRs capture durable architecture choices that affect implementation, boundaries, dependencies, runtime behavior, evidence, policy, and future evolvability.

Product decisions define what Aegis is and why it exists. ADRs define how the architecture will preserve those decisions in implementation.

## 2. ADR Index

| ID | Title | Status |
|---|---|---|
| ADR-0001 | Local-first modular monolith for MVP-A | Proposed |
| ADR-0002 | Clean Architecture package boundaries | Proposed |
| ADR-0003 | Model output as Proposal records | Proposed |
| ADR-0004 | Tool Broker required for tool actions | Proposed |
| ADR-0005 | Policy Check before external effect | Proposed |
| ADR-0006 | Evidence Pack as MVP-A artifact | Proposed |
| ADR-0007 | Event-rich records without full event sourcing | Proposed |
| ADR-0008 | MVP-A independent from MVP-B Learning Loop | Proposed |
| ADR-0009 | Mock model and mock tools for MVP-A | Proposed |
| ADR-0010 | Headless/API-first MVP | Proposed |

## 3. ADR Status Values

Use these statuses:

- Proposed
- Accepted
- Superseded
- Deprecated
- Deferred
- Rejected

## 4. ADR Template

```markdown
# ADR-XXXX — Decision Title

## Status

Proposed | Accepted | Superseded | Deprecated | Deferred | Rejected

## Date

YYYY-MM-DD

## Context

What forces, constraints, doctrine, risks, and ambiguity require a decision?

## Decision

What decision is being made?

## Rationale

Why is this the right decision for Aegis?

## Consequences

What becomes easier, harder, enabled, constrained, or deferred?

## Alternatives Considered

What other options were considered and why were they not selected?

## Doctrine Alignment

How does this preserve the Aegis core law and architecture doctrine?

## Risks and Mitigations

What could go wrong and how is the risk reduced?

## Related

- Work packets
- Doctrine docs
- Product decisions
- Fitness functions
```

## 5. ADR Rules

1. ADRs must preserve the core law: the model proposes; the platform disposes.
2. ADRs must not silently expand MVP scope.
3. ADRs must distinguish MVP-A from MVP-B.
4. ADRs must not introduce real customer data, real external effects, or production connectors into MVP-A.
5. ADRs must preserve Clean Architecture boundaries.
6. ADRs must explain consequences, not only decisions.
7. ADRs that supersede earlier decisions must explicitly identify what changed.
