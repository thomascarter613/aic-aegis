# WP-E0-001 — Product Charter

Status: proposed  
Codename: Aegis  
Product name: AIC AI Reliability Control Plane  
Short name: AIC Aegis  
Company: Applied Innovation Corp  
Owner: Thomas Carter  
Document type: Product charter  
Work packet: WP-E0-001  
Parent epic: E0 — Product Charter & Architecture  
Last updated: 2026-06-15  

---

## 1. Executive Summary

AIC Aegis is the software layer that makes AI systems reliable enough to operate inside real businesses.

It wraps AI models, agents, tools, memory stores, business systems, policies, evaluations, traces, evidence, and outcomes inside a governed runtime. Its purpose is to let organizations deploy AI systems that can remember reliably, act safely, learn from feedback, use tools through controlled channels, evaluate themselves, follow policy, produce evidence, and improve measurable business results.

Aegis is not merely a chatbot, prompt library, agent framework, RAG app, observability tool, or compliance dashboard. It is an **AI Reliability Control Plane**.

Its central product claim is:

> Aegis makes agentic AI workflows governable, observable, correctable, auditable, and outcome-driven.

The MVP should prove this with one concrete workflow: a governed Sales/Ops Assistant that can analyze a customer conversation, retrieve approved memory, propose safe actions, create a draft, block or require approval for risky tool calls, generate an evidence pack, collect feedback, run evals, and produce a business outcome record.

---

## 2. Product Definition

### 2.1 Product category

Aegis belongs to a new but increasingly necessary category:

> AI Reliability Control Plane

Adjacent categories include:

- AgentOps
- LLMOps
- AI governance
- AI observability
- AI evals
- RAG governance
- tool-use governance
- workflow automation
- enterprise AI infrastructure
- policy-as-code for AI systems
- AI memory infrastructure
- AI evidence and audit infrastructure

Aegis is broader than any one of these. It combines them into an operational layer for production AI work.

### 2.2 Product statement

Aegis is a control plane for production AI systems. It governs how AI agents remember, reason over context, use tools, follow policy, generate evidence, receive feedback, evaluate performance, and connect activity to business outcomes.

### 2.3 One-liner

Memory, tools, policy, evals, evidence, and business outcome intelligence for production AI systems.

### 2.4 Short description

Aegis wraps AI workflows with reliable memory, governed tool execution, runtime policy checks, traceability, evidence packs, feedback loops, evaluations, and outcome analytics so businesses can safely operationalize AI.

### 2.5 Long description

Aegis is a reliability and governance layer for AI systems that sit inside business workflows. It captures every AI run in a structured envelope, attaches policy and memory context, governs tool use through a broker, records model and tool events, generates evidence packs, collects human and business feedback, runs evaluations, and creates a continuous improvement loop.

The product exists because companies do not only need access to AI models. They need AI systems that behave predictably, respect operational boundaries, remember correctly, use tools safely, prove what happened, and improve real business metrics over time.

---

## 3. Mission

Aegis exists to help Applied Innovation Corp build the software layer that makes AI operationally trustworthy.

The mission is:

> Help businesses safely, repeatedly, and profitably convert AI into operations, automation, governance, software delivery, and measurable revenue by giving AI systems memory, policy, tool governance, evals, evidence, and outcome intelligence.

---

## 4. Vision

The long-term vision is for Aegis to become the default reliability substrate for agentic AI systems.

A mature Aegis deployment should answer these questions for any AI action:

1. Who requested this?
2. What was the AI asked to do?
3. Which agent or workflow handled it?
4. What context was retrieved?
5. What memory was used?
6. What policy applied?
7. What tools were requested?
8. Which tools were allowed, denied, or escalated?
9. What model was called?
10. What output was produced?
11. What human approvals occurred?
12. What business system changed?
13. What evidence proves it?
14. What did it cost?
15. Was the result good?
16. What was learned?
17. Did it improve the business?

Aegis should eventually become a platform that lets organizations move from ad hoc AI usage to governed AI operations.

---

## 5. Strategic Thesis

The core thesis is:

> The future bottleneck in business AI adoption is not model access. It is operational trust.

Most organizations can already access capable AI models. What they cannot easily do is safely connect those models to memory, tools, workflows, sensitive data, business processes, human approvals, and outcome measurement.

As AI systems become more agentic, the unsolved problems become more severe:

- unreliable memory,
- hidden hallucinations,
- unsafe tool use,
- weak policy enforcement,
- insufficient evals,
- no clear audit trail,
- no human feedback loop,
- disconnected business metrics,
- inability to prove ROI,
- inability to explain what happened.

