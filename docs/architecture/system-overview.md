# WP-E0-003 — Architecture Overview

Status: proposed  
Codename: Aegis  
Product: AIC AI Reliability Control Plane  
Short name: AIC Aegis  
Parent epic: E0 — Product Charter & Architecture  
Last updated: 2026-06-15  

---

## 1. Purpose

This document is the canonical architecture overview for Aegis.

It translates the Product Charter, System Glossary, Architecture Doctrine Pack, Aegis Laws, Control Catalog, Risk Register, MVP Strategy, Trust Ladder, and Maturity Model into a coherent system architecture that future work packets can implement.

Aegis is not a chatbot, not merely an agent framework, and not a generic workflow app.

Aegis is an **AI Reliability Control Plane for provable AI work**.

---

## 2. Architecture Doctrine Summary

Aegis is a:

> Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

The architecture exists to make AI work:

- identifiable,
- bounded,
- policy-governed,
- tool-safe,
- memory-governed,
- evidence-backed,
- evaluated,
- correctable,
- outcome-measured.

The most important product rule is:

> The model proposes; the platform disposes.

The model may summarize, classify, recommend, draft, and propose. The platform decides, authorizes, executes, blocks, escalates, records, evaluates, and proves.

---

## 3. Highest-Level Architecture Test

Every major feature must improve at least one of these:

- identity,
- authorization,
- context governance,
- memory governance,
- tool governance,
- policy enforcement,
- approval handling,
- evidence generation,
- evaluation,
- feedback,
- outcome measurement,
- control coverage,
- reliability.

If it does not, it is deferred.

---

## 4. System Context

Aegis sits between users, applications, agents, models, memory, tools, business systems, policies, evaluators, and evidence consumers.

```text
Users / Apps / SDKs / Admin UI
        |
        v
Aegis API / Gateway
        |
        v
Aegis Runtime / AgentOps Kernel
        |
        +--> Memory Plane
        +--> Policy Plane
        +--> Tool Governance Plane
        +--> Evidence Plane
        +--> Evaluation Plane
        +--> Feedback Plane
        +--> Outcome Plane
        |
        v
Data, Events, Telemetry, Evidence, and Audit Records
```

Aegis is responsible for governing the work. It is not required to own every external model, tool, or business system.

---

## 5. Architectural Shape

Aegis should be designed as logical service boundaries but implemented first as a modular local-first system.

Recommended MVP physical shape:

```text
apps/
  admin-ui/
  demo-console/

services/
  aegis-api/
  aegis-worker/

packages/
  core/
  schemas/
  adapters/
  sdk-ts/
  sdk-python/
  policy-packs/
  tool-packs/
  eval-packs/
  prompt-packs/

db/
  migrations/

infra/
  docker/
  postgres/
  redis/
  opa/
  otel/
  minio-later/
```

Recommended MVP deployment shape:

```text
aegis-api
  HTTP/API boundary
  auth placeholder
  tenant context
  command/query routes

aegis-worker
  runtime jobs
  tool execution jobs
  evidence generation
  eval jobs
  feedback/outcome processing

postgres + pgvector
  source of truth
  semantic retrieval support

redis
  queues/cache/locks where needed

opa
  first policy decision adapter

otel collector
  traces/logs/metrics pipeline
```

Do not split every plane into a physical microservice in MVP.

---

## 6. Clean Architecture Layers

Aegis follows Clean Architecture with Ports and Adapters.

```text
External Interfaces
  Admin UI, Demo Console, REST API, SDKs, Webhooks, CLI

Interface Adapters
  Controllers, Presenters, Repositories, Provider Adapters,
  OPA Adapter, Tool Adapters, Model Adapters, Storage Adapters

Application Layer
  Commands, Queries, Use Cases, Ports, Application Services

Domain Core
  Run, RunEnvelope, RunEvent, MemoryCandidate, MemoryRecord,
  ToolManifest, ToolProposal, ToolCall, PolicyDecision,
  EvidencePack, EvalResult, FeedbackRecord, BusinessOutcome
```

Dependency rule:

