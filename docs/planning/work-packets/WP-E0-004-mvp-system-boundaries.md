---

title: WP-E0-004 — MVP System Boundaries
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
work_packet: WP-E0-004
depends_on:

* WP-E0-001
* WP-E0-002
* WP-E0-003A
* WP-E0-003
  next_work_packet: WP-E0-005
  last_updated: 2026-06-15

---

# WP-E0-004 — MVP System Boundaries

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Work Packet Summary

WP-E0-004 defines the exact MVP system boundaries for AIC Aegis.

This work packet exists to prevent ambiguity before implementation planning begins. It translates the Product Charter, System Glossary, Architecture Doctrine, MVP Strategy, Control Catalog, Risk Register, and Architecture Overview into concrete MVP boundaries.

The purpose is not to design the full future platform. The purpose is to define the smallest coherent system boundary that can prove governed AI work from model proposal to platform disposition to evidence.

## 2. Objective

Define the MVP boundaries for:

* MVP-A Proof Loop vs MVP-B Learning Loop;
* API service vs worker service;
* domain/application/adapters/interfaces package boundaries;
* command vs query boundaries;
* event boundaries;
* schema boundaries;
* persistence boundaries;
* policy/tool/memory/evidence/eval/outcome thin-slice boundaries;
* explicit non-goals and deferred scope;
* acceptance criteria for moving into WP-E0-005 Initial ADR Pack.

## 3. Doctrine Anchor

Aegis must remain a reliability control plane for provable AI work.

This means:

1. the model may propose;
2. the platform must dispose;
3. no tool action may bypass the Tool Broker;
4. no important model proposal may bypass Proposal capture;
5. no external effect may occur without policy disposition;
6. high-risk work must be blocked, mocked, modified, or approval-gated;
7. evidence must be generated as a first-class product artifact;
8. Run Timelines must be reconstructable;
9. memory writes are deferred to MVP-B and must pass through Memory Admission;
10. MVP simplicity must not erase governance boundaries.

## 4. Inputs

This work packet depends on:

* `docs/product/product-charter.md`
* `docs/glossary/system-glossary.md`
* `docs/architecture/architecture-doctrine.md`
* `docs/architecture/aegis-laws.md`
* `docs/architecture/system-overview.md`
* `docs/architecture/architecture-fitness-functions.md`
* `docs/governance/control-catalog.md`
* `docs/governance/risk-register.md`
* `docs/product/mvp-strategy.md`
* `docs/product/trust-ladder.md`
* `docs/product/maturity-model.md`
* `docs/decisions/product-decisions/README.md`
* `docs/planning/work-packets/WP-E0-003-architecture-overview.md`

## 5. Output

Primary output:

* `docs/planning/work-packets/WP-E0-004-mvp-system-boundaries.md`

Expected downstream output:

* `docs/decisions/adr/` initial ADR pack in WP-E0-005

## 6. MVP-A / MVP-B Boundary

### 6.1 MVP-A — Proof Loop

MVP-A proves that Aegis can govern a single model-originated tool action proposal and produce inspectable evidence.

MVP-A includes:

1. create Run;
2. identify Actor;
3. record Run Events;
4. generate or accept mock model Tool Action Proposal;
5. validate and record Proposal;
6. pass Tool Action Proposal to Tool Broker;
7. validate tool action schema;
8. perform Policy Check;
9. produce platform Disposition;
10. allow, block, mock, or approval-gate the proposed action;
11. record Tool Broker decision;
12. record approval request when required;
13. execute only mock-safe tool behavior for MVP;
14. generate Evidence Pack;
15. expose Run Timeline.

MVP-A does not include:

* governed memory retrieval;
* Memory Candidate proposal;
* Memory Admission Gate implementation;
* Feedback Event capture;
* Eval Result recording;
* Business Outcome Event recording;
* real customer data;
* production email sending;
* real CRM updates;
* broad connector framework;
* multi-agent orchestration;
* enterprise authentication;
* billing;
* Kubernetes;
* formal compliance claims.

