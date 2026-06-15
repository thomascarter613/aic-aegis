from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


@dataclass(frozen=True)
class RunEnvelope:
    run_id: str
    tenant_id: str
    agent_id: str
    task_type: str
    status: str
    created_at: str
    user_id: str | None = None
    trace_id: str | None = None
    evidence_pack_id: str | None = None
    input_refs: list[str] = field(default_factory=list)
    policy_context: dict[str, Any] = field(default_factory=dict)
    memory_context: dict[str, Any] = field(default_factory=dict)


def create_local_run_envelope(
    *,
    tenant_id: str,
    agent_id: str,
    task_type: str,
    user_id: str | None = None,
) -> RunEnvelope:
    now = datetime.now(timezone.utc).isoformat()
    return RunEnvelope(
        run_id=f"run_{uuid4()}",
        tenant_id=tenant_id,
        user_id=user_id,
        agent_id=agent_id,
        task_type=task_type,
        status="created",
        trace_id=f"trace_{uuid4()}",
        created_at=now,
    )
