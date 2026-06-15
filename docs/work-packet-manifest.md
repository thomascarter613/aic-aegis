# AIC Aegis Work Packet Manifest

Codename: **Aegis**
Product: **AIC AI Reliability Control Plane**
Manifest version: **v0.1**
Scope: **MVP through local demo, evidence-backed workflow, and GitHub issue execution plan**

---

# Epic Overview

| Epic | Name                                        | Purpose                                                                  |
| ---- | ------------------------------------------- | ------------------------------------------------------------------------ |
| E0   | Product Charter & Architecture              | Define what Aegis is, what it is not, and how the system is structured   |
| E1   | Run Envelope & Trace Backbone               | Create the canonical execution identity and event spine                  |
| E2   | Memory System                               | Build governed, reliable, correctable AI memory                          |
| E3   | Tool Registry & Tool Broker                 | Govern AI tool use through manifests, policy, approval, and audit        |
| E4   | Policy & Safety Engine                      | Enforce runtime policy decisions for memory, tools, context, and outputs |
| E5   | Evidence & Audit System                     | Produce proof artifacts for AI activity                                  |
| E6   | Evaluation System                           | Measure quality, safety, correctness, and regressions                    |
| E7   | Feedback & Learning Loop                    | Convert corrections, failures, and reviews into improvements             |
| E8   | Business Outcome Analytics                  | Tie AI activity to measurable business value                             |
| E9   | APIs, SDKs & Integration Surface            | Make Aegis usable by apps, agents, and workflows                         |
| E10  | Local Infrastructure & Developer Experience | Make the MVP easy to run, inspect, test, and extend                      |
| E11  | Admin UI & Demo Workflows                   | Provide a visible product surface and canonical demo                     |
| E12  | Security, Governance & Release Readiness    | Harden the MVP enough to be credible and safe                            |

---

# E0 — Product Charter & Architecture

| WP ID     | Title                        | Done when                                                              |
| --------- | ---------------------------- | ---------------------------------------------------------------------- |
| WP-E0-001 | Product Charter              | Product category, mission, MVP wedge, scope, and non-goals are defined |
| WP-E0-002 | System Glossary              | Core terms are defined consistently                                    |
| WP-E0-003 | Architecture Overview        | System planes, service boundaries, and core flows are documented       |
| WP-E0-004 | MVP System Boundaries        | In-scope and out-of-scope MVP boundaries are explicit                  |
| WP-E0-005 | Initial ADR Pack             | Foundational architecture decisions are written                        |
| WP-E0-006 | Threat Model Draft           | Initial risks and mitigations are documented                           |
| WP-E0-007 | First Workflow Specification | Governed Sales/Ops Assistant workflow is fully specified               |
| WP-E0-008 | Canonical Object Model       | Core entities are named and related                                    |
| WP-E0-009 | Repository Operating Model   | Rules for docs, schemas, services, issues, and changes are defined     |
| WP-E0-010 | MVP Acceptance Plan          | End-to-end MVP demo acceptance criteria are defined                    |

---

# E1 — Run Envelope & Trace Backbone

| WP ID     | Title                      | Done when                                                                  |
| --------- | -------------------------- | -------------------------------------------------------------------------- |
| WP-E1-001 | Run Envelope Schema        | Canonical run envelope JSON schema exists                                  |
| WP-E1-002 | Run State Machine          | Run statuses and transitions are defined                                   |
| WP-E1-003 | Run Event Taxonomy         | Canonical event names and payload classes are defined                      |
| WP-E1-004 | Run Persistence Schema     | Database tables for runs and run events exist                              |
| WP-E1-005 | Trace Identity Rules       | `run_id`, `trace_id`, `tenant_id`, and `agent_id` propagation is specified |
| WP-E1-006 | Model Call Record Contract | Model call metadata schema is defined                                      |
| WP-E1-007 | Runtime Event Append API   | Runtime can append structured events                                       |
| WP-E1-008 | Run Replay Contract        | A run can be reconstructed from stored events                              |
| WP-E1-009 | Run Error Model            | Failures, retries, cancellations, and partial completions are modeled      |
| WP-E1-010 | Run Summary Generator      | A readable run summary can be produced from events                         |

---

# E2 — Memory System

