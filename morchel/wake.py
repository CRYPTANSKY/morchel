from __future__ import annotations

from .models import RankDecision, SealReport, WakeNotice


class WakeRoot:
    """Interrupt a human only when ranked evidence is reproducibly sealed."""

    name = "WAKE"
    permissions = frozenset({"read_rank_decision", "read_seal_report", "emit_human_notice"})

    def decide(self, rank: RankDecision, seal: SealReport) -> WakeNotice:
        if not seal.reproducible:
            return WakeNotice("morchel.wake.v1", rank.card_id, "HOLD", "source_not_reproducible")
        if rank.state != "WAKE_HUMAN":
            return WakeNotice("morchel.wake.v1", rank.card_id, "HOLD", "attention_threshold_not_met")
        return WakeNotice("morchel.wake.v1", rank.card_id, "WAKE_HUMAN", "sealed_evidence_passed_rank")
