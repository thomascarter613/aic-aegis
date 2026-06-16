"""CLI/demo entry point for the MVP-A local proof loop."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .application import AegisMvpA, EvidenceWriter, InMemoryStore
from .serialization import to_plain


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the AIC Aegis MVP-A local proof-loop demo.")
    parser.add_argument(
        "scenario",
        choices=["safe", "risky", "blocked"],
        help="MVP-A demo scenario to execute.",
    )
    parser.add_argument(
        "--approve",
        action="store_true",
        help="Approve a risky approval-gated scenario and resume mock execution.",
    )
    parser.add_argument(
        "--evidence-root",
        default=".aic/runtime/evidence",
        help="Directory for generated evidence artifacts.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    store = InMemoryStore()
    app = AegisMvpA(store=store)
    app.evidence_writer = EvidenceWriter(store, Path(args.evidence_root))

    result = app.run_demo(args.scenario, approve=args.approve)

    summary = {
        "scenario": args.scenario,
        "approved": args.approve,
        "run_id": result["run"].run_id,
        "run_status": result["run"].status.value,
        "tool_action_id": result["tool_action"].tool_action_id,
        "tool_action_status": result["tool_action"].status.value,
        "approval_request_id": (
            result["approval_request"].approval_request_id if result["approval_request"] else None
        ),
        "approval_status": (
            result["approval_request"].status.value if result["approval_request"] else None
        ),
        "evidence_pack_id": result["evidence_pack"].evidence_pack_id,
        "evidence_artifacts": len(result["evidence_pack"].artifacts),
        "timeline_items": len(result["timeline"].items),
    }

    print(json.dumps(to_plain(summary), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