| WP ID     | Title                            | Done when                                                                  |
| --------- | -------------------------------- | -------------------------------------------------------------------------- |
| WP-E2-001 | Memory Model Specification       | Working, episodic, semantic, procedural, and evaluative memory are defined |
| WP-E2-002 | Memory Database Schema           | Memory tables and event tables exist                                       |
| WP-E2-003 | Memory Candidate Schema          | Proposed memory write schema exists                                        |
| WP-E2-004 | Memory Admission Gate            | Accept/reject/review/merge/supersede logic is specified                    |
| WP-E2-005 | Memory Sensitivity Model         | Public/internal/confidential/restricted handling is defined                |
| WP-E2-006 | Memory Retrieval Contract        | Scoped retrieval API is specified                                          |
| WP-E2-007 | Memory Provenance Model          | Every memory has source, reason, confidence, and lifecycle metadata        |
| WP-E2-008 | Memory Correction Workflow       | Users can correct or invalidate memory                                     |
| WP-E2-009 | Memory Expiration & Supersession | Old or replaced memory can expire or be superseded                         |
| WP-E2-010 | Semantic Retrieval Baseline      | pgvector-based retrieval baseline is specified                             |
| WP-E2-011 | Memory Evidence Integration      | Evidence packs can reference retrieved and written memory                  |
| WP-E2-012 | Memory Poisoning Test Cases      | Initial tests cover unsafe or incorrect memory writes                      |

---

# E3 — Tool Registry & Tool Broker

| WP ID     | Title                     | Done when                                                                        |
| --------- | ------------------------- | -------------------------------------------------------------------------------- |
| WP-E3-001 | Tool Manifest Schema      | Canonical tool manifest schema exists                                            |
| WP-E3-002 | Tool Risk Classification  | Read-only, low-write, medium-write, high-write, and critical classes are defined |
| WP-E3-003 | Tool Registry Model       | Tool definitions can be registered and discovered                                |
| WP-E3-004 | Tool Proposal Contract    | Model-generated tool proposals have a standard shape                             |
| WP-E3-005 | Tool Broker Decision Flow | Broker flow for validate/check/approve/execute/log is defined                    |
| WP-E3-006 | Tool Input Validation     | Tool inputs are validated against schemas                                        |
| WP-E3-007 | Tool Output Validation    | Tool outputs are validated and filterable                                        |
| WP-E3-008 | Tool Approval Hooks       | High-risk tool actions can require human approval                                |
| WP-E3-009 | Mock Tool Executor        | MVP has safe fake tools for demo                                                 |
| WP-E3-010 | Sales/Ops Tool Pack       | Initial CRM and email tool manifests exist                                       |
| WP-E3-011 | Tool Evidence Integration | Tool proposals, decisions, and results are included in evidence packs            |

---

# E4 — Policy & Safety Engine

| WP ID     | Title                         | Done when                                            |
| --------- | ----------------------------- | ---------------------------------------------------- |
| WP-E4-001 | Policy Decision Schema        | Canonical policy decision object exists              |
| WP-E4-002 | Policy Checkpoint Model       | Required checkpoints are defined                     |
| WP-E4-003 | Base Tool Policy Pack         | Tool allow/deny/approval rules exist                 |
| WP-E4-004 | Base Memory Policy Pack       | Memory admission rules exist                         |
| WP-E4-005 | Base Output Policy Pack       | Final output/action release rules exist              |
| WP-E4-006 | Policy Service Contract       | Policy service API is specified                      |
| WP-E4-007 | OPA/Rego Integration Baseline | Local OPA policy execution path works conceptually   |
| WP-E4-008 | Policy Decision Persistence   | Decisions are stored with reason and policy version  |
| WP-E4-009 | Policy Test Fixtures          | Known allow/deny/approval examples exist             |
| WP-E4-010 | Policy Evidence Integration   | Evidence packs include all relevant policy decisions |

---

# E5 — Evidence & Audit System

| WP ID     | Title                            | Done when                                                              |
| --------- | -------------------------------- | ---------------------------------------------------------------------- |
| WP-E5-001 | Evidence Pack Schema             | Canonical evidence pack schema exists                                  |
| WP-E5-002 | Evidence Pack Data Sources       | Required run, memory, policy, tool, eval, and outcome refs are defined |
| WP-E5-003 | Evidence Pack Generator Contract | Evidence generation API is specified                                   |
| WP-E5-004 | Evidence Markdown Renderer       | Human-readable evidence summary format exists                          |
| WP-E5-005 | Evidence JSON Export             | Machine-readable export format exists                                  |
| WP-E5-006 | Evidence Redaction Rules         | Sensitive fields can be excluded or redacted                           |
| WP-E5-007 | Evidence Completeness Eval       | Evidence packs can be scored for completeness                          |
| WP-E5-008 | Evidence Storage Model           | Evidence persistence table/object model exists                         |
| WP-E5-009 | Evidence Integrity Model         | Tamper-resistance strategy is documented                               |
| WP-E5-010 | Sales/Ops Evidence Example       | Example evidence pack exists for the first workflow                    |

---

# E6 — Evaluation System

