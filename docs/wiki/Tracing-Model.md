# Tracing Model

Trace propagation through runs.

---

## Purpose

Tracing Model defines how `trace_id` connects system activity.

---

## Trace Should Connect

* API request,
* runtime,
* model call,
* tool broker,
* policy adapter,
* evidence generator,
* eval runner,
* logs,
* events.

---

## MVP Scope

MVP-A should propagate `trace_id` across Run Envelope and Run Events.

---

## North Star

Tracing lets Aegis follow a run through the system.
