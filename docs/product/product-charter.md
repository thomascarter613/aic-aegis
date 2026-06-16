---
title: Product Charter
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Accepted
work_packet: WP-E0-001
source_bundle: ChatGPT Project Sources
last_updated: 2026-06-15
---

# Product Charter

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Purpose

This document defines the product charter for **AIC Aegis**, the AIC AI Reliability Control Plane.

Aegis exists to make AI work provable. It is not a chatbot, agent framework, workflow builder, prompt library, observability dashboard, or governance checklist. It is a headless control plane that governs AI runs through identity, runtime events, model proposals, policy checks, brokered tool execution, approval gates, governed memory, evidence packs, evals, feedback, and business outcome records.

The product charter establishes the stable product intent that later architecture, work packets, ADRs, APIs, schemas, and implementation tasks must preserve.

## 2. Product Identity

| Field | Value |
|---|---|
| Codename | Aegis |
| Product name | AIC AI Reliability Control Plane |
| Short name | AIC Aegis |
| Repository | https://github.com/thomascarter613/aic-aegis |
| Product category | AI reliability control plane |
| Initial deployment posture | Local-first |
| External posture | Headless, API-first |
| Initial workflow | Governed Sales/Ops Follow-Up |
| Initial MVP strategy | Thin vertical slice through the trust loop |

## 3. Product Thesis

Organizations will not be able to responsibly scale AI work if model activity remains opaque, ungoverned, unauditable, and disconnected from business outcomes.

Aegis turns AI work into governed work by forcing every important action through explicit platform boundaries:

1. a Run is created;
2. an Actor is identified;
3. runtime events are recorded;
4. model output is represented as a Proposal;
5. policy evaluates the Proposal;
6. a Tool Broker mediates external effects;
7. approval gates handle risky work;
8. evidence artifacts are captured;
9. the Run Timeline explains what happened;
10. feedback, evals, memory, and outcomes improve future work.

Aegis does not attempt to make the model inherently trustworthy. Aegis treats the model as an untrusted proposer and makes the platform responsible for disposition.

## 4. Core Law

**The model proposes; the platform disposes.**

### 4.1 Meaning

Models may propose actions, text, tool calls, memory writes, workflow steps, classifications, recommendations, and decisions. Aegis decides whether those proposals are allowed, blocked, modified, routed for approval, logged, evaluated, admitted into memory, attached to evidence, or converted into business outcomes.

### 4.2 Product Implications

Aegis must never allow model output to become an external side effect without passing through platform controls. This implies:

- model output is not equivalent to permission;
- proposal capture is mandatory;
- policy checks are first-class records;
- tool execution is brokered;
- approval gates are explicit;
- evidence is generated as a product capability, not a logging afterthought;
- timelines are queryable;
- memory admission is governed;
- feedback and outcomes are recorded separately from model claims.

## 5. Target Users

### 5.1 Initial Builder User

The first user is a builder or operator implementing the MVP locally. This user needs:

- simple local setup;
- API-first interaction;
- deterministic mock model behavior;
- inspectable runtime records;
- visible run timeline;
- evidence pack generation.

### 5.2 Future Internal Platform User

A future internal platform team needs Aegis to:

- enforce policy over AI workflows;
- centralize runtime evidence;
- manage high-risk proposals;
- connect AI work to controls and risks;
- evaluate whether AI outputs are improving.

### 5.3 Future Governance User

A future governance, security, risk, compliance, or operations stakeholder needs Aegis to:

- ask what happened during an AI run;
- see who or what initiated work;
- inspect model proposals and platform decisions;
- understand which controls were applied;
- inspect evidence packs;
- review blocked or approval-gated actions;
- trace work to feedback and outcomes.

## 6. Initial Problem Statement

AI-assisted work creates operational risk when organizations cannot answer:

- What did the model propose?
- What did the platform allow?
- What did the platform block?
- Which policy was applied?
- Was approval required?
- Was a tool actually executed?
- What evidence exists?
- What memory was used or proposed?
- Was feedback captured?
- Did the work produce a business outcome?
- Can the full timeline be reconstructed?

Aegis exists to make these answers native to the platform.

## 7. Initial Product Scope

### 7.1 MVP-A: Proof Loop

MVP-A proves that Aegis can govern a single AI-assisted workflow end-to-end.

MVP-A includes:

