# AIC Aegis

**Codename:** `aegis`

AIC Aegis is the MVP repository for the **AIC AI Reliability Control Plane**.

It is the software layer that makes AI systems:

- remember reliably,
- act safely,
- learn from feedback,
- use tools through governed brokers,
- evaluate themselves,
- follow policy,
- produce evidence,
- and improve business outcomes.

## Product shape

Aegis is not a chatbot framework. It is an **AI Reliability Control Plane** that wraps model calls, agent workflows, memory, tools, policy decisions, evaluations, traces, approvals, and business outcomes.

## MVP wedge

> Wrap any AI workflow with durable memory, governed tool use, runtime policy checks, traces, evals, and evidence packs.

## Core planes

1. Agent Runtime Plane
2. Memory Plane
3. Tool Governance Plane
4. Policy & Safety Plane
5. Evaluation Plane
6. Evidence & Audit Plane
7. Learning & Business Outcome Plane

## First workflow

The first canonical workflow is a **Sales/Ops Assistant**:

1. Create an AI run.
2. Retrieve governed memory.
3. Call an LLM.
4. Propose tool calls.
5. Broker tool calls through policy.
6. Generate an evidence pack.
7. Collect human feedback.
8. Run evals.
9. Admit or reject memory updates.

## Getting started

```bash
cp .env.example .env
bash scripts/doctor.sh
bash scripts/dev.sh
```

This scaffold intentionally starts as a planning-first, contract-first repository. The next steps are:

1. Fill out `docs/product/WP-E0-001-product-charter.md`.
2. Finalize ADRs in `docs/adrs/`.
3. Define GitHub epics and work packets.
4. Implement the run envelope and evidence schema.
