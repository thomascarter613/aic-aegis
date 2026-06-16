"""Serialization helpers for Aegis MVP-A domain objects."""

from __future__ import annotations

from dataclasses import asdict, is_dataclass
from enum import Enum
from pathlib import Path
from typing import Any
import hashlib
import json


def to_plain(value: Any) -> Any:
    """Convert dataclasses/enums into JSON-friendly plain objects."""
    if isinstance(value, Enum):
        return value.value
    if is_dataclass(value):
        return {k: to_plain(v) for k, v in asdict(value).items()}
    if isinstance(value, dict):
        return {str(k): to_plain(v) for k, v in value.items()}
    if isinstance(value, list):
        return [to_plain(item) for item in value]
    return value


def write_json(path: Path, value: Any) -> str:
    """Write JSON and return the SHA-256 digest of the written bytes."""
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(to_plain(value), indent=2, sort_keys=True).encode("utf-8")
    path.write_bytes(payload + b"\n")
    return hashlib.sha256(payload).hexdigest()
