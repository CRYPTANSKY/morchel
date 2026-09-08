from __future__ import annotations

import hashlib
import json

from .models import EvidenceCard, LaunchObservation


class MintRoot:
    """Normalize one launch observation into a fixed, read-only evidence card."""

    name = "MINT"
    permissions = frozenset({"read_public_data", "emit_evidence"})

    def observe(self, raw: dict) -> EvidenceCard:
        observation = LaunchObservation.from_dict(raw)
        fingerprint = json.dumps(raw, sort_keys=True, separators=(",", ":"))
        card_id = hashlib.sha256(fingerprint.encode()).hexdigest()[:12]

        checks = [
            bool(observation.deployer),
            bool(observation.funded_by),
            bool(observation.fee_destination),
            bool(observation.early_buyers),
            bool(observation.source_urls),
        ]
        coverage = round(sum(checks) / len(checks), 2)

        return EvidenceCard(
            schema_version="morchel.evidence.v1",
            card_id=card_id,
            chain=observation.chain,
            token=observation.token,
            deployer=observation.deployer,
            funded_by=observation.funded_by,
            prior_launches=observation.prior_launches,
            early_buyers=observation.early_buyers,
            fee_destination=observation.fee_destination,
            source_urls=observation.source_urls,
            source_coverage=coverage,
        )