```text
Interfaces and infrastructure depend inward.
The domain core does not depend outward.
```

The domain core must not import:

- model provider SDKs,
- OPA/Rego internals,
- Postgres row types,
- Redis clients,
- MCP SDK types,
- OpenTelemetry SDKs,
- UI framework types,
- cloud provider SDKs.

---

## 7. Bounded Contexts

Aegis uses Domain-Driven Design bounded contexts.

| Context | Responsibility |
|---|---|
| Runtime Context | Run lifecycle, state machine, run events, orchestration |
| Memory Context | Memory records, candidates, retrieval, admission, correction |
| Tool Governance Context | Tool manifests, proposals, broker decisions, tool results |
| Policy Context | Policy checkpoints, decisions, reasons, policy versions |
| Evidence Context | Evidence packs, trust artifacts, redaction, exports |
| Evaluation Context | Eval cases, eval packs, eval runs, eval results |
| Feedback Context | Human feedback, corrections, failure classification |
| Outcome Context | Business outcomes, estimates, verification, dashboards |
| Identity/Tenant Context | Tenants, users, roles, permissions, tenant isolation |
| Integration Context | Model providers, MCP, CRM, email, storage, telemetry adapters |

These are logical contexts first. Physical service boundaries may come later.

---

## 8. Seven System Planes

Aegis has seven core planes.

| Plane | Purpose | MVP Capability |
|---|---|---|
| Agent Runtime Plane | Create and execute governed runs | Run Envelope, run events, state transitions |
| Memory Plane | Govern what AI remembers and retrieves | basic retrieval, memory candidate shape |
| Tool Governance Plane | Broker and govern tool execution | tool proposal, tool manifest, high-risk block/approval |
| Policy & Safety Plane | Decide allow/deny/approval/redaction | OPA-backed or mock policy decision |
| Evaluation Plane | Score behavior and protect promotion | basic eval result for golden workflow |
| Evidence & Audit Plane | Prove what happened | Evidence Level 2 pack |
| Learning & Business Outcome Plane | Convert feedback into improvement and value | feedback record, basic outcome event |

The MVP should build a thin vertical slice through all planes, not deep implementations of each plane.

---

## 9. Core Runtime Loop

The canonical reliability loop is:

```text
request
  -> create run envelope
  -> record run.created
  -> retrieve governed memory when applicable
  -> check policy
  -> call model or mock model
  -> receive model output and tool proposals
  -> broker tool proposals
  -> allow, deny, or require approval
  -> execute safe actions or pause risky actions
  -> generate evidence pack
  -> run eval
  -> capture feedback
  -> propose/admit memory if applicable
  -> record business outcome
  -> complete run
```

This loop is the product.

---

## 10. MVP Golden Workflow

The canonical golden workflow is:

> Governed Sales/Ops Follow-Up

It uses synthetic data only.

Flow:

```text
Synthetic customer conversation
  -> Sales/Ops Assistant run
  -> summary and follow-up recommendation
  -> draft email proposal
  -> crm.suggest_update proposal
  -> email.send proposal
  -> Tool Broker checks risk
  -> policy allows draft/suggestion
  -> policy blocks or approval-gates email.send
  -> Evidence Pack generated
  -> Eval Result recorded
  -> Feedback accepted
  -> Outcome event records time saved and risk prevented
```

The first demo should clearly show:

```text
AI tries to perform useful work.
Aegis lets safe work proceed.
Aegis blocks or escalates risky work.
Aegis explains why.
Aegis produces evidence.
Aegis records business value.
```

---

## 11. MVP-A and MVP-B Scope

### MVP-A — Proof Loop

MVP-A proves:

1. create run,
2. record events,
3. model/mock model proposes tool action,
4. Tool Broker receives proposal,
5. policy checks tool,
6. safe action proceeds or is mocked,
7. high-risk action is blocked or approval-gated,
8. Evidence Pack is generated,
9. run timeline is visible.

### MVP-B — Learning Loop

MVP-B adds:

1. governed memory retrieval,
2. memory candidate proposal,
3. Memory Admission Gate,
4. feedback capture,
5. basic eval result,
6. business outcome event.

