from __future__ import annotations

from .models import EvidenceCard, RankDecision, TraceReport


class RankRoot:
    """Reduce verified evidence to an attention state, never a trade signal."""

    name = "RANK"
    permissions = frozenset({"read_evidence", "read_trace_report", "emit_attention_state"})
    states = ("ARCHIVE", "WATCH", "WAKE_HUMAN")

    def decide(self, card: EvidenceCard, report: TraceReport) -> RankDecision:
        score = 0
        reasons: list[str] = []

        if card.source_coverage >= 0.8:
            score += 30
            reasons.append("strong_source_coverage")

        reproduced = sum(f.status == "reproduced" for f in report.findings)
        observed = sum(f.status == "observed" for f in report.findings)
        score += reproduced * 30 + observed * 15

        if reproduced:
            reasons.append("reproducible_relationship")
        if observed >= 2:
            reasons.append("multiple_observed_patterns")

        score = min(score, 100)
        if score >= 80:
            state = "WAKE_HUMAN"
        elif score >= 45:
            state = "WATCH"
        else:
            state = "ARCHIVE"

        return RankDecision(
            schema_version="morchel.rank.v1",
            card_id=card.card_id,
            state=state,
            score=score,
            reasons=tuple(reasons),
            human_review_required=state == "WAKE_HUMAN",
        )
