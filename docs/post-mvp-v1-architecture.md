My expectation for **post-MVP v1** is:

> **Aegis v1 becomes a production-capable AI Reliability Control Plane, not just a local demo runtime.**

The MVP proves the loop.
v1 makes the loop deployable, multi-tenant, observable, governable, secure, and extensible.

The v1 architecture should still avoid “enterprise bloat,” but it should be strong enough that AIC could use it for real consulting delivery, internal operations, and early customer pilots.

---

# MVP vs Post-MVP v1

| Layer    | MVP                          | Post-MVP v1                                                |
| -------- | ---------------------------- | ---------------------------------------------------------- |
| Runtime  | modular local app            | production runtime service with durable execution          |
| Tenancy  | demo tenant                  | real tenant isolation                                      |
| Auth     | placeholder                  | auth, RBAC, service tokens                                 |
| Memory   | Postgres + pgvector baseline | governed memory service with review, correction, lifecycle |
| Tools    | mock tools + manifests       | Tool Broker with native tools, MCP adapter, approvals      |
| Policy   | base OPA/Rego policies       | policy bundles, tenant overrides, policy tests             |
| Evidence | JSON/Markdown evidence pack  | evidence store, redaction, export, integrity strategy      |
| Evals    | simple eval runner           | offline + online evals, regression gates, review queue     |
| Feedback | basic feedback capture       | feedback-to-memory and feedback-to-eval loops              |
| Outcomes | basic outcome event          | KPI dashboard and workflow ROI summaries                   |
| UI       | demo console / basic admin   | real admin console                                         |
| Infra    | Docker Compose               | deployable stack, CI/CD, migrations, telemetry             |
| SDKs     | starter SDKs                 | usable TypeScript/Python SDKs                              |

---

# The v1 Architecture in One Sentence

> Aegis v1 should be a multi-tenant, event-driven, policy-enforced AI reliability platform where every AI workflow runs through a durable runtime, governed memory layer, tool broker, policy engine, evidence system, eval system, feedback loop, and outcome analytics layer.

---

# Proposed v1 Architecture

```text id="tfh2m6"
┌────────────────────────────────────────────────────────────────────┐
│                           Client Layer                             │
│                                                                    │
│  Admin UI     Demo Apps     Customer Apps     SDKs     Webhooks     │
└───────────────────────────────┬────────────────────────────────────┘
                                │
┌───────────────────────────────▼────────────────────────────────────┐
│                         API / Edge Layer                            │
│                                                                    │
│  API Gateway     Auth     RBAC     Rate Limits     Tenant Context   │
└───────────────────────────────┬────────────────────────────────────┘
                                │
┌───────────────────────────────▼────────────────────────────────────┐
│                       Aegis Runtime Plane                           │
│                                                                    │
│  Run Orchestrator   Run State Machine   Durable Workflows           │
│  Event Recorder     Trace Context       Model Adapter Layer         │
└──────────────┬────────────────┬─────────────────┬─────────────────┘
               │                │                 │
┌──────────────▼──────┐ ┌───────▼─────────┐ ┌─────▼──────────────────┐
│ Memory Plane        │ │ Policy Plane    │ │ Tool Governance Plane   │
│                     │ │                 │ │                        │
│ Memory Service      │ │ OPA/Rego        │ │ Tool Broker             │
│ Memory Candidates   │ │ Policy Bundles  │ │ Tool Registry           │
│ Admission Gate      │ │ PDP/PEP Model   │ │ Approval Gates          │
│ Retrieval           │ │ Decision Store  │ │ MCP / Native Adapters   │
└──────────────┬──────┘ └───────┬─────────┘ └─────┬──────────────────┘
               │                │                 │
               └────────────────┼─────────────────┘
                                │
┌───────────────────────────────▼────────────────────────────────────┐
│                 Evidence / Evals / Feedback / Outcomes              │
│                                                                    │
│ Evidence Service   Eval Service   Review Queue   Outcomes Service  │
│ Feedback Service   Redaction      Regression     KPI Summaries      │
└───────────────────────────────┬────────────────────────────────────┘
                                │
┌───────────────────────────────▼────────────────────────────────────┐
│                         Data & Telemetry Layer                      │
│                                                                    │
│ Postgres   pgvector   Redis/Queue   Object Store   OTEL Collector   │
│ Event Log  Audit Log  Policy Store  Eval Store     Metrics/Traces   │
└────────────────────────────────────────────────────────────────────┘
```

