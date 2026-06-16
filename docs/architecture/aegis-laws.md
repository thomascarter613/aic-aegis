---
title: Aegis Laws
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Accepted
work_packet: WP-E0-003A
source_bundle: ChatGPT Project Sources
last_updated: 2026-06-15
---

# Aegis Laws

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Purpose

This document defines the Aegis laws. Laws are stronger than preferences. They express invariant product and architecture constraints.

## 2. Laws

### Law 1 — The Model Proposes; the Platform Disposes

Model output is never inherently authoritative. Aegis must decide what happens to every important model-originated proposal.

**Implications:**

- The law must be visible in work packets, ADRs, APIs, and schemas.
- Implementations that violate this law require explicit rejection or redesign.
- Tests should eventually encode this law as an architecture or fitness check.

### Law 2 — No External Effect Without a Governed Boundary

No tool action, memory write, approval-sensitive step, or business-impacting side effect may bypass Aegis boundaries.

**Implications:**

- The law must be visible in work packets, ADRs, APIs, and schemas.
- Implementations that violate this law require explicit rejection or redesign.
- Tests should eventually encode this law as an architecture or fitness check.

### Law 3 — Proposals Are Records

Important model outputs must be captured as Proposal records before disposition.

**Implications:**

- The law must be visible in work packets, ADRs, APIs, and schemas.
- Implementations that violate this law require explicit rejection or redesign.
- Tests should eventually encode this law as an architecture or fitness check.

### Law 4 — Policy Is Attached to Disposition

A platform disposition must be traceable to policy, control, approval, or configured rule.

**Implications:**

- The law must be visible in work packets, ADRs, APIs, and schemas.
- Implementations that violate this law require explicit rejection or redesign.
- Tests should eventually encode this law as an architecture or fitness check.

### Law 5 — Tools Are Brokered

External tools are reached through the Tool Broker, not directly by the model.

**Implications:**

- The law must be visible in work packets, ADRs, APIs, and schemas.
- Implementations that violate this law require explicit rejection or redesign.
- Tests should eventually encode this law as an architecture or fitness check.

### Law 6 — Memory Is Admitted, Not Merely Written

New memory begins as a Memory Candidate and becomes governed memory only after admission.

**Implications:**

- The law must be visible in work packets, ADRs, APIs, and schemas.
- Implementations that violate this law require explicit rejection or redesign.
- Tests should eventually encode this law as an architecture or fitness check.

### Law 7 — Evidence Is a Product Primitive

Aegis must generate evidence artifacts that explain governed AI work.

**Implications:**

- The law must be visible in work packets, ADRs, APIs, and schemas.
- Implementations that violate this law require explicit rejection or redesign.
- Tests should eventually encode this law as an architecture or fitness check.

### Law 8 — Timelines Must Be Reconstructable

A Run must be explainable after the fact through ordered events and related records.

**Implications:**

- The law must be visible in work packets, ADRs, APIs, and schemas.
- Implementations that violate this law require explicit rejection or redesign.
- Tests should eventually encode this law as an architecture or fitness check.

### Law 9 — High-Risk Work Requires Stronger Disposition

High-risk proposals must be blocked, mocked, modified, or approval-gated.

**Implications:**

- The law must be visible in work packets, ADRs, APIs, and schemas.
- Implementations that violate this law require explicit rejection or redesign.
- Tests should eventually encode this law as an architecture or fitness check.

### Law 10 — Local Simplicity Must Not Break Future Governance

The MVP may be simple, but simplicity must not remove the governing boundaries that define Aegis.

**Implications:**

- The law must be visible in work packets, ADRs, APIs, and schemas.
- Implementations that violate this law require explicit rejection or redesign.
- Tests should eventually encode this law as an architecture or fitness check.


## 3. Law-to-MVP Mapping

| Law | MVP-A Proof Loop | MVP-B Learning Loop |
|---|---|---|
| Model proposes; platform disposes | Proposal and disposition records | Memory/eval/outcome proposals are still governed |
| No external effect without boundary | Tool Broker | Memory Admission Gate and outcome recording |
| Proposals are records | Tool Action Proposal | Memory Candidate and feedback-derived candidates |
| Policy attached to disposition | Policy Check record | Memory admission and eval criteria |
| Tools are brokered | Required | Still required |
| Memory is admitted | Deferred | Required |
| Evidence is product primitive | Evidence Pack | Evidence includes feedback/eval/outcome |
| Timelines reconstructable | Run Timeline | Learning Timeline extensions |
| High-risk work stronger disposition | Block/approval gate | Admission rejection and eval failure |
| Local simplicity preserves governance | Mock model/tool allowed | Local memory/eval allowed |

## 4. Non-Negotiable Design Tests

A proposed design fails if:

1. the model can execute a tool directly;
2. a tool action lacks a Proposal record;
3. policy is not attached to disposition;
4. high-risk work can proceed silently;
5. evidence is optional for governed actions;
6. memory can be written without admission;
7. a Run cannot be reconstructed;
8. the architecture forces Kubernetes or cloud services for the MVP;
9. Aegis is described primarily as an agent framework;
10. the UI bypasses the headless API and governing boundaries.

## 5. Done Means

This laws document is done when it:

- states the core law;
- expands it into enforceable supporting laws;
- maps laws to MVP-A and MVP-B;
- provides design tests for later review;
- gives future ADRs a clear normative reference.
