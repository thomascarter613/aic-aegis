"""Domain model for AIC Aegis MVP-A.

The domain layer is deliberately stdlib-only. It must not depend on HTTP,
database, model SDK, queue, cloud, or external tool libraries.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4


SCHEMA_VERSION = "mvp-a.v1"


class InvariantViolation(RuntimeError):
    """Raised when an Aegis MVP-A invariant would be violated."""


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex}"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


class ActorType(str, Enum):
    HUMAN = "human"
    MOCK_MODEL = "mock_model"
    SERVICE = "service"
    WORKER = "worker"
    SYSTEM = "system"


class RunStatus(str, Enum):
    CREATED = "created"
    RUNNING = "running"
    AWAITING_APPROVAL = "awaiting_approval"
    COMPLETED = "completed"
    BLOCKED = "blocked"
    FAILED = "failed"
    CANCELLED = "cancelled"


class ProposalType(str, Enum):
    TOOL_ACTION = "tool_action"


class ProposalStatus(str, Enum):
    SUBMITTED = "submitted"
    UNDER_POLICY_REVIEW = "under_policy_review"
    DISPOSITIONED = "dispositioned"
    APPROVAL_REQUIRED = "approval_required"
    BLOCKED = "blocked"
    MOCK_EXECUTED = "mock_executed"
    CANCELLED = "cancelled"


class ToolActionStatus(str, Enum):
    PROPOSED = "proposed"
    POLICY_CHECKED = "policy_checked"
    APPROVAL_REQUIRED = "approval_required"
    APPROVED = "approved"
    REJECTED = "rejected"
    MOCK_EXECUTED = "mock_executed"
    BLOCKED = "blocked"
    FAILED = "failed"


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Disposition(str, Enum):
    ALLOW = "allow"
    MOCK = "mock"
    BLOCK = "block"
    APPROVAL_REQUIRED = "approval_required"
    DEFER = "defer"


class ApprovalStatus(str, Enum):
    REQUESTED = "requested"
    APPROVED = "approved"
    REJECTED = "rejected"
    EXPIRED = "expired"
    CANCELLED = "cancelled"


class ApprovalDecision(str, Enum):
    APPROVED = "approved"
    REJECTED = "rejected"


class EventType(str, Enum):
    RUN_CREATED = "RunCreated"
    RUN_EVENT_RECORDED = "RunEventRecorded"
    PROPOSAL_SUBMITTED = "ProposalSubmitted"
    TOOL_ACTION_PROPOSED = "ToolActionProposed"
    POLICY_CHECK_COMPLETED = "PolicyCheckCompleted"
    TOOL_ACTION_DISPOSITIONED = "ToolActionDispositioned"
    APPROVAL_GATE_REQUESTED = "ApprovalGateRequested"
    APPROVAL_DECISION_RECORDED = "ApprovalDecisionRecorded"
    TOOL_ACTION_MOCK_EXECUTED = "ToolActionMockExecuted"
    TOOL_ACTION_BLOCKED = "ToolActionBlocked"
    EVIDENCE_PACK_GENERATED = "EvidencePackGenerated"
    TIMELINE_GENERATED = "TimelineGenerated"


@dataclass(slots=True)
class Actor:
    actor_id: str
    actor_type: ActorType
    display_name: str
    external_ref: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    schema_version: str = SCHEMA_VERSION


@dataclass(slots=True)
class Run:
    run_id: str
    workflow: str
    purpose: str
    status: RunStatus
    initiating_actor_id: str
    created_at: str
    updated_at: str
    metadata: dict[str, Any] = field(default_factory=dict)
    schema_version: str = SCHEMA_VERSION


@dataclass(slots=True)
class RunEvent:
    event_id: str
    run_id: str
    event_type: EventType
    event_version: int
    occurred_at: str
    actor_id: str | None
    payload: dict[str, Any]
    correlation_id: str | None = None
    causation_id: str | None = None
    schema_version: str = SCHEMA_VERSION


@dataclass(slots=True)
class Proposal:
    proposal_id: str
    run_id: str
    proposed_by_actor_id: str
    proposal_type: ProposalType
    status: ProposalStatus
    created_at: str
    summary: str
    payload: dict[str, Any]
    source: dict[str, Any]
    schema_version: str = SCHEMA_VERSION


@dataclass(slots=True)
class ToolAction:
    tool_action_id: str
    run_id: str
    proposal_id: str
    tool_name: str
    operation: str
    target: str
    arguments: dict[str, Any]
    status: ToolActionStatus
    created_at: str
    updated_at: str
    mock_result: dict[str, Any] | None = None
    schema_version: str = SCHEMA_VERSION


@dataclass(slots=True)
class PolicyCheck:
    policy_check_id: str
    run_id: str
    proposal_id: str
    tool_action_id: str
    checked_at: str
    policy_engine: str
    input_ref: str | None
    risk_level: RiskLevel
    matched_controls: list[str]
    disposition: Disposition
    rationale: str
    schema_version: str = SCHEMA_VERSION


@dataclass(slots=True)
class ApprovalRequest:
    approval_request_id: str
    run_id: str
    proposal_id: str
    tool_action_id: str
    requested_by_actor_id: str
    status: ApprovalStatus
    rationale: str
    created_at: str
    expires_at: str | None = None
    schema_version: str = SCHEMA_VERSION


@dataclass(slots=True)
class ApprovalDecisionRecord:
    approval_decision_id: str
    approval_request_id: str
    decided_by_actor_id: str
    decision: ApprovalDecision
    rationale: str
    decided_at: str
    schema_version: str = SCHEMA_VERSION


@dataclass(slots=True)
class EvidenceArtifact:
    artifact_id: str
    artifact_type: str
    record_ref: str
    uri: str
    sha256: str | None = None


@dataclass(slots=True)
class EvidencePack:
    evidence_pack_id: str
    run_id: str
    generated_at: str
    generated_by_actor_id: str
    manifest_version: str
    artifacts: list[EvidenceArtifact]
    summary: str = ""
    schema_version: str = SCHEMA_VERSION


@dataclass(slots=True)
class TimelineItem:
    timeline_item_id: str
    occurred_at: str
    event_type: EventType
    title: str
    description: str
    record_refs: list[dict[str, str]]


@dataclass(slots=True)
class Timeline:
    run_id: str
    generated_at: str
    items: list[TimelineItem]
    schema_version: str = SCHEMA_VERSION