---

# v1 Should Have 10 Major Subsystems

## 1. API / Edge Layer

The v1 platform needs a real edge layer.

Responsibilities:

```text id="qgvlyl"
- API gateway
- auth
- tenant resolution
- RBAC
- request validation
- rate limiting
- API keys / service tokens
- webhook ingress
- SDK ingress
```

Minimum v1 endpoints:

```text id="d4gm3y"
POST /runs
GET  /runs/:id
GET  /runs/:id/events
GET  /runs/:id/evidence
POST /runs/:id/feedback

GET  /memories
POST /memory-candidates
POST /memory-candidates/:id/review

GET  /tools
POST /tool-proposals
POST /approvals/:id/decision

GET  /evals
POST /eval-runs

GET  /outcomes
GET  /dashboards/overview
```

The gateway should not contain the intelligence. It should enforce identity, tenancy, request shape, and routing.

---

## 2. Runtime Orchestrator

The runtime becomes the center of v1.

MVP runtime can be simple. v1 runtime needs durable execution semantics.

Responsibilities:

```text id="8bw5qc"
- create Run Envelope
- enforce Run State Machine
- append Run Events
- coordinate model calls
- coordinate memory retrieval
- coordinate policy checks
- route tool proposals
- pause for approvals
- resume after approvals
- handle retries and failure states
- request evidence generation
- request eval execution
- record final outcome
```

The v1 runtime should support these states:

```text id="o7z2ra"
created
queued
running
waiting_for_approval
waiting_for_tool
waiting_for_human_review
completed
failed
cancelled
expired
```

MVP can fake this with simple function calls. v1 should have real resumability.

I would design for this eventual runtime model:

```text id="d0gpd6"
Run Request
  -> durable workflow/job
  -> event stream
  -> state machine
  -> resumable approval waits
  -> evidence generation
  -> eval/outcome post-processing
```

---

## 3. Event Backbone

v1 needs an event backbone.

Not necessarily Kafka yet. But it needs event discipline.

Minimum v1 pattern:

```text id="dbu2i9"
Postgres transaction
  -> write domain record
  -> write outbox event
  -> background dispatcher
  -> async consumers
```

Use this for:

```text id="4z2877"
run.created
memory.retrieved
policy.checked
tool.proposed
tool.allowed
tool.denied
approval.requested
evidence.generated
eval.completed
feedback.received
outcome.recorded
```

Postgres can be enough for v1. Kafka/NATS/Redpanda can come later.

The important part is the **event model**, not the broker.

---

## 4. Memory Service

In v1, Memory becomes a real product subsystem.

Responsibilities:

```text id="ip20j1"
- memory records
- memory candidates
- Memory Admission Gate
- memory review queue
- memory correction
- memory supersession
- memory expiration
- memory sensitivity classification
- memory provenance
- governed retrieval
- semantic retrieval with pgvector
```

The memory system should support five memory types:

```text id="ppzcsu"
working
episodic
semantic
procedural
evaluative
```

The most important v1 distinction:

```text id="k4h26x"
Memory Candidate != Memory Record
```

The AI may propose memory. Aegis decides whether to store it.

v1 memory flow:

```text id="f2s6c8"
candidate proposed
  -> policy check
  -> confidence scoring
  -> sensitivity classification
  -> duplicate/supersession check
  -> accept / reject / queue for review
  -> evidence record
```

