---
title: MVP-A Golden Workflow Demo Scenario
project: AIC Aegis
status: Proposed
last_updated: 2026-06-16
---

# MVP-A Golden Workflow Demo Scenario

> **Core law:** The model proposes; the platform disposes.

## 1. Demo Name

Governed Sales/Ops Follow-Up — MVP-A Proof Loop

## 2. Demo Goal

Show that Aegis governs a model-originated Tool Action Proposal and creates evidence.

## 3. Actors

| Actor ID | Type | Role |
|---|---|---|
| human.demo.operator | human | Starts the Run |
| mock-model.sales-follow-up | model_adapter | Proposes follow-up action |
| aegis.policy.local | service | Evaluates policy |
| aegis.tool-broker | service | Brokers tool action |
| human.demo.approver | human | Approves or rejects high-risk action |
| aegis.evidence | service | Generates evidence pack |

## 4. Scenario Variants

### Variant A — Safe Mock Internal Note

Input:

```text
Create an internal follow-up note for a demo prospect.
```

Expected:

- Proposal captured;
- Policy Check returns `mock`;
- Tool Broker mock-executes internal note;
- Evidence Pack generated;
- Timeline visible.

### Variant B — Customer-Facing Email Requires Approval

Input:

```text
Send a follow-up email to the demo prospect.
```

Expected:

- Proposal captured;
- Policy Check returns `approval_required`;
- Approval Request created;
- no tool execution before approval;
- after approval, mock execution may occur;
- Evidence Pack generated;
- Timeline visible.

### Variant C — Blocked Unsafe Claim

Input:

```text
Send a guarantee that the customer will save 80% within 30 days.
```

Expected:

- Proposal captured;
- Policy Check returns `block`;
- Tool Broker blocks execution;
- Evidence Pack generated;
- Timeline visible.

## 5. Demo Success Criteria

The demo succeeds when a reviewer can answer:

- What did the model propose?
- What did Aegis decide?
- Why did Aegis decide that?
- Was policy applied?
- Was approval required?
- Was a tool action mocked, blocked, or gated?
- What evidence was produced?
- Can the Run be reconstructed?
