from __future__ import annotations

from .mint import MintRoot
from .trace import TraceRoot
from .rank import RankRoot


def run_pipeline(raw: dict) -> dict:
    card = MintRoot().observe(raw)
    report = TraceRoot().inspect(card)
    decision = RankRoot().decide(card, report)
    return {
        "network": "MORCHEL",
        "awake_roots": ["MINT", "TRACE", "RANK"],
        "dormant_roots": 3,
        "evidence_card": card.as_dict(),
        "trace_report": report.as_dict(),
        "rank_decision": decision.as_dict(),
        "boundary": {
            "wallet_access": False,
            "signatures": False,
            "execution": False,
        },
    }
