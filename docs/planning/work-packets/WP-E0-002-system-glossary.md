# WP-E0-002 — System Glossary

Status: proposed  
Codename: Aegis  
Product name: AIC AI Reliability Control Plane  
Short name: AIC Aegis  
Company: Applied Innovation Corp  
Owner: Thomas Carter  
Document type: System glossary  
Work packet: WP-E0-002  
Parent epic: E0 — Product Charter & Architecture  
Last updated: 2026-06-15  

---

## 1. Purpose

This glossary defines the canonical language for AIC Aegis.

Aegis is an AI Reliability Control Plane. Its work spans agents, runs, tools, memory, policy, evidence, evals, feedback, and business outcomes. Without consistent language, implementation work will fragment quickly.

This document exists so that:

1. docs use the same terms,
2. schemas use the same names,
3. GitHub issues use the same nouns,
4. services have clear ownership,
5. logs and events are understandable,
6. evidence packs are readable,
7. agents, humans, and future coding agents share a stable vocabulary.

---

## 2. Naming Rules

### 2.1 Canonical nouns

Aegis should prefer stable domain nouns over implementation-specific names.

Use:

- `Run`, not “session” or “conversation execution”
- `Run Event`, not “log line”
- `Evidence Pack`, not “audit log”
- `Memory Candidate`, not “thing to remember”
- `Tool Broker`, not “tool caller”
- `Policy Decision`, not “guardrail result”
- `Business Outcome`, not “success metric” when referring to a stored outcome object

### 2.2 Avoid overloaded words

Avoid using these loosely:

| Avoid loose use | Prefer |
|---|---|
| session | thread, run, or conversation depending on meaning |
| memory | memory record, retrieved memory, memory candidate, or working memory |
| log | run event, trace event, audit event, or evidence entry |
| guardrail | policy, policy check, policy decision, or validation |
| agent | agent definition, agent instance, runtime actor, or workflow |
| tool | tool definition, tool proposal, tool call, or tool result |
| feedback | user feedback, human review, correction, eval result, or outcome |

### 2.3 Required identifiers

Most major objects should carry these identifiers when applicable:

- `tenant_id`
- `user_id`
- `agent_id`
- `run_id`
- `trace_id`
- `evidence_pack_id`
- `policy_decision_id`
- `tool_call_id`
- `memory_id`
- `eval_result_id`
- `business_outcome_id`

### 2.4 Product-level language

Use:

> Aegis is an AI Reliability Control Plane.

Avoid reducing Aegis to:

- chatbot,
- agent framework,
- RAG app,
- observability tool,
- eval tool,
- workflow builder,
- policy dashboard.

Aegis may contain pieces of those, but its product category is broader.

---

## 3. Product Terms

### Aegis

The codename and short product name for the AIC AI Reliability Control Plane.

Aegis is the reliability layer around AI workflows. It governs memory, tools, policy, evals, evidence, feedback, and business outcomes.

### AIC AI Reliability Control Plane

The formal product name for Aegis.

It is the platform layer that makes AI systems governable, observable, correctable, auditable, and outcome-driven.

### AI Reliability Control Plane

The product category.

A software layer that sits between AI systems and business systems to govern execution, memory, tool use, policy, evaluation, evidence, feedback, and outcomes.

### Reliability Layer

A less formal phrase for the same concept as AI Reliability Control Plane.

Use this phrase in positioning and marketing when “control plane” feels too technical.

### AgentOps Kernel

The MVP runtime kernel inside Aegis.

The AgentOps Kernel is the minimum platform capability that can create a run, apply policy, retrieve memory, broker tool calls, generate evidence, evaluate the output, collect feedback, and record business outcomes.

### Governed AI Workflow

An AI workflow executed under Aegis controls.

A governed workflow has run identity, traceability, policy checks, memory controls, tool governance, evidence, evaluation, and outcome tracking.

### Ungoverned AI Workflow

An AI workflow that acts without sufficient controls.

Examples:

- model calls with no run record,
- tool calls without broker approval,
- memory writes without admission,
- outputs without evidence,
- production changes without policy checks.

### MVP Wedge

The first narrow product proof.

For Aegis, the MVP wedge is a governed Sales/Ops Assistant that demonstrates the complete reliability loop.

### Sales/Ops Assistant

The first canonical Aegis workflow.

It analyzes customer conversations, retrieves allowed memory, proposes follow-up actions, drafts safe messages, blocks or escalates risky actions, generates evidence, runs evals, collects feedback, and records business outcomes.

---

## 4. Actor Terms

### Tenant

A business, organization, workspace, or deployment boundary using Aegis.

The tenant is the highest-level data isolation boundary in the product.

### User

A human who interacts with Aegis.

A user can submit tasks, review outputs, approve actions, correct memory, give feedback, inspect evidence, or manage workflows.

### Actor

Any entity that initiates or performs an action.

Actors can be:

- human users,
- agents,
- services,
- automation jobs,
- system processes.

### Agent

A configured AI actor that performs tasks.

An agent may have:

- instructions,
- tools,
- memory access rules,
- policy context,
- eval requirements,
- workflow role.

In Aegis, an agent does not directly own final authority. The agent proposes. The platform disposes.

### Agent Definition

The durable configuration of an agent.

It includes the agent’s name, role, purpose, model configuration, allowed tools, memory scope, policies, and output expectations.

### Agent Version

A versioned snapshot of an Agent Definition.

Agent versions matter because evals, evidence, and business outcomes should be attributable to the specific configuration used.

### Runtime Actor

The effective actor executing inside a run.

For example, the runtime actor may be a specific agent version acting on behalf of a user in a tenant.

### Human Reviewer

A user responsible for reviewing AI output, memory candidates, policy exceptions, eval failures, or high-risk tool actions.

### Approver

A human or authorized system role that can approve an action.

Approvers are especially important for high-risk tool calls, sensitive memory writes, policy overrides, and final output release.

### Operator

A human responsible for running and improving AI workflows.

In AIC’s business context, operators may include founders, technical operators, implementation consultants, AI workflow owners, and internal automation owners.

---

## 5. Runtime Terms

### Run

A single bounded execution of an AI workflow.

A run begins when Aegis accepts a task and creates a run envelope. A run ends when the workflow completes, fails, is cancelled, or is deferred.

A run is not necessarily the same as a conversation. A conversation may contain many runs.

### Run Envelope

The canonical object that identifies and bounds a run.

A Run Envelope includes:

- `run_id`,
- `tenant_id`,
- `user_id`,
- `agent_id`,
- `agent_version`,
- `task_type`,
- `status`,
- `trace_id`,
- `evidence_pack_id`,
- `input_refs`,
- `policy_context`,
- `memory_context`,
- timestamps.

### Run State

The current lifecycle state of a run.

Initial MVP states:

- `created`,
- `running`,
- `waiting_for_approval`,
- `completed`,
- `failed`,
- `cancelled`.

### Run State Machine

The allowed transitions between run states.

Example:

```text
created -> running -> waiting_for_approval -> running -> completed
created -> running -> failed
created -> cancelled
```

### Run Event

A structured event recorded during a run.

Run Events are not loose logs. They are domain events that explain what happened.

Examples:

- `run.created`,
- `memory.retrieved`,
- `policy.checked`,
- `model.called`,
- `tool.proposed`,
- `tool.allowed`,
- `tool.denied`,
- `approval.requested`,
- `evidence.generated`,
- `eval.completed`,
- `feedback.received`,
- `outcome.recorded`.

### Event Taxonomy

The canonical list of event names and event payload classes used by Aegis.

The event taxonomy prevents inconsistent event names.

### Trace

The distributed execution trace associated with a run.

A trace links spans and events across services, model calls, policy checks, memory retrieval, tool execution, evidence generation, and evals.

### Trace ID

The identifier used to correlate runtime activity across services and telemetry systems.

Every meaningful action inside a run should carry the `trace_id`.

### Span

A timed unit of work inside a trace.

Examples:

- memory retrieval span,
- policy check span,
- model call span,
- tool broker span,
- eval runner span.

### Runtime

The system component responsible for orchestrating an AI run.

The runtime creates the run envelope, coordinates memory retrieval, calls models, routes tool proposals, records events, requests evidence, and manages lifecycle.

### Runtime Service

The service or module implementing runtime responsibilities.

In the MVP, this may be a dedicated service or a module inside a monolithic local app. The logical boundary matters more than physical deployment early on.

### Task

The work requested by a user or system.

Examples:

- analyze customer conversation,
- draft follow-up email,
- summarize support ticket,
- propose CRM update,
- evaluate prior run.

### Task Type

A canonical category for a task.

Examples:

- `customer_follow_up`,
- `support_triage`,
- `memory_review`,
- `evidence_generation`,
- `policy_review`.

### Input Reference

A reference to input used by a run.

An input reference should point to stored content, uploaded files, conversation messages, CRM records, tickets, or other source objects. Evidence packs should refer to input references rather than copying sensitive content unnecessarily.

### Output

A result produced by an agent or workflow.

Outputs can include text, structured JSON, tool proposals, draft artifacts, summaries, decisions, recommendations, or generated evidence.

### Output Reference

A reference to a stored output.

Evidence packs should link outputs through output refs.

---

## 6. Model Terms

### Model

The AI model used for reasoning, generation, classification, evaluation, or transformation.

Aegis should be provider-agnostic.

### Model Provider

The vendor, local runtime, or system that serves a model.

Examples:

- hosted model provider,
- local model server,
- mock provider,
- internal provider.

### Mock Model Provider

A local deterministic provider used for development and tests.

The MVP should support mock model mode so the platform can be developed without paid APIs.