Aegis should solve those problems by sitting between agents and the business.

---

## 6. Product Principles

### 6.1 The model proposes; the platform disposes

AI models may suggest actions. The Aegis runtime decides whether those actions are allowed, denied, transformed, escalated, or executed.

The model should not directly own:

- credentials,
- durable memory writes,
- irreversible tool execution,
- policy decisions,
- approval decisions,
- final evidence generation,
- business outcome claims.

### 6.2 Memory must be governed

Memory is not a vector dump. Reliable memory requires:

- ownership,
- source,
- scope,
- provenance,
- sensitivity classification,
- confidence,
- expiration,
- correction,
- supersession,
- auditability.

A memory that cannot be explained, corrected, or scoped should not be trusted.

### 6.3 Tool use must be brokered

Tools are where AI becomes useful and dangerous. Every tool call must pass through a Tool Broker that can enforce:

- identity,
- permissions,
- schema validation,
- data classification,
- policy,
- approval,
- rate limits,
- execution boundaries,
- result filtering,
- audit logging.

### 6.4 Policy must execute at runtime

Policies should not only live in documents. Aegis must enforce policies during AI execution.

Policy checkpoints should exist before:

1. context retrieval,
2. prompt assembly,
3. model calls,
4. tool calls,
5. memory writes,
6. final output release,
7. business system mutation,
8. evidence generation.

### 6.5 Evals are part of delivery

Prompts, agents, policies, tools, workflows, memory rules, and retrieval strategies should be evaluated like software.

Aegis should make it possible to say:

> This AI workflow version is better, safer, cheaper, or more reliable than the previous version.

### 6.6 Evidence is a first-class product feature

Aegis should produce evidence, not merely logs.

An evidence pack should explain what happened in a way that a founder, operator, engineer, auditor, or customer success owner can understand.

### 6.7 Business outcomes are the final score

The platform is not successful merely because the AI responded.

It is successful when it improves measurable outcomes:

- fewer manual hours,
- faster cycle time,
- fewer errors,
- better response quality,
- less rework,
- more qualified leads,
- better customer follow-up,
- improved compliance posture,
- lower operational cost,
- higher revenue throughput.

---

## 7. Target Users

### 7.1 Initial internal user

The first user is Applied Innovation Corp itself.

Aegis should help AIC develop repeatable AI implementation infrastructure for:

- consulting delivery,
- internal operations,
- SMB automation,
- AI governance,
- agent workflow implementation,
- evidence-backed client reporting.

### 7.2 Initial external users

Initial external users are likely:

1. SMB and mid-market operators adopting AI,
2. engineering teams deploying AI workflows,
3. founders building AI-assisted operations,
4. AI implementation consultants,
5. CTOs or technical operators responsible for safe AI adoption,
6. teams that need proof that AI work happened correctly.

### 7.3 Future users

Future users may include:

- enterprise AI platform teams,
- compliance and risk teams,
- internal automation teams,
- AI product teams,
- support operations,
- sales operations,
- software delivery organizations,
- managed service providers,
- vertical AI solution builders.

---

## 8. Primary Buyer Personas

### 8.1 Technical founder / operator

Pain:

- wants to use AI to automate operations,
- lacks a trustworthy runtime,
- cannot afford fragile agent demos,
- needs proof, logs, safety, and repeatability.

Aegis value:

- gives them a structured AI operating layer.

### 8.2 CTO / VP Engineering

Pain:

- AI tools are spreading across the company,
- teams are connecting models to code, docs, tickets, and customer systems,
- risk is rising,
- reliability is unclear,
- eval coverage is weak.

Aegis value:

- provides governance, evals, traces, and tool controls.

### 8.3 SMB owner / operations leader

Pain:

- knows AI can help but does not know how to safely integrate it,
- needs measurable results,
- does not want black-box automation.

Aegis value:

- enables safe, evidence-backed automation.

### 8.4 AI implementation consultant

Pain:

- each client implementation is custom,
- difficult to prove ROI,
- difficult to reuse governance patterns.

Aegis value:

- becomes the reusable delivery substrate.

---

## 9. Core Problem

The core problem is:

> AI systems are becoming capable enough to perform business work, but most organizations lack the reliability layer required to let those systems act safely, remember accurately, follow policy, generate proof, learn from feedback, and improve business outcomes.

Symptoms include:

- agents forget important context,
- agents remember incorrect context,
- vector databases accumulate stale or unsafe memory,
- tool calls are over-permissive,
- risky actions are not escalated,
- prompts contain policy but runtime does not enforce it,
- AI outputs are difficult to audit,
- teams cannot reproduce what happened,
- failures do not become tests,
- feedback does not improve the system,
- ROI is claimed but not measured.

