"""Stdlib HTTP API boundary for AIC Aegis MVP-A."""

from __future__ import annotations

from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
import json
import re

from .application import AegisMvpA, EvidenceWriter, InMemoryStore
from .domain import ActorType, InvariantViolation
from .serialization import to_plain


class AegisApiState:
    """Shared local API state for MVP-A."""

    def __init__(self, evidence_root: Path | None = None):
        self.store = InMemoryStore()
        self.app = AegisMvpA(store=self.store)
        self.app.evidence_writer = EvidenceWriter(self.store, evidence_root or Path('.aic/runtime/evidence'))
        self.system_actor = self.app.create_actor(ActorType.SYSTEM, 'MVP-A API System')
        self.default_human = self.app.create_actor(ActorType.HUMAN, 'MVP-A API Operator')
        self.default_model = self.app.create_actor(ActorType.MOCK_MODEL, 'MVP-A API Mock Model')


class AegisMvpARequestHandler(BaseHTTPRequestHandler):
    """Request handler for MVP-A local API."""

    server_version = 'AegisMvpAHTTP/0.1'

    @property
    def state(self) -> AegisApiState:
        return self.server.state  # type: ignore[attr-defined]

    def log_message(self, fmt: str, *args: Any) -> None:
        return

    def do_GET(self) -> None:  # noqa: N802
        try:
            path = urlparse(self.path).path
            if path == '/health':
                self._send_json(HTTPStatus.OK, {
                    'status': 'ok',
                    'project': 'AIC Aegis',
                    'product': 'AIC AI Reliability Control Plane',
                    'mvp': 'MVP-A',
                    'core_law': 'The model proposes; the platform disposes.',
                })
                return
            match = re.fullmatch(r'/v1/runs/([^/]+)', path)
            if match:
                run_id = match.group(1)
                run = self.state.store.runs.get(run_id)
                if run is None:
                    self._send_error(HTTPStatus.NOT_FOUND, f'Run not found: {run_id}')
                    return
                self._send_json(HTTPStatus.OK, {'run': to_plain(run)})
                return
            match = re.fullmatch(r'/v1/runs/([^/]+)/timeline', path)
            if match:
                timeline = self.state.app.get_timeline(match.group(1))
                self._send_json(HTTPStatus.OK, {'timeline': to_plain(timeline)})
                return
            self._send_error(HTTPStatus.NOT_FOUND, f'Unknown route: {path}')
        except InvariantViolation as exc:
            self._send_error(HTTPStatus.BAD_REQUEST, str(exc))
        except Exception as exc:  # pragma: no cover
            self._send_error(HTTPStatus.INTERNAL_SERVER_ERROR, str(exc))

    def do_POST(self) -> None:  # noqa: N802
        try:
            path = urlparse(self.path).path
            body = self._read_json()
            if path == '/v1/demo':
                result = self.state.app.run_demo(str(body.get('scenario', 'safe')), approve=bool(body.get('approve', False)))
                self._send_json(HTTPStatus.OK, {
                    'run': to_plain(result['run']),
                    'tool_action': to_plain(result['tool_action']),
                    'approval_request': to_plain(result['approval_request']),
                    'evidence_pack': to_plain(result['evidence_pack']),
                    'timeline': to_plain(result['timeline']),
                })
                return
            if path == '/v1/runs':
                run = self.state.app.create_run(
                    str(body.get('workflow', 'Governed Sales/Ops Follow-Up')),
                    str(body.get('purpose', 'MVP-A API Run')),
                    str(body.get('actor_id', self.state.default_human.actor_id)),
                )
                self._send_json(HTTPStatus.CREATED, {'run': to_plain(run)})
                return
            match = re.fullmatch(r'/v1/runs/([^/]+)/mock-proposals', path)
            if match:
                proposal, tool_action = self.state.app.propose_tool_action(
                    match.group(1),
                    str(body.get('actor_id', self.state.default_model.actor_id)),
                    str(body.get('scenario', 'safe')),
                )
                self._send_json(HTTPStatus.CREATED, {'proposal': to_plain(proposal), 'tool_action': to_plain(tool_action)})
                return
            match = re.fullmatch(r'/v1/tool-actions/([^/]+)/broker', path)
            if match:
                tool_action = self.state.app.broker_tool_action(match.group(1), str(body.get('actor_id', self.state.default_human.actor_id)))
                self._send_json(HTTPStatus.OK, {
                    'tool_action': to_plain(tool_action),
                    'policy_check': to_plain(self.state.store.policy_for_tool_action(tool_action.tool_action_id)),
                    'approval_request': to_plain(self.state.store.approval_for_tool_action(tool_action.tool_action_id)),
                })
                return
            match = re.fullmatch(r'/v1/approvals/([^/]+)/approve', path)
            if match:
                tool_action = self.state.app.approve_and_resume(
                    match.group(1),
                    str(body.get('actor_id', self.state.default_human.actor_id)),
                    str(body.get('rationale', 'Approved through MVP-A local API.')),
                )
                self._send_json(HTTPStatus.OK, {
                    'tool_action': to_plain(tool_action),
                    'approval_request': to_plain(self.state.store.approval_for_tool_action(tool_action.tool_action_id)),
                })
                return
            match = re.fullmatch(r'/v1/runs/([^/]+)/evidence-packs', path)
            if match:
                pack = self.state.app.generate_evidence_pack(match.group(1), str(body.get('actor_id', self.state.default_human.actor_id)))
                self._send_json(HTTPStatus.CREATED, {'evidence_pack': to_plain(pack)})
                return
            self._send_error(HTTPStatus.NOT_FOUND, f'Unknown route: {path}')
        except (InvariantViolation, ValueError) as exc:
            self._send_error(HTTPStatus.BAD_REQUEST, str(exc))
        except Exception as exc:  # pragma: no cover
            self._send_error(HTTPStatus.INTERNAL_SERVER_ERROR, str(exc))

    def _read_json(self) -> dict[str, Any]:
        length = int(self.headers.get('content-length', '0') or '0')
        if length <= 0:
            return {}
        raw = self.rfile.read(length)
        return json.loads(raw.decode('utf-8')) if raw else {}

    def _send_json(self, status: HTTPStatus, payload: dict[str, Any]) -> None:
        data = json.dumps(to_plain(payload), indent=2, sort_keys=True).encode('utf-8')
        self.send_response(status.value)
        self.send_header('content-type', 'application/json; charset=utf-8')
        self.send_header('content-length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_error(self, status: HTTPStatus, message: str) -> None:
        self._send_json(status, {'error': {'status': status.value, 'message': message}})


class AegisMvpAHTTPServer(ThreadingHTTPServer):
    def __init__(self, server_address: tuple[str, int], state: AegisApiState):
        self.state = state
        super().__init__(server_address, AegisMvpARequestHandler)


def create_server(host: str = '127.0.0.1', port: int = 8080, evidence_root: Path | None = None) -> AegisMvpAHTTPServer:
    return AegisMvpAHTTPServer((host, port), AegisApiState(evidence_root=evidence_root))
