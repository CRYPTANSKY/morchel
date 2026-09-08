# Architecture

MORCHEL uses a one-way, inspectable handoff between narrow roots.

```mermaid
flowchart LR
    O[Public observation] --> M[MINT]
    M --> C[EvidenceCard v1]
    C --> T[TRACE]
    T --> R[TraceReport v1]
    R --> H[Human review]
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

## Dormant roots

Roots 03 through 06 are intentionally undocumented until activated. This prevents the
story from outrunning the code and keeps each public release independently inspectable.

## Non-goals

- price forecasting;
- token scoring;
- order execution;
- wallet automation;
- autonomous financial decisions.

