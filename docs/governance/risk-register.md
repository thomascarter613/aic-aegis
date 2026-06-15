# Aegis Risk Register

Status: proposed  
Codename: Aegis  
Product: AIC AI Reliability Control Plane  
Last updated: 2026-06-15  

## Purpose

This register identifies key Aegis risks and mitigation themes. It should evolve as implementation progresses.

## Risk Scale

Severity: Low, Medium, High, Critical  
Likelihood: Low, Medium, High  
Status: Open, Mitigated, Accepted, Deferred, Needs Review

## Initial Risks

| Risk ID | Risk | Severity | Likelihood | Status |
|---|---|---:|---:|---|
| RISK-AI-001 | Prompt injection manipulates model behavior | High | High | Open |
| RISK-AI-002 | Tool injection manipulates tool calls | High | Medium | Open |
| RISK-AI-003 | Memory poisoning corrupts future behavior | High | Medium | Open |
| RISK-AI-004 | Model hallucination produces incorrect output | Medium | High | Open |
| RISK-AI-005 | Unsafe output is trusted without validation | High | Medium | Open |
| RISK-TOOL-001 | High-risk tool executes without approval | Critical | Medium | Open |
| RISK-TOOL-002 | Tool credentials leak to model | Critical | Low | Open |
| RISK-TOOL-003 | Tool schema accepts unsafe input | High | Medium | Open |
| RISK-POL-001 | Policy bypass through missing checkpoint | High | Medium | Open |
| RISK-POL-002 | Policy service unavailable and action fails open | High | Medium | Open |
| RISK-MEM-001 | Memory written without source/provenance | High | Medium | Open |
| RISK-MEM-002 | Restricted memory retrieved into prompt | Critical | Low | Open |
| RISK-EVD-001 | Evidence pack missing critical decision records | High | Medium | Open |
| RISK-EVD-002 | Evidence export leaks sensitive data | Critical | Low | Open |
| RISK-TEN-001 | Cross-tenant data leakage | Critical | Low | Open |
| RISK-SEC-001 | Secrets committed or logged | Critical | Medium | Open |
| RISK-EVAL-001 | Bad eval gives false confidence | Medium | Medium | Open |
| RISK-OUT-001 | Outcome/ROI overclaimed | Medium | Medium | Open |
| RISK-OPS-001 | Silent failure hides governance gap | High | Medium | Open |
| RISK-ARCH-001 | Domain core becomes coupled to infrastructure | High | Medium | Open |
| RISK-SCOPE-001 | MVP scope becomes too broad to ship | High | High | Open |

## Mitigation Themes

Prompt/tool injection:

- tool broker,
- schema validation,
- policy checkpoints,
- red-team evals,
- evidence logging.

Memory poisoning:

- Memory Candidate stage,
- Memory Admission Gate,
- provenance,
- confidence,
- sensitivity,
- human review,
- correction/supersession.

Unsafe tool execution:

- risk classes,
- policy decisions,
- approval gates,
- denied tools cannot execute,
- evidence records.

Policy failure:

- fail closed for high-risk actions,
- policy failure events,
- degradation rules.

Evidence leakage:

- redaction policy,
- audience-specific evidence views,
- export logging.

Tenant leakage:

- tenant_id everywhere,
- tenant-scoped repositories,
- isolation tests,
- optional RLS later.

Scope overbuild:

- thin vertical slice,
- golden workflow,
- explicit defer list,
- MVP-A/MVP-B sequencing.

## Final Principle

Aegis is successful only if its risks are visible, controlled, tested, and evidenced.

