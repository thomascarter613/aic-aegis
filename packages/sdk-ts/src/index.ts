export type RunStatus =
  | "created"
  | "running"
  | "waiting_for_approval"
  | "completed"
  | "failed"
  | "cancelled";

export interface RunEnvelope {
  run_id: string;
  tenant_id: string;
  user_id?: string;
  agent_id: string;
  agent_version?: string;
  task_type: string;
  status: RunStatus;
  trace_id?: string;
  evidence_pack_id?: string;
  input_refs?: string[];
  policy_context?: Record<string, unknown>;
  memory_context?: Record<string, unknown>;
  created_at: string;
  updated_at?: string;
}

export function createLocalRunEnvelope(input: {
  tenantId: string;
  agentId: string;
  taskType: string;
  userId?: string;
}): RunEnvelope {
  const now = new Date().toISOString();
  const id = `run_${crypto.randomUUID()}`;

  return {
    run_id: id,
    tenant_id: input.tenantId,
    user_id: input.userId,
    agent_id: input.agentId,
    task_type: input.taskType,
    status: "created",
    trace_id: `trace_${crypto.randomUUID()}`,
    input_refs: [],
    policy_context: {},
    memory_context: {},
    created_at: now,
    updated_at: now
  };
}
