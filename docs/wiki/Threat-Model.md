# Threat Model

Threats specific to agentic AI control planes.

---

## Purpose

Threat Model identifies risks Aegis must control.

---

## Key Threats

| Threat               | Description                            |
| -------------------- | -------------------------------------- |
| Prompt Injection     | Model manipulated into unsafe behavior |
| Tool Abuse           | AI calls risky tools incorrectly       |
| Memory Poisoning     | Bad memory admitted                    |
| Data Leakage         | Sensitive data exposed                 |
| Cross-Tenant Leakage | Tenant data mixed                      |
| Policy Bypass        | Action avoids runtime policy           |
| Evidence Tampering   | Proof altered or incomplete            |
| Over-Autonomy        | AI acts beyond trust level             |
| Hallucinated Action  | AI invents facts or commitments        |
| Outcome Inflation    | Value claims exaggerated               |

---

## North Star

Threat modeling keeps Aegis honest about AI risk.
