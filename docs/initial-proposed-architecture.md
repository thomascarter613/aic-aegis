initial-proposed-architecture.md

**Aegis** as a **logical control-plane architecture** 
(not a premature microservices system)

The important distinction:

> **Design as services. Implement the MVP as a modular local-first runtime. Split into physical services only when the boundaries prove themselves.**

That keeps the architecture serious without making the MVP slow to build.

# Proposed Aegis Architecture

```text
┌──────────────────────────────────────────────────────────────┐
│                         Apps / Interfaces                    │
│                                                              │
│  Admin UI       Demo Console       SDKs       API Gateway     │
└──────────────────────────────┬───────────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────┐
│                  Aegis AgentOps Kernel / Runtime              │
│                                                              │
│  Run Envelope   State Machine   Event Log   Trace Context     │
└───────────────┬──────────────┬──────────────┬────────────────┘
                │              │              │
┌───────────────▼───┐ ┌────────▼────────┐ ┌───▼────────────────┐
│ Memory Plane      │ │ Policy Plane    │ │ Tool Governance     │
│                  │ │                 │ │ Plane               │
│ Memory records    │ │ OPA/Rego rules  │ │ Tool registry       │
│ Memory candidates │ │ Decisions       │ │ Tool broker         │
│ Admission gate    │ │ Checkpoints     │ │ Approval gates      │
│ Retrieval         │ │ Explanations    │ │ Mock/real executors │
└───────────────┬───┘ └────────┬────────┘ └───┬────────────────┘
                │              │              │
                └──────────────┼──────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────┐
│                    Evidence / Evals / Outcomes                │
│                                                              │
│  Evidence Packs   Eval Runner   Feedback   Business Outcomes  │
└──────────────────────────────┬───────────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────┐
│                    Persistence / Telemetry                    │
│                                                              │
│  Postgres + pgvector   Redis   Object Storage later   OTEL    │
└──────────────────────────────────────────────────────────────┘
```

The architecture has **seven logical planes**:

```text
1. Agent Runtime Plane
2. Memory Plane
3. Tool Governance Plane
4. Policy & Safety Plane
5. Evidence & Audit Plane
6. Evaluation Plane
7. Learning & Business Outcome Plane
```

But for the MVP, I would not deploy seven services unless necessary. I would start with a **single local runtime app** with clean internal modules.

---

# The Core Architectural Bet

Aegis should not be the agent.

Aegis should be the thing that wraps agents.

The core loop is:

```text
request
  -> create run envelope
  -> retrieve governed memory
  -> check policy
  -> call model
  -> receive proposed tool calls
  -> broker tool calls
  -> approve/block/execute
  -> generate evidence
  -> evaluate result
  -> collect feedback
  -> admit/reject memory updates
  -> record business outcome
```

That loop is the product.

Everything else exists to make that loop reliable.

---

# Recommended MVP Physical Architecture

For MVP, I propose this:

```text
apps/
  admin-ui/
  demo-console/

services/
  aegis-runtime/
    modules/
      gateway/
      runtime/
      memory/
      policy/
      tools/
      evidence/
      evals/
      feedback/
      outcomes/

packages/
  schemas/
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
```

Even if your repo currently has separate `services/runtime`, `services/memory`, etc., I would treat those as **logical service boundaries** first.

The first implementation can be one process:

```text
aegis-runtime
```

with internal modules.

Later, when needed, split into real services:

```text
gateway-service
runtime-service
memory-service
tool-broker-service
policy-service
evidence-service
eval-service
outcomes-service
```

This avoids overengineering while preserving clean future boundaries.

---

# Recommended Stack

For your specific goals, I would use:

| Layer            | Recommendation                                     |
| ---------------- | -------------------------------------------------- |
| Main MVP runtime | Python FastAPI or TypeScript/Bun                   |
| Admin UI         | TanStack Start or Next.js                          |
| Database         | PostgreSQL                                         |
| Vector retrieval | pgvector                                           |
| Queue/cache      | Redis                                              |
| Policy engine    | OPA/Rego                                           |
| Telemetry        | OpenTelemetry                                      |
| Evidence format  | JSON first, Markdown renderer second               |
| SDKs             | TypeScript first, Python second                    |
| Tool manifests   | YAML + JSON Schema                                 |
| Eval packs       | YAML + JSON Schema                                 |
| Local infra      | Docker Compose                                     |
| Model provider   | Mock provider first, real providers behind adapter |