Postgres should remain canonical. pgvector supports semantic retrieval, but vector search should not become the source of truth.

---

## 5. Tool Governance Plane

v1 needs the Tool Broker to become a real enforcement point.

Responsibilities:

```text id="q3qzdo"
- tool registry
- tool manifests
- tool proposal validation
- input schema validation
- output schema validation
- policy check
- risk classification
- approval gate
- credential brokering
- execution sandboxing where possible
- result filtering/redaction
- tool call audit
```

Tool risk classes:

```text id="tq8f6o"
read_only
low_write
medium_write
high_write
critical
```

v1 should support both:

```text id="5xl8ya"
native Aegis tools
MCP-compatible tools
```

MCP is relevant because it provides a standard way for AI applications to connect to external tools and context, and the current MCP specification explicitly includes user consent expectations around tool invocation. ([Model Context Protocol][1])

But Aegis should not blindly expose MCP tools to agents.

v1 rule:

> MCP tools enter through the Tool Broker, not directly into the model.

That means:

```text id="5jmcag"
MCP server
  -> Aegis MCP adapter
  -> Tool Registry
  -> Tool Broker
  -> Policy check
  -> Approval gate
  -> Tool execution
  -> Evidence Pack
```

---

## 6. Policy & Safety Engine

v1 should make policy a real runtime dependency.

Use OPA/Rego as the first policy engine. OPA is a general-purpose policy engine intended to unify policy enforcement across the stack, and Rego is its declarative policy language for reasoning over structured inputs. ([Open Policy Agent][2])

v1 policy layers:

```text id="rnq2ks"
global platform policies
tenant policies
workflow policies
agent policies
tool policies
memory policies
output policies
evidence export policies
```

v1 policy architecture:

```text id="p2nv9x"
Policy Enforcement Points:
  gateway
  runtime
  memory service
  tool broker
  evidence exporter

Policy Decision Point:
  policy service / OPA

Policy Store:
  versioned policy bundles
```

Policy decisions should always persist:

```text id="mq1fyh"
decision
reason
policy_id
policy_version
input_hash
run_id
trace_id
actor
timestamp
```

v1 should support policy decisions:

```text id="r6o6w4"
allow
deny
require_approval
sanitize
redact
escalate
defer
```

---

## 7. Evidence & Audit Service

Evidence becomes one of the core v1 moats.

v1 Evidence Service responsibilities:

```text id="f4tlgz"
- collect run references
- collect memory references
- collect model call records
- collect tool call records
- collect policy decisions
- collect approvals
- collect eval results
- collect outcome events
- apply redaction rules
- generate JSON Evidence Pack
- generate Markdown report
- support export
- support evidence completeness scoring
```

v1 should produce two evidence artifacts:

```text id="g5lap3"
machine-readable evidence JSON
human-readable evidence report
```

The Evidence Pack should become the thing AIC can show a client:

> “Here is what the AI did, what it used, what it was allowed to do, what was blocked, what humans approved, how it scored, and what outcome resulted.”

That is a real business differentiator.

---

## 8. Eval Service

v1 should elevate evals from a test helper to a platform capability.

Responsibilities:

```text id="cq1wdj"
- store eval cases
- organize eval packs
- run evals against workflows
- score outputs
- evaluate tool correctness
- evaluate memory correctness
- evaluate policy compliance
- evaluate evidence completeness
- run regression checks
- store eval results
- attach evals to evidence
```

v1 eval types:

```text id="sav2v5"
offline evals
online evals
regression evals
red-team evals
human-review evals
```

The eval system should become part of workflow promotion:

```text id="htl2xs"
new prompt / tool / policy / workflow version
  -> run eval pack
  -> compare to baseline
  -> pass/fail gate
  -> promote or reject
```

---

## 9. Feedback & Review System

v1 needs a review queue.

The MVP can simply record feedback. v1 should route feedback into action.

Review queue item types:

