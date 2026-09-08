# Architecture

MORCHEL uses a one-way, inspectable handoff between narrow roots.

```mermaid
flowchart LR
    O[Public observation] --> M[MINT]
    M --> C[EvidenceCard v1]
    C --> T[TRACE]
    T --> R[TraceReport v1]
    R --> K[RANK]
    K --> D[Attention state]
    D --> H[Human review]
```

## Root 01: MINT

Input: a supplied launch observation.  
Output: `morchel.evidence.v1`.

MINT validates public addresses, normalizes the observation, computes a stable card ID,
and records source coverage. It has no ability to interpret the evidence as a trade.

## Root 02: TRACE

Input: an `EvidenceCard`.  
Output: `morchel.trace.v1`.

TRACE tests explicit relationships and labels each one `reproduced`, `not_reproduced`,
`observed`, or `insufficient_evidence`. It emits no executable actions.

## Root 03: RANK

Inputs: an `EvidenceCard` and its `TraceReport`.  
Output: `morchel.rank.v1`.

RANK scores only inspectable properties: source coverage and the number of relationships
TRACE reproduced or observed. Its complete output vocabulary is `ARCHIVE`, `WATCH`, and
`WAKE_HUMAN`. These are attention states, not price predictions or trade instructions.

## Dormant roots

Roots 04 through 06 are intentionally undocumented until activated. This prevents the
story from outrunning the code and keeps each public release independently inspectable.

## Non-goals

- price forecasting;
- token scoring;
- order execution;
- wallet automation;
- autonomous financial decisions.
