package aegis.tool_policy

default decision := {
  "decision": "deny",
  "reason": "No allow rule matched."
}

decision := {
  "decision": "allow",
  "reason": "Read-only tool is allowed for this role and data class."
} if {
  input.tool.risk_level == "read_only"
  input.actor.role in input.tool.allowed_roles
  input.data_class in input.tool.data_classes_allowed
}

decision := {
  "decision": "require_approval",
  "reason": "Tool has side effects and requires approval."
} if {
  input.tool.side_effect == true
  input.tool.requires_approval != "never"
}

decision := {
  "decision": "deny",
  "reason": "Restricted data is blocked by default."
} if {
  input.data_class == "restricted"
  not input.explicit_restricted_data_grant
}