---

## 10. Desired Outcome

Aegis should let a business say:

> We know what our AI systems did, why they did it, what data they used, what policy they followed, what tools they called, what humans approved, what evidence was produced, and whether the result improved the business.

---

## 11. Product Scope

### 11.1 In scope for MVP

The MVP includes:

1. run envelope,
2. run event log,
3. memory schema,
4. Memory Admission Gate,
5. governed memory retrieval,
6. tool registry,
7. tool manifest schema,
8. Tool Broker,
9. policy decision interface,
10. base policy pack,
11. evidence pack schema,
12. evidence pack generator,
13. eval case schema,
14. basic eval runner,
15. feedback capture,
16. business outcome event schema,
17. local development environment,
18. one canonical example workflow.

### 11.2 Out of scope for MVP

The MVP does not include:

- enterprise SSO,
- billing,
- marketplace,
- full multi-tenant SaaS hardening,
- complex visual workflow builder,
- fine-tuning,
- autonomous browser operation,
- production HIPAA or PCI support,
- complete connector ecosystem,
- fully autonomous destructive actions,
- generalized multi-agent swarm framework,
- customer-facing no-code builder,
- large-scale hosted cloud platform.

### 11.3 Explicit non-goal

The MVP should not try to become the AI agent itself.

The MVP should become the layer that governs the agent.

---

## 12. First Canonical Workflow

The first workflow is:

> Governed Sales/Ops Assistant

### 12.1 Workflow purpose

The Sales/Ops Assistant helps analyze a customer conversation and produce safe follow-up actions.

It is intentionally chosen because it touches the core Aegis planes without requiring high-risk automation.

### 12.2 Example user request

> Analyze this customer conversation, summarize what matters, draft a follow-up email, suggest CRM updates, and tell me what should happen next.

### 12.3 MVP workflow steps

1. User submits conversation.
2. Gateway creates request.
3. Runtime creates run envelope.
4. Runtime creates trace ID.
5. Policy service checks data classification.
6. Memory service retrieves allowed memories.
7. Runtime assembles governed model context.
8. Model produces summary, recommendations, and proposed tool calls.
9. Tool Broker receives tool proposals.
10. Policy service evaluates each tool call.
11. CRM read is allowed.
12. Email draft creation is allowed or conditionally allowed.
13. Email send is blocked or requires approval.
14. Evidence service records all relevant steps.
15. Eval service scores the result.
16. User gives feedback.
17. Memory Admission Gate evaluates memory candidates.
18. Outcome service records an estimated business result.

### 12.4 Why this is the correct first workflow

This workflow proves:

- memory retrieval,
- policy enforcement,
- tool governance,
- approval logic,
- evidence generation,
- eval scoring,
- feedback capture,
- outcome tracking.

It also has a clear business story:

- better follow-up,
- faster response,
- fewer missed details,
- safer automation,
- measurable time savings.

---

## 13. Core System Planes

### 13.1 Agent Runtime Plane

Owns:

- run lifecycle,
- agent identity,
- state transitions,
- model call orchestration,
- event sequencing,
- trace propagation,
- tool proposal routing,
- error handling,
- retries,
- status changes.

Minimum MVP responsibilities:

- create run,
- update run status,
- append run events,
- attach trace ID,
- call mock or real model provider,
- pass tool proposals to Tool Broker,
- request evidence generation.

### 13.2 Memory Plane

Owns:

- working memory,
- episodic memory,
- semantic memory,
- procedural memory,
- evaluative memory,
- memory candidates,
- memory admission,
- memory correction,
- memory expiration,
- memory supersession.

Minimum MVP responsibilities:

- store memory records,
- retrieve allowed memory,
- propose memory candidates,
- admit/reject/queue candidates,
- record memory events.

### 13.3 Tool Governance Plane

Owns:

- tool registry,
- tool manifests,
- tool risk classes,
- input/output schemas,
- tool permissions,
- tool call validation,
- execution boundary,
- approval requirement,
- audit record,
- tool result filtering.

Minimum MVP responsibilities:

- register basic tools,
- validate proposed tool calls,
- classify risk,
- consult policy service,
- allow safe tools,
- require approval for risky tools,
- block disallowed tools.

### 13.4 Policy & Safety Plane

Owns:

- runtime policy decisions,
- data classification rules,
- tool permission rules,
- memory write rules,
- output release rules,
- approval rules,
- policy decision records.

Minimum MVP responsibilities:

