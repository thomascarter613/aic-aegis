# Outcome Schema

Business outcome events.

---

## Purpose

Outcome Schema defines how Aegis records business value and risk prevention.

---

## Fields

Required:

* `outcome_id`,
* `tenant_id`,
* `run_id`,
* `workflow_id`,
* `agent_id`,
* `outcome_type`,
* `measurement_type`,
* `value`,
* `unit`,
* `confidence`,
* `source`,
* `evidence_pack_id`,
* `recorded_at`.

---

## Event Types

Examples:

* `outcome.recorded`,
* `outcome.verified`,
* `outcome.disputed`,
* `outcome.retracted`.

---

## North Star

Outcome Schema ensures value claims are attributable and honest.
