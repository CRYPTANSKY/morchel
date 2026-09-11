# MORCHEL

**A six-root, read-only agent network for turning onchain observations into inspectable evidence.**

```text
observation -> MINT -> TRACE -> RANK -> REPLAY -> SEAL -> WAKE -> human
```

| Root | Responsibility | Authority |
|---|---|---|
| MINT | normalize supplied public observations | emit an evidence card |
| TRACE | challenge explicit relationships | emit a trace report |
| RANK | ration human attention | ARCHIVE / WATCH / WAKE_HUMAN |
| REPLAY | compare with supplied archive history | emit recurrence evidence |
| SEAL | verify that declared sources remain recoverable | seal or reject the packet |
| WAKE | enforce the final interruption boundary | notify a human or HOLD |

All six roots are awake. None can predict price, access wallets, sign messages, place trades,
or move funds. `WAKE_HUMAN` is an attention state, never an execution instruction.

## Run

Requires Python 3.11+ and no third-party packages.

```bash
python -m morchel examples/launch.json
python -m morchel examples/case_001.json
python -m unittest discover -s tests -v
```

## CASE 001

The first six-root fixture deliberately ends in disagreement: `3 ACCEPT / 3 OBJECT`.
RANK crosses its threshold, but SEAL cannot recover one declared source, so WAKE returns `HOLD`.
Read the complete walkthrough in [docs/case-001.md](docs/case-001.md).

## Permission boundary

| Capability | Status |
|---|---|
| Read supplied public data | Allowed |
| Save inspectable evidence | Allowed |
| Produce reports and attention states | Allowed |
| Access a wallet | Forbidden |
| Sign a transaction | Forbidden |
| Place a trade or move funds | Forbidden |

See [SECURITY.md](SECURITY.md), [architecture](docs/architecture.md), and [CHANGELOG.md](CHANGELOG.md).

## Status

`ROOT 01 / MINT: AWAKE`  
`ROOT 02 / TRACE: AWAKE`  
`ROOT 03 / RANK: AWAKE`  
`ROOT 04 / REPLAY: AWAKE`  
`ROOT 05 / SEAL: AWAKE`  
`ROOT 06 / WAKE: AWAKE`

This repository is an educational prototype. All included observations are synthetic fixtures.
It is not financial advice and it is not a trading system.