---

## 12. Command and Query Architecture

Aegis uses selective CQRS.

Commands change state and enforce rules.

Queries assemble read models and projections.

Example command handlers:

```text
CreateRun
StartRun
AppendRunEvent
ProposeToolCall
BrokerToolCall
RequestApproval
RecordPolicyDecision
GenerateEvidencePack
RunEvaluation
CaptureFeedback
RecordBusinessOutcome
AdmitMemoryCandidate
CompleteRun
FailRun
```

Example query handlers:

```text
GetRun
GetRunTimeline
GetEvidencePack
GetEvidenceSummary
ListPendingApprovals
ListMemoryCandidates
GetEvalResults
GetOutcomeSummary
GetControlCoverage
```

CQRS is applied where it clarifies controlled writes versus optimized reads. It should not become ceremony for simple lookup data.

---

## 13. Event Architecture

Aegis is event-rich from day one.

MVP uses:

```text
state tables + run_events table
```

v1 should add:

```text
state tables + domain events + outbox_events + projections
```

Full event sourcing is deferred until replay/reconstruction requirements justify it.

Core event families:

```text
run.*
policy.*
memory.*
model.*
tool.*
approval.*
evidence.*
eval.*
feedback.*
outcome.*
```

Required event properties:

```text
event_id
event_type
event_version
tenant_id
run_id when applicable
actor when applicable
occurred_at
payload
```

Important rule:

> No silent failure.

Known failures emit events.

---

## 14. Data Architecture

PostgreSQL is the canonical source of truth for MVP and v1.

pgvector supports semantic retrieval, but vectors are not the truth layer.

Rule:

> Postgres stores truth. Vectors help find truth.

Core tables/groups:

```text
tenants
users
roles
agents
agent_versions
workflows
workflow_versions
runs
run_events
model_calls
memories
memory_candidates
memory_events
tool_definitions
tool_calls
policy_decisions
approval_requests
approval_decisions
evidence_packs
eval_cases
eval_runs
eval_results
feedback_records
business_outcomes
outbox_events later
```

Object storage is deferred until large evidence exports, file uploads, eval datasets, and model snapshots require it.

---

## 15. Memory Architecture

Memory is governed state, not a vector dump.

Memory records require:

- tenant scope,
- subject,
- source,
- confidence,
- sensitivity,
- lifecycle status,
- provenance,
- correction path,
- supersession path,
- evidence reference where applicable.

The AI may propose memory. The Memory Admission Gate decides whether memory is admitted.

MVP-B should support:

```text
MemoryCandidate
MemoryAdmissionDecision
MemoryRecord
basic governed retrieval
basic correction/supersession model
```

---

## 16. Tool Governance Architecture

Models and agents never directly execute tools.

Tool flow:

```text
model output
  -> ToolProposal
  -> Tool Broker
  -> manifest validation
  -> schema validation
  -> policy decision
  -> approval if required
  -> execution or denial
  -> result filtering
  -> event recording
  -> evidence reference
```

Tool risk classes:

```text
read_only
low_write
medium_write
high_write
critical
```

MVP tools should be synthetic or mocked.

Initial tool examples:

```text
crm.read_contact
crm.suggest_update
email.create_draft
email.send
memory.propose_candidate
evidence.generate_pack
```

`email.send` is the canonical high-risk MVP action and should be blocked or approval-gated.

MCP is supported later as an adapter, not as the core domain.

---

## 17. Policy Architecture

Policy must run at sensitive checkpoints.

Initial policy decision values:

```text
allow
deny
require_approval
sanitize
redact
escalate
defer
```

Policy Enforcement Points:

- gateway,
- runtime,
- memory retrieval,
- memory admission,
- tool broker,
- output release,
- evidence export.

Policy Decision Point:

- OPA/Rego adapter first,
- mock policy adapter for local tests,
- future adapter neutrality preserved.

Every policy decision should include:

```text
decision
reason
policy_id
policy_version when available
input hash when available
tenant_id
run_id when applicable
actor when applicable
timestamp
```

