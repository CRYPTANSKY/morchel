# Security boundary

MORCHEL is deliberately read-only.

## The prototype will never

- request or store seed phrases, private keys, API secrets, or session cookies;
- construct, sign, simulate, submit, or relay transactions;
- connect to a brokerage or exchange account;
- place orders or make autonomous financial decisions;
- treat an agent's freeform text as executable instructions.

## Data model

The CLI reads one local JSON document supplied by the operator. All six roots return fixed,
JSON-serializable dataclasses. Every handoff accepts only validated structured data, never
arbitrary instructions. Every root exposes an empty `executable_actions` tuple.

SEAL fails closed: if any declared source cannot be recovered, WAKE returns `HOLD` even when
RANK previously returned `WAKE_HUMAN`.

## Reporting

Please report vulnerabilities through GitHub's private vulnerability reporting feature.
Do not include real secrets, private wallet data, or personal information in an issue.
