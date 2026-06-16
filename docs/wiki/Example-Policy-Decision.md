# Example-Policy-Decision

Sample allow, deny, or approval-gated decision.

---

## Example

```json
{
  "policy_decision_id": "pd_001",
  "tenant_id": "tenant_aic",
  "run_id": "run_001",
  "checkpoint": "tool_broker",
  "decision": "require_approval",
  "reason": "email.send is high_write and externally visible.",
  "policy_id": "high_risk_tool_policy",
  "policy_version": "0.1.0"
}
```

---

## Meaning

The model proposed sending an email.

Aegis required approval before execution.

---

## North Star

Policy decisions make governance explainable.

---
