---
title: Maturity Model
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Accepted
work_packet: WP-E0-003A
source_bundle: ChatGPT Project Sources
last_updated: 2026-06-15
---

# Maturity Model

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Purpose

The maturity model describes how Aegis can evolve without losing its doctrine.

It is not a commitment to build every level immediately. It is a guide for sequencing.

## 2. Maturity Levels

| Level | Name | Description | Product State |
|---|---|---|---|
| M0 | Doctrine Defined | Core law, glossary, charter, architecture doctrine exist. | Completed by E0 documents |
| M1 | Proof Loop | A single governed workflow proves proposal-to-evidence. | MVP-A |
| M2 | Learning Loop | Governed memory, feedback, evals, and outcomes are added. | MVP-B |
| M3 | Repeatable Operations | Multiple runs and policies support repeated internal use. | Post-MVP |
| M4 | Governed Integrations | Carefully selected real integrations are added. | Later |
| M5 | Enterprise Control Plane | Multi-tenant, enterprise controls, approvals, reporting mature. | Later |
| M6 | Ecosystem Platform | Plugin/marketplace patterns become safe and useful. | Much later |

## 3. Current Target

The current target is **M1 Proof Loop** through MVP-A.

M2 Learning Loop is next, but must not be mixed into MVP-A except as explicit design preparation.

## 4. Maturity Requirements

### M0 — Doctrine Defined

Required:

- product charter;
- glossary;
- architecture doctrine;
- laws;
- MVP strategy;
- control catalog;
- risk register;
- system overview.

### M1 — Proof Loop

Required:

- Run creation;
- event recording;
- Proposal capture;
- Tool Broker;
- Policy Check;
- allow/block/mock/approval disposition;
- Evidence Pack;
- Timeline.

### M2 — Learning Loop

Required:

- governed memory retrieval;
- Memory Candidate;
- Memory Admission Gate;
- Feedback Event;
- Eval Result;
- Business Outcome Event.

### M3 — Repeatable Operations

Possible later capabilities:

- multiple workflow templates;
- expanded policy library;
- richer evidence query;
- admin review workflows;
- replay/simulation;
- metrics.

### M4 — Governed Integrations

Possible later capabilities:

- real CRM connector;
- real email connector;
- task system connector;
- signed tool execution records;
- integration-specific controls.

### M5 — Enterprise Control Plane

Possible later capabilities:

- enterprise identity;
- multi-tenant governance;
- approval delegation;
- audit reporting;
- retention controls;
- compliance mappings.

### M6 — Ecosystem Platform

Possible later capabilities:

- plugin registry;
- marketplace;
- third-party controls;
- connector certification;
- partner ecosystem.

## 5. Explicit Sequencing Guardrail

Do not pursue M4-M6 capabilities until M1 and M2 prove the trust loop.

## 6. Done Means

The maturity model is done when it:

- defines maturity levels;
- identifies the current target;
- protects MVP sequencing;
- distinguishes future enterprise/platform ambitions from current work.