### Model Call

A single invocation of a model.

A Model Call should record:

- provider,
- model,
- input reference,
- output reference,
- token usage if available,
- latency,
- cost if available,
- run ID,
- trace ID,
- status,
- error if any.

### Model Call Record

The persisted metadata about a Model Call.

The record should support evidence generation, debugging, evals, and cost tracking.

### Prompt

The instruction and context sent to a model.

In Aegis, prompts should be assembled under policy and should include only allowed context.

### Prompt Pack

A reusable collection of prompts, prompt fragments, instructions, rubrics, and examples.

Prompt packs should eventually be versioned and evaluated.

### Prompt Assembly

The process of building the final model input.

Prompt assembly may use:

- user task,
- system instructions,
- retrieved memory,
- retrieved documents,
- tool definitions,
- policies,
- output schema,
- prior run state.

### Structured Output

Model output constrained to a schema.

Structured output is preferred when the runtime needs to route tool proposals, eval results, memory candidates, or policy-relevant decisions.

### Tool Proposal

A model-generated suggestion to call a tool.

Tool Proposals are not Tool Calls yet. They must pass through the Tool Broker.

---

## 7. Memory Terms

### Memory

A governed record that the system may use to improve future behavior.

Memory is not simply anything stored in a vector database. Aegis memory must have source, scope, confidence, sensitivity, lifecycle, and correction path.

### Memory Record

A persisted memory object.

A Memory Record may represent a fact, preference, procedure, past event, or learned lesson.

### Working Memory

Temporary state used during the current task or run.

Working memory is not necessarily durable.

### Episodic Memory

Memory of what happened.

Examples:

- a customer asked for a Friday follow-up,
- an agent sent a draft to review,
- a policy denied a send action.

### Semantic Memory

Durable factual memory.

Examples:

- customer prefers weekly summaries,
- account owner is Jane,
- product X has a standard onboarding timeline.

### Procedural Memory

Memory about how work should be done.

Examples:

- always verify PO number before invoice follow-up,
- for customer escalations, draft but do not send without approval.

### Evaluative Memory

Memory about what worked or failed.

Examples:

- this prompt caused vague summaries,
- this workflow failed because it retrieved stale account data,
- this tool schema prevented invalid CRM updates.

### Memory Candidate

A proposed memory that has not yet been admitted.

Memory Candidates may be generated from user statements, feedback, run outputs, corrections, eval failures, or tool results.

### Memory Admission Gate

The component or process that decides whether a Memory Candidate becomes a Memory Record.

Possible decisions:

- accept,
- reject,
- queue for review,
- merge,
- supersede,
- store temporarily,
- expire.

### Memory Admission Decision

The result of evaluating a Memory Candidate.

It should include:

- decision,
- reason,
- policy decision reference,
- reviewer if applicable,
- timestamp.

### Memory Scope

The boundary where a memory applies.

Examples:

- tenant-wide,
- user-specific,
- customer-specific,
- agent-specific,
- workflow-specific,
- project-specific.

### Memory Subject

The entity that a memory is about.

Examples:

- user,
- customer,
- company,
- project,
- workflow,
- agent.

### Memory Source

The origin of a memory.

Examples:

- conversation message,
- user feedback,
- uploaded file,
- CRM record,
- support ticket,
- eval failure,
- human correction.

### Memory Provenance

The traceable origin and history of a memory.

Provenance includes source, source reference, creator, confidence, timestamps, prior versions, and supersession links.

### Memory Confidence

A score or rating indicating how reliable the memory is believed to be.

Confidence should influence admission, retrieval, and output use.

### Memory Sensitivity

The data classification of a memory.

Initial classes:

- public,
- internal,
- confidential,
- restricted.

### Memory Lifecycle

The lifecycle of a memory from proposal to admission, use, correction, supersession, expiration, or deletion.

### Memory Supersession

The process of replacing an older memory with a newer or corrected memory.

Supersession should preserve history.

### Memory Correction

A user or system action that corrects, invalidates, or updates memory.

### Memory Poisoning

The introduction of incorrect, malicious, unauthorized, or misleading information into memory.

Aegis must treat memory poisoning as a first-class risk.

### Retrieval

The process of finding relevant context or memory.

Retrieval must be scoped and policy-aware.

### Governed Retrieval

Retrieval that applies tenant, subject, sensitivity, policy, and relevance constraints before context reaches a model.

### Retrieved Memory

Memory selected for use in a run.

Evidence packs should list retrieved memory references.

### Vector Search

Similarity search over embeddings.

In Aegis, vector search is an access pattern, not the canonical source of truth.

### Embedding

A numerical representation used for semantic search.

Embeddings may be stored for Memory Records or documents, but the canonical record remains relational and auditable.

### pgvector

The initial semantic retrieval extension for PostgreSQL in the MVP.

### Qdrant

A possible optional retrieval accelerator later.

