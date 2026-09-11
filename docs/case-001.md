# CASE 001: evidence held

CASE 001 is a synthetic fixture for the first disagreement across all six roots.
It is not a real token, wallet investigation, profit claim, or trading result.

## Result

| Root | Position | Reason |
|---|---|---|
| MINT | ACCEPT | the supplied observation can be normalized |
| TRACE | ACCEPT | funding and fee destination converge |
| RANK | ACCEPT | the inspectable evidence crosses the attention threshold |
| REPLAY | OBJECT | no archive match was supplied |
| SEAL | OBJECT | one declared source cannot be recovered |
| WAKE | OBJECT | an unsealed packet cannot interrupt a human |

Final state: `HOLD` (`3 ACCEPT / 3 OBJECT`).

Run it with:

```bash
python -m morchel examples/case_001.json
```

The fixture exists to prove a boundary: a high RANK score is necessary but insufficient.
If SEAL cannot reproduce every declared source, WAKE must remain silent.