```text id="8iygbc"
memory_candidate_review
approval_request
policy_exception_review
eval_failure_review
evidence_redaction_review
tool_failure_review
user_correction_review
```

Feedback flows:

```text id="o4lioz"
thumbs down -> failure classification
correction -> memory candidate
bad output -> eval case
unsafe proposal -> policy update suggestion
bad tool call -> tool schema update suggestion
missing proof -> evidence template update
```

This is where Aegis starts “learning” without pretending the model self-improves magically.

---

## 10. Business Outcome Service

v1 should make business value visible.

Responsibilities:

```text id="8t794o"
- record outcome events
- estimate time saved
- track risk prevented
- track approval burden
- track output usefulness
- connect runs to workflow KPIs
- generate outcome summaries
- power dashboards
```

v1 outcome model:

```text id="zpuhae"
run_id
workflow_id
tenant_id
metric_name
metric_value
unit
baseline_value
estimated
verified
source
notes
created_at
```

Example outcome metrics:

```text id="d37jpo"
time_saved_minutes
draft_created
follow_up_created
risky_action_prevented
approval_required
approval_granted
manual_review_required
eval_passed
customer_response_time_reduced
```

This makes Aegis commercially useful.

---

# v1 Data Architecture

Postgres remains canonical.

```text id="fm2vit"
Postgres:
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
  outbox_events
```

Add object storage for large artifacts:

```text id="2f145i"
object storage:
  evidence exports
  uploaded files
  model input/output snapshots when allowed
  redacted reports
  eval datasets
```

Add Redis or equivalent for:

```text id="q1h1b5"
queues
locks
temporary state
approval wait notifications
rate limits
```

Add pgvector for:

```text id="cv53jo"
semantic memory search
document chunk search
eval case similarity search
failure pattern similarity
```

Optional later:

```text id="kpa0y1"
Qdrant for retrieval acceleration
ClickHouse for analytics-heavy event queries
S3/MinIO for evidence/object storage
NATS/Kafka/Redpanda for higher-scale event streaming
```

But for v1, Postgres + pgvector + Redis + object storage is enough.

---

# v1 Service Architecture

I would expect v1 to have **logical services** that can run either:

1. as modules in one deployment, or
2. as separate services.

Recommended v1 physical compromise:

```text id="gv816f"
1. aegis-api
2. aegis-worker
3. aegis-admin-ui
4. postgres
5. redis
6. opa
7. otel-collector
8. object-storage
```

Where `aegis-api` contains:

```text id="ui9u4q"
gateway
auth middleware
run APIs
memory APIs
tool APIs
policy APIs
evidence APIs
eval APIs
outcome APIs
```

And `aegis-worker` handles:

```text id="vf5xxw"
async run execution
tool execution
evidence generation
eval runs
feedback processing
outbox dispatch
notifications
```

This is cleaner than deploying eight services too early.

Later, split if needed:

```text id="2my7sf"
aegis-runtime-service
aegis-memory-service
aegis-tool-broker-service
aegis-policy-service
aegis-evidence-service
aegis-eval-service
aegis-outcome-service
```

But v1 does not need that much operational complexity.

---

# v1 Deployment Architecture

For v1, I would support three deployment modes.

## 1. Local Developer Mode

```text id="kzb9uu"
Docker Compose
Postgres
Redis
OPA
OTEL Collector
MinIO optional
mock model provider
```

Purpose:

```text id="ia4sbw"
development
demos
tests
consulting pilots
```

## 2. Single-Tenant Pilot Mode

```text id="6mn5jk"
one customer
one deployment
isolated database or schema
managed Postgres
managed Redis
containerized API/worker/UI
```

Purpose:

```text id="ev7zbu"
paid pilots
AIC consulting delivery
early production validation
```

## 3. Multi-Tenant SaaS Mode

```text id="ycft1d"
shared control plane
tenant isolation
RBAC
billing later
usage tracking
tenant policy bundles
tenant evidence boundaries
```

Purpose:

```text id="6tuo5n"
early SaaS
repeatable SMB deployments
platform business
```

For v1, I would prioritize **single-tenant pilot mode** before full multi-tenant SaaS.

---

# v1 Tenant Isolation Model

At v1, I would implement tenant isolation at the application and database level.

Minimum:

```text id="iy9g3y"
every table has tenant_id
all queries are tenant-scoped
all run events are tenant-scoped
all memory retrieval is tenant-scoped
all evidence is tenant-scoped
all tool credentials are tenant-scoped
```

Better v1:

```text id="w8d1ie"
Postgres Row-Level Security for tenant-owned records
tenant-specific encryption keys later
tenant-specific policy bundles
tenant-specific tool credentials
tenant-specific evidence export controls
```

Do not let tenant scoping be an afterthought.

---

# v1 Observability Architecture

Aegis should use OpenTelemetry from v1.

OpenTelemetry has GenAI semantic conventions for spans, metrics, events, and attributes around generative AI systems, so Aegis should align its model calls, tool calls, evals, and agent workflow traces with that direction rather than inventing isolated telemetry. ([OpenTelemetry][3])

v1 observability should include:

```text id="cop2tw"
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

Metrics:

```text id="ceir97"
runs_started
runs_completed
runs_failed
approval_required_count
tool_denied_count
policy_denied_count
eval_pass_rate
evidence_completeness_score
memory_candidate_accept_rate
cost_per_run
latency_per_run
time_saved_estimate
```

Logs:

```text id="u8q1ee"
structured JSON logs
correlation IDs
no secrets
redacted sensitive payloads
```

Traces:

```text id="9rw56n"
gateway request
runtime orchestration
memory retrieval
policy check
model call
tool broker decision
tool execution
evidence generation
eval run
outcome recording
```

---

# v1 Security Architecture

Security becomes central in v1.

Minimum v1 security controls:

```text id="d0kkhl"
auth
RBAC
tenant scoping
service tokens
secret manager integration
tool credential boundary
policy enforcement
approval gates
audit trail
redaction
rate limits
egress controls for tool execution
```

Credential rule:

> Models never see credentials.

Tool execution flow:

```text id="7zqtz7"
agent proposes tool call
  -> Tool Broker validates
  -> Policy decides
  -> approval if needed
  -> platform injects scoped credential
  -> tool executes
  -> result is filtered
  -> evidence is recorded
```

For MCP specifically, I would treat every MCP tool server as an untrusted integration until registered, permissioned, policy-checked, and evidence-wrapped. MCP is valuable as an integration standard, but Aegis’s value is controlling and auditing those capabilities, not merely exposing them. MCP’s authorization specification for HTTP transports centers on authorization flows for restricted servers, which fits Aegis’s brokered access model. ([Model Context Protocol][4])

---

# v1 Admin UI

The v1 admin UI should not be a giant workflow builder yet.

It should be an **inspection and control UI**.

Pages:

```text id="xj2xs1"
Dashboard
Runs
Run Detail
Evidence Pack Viewer
Memory Records
Memory Candidate Review
Tool Registry
Tool Call Detail
Policy Decisions
Approval Queue
Eval Runs
Eval Results
Feedback Queue
Business Outcomes
Settings
```

Most important v1 screens:

```text id="j1mwkg"
Run Timeline
Evidence Pack Viewer
Approval Queue
Memory Candidate Review
Eval Result Viewer
Outcome Summary
```

The v1 UI should make the product obvious:

> Here is what the AI did, what it used, what was blocked, what was approved, how it scored, and what business value resulted.

---

# v1 SDK Architecture

SDKs should make it easy to wrap external workflows.

TypeScript SDK first:

```text id="ahll10"
createRun()
appendEvent()
submitToolProposal()
recordModelCall()
submitMemoryCandidate()
generateEvidence()
submitFeedback()
recordOutcome()
```

Python SDK second:

```text id="azmy0h"
agent integration
eval runner integration
RAG/memory integration
model provider adapters
```

The SDKs should not hide governance. They should make governance easy.

---

# v1 Integration Architecture

v1 should support three integration styles.

## 1. Wrapped workflow

Existing app calls Aegis before/after model/tool actions.

```text id="sl6ua0"
external app
  -> Aegis SDK
  -> Aegis run/evidence/policy APIs