Qdrant should not replace PostgreSQL as the canonical memory source of truth unless a future ADR explicitly changes that decision.

---

## 8. Tool Terms

### Tool

A callable capability that lets an AI workflow interact with an external system, internal service, computation, or side-effecting operation.

Examples:

- read CRM contact,
- create email draft,
- search knowledge base,
- update ticket,
- generate evidence pack,
- propose memory candidate.

### Tool Definition

The registered definition of a tool.

A Tool Definition includes the tool manifest, input/output schemas, risk level, and execution metadata.

### Tool Manifest

A structured description of a tool.

A Tool Manifest includes:

- tool ID,
- name,
- description,
- risk level,
- side-effect status,
- approval requirement,
- input schema,
- output schema,
- allowed roles,
- allowed data classes,
- evidence requirement.

### Tool Registry

The catalog of available tools.

The registry lets agents and runtimes discover what tools exist, but discovery does not imply execution permission.

### Tool Broker

The component that controls tool execution.

The Tool Broker validates proposals, checks schemas, asks policy for a decision, handles approval requirements, executes allowed tools, blocks denied tools, records results, and emits evidence data.

### Tool Proposal

A proposed tool action generated by a model or workflow.

Tool Proposals must be validated and authorized before execution.

### Tool Call

An authorized or attempted execution of a tool.

A Tool Call should record:

- tool call ID,
- run ID,
- tool ID,
- input,
- output,
- status,
- policy decision,
- approval reference,
- timestamps.

### Tool Result

The output returned by a tool.

Tool Results may need filtering, redaction, validation, or transformation before being shown to a model or user.

### Tool Input Schema

The schema that defines valid tool input.

### Tool Output Schema

The schema that defines valid tool output.

### Tool Risk Class

The risk category of a tool.

Initial classes:

- `read_only`,
- `low_write`,
- `medium_write`,
- `high_write`,
- `critical`.

### Read-only Tool

A tool that retrieves information but does not mutate external systems.

Example:

- `crm.read_contact`.

### Low-write Tool

A tool that creates or changes low-risk, reversible artifacts.

Example:

- `email.create_draft`.

### Medium-write Tool

A tool that changes business records but is not inherently external or irreversible.

Example:

- `crm.update_contact`.

### High-write Tool

A tool that performs consequential or external actions.

Example:

- `email.send`.

### Critical Tool

A tool that performs destructive, regulated, financial, legal, medical, security-sensitive, or infrastructure-critical actions.

Critical tools should be blocked by default in the MVP.

### Side Effect

A change caused outside the model response itself.

Examples:

- creating a draft,
- sending an email,
- updating CRM,
- deleting a record,
- deploying code.

### Approval Hook

A mechanism that pauses execution until an authorized approver approves or denies an action.

### Capability Token

A scoped, temporary authorization granted by the platform to execute a specific capability.

The model should never directly own credentials.

### Tool Evidence

The evidence records associated with a tool proposal, decision, call, and result.

---

## 9. Policy & Safety Terms

### Policy

A rule or set of rules that determines whether an action is allowed, denied, transformed, escalated, or requires approval.

### Policy-as-Code

A policy implementation stored and versioned as executable code.

Aegis should use policy-as-code for runtime decisions.

### Policy Pack

A collection of policies for a specific area.

Examples:

- base tool policy pack,
- base memory policy pack,
- output release policy pack,
- tenant policy pack.

### Policy Check

The act of evaluating input against policy.

### Policy Checkpoint

A point in the runtime where policy must be checked.

Required checkpoints may include:

- before context retrieval,
- before prompt assembly,
- before model call,
- before tool call,
- before memory write,
- before output release,
- before business system mutation,
- before evidence export.

### Policy Decision

The recorded result of a policy check.

Decision types:

- allow,
- deny,
- require approval,
- sanitize,
- redact,
- escalate,
- defer.

### Allow

A policy decision that permits the action.

### Deny

A policy decision that blocks the action.

### Require Approval

A policy decision that pauses the action until an approver decides.

### Sanitize

A policy decision that permits use only after removing unsafe or unwanted content.

### Redact

A policy decision that removes sensitive information before release, storage, or model exposure.

### Escalate

A policy decision that routes the issue to a human or higher-authority process.

### Defer

A policy decision that postpones the action because information, approval, or context is missing.

### Policy Reason

The human-readable explanation for a Policy Decision.

Every policy decision should have a reason.

### Policy Version

The version of the policy that produced a decision.

Policy versioning is necessary for evidence, replay, debugging, and audits.

### Guardrail

A general safety mechanism.

In Aegis docs, prefer specific terms such as policy check, schema validation, approval gate, redaction, memory admission, or tool broker. Use “guardrail” only as a broad informal umbrella term.

### Approval Gate

A control that requires human or authorized approval before proceeding.

### Override

A deliberate decision to bypass or alter a default policy outcome.

