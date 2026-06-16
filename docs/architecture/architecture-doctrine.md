---
title: Architecture Doctrine
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Accepted
work_packet: WP-E0-003A
source_bundle: ChatGPT Project Sources
last_updated: 2026-06-15
---

# Architecture Doctrine

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Purpose

This document defines the architecture doctrine for AIC Aegis. It is the durable architectural compass for all work packets, ADRs, implementation plans, schemas, APIs, and code.

Doctrine is more stable than implementation detail. Later decisions may refine implementation, but they must not violate this doctrine without an explicit Decision Record.

## 2. Doctrine Statement

Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 3. Architectural Meaning

Aegis is a **control plane**. It coordinates, governs, records, and evaluates AI work. It is not the model, the business application, the user interface, or the external tool itself.

The architecture must separate:

- model proposal from platform disposition;
- policy evaluation from tool execution;
- run orchestration from infrastructure adapters;
- evidence generation from incidental logging;
- memory candidates from admitted memory;
- feedback from business outcomes;
- local MVP implementation from future cloud-native scaling.

## 4. Clean Architecture Doctrine

Aegis uses Clean Architecture boundaries.

### 4.1 Domain Layer

The domain layer contains core business concepts and rules.

Allowed domain concepts include:

- Run
- Actor
- Proposal
- Tool Action
- Policy Check
- Control
- Risk
- Approval Gate
- Evidence Pack
- Memory Candidate
- Memory Admission
- Feedback Event
- Eval Result
- Business Outcome Event
- Timeline
- Decision Record

The domain layer must not depend on:

- web frameworks;
- databases;
- queues;
- model SDKs;
- cloud providers;
- external tools;
- persistence libraries;
- HTTP clients.

### 4.2 Application Layer

The application layer contains use cases, commands, queries, orchestration, and ports.

Responsibilities include:

- create Run;
- record Run Event;
- submit Proposal;
- broker Tool Action;
- check policy;
- request approval;
- generate Evidence Pack;
- retrieve Timeline;
- propose Memory Candidate;
- admit or reject memory;
- capture feedback;
- record Eval Result;
- record Business Outcome Event.

The application layer may define ports for:

- Run repository;
- event store;
- policy engine;
- tool executor;
- approval store;
- evidence writer;
- model adapter;
- memory store;
- eval recorder;
- outcome recorder.

### 4.3 Adapters Layer

Adapters implement application ports.

Initial adapters may be simple and local:

- in-memory repository;
- file-backed evidence writer;
- mock model adapter;
- mock tool executor;
- local policy evaluator;
- SQLite/Postgres persistence adapter when needed.

Adapters are replaceable. Adapters do not own Aegis business language.

### 4.4 Interfaces Layer

Interfaces expose Aegis capabilities.

Initial interfaces may include:

- HTTP API;
- CLI;
- worker process;
- local script entry point.

Interfaces translate external requests into commands and queries.

## 5. Domain-Driven Doctrine

Aegis must use its own domain language rather than generic AI-agent language.

Domain-driven design means:

- concepts are named after the Aegis trust loop;
- terms are defined in the glossary;
- invariants are protected in domain/application boundaries;
- external tool and model concepts are mapped into Aegis concepts;
- the model does not define the domain.

## 6. Event-Rich Doctrine

Aegis is event-rich because explainability requires a historical record.

Event-rich does not mean full event sourcing in the MVP.

MVP events must be enough to reconstruct:

- who started the Run;
- what the model proposed;
- which policy checks were applied;
- what disposition occurred;
- whether approval was required;
- whether a tool was executed, mocked, blocked, or deferred;
- which evidence artifacts were generated;
- how the Timeline is assembled.

## 7. Selective CQRS Doctrine

Aegis may use command/query separation where it improves clarity.

Commands change state, such as:

- CreateRun
- RecordRunEvent
- SubmitProposal
- EvaluatePolicy
- BrokerToolAction
- RequestApproval
- GenerateEvidencePack

Queries read state, such as:

- GetRun
- ListRunEvents
- GetRunTimeline
- GetEvidencePack
- GetPolicyCheckResult

The MVP should not introduce heavy CQRS infrastructure. The doctrine requires semantic separation, not premature distributed systems.

## 8. Policy-Enforced Doctrine

Policy enforcement is not an afterthought.

Policy must be attached to platform disposition. Aegis must be able to answer:

- what policy was applied;
- what input was evaluated;
- what result was produced;
- which controls were implicated;
- what risk level was assigned;
- what disposition followed.

## 9. Evidence-First Doctrine

Evidence is a product primitive.

Every important action should be explainable later through:

- Run Events;
- Proposal records;
- Policy Check results;
- Tool Broker decisions;
- Approval Gate records;
- tool execution or mock records;
- Evidence Pack manifests;
- timeline exports.

Logs may support operations, but logs are not a substitute for evidence.

## 10. Headless and API-First Doctrine

Aegis must be usable without a UI.

The core product surface is:

- APIs;
- commands;
- queries;
- schemas;
- events;
- evidence artifacts.

A UI may be added later, but it must consume the same governed APIs rather than bypassing them.

## 11. Local-First Doctrine

MVP should run locally with minimal infrastructure.

Local-first implies:

- mock model is acceptable;
- mock tool execution is acceptable;
- file-backed evidence is acceptable;
- lightweight persistence is acceptable;
- no required Kubernetes;
- no required managed cloud services.

## 12. Cloud-Native-Capable Doctrine

Local-first must not prevent later cloud-native deployment.

This implies:

- clear ports and adapters;
- durable schemas;
- environment-based configuration;
- stateless API interface where practical;
- background worker boundary where needed;
- persistence abstractions that can later move from local to managed infrastructure.

## 13. MVP Architecture Constraints

MVP-A must remain the Proof Loop. It should not include the full Learning Loop unless explicitly marked as deferred.

MVP-A includes:

- Run creation;
- event recording;
- proposal submission;
- Tool Broker flow;
- policy check;
- allow/block/approval-gate disposition;
- evidence pack generation;
- timeline query.

MVP-B adds:

- memory retrieval;
- memory candidate proposal;
- memory admission;
- feedback;
- eval result;
- business outcome event.

## 14. Doctrine Violations

The following are doctrine violations unless explicitly scoped as future planning:

- direct model-to-tool execution;
- ungoverned memory writes;
- policy checks that are not persisted or evidenced;
- evidence generation as optional logging only;
- UI-first architecture;
- Kubernetes-first MVP;
- generic agent framework naming;
- full microservices before the vertical slice;
- model output described as authoritative decision;
- hidden tool execution outside the Tool Broker.

## 15. Done Means

WP-E0-003A is done when this doctrine:

- states the architectural identity of Aegis;
- anchors the core law;
- defines Clean Architecture layer responsibilities;
- preserves domain language;
- requires event-rich evidence;
- supports selective CQRS without overengineering;
- keeps MVP local-first and cloud-native-capable;
- identifies doctrine violations.