My recommendation for the **first implementation language**:

> Use **TypeScript/Bun** for the MVP runtime if you want speed, repo consistency, admin UI integration, and SDK reuse.

Use Python later for evals, model experimentation, and ML/RAG-heavy workflows.

So the practical build would be:

```text
TypeScript/Bun:
  gateway
  runtime
  tool broker
  evidence generator
  SDK
  demo console

Python:
  eval runner later
  optional model/retrieval experiments later

Postgres:
  source of truth

OPA:
  policy decisions

Redis:
  queues and temporary workflow state
```

---

# Main Components

## 1. Gateway

Purpose:

```text
Receives external requests and starts governed AI runs.
```

Responsibilities:

```text
- validate request
- attach tenant/user/agent context
- create run request
- route to runtime
- expose API contracts
```

MVP endpoints:

```text
POST /runs
GET  /runs/:id
GET  /runs/:id/events
GET  /runs/:id/evidence
POST /runs/:id/feedback
```

---

## 2. Runtime Kernel

Purpose:

```text
The orchestrator for every AI workflow.
```

Responsibilities:

```text
- create Run Envelope
- manage Run State Machine
- append Run Events
- propagate trace_id
- call memory retrieval
- call policy checks
- call model provider
- route tool proposals to Tool Broker
- request evidence generation
- request evals
- record outcomes
```

The runtime should be boring and strict.

It should not “trust” the model. It should treat the model as one component inside a governed workflow.

---

## 3. Memory Service / Memory Module

Purpose:

```text
Reliable, governed AI memory.
```

Responsibilities:

```text
- store memory records
- store memory candidates
- retrieve memory under scope/policy
- run Memory Admission Gate
- record corrections
- expire/supersede memory
- expose memory references to evidence packs
```

Memory types:

```text
working
episodic
semantic
procedural
evaluative
```

Key rule:

> The model can propose memory. The platform decides whether memory is stored.

---

## 4. Policy Service

Purpose:

```text
Runtime policy decisions.
```

Responsibilities:

```text
- evaluate tool calls
- evaluate memory candidates
- evaluate output release
- evaluate context access
- return allow/deny/require_approval/redact/sanitize/escalate
- record policy decision with reason
```

MVP policy engine:

```text
OPA/Rego
```

Policy checkpoints:

```text
before memory retrieval
before model call
before tool call
before memory write
before output release
before evidence export
```

---

## 5. Tool Registry + Tool Broker

Purpose:

```text
Governed AI tool use.
```

Responsibilities:

```text
- register tool manifests
- expose allowed tools
- validate tool proposals
- validate tool input/output
- check policy
- require approval when needed
- execute safe tools
- block risky tools
- record tool evidence
```

Risk classes:

```text
read_only
low_write
medium_write
high_write
critical
```

MVP tool examples:

```text
crm.read_contact
crm.suggest_update
email.create_draft
email.send
memory.propose_candidate
evidence.generate_pack
```

Important rule:

> Agents never directly call tools. They submit Tool Proposals. The Tool Broker decides.

---

## 6. Evidence Service

Purpose:

```text
Generate proof of what happened.
```

Responsibilities:

```text
- gather run data
- gather memory refs
- gather policy decisions
- gather model call metadata
- gather tool calls
- gather approvals
- gather eval results
- gather outcomes
- produce Evidence Pack JSON
- produce Markdown evidence summary
```

Evidence Pack should answer:

```text
Who asked?
What was requested?
What agent ran?
What memory was used?
What policy applied?
What tools were proposed?
What was allowed or blocked?
What did the model produce?
What did humans approve?
What was evaluated?
What business outcome resulted?
```

This is a major differentiator.

---

## 7. Eval Service

Purpose:

```text
Measure whether the workflow worked.
```

Responsibilities:

```text
- load eval cases
- run workflow evals
- score outputs
- check policy compliance
- check tool correctness
- check memory correctness
- check evidence completeness
- store Eval Results
```

MVP eval dimensions:

```text
task completion
policy compliance
tool correctness
memory correctness
evidence completeness
usefulness
```

---

## 8. Feedback + Learning Loop

Purpose:

```text
Turn human corrections and failures into system improvements.
```

Responsibilities:

```text
- collect user rating
- collect correction
- link feedback to run/output
- propose memory candidates
- propose eval cases
- classify failures
- suggest improvements
```

Failure should flow into one of:

```text
memory correction
new eval case
policy update
tool schema update
prompt update
workflow constraint
```

---

## 9. Outcomes Service

Purpose:

```text
Connect AI activity to business value.
```

Responsibilities:

```text
- record business outcome events
- estimate time saved
- record risky action prevented
- record draft created
- record approval required
- connect outcome to run/evidence
```

MVP outcome metrics:

```text
time_saved_minutes
draft_created
risky_action_prevented
approval_required
follow_up_created
eval_passed
human_feedback_score
```

This is what makes Aegis useful for AIC as a business, not just as infrastructure.

---

# Database Architecture

Postgres is the canonical source of truth.

Core tables:

```text
tenants
users
agents
agent_versions

runs
run_events
model_calls

memories
memory_candidates
memory_events
memory_feedback

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
```

Use `pgvector` for semantic retrieval, but do not make the vector DB the truth layer.

The canonical rule:

> Postgres stores truth. Vectors help find truth.

---

# Event Architecture

Aegis should be event-rich from the start.

Every important thing should produce a `RunEvent`.

Example event stream:

```text
run.created
policy.checked
memory.retrieved
model.called
tool.proposed
tool.policy_checked
tool.approval_required
tool.denied
evidence.generated
eval.completed
feedback.received
memory.candidate_proposed
outcome.recorded
run.completed
```

This gives you:

```text
debugging
replay
evidence generation
UI timeline
eval context
auditing
future analytics
```

The event log is one of the core assets of the system.

---

# Control Flow for the First Demo

The first demo should be **Governed Sales/Ops Assistant**.

```text
1. User submits customer conversation.
2. Gateway validates request.
3. Runtime creates Run Envelope.
4. Runtime appends run.created.
5. Memory module retrieves allowed customer memories.
6. Policy checks whether memory/context can be used.
7. Runtime calls model provider.
8. Model returns:
   - summary
   - recommendations
   - proposed CRM update
   - proposed email draft
   - proposed email send
9. Tool Broker validates proposals.
10. Policy allows CRM read.
11. Policy allows email draft creation.
12. Policy blocks or requires approval for email send.
13. Evidence Pack is generated.
14. Eval runner scores result.
15. User gives feedback.
16. Memory candidate is proposed.
17. Memory Admission Gate accepts/rejects/queues it.
18. Outcome event records time saved and risky action prevented.
19. Run completes.
```

That demo proves the whole architecture.

---

# What I Would Not Build Yet

I would avoid these in the MVP:

```text
full microservice deployment
Kubernetes
enterprise SSO
billing
marketplace
visual workflow builder
multi-agent swarm UI
fine-tuning
complex connector ecosystem
production MCP server marketplace
autonomous browser agents
real customer data ingestion
HIPAA/PCI workflows
```

Those can come later.

The MVP should prove the control loop.

---

# Architectural Decisions I’m Proposing

These should become ADRs:

```text
ADR-0001: Aegis is an AI Reliability Control Plane, not a chatbot or agent framework.
ADR-0002: MVP is local-first.
ADR-0003: MVP is logically service-oriented but physically modular.
ADR-0004: PostgreSQL is the canonical source of truth.
ADR-0005: pgvector is the initial semantic retrieval layer.
ADR-0006: Tool calls must go through Tool Broker.
ADR-0007: Memory writes must pass through Memory Admission Gate.
ADR-0008: Runtime policy checks are required for sensitive actions.
ADR-0009: Evidence Packs are first-class artifacts.
ADR-0010: Eval results are part of workflow promotion.
ADR-0011: Business outcomes are tracked as first-class records.
ADR-0012: Mock model provider is required for local development.
ADR-0013: Aegis is provider-agnostic.
ADR-0014: Run Events are the canonical execution history.
ADR-0015: High-risk actions require approval or are blocked by default.
```

---

# The Architecture in One Sentence

> Aegis is a local-first, provider-agnostic AI Reliability Control Plane whose runtime wraps every AI workflow in a run envelope, retrieves governed memory, enforces policy, brokers tool calls, records events, generates evidence, runs evals, captures feedback, and measures business outcomes.

That is what I would put into **WP-E0-003 — Architecture Overview** unless you want to change direction first.