Overrides must be recorded and justified.

### Data Classification

The classification of data sensitivity.

Initial classes:

- public,
- internal,
- confidential,
- restricted.

### Restricted Data

Data blocked by default unless there is an explicit grant and policy path.

### Prompt Injection

An attack or failure mode where input attempts to override or manipulate instructions, tools, policies, or data boundaries.

### Tool Injection

An attack or failure mode where data or model output attempts to manipulate tool calls or tool parameters unsafely.

### Data Exfiltration

Unauthorized disclosure or movement of data.

### Unsafe Output Handling

A failure mode where model output is trusted or executed without validation.

### Policy Bypass

Any attempt to avoid or defeat runtime policy controls.

---

## 10. Evidence & Audit Terms

### Evidence

Structured proof of what happened during an AI run.

Evidence is more than logs. It is curated, referential, inspectable, and tied to decisions and outcomes.

### Evidence Pack

The canonical audit artifact for a run.

An Evidence Pack links:

- run summary,
- input refs,
- memory refs,
- context refs,
- model call refs,
- tool call refs,
- policy decision refs,
- approval refs,
- output refs,
- eval result refs,
- business outcome refs,
- cost records,
- timestamps,
- errors.

### Evidence Pack ID

The identifier for an Evidence Pack.

### Evidence Generator

The component that builds evidence packs from run data.

### Evidence Renderer

The component that converts evidence data into human-readable formats, such as Markdown.

### Evidence Export

A machine-readable or human-readable export of evidence.

Examples:

- JSON evidence pack,
- Markdown evidence report,
- PDF evidence report later.

### Evidence Reference

A pointer from evidence to a related object.

Examples:

- memory reference,
- tool call reference,
- policy decision reference,
- eval result reference.

### Evidence Completeness

A measure of whether the Evidence Pack contains all required sections.

### Evidence Redaction

The removal or masking of sensitive content from evidence outputs.

### Audit Trail

The complete chain of records needed to understand an action.

An audit trail may include run events, policy decisions, tool calls, memory events, approvals, and evidence packs.

### Tamper Resistance

A strategy for making evidence difficult to alter without detection.

MVP may document the strategy before implementing cryptographic guarantees.

### Human-readable Evidence

Evidence formatted for people.

### Machine-readable Evidence

Evidence formatted for systems.

Aegis should support both.

---

## 11. Evaluation Terms

### Evaluation

The process of measuring whether an AI workflow performed well.

Evaluation can assess quality, safety, correctness, policy compliance, tool use, memory use, evidence completeness, cost, latency, or business outcome.

### Eval

Short form of Evaluation.

Acceptable in issue titles and technical docs, but define clearly.

### Eval Case

A single test case for evaluating an AI workflow.

An Eval Case includes:

- input,
- expected behavior,
- rubric,
- tags,
- risk category.

### Eval Dataset

A collection of Eval Cases.

### Eval Pack

A reusable package of eval datasets, rubrics, and configuration.

### Eval Run

A single execution of one or more Eval Cases.

### Eval Result

The result of an evaluation.

An Eval Result should include:

- score,
- pass/fail,
- evaluator,
- rubric,
- details,
- related run,
- timestamp.

### Rubric

A scoring guide for evaluation.

### Regression Eval

An eval used to ensure a change did not make behavior worse.

### Online Eval

An eval performed on production or live workflow output.

### Offline Eval

An eval performed outside live production traffic, usually in CI or staging.

### Red-Team Eval

An adversarial eval designed to reveal unsafe or vulnerable behavior.

### Human Review Eval

An eval based on human judgment, rating, correction, or review.

### LLM-as-Judge

A model used to evaluate another model’s output.

LLM-as-judge results should be treated as useful but not automatically authoritative.

### Eval Gate

A requirement that a workflow, prompt, tool, policy, or agent version pass evals before promotion.

### Evaluation Dimension

A quality or safety dimension being measured.

Initial MVP dimensions:

- task completion,
- correctness,
- policy compliance,
- tool correctness,
- memory correctness,
- evidence completeness,
- final answer usefulness,
- cost,
- latency,
- user satisfaction.

---

## 12. Feedback & Learning Terms

### Feedback

Information about the quality, correctness, safety, or usefulness of an output or action.

Feedback may come from users, reviewers, evals, failures, or business metrics.

### User Feedback

Feedback submitted by the human using the workflow.

Examples:

- thumbs up,
- thumbs down,
- correction,
- comment,
- rating.

### Correction

A specific statement that something was wrong and what the right version should be.

Corrections may produce memory candidates or eval cases.

### Human Review

A structured review by a user or reviewer.

### Feedback Record

The persisted object representing feedback.

It should link to:

- run,
- output,
- user,
- timestamp,
- feedback type,
- correction if any.

### Failure

A meaningful breakdown in AI behavior or system behavior.

Examples:

- hallucinated fact,
- wrong tool call,
- policy violation,
- missing evidence,
- unsafe memory write,
- bad recommendation.

### Failure Taxonomy

The canonical classification system for failures.

Initial categories may include:

- factual error,
- missing context,
- wrong memory,
- unsafe memory candidate,
- policy violation,
- unsafe tool proposal,
- wrong tool parameters,
- bad output format,
- incomplete evidence,
- poor user value,
- excessive cost,
- latency failure.

### Learning Loop

The process by which feedback and failures improve the system.

Aegis learning loop:

```text
run -> evidence -> eval -> feedback -> failure pattern -> improvement proposal -> regression test -> policy/memory/tool/prompt update
```

### Improvement Recommendation

A proposed change to improve the system.

Examples:

- update prompt,
- add eval case,
- correct memory,
- tighten policy,
- change tool schema,
- require approval,
- improve evidence rendering.

### Feedback-to-Memory Flow

The process where user correction creates or modifies a Memory Candidate.

### Feedback-to-Eval Flow

The process where failures become future eval cases.

### Review Queue

A queue of items needing human attention.

Examples:

- memory candidates,
- approval requests,
- eval failures,
- policy exceptions,
- high-risk actions.

---

## 13. Business Outcome Terms

### Business Outcome

A measurable business result connected to an AI run or workflow.

Examples:

- time saved,
- lead qualified,
- customer response drafted,
- risky action prevented,
- rework avoided,
- ticket resolved,
- cycle time reduced.

### Outcome Event

The stored record of a Business Outcome.

### Outcome Metric

The named measurement being tracked.

Examples:

- `time_saved_minutes`,
- `follow_up_created`,
- `risk_prevented`,
- `draft_created`,
- `approval_required`,
- `eval_passed`.

### KPI

Key performance indicator.

A KPI may aggregate many Outcome Events.

### ROI

Return on investment.

Aegis should eventually support ROI reporting, but MVP outcome metrics may be estimated.

### Estimated Outcome

An outcome value calculated by heuristic rather than direct measurement.

Example:

- “draft creation saved 12 minutes.”

### Verified Outcome

An outcome confirmed by external data or human review.

Example:

- a customer replied,
- a ticket was resolved,
- a lead converted.

### Time Saved

An estimated or verified reduction in manual work.

### Risk Prevented

A business outcome where Aegis blocked, escalated, or required approval for an unsafe action.

### Revenue Influenced

A business outcome indicating that an AI workflow contributed to revenue activity.

This should be treated carefully and not overclaimed.

### Outcome Summary

A human-readable summary of business impact for a run or workflow.

---

## 14. Architecture Terms

### Plane

A major conceptual layer of the control plane.

Aegis has seven core planes:

1. Agent Runtime Plane
2. Memory Plane
3. Tool Governance Plane
4. Policy & Safety Plane
5. Evaluation Plane
6. Evidence & Audit Plane
7. Learning & Business Outcome Plane

### Service

A deployable or logical component with a clear responsibility.

Services may be physically separate later. In the MVP, they may begin as modules.

### Module

A code-level unit inside a service or application.

### Boundary

A line that separates responsibilities.

Examples:

- Runtime owns orchestration.
- Memory owns memory records.
- Tool Broker owns tool execution.
- Policy owns decisions.
- Evidence owns proof artifacts.

### Contract

A stable interface between components.

Contracts may be represented as:

- JSON Schema,
- OpenAPI,
- AsyncAPI,
- event schemas,
- Markdown specs,
- database schema,
- SDK interfaces.

### Schema

A formal definition of data shape.

Schemas are core to Aegis because the platform depends on structured evidence, tool calls, policy decisions, and evals.

### Adapter

A component that connects Aegis to an external system or provider.

Examples:

- model provider adapter,
- MCP adapter,
- CRM adapter,
- email adapter.

### Gateway

The service that receives external API requests.

### Admin UI

The user interface for inspecting runs, evidence, memory, tools, policy decisions, evals, feedback, and outcomes.

### Demo Console

A simple local workflow runner for demonstrating the MVP before the full UI exists.

### Local-first

A design principle requiring the MVP to run locally without paid services.

### Provider-agnostic

A design principle requiring Aegis not to be hardwired to one model provider, vector store, or agent framework.

### Contract-first

A design principle requiring schemas and interfaces to be defined before or alongside implementation.

### Evidence-first

A design principle requiring important behavior to produce evidence.

### Policy-first

A design principle requiring sensitive behavior to be mediated by policy.

---

## 15. GitHub Planning Terms

### Epic

A major body of work.

In GitHub, Aegis models epics as issues labeled `epic`.

### Work Packet

A bounded, executable unit of planning or implementation.

In GitHub, Aegis models work packets as issues labeled `work-packet`.

### Task

A smaller implementation step under a Work Packet.

Tasks may be created later as GitHub issues or tracked in checklists.

### Milestone