```

## 2. Aegis-orchestrated workflow

Aegis owns the whole workflow.

```text id="a0rf66"
user request
  -> Aegis runtime
  -> model/tools/policy/evidence/evals
```

## 3. Tool-broker-only mode

A customer uses Aegis only to govern tool calls.

```text id="dwaebe"
agent framework
  -> Aegis Tool Broker
  -> policy/evidence/approval
```

This is commercially important because many teams may already have agents.

Aegis should wrap them rather than force them to rewrite everything.

---

# v1 Should Support External Agent Frameworks

I would expect v1 to support agent-framework neutrality.

Aegis should be able to wrap:

```text id="rqit96"
custom agent code
OpenAI Agents SDK-style workflows
LangGraph-style workflows
CrewAI-style workflows
MCP-based tool ecosystems
plain API workflows
```

The exact adapters can come incrementally.

LangGraph’s persistence docs distinguish short-term memory through checkpointers and long-term memory through stores, which is conceptually aligned with Aegis’s separation between run state and durable governed memory. ([LangChain Docs][5])

Aegis should treat those frameworks as execution clients or adapters, not as the source of truth for governance.

---

# v1 Architecture by Repository Shape

I would expect the repo to evolve toward this:

```text id="1yowuz"
apps/
  admin-ui/
  demo-console/

services/
  aegis-api/
  aegis-worker/

packages/
  core/
  runtime/
  memory/
  tools/
  policy/
  evidence/
  evals/
  feedback/
  outcomes/
  schemas/
  sdk-ts/
  sdk-python/
  policy-packs/
  tool-packs/
  eval-packs/
  prompt-packs/
  adapters/
    model-providers/
    mcp/
    langgraph/
    openai-agents/
    crm/
    email/

contracts/
  openapi/
  events/
  asyncapi/

db/
  migrations/
  seeds/

infra/
  docker-compose/
  terraform/
  helm-later/
  otel/
  opa/
  postgres/
  redis/
  minio/

docs/
  product/
  architecture/
  adrs/
  planning/
  security/
  operations/
  evals/
  evidence/
