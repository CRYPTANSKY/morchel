import json
import unittest
from pathlib import Path

from morchel import MintRoot, RankRoot, TraceRoot, run_pipeline


ROOT = Path(__file__).parents[1]


class MorchelTests(unittest.TestCase):
    def load(self, name="launch.json"):
        return json.loads((ROOT / "examples" / name).read_text())

    def test_mint_emits_fixed_schema(self):
        card = MintRoot().observe(self.load())
        self.assertEqual(card.schema_version, "morchel.evidence.v1")
        self.assertEqual(card.permissions, ("read_public_data", "emit_evidence"))
        self.assertEqual(card.source_coverage, 1.0)

    def test_trace_has_no_executable_actions(self):
        report = TraceRoot().inspect(MintRoot().observe(self.load()))
        self.assertTrue(report.human_review_required)
        self.assertEqual(report.executable_actions, ())

    def test_all_six_roots_are_awake_and_read_only(self):
        result = run_pipeline(self.load())
        self.assertEqual(result["awake_roots"], ["MINT", "TRACE", "RANK", "REPLAY", "SEAL", "WAKE"])
        self.assertEqual(result["dormant_roots"], 0)
        self.assertFalse(any(result["boundary"].values()))

    def test_rank_emits_attention_state_not_trade(self):
        card = MintRoot().observe(self.load())
        decision = RankRoot().decide(card, TraceRoot().inspect(card))
        self.assertIn(decision.state, RankRoot.states)
        self.assertEqual(decision.executable_actions, ())

    def test_unrecoverable_source_blocks_wake_human(self):
        result = run_pipeline(self.load("case_001.json"))
        self.assertEqual(result["rank_decision"]["state"], "WAKE_HUMAN")
        self.assertFalse(result["seal_report"]["reproducible"])
        self.assertEqual(result["wake_notice"]["state"], "HOLD")
        self.assertEqual(result["wake_notice"]["reason"], "source_not_reproducible")
        self.assertEqual(list(result["root_positions"].values()).count("ACCEPT"), 3)
        self.assertEqual(list(result["root_positions"].values()).count("OBJECT"), 3)


if __name__ == "__main__": unittest.main()