### 6.2 MVP-B — Learning Loop

MVP-B extends MVP-A with governed learning.

MVP-B includes:

1. governed memory retrieval record;
2. Memory Candidate proposal;
3. Memory Admission Gate decision;
4. Feedback Event capture;
5. basic Eval Result recording;
6. Business Outcome Event recording;
7. Timeline and Evidence Pack extensions for learning records.

MVP-B does not include:

* autonomous memory mutation;
* unreviewed memory writes;
* complex eval framework;
* large analytics system;
* full outcome attribution engine;
* enterprise-grade data retention;
* multi-tenant governance;
* customer production data.

### 6.3 Boundary Rule

MVP-A must be buildable, demonstrable, and testable without MVP-B.

MVP-B may reuse MVP-A Run, Event, Proposal, Policy, Evidence, and Timeline primitives, but MVP-A must not depend on memory, eval, feedback, or business outcome capabilities.

## 7. Golden Workflow Boundary

The golden workflow is:

**Governed Sales/Ops Follow-Up**

For MVP-A, this workflow is represented as a controlled mock scenario:

1. an Actor starts a Run for a sales or operations follow-up;
2. a mock model proposes a follow-up Tool Action;
3. the Tool Action may be classified as safe, risky, or blocked;
4. Aegis policy evaluates the proposal;
5. the Tool Broker applies platform disposition;
6. an allowed action is mocked, not sent to a real customer;
7. a high-risk action is blocked or approval-gated;
8. an Evidence Pack and Timeline explain the Run.

MVP-A must not send real emails, contact real prospects, update real CRMs, or use real customer data.

## 8. Service Boundary

### 8.1 MVP Deployment Shape

The MVP should begin as a local-first modular system.

Acceptable MVP shapes:

* single process with clear package boundaries;
* API process plus optional worker process;
* synchronous implementation of worker-like use cases where the worker boundary remains explicit;
* file-backed or lightweight local persistence.

Not acceptable for MVP-A:

* mandatory Kubernetes;
* mandatory cloud infrastructure;
* mandatory distributed event broker;
* mandatory microservice decomposition;
* mandatory managed database;
* mandatory production connector setup.

### 8.2 API Service Boundary

The API service owns request/response interaction.

MVP-A API responsibilities:

* create Run;
* get Run;
* list Runs;
* record Run Event when needed;
* submit Tool Action Proposal;
* run Tool Broker use case;
* request or retrieve Evidence Pack;
* retrieve Run Timeline;
* retrieve Policy Check result;
* retrieve Tool Broker decision;
* retrieve Approval Gate status.

The API service must not:

* execute tools directly outside Tool Broker;
* perform policy decisions hidden inside controllers;
* write evidence as incidental logs only;
* allow direct mutation of domain records without application use cases;
* expose UI-only behavior as the primary product surface.

### 8.3 Worker Service Boundary

The worker boundary owns deferred or long-running execution.

MVP-A worker responsibilities may include:

* evidence pack generation;
* mock tool execution;
* approval wait/resume behavior;
* asynchronous timeline enrichment.

MVP-A may implement these synchronously if:

* the application use case remains separate;
* the boundary can later become an actual worker;
* the API does not embed infrastructure logic directly.

MVP-B worker responsibilities may include:

* memory admission workflows;
* eval processing;
* feedback processing;
* outcome processing.

## 9. Clean Architecture Package Boundary

The MVP should preserve the following logical package boundary:

```text
src/
  domain/
    actor/
    run/
    event/
    proposal/
    policy/
    tool/
    approval/
    evidence/
    timeline/
    memory/
    feedback/
    eval/
    outcome/

  application/
    commands/
    queries/
    use-cases/
    ports/

  adapters/
    persistence/
    policy/
    model/
    tools/
    evidence/
    memory/

  interfaces/
    http/
    cli/
    worker/
```

The exact language, framework, and directory names may change in implementation, but the architectural responsibilities must remain intact.

## 10. Domain Boundary

The domain layer owns Aegis business concepts and rules.

### 10.1 MVP-A Domain Concepts