| WP ID     | Title                     | Done when                                                                                                       |
| --------- | ------------------------- | --------------------------------------------------------------------------------------------------------------- |
| WP-E6-001 | Eval Case Schema          | Canonical eval case schema exists                                                                               |
| WP-E6-002 | Eval Dataset Model        | Eval packs and cases are organized                                                                              |
| WP-E6-003 | Eval Result Schema        | Eval result object is defined                                                                                   |
| WP-E6-004 | MVP Eval Dimensions       | Task completion, policy compliance, tool correctness, memory correctness, and evidence completeness are defined |
| WP-E6-005 | Sales/Ops Eval Pack       | Initial eval cases for the first workflow exist                                                                 |
| WP-E6-006 | Eval Runner Contract      | Eval runner API and execution flow are specified                                                                |
| WP-E6-007 | Regression Gate Model     | Prompt/tool/policy/workflow changes can require eval checks                                                     |
| WP-E6-008 | Human Review Eval Model   | Human ratings and corrections can feed evals                                                                    |
| WP-E6-009 | Red-Team Seed Cases       | Initial adversarial cases exist                                                                                 |
| WP-E6-010 | Eval Evidence Integration | Evidence packs include eval scores and failures                                                                 |

---

# E7 — Feedback & Learning Loop

| WP ID     | Title                              | Done when                                              |
| --------- | ---------------------------------- | ------------------------------------------------------ |
| WP-E7-001 | Feedback Schema                    | Canonical feedback object exists                       |
| WP-E7-002 | Feedback Capture Flow              | User can rate, correct, or comment on output           |
| WP-E7-003 | Feedback Persistence               | Feedback is linked to runs and outputs                 |
| WP-E7-004 | Failure Taxonomy                   | Failure categories are defined                         |
| WP-E7-005 | Feedback-to-Memory Candidate Flow  | Corrections can propose memory updates                 |
| WP-E7-006 | Feedback-to-Eval Flow              | Failures can become future eval cases                  |
| WP-E7-007 | Improvement Recommendation Model   | System can suggest prompt/tool/policy/memory fixes     |
| WP-E7-008 | Human Review Queue Model           | Items requiring review can be tracked                  |
| WP-E7-009 | Learning Loop Evidence Integration | Feedback and learning actions appear in evidence packs |

---

# E8 — Business Outcome Analytics

| WP ID     | Title                        | Done when                                                 |
| --------- | ---------------------------- | --------------------------------------------------------- |
| WP-E8-001 | Business Outcome Schema      | Canonical outcome event schema exists                     |
| WP-E8-002 | MVP KPI Model                | First workflow KPIs are defined                           |
| WP-E8-003 | Time Saved Estimation Model  | Basic productivity value estimate exists                  |
| WP-E8-004 | Risk Prevented Metric        | Blocked or approval-required risky actions are measurable |
| WP-E8-005 | Outcome Persistence          | Outcome events are stored and linked to runs              |
| WP-E8-006 | Outcome Summary Generator    | Run summaries can show business impact                    |
| WP-E8-007 | Outcome Dashboard Contract   | Future UI requirements are specified                      |
| WP-E8-008 | Outcome Evidence Integration | Evidence packs include outcome refs and summaries         |

---

# E9 — APIs, SDKs & Integration Surface

| WP ID     | Title                           | Done when                                                        |
| --------- | ------------------------------- | ---------------------------------------------------------------- |
| WP-E9-001 | Public API Surface Map          | Gateway/runtime/memory/tool/policy/evidence/eval APIs are listed |
| WP-E9-002 | OpenAPI Baseline                | Initial OpenAPI contracts exist                                  |
| WP-E9-003 | Event Contract Baseline         | Domain events are defined                                        |
| WP-E9-004 | TypeScript SDK Baseline         | TS SDK can create run envelopes and submit events                |
| WP-E9-005 | Python SDK Baseline             | Python SDK can create run envelopes and submit events            |
| WP-E9-006 | Agent Adapter Contract          | External agents can be wrapped by Aegis                          |
| WP-E9-007 | Model Provider Adapter Contract | Mock and future real providers have a standard interface         |
| WP-E9-008 | MCP Adapter Design              | MCP compatibility strategy is documented                         |
| WP-E9-009 | Webhook Contract                | External systems can receive run/evidence/eval events            |
| WP-E9-010 | API Auth Placeholder            | Auth boundaries are specified even if not fully implemented      |

---

# E10 — Local Infrastructure & Developer Experience

| WP ID      | Title                         | Done when                                                               |
| ---------- | ----------------------------- | ----------------------------------------------------------------------- |
| WP-E10-001 | Local Docker Compose Stack    | Postgres, Redis, OPA, and OTEL collector are defined                    |
| WP-E10-002 | Environment Template          | `.env.example` covers required local variables                          |
| WP-E10-003 | Doctor Script                 | Repo health script verifies required files and tools                    |
| WP-E10-004 | Check Script                  | Lightweight checks validate schemas and scaffold health                 |
| WP-E10-005 | Dev Script                    | Local dependencies can be started                                       |
| WP-E10-006 | Migration Runner Plan         | Database migration strategy is defined                                  |
| WP-E10-007 | Seed Data Plan                | Demo tenant, agent, memory, and tools can be seeded                     |
| WP-E10-008 | Logging Standard              | Local logging rules and correlation IDs are defined                     |
| WP-E10-009 | Observability Baseline        | OpenTelemetry events and spans are specified                            |
| WP-E10-010 | Repository Automation Scripts | Repeatable scripts exist for setup, checks, and future issue generation |