Failure mode rule:

> High-risk actions fail closed when policy is unavailable.

---

## 18. Evidence Architecture

Evidence is a first-class trust artifact.

Evidence is not the same as logs.

MVP target: **Evidence Level 2 — Operational Evidence**.

Evidence levels:

| Level | Name | Description |
|---|---|---|
| 0 | None | no evidence |
| 1 | Basic | run ID, input ref, output ref, timestamps |
| 2 | Operational | events, model calls, tool calls, policy decisions |
| 3 | Governance | approvals, memory refs, evals, redaction, outcomes |
| 4 | Audit-grade | hashes, signed exports, immutable retention |
| 5 | Regulated-grade | legal hold, WORM, strict retention, external attestations |

Evidence Pack should answer:

- Who requested the work?
- What was requested?
- Which agent/workflow ran?
- What memory/context was used?
- What policies were checked?
- What tools were proposed?
- What was allowed, denied, or approval-gated?
- What output was produced?
- What evals ran?
- What feedback was received?
- What outcome resulted?

---

## 19. Evaluation Architecture

Evals are promotion gates, not optional decoration.

MVP should include at least one eval case for the golden workflow.

Eval dimensions:

```text
task completion
policy compliance
tool correctness
memory correctness later
evidence completeness
usefulness
safety behavior
```

Future promotion gates should apply to:

- workflow versions,
- prompt versions,
- policy versions,
- tool manifest versions,
- agent versions,
- memory rules,
- eval packs.

---

## 20. Feedback and Learning Architecture

Feedback is structured data.

Feedback should be able to create:

- memory candidates,
- eval cases,
- failure classifications,
- improvement recommendations,
- policy suggestions,
- tool schema improvements,
- prompt regression cases.

The model does not rewrite itself automatically.

Learning flow:

```text
feedback
  -> classification
  -> recommendation or candidate
  -> human/developer review
  -> artifact change
  -> evals/tests
  -> promotion
```

---

## 21. Business Outcome Architecture

Aegis must connect AI work to business value.

Outcome records should distinguish:

```text
estimated
verified
```

Initial outcome examples:

```text
time_saved_minutes
draft_created
follow_up_created
risk_prevented
approval_required
eval_passed
human_feedback_score
```

Rule:

> No business-value claim without an outcome record.

---

## 22. Trust and Autonomy Model

Every workflow should eventually declare an autonomy level.

| Level | Name | Meaning |
|---|---|---|
| 0 | Observe Only | AI output is logged/evaluated but does not act |
| 1 | Draft Only | AI creates drafts/recommendations |
| 2 | Low-Risk Reversible Action | AI performs reversible low-risk actions |
| 3 | Approval-Gated Action | AI proposes consequential actions requiring approval |
| 4 | Policy-Bounded Autonomy | AI acts within strict policy limits |
| 5 | High Autonomy | AI acts in defined workflows with mature monitoring/rollback |
| 6 | Prohibited/Critical | AI cannot act autonomously |

MVP demonstrates Levels 1–3.

---

## 23. API Architecture

Aegis is API-first and headless.

Initial API resource model:

```text
/runs
/runs/{run_id}/events
/runs/{run_id}/evidence
/runs/{run_id}/feedback
/memories
/memory-candidates
/tools
/tool-calls
/policy-decisions
/approvals
/evals
/eval-runs
/outcomes
```

Write endpoints that can create side effects should support idempotency keys.

The Admin UI and SDKs should use the same APIs. No hidden business logic should live only in the UI.

---

## 24. Security and Tenant Architecture

Every tenant-owned record should include `tenant_id`.

Tenant scoping applies to:

- runs,
- memory,
- tools,
- policies,
- evidence,
- evals,
- feedback,
- outcomes,
- approvals,
- users,
- agents,
- workflows.

Security rules:

- secrets are never exposed to models,
- tool credentials are brokered by platform code,
- high-risk actions require policy and approval/denial,
- synthetic data only for MVP,
- no cross-tenant leakage,
- production logs must avoid sensitive payloads.