- expose policy decision API,
- evaluate tool calls,
- evaluate memory candidates,
- return allow/deny/require_approval,
- record policy decision metadata.

### 13.5 Evaluation Plane

Owns:

- eval cases,
- eval datasets,
- eval runs,
- eval results,
- regression checks,
- online evaluation,
- red-team cases later.

Minimum MVP responsibilities:

- evaluate first workflow against a simple rubric,
- record eval result,
- attach eval result to evidence pack.

### 13.6 Evidence & Audit Plane

Owns:

- evidence pack generation,
- evidence schema,
- run summary,
- memory refs,
- context refs,
- model call refs,
- tool call refs,
- policy decision refs,
- approval refs,
- output refs,
- eval result refs,
- outcome refs.

Minimum MVP responsibilities:

- generate evidence pack JSON,
- generate readable Markdown summary,
- link evidence pack to run.

### 13.7 Learning & Business Outcome Plane

Owns:

- feedback capture,
- correction records,
- failure taxonomy,
- improvement recommendations,
- outcome events,
- ROI estimates.

Minimum MVP responsibilities:

- collect thumbs up/down plus notes,
- produce memory candidate from feedback when appropriate,
- record basic business outcome metric.

---

## 14. MVP Architecture

### 14.1 Initial repository architecture

```text
apps/
  admin-ui/
  demo-console/

services/
  gateway/
  runtime/
  memory/
  tool-broker/
  policy/
  evals/
  evidence/
  outcomes/

packages/
  sdk-ts/
  sdk-python/
  schemas/
  policy-packs/
  tool-packs/
  eval-packs/
  prompt-packs/

contracts/
  openapi/
  asyncapi/
  events/

db/
  migrations/

infra/
  postgres/
  redis/
  opa/
  otel/
  docker/

docs/
  product/
  architecture/
  adrs/
  planning/
  governance/
  security/
  evidence/
  evals/
  business/
  operations/

examples/
  sales-ops-assistant/
  support-triage/
```

### 14.2 MVP deployment mode

The first deployment mode should be local-first.

Minimum local dependencies:

- PostgreSQL with pgvector,
- Redis,
- OPA,
- OpenTelemetry collector,
- mock LLM provider,
- optional local model provider later.

### 14.3 MVP implementation posture

The MVP should be:

- contract-first,
- local-first,
- evidence-first,
- policy-first,
- testable,
- modular,
- provider-agnostic,
- framework-agnostic,
- easy to run on a laptop.

---

## 15. Canonical Data Objects

### 15.1 Run Envelope

The Run Envelope is the canonical object that identifies and bounds an AI workflow execution.

It includes:

- run ID,
- tenant ID,
- user ID,
- agent ID,
- agent version,
- task type,
- status,
- trace ID,
- evidence pack ID,
- input refs,
- policy context,
- memory context,
- timestamps.

### 15.2 Run Event

Run Events record what happened during a run.

Examples:

- run.created,
- policy.checked,
- memory.retrieved,
- model.called,
- tool.proposed,
- tool.allowed,
- tool.denied,
- tool.requires_approval,
- approval.requested,
- evidence.generated,
- eval.completed,
- feedback.received,
- outcome.recorded.

### 15.3 Memory

A Memory is a durable or temporary knowledge record governed by source, scope, confidence, sensitivity, and lifecycle.

Memory types:

- working,
- episodic,
- semantic,
- procedural,
- evaluative.

### 15.4 Memory Candidate

A Memory Candidate is a proposed memory that has not yet been admitted.

It must be evaluated by the Memory Admission Gate.

### 15.5 Tool Manifest

A Tool Manifest describes:

- tool ID,
- name,
- description,
- risk level,
- side effect status,
- approval requirement,
- input schema,
- output schema,
- allowed roles,
- allowed data classes,
- evidence requirement.

### 15.6 Tool Call

A Tool Call records a proposed or executed tool action.

It includes:

- tool call ID,
- run ID,
- tool ID,
- input,
- output,
- status,
- policy decision ID,
- timestamps.

### 15.7 Policy Decision

A Policy Decision records a runtime decision.

Decision types:

- allow,
- deny,
- require_approval,
- sanitize,
- redact,
- escalate,
- defer.

### 15.8 Evidence Pack

An Evidence Pack is the audit artifact for a run.

It links:

- input refs,
- memory refs,
- context refs,
- policy decision refs,
- model call refs,
- tool call refs,
- approval refs,
- output refs,
- eval result refs,
- outcome refs,
- cost record.

### 15.9 Eval Result

An Eval Result records quality, safety, or performance assessment.

Dimensions may include:

