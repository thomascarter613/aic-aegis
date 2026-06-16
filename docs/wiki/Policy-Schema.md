# Policy Schema

Policy decisions and policy metadata.

---

## Purpose

Policy Schema defines how Aegis records runtime policy decisions.

---

## Policy Decision Fields

Required:

* `policy_decision_id`,
* `tenant_id`,
* `run_id`,
* `trace_id`,
* `checkpoint`,
* `decision`,
* `reason`,
* `policy_id`,
* `policy_version`,
* `created_at`.

---

## Policy Metadata

Policy metadata may include:

* policy pack ID,
* risk area,
* input hash,
* actor,
* tool ID,
* memory ID,
* evidence pack ID.

---

## North Star

Policy Schema makes governance decisions durable and reviewable.