---

## 25. Observability Architecture

Aegis should use OpenTelemetry-compatible concepts.

Core correlation fields:

```text
trace_id
run_id
tenant_id
agent_id
workflow_id
model_call_id
tool_call_id
policy_decision_id
evidence_pack_id
```

Metrics should include:

```text
runs_started
runs_completed
runs_failed
run_latency
model_latency
tool_call_count
tool_denied_count
approval_required_count
policy_denied_count
memory_candidate_accept_rate
eval_pass_rate
evidence_completeness_score
feedback_negative_rate
outcome_time_saved
```

Trace-to-evidence linkage should become a v1 capability.

---

## 26. Deployment Modes

Aegis should support progressive hardening.

| Level | Mode | Description |
|---|---|---|
| 1 | Local governed demo | Docker/local, synthetic data, mock tools |
| 2 | Single-tenant pilot | isolated tenant, limited real integrations |
| 3 | Internal production | AIC uses Aegis for real internal workflows |
| 4 | Customer pilot | governed pilot with scoped data/tools |
| 5 | Multi-tenant SaaS | shared control plane with tenant isolation |
| 6 | Enterprise self-hosted | customer-owned deployment |
| 7 | Regulated-enterprise posture | strict retention, audit, legal hold, advanced controls |

MVP targets Level 1. v1 should move toward Levels 2–3.

---

## 27. Architecture Fitness Functions

The architecture must become testable.

Initial fitness functions include:

- every run has identity,
- every high-risk tool call has policy and approval/denial,
- every durable memory write has admission,
- every evidence pack references a run,
- every tenant-owned record has tenant scope,
- no model provider type leaks into domain,
- no OPA-specific object leaks into domain,
- no database row type leaks into domain,
- no secrets appear in model-visible context,
- golden workflow has eval coverage.

---

## 28. Non-Goals and Deferred Scope

Explicitly defer:

- full microservices,
- Kubernetes,
- marketplace,
- plugin registry,
- visual workflow builder,
- multi-agent swarm,
- fine-tuning,
- enterprise SSO,
- billing,
- full event sourcing,
- real customer data,
- formal compliance claims,
- large connector ecosystem.

These are not rejected. They are deferred until the core trust loop works.

---

## 29. Architecture Decision Implications

Future ADRs should formalize:

- Aegis is an AI Reliability Control Plane,
- Clean Architecture and Ports/Adapters,
- Domain-Driven Design and Ubiquitous Language,
- Event-Driven Architecture for auditability,
- Selective CQRS,
- MACH alignment without premature microservices,
- API + worker first,
- Postgres as canonical source of truth,
- governed memory,
- tool broker required,
- policy-as-code,
- evidence packs as first-class artifacts,
- evals as promotion gates,
- outcomes as first-class records,
- MCP as adapter, not core domain,
- local-first MVP and cloud-native v1.

---

## 30. Acceptance Criteria for WP-E0-003

This work packet is complete when the repo has a system overview that defines:

- the system purpose,
- architecture doctrine,
- system context,
- Clean Architecture layering,
- bounded contexts,
- seven planes,
- runtime loop,
- MVP golden workflow,
- MVP-A/MVP-B scope,
- CQRS/event posture,
- data architecture,
- memory architecture,
- tool governance architecture,
- policy architecture,
- evidence architecture,
- eval/feedback/outcome architecture,
- trust/autonomy model,
- API model,
- security/tenant model,
- observability model,
- deployment modes,
- deferred scope,
- next ADR implications.

---

## 31. Next Work Packets

Recommended next sequence:

1. WP-E0-004 — MVP System Boundaries
2. WP-E0-005 — Initial ADR Pack
3. WP-E0-006 — Threat Model Draft
4. WP-E0-007 — First Workflow Specification
5. WP-E1-001 — Run Envelope Schema

---

## 32. Final Summary

Aegis is a control plane for provable AI work.

It should not merely make agents run.

It should make AI work governable, observable, auditable, correctable, measurable, and improvable.

If Aegis cannot prove what happened, Aegis did not govern the work.
