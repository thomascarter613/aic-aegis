# Example-Memory-Record

Sample governed memory.

---

## Example

```json
{
  "memory_id": "mem_001",
  "tenant_id": "tenant_aic",
  "memory_type": "semantic",
  "subject": "customer:acme_hvac",
  "content": "Customer does not want emails sent without approval.",
  "source_type": "conversation",
  "source_ref": "run_001",
  "confidence": "medium",
  "sensitivity": "internal",
  "status": "active",
  "admission_decision_id": "mad_001"
}
```

---

## Meaning

This memory was admitted and can be retrieved if policy permits.

---

## North Star

Memory records make durable memory accountable.

---
