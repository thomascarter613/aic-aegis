---
title: WP-E0-003 — Architecture Overview
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Complete
work_packet: WP-E0-003
source_bundle: ChatGPT Project Sources
last_updated: 2026-06-15
---

# WP-E0-003 — Architecture Overview

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Work Packet Summary

WP-E0-003 produced the initial architecture overview for AIC Aegis.

It translated the product charter, glossary, and architecture doctrine into a system-level description of how Aegis governs AI work through the MVP proof loop and future learning loop.

## 2. Objective

Define the first architecture overview for Aegis as a control plane for provable AI work.

The work packet must answer:

- What kind of system is Aegis?
- What are its major logical components?
- How does MVP-A flow from Run creation to Evidence Pack?
- How does MVP-B extend MVP-A with governed learning?
- Which architecture boundaries must be preserved?
- Which platform ambitions are deferred?

## 3. Inputs

This work packet depends on:

- WP-E0-001 Product Charter;
- WP-E0-002 System Glossary;
- WP-E0-003A Architecture Doctrine Pack;
- Aegis Laws;
- MVP Strategy;
- Control Catalog;
- Risk Register.

## 4. Outputs

Primary output:

- `docs/architecture/system-overview.md`

Related updated output:

- `docs/architecture/README.md`

## 5. Architecture Decisions Captured

This work packet established that Aegis should be described as:

- a reliability control plane;
- Clean Architecture-based;
- domain-driven;
- event-rich;
- selectively CQRS;
- policy-enforced;
- evidence-first;
- headless;
- API-first;
- local-first;
- cloud-native-capable.

## 6. MVP-A Proof Loop Boundary

WP-E0-003 confirms that MVP-A includes:

1. create Run;
2. record events;
3. model/mock model proposes Tool Action;
4. Tool Broker receives Proposal;
5. policy checks tool action;
6. safe action proceeds or is mocked;
7. high-risk action is blocked or approval-gated;
8. Evidence Pack is generated;
9. Run Timeline is visible.

## 7. MVP-B Learning Loop Boundary

WP-E0-003 confirms that MVP-B includes:

1. governed memory retrieval;
2. memory candidate proposal;
3. Memory Admission Gate;
4. feedback capture;
5. basic Eval Result;
6. Business Outcome Event.

## 8. Major Logical Components

The architecture overview identifies these components:

- Run Registry;
- Event Recorder;
- Proposal Intake;
- Tool Broker;
- Policy Engine Port;
- Approval Gate;
- Evidence Service;
- Timeline Query;
- Memory Service;
- Eval and Outcome Services.

## 9. Clean Architecture Boundary

WP-E0-003 reinforces:

- domain owns core concepts and rules;
- application owns use cases, commands, queries, orchestration, and ports;
- adapters implement persistence, policy, model, tool, evidence, and memory ports;
- interfaces expose HTTP/API/CLI/worker entry points.

## 10. Explicit Non-Goals

WP-E0-003 does not introduce:

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

## 11. Acceptance Criteria

This work packet is complete when:

- the system overview explains Aegis as a control plane;
- MVP-A and MVP-B are clearly separated;
- major logical components are named;
- Clean Architecture boundaries are present;
- evidence-first and policy-enforced doctrine are preserved;
- local-first and cloud-native-capable posture is stated;
- deferred platform ambitions are explicit;
- WP-E0-004 can begin from the overview.

## 12. Completion Status

Status: **Complete**

WP-E0-003 is complete and the next recommended work packet is:

**WP-E0-004 — MVP System Boundaries**

## 13. Handoff to WP-E0-004

WP-E0-004 should define exact MVP boundaries for:

- what belongs in MVP-A vs MVP-B;
- API service vs worker service;
- domain/application/adapters package boundaries;
- command/query boundaries;
- event boundaries;
- schema boundaries;
- persistence boundaries;
- policy/tool/memory/evidence/eval/outcome thin-slice boundaries;
- what is explicitly out of scope;
- acceptance criteria for moving into WP-E0-005 Initial ADR Pack.
