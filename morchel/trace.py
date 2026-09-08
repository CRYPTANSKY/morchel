from __future__ import annotations

from .models import EvidenceCard, TraceFinding, TraceReport


class TraceRoot:
    """Test relationships in an EvidenceCard without predicting or acting."""

    name = "TRACE"
    permissions = frozenset({"read_evidence", "emit_report"})

    def inspect(self, card: EvidenceCard) -> TraceReport:
        findings: list[TraceFinding] = []

        if card.funded_by == card.fee_destination:
            findings.append(TraceFinding(
                relationship="funding_fee_convergence",
                status="reproduced",
                evidence=(card.funded_by, card.fee_destination),
            ))
        else:
            findings.append(TraceFinding(
                relationship="funding_fee_convergence",
                status="not_reproduced",
                evidence=(card.funded_by, card.fee_destination),
            ))

        findings.append(TraceFinding(
            relationship="creator_history",
            status="observed" if card.prior_launches else "insufficient_evidence",
            evidence=card.prior_launches,
        ))
        findings.append(TraceFinding(
            relationship="early_buyer_cluster",
            status="observed" if len(set(card.early_buyers)) >= 2 else "insufficient_evidence",
            evidence=tuple(sorted(set(card.early_buyers))),
        ))

        return TraceReport(
            schema_version="morchel.trace.v1",
            card_id=card.card_id,
            findings=tuple(findings),
            rejected_claims=("price_prediction", "trade_recommendation"),
        )

