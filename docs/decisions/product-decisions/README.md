---
title: Product Decisions README
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Accepted
source_bundle: ChatGPT Project Sources
last_updated: 2026-06-15
---

# Product Decisions README

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Purpose

This directory contains product decision records for AIC Aegis.

Product decisions capture durable choices that guide work packets and architecture decisions. They are related to ADRs, but focus on product identity, MVP scope, sequencing, and positioning.

## 2. Product Decision Index

| ID | Decision | Status | Summary |
|---|---|---|---|
|PDR-0001|Aegis is a reliability control plane|Accepted|Aegis is positioned as a control plane for provable AI work, not a generic agent framework.|
|PDR-0002|Core law|Accepted|The model proposes; the platform disposes.|
|PDR-0003|MVP strategy|Accepted|Build a thin vertical slice through the trust loop, not a broad platform.|
|PDR-0004|Golden workflow|Accepted|Governed Sales/Ops Follow-Up|
|PDR-0005|MVP-A / MVP-B separation|Accepted|MVP-A is Proof Loop; MVP-B is Learning Loop.|
|PDR-0006|Local-first MVP|Accepted|MVP must run locally without required cloud infrastructure.|
|PDR-0007|Headless/API-first posture|Accepted|APIs, schemas, events, and evidence artifacts are primary.|
|PDR-0008|Deferred platform breadth|Accepted|Microservices, Kubernetes, marketplace, enterprise SSO, billing, and large connector ecosystem are deferred.|

## 3. Decision Record Template

Use this template for new product decisions:

```markdown
# PDR-XXXX — Decision Title

## Status

Proposed | Accepted | Superseded | Deferred

## Context

What problem or ambiguity requires a decision?

## Decision

What decision was made?

## Rationale

Why is this the right product decision?

## Consequences

What becomes easier, harder, enabled, or deferred?

## Related Doctrine

- Product Charter
- System Glossary
- Aegis Laws
- Architecture Doctrine
- MVP Strategy

## Related Work Packets

- WP-E0-XXX
```

## 4. Decision Rules

1. Product decisions must preserve the core law.
2. Product decisions must not silently expand MVP scope.
3. Product decisions must distinguish accepted scope from deferred ambition.
4. Decisions affecting architecture must later be represented in ADRs when implementation begins.
5. Decisions that change terminology must update the System Glossary.

## 5. Initial Decision Notes

### PDR-0001 — Aegis is a reliability control plane

Aegis governs AI work. It is not primarily a chatbot, a prompt tool, an agent runtime, a generic workflow builder, or an observability dashboard.

### PDR-0002 — Core law

The model proposes; the platform disposes.

### PDR-0003 — MVP strategy

The first milestone must prove the smallest coherent trust loop.

### PDR-0004 — Golden workflow

Governed Sales/Ops Follow-Up is narrow enough for MVP and realistic enough to exercise governance.

### PDR-0005 — MVP-A / MVP-B separation

MVP-A proves proposal-to-evidence. MVP-B adds governed learning.

## 6. Done Means

This README is done when it:

- defines purpose of product decision records;
- indexes initial decisions;
- provides a template;
- ties decisions to doctrine and work packets.
