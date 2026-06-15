# Aegis Architecture Doctrine

Status: proposed  
Codename: Aegis  
Product: AIC AI Reliability Control Plane  
Last updated: 2026-06-15  

## Doctrine Statement

Aegis is a **Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work**.

Aegis does not merely run AI agents. Aegis governs AI work.

## Highest-Level Architecture Test

Every major feature must help Aegis explain or improve at least one of these:

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
- system reliability.

If a feature does not improve one of these, defer it.

## Core Loop

The product is the reliability loop:

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

MVP must implement a thin vertical slice through this loop.

## Foundational Principles

### Clean Architecture

The domain core must not depend on frameworks, databases, policy engines, model providers, tool protocols, UI frameworks, or deployment infrastructure.

### Ports and Adapters

All external systems are adapters:

- model providers,
- OPA/Rego,
- Postgres,
- Redis,
- MCP,
- OpenTelemetry,
- CRM/email systems,
- object storage,
- UI.

### Domain-Driven Design

Aegis must preserve its ubiquitous language:

- Run,
- Run Envelope,
- Run Event,
- Memory Candidate,
- Memory Record,
- Memory Admission Gate,
- Tool Manifest,
- Tool Proposal,
- Tool Call,
- Tool Broker,
- Policy Decision,
- Approval Request,
- Evidence Pack,
- Eval Result,
- Feedback Record,
- Business Outcome.

### Event-Driven Architecture

Every meaningful AI action should become a domain event. Event history powers evidence, auditability, reconstruction, evals, projections, and outcome analytics.

### Selective CQRS

Use command/query separation where write rules and read needs differ: runs, memory candidates, tool calls, evidence, evals, feedback, outcomes, and approvals.

### MACH-Aligned

Aegis should be modular, API-first, cloud-native-capable, and headless. Physical microservices are deferred until scale, team, or deployment boundaries justify them.

### Local-First, Cloud-Native-Capable

The MVP must run locally without paid APIs. v1 should be deployable as a production stack.

## MVP Doctrine

The MVP should not be a broad platform. It should be a narrow proof that Aegis can govern useful AI work.

First visible win:

> The AI tries to perform useful work. Aegis lets safe work proceed, blocks or escalates risky work, explains why, produces evidence, and records business value.

## Evidence Doctrine

Evidence is not logging. Evidence is a first-class trust artifact.

Every governed run should produce structured, referential, inspectable, redaction-aware evidence.

MVP target: Evidence Level 2.  
v1 target: Evidence Level 3.  
Enterprise target: Evidence Level 4+.

## Memory Doctrine

Memory is governed state, not a vector dump.

Durable memory requires source, subject, scope, sensitivity, confidence, lifecycle, admission decision, correction path, supersession path, and evidence reference.

## Tool Doctrine

Agents do not call tools directly. Agents propose Tool Proposals.

The Tool Broker validates, authorizes, approves/blocks, executes, filters, records, and emits evidence.

## Policy Doctrine

Policy must execute at runtime. Every policy decision must include a reason.

## Evaluation Doctrine

Evals are promotion gates. Every meaningful failure should become an eval case, policy test, memory correction, tool schema test, prompt regression, or workflow constraint.

## Outcome Doctrine

Aegis must not merely produce text. Aegis must connect AI activity to business value. Outcomes may be estimated or verified, but they must be labeled accurately.

## Defer Doctrine

Explicitly defer:

- full microservices,
- Kubernetes,
- marketplace,
- visual workflow builder,
- multi-agent swarm,
- fine-tuning,
- enterprise SSO,
- billing,
- full event sourcing,
- real customer data,
- formal compliance claims,
- large connector ecosystem.

## Golden Workflow

Aegis must maintain one canonical golden workflow:

> Governed Sales/Ops Follow-Up

It is the demo, regression test, onboarding path, and product proof.

## Final Doctrine

Aegis is for **provable AI work**.

If Aegis cannot prove what happened, Aegis did not govern the work.

