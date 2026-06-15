Yes — **the proposed Aegis architecture is compatible with Clean Architecture**, but I would phrase it more precisely:

> **Aegis should be a Clean Architecture system with a control-plane/domain-core at the center, surrounded by adapters for models, tools, policy engines, databases, UIs, SDKs, queues, telemetry, and external systems.**

Right now, what I’ve proposed is **clean-architecture-shaped**, but we should explicitly formalize it that way in WP-E0-003 and the ADRs.

# Clean Architecture Fit

Clean Architecture says your core business rules should not depend on frameworks, databases, UI, APIs, or vendors.

For Aegis, the core business rules are things like:

```text
A run must have identity.
A tool proposal must go through the Tool Broker.
A memory candidate must pass admission before becoming durable memory.
A policy decision must be recorded.
A high-risk tool call must require approval or be blocked.
An evidence pack must reference the events, policies, memory, tools, evals, and outcomes used in a run.
```

Those rules should live in the **domain/application core**, not in FastAPI, Bun, Postgres, OPA, Redis, LangGraph, MCP, OpenAI, or the admin UI.

So yes: Aegis should absolutely use Clean Architecture.

---

# How I Would Map Aegis to Clean Architecture

```text
┌──────────────────────────────────────────────────────────────┐
│ External Interfaces                                           │
│ Admin UI, CLI, SDKs, Webhooks, REST API                       │
└───────────────────────────┬──────────────────────────────────┘
                            │
┌───────────────────────────▼──────────────────────────────────┐
│ Interface Adapters                                            │
│ Controllers, Presenters, Repositories, Provider Adapters       │
│ Model adapters, Tool adapters, OPA adapter, DB repositories    │
└───────────────────────────┬──────────────────────────────────┘
                            │
┌───────────────────────────▼──────────────────────────────────┐
│ Application Use Cases                                         │
│ CreateRun, RetrieveMemory, ProposeToolCall, BrokerToolCall,    │
│ AdmitMemoryCandidate, GenerateEvidencePack, RunEval,           │
│ CaptureFeedback, RecordOutcome                                │
└───────────────────────────┬──────────────────────────────────┘
                            │
┌───────────────────────────▼──────────────────────────────────┐
│ Domain Core                                                   │
│ Run, RunEnvelope, RunEvent, MemoryCandidate, MemoryRecord,     │
│ ToolManifest, ToolProposal, ToolCall, PolicyDecision,          │
│ EvidencePack, EvalResult, FeedbackRecord, BusinessOutcome      │
└──────────────────────────────────────────────────────────────┘
```

The dependency rule should be:

```text
UI/API/DB/OPA/LLM/tools depend inward on Aegis core.
Aegis core does not depend outward on UI/API/DB/OPA/LLM/tools.
```

---

# The Aegis Clean Architecture Layers

## 1. Domain Layer

This is the heart of Aegis.

Contains entities/value objects like:

```text
Run
RunEnvelope
RunEvent
Agent
AgentVersion
MemoryRecord
MemoryCandidate
MemoryAdmissionDecision
ToolManifest
ToolProposal
ToolCall
PolicyDecision
ApprovalRequest
ApprovalDecision
EvidencePack
EvalCase
EvalResult
FeedbackRecord
BusinessOutcome
```

Contains domain rules like:

```text
A high-risk tool proposal cannot execute without approval.
A memory candidate cannot become durable memory without admission.
A run cannot complete without final status.
A policy decision must include a reason.
An evidence pack must reference its run.
```

This layer should have **zero dependency** on:

```text
Postgres
Redis
OPA
OpenAI
MCP
FastAPI
Bun
React
Docker
GitHub
```

---

## 2. Application / Use Case Layer

This layer coordinates domain behavior.

Use cases:

```text
CreateRun
StartRun
AppendRunEvent
RetrieveGovernedMemory
ProposeMemoryCandidate
AdmitMemoryCandidate
ProposeToolCall
BrokerToolCall
RequestApproval
RecordPolicyDecision
GenerateEvidencePack
RunEvaluation
CaptureFeedback
RecordBusinessOutcome
CompleteRun
FailRun
```

The use case layer can define ports/interfaces such as:

```text
RunRepository
MemoryRepository
ToolRegistry
PolicyDecisionPort
ModelProviderPort
ToolExecutorPort
EvidenceStore
EvalRunnerPort
OutcomeRepository
EventPublisher
TelemetryPort
```

But it should not know the concrete implementation.

So instead of:

```ts
const rows = await postgres.query(...)
```

the use case should say:

```ts
await runRepository.save(run)
```

Instead of:

```ts
await opa.evaluate(...)
```

the use case should say:

```ts
await policyPort.decide(input)
```

Instead of:

```ts
await openai.chat.completions.create(...)
```

the use case should say:

```ts
await modelProvider.generate(request)
```

---

## 3. Interface Adapter Layer

This layer translates between the outside world and the core.

Adapters include:

```text
REST controllers
SDK handlers
CLI commands
database repositories
OPA policy adapter
model provider adapters
MCP adapter
tool executor adapters
queue workers
OpenTelemetry adapter
evidence renderers
```

Example:

```text
HTTP POST /runs
  -> controller validates request
  -> maps request DTO to CreateRun command
  -> calls CreateRun use case
  -> maps result to HTTP response
```

