from __future__ import annotations

from .mint import MintRoot
from .trace import TraceRoot


def run_pipeline(raw: dict) -> dict:
    card = MintRoot().observe(raw)
    report = TraceRoot().inspect(card)
    return {
        "network": "MORCHEL",
        "awake_roots": ["MINT", "TRACE"],
        "dormant_roots": 4,
        "evidence_card": card.as_dict(),
        "trace_report": report.as_dict(),
        "boundary": {
            "wallet_access": False,
            "signatures": False,
            "execution": False,
        },
    }

