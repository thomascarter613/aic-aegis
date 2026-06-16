---
title: System Overview
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Accepted
work_packet: WP-E0-003
source_bundle: ChatGPT Project Sources
last_updated: 2026-06-15
---

# System Overview

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Purpose

This document describes the AIC Aegis system at the architecture-overview level. It explains the major components, their responsibilities, and the MVP trust loop without locking the project into premature infrastructure choices.

## 2. System Summary

Aegis is a control plane for provable AI work.

It governs Runs through:

- identity and Actor tracking;
- runtime events;
- model/mock model Proposals;
- policy checks;
- Tool Broker decisions;
- approval gates;
- evidence packs;
- run timelines;
- governed memory;
- evals;
- feedback loops;
- business outcome records.

## 3. Architectural Posture

Aegis is:

- **headless:** primary interaction is through APIs, commands, queries, schemas, and artifacts;
- **API-first:** UI is optional and later;
- **local-first:** MVP runs without cloud dependencies;
- **cloud-native-capable:** architecture remains portable to cloud deployment;
- **Clean Architecture-based:** domain and application boundaries stay independent of adapters;
- **event-rich:** important work is captured as events and records;
- **policy-enforced:** platform disposition depends on explicit policy/control results;
- **evidence-first:** evidence is generated as a product outcome.

## 4. Major Logical Components

### 4.1 Run Registry

Owns Run identity and lifecycle.

Responsibilities:

- create Run;
- store Run metadata;
- associate Actor, purpose, workflow, status, timestamps;
- expose Run queries.

### 4.2 Event Recorder

Captures Run Events.

Responsibilities:

- append normalized events;
- validate event schema;
- preserve event ordering;
- provide Timeline source data.

### 4.3 Proposal Intake

Receives model/mock model proposals.

Responsibilities:

- validate proposal schema;
- associate proposal with Run and Actor;
- classify proposal type and risk context;
- forward Tool Action proposals to the Tool Broker.

### 4.4 Tool Broker

Mediates proposed external effects.

Responsibilities:

- receive Tool Action Proposal;
- validate tool/action schema;
- request Policy Check;
- enforce disposition;
- route to approval if required;
- call mock or real tool adapter when allowed;
- record Tool Action result;
- attach evidence.

### 4.5 Policy Engine Port

Evaluates proposals and tool actions against controls.

Responsibilities:

- accept normalized policy input;
- return allow/block/approval/mocking disposition;
- identify controls and risks;
- produce policy evidence.

### 4.6 Approval Gate

Handles proposals that require human or configured approval.

Responsibilities:

- create approval request;
- record approval status;
- prevent execution until approved;
- preserve approver identity and rationale.

### 4.7 Evidence Service

Generates Evidence Packs.

Responsibilities:

- collect Run records;
- collect events, proposals, policy checks, tool results, approvals;
- produce manifest;
- write evidence artifacts;
- expose evidence pack metadata.

### 4.8 Timeline Query

Builds explainable Run Timeline.

Responsibilities:

- order events;
- join related records;
- present platform decisions;
- expose queryable timeline response.

### 4.9 Memory Service

Deferred to MVP-B.

Responsibilities:

- retrieve governed memory;
- accept Memory Candidates;
- invoke Memory Admission Gate;
- record admission/rejection;
- preserve provenance.

### 4.10 Eval and Outcome Services

Deferred to MVP-B.

Responsibilities:

- record feedback;
- record Eval Results;
- record Business Outcome Events;
- connect learning records to Runs.

## 5. MVP-A Flow

1. Client creates a Run.
2. A Run Event is recorded.
3. Mock model creates a Tool Action Proposal.
4. Proposal Intake validates and records the Proposal.
5. Tool Broker receives the Tool Action Proposal.
6. Policy Check evaluates the proposed action.
7. Platform disposition is produced:
   - allowed;
   - mocked;
   - blocked;
   - approval required.
8. Tool Broker executes or mocks safe action.
9. Approval Gate handles high-risk action if applicable.
10. Evidence Service generates Evidence Pack.
11. Timeline Query returns a visible Run Timeline.

## 6. MVP-B Flow

1. Client or workflow retrieves governed memory.
2. Run proceeds with retrieved memory recorded as context.
3. Model/mock model proposes Memory Candidate.
4. Memory Admission Gate evaluates candidate.
5. Feedback Event is captured.
6. Eval Result is recorded.
7. Business Outcome Event is recorded.
8. Evidence and Timeline include learning-loop records.

## 7. Clean Architecture Package Boundary

Recommended logical packages:

```text
src/
  domain/
    run/
    actor/
    proposal/
    policy/
    tool/
    approval/
    evidence/
    memory/
    feedback/
    eval/
    outcome/
  application/
    commands/
    queries/
    ports/
    use-cases/
  adapters/
    persistence/
    policy/
    model/
    tools/
    evidence/
    memory/
  interfaces/
    http/
    cli/
    worker/
```

## 8. API and Worker Boundary

### API Service

The API service should own request/response interaction:

- create Run;
- submit Proposal;
- query Run;
- query Timeline;
- request Evidence Pack generation;
- retrieve Evidence Pack metadata.

### Worker Service

The worker boundary may handle asynchronous or long-running work:

- evidence generation;
- tool execution;
- approval wait/resume;
- eval processing;
- memory admission workflows.

MVP-A may implement worker-like behavior synchronously if the boundary remains conceptually intact.

## 9. Persistence Overview

MVP persistence may begin simple.

Minimum records:

- Run;
- Run Event;
- Proposal;
- Policy Check;
- Tool Action;
- Approval Request;
- Evidence Pack;
- Evidence Artifact.

MVP-B adds:

- Memory Candidate;
- Memory Admission;
- Feedback Event;
- Eval Result;
- Business Outcome Event.

## 10. Out of Scope for MVP

The following are deferred:

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

WP-E0-003 is accepted when the system overview:

- explains Aegis as a control plane;
- names major logical components;
- shows MVP-A proof-loop flow;
- shows MVP-B learning-loop extension;
- preserves Clean Architecture boundaries;
- identifies API and worker responsibilities;
- avoids premature infrastructure expansion;
- prepares WP-E0-004 to define exact MVP boundaries.