MVP-A domain includes:

* Actor;
* Run;
* Run Event;
* Proposal;
* Tool Action;
* Policy Check;
* Control;
* Risk;
* Disposition;
* Approval Gate;
* Evidence Pack;
* Evidence Artifact;
* Timeline.

### 10.2 MVP-B Domain Concepts

MVP-B domain adds:

* Memory;
* Memory Candidate;
* Memory Admission;
* Feedback Event;
* Eval Result;
* Business Outcome Event.

### 10.3 Domain Must Not Depend On

The domain layer must not depend on:

* HTTP framework;
* database library;
* ORM;
* queue library;
* model SDK;
* cloud SDK;
* external tool SDK;
* filesystem implementation;
* web UI framework.

## 11. Application Boundary

The application layer owns use cases, commands, queries, orchestration, and ports.

### 11.1 MVP-A Commands

MVP-A commands:

* `CreateRun`
* `RecordRunEvent`
* `SubmitProposal`
* `BrokerToolAction`
* `EvaluatePolicy`
* `RequestApproval`
* `RecordApprovalDecision`
* `GenerateEvidencePack`

### 11.2 MVP-A Queries

MVP-A queries:

* `GetRun`
* `ListRuns`
* `ListRunEvents`
* `GetProposal`
* `GetPolicyCheck`
* `GetToolAction`
* `GetApprovalRequest`
* `GetEvidencePack`
* `GetRunTimeline`

### 11.3 MVP-B Commands

MVP-B commands:

* `RetrieveGovernedMemory`
* `ProposeMemoryCandidate`
* `EvaluateMemoryAdmission`
* `CaptureFeedback`
* `RecordEvalResult`
* `RecordBusinessOutcome`

### 11.4 MVP-B Queries

MVP-B queries:

* `GetMemoryCandidate`
* `GetMemoryAdmission`
* `ListFeedbackEvents`
* `GetEvalResult`
* `GetBusinessOutcome`
* `GetLearningTimeline`

### 11.5 Application Ports

MVP-A ports:

* `RunRepository`
* `RunEventStore`
* `ProposalRepository`
* `PolicyEngine`
* `ToolExecutor`
* `ApprovalRepository`
* `EvidenceWriter`
* `EvidenceRepository`
* `TimelineReader`
* `ModelProposalProvider`

MVP-B ports:

* `MemoryStore`
* `MemoryAdmissionPolicy`
* `FeedbackRepository`
* `EvalResultRepository`
* `OutcomeRepository`

## 12. Adapter Boundary

Adapters implement application ports.

### 12.1 MVP-A Adapters

MVP-A adapters may include:

* in-memory repository;
* SQLite or local Postgres repository;
* file-backed event store;
* local policy evaluator;
* deterministic mock model adapter;
* mock tool executor;
* file-backed evidence writer;
* local timeline reader.

### 12.2 MVP-B Adapters

MVP-B adapters may include:

* local governed memory store;
* file-backed memory candidate store;
* local feedback repository;
* local eval result repository;
* local outcome repository.

### 12.3 Adapter Rules

Adapters must not own domain language.

Adapters translate between infrastructure details and Aegis application ports.

Adapters must not bypass:

* Proposal capture;
* Policy Check;
* Tool Broker;
* Approval Gate;
* Evidence Pack generation;
* Memory Admission Gate.

## 13. Interface Boundary

Interfaces expose Aegis capabilities.

MVP interfaces may include:

* HTTP API;
* CLI;
* worker entry point;
* local script or demo runner.

Interface responsibilities:

* validate transport-level request shape;
* translate request into application command or query;
* return application response;
* avoid embedding domain or policy logic.

Interfaces must not:

* directly call external tools;
* directly mutate persistence records;
* perform hidden policy decisions;
* generate evidence outside the Evidence use case;
* make UI-only behavior authoritative.

## 14. Event Boundary

Aegis is event-rich, but MVP-A is not full event sourcing.

Events exist to reconstruct the Run Timeline and support Evidence Pack generation.

