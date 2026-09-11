from __future__ import annotations

from .mint import MintRoot
from .rank import RankRoot
from .replay import ReplayRoot
from .seal import SealRoot
from .trace import TraceRoot
from .wake import WakeRoot


def run_pipeline(raw: dict) -> dict:
    card = MintRoot().observe(raw)
    trace = TraceRoot().inspect(card)
    rank = RankRoot().decide(card, trace)
    replay = ReplayRoot().inspect(card, raw)
    seal = SealRoot().inspect(card, raw)
    wake = WakeRoot().decide(rank, seal)

    reproduced = any(f.status == "reproduced" for f in trace.findings)
    positions = {
        "MINT": "ACCEPT",
        "TRACE": "ACCEPT" if reproduced else "OBJECT",
        "RANK": "ACCEPT" if rank.state != "ARCHIVE" else "OBJECT",
        "REPLAY": "ACCEPT" if replay.recurrence_found else "OBJECT",
        "SEAL": "ACCEPT" if seal.reproducible else "OBJECT",
        "WAKE": "ACCEPT" if wake.state == "WAKE_HUMAN" else "OBJECT",
    }

    return {
        "network": "MORCHEL",
        "awake_roots": ["MINT", "TRACE", "RANK", "REPLAY", "SEAL", "WAKE"],
        "dormant_roots": 0,
        "evidence_card": card.as_dict(),
        "trace_report": trace.as_dict(),
        "rank_decision": rank.as_dict(),
        "replay_report": replay.as_dict(),
        "seal_report": seal.as_dict(),
        "wake_notice": wake.as_dict(),
        "root_positions": positions,
        "boundary": {"wallet_access": False, "signatures": False, "execution": False},
    }
