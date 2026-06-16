# Database Tables

Current and planned database tables.

---

## Purpose

This page lists database tables for Aegis.

---

## MVP-A Tables

| Table               | Purpose                      |
| ------------------- | ---------------------------- |
| `tenants`           | Tenant records               |
| `agents`            | Agent identity               |
| `workflows`         | Workflow identity            |
| `runs`              | Governed runs                |
| `run_events`        | Timeline events              |
| `model_calls`       | Model/mock model calls       |
| `tool_definitions`  | Tool registry                |
| `tool_calls`        | Tool proposals and execution |
| `policy_decisions`  | Policy decision records      |
| `approval_requests` | Approval requests            |
| `evidence_packs`    | Evidence output              |

---

## MVP-B Tables

* `memories`,
* `memory_candidates`,
* `feedback_records`,
* `eval_cases`,
* `eval_packs`,
* `eval_runs`,
* `eval_results`,
* `business_outcomes`.

---

## North Star

Database tables persist the truth Aegis needs to govern AI work.
