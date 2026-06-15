# Contributing

AIC Aegis is currently pre-MVP.

Contribution rules:

1. Do not add real secrets, credentials, customer data, or private business data.
2. Every runtime behavior should be traceable to a run ID.
3. Every sensitive action should have a policy decision.
4. Every durable memory write should pass through the Memory Admission Gate.
5. Every high-risk tool call should be approved or blocked.
6. Every workflow change should eventually have an eval.
7. Every major design decision should have an ADR.

## Local checks

```bash
bash scripts/doctor.sh
bash scripts/check.sh
```
