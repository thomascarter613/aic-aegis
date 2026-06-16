---
title: MVP Strategy
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Accepted
work_packet: WP-E0-003A
source_bundle: ChatGPT Project Sources
last_updated: 2026-06-15
---

# MVP Strategy

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Purpose

This document defines the MVP strategy for AIC Aegis.

The MVP strategy is:

**Build a thin vertical slice through the trust loop, not a broad platform.**

## 2. Strategic Principle

Aegis must prove that governed AI work can be represented, controlled, evidenced, and inspected.

The MVP should not attempt to prove every future platform capability. It should prove the irreducible trust loop.

## 3. Golden Workflow

The golden workflow is:

**Governed Sales/Ops Follow-Up**

This workflow is intentionally narrow because it naturally exercises the Aegis boundaries:

- a business purpose exists;
- a model can propose a follow-up action;
- the action may be safe or risky;
- policy can classify the action;
- approval may be required;
- evidence matters;
- outcomes can later be tracked.

## 4. MVP-A: Proof Loop

MVP-A proves platform disposition over proposed AI work.

### 4.1 Included

- create Run;
- record Run Events;
- model/mock model proposes Tool Action;
- Tool Broker receives Proposal;
- policy checks tool action;
- safe action proceeds or is mocked;
- high-risk action is blocked or approval-gated;
- Evidence Pack is generated;
- Run Timeline is visible.

### 4.2 Not Included

- governed memory retrieval;
- memory candidate proposal;
- eval loops;
- business outcome records;
- broad integrations;
- production email sending;
- customer data;
- enterprise auth;
- billing.

## 5. MVP-B: Learning Loop

MVP-B extends MVP-A with governed learning.

### 5.1 Included

- governed memory retrieval;
- Memory Candidate proposal;
- Memory Admission Gate;
- feedback capture;
- basic Eval Result;
- Business Outcome Event.

### 5.2 Not Included

- autonomous memory mutation;
- complex eval frameworks;
- large-scale analytics;
- full outcome attribution;
- multi-tenant enterprise governance.

## 6. Thin Slice Test

A proposed MVP feature should be rejected or deferred if it does not help answer one of these questions:

1. What did the model propose?
2. What did Aegis decide?
3. Why did Aegis decide that?
4. Was policy applied?
5. Was approval required?
6. Was a tool action allowed, blocked, mocked, or gated?
7. What evidence was produced?
8. Can the Run be reconstructed?
9. For MVP-B, what was learned and how was it admitted?

## 7. Recommended Build Order

### Stage A1 — Run and Event Backbone

- Run entity;
- Actor identity;
- Run Event schema;
- append/list events;
- basic Timeline query.

### Stage A2 — Proposal and Tool Broker

- Proposal schema;
- Tool Action Proposal;
- Tool Broker use case;
- mock tool adapter.

### Stage A3 — Policy and Disposition

- policy input schema;
- policy result schema;
- allow/block/mock/approval-required dispositions;
- risk/control references.

### Stage A4 — Approval and Evidence

- Approval Gate records;
- Evidence Pack manifest;
- artifact writer;
- Timeline enrichment.

### Stage B1 — Governed Memory

- memory retrieval record;
- Memory Candidate;
- Memory Admission Gate.

### Stage B2 — Feedback, Eval, Outcome

- Feedback Event;
- Eval Result;
- Business Outcome Event;
- evidence/timeline learning extensions.

## 8. Explicitly Deferred

- full microservices;
- Kubernetes;
- marketplace;
- plugin registry;
- visual workflow builder;
- multi-agent swarm;
- fine-tuning;
- enterprise SSO;
- billing;
- full event sourcing;
- real customer data;
- formal compliance claims;
- large connector ecosystem.

## 9. MVP Acceptance Criteria

The MVP strategy is accepted when:

- MVP-A and MVP-B are distinct;
- the golden workflow is named;
- MVP-A proves governed proposal-to-evidence flow;
- MVP-B adds learning without memory bypass;
- deferred items are explicit;
- the strategy supports WP-E0-004 boundary definition.
