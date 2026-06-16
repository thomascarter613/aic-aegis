# AI Agent Contributor Guide

Rules for Codex and other AI agents working in the repo.

---

## Purpose

AI Agent Contributor Guide defines how AI coding agents may contribute to Aegis.

---

## Rules

AI agents must:

1. work from explicit task or work packet,
2. preserve Aegis Laws,
3. avoid architecture drift,
4. avoid provider leakage into domain core,
5. update docs when needed,
6. run or describe tests,
7. avoid inventing decisions,
8. preserve tenant isolation,
9. preserve evidence generation,
10. avoid direct tool execution bypasses.

---

## Forbidden Changes

AI agents must not:

* bypass Tool Broker,
* bypass Memory Admission Gate,
* skip policy decisions,
* skip evidence,
* claim business value without outcome records,
* introduce silent failures.

---

## North Star

AI agents may help build Aegis, but they must not weaken Aegis governance.
