import json
import unittest
from pathlib import Path

from morchel import MintRoot, TraceRoot, RankRoot, run_pipeline


FIXTURE = Path(__file__).parents[1] / "examples" / "launch.json"


class MorchelTests(unittest.TestCase):
    def setUp(self):
        self.raw = json.loads(FIXTURE.read_text())

    def test_mint_emits_fixed_schema(self):
        card = MintRoot().observe(self.raw)
        self.assertEqual(card.schema_version, "morchel.evidence.v1")
        self.assertEqual(card.permissions, ("read_public_data", "emit_evidence"))
        self.assertEqual(card.source_coverage, 1.0)

    def test_trace_has_no_executable_actions(self):
        report = TraceRoot().inspect(MintRoot().observe(self.raw))
        self.assertTrue(report.human_review_required)
        self.assertEqual(report.executable_actions, ())

    def test_pipeline_boundary_is_read_only(self):
        result = run_pipeline(self.raw)
        self.assertEqual(result["awake_roots"], ["MINT", "TRACE", "RANK"])
        self.assertFalse(any(result["boundary"].values()))

    def test_rank_emits_attention_state_not_trade(self):
        card = MintRoot().observe(self.raw)
        report = TraceRoot().inspect(card)
        decision = RankRoot().decide(card, report)
        self.assertIn(decision.state, RankRoot.states)
        self.assertEqual(decision.executable_actions, ())
        self.assertEqual(decision.state, "WAKE_HUMAN")


if __name__ == "__main__":
    unittest.main()
