from __future__ import annotations

from .models import EvidenceCard, SealReport


class SealRoot:
    """Freeze source coverage and block claims whose sources cannot be recovered."""

    name = "SEAL"
    permissions = frozenset({"read_evidence", "verify_sources", "emit_seal_report"})

    def inspect(self, card: EvidenceCard, raw: dict) -> SealReport:
        declared = set(card.source_urls)
        recovered = set(str(url) for url in raw.get("recoverable_sources", card.source_urls))
        missing = tuple(sorted(declared - recovered))
        present = tuple(sorted(declared & recovered))
        return SealReport(
            "morchel.seal.v1", card.card_id, present, missing,
            reproducible=bool(declared) and not missing,
        )
