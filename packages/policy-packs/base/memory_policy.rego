package aegis.memory_policy

default decision := {
  "decision": "deny",
  "reason": "Memory write did not meet admission rules."
}

decision := {
  "decision": "allow",
  "reason": "Memory candidate has source, reason, confidence, and acceptable sensitivity."
} if {
  input.source_ref != ""
  input.write_reason != ""
  input.confidence >= 0.75
  input.sensitivity != "restricted"
}

decision := {
  "decision": "require_approval",
  "reason": "Low-confidence or confidential memory requires human confirmation."
} if {
  input.confidence < 0.75
}

decision := {
  "decision": "require_approval",
  "reason": "Confidential memory requires confirmation."
} if {
  input.sensitivity == "confidential"
}

decision := {
  "decision": "deny",
  "reason": "Restricted memory writes are blocked by default."
} if {
  input.sensitivity == "restricted"
}
