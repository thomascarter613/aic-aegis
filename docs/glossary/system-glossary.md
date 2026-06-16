---
title: System Glossary
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Accepted
work_packet: WP-E0-002
source_bundle: ChatGPT Project Sources
last_updated: 2026-06-15
---

# System Glossary

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Purpose

This glossary defines the canonical language of AIC Aegis. It exists to prevent product and architecture drift.

Aegis terms are not generic labels. They describe boundaries, responsibilities, records, and controls required to enforce the core law:

**The model proposes; the platform disposes.**

## 2. Naming Rules

1. Use these terms consistently in documentation, schemas, APIs, events, code, ADRs, and work packets.
2. Do not replace Aegis vocabulary with generic agent-framework language unless explicitly mapping to an external concept.
3. Avoid vague names such as `agent_action`, `ai_decision`, `chat_result`, or `memory_write` when the precise Aegis term is known.
4. A model output that suggests an action is a **Proposal**, not a decision.
5. A tool action must pass through the **Tool Broker**.
6. A memory write starts as a **Memory Candidate** and must pass through the **Memory Admission Gate**.
7. Evidence must be attached to a **Run** or related governed record.

## 3. Canonical Terms

| Term | Definition |
|---|---|
| Actor | An entity that initiates, proposes, approves, executes, observes, or records work in Aegis. Actors may be humans, services, model adapters, workers, or system components. |
| Run | The bounded unit of governed AI work. A Run has identity, purpose, initiating Actor, events, proposals, policy checks, tool actions, evidence, and timeline records. |
| Run Event | A normalized record describing something that happened during a Run. Events are the backbone of the Run Timeline and Evidence Pack. |
| Timeline | The ordered reconstruction of a Run from events and related records. The Timeline exists so later reviewers can understand what happened. |
| Proposal | A model-originated or model-like suggestion for an action, text, memory write, workflow step, classification, or decision. A Proposal is not permission. |
| Disposition | The platform decision applied to a Proposal: allow, block, modify, mock, require approval, defer, reject, or record-only. |
| Tool Action | A proposed or executed interaction with an external capability such as sending a message, updating a CRM record, creating a task, retrieving data, or calling an API. |
| Tool Broker | The application boundary that receives Tool Action proposals and ensures schema validation, policy check, approval handling, execution/mocking, and evidence capture. |
| Policy Check | An explicit evaluation of a Proposal, Tool Action, Memory Candidate, or workflow step against defined controls and rules. |
| Control | A named safeguard or governance requirement used to reduce risk. Controls may be checked by policy, procedure, review, or evidence. |
| Risk | A potential failure mode or harm that Aegis must reduce, expose, or control. |
| Approval Gate | A platform boundary that routes high-risk or ambiguous proposals to human approval or configured authorization before execution. |
| Evidence Pack | A generated artifact or artifact set that preserves run-relevant facts, events, policy results, tool decisions, approvals, and outputs. |
| Evidence Artifact | A single evidence item such as a JSON event file, policy result, tool execution record, approval record, schema validation result, or timeline export. |
| Memory | Governed information available to future Runs. Memory is not merely stored context; it must have provenance and admission rules. |
| Memory Candidate | A proposed memory write generated from a Run, feedback, outcome, or human input. A candidate is not admitted memory until the Memory Admission Gate accepts it. |
| Memory Admission Gate | The boundary that decides whether a Memory Candidate becomes governed memory. |
| Feedback Event | A record of human, system, customer, or operator feedback about a Run, Proposal, output, tool action, or outcome. |
| Eval Result | A structured result from evaluating a Run, output, behavior, or control outcome against criteria. |
| Business Outcome Event | A record connecting governed AI work to an operational or business result. |
| Command | An application request that intends to change state. |
| Query | An application request that reads state without changing it. |
| Schema | A versioned contract for data crossing boundaries: API requests, events, policy inputs, evidence outputs, and persisted records. |
| Port | An application-defined interface required by a use case, implemented by adapters. |
| Adapter | Infrastructure implementation of a port, such as database, model, tool, evidence store, policy engine, or queue adapter. |
| Interface | An entry point into the system, such as HTTP API, CLI, worker, or local command. |
| Decision Record | A durable record of an architectural, product, governance, or implementation decision. |
| Trust Loop | The recurring cycle of proposal, disposition, evidence, feedback, evaluation, memory admission, and outcome learning. |

## 4. Term Relationships

### 4.1 MVP-A Proof Loop Terms

MVP-A primarily uses:

- Actor
- Run
- Run Event
- Proposal
- Tool Action
- Tool Broker
- Policy Check
- Approval Gate
- Evidence Pack
- Timeline

MVP-A proves that the platform can govern proposed tool execution and produce evidence.

### 4.2 MVP-B Learning Loop Terms

MVP-B adds:

- Memory
- Memory Candidate
- Memory Admission Gate
- Feedback Event
- Eval Result
- Business Outcome Event

MVP-B proves that Aegis can learn without allowing ungated memory mutation.

## 5. Anti-Terms

Avoid these terms unless quoting external systems:

| Avoid | Prefer | Reason |
|---|---|---|
| AI decision | Proposal or Disposition | The model does not decide; the platform disposes |
| Agent action | Tool Action Proposal | Makes governance boundary explicit |
| Chat history | Run Timeline or Run Events | Aegis is not chat-centric |
| Memory write | Memory Candidate | Admission is governed |
| Audit log only | Evidence Pack | Evidence is product capability, not incidental logging |
| Workflow automation platform | Reliability Control Plane | Prevents category drift |

## 6. Schema Naming Guidance

Use stable nouns in schema names:

- `RunCreated`
- `RunEventRecorded`
- `ProposalSubmitted`
- `PolicyCheckCompleted`
- `ToolActionProposed`
- `ToolActionDispositioned`
- `ApprovalGateRequested`
- `EvidencePackGenerated`
- `MemoryCandidateProposed`
- `MemoryAdmissionCompleted`
- `FeedbackCaptured`
- `EvalResultRecorded`
- `BusinessOutcomeRecorded`

## 7. Done Means

WP-E0-002 is done when this glossary:

- defines the canonical Aegis terms;
- distinguishes model proposals from platform decisions;
- preserves the Tool Broker and Memory Admission Gate boundaries;
- supports MVP-A and MVP-B without mixing them;
- provides naming guidance for future schemas, APIs, and code.
