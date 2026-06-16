---
title: WP-E0-005 — Initial ADR Pack
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
work_packet: WP-E0-005
depends_on:
  - WP-E0-001
  - WP-E0-002
  - WP-E0-003A
  - WP-E0-003
  - WP-E0-004
last_updated: 2026-06-16
---

# WP-E0-005 — Initial ADR Pack

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Work Packet Summary

WP-E0-005 establishes the initial Architecture Decision Record pack for AIC Aegis.

The purpose of this work packet is to convert accepted doctrine and MVP system boundaries into durable implementation-shaping decisions before coding begins.

This packet does not implement the MVP. It creates the decision baseline that future implementation work packets must follow.

## 2. Objective

Create an initial ADR pack that locks the MVP-A architectural path without prematurely expanding the platform.

The ADR pack must decide:

- local-first modular architecture for MVP-A;
- Clean Architecture package boundaries;
- model output as Proposal records;
- Tool Broker as mandatory boundary for tool actions;
- Policy Check before external effect;
- Evidence Pack as a product artifact;
- event-rich records without full event sourcing;
- MVP-A independence from MVP-B learning loop;
- mock model and mock tools for MVP-A;
- headless/API-first system posture.

## 3. Inputs

This work packet depends on:

- `docs/product/product-charter.md`
- `docs/glossary/system-glossary.md`
- `docs/architecture/architecture-doctrine.md`
- `docs/architecture/aegis-laws.md`
- `docs/architecture/system-overview.md`
- `docs/architecture/architecture-fitness-functions.md`
- `docs/governance/control-catalog.md`
- `docs/governance/risk-register.md`
- `docs/product/mvp-strategy.md`
- `docs/product/trust-ladder.md`
- `docs/product/maturity-model.md`
- `docs/decisions/product-decisions/README.md`
- `docs/planning/work-packets/WP-E0-004-mvp-system-boundaries.md`

## 4. Outputs

Primary outputs:

- `docs/decisions/adr/README.md`
- `docs/decisions/adr/ADR-0001-local-first-modular-monolith-for-mvp-a.md`
- `docs/decisions/adr/ADR-0002-clean-architecture-package-boundaries.md`
- `docs/decisions/adr/ADR-0003-model-output-as-proposal-records.md`
- `docs/decisions/adr/ADR-0004-tool-broker-required-for-tool-actions.md`
- `docs/decisions/adr/ADR-0005-policy-check-before-external-effect.md`
- `docs/decisions/adr/ADR-0006-evidence-pack-as-mvp-a-artifact.md`
- `docs/decisions/adr/ADR-0007-event-rich-records-without-full-event-sourcing.md`
- `docs/decisions/adr/ADR-0008-mvp-a-independent-from-mvp-b-learning-loop.md`
- `docs/decisions/adr/ADR-0009-mock-model-and-mock-tools-for-mvp-a.md`
- `docs/decisions/adr/ADR-0010-headless-api-first-mvp.md`

## 5. ADR Index

| ID | Title | Status | Scope |
|---|---|---|---|
| ADR-0001 | Local-first modular monolith for MVP-A | Proposed | MVP-A deployment and codebase shape |
| ADR-0002 | Clean Architecture package boundaries | Proposed | Domain/application/adapters/interfaces |
| ADR-0003 | Model output as Proposal records | Proposed | Model boundary and Proposal capture |
| ADR-0004 | Tool Broker required for tool actions | Proposed | Tool execution governance |
| ADR-0005 | Policy Check before external effect | Proposed | Policy and disposition |
| ADR-0006 | Evidence Pack as MVP-A artifact | Proposed | Evidence-first product behavior |
| ADR-0007 | Event-rich records without full event sourcing | Proposed | Timeline/evidence events |
| ADR-0008 | MVP-A independent from MVP-B Learning Loop | Proposed | MVP sequencing |
| ADR-0009 | Mock model and mock tools for MVP-A | Proposed | Local-safe demonstration |
| ADR-0010 | Headless/API-first MVP | Proposed | Interface posture |

## 6. Decision Themes

### 6.1 Preserve Control-Plane Identity

The ADRs protect Aegis from drifting into a generic AI agent framework, chatbot application, workflow builder, or observability dashboard.

### 6.2 Preserve MVP Thin Slice

The ADRs keep MVP-A focused on the Proof Loop:

1. create Run;
2. record events;
3. capture Proposal;
4. broker Tool Action;
5. check policy;
6. dispose proposal;
7. mock/block/approval-gate action;
8. generate Evidence Pack;
9. show Timeline.

### 6.3 Preserve Future Optionality

The ADRs allow local-first MVP implementation while keeping future cloud-native capability possible through ports, adapters, schemas, and clear boundaries.

## 7. Non-Goals

WP-E0-005 does not decide:

- final programming language;
- web framework;
- ORM;
- database;
- queue/broker technology;
- cloud provider;
- deployment platform;
- authentication provider;
- production connector architecture;
- UI framework;
- enterprise tenant model;
- compliance certification strategy.

Those decisions belong to later implementation ADRs only when needed.

## 8. Acceptance Criteria

WP-E0-005 is accepted when:

- the initial ADR directory exists;
- each ADR uses a consistent template;
- each ADR references the core law;
- each ADR preserves MVP-A/MVP-B separation;
- the ADR pack supports WP-E0-004 boundaries;
- the ADRs do not introduce premature microservices, Kubernetes, marketplace, enterprise SSO, billing, real customer data, or broad connector scope;
- the ADRs provide enough implementation direction to begin MVP-A planning.

## 9. Done Means

WP-E0-005 is done when:

1. the ADR index is present;
2. ADR-0001 through ADR-0010 are drafted;
3. all ADRs are internally consistent;
4. doctrine and boundary violations are avoided;
5. the project is ready for the first implementation planning work packet.

## 10. Handoff

After WP-E0-005 is accepted, the next work should be an implementation planning packet for the MVP-A Proof Loop.

Recommended next packet:

**WP-E1-001 — MVP-A Implementation Plan**

Likely scope:

- choose initial implementation language/framework;
- define repository package/module layout;
- define MVP-A schemas;
- define MVP-A API routes;
- define MVP-A persistence records;
- define local demo scenario;
- define acceptance tests;
- define minimal CI checks;
- define first coding sequence.
