# Example-Tool-Manifest

Sample tool declaration.

---

## Example

```json
{
  "tool_id": "email.create_draft",
  "name": "Create Email Draft",
  "version": "0.1.0",
  "risk_class": "low_write",
  "description": "Creates a draft email without sending.",
  "permissions_required": ["email:draft"],
  "approval_required": "policy_based",
  "status": "active"
}
```

---

## Meaning

This tool is low risk because it creates a draft but does not send externally.

---

## North Star

Tool manifests let Aegis know what it is authorizing.

---
