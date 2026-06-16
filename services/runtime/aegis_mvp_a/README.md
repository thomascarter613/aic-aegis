# Aegis MVP-A Runtime Skeleton

> **Core law:** The model proposes; the platform disposes.

This package is a local-first MVP-A Proof Loop skeleton for AIC Aegis.

It demonstrates:

- Run creation;
- Actor attribution;
- Proposal capture;
- Tool Broker enforcement;
- Policy Check before effect;
- Approval Gate for high-risk work;
- mock-safe tool execution;
- Evidence Pack generation;
- Timeline reconstruction.

## Run Tests

From the repository root:

```bash
bash scripts/test-mvp-a.sh
```

## Run Demo

```bash
bash scripts/mvp-a-demo.sh safe
bash scripts/mvp-a-demo.sh risky
bash scripts/mvp-a-demo.sh risky --approve
bash scripts/mvp-a-demo.sh blocked
```

Evidence output is written to:

```text
.aic/runtime/evidence/
```

## Scope Boundary

This package does not implement MVP-B memory, feedback, eval, or business outcome capabilities.