The controller should not contain business rules.

---

## 4. Infrastructure Layer

This is the replaceable outer ring.

Contains:

```text
PostgreSQL
pgvector
Redis
OPA
OpenTelemetry
MinIO/S3
Docker Compose
GitHub Actions
model providers
MCP servers
CRM/email APIs
object storage
queue system
```

Infrastructure is important, but it is not the architecture’s center.

---

# Clean Architecture Version of the Core Loop

```text
API Controller
  -> CreateRun Use Case
    -> Run entity
    -> RunRepository port
    -> EventPublisher port

Runtime Worker
  -> ExecuteRun Use Case
    -> MemoryRetrieval port
    -> PolicyDecision port
    -> ModelProvider port
    -> ToolBroker use case
    -> EvidenceGeneration use case
    -> EvalRunner port
    -> OutcomeRepository port
```

The key is that **Postgres, OPA, Redis, OpenAI, MCP, and the UI are all details**.

The stable thing is the Aegis domain.

---

# The Clean Architecture Rule for Aegis

I would make this an explicit ADR:

> **ADR: Aegis follows Clean Architecture dependency direction.**

Decision:

```text
Domain and application code must not depend on frameworks, databases,
model providers, policy engines, tool protocols, UI frameworks, or deployment infrastructure.

All external systems are accessed through ports/adapters.
```

Consequences:

```text
- Easier to test core behavior.
- Easier to swap model providers.
- Easier to replace OPA later if needed.
- Easier to support MCP without becoming MCP-dependent.
- Easier to move from local-first to hosted v1.
- Easier to avoid business logic leaking into controllers or database code.
```

---

# What Would Make It “Not Clean”

Aegis would violate Clean Architecture if we did things like:

```text
Tool Broker logic directly imports OPA-specific code everywhere.
Memory admission logic is embedded in SQL queries.
Run state transitions live only in HTTP controllers.
Evidence generation depends directly on Postgres row shapes.
Domain entities know about JSON Schema libraries.
Business outcome logic lives in the UI.
Model-provider-specific objects leak into core use cases.
MCP-specific tool types become the canonical domain model.
```

That would make the system brittle.

Instead:

```text
OPA is an adapter.
Postgres is an adapter.
MCP is an adapter.
OpenAI/local models are adapters.
Admin UI is an adapter.
JSON Schema is a contract artifact.
```

---

# Best Clean Architecture Package Shape

For TypeScript/Bun, I would structure v1 like this:

```text
packages/
  core/
    src/
      domain/
        run/
        memory/
        tools/
        policy/
        evidence/
        evals/
        feedback/
        outcomes/
      application/
        use-cases/
        ports/
        services/
      shared/
        errors/
        ids/
        result/
        clock/

  adapters/
    src/
      postgres/
      redis/
      opa/
      otel/
      model-providers/
      mcp/
      email/
      crm/
      object-storage/

services/
  aegis-api/
    src/
      http/
      controllers/
      routes/
      middleware/

  aegis-worker/
    src/
      jobs/
      consumers/
      workflows/

apps/
  admin-ui/
```

That is cleaner than putting domain rules directly inside `services/runtime`, `services/memory`, etc.

---

# Clean Architecture Service Boundary Recommendation

Instead of thinking first in physical services:

```text
runtime service
memory service
tool service
policy service
evidence service
```

I would think first in Clean Architecture modules:

```text
core/domain
core/application
adapters/postgres
adapters/opa
adapters/model-provider
adapters/tool-executor
api/controllers
worker/jobs
ui
```

Then later, if needed, split physical services around those modules.

For MVP:

```text
one API process
one worker process
one shared core package
many adapters
```

For v1:

```text
same architecture, stronger deployment and tenant isolation
```

For v2/scale:

```text
split runtime, memory, tool broker, policy, evidence, evals if needed
```

---

# Hexagonal Architecture Also Fits

Aegis is also naturally **Hexagonal Architecture / Ports and Adapters**.

The domain core has ports:

```text
ModelProviderPort
PolicyDecisionPort
MemoryRepositoryPort
ToolExecutorPort
EvidenceStorePort
EvalRunnerPort
OutcomeRepositoryPort
TelemetryPort
EventPublisherPort
ApprovalPort
```

And adapters:

```text
OpenAIModelAdapter
LocalModelAdapter
MockModelAdapter
OPAAdapter
PostgresMemoryRepository
PostgresRunRepository
MCPToolAdapter
NativeToolAdapter
OTelTelemetryAdapter
S3EvidenceStore
```

So the exact architectural style could be described as:

> **Clean Architecture implemented with ports and adapters.**

That is the strongest formulation.

---

# Final Answer

Yes.

I would say:

> **Aegis should explicitly be designed as Clean Architecture / Hexagonal Architecture: a domain core of AI reliability rules, surrounded by use cases, ports, adapters, infrastructure, and interfaces.**

The product’s control-plane nature makes Clean Architecture especially appropriate because Aegis must remain independent of:

```text
specific model providers
specific agent frameworks
specific policy engines
specific tool protocols
specific databases
specific UI frameworks
specific deployment targets
```

The clean core is:

```text
runs
memory
tool governance
policy decisions
evidence
evals
feedback
outcomes
```

Everything else is an adapter.

That should become one of the foundational ADRs.