### 14.1 MVP-A Event Types

MVP-A events:

* `RunCreated`
* `RunEventRecorded`
* `ProposalSubmitted`
* `ToolActionProposed`
* `PolicyCheckCompleted`
* `ToolActionDispositioned`
* `ApprovalGateRequested`
* `ApprovalDecisionRecorded`
* `ToolActionMockExecuted`
* `ToolActionBlocked`
* `EvidencePackGenerated`
* `TimelineGenerated`

### 14.2 MVP-B Event Types

MVP-B adds:

* `GovernedMemoryRetrieved`
* `MemoryCandidateProposed`
* `MemoryAdmissionCompleted`
* `FeedbackCaptured`
* `EvalResultRecorded`
* `BusinessOutcomeRecorded`

### 14.3 Event Rules

Each event must include:

* event ID;
* event type;
* event version;
* Run ID;
* Actor ID where applicable;
* timestamp;
* correlation ID where applicable;
* causation ID where applicable;
* payload;
* schema version.

MVP-A events may be persisted simply, but event shape must be stable enough to support future migration.

## 15. Schema Boundary

Schemas define contracts for data crossing system boundaries.

### 15.1 MVP-A Schema Families

MVP-A schema families:

* Run schemas;
* Actor schemas;
* Run Event schemas;
* Proposal schemas;
* Tool Action schemas;
* Policy Check schemas;
* Disposition schemas;
* Approval schemas;
* Evidence Pack schemas;
* Timeline schemas.

### 15.2 MVP-B Schema Families

MVP-B adds:

* Memory Retrieval schemas;
* Memory Candidate schemas;
* Memory Admission schemas;
* Feedback Event schemas;
* Eval Result schemas;
* Business Outcome Event schemas.

### 15.3 Schema Rules

Schemas must be:

* explicit;
* versioned;
* stable enough for evidence;
* validated at boundaries;
* named using Aegis vocabulary;
* attached to evidence when relevant.

Schema names must avoid generic agent-framework language.

## 16. Persistence Boundary

MVP persistence must support inspection, evidence, and timeline reconstruction.

### 16.1 MVP-A Minimum Records

MVP-A minimum persisted or persistable records:

* Run;
* Actor reference;
* Run Event;
* Proposal;
* Tool Action;
* Policy Check;
* Disposition;
* Approval Request;
* Approval Decision;
* Evidence Pack;
* Evidence Artifact;
* Timeline Snapshot or Timeline Query Source.

### 16.2 MVP-B Minimum Records

MVP-B adds:

* Memory Retrieval Record;
* Memory Candidate;
* Memory Admission Decision;
* Feedback Event;
* Eval Result;
* Business Outcome Event.

### 16.3 Persistence Rules

Persistence may be local and simple, but it must preserve:

* IDs;
* timestamps;
* event order;
* actor attribution;
* proposal-to-disposition trace;
* policy-to-disposition trace;
* tool action result;
* approval status;
* evidence artifact references.

Persistence must not be treated as incidental logging.

## 17. Policy Boundary

Policy is a first-class application boundary.

### 17.1 MVP-A Policy Scope

MVP-A policy must determine whether a Tool Action Proposal is:

* allowed;
* mocked;
* blocked;
* approval required.

Policy input should include:

* Run context;
* Actor;
* Proposal;
* Tool Action;
* target operation;
* risk context;
* configured controls.

Policy output should include:

* Policy Check ID;
* disposition;
* risk level;
* matched controls;
* rationale;
* timestamp;
* evidence reference when available.

### 17.2 MVP-B Policy Scope

MVP-B policy extends to:

* memory admission;
* feedback-derived candidates;
* eval result interpretation;
* business outcome evidence quality.

## 18. Tool Boundary

All tool actions must pass through the Tool Broker.

### 18.1 MVP-A Tool Scope

MVP-A tool behavior should be mock-safe.

Allowed MVP-A tool examples:

* mock send follow-up email;
* mock create CRM note;
* mock create task;
* mock update sales/ops follow-up status.

Not allowed in MVP-A:

* real email sending;
* real CRM mutation;
* real customer data processing;
* arbitrary external API execution;
* direct model-to-tool invocation.

### 18.2 Tool Broker Responsibilities

The Tool Broker must:

1. receive Tool Action Proposal;
2. validate schema;
3. request Policy Check;
4. enforce disposition;
5. route to Approval Gate when required;
6. execute mock action only when allowed;
7. record result;
8. attach evidence.

## 19. Approval Boundary

The Approval Gate handles high-risk or ambiguous proposed work.

### 19.1 MVP-A Approval Scope

MVP-A approval may be simulated or local.

Minimum approval states:

* requested;
* approved;
* rejected;
* expired;
* cancelled.

Minimum approval fields:

* approval request ID;
* Run ID;
* Proposal ID;
* Tool Action ID;
* requested by Actor;
* approver Actor when decided;
* status;
* rationale;
* timestamps.

### 19.2 Approval Rule

A high-risk action must not execute until approval is recorded.

If approval is not implemented fully, the action must be blocked or mocked.

## 20. Evidence Boundary

Evidence is a product primitive.

### 20.1 MVP-A Evidence Scope

MVP-A Evidence Pack must include or reference:

* Run metadata;
* Actor metadata;
* Run Events;
* Proposal;
* Tool Action;
* Policy Check;
* Disposition;
* Approval Request and Decision if applicable;
* mock Tool Action result if applicable;
* Timeline export;
* Evidence Pack manifest.

### 20.2 MVP-B Evidence Scope

MVP-B Evidence Pack adds:

* memory retrieval record;
* Memory Candidate;
* Memory Admission Decision;
* Feedback Event;
* Eval Result;
* Business Outcome Event.

### 20.3 Evidence Rules

Evidence artifacts must be:

* inspectable;
* tied to Run ID;
* tied to schema versions;
* generated by application use case;
* not replaced by logs;
* sufficient to reconstruct what happened.

## 21. Timeline Boundary

The Timeline is the ordered reconstruction of a Run.

### 21.1 MVP-A Timeline Must Show

MVP-A Timeline must show:

1. Run created;
2. Proposal submitted;
3. Tool Action proposed;
4. Policy Check completed;
5. Disposition applied;
6. Approval requested/decided if applicable;
7. Tool action mocked, blocked, or deferred;
8. Evidence Pack generated.

### 21.2 Timeline Rule

The Timeline must be reconstructable from events and related records.

It should not depend on hidden UI state, transient logs, or model-generated summaries.

## 22. Memory Boundary

Memory is deferred to MVP-B.

### 22.1 MVP-A Memory Rule

MVP-A must not require memory retrieval or memory writes.

MVP-A may include placeholder interfaces only if they do not affect MVP-A acceptance.

### 22.2 MVP-B Memory Rule

MVP-B must treat new memory as a Memory Candidate.

No Memory Candidate becomes governed memory without Memory Admission Gate decision.

## 23. Eval Boundary

Evals are deferred to MVP-B.

MVP-A must not require eval framework implementation.

MVP-B minimum eval capability:

* record basic Eval Result;
* associate Eval Result with Run, output, Proposal, Tool Action, or Evidence Pack;
* distinguish eval result from model self-assessment.

## 24. Feedback Boundary

Feedback is deferred to MVP-B.

MVP-B minimum feedback capability:

* capture Feedback Event;
* associate feedback with Run or output;
* preserve Actor/source;
* make feedback available for evidence and future learning.

## 25. Business Outcome Boundary

Business Outcome Events are deferred to MVP-B.

MVP-B minimum outcome capability:

* record operational or business outcome;
* associate outcome with Run or workflow;
* distinguish outcome from model assertion;
* preserve evidence/provenance.

Aegis must not infer business success from generated text alone.

## 26. Out of Scope

The following are explicitly out of scope for MVP-A:

