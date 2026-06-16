---
title: Architecture Fitness Functions
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Accepted
work_packet: WP-E0-003A
source_bundle: ChatGPT Project Sources
last_updated: 2026-06-15
---

# Architecture Fitness Functions

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Purpose

Architecture fitness functions are objective checks that help preserve Aegis doctrine as the system evolves.

They turn doctrine into reviewable criteria.

## 2. Fitness Functions

| ID | Name | Requirement | Verification |
|---|---|---|---|
|FF-001|Core law visible|Architecture/docs must state that the model proposes and platform disposes.|Documentation review|
|FF-002|No direct model-to-tool execution|Tool execution must pass through Tool Broker.|Static architecture review / tests|
|FF-003|Proposal before disposition|Tool action cannot be dispositioned without Proposal record.|Use-case test|
|FF-004|Policy before external effect|External effect requires policy result unless explicitly mocked/blocked.|Use-case test|
|FF-005|Evidence pack generated|MVP-A happy path generates Evidence Pack manifest.|Integration test|
|FF-006|Timeline reconstructable|Run Timeline can reconstruct proposal, policy, disposition, and tool result.|Integration test|
|FF-007|Domain independence|Domain layer has no framework/database/model SDK dependency.|Static dependency check|
|FF-008|API-first|Core capability exposed through API/command boundary, not UI-only behavior.|Architecture review|
|FF-009|MVP-A/MVP-B separation|Memory/eval/outcome capabilities are not required to complete MVP-A.|Work-packet review|
|FF-010|Local-first setup|MVP can run without managed cloud infrastructure.|Setup test|

## 3. MVP-A Required Fitness Set

MVP-A must satisfy:

- FF-001 Core law visible
- FF-002 No direct model-to-tool execution
- FF-003 Proposal before disposition
- FF-004 Policy before external effect
- FF-005 Evidence pack generated
- FF-006 Timeline reconstructable
- FF-007 Domain independence
- FF-010 Local-first setup

## 4. MVP-B Additional Fitness Set

MVP-B adds:

- memory candidates are not admitted without the Memory Admission Gate;
- feedback events are separate records;
- eval results are structured records;
- business outcomes are not inferred from model claims alone.

## 5. Future Fitness Functions

Future work may add:

- schema compatibility checks;
- event versioning checks;
- evidence artifact completeness checks;
- risk-control coverage checks;
- approval SLA checks;
- policy decision explainability checks;
- adapter contract tests.

## 6. Failure Handling

A failed fitness function should produce one of:

1. code or documentation correction;
2. explicit ADR changing the rule;
3. work packet deferral;
4. rejection of the proposed change.

Silent failure is not acceptable.

## 7. Done Means

This document is done when it:

- translates doctrine into testable checks;
- identifies required MVP-A fitness functions;
- identifies MVP-B additions;
- creates a basis for later CI and review gates.
