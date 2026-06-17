"""Command-line server entry point for the MVP-A HTTP API."""

from __future__ import annotations

import argparse
from pathlib import Path

from .http_api import create_server


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Run the AIC Aegis MVP-A local HTTP API.')
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8080)
    parser.add_argument('--evidence-root', default='.aic/runtime/evidence')
    args = parser.parse_args(argv)
    server = create_server(args.host, args.port, Path(args.evidence_root))
    print(f'AIC Aegis MVP-A API listening on http://{args.host}:{args.port}')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down AIC Aegis MVP-A API.')
    finally:
        server.server_close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