- create Run;
- record Run Events;
- mock model proposes Tool Action;
- Tool Broker receives Proposal;
- policy checks Tool Action;
- safe action proceeds or is mocked;
- high-risk action is blocked or approval-gated;
- Evidence Pack is generated;
- Run Timeline is visible.

### 7.2 MVP-B: Learning Loop

MVP-B extends the proof loop into governed learning.

MVP-B includes:

- governed memory retrieval;
- memory candidate proposal;
- Memory Admission Gate;
- feedback capture;
- basic Eval Result;
- Business Outcome Event.

### 7.3 Golden Workflow

The initial golden workflow is **Governed Sales/Ops Follow-Up**.

This workflow is intentionally narrow. It gives Aegis enough real-world shape to prove governed AI work without expanding into a broad workflow platform.

## 8. Non-Goals

Aegis is not, in the MVP:

- a general chatbot application;
- a general-purpose autonomous agent framework;
- a visual workflow builder;
- a prompt management product;
- a broad observability dashboard;
- a compliance certification product;
- an enterprise connector marketplace;
- a multi-agent swarm runtime;
- a fine-tuning platform;
- a Kubernetes-first platform;
- a billing platform;
- an enterprise SSO platform;
- a replacement for business applications.

## 9. Differentiation

Aegis differentiates by treating AI reliability as a control-plane problem.

| Generic AI App Behavior | Aegis Behavior |
|---|---|
| Model responds | Model proposes |
| Tool call executes directly | Tool Broker mediates |
| Logs are incidental | Evidence is first-class |
| Memory is written freely | Memory Admission Gate decides |
| Policy is advisory | Policy Check disposes proposals |
| Approval is external | Approval Gate is part of run semantics |
| Outcomes are assumed | Business Outcome Events are recorded |
| Trust is asserted | Trust is earned through evidence |

## 10. Product Principles

### 10.1 Evidence First

Aegis must produce evidence as a normal result of governed AI work.

### 10.2 Headless First

APIs, schemas, events, and evidence artifacts are primary. UI is optional and later.

### 10.3 Local First

The MVP must run locally without requiring cloud infrastructure.

### 10.4 Cloud-Native Capable

Local-first must not create architectural dead ends that prevent later cloud-native deployment.

### 10.5 Policy Enforced

Policy checks must be explicit, inspectable, and attached to run evidence.

### 10.6 Domain Driven

Aegis terms must remain stable and meaningful: Run, Actor, Proposal, Tool Action, Policy Check, Tool Broker, Approval Gate, Evidence Pack, Memory Candidate, Memory Admission Gate, Eval Result, Feedback Event, Business Outcome Event, Timeline, Control, Risk, Decision Record.

### 10.7 Thin Slice First

The MVP proves a coherent trust loop before expanding breadth.

## 11. Success Criteria

Aegis succeeds at the product-charter level when a user can demonstrate:

1. a Run was created;
2. a model/mock model proposed an action;
3. the platform evaluated the proposal;
4. the proposal was allowed, blocked, or approval-gated;
5. a tool action did not bypass the Tool Broker;
6. evidence was generated;
7. the timeline explains what happened;
8. the result can be inspected through APIs or local artifacts.

## 12. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Dilution into generic agent framework | Loss of product clarity | Preserve core law and control-plane vocabulary |
| Premature platform breadth | MVP never lands | Thin vertical slice only |
| Weak evidence model | Trust claims become unverifiable | Make evidence packs part of MVP-A |
| Tool execution bypasses policy | Core law violated | Tool Broker is mandatory |
| Memory becomes ungoverned | Bad facts accumulate | Defer memory to MVP-B and gate admission |
| UI dominates early design | Headless doctrine weakens | APIs and artifacts first |

## 13. Done Means

WP-E0-001 is done when this charter:

- states the product identity;
- states the core law;
- defines Aegis as a reliability control plane;
- distinguishes Aegis from generic AI apps;
- defines MVP-A and MVP-B at a product level;
- identifies golden workflow;
- establishes product principles;
- names non-goals;
- provides success criteria for later work packets.

## 14. Relationship to Later Work

This charter constrains:

- WP-E0-002 System Glossary;
- WP-E0-003A Architecture Doctrine Pack;
- WP-E0-003 Architecture Overview;
- WP-E0-004 MVP System Boundaries;
- WP-E0-005 Initial ADR Pack.

Any later decision that contradicts this charter must be captured as a Decision Record and explicitly justified.