---

# E11 — Admin UI & Demo Workflows

| WP ID      | Title                         | Done when                                                 |
| ---------- | ----------------------------- | --------------------------------------------------------- |
| WP-E11-001 | Admin UI Scope                | MVP UI pages and non-goals are defined                    |
| WP-E11-002 | Run Viewer Design             | UI can display run status and event timeline              |
| WP-E11-003 | Evidence Viewer Design        | UI can display evidence pack summary                      |
| WP-E11-004 | Memory Viewer Design          | UI can display retrieved and proposed memory              |
| WP-E11-005 | Tool Call Viewer Design       | UI can show proposed/allowed/blocked tool calls           |
| WP-E11-006 | Policy Decision Viewer Design | UI can show policy decisions and reasons                  |
| WP-E11-007 | Eval Result Viewer Design     | UI can show eval scores and failures                      |
| WP-E11-008 | Feedback Capture UI Design    | UI can capture rating and correction                      |
| WP-E11-009 | Sales/Ops Assistant Demo Spec | End-to-end demo script is documented                      |
| WP-E11-010 | Demo Console Baseline         | CLI or simple console demo can run the canonical workflow |

---

# E12 — Security, Governance & Release Readiness

| WP ID      | Title                            | Done when                                                   |
| ---------- | -------------------------------- | ----------------------------------------------------------- |
| WP-E12-001 | Security Policy                  | `SECURITY.md` reflects AI-specific risks                    |
| WP-E12-002 | Data Classification Rules        | Public/internal/confidential/restricted model is documented |
| WP-E12-003 | Secret Handling Rules            | Credentials are never exposed to models                     |
| WP-E12-004 | Approval Governance Rules        | Human approval and override rules are documented            |
| WP-E12-005 | Audit Retention Policy           | Evidence/run/event retention strategy is defined            |
| WP-E12-006 | Dependency Risk Baseline         | Dependency/security scanning plan exists                    |
| WP-E12-007 | CI Baseline                      | GitHub Actions runs scaffold checks                         |
| WP-E12-008 | Release Checklist                | MVP release criteria are explicit                           |
| WP-E12-009 | Documentation Completeness Check | Required docs are listed and checked                        |
| WP-E12-010 | MVP Readiness Review             | Final MVP readiness review template exists                  |

---

# MVP Critical Path

The shortest path to a credible MVP is:

```text
WP-E0-001 Product Charter
WP-E0-002 System Glossary
WP-E0-003 Architecture Overview
WP-E1-001 Run Envelope Schema
WP-E1-002 Run State Machine
WP-E1-003 Run Event Taxonomy
WP-E2-001 Memory Model Specification
WP-E2-003 Memory Candidate Schema
WP-E3-001 Tool Manifest Schema
WP-E3-005 Tool Broker Decision Flow
WP-E4-001 Policy Decision Schema
WP-E4-003 Base Tool Policy Pack
WP-E5-001 Evidence Pack Schema
WP-E6-001 Eval Case Schema
WP-E8-001 Business Outcome Schema
WP-E10-001 Local Docker Compose Stack
WP-E11-009 Sales/Ops Assistant Demo Spec
```

That critical path gives you the conceptual, schema, policy, and demo backbone.

---

# Recommended GitHub Labels

```text
epic
work-packet
task
docs
architecture
adr
runtime
memory
tools
policy
evidence
evals
feedback
outcomes
sdk
api
infra
security
ui
demo
mvp
blocked
needs-decision
```

---

# Recommended Milestones

| Milestone                    | Includes       |
| ---------------------------- | -------------- |
| M0 — Charter & Architecture  | E0             |
| M1 — Runtime Backbone        | E1             |
| M2 — Governed Memory         | E2             |
| M3 — Governed Tools & Policy | E3 + E4        |
| M4 — Evidence & Evals        | E5 + E6        |
| M5 — Feedback & Outcomes     | E7 + E8        |
| M6 — SDKs, Infra, Demo UI    | E9 + E10 + E11 |
| M7 — MVP Readiness           | E12            |

---

# Count Summary

| Type                       | Count |
| -------------------------- | ----: |
| Epics                      |    13 |
| Work packets               |   120 |
| Critical-path work packets |    17 |

This gives us enough structure to generate GitHub issues cleanly without improvising later.
