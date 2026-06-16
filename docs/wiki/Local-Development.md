# Local Development

Doctor script, dev script, local services.

---

## Purpose

Local Development defines how contributors run Aegis locally.

---

## Desired Local Services

* Aegis API,
* Aegis worker,
* PostgreSQL,
* pgvector,
* Redis if needed,
* mock policy adapter,
* mock model provider,
* demo console.

---

## Target Commands

```bash
bash scripts/doctor.sh
bash scripts/dev.sh
bash scripts/test.sh
```

---

## Local Data

Use synthetic data only.

No real customer data should be required for MVP demos.

---

## North Star

Local development should prove the control loop without cloud complexity.