```

I would avoid too many separate service folders until v1 proves runtime load and boundaries.

---

# Recommended v1 Technology Stack

My recommended v1 stack:

| Layer               | Choice                               |
| ------------------- | ------------------------------------ |
| API / runtime       | TypeScript + Bun                     |
| Worker              | TypeScript + Bun initially           |
| Admin UI            | TanStack Start or Next.js            |
| Database            | PostgreSQL                           |
| Semantic search     | pgvector                             |
| Queue/cache         | Redis                                |
| Policy              | OPA/Rego                             |
| Evidence storage    | Postgres + object storage            |
| Object storage      | MinIO locally, S3-compatible later   |
| Telemetry           | OpenTelemetry                        |
| SDKs                | TypeScript + Python                  |
| Tool manifests      | YAML + JSON Schema                   |
| Evals               | YAML + JSON Schema + runner          |
| Local deployment    | Docker Compose                       |
| Pilot deployment    | Containers + managed Postgres/Redis  |
| Later orchestration | Kubernetes/Nomad only when justified |

Why TypeScript/Bun first?

Because v1 needs:

```text id="ah2noi"
API
SDK
UI
schemas
tool broker
runtime
developer velocity
```

Python remains useful for:

```text id="23pvu7"
eval experiments
RAG experiments
ML-heavy components
model-provider integrations
notebooks
```

---

# v1 Critical Path

The post-MVP v1 critical path should be:

```text id="2x8jr7"
1. Harden Run Envelope and Run Events.
2. Add real auth and tenant context.
3. Build durable runtime worker.
4. Implement Memory Candidate review.
5. Implement Tool Broker with approval queue.
6. Implement OPA-backed policy service.
7. Implement Evidence Pack store and viewer.
8. Implement Eval Runner with regression packs.
9. Implement Feedback-to-memory and feedback-to-eval flows.
10. Implement Business Outcome dashboard.
11. Add SDK wrappers.
12. Add deployable single-tenant pilot mode.
```

That gives you a real v1.

---

# What v1 Should Not Be Yet

v1 should still not be:

```text id="5ji1fb"
a giant enterprise SaaS
a no-code workflow builder
a marketplace
a full agent framework
a Kubernetes platform
a replacement for every agent library
a compliance certification product
a massive connector marketplace
a fully autonomous business operating system
```

v1 should be:

```text id="bhu4bu"
a production-capable reliability layer
a governed runtime
a memory admission system
a tool broker
a policy enforcement layer
an evidence generator
an eval/feedback loop
an outcome measurement system
```

---

# My Expected v1 Milestones

## V1-M1 — Production Runtime

```text id="7n8q5f"
durable run execution
state machine
event backbone
worker model
retries
approval waits
```

## V1-M2 — Real Governance

```text id="tch6l5"
tenant policies
tool policies
memory policies
output policies
OPA bundles
policy decision store
```

## V1-M3 — Reliable Memory

```text id="7xkjwo"
memory candidates
review queue
correction
supersession
retrieval
provenance
poisoning tests
```

## V1-M4 — Tool Broker

```text id="8nb6g4"
native tools
MCP adapter
tool manifests
risk classes
approval gates
result filtering
tool evidence
```

## V1-M5 — Evidence + Evals

```text id="qo7gah"
evidence store
evidence viewer
redaction
eval runner
regression gates
red-team seeds
```

## V1-M6 — Feedback + Outcomes

```text id="5ry8lb"
feedback capture
review queue
failure taxonomy
memory/eval suggestions
outcome metrics
dashboard
```

## V1-M7 — Pilot Deployment

```text id="xtjqsf"
auth
tenant isolation
CI/CD
migrations
observability
backup/restore
single-tenant deployment
```

---

# The Big v1 Shift

The MVP proves:

```text id="y03y4l"
Aegis can govern one AI workflow.
```

v1 proves:

```text id="4dvtx9"
Aegis can govern many AI workflows for a real tenant with real evidence, real policy, real approvals, real evals, real feedback, and real outcome reporting.
```

That is the difference.

---

# Final Recommendation

My expected post-MVP v1 architecture is:

```text id="czx3k6"
A hosted or self-hosted AI Reliability Control Plane with:

- API gateway
- auth/RBAC/tenant isolation
- durable runtime worker
- run event backbone
- governed memory service
- tool broker with MCP/native adapters
- OPA-backed policy service
- approval and review queues
- evidence pack service
- eval service
- feedback learning loop
- business outcome analytics
- admin UI
- TypeScript/Python SDKs
- Postgres/pgvector canonical data layer
- Redis queue/cache
- object storage
- OpenTelemetry observability
```

The guiding principle should remain:

> **Aegis governs AI work. It does not merely run AI work.**

[1]: https://modelcontextprotocol.io/specification/2025-06-18?utm_source=chatgpt.com "Specification"
[2]: https://openpolicyagent.org/docs?utm_source=chatgpt.com "Open Policy Agent (OPA)"
[3]: https://opentelemetry.io/docs/specs/semconv/gen-ai/?utm_source=chatgpt.com "Semantic conventions for generative AI systems"
[4]: https://modelcontextprotocol.io/specification/draft/basic/authorization?utm_source=chatgpt.com "Authorization"
[5]: https://docs.langchain.com/oss/python/langgraph/persistence?utm_source=chatgpt.com "Persistence - Docs by LangChain"