A GitHub milestone grouping related epics and work packets.

### Critical Path

The shortest set of work packets needed to reach a credible MVP demo.

### Label

A GitHub issue label used for filtering, grouping, and reporting.

Examples:

- `epic`,
- `work-packet`,
- `critical-path`,
- `area:memory`,
- `area:policy`.

### Project Board

The GitHub Project used to manage Aegis issues.

### Parent Epic Link

A link from a Work Packet issue to its parent Epic issue.

GitHub Issues do not provide native epic hierarchy in the repo issue model, so Aegis uses labels and issue body links.

---

## 16. Repository Terms

### Project Index Entry

The metadata record that lets the user look up the codename and retrieve project metadata.

For Aegis, this is represented by `PROJECT_INDEX_ENTRY.yaml`.

### Project Metadata

Canonical project metadata stored under `.aic/metadata/project.yaml`.

### ADR

Architecture Decision Record.

ADRs record important decisions, context, alternatives, and consequences.

### Planning Doc

A document that defines work before implementation.

### Acceptance Criteria

The conditions that must be true for work to be considered complete.

### Definition of Done

A stronger completion standard that may include tests, docs, review, evidence, and issue updates.

### Scaffold

The generated repository skeleton.

### Install Script

A safe script that writes generated artifacts into the repo and backs up overwritten files.

### Script Backup

A copy of a file before a generated install script overwrites it.

Aegis scripts should store backups under `.aic/script-backups/`.

---

## 17. Security Terms

### Secret

A credential, token, key, password, certificate, or other sensitive authentication material.

Secrets must never be exposed to models.

### Credential Boundary

The boundary that prevents AI models from directly owning or seeing credentials.

### Scoped Credential

A credential limited to a specific tool, action, tenant, user, or time window.

### Least Privilege

The principle of granting only the minimum permissions needed.

### Approval

A recorded human or system decision allowing a pending action.

### Approval Request

A request for approval before performing a controlled action.

### Approval Decision

The recorded approve or deny response.

### Human-in-the-Loop

A control pattern where humans review, approve, correct, or supervise AI behavior.

### Audit Retention

The policy for how long run events, evidence packs, policy decisions, and related records are stored.

### Sensitive Data

Data that requires controlled handling.

In Aegis MVP, sensitivity is represented through data classification.

---

## 18. Common Phrases and Canonical Usage

### “The model proposes; the platform disposes.”

This is the core Aegis control principle.

Meaning:

- the model can suggest,
- Aegis decides,
- tools execute only through brokers,
- memory writes require admission,
- policy decisions happen outside the model,
- evidence is generated by the platform.

### “Memory is not a vector dump.”

Meaning:

- memory must have provenance,
- memory must be scoped,
- memory must be correctable,
- memory must have lifecycle,
- memory must not become unmanaged organizational hallucination.

### “Evidence is a product feature.”

Meaning:

- auditability is not an afterthought,
- every meaningful run should produce proof,
- evidence should be readable and exportable.

### “Business outcomes are the final score.”

Meaning:

- AI output alone is not enough,
- Aegis must connect AI activity to operational value.

### “Govern agents, do not merely run agents.”

Meaning:

- Aegis is not just an agent runtime,
- Aegis is the control plane around agent execution.

---

## 19. Reserved Event Names

The following event names should be treated as reserved MVP vocabulary.

### Run lifecycle

- `run.created`
- `run.started`
- `run.waiting_for_approval`
- `run.completed`
- `run.failed`
- `run.cancelled`

### Policy

- `policy.check_requested`
- `policy.checked`
- `policy.allowed`
- `policy.denied`
- `policy.approval_required`

### Memory

- `memory.retrieval_requested`
- `memory.retrieved`
- `memory.candidate_proposed`
- `memory.candidate_accepted`
- `memory.candidate_rejected`
- `memory.candidate_queued`
- `memory.corrected`
- `memory.superseded`
- `memory.expired`

### Model

- `model.call_requested`
- `model.called`
- `model.completed`
- `model.failed`

### Tools

- `tool.proposed`
- `tool.validation_failed`
- `tool.policy_checked`
- `tool.allowed`
- `tool.denied`
- `tool.approval_required`
- `tool.executed`
- `tool.failed`
- `tool.result_filtered`

### Approval

- `approval.requested`
- `approval.granted`
- `approval.denied`
- `approval.expired`

### Evidence

- `evidence.generation_requested`
- `evidence.generated`
- `evidence.exported`
- `evidence.redacted`

### Evals

- `eval.requested`
- `eval.started`
- `eval.completed`
- `eval.failed`
- `eval.regression_detected`

### Feedback

- `feedback.received`
- `feedback.correction_received`
- `feedback.memory_candidate_created`
- `feedback.eval_case_created`

### Outcomes

- `outcome.recorded`
- `outcome.estimated`
- `outcome.verified`

---

## 20. Reserved Object Names