- task completion,
- correctness,
- policy compliance,
- tool correctness,
- memory correctness,
- evidence completeness,
- cost,
- latency,
- user satisfaction.

### 15.10 Business Outcome

A Business Outcome connects AI activity to operational value.

Examples:

- time_saved_minutes,
- response_cycle_time_reduced,
- lead_qualified,
- ticket_resolved,
- rework_avoided,
- risk_prevented,
- revenue_influenced.

---

## 16. Policy Model

### 16.1 Required policy checkpoints

Aegis must eventually check policy:

1. before context retrieval,
2. before prompt assembly,
3. before model call,
4. before tool call,
5. before memory write,
6. before output release,
7. before business system mutation,
8. before evidence export.

The MVP should implement at least:

1. tool call policy,
2. memory write policy,
3. output/action release policy.

### 16.2 Policy decision outcomes

Policy can return:

- allow,
- deny,
- require_approval,
- sanitize,
- redact,
- escalate,
- defer.

### 16.3 Policy design principle

Policy should be explainable.

Every decision must include:

- decision,
- reason,
- policy ID,
- policy version,
- run ID,
- timestamp.

---

## 17. Tool Governance Model

### 17.1 Tool risk classes

| Risk class | Meaning | Example | MVP behavior |
|---|---|---|---|
| read_only | Reads information only | Read CRM contact | Allow with log and policy check |
| low_write | Creates reversible artifact | Create email draft | Allow or conditional approval |
| medium_write | Changes business records | Update CRM | Require stronger policy check |
| high_write | External or consequential action | Send email | Require approval |
| critical | Destructive or regulated action | Delete records, issue refund | Block by default |

### 17.2 MVP tools

The first tool pack should include:

1. `crm.read_contact`
2. `crm.suggest_update`
3. `email.create_draft`
4. `email.send`
5. `evidence.generate_pack`
6. `memory.propose_candidate`

Only `email.create_draft` should be executable in the first demo. `email.send` should be blocked or require approval.

### 17.3 Tool principle

Agents do not call tools directly.

Agents propose tool calls. The Tool Broker validates, authorizes, executes, records, and returns results.

---

## 18. Memory Model

### 18.1 Memory types

| Type | Purpose |
|---|---|
| working | temporary task state |
| episodic | record of what happened |
| semantic | durable facts |
| procedural | how work should be done |
| evaluative | lessons about quality or failure |

### 18.2 Memory admission states

A memory candidate can be:

- accepted,
- rejected,
- queued_for_review,
- merged,
- superseded,
- stored_temporary,
- expired.

### 18.3 Memory admission rules

A durable memory should require:

- clear source,
- clear subject,
- clear reason,
- confidence score,
- sensitivity classification,
- scope,
- lifecycle,
- correction path.

### 18.4 Memory principle

The AI model can propose memory. The platform decides whether memory is stored.

---

## 19. Evaluation Model

### 19.1 MVP eval dimensions

The MVP should score:

1. task completion,
2. policy compliance,
3. tool correctness,
4. memory correctness,
5. evidence completeness,
6. final answer usefulness,
7. cost/latency when available.

### 19.2 Eval sources

Eval cases can come from:

- curated test cases,
- production failures,
- human feedback,
- red-team prompts,
- policy violations,
- tool errors,
- memory corrections.

### 19.3 Eval principle

Every meaningful failure should become one of:

- a regression test,
- a policy update,
- a tool schema update,
- a memory correction,
- a prompt improvement,
- a workflow constraint.

---

## 20. Evidence Model

### 20.1 Evidence Pack purpose

Evidence Packs should make AI behavior inspectable.

They should be useful for:

- operators,
- developers,
- founders,
- auditors,
- clients,
- customer success teams,
- future debugging,
- ROI reporting.

### 20.2 Evidence Pack minimum contents

The MVP Evidence Pack must include:

- run summary,
- input refs,
- memory refs,
- policy decisions,
- model call summary,
- tool call summary,
- approval summary,
- output summary,
- eval summary,
- outcome summary,
- error summary,
- timestamps.

### 20.3 Evidence principle

Aegis should not ask users to “trust the AI.”

Aegis should show the evidence.

---

## 21. Business Outcome Model

### 21.1 Outcome categories

Aegis should track:

- productivity,
- quality,
- risk reduction,
- revenue influence,
- cost reduction,
- customer experience,
- cycle time,
- compliance posture.

### 21.2 MVP business metrics

For the first workflow, track:

- time_saved_minutes,
- follow_up_created,
- risky_action_prevented,
- approval_required,
- draft_created,
- eval_passed,
- human_feedback_score.

