from __future__ import annotations

from .models import EvidenceCard, ReplayReport


class ReplayRoot:
    """Compare a card with supplied archive matches; never infer missing history."""

    name = "REPLAY"
    permissions = frozenset({"read_evidence", "read_local_archive", "emit_replay_report"})

    def inspect(self, card: EvidenceCard, raw: dict) -> ReplayReport:
        matches = tuple(str(item) for item in raw.get("archive_matches", ()))
        return ReplayReport("morchel.replay.v1", card.card_id, matches, bool(matches))
