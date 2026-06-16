# Feedback Schema

Feedback records.

---

## Purpose

Feedback Schema defines how Aegis captures human or system feedback.

---

## Fields

Required:

* `feedback_id`,
* `tenant_id`,
* `run_id`,
* `target_type`,
* `target_id`,
* `rating`,
* `classification`,
* `comment`,
* `created_by`,
* `created_at`.

---

## Feedback Targets

Feedback may target:

* output,
* memory,
* tool decision,
* policy decision,
* Evidence Pack,
* eval result,
* business outcome.

---

## North Star

Feedback Schema turns user judgment into improvement data.