### 21.3 Outcome principle

The product must help answer:

> Did AI improve the business process, or did it merely produce text?

---

## 22. Initial Service Boundaries

### 22.1 Gateway service

Responsibilities:

- receive API requests,
- authenticate later,
- validate request shape,
- create initial run request,
- forward to runtime.

### 22.2 Runtime service

Responsibilities:

- create run envelope,
- manage run lifecycle,
- orchestrate model and tool flow,
- append run events,
- request evidence generation.

### 22.3 Memory service

Responsibilities:

- retrieve memory,
- propose memory candidates,
- apply Memory Admission Gate,
- record memory events.

### 22.4 Tool Broker service

Responsibilities:

- register tools,
- validate tool calls,
- check risk level,
- request policy decision,
- execute or block tool,
- record tool call.

### 22.5 Policy service

Responsibilities:

- evaluate policy input,
- return policy decision,
- record policy decision,
- expose base policy packs.

### 22.6 Evidence service

Responsibilities:

- gather run artifacts,
- generate evidence pack,
- export JSON and Markdown,
- attach evidence pack to run.

### 22.7 Eval service

Responsibilities:

- run eval cases,
- score workflow output,
- store eval results,
- link evals to evidence.

### 22.8 Outcomes service

Responsibilities:

- record business outcome events,
- estimate time saved,
- connect run to KPI,
- support future dashboards.

---

## 23. MVP User Stories

### Story 1 — Create a governed run

As an operator, I want every AI workflow to begin with a run envelope so that all activity can be traced.

Acceptance:

- run ID is created,
- trace ID is created,
- agent ID is attached,
- tenant ID is attached,
- status is tracked,
- run events can be appended.

### Story 2 — Retrieve governed memory

As an operator, I want the agent to retrieve only allowed memory so that sensitive or irrelevant information is not used.

Acceptance:

- memory query includes tenant and subject scope,
- policy can filter retrieval,
- retrieved memory refs are recorded,
- evidence pack includes memory refs.

### Story 3 — Propose but broker tool calls

As an operator, I want the model to propose tool calls but not execute them directly so that tool use is safe.

Acceptance:

- tool proposal is captured,
- Tool Broker validates schema,
- policy decision is requested,
- allowed tools execute,
- risky tools require approval,
- blocked tools do not execute.

### Story 4 — Generate evidence pack

As an operator, I want a readable evidence pack for each run so that I can understand and prove what happened.

Acceptance:

- evidence pack JSON is generated,
- evidence pack Markdown summary is generated,
- run links to evidence pack,
- evidence includes policy, memory, tools, and evals.

### Story 5 — Evaluate the result

As an operator, I want each workflow output scored so that I can improve quality and safety.

Acceptance:

- eval case is selected,
- eval result is stored,
- score is attached to evidence,
- failed eval can become follow-up work.

### Story 6 — Capture feedback

As a user, I want to correct or rate AI output so that the system improves over time.

Acceptance:

- feedback is stored,
- feedback links to run,
- feedback may produce memory candidate or eval case,
- evidence pack references feedback.

### Story 7 — Record business outcome

As a founder or operator, I want to know whether the workflow saved time or reduced risk so that AI value is measurable.

Acceptance:

- outcome event is recorded,
- outcome links to run,
- metric name and value are stored,
- estimated flag is supported.

---

## 24. MVP Acceptance Criteria

The MVP is done when the Sales/Ops Assistant demo can perform the following end-to-end flow:

1. Accept a customer conversation input.
2. Create a run envelope.
3. Create a trace ID.
4. Record `run.created`.
5. Retrieve allowed memory.
6. Record `memory.retrieved`.
7. Evaluate context/tool policy.
8. Record policy decisions.
9. Call a mock or real model.
10. Record model call metadata.
11. Produce proposed actions.
12. Route tool proposals to Tool Broker.
13. Allow safe tool action.
14. Block or require approval for risky action.
15. Record tool call results.
16. Generate evidence pack.
17. Run at least one eval case.
18. Record eval result.
19. Capture user feedback.
20. Propose or reject memory candidate.
21. Record business outcome event.
22. Produce a readable run summary.

The MVP should be demonstrable locally with seeded data.

---

## 25. MVP Nonfunctional Requirements

### 25.1 Local-first

The MVP must run locally without requiring paid APIs.

Real model providers may be added, but mock provider mode must exist.

### 25.2 Provider-agnostic

The runtime must not be hardwired to one LLM provider.

### 25.3 Contract-first

Core objects must have schemas before deep implementation.

### 25.4 Audit-first

Every important action must create an event or evidence reference.