* real customer data;
* real production email sending;
* real CRM updates;
* broad connector ecosystem;
* marketplace;
* plugin registry;
* visual workflow builder;
* multi-agent swarm;
* fine-tuning;
* enterprise SSO;
* billing;
* Kubernetes;
* full microservices;
* full event sourcing;
* formal compliance claims;
* large-scale observability platform;
* advanced analytics;
* complex eval framework;
* autonomous memory mutation.

The following are explicitly out of scope for MVP-B:

* marketplace;
* plugin certification;
* enterprise multi-tenancy;
* compliance certification;
* full outcome attribution;
* production connector ecosystem;
* billing;
* customer data residency;
* legal hold;
* enterprise identity federation.

## 27. Acceptance Criteria

WP-E0-004 is accepted when it:

* clearly separates MVP-A Proof Loop from MVP-B Learning Loop;
* defines the golden workflow boundary;
* defines API service responsibilities;
* defines worker boundary responsibilities;
* defines Clean Architecture package responsibilities;
* defines domain/application/adapters/interfaces boundaries;
* defines command and query boundaries;
* defines event boundaries;
* defines schema boundaries;
* defines persistence boundaries;
* defines policy boundary;
* defines tool and Tool Broker boundary;
* defines approval boundary;
* defines evidence boundary;
* defines timeline boundary;
* defines memory/eval/feedback/outcome deferral to MVP-B;
* lists explicit non-goals;
* preserves local-first implementation;
* avoids premature microservices and Kubernetes;
* prepares the project for WP-E0-005 Initial ADR Pack.

## 28. Fitness Checks

WP-E0-004 supports these MVP-A fitness checks:

* core law visible;
* no direct model-to-tool execution;
* Proposal exists before disposition;
* Policy Check exists before external effect;
* Evidence Pack generated;
* Timeline reconstructable;
* domain layer independent from infrastructure;
* MVP-A does not depend on MVP-B;
* MVP can run locally without managed cloud infrastructure.

## 29. Risks and Mitigations

| Risk                    | Boundary Mitigation                                                       |
| ----------------------- | ------------------------------------------------------------------------- |
| Direct tool execution   | Tool Broker is mandatory for all Tool Actions.                            |
| Policy bypass           | Policy Check required before allowed or mocked execution.                 |
| Evidence gaps           | Evidence Pack required for MVP-A completion.                              |
| Ungoverned memory       | Memory deferred to MVP-B and gated by Memory Admission.                   |
| Premature microservices | MVP begins local-first with modular boundaries.                           |
| UI-first drift          | Headless API-first interfaces remain primary.                             |
| Generic agent drift     | Aegis domain vocabulary is required.                                      |
| Weak schemas            | Boundary schemas must be explicit and versioned.                          |
| Approval ambiguity      | Approval states and records are defined.                                  |
| Outcome overclaiming    | Outcomes are deferred to MVP-B and recorded separately from model claims. |

## 30. Done Means

WP-E0-004 is done when:

1. the MVP-A system boundary is explicit enough to implement;
2. the MVP-B boundary is explicit enough to defer correctly;
3. Clean Architecture boundaries are concrete enough for code organization;
4. command/query/event/schema/persistence boundaries are named;
5. policy/tool/approval/evidence/timeline boundaries are enforceable;
6. memory/eval/feedback/outcome are kept out of MVP-A;
7. out-of-scope items are explicit;
8. the next work packet can define ADRs without reopening product scope.

## 31. Handoff to WP-E0-005

WP-E0-005 should create the Initial ADR Pack.

Recommended ADRs:

* ADR-0001 — Adopt local-first modular monolith for MVP-A
* ADR-0002 — Use Clean Architecture package boundaries
* ADR-0003 — Treat model output as Proposal records
* ADR-0004 — Require Tool Broker for all tool actions
* ADR-0005 — Require Policy Check before external effect
* ADR-0006 — Generate Evidence Pack as MVP-A product artifact
* ADR-0007 — Use event-rich records without full event sourcing in MVP
* ADR-0008 — Keep MVP-A independent from MVP-B learning loop
* ADR-0009 — Use mock model and mock tools for MVP-A
* ADR-0010 — Keep MVP headless and API-first
