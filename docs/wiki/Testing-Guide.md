# Testing Guide

Unit, integration, contract, eval, and acceptance tests.

---

## Purpose

Testing Guide defines how Aegis proves correctness.

---

## Test Types

| Test Type   | Purpose                           |
| ----------- | --------------------------------- |
| Unit        | Test domain and application logic |
| Integration | Test adapters and persistence     |
| Contract    | Test APIs, schemas, and events    |
| Eval        | Test AI workflow behavior         |
| Acceptance  | Test work-packet completion       |

---

## MVP-A Tests

MVP-A should test:

* run creation,
* event recording,
* tool proposal flow,
* policy decision recording,
* high-risk tool block,
* Evidence Pack generation.

---

## North Star

Tests prove Aegis works before claims are made.
