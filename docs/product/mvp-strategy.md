# Aegis MVP Strategy

Status: proposed  
Codename: Aegis  
Product: AIC AI Reliability Control Plane  
Last updated: 2026-06-15  

## MVP Principle

The MVP is not a broad platform. The MVP is a thin vertical slice through the trust loop.

Aegis should prove:

> AI can perform useful work under identity, policy, tool governance, evidence, eval, feedback, and outcome tracking.

## Golden Workflow

The golden workflow is:

> Governed Sales/Ops Follow-Up

It accepts a synthetic customer conversation and produces a governed follow-up workflow.

## MVP-A — Proof Loop

MVP-A must show:

1. create run,
2. record events,
3. model proposes a tool action,
4. Tool Broker receives proposal,
5. policy checks the tool,
6. safe action proceeds or is mocked,
7. high-risk action is blocked or approval-gated,
8. Evidence Pack is generated,
9. run timeline is visible.

MVP-A can defer rich memory, complex evals, advanced outcomes, full UI, real external tools, and real customer data.

## MVP-B — Learning Loop

MVP-B adds:

1. governed memory retrieval,
2. memory candidate proposal,
3. Memory Admission Gate,
4. feedback capture,
5. basic eval result,
6. business outcome event.

## Recommended First Visible Win

The clearest first demo is:

```text
The AI analyzes a customer conversation.
It drafts a useful follow-up.
It proposes sending the email.
Aegis blocks or requires approval for email.send.
Aegis explains why.
Aegis generates evidence.
Aegis records that risk was prevented and time was saved.
```

## MVP Included Capabilities

Thin versions of:

- Run Envelope,
- Run Events,
- Tool Proposal,
- Tool Broker,
- Policy Decision,
- Approval Required state,
- Evidence Pack,
- Eval Result,
- Feedback Record,
- Business Outcome,
- Synthetic Demo Tenant.

## MVP Deferred Capabilities

Explicitly defer full microservices, Kubernetes, marketplace, plugin registry, visual workflow builder, multi-agent swarm, fine-tuning, enterprise SSO, billing, full event sourcing, real customer data, formal compliance claims, and large connector ecosystem.

## MVP Data Rule

Use synthetic data only.

Seed:

- `tenant_demo`,
- `agent_sales_ops`,
- `workflow_sales_follow_up`,
- sample customer,
- sample conversation,
- sample CRM record,
- sample memory,
- sample tool pack,
- sample eval pack.

## MVP Evidence Target

MVP targets **Evidence Level 2 — Operational Evidence**.

## MVP Definition of Done

MVP is done when the golden workflow can run locally and demonstrate run creation, events, model/mock output, tool proposal, policy decision, high-risk block/approval, evidence, eval, feedback, outcome, and run summary.

## MVP Anti-Goal

Do not build a giant platform first. Build a narrow, obvious proof of governed AI work.

