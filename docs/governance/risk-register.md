---
title: Risk Register
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Accepted
work_packet: WP-E0-003A
source_bundle: ChatGPT Project Sources
last_updated: 2026-06-15
---

# Risk Register

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Purpose

The risk register identifies early product and architecture risks for AIC Aegis. It is not a compliance claim. It is an engineering and governance tool.

## 2. Risk Register

| ID | Risk | Description | Severity | Mitigation |
|---|---|---|---|---|
|RISK-001|Direct tool execution|Model or adapter executes tool without Tool Broker.|High|Tool Broker mandatory; architecture fitness check.|
|RISK-002|Policy bypass|Proposal proceeds without policy check.|High|Require Policy Check before external effect.|
|RISK-003|Evidence gaps|Run cannot be explained after completion.|High|Generate Evidence Pack and Timeline.|
|RISK-004|Ungoverned memory|Bad or sensitive facts are written to memory.|High|Defer to MVP-B; require Memory Admission Gate.|
|RISK-005|Premature microservices|System becomes too broad before proof loop works.|Medium|Local-first modular monolith or simple services.|
|RISK-006|UI-first drift|UI shapes core model and bypasses APIs.|Medium|Headless/API-first doctrine.|
|RISK-007|Generic agent drift|Aegis becomes a generic agent framework.|High|Preserve control-plane vocabulary.|
|RISK-008|Weak schema boundaries|Events and records become inconsistent.|Medium|Version schemas and validate boundaries.|
|RISK-009|Approval ambiguity|High-risk work lacks clear approval semantics.|Medium|Approval Gate records approver/status/rationale.|
|RISK-010|Outcome overclaiming|Model claims success without business evidence.|Medium|Business Outcome Events separate from model output.|

## 3. MVP-A Critical Risks

MVP-A must especially reduce:

- RISK-001 Direct tool execution;
- RISK-002 Policy bypass;
- RISK-003 Evidence gaps;
- RISK-005 Premature microservices;
- RISK-007 Generic agent drift;
- RISK-008 Weak schema boundaries;
- RISK-009 Approval ambiguity.

## 4. MVP-B Critical Risks

MVP-B must especially reduce:

- RISK-004 Ungoverned memory;
- RISK-010 Outcome overclaiming;
- feedback/eval records that are too vague to support learning.

## 5. Risk Handling Rules

1. High risks require explicit controls.
2. Any design that increases a high risk must be reviewed.
3. Risks should be attached to policy checks and evidence where possible.
4. Deferred risks must remain visible rather than silently ignored.

## 6. Done Means

The risk register is done when it:

- identifies early high-value risks;
- maps risks to MVP controls;
- avoids premature formal compliance language;
- supports work-packet and ADR review.