### 25.5 Policy-first

Sensitive actions must pass through policy before execution.

### 25.6 Safe by default

Unknown or high-risk actions should be denied or require approval.

### 25.7 Human-overridable with record

Human overrides should be allowed only with explicit recorded approval.

---

## 26. Initial Technical Decisions

These should become ADRs:

1. Aegis is an AI Reliability Control Plane.
2. PostgreSQL is the canonical source of truth.
3. pgvector is the initial semantic memory retrieval layer.
4. Qdrant may become an optional retrieval accelerator later.
5. Tools execute only through Tool Broker.
6. Policies execute at runtime.
7. Evidence Packs are first-class artifacts.
8. Evals are part of workflow promotion.
9. The MVP is local-first.
10. The system is provider-agnostic.
11. The first workflow is Sales/Ops Assistant.
12. Mock LLM mode is required.
13. High-risk actions require approval or are blocked.
14. Durable memory writes require admission.
15. Every run must have trace identity.

---

## 27. Risks

### 27.1 Scope creep

Risk:

Aegis could become too broad too early.

Mitigation:

Limit MVP to one workflow and the minimum platform pieces required to prove the architecture.

### 27.2 Building framework instead of product

Risk:

The project could become a generic agent framework.

Mitigation:

Keep focus on control, governance, evidence, and outcomes.

### 27.3 Overengineering

Risk:

Too many services too early could slow delivery.

Mitigation:

Service boundaries may begin as modules in one runtime, while preserving logical separation.

### 27.4 Weak demo value

Risk:

A platform demo may feel abstract.

Mitigation:

Use Sales/Ops Assistant to show concrete business workflow value.

### 27.5 Evidence without insight

Risk:

Evidence packs could become verbose logs.

Mitigation:

Generate both machine-readable JSON and human-readable summaries.

### 27.6 Memory poisoning

Risk:

Incorrect or malicious memory could degrade future behavior.

Mitigation:

Use Memory Admission Gate, confidence, source tracking, feedback, and supersession.

### 27.7 Policy bypass

Risk:

The agent may try to bypass tool or memory restrictions.

Mitigation:

The model never executes tools directly; runtime controls enforce decisions.

---

## 28. Success Metrics

### 28.1 MVP technical success

- local demo runs end-to-end,
- run envelope is created,
- events are recorded,
- memory is retrieved,
- tool calls are brokered,
- policy decisions are recorded,
- evidence pack is generated,
- eval result is recorded,
- feedback is captured,
- outcome event is created.

### 28.2 MVP product success

- the demo clearly explains why Aegis exists,
- the workflow proves safety and evidence,
- the architecture can support future workflows,
- the output can be used in AIC consulting,
- the project can generate GitHub epics and work packets.

### 28.3 Business success

Aegis becomes useful if it helps AIC:

- sell AI implementation services,
- deliver repeatable client outcomes,
- produce evidence-backed reports,
- reduce custom implementation effort,
- build reusable SaaS infrastructure,
- differentiate around trustworthy AI operations.

---

## 29. Naming

### 29.1 Codename

Aegis

### 29.2 Meaning

Aegis means shield, protection, sponsorship, or divine/strategic covering. It fits because the product protects and governs AI systems while enabling them to act.

### 29.3 Product naming options

Internal:

- Aegis
- AIC Aegis
- Aegis Runtime
- Aegis Control Plane

External later:

- AIC Reliability Layer
- AIC AgentOps Control Plane
- AIC AI Reliability Control Plane
- AIC Governed Agent Runtime

Recommended MVP name:

> AIC Aegis

Recommended category phrase:

> AI Reliability Control Plane

---

## 30. Positioning

### 30.1 Positioning statement

For organizations deploying AI into real workflows, Aegis is an AI Reliability Control Plane that governs memory, tools, policy, evals, evidence, and outcomes, so AI systems can act safely, improve continuously, and prove business value.

Unlike chatbot builders or agent frameworks, Aegis focuses on operational trust: what the AI remembered, what it was allowed to do, what it actually did, what evidence exists, and whether the business improved.

### 30.2 Tagline options

1. Make AI work provable.
2. The reliability layer for agentic AI.
3. Governed memory, tools, evals, and evidence for production AI.
4. From AI demos to AI operations.
5. Trust infrastructure for business AI.
6. The control plane for safe AI action.
7. Make agents accountable.

Recommended tagline:

> The reliability layer for agentic AI.

---

## 31. Competitive Differentiation

Aegis should differentiate by combining pieces that are often separate:

| Common tool type | What it usually solves | Aegis difference |
|---|---|---|
| Agent framework | agent execution | governs execution and evidence |
| RAG framework | retrieval | governs memory lifecycle |
| Observability platform | traces/logs | turns traces into evidence packs |
| Eval platform | quality scoring | connects evals to policy, memory, and outcomes |
| Workflow automation | action execution | brokers AI tool use through policy |
| Governance dashboard | oversight | enforces decisions at runtime |
| CRM/workflow app | business process | provides reusable AI reliability substrate |

Aegis should be sold as the connective reliability layer.

---

## 32. Initial Epics

### E0 — Product Charter & Architecture

Define product, scope, boundaries, architecture, and decision records.

### E1 — Run Envelope & Trace Model

Create the runtime identity backbone.

### E2 — Memory Service

Implement governed memory storage, retrieval, correction, and admission.

### E3 — Tool Registry & Broker

Implement governed tool use.

### E4 — Policy Engine

Implement runtime policy decisions.

### E5 — Evidence Packs

Generate proof artifacts for every run.

### E6 — Evaluation Runner

Measure workflow quality, safety, and regression.

### E7 — Feedback & Learning Loop

Turn human and system feedback into improvements.

### E8 — Business Outcome Analytics

Connect AI activity to business value.

---

## 33. First Work Packets

### WP-E0-001 — Product Charter

This document.

### WP-E0-002 — System Glossary

Define canonical terms.

### WP-E0-003 — Architecture Overview

Create system diagrams and boundaries.

### WP-E0-004 — Threat Model

Identify MVP risks and mitigations.

### WP-E0-005 — ADR Set

Finalize initial architecture decisions.

### WP-E1-001 — Run Envelope Schema

Define and validate run identity model.

### WP-E1-002 — Run Event Taxonomy

Define event model.

### WP-E2-001 — Memory Schema

Define canonical memory tables and schemas.

### WP-E3-001 — Tool Manifest Schema

Define tool registry contract.

### WP-E4-001 — Base Policy Pack

Define initial OPA/Rego decisions.

### WP-E5-001 — Evidence Pack Schema

Define evidence artifact.

### WP-E6-001 — Eval Case Schema

Define first evaluation pack.

### WP-E7-001 — Feedback Capture

Define user correction and feedback flow.

### WP-E8-001 — Outcome Event Schema

Define business outcome record.

---

## 34. Definition of Done for WP-E0-001

WP-E0-001 is complete when:

- product category is defined,
- mission is defined,
- vision is defined,
- target users are defined,
- MVP wedge is defined,
- first workflow is defined,
- in-scope and out-of-scope boundaries are clear,
- core planes are named,
- canonical objects are identified,
- MVP acceptance criteria are written,
- first epics are listed,
- first work packets are listed,
- the document can support GitHub issue generation.

---

## 35. Decision Summary

Approved or proposed decisions from this charter:

| Decision | Status |
|---|---|
| Codename is Aegis | proposed |
| Product category is AI Reliability Control Plane | proposed |
| MVP wedge is governed Sales/Ops Assistant | proposed |
| Aegis governs agents rather than becoming the agent | proposed |
| PostgreSQL is canonical data/memory store | proposed |
| Memory writes require admission | proposed |
| Tool calls require broker | proposed |
| Runtime policy checks are required | proposed |
| Evidence packs are first-class artifacts | proposed |
| Evals are required for improvement | proposed |
| Business outcomes are tracked | proposed |
| Local-first MVP mode is required | proposed |

---

## 36. Final Charter Statement

AIC Aegis is the AI Reliability Control Plane for Applied Innovation Corp.

It exists to turn AI from a powerful but opaque assistant into a governed operational system that can be trusted inside real business workflows.

The MVP should prove one complete loop:

```text
request
  -> run envelope
  -> governed memory
  -> policy check
  -> model call
  -> tool proposal
  -> tool broker
  -> approval/block/execute
  -> evidence pack
  -> eval
  -> feedback
  -> memory candidate
  -> business outcome
```

If this loop works, Aegis becomes the foundation for AIC’s consulting delivery, internal automation, SMB AI systems, future SaaS platform, and long-term AI governance/runtime product.

---

## 37. Next Recommended Work

After accepting this charter, proceed to:

1. WP-E0-002 — System Glossary
2. WP-E0-003 — Architecture Overview
3. WP-E0-004 — MVP Threat Model
4. WP-E0-005 — Initial ADR Pack
5. WP-E1-001 — Run Envelope and Event Schema

The immediate next best document is:

> WP-E0-002 — System Glossary

because consistent terminology will make the ADRs, epics, work packets, schemas, and GitHub issues much easier to generate cleanly.

