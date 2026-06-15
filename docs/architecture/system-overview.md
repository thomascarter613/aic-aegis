# System Overview

AIC Aegis is an AI Reliability Control Plane.

## Core system planes

1. Agent Runtime Plane
2. Memory Plane
3. Tool Governance Plane
4. Policy & Safety Plane
5. Evaluation Plane
6. Evidence & Audit Plane
7. Learning & Business Outcome Plane

## High-level flow

```text
User / App
  -> Gateway
  -> Runtime
  -> Policy checks
  -> Memory retrieval
  -> Model call
  -> Tool proposal
  -> Tool Broker
  -> Evidence Pack
  -> Eval result
  -> Feedback and outcome event
```

## Principle

The model proposes. The platform disposes.

The model does not directly own credentials, durable memory writes, tool execution, approval decisions, or evidence generation.