These names should be used consistently in schemas, docs, APIs, and service code.

- `Tenant`
- `User`
- `Actor`
- `Agent`
- `AgentDefinition`
- `AgentVersion`
- `Run`
- `RunEnvelope`
- `RunEvent`
- `Trace`
- `ModelCall`
- `Memory`
- `MemoryRecord`
- `MemoryCandidate`
- `MemoryAdmissionDecision`
- `ToolDefinition`
- `ToolManifest`
- `ToolProposal`
- `ToolCall`
- `ToolResult`
- `Policy`
- `PolicyCheck`
- `PolicyDecision`
- `ApprovalRequest`
- `ApprovalDecision`
- `EvidencePack`
- `EvalCase`
- `EvalDataset`
- `EvalRun`
- `EvalResult`
- `FeedbackRecord`
- `BusinessOutcome`
- `OutcomeEvent`

---

## 21. Acronyms

| Acronym | Meaning |
|---|---|
| AIC | Applied Innovation Corp |
| ADR | Architecture Decision Record |
| AI | Artificial Intelligence |
| API | Application Programming Interface |
| CI | Continuous Integration |
| CRM | Customer Relationship Management |
| DX | Developer Experience |
| E2E | End-to-End |
| Eval | Evaluation |
| KPI | Key Performance Indicator |
| LLM | Large Language Model |
| MCP | Model Context Protocol |
| MVP | Minimum Viable Product |
| OPA | Open Policy Agent |
| OTEL | OpenTelemetry |
| RAG | Retrieval-Augmented Generation |
| ROI | Return on Investment |
| SDK | Software Development Kit |
| UI | User Interface |
| WP | Work Packet |

---

## 22. Term Ownership by System Plane

| Term family | Owning plane |
|---|---|
| Run, Run Envelope, Run Event, Trace | Agent Runtime Plane |
| Memory, Memory Candidate, Retrieval, Admission | Memory Plane |
| Tool Manifest, Tool Proposal, Tool Call, Broker | Tool Governance Plane |
| Policy, Policy Checkpoint, Policy Decision | Policy & Safety Plane |
| Eval Case, Eval Run, Eval Result | Evaluation Plane |
| Evidence Pack, Evidence Export, Audit Trail | Evidence & Audit Plane |
| Feedback, Failure, Outcome, KPI | Learning & Business Outcome Plane |

---

## 23. Anti-Glossary

These are terms or phrases Aegis should avoid or use carefully.

### “Autonomous employee”

Avoid for MVP.

It overpromises and implies unsafe autonomy.

Prefer:

- governed assistant,
- supervised agent workflow,
- controlled automation,
- AI workflow under policy.

### “AI remembers everything”

Avoid.

Prefer:

- AI can retrieve governed memory,
- Aegis stores admitted memory,
- memory has scope, source, confidence, and lifecycle.

### “Fully automated”

Avoid unless it is truly accurate.

Prefer:

- human-supervised,
- policy-governed,
- approval-gated,
- bounded autonomy.

### “Compliance guaranteed”

Avoid.

Prefer:

- evidence-backed,
- policy-enforced,
- audit-ready,
- compliance-supporting.

### “Hallucination-proof”

Avoid.

Prefer:

- evaluated,
- grounded,
- evidence-backed,
- lower hallucination risk,
- correction-enabled.

### “Agent framework”

Avoid as the primary category.

Prefer:

- AI Reliability Control Plane,
- reliability layer,
- governed agent runtime.

---

## 24. Glossary Acceptance Criteria

WP-E0-002 is complete when:

- core product terms are defined,
- runtime terms are defined,
- memory terms are defined,
- tool terms are defined,
- policy terms are defined,
- evidence terms are defined,
- eval terms are defined,
- feedback terms are defined,
- business outcome terms are defined,
- architecture terms are defined,
- GitHub planning terms are defined,
- reserved event names are listed,
- reserved object names are listed,
- anti-glossary terms are listed,
- future docs can reference this glossary as the canonical vocabulary.

---

## 25. Next Documents That Should Use This Glossary

This glossary should directly inform:

1. WP-E0-003 — Architecture Overview
2. WP-E0-004 — MVP System Boundaries
3. WP-E0-005 — Initial ADR Pack
4. WP-E0-006 — Threat Model Draft
5. WP-E0-007 — First Workflow Specification
6. WP-E1-001 — Run Envelope Schema
7. WP-E1-003 — Run Event Taxonomy
8. WP-E2-001 — Memory Model Specification
9. WP-E3-001 — Tool Manifest Schema
10. WP-E5-001 — Evidence Pack Schema

---

## 26. Final Glossary Statement

Aegis is not just a place where AI work runs.

Aegis is the control layer that gives AI work identity, boundaries, policy, memory, evidence, evals, feedback, and business accountability.

The vocabulary in this glossary should be treated as the canonical language for building that system.

