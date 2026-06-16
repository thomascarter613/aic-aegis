---
title: Control Catalog
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Accepted
work_packet: WP-E0-003A
source_bundle: ChatGPT Project Sources
last_updated: 2026-06-15
---

# Control Catalog

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Purpose

The control catalog defines named controls for Aegis governance. Controls are used by policy checks, evidence packs, risk review, and future acceptance tests.

The catalog is intentionally small for the early work packets. It should grow from real governed workflows, not speculative enterprise breadth.

## 2. Control Catalog

| ID | Control | Description | Phase | Status |
|---|---|---|---|---|
|CTRL-001|Proposal Capture|Every model-originated action proposal is recorded before disposition.|MVP-A|Required|
|CTRL-002|Tool Broker Enforcement|Tool actions cannot execute outside the Tool Broker.|MVP-A|Required|
|CTRL-003|Policy Check Before Effect|External effects require a policy check result.|MVP-A|Required|
|CTRL-004|Risk-Based Disposition|Risk level influences allow/block/mock/approval decision.|MVP-A|Required|
|CTRL-005|Approval Gate|High-risk proposals can be routed for approval before execution.|MVP-A|Required|
|CTRL-006|Evidence Pack Generation|Run evidence can be generated and inspected.|MVP-A|Required|
|CTRL-007|Timeline Reconstruction|Run timeline can be reconstructed from events and related records.|MVP-A|Required|
|CTRL-008|Schema Validation|Boundary inputs and outputs are validated against versioned schemas.|MVP-A|Required|
|CTRL-009|Actor Attribution|Runs, proposals, approvals, and tool actions identify the responsible Actor.|MVP-A|Required|
|CTRL-010|Mock-Safe Execution|MVP can demonstrate safe execution without real external side effects.|MVP-A|Required|
|CTRL-011|Memory Admission|New memory must pass through Memory Admission Gate.|MVP-B|Required|
|CTRL-012|Feedback Capture|Feedback is recorded as a first-class event.|MVP-B|Required|
|CTRL-013|Eval Result Recording|Eval results are structured and tied to Runs or outputs.|MVP-B|Required|
|CTRL-014|Business Outcome Recording|Business outcomes are recorded separately from model assertions.|MVP-B|Required|

## 3. MVP-A Control Minimum

MVP-A must implement or simulate enough of these controls to prove the proof loop:

- CTRL-001 Proposal Capture
- CTRL-002 Tool Broker Enforcement
- CTRL-003 Policy Check Before Effect
- CTRL-004 Risk-Based Disposition
- CTRL-005 Approval Gate
- CTRL-006 Evidence Pack Generation
- CTRL-007 Timeline Reconstruction
- CTRL-008 Schema Validation
- CTRL-009 Actor Attribution
- CTRL-010 Mock-Safe Execution

## 4. MVP-B Control Minimum

MVP-B must add:

- CTRL-011 Memory Admission
- CTRL-012 Feedback Capture
- CTRL-013 Eval Result Recording
- CTRL-014 Business Outcome Recording

## 5. Control Evidence Expectations

Each implemented control should produce evidence.

Examples:

- CTRL-001 produces Proposal record;
- CTRL-002 produces Tool Broker decision record;
- CTRL-003 produces Policy Check result;
- CTRL-005 produces Approval Request and decision;
- CTRL-006 produces Evidence Pack manifest;
- CTRL-007 produces Timeline response;
- CTRL-011 produces Memory Admission result.

## 6. Out of Scope Controls

Deferred controls include:

- enterprise SSO enforcement;
- billing controls;
- formal compliance mappings;
- customer data residency controls;
- marketplace/plugin trust controls;
- full data retention and legal hold;
- multi-tenant isolation controls.

## 7. Done Means

The control catalog is done when it:

- names the minimum controls;
- maps controls to MVP-A and MVP-B;
- identifies required evidence expectations;
- avoids premature enterprise compliance claims.
