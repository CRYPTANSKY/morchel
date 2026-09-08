from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


def _address(value: str) -> str:
    value = value.strip().lower()
    if not value.startswith("0x") or len(value) < 8:
        raise ValueError(f"invalid public address: {value!r}")
    return value


@dataclass(frozen=True)
class LaunchObservation:
    chain: str
    token: str
    deployer: str
    funded_by: str
    prior_launches: tuple[str, ...] = ()
    early_buyers: tuple[str, ...] = ()
    fee_destination: str = ""
    source_urls: tuple[str, ...] = ()

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "LaunchObservation":
        required = ("chain", "token", "deployer", "funded_by", "fee_destination")
        missing = [key for key in required if not raw.get(key)]
        if missing:
            raise ValueError(f"missing required fields: {', '.join(missing)}")
        return cls(
            chain=str(raw["chain"]),
            token=str(raw["token"]),
            deployer=_address(str(raw["deployer"])),
            funded_by=_address(str(raw["funded_by"])),
            prior_launches=tuple(str(x) for x in raw.get("prior_launches", [])),
            early_buyers=tuple(_address(str(x)) for x in raw.get("early_buyers", [])),
            fee_destination=_address(str(raw["fee_destination"])),
            source_urls=tuple(str(x) for x in raw.get("source_urls", [])),
        )


@dataclass(frozen=True)
class EvidenceCard:
    schema_version: str
    card_id: str
    chain: str
    token: str
    deployer: str
    funded_by: str
    prior_launches: tuple[str, ...]
    early_buyers: tuple[str, ...]
    fee_destination: str
    source_urls: tuple[str, ...]
    source_coverage: float
    permissions: tuple[str, ...] = ("read_public_data", "emit_evidence")

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class TraceFinding:
    relationship: str
    status: str
    evidence: tuple[str, ...] = ()


@dataclass(frozen=True)
class TraceReport:
    schema_version: str
    card_id: str
    findings: tuple[TraceFinding, ...]
    rejected_claims: tuple[str, ...] = ()
    human_review_required: bool = True
    executable_actions: tuple[str, ...] = field(default_factory=tuple)

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)

