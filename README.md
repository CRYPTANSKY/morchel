# MORCHEL

**A read-only agent network for turning onchain activity into inspectable evidence.**

MORCHEL is an experiment in narrow agents, narrow permissions, and visible handoffs.
The prototype currently exposes three roots:

```text
launch event -> MINT -> evidence card -> TRACE -> relationship report -> RANK -> human
```

- **MINT** reconstructs the wallet behind a launch.
- **TRACE** challenges the resulting evidence card by looking for reproducible relationships.
- **RANK** reduces surviving evidence to `ARCHIVE`, `WATCH`, or `WAKE_HUMAN`.
- **Three additional roots remain dormant.** Their responsibilities will be published as they wake.

MORCHEL does not predict price, place trades, hold keys, sign messages, or move funds.

## Run the prototype

Requires Python 3.11+ and no third-party packages.

```bash
python -m morchel examples/launch.json
```

Expected output is a JSON relationship report. The report includes the original evidence,
TRACE findings, source coverage, and the mandatory `human_review_required` flag.

Run the tests:

```bash
python -m unittest discover -s tests -v
```

## Why three roots?

One model should not research, judge, and act in the same context. MORCHEL splits the work:

1. MINT normalizes observable facts into a fixed schema.
2. TRACE attempts to reproduce or reject the relationships implied by those facts.
3. RANK decides whether the surviving evidence deserves scarce human attention.
4. A human decides what the report means.

Every handoff is JSON-serializable and inspectable. No freeform agent output is trusted as a command.

## Permission boundary

| Capability | Status |
|---|---|
| Read supplied public data | Allowed |
| Save evidence locally | Allowed |
| Produce a report | Allowed |
| Access a wallet | Forbidden |
| Sign a transaction | Forbidden |
| Place a trade | Forbidden |
| Move funds | Forbidden |

See [SECURITY.md](SECURITY.md) and [docs/architecture.md](docs/architecture.md).

## Current status

`ROOT 01 / MINT: AWAKE`  
`ROOT 02 / TRACE: AWAKE`  
`ROOT 03 / RANK: AWAKE`  
`ROOT 04-06: DORMANT`

This repository is an educational prototype. It is not financial advice and is not a trading system.
