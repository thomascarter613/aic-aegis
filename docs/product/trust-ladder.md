# Aegis Trust and Autonomy Ladder

Status: proposed  
Codename: Aegis  
Product: AIC AI Reliability Control Plane  
Last updated: 2026-06-15  

## Purpose

The Trust and Autonomy Ladder defines how Aegis should gradually increase what AI systems are allowed to do.

Aegis should help organizations move AI workflows up the ladder safely.

## Ladder Summary

| Level | Name | AI Capability | Required Controls |
|---|---|---|---|
| 0 | Observe Only | AI output is logged/evaluated but does not act | run identity, evidence |
| 1 | Draft Only | AI drafts summaries/recommendations | evidence, feedback |
| 2 | Low-Risk Reversible Action | AI performs reversible actions | tool broker, policy |
| 3 | Approval-Gated Action | AI proposes consequential actions | approval, evidence |
| 4 | Policy-Bounded Autonomy | AI acts within strict limits | policy, evals, monitoring |
| 5 | High Autonomy | AI acts in defined workflows with rollback/audit | mature controls |
| 6 | Prohibited/Critical | AI cannot act autonomously | deny by default |

## MVP Target

MVP should demonstrate Levels 1–3:

- draft useful response,
- allow safe draft creation,
- block or approval-gate email send.

## Product Use

Every workflow should declare its autonomy level. Every tenant should eventually configure maximum autonomy by workflow, tool, and data class.

## Final Principle

Aegis does not maximize autonomy. Aegis maximizes justified autonomy.

