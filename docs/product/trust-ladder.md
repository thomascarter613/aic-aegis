---
title: Trust Ladder
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Accepted
work_packet: WP-E0-003A
source_bundle: ChatGPT Project Sources
last_updated: 2026-06-15
---

# Trust Ladder

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Purpose

The trust ladder describes how Aegis earns trust progressively. Aegis does not claim trust because a model is advanced. Aegis earns trust by governing work and producing evidence.

## 2. Trust Ladder Levels

| Level | Name | Meaning | Aegis Capability |
|---|---|---|---|
| 0 | Ungoverned AI Output | Model output exists with no platform control. | Out of scope as acceptable Aegis behavior |
| 1 | Recorded Proposal | Model output is captured as a Proposal. | Proposal records |
| 2 | Policy-Checked Proposal | Proposal is evaluated against policy/controls. | Policy Check |
| 3 | Brokered Action | Tool action is mediated by Tool Broker. | Tool Broker |
| 4 | Approval-Gated Risk | Risky proposals are blocked or routed for approval. | Approval Gate |
| 5 | Evidence-Backed Run | Run can be inspected through Evidence Pack and Timeline. | Evidence Service and Timeline |
| 6 | Governed Learning | Memory, feedback, evals, and outcomes are governed. | MVP-B Learning Loop |
| 7 | Operational Reliability | Controls, evidence, and outcomes improve repeated work. | Future maturity |

## 3. MVP-A Trust Target

MVP-A should reach Level 5:

**Evidence-Backed Run**

A user should be able to inspect a Run and understand:

- what was proposed;
- what policy decided;
- what disposition occurred;
- whether a tool was executed or mocked;
- whether approval was required;
- what evidence exists;
- how the Timeline reconstructs the work.

## 4. MVP-B Trust Target

MVP-B should reach Level 6:

**Governed Learning**

A user should be able to inspect:

- what memory was retrieved;
- what Memory Candidate was proposed;
- why memory was admitted or rejected;
- what feedback was captured;
- what eval result was recorded;
- what business outcome event was recorded.

## 5. Trust Anti-Patterns

Aegis must avoid:

- claiming model confidence as operational trust;
- equating logs with evidence;
- allowing direct tool execution;
- writing memory without admission;
- using hidden prompts as governance;
- presenting a UI dashboard without control-plane records;
- inferring business success from generated text.

## 6. Trust Evidence

Trust requires evidence such as:

- Run records;
- Proposal records;
- Policy Check results;
- Tool Broker decisions;
- Approval Gate records;
- tool execution/mock records;
- Evidence Pack manifests;
- Timeline exports;
- Memory Admission results;
- Feedback Events;
- Eval Results;
- Business Outcome Events.

## 7. Done Means

The trust ladder is done when it:

- defines progressive trust levels;
- maps MVP-A to evidence-backed runs;
- maps MVP-B to governed learning;
- prevents model-confidence trust claims;
- supports product messaging and architecture review.
