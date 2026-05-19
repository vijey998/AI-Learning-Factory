import json
import subprocess
import sys
import unittest
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
import milestone_labs as labs


class MilestoneLabTests(unittest.TestCase):
    def test_all_labs_return_complete_experiment_records(self):
        records = labs.run("all")
        self.assertEqual([r["lab"] for r in records], [f"{i:02d}" for i in range(1, 16)])
        for record in records:
            self.assertEqual(record["status"], "reference-complete")
            self.assertIn(record["execution_mode"], ("measured-cpu", "simulated-cpu"))
            self.assertIn("environment", record)
            self.assertIn("result", record)
            self.assertEqual(record["failures"], [])

    def test_tokenizer_unicode_specials_and_unseen_text(self):
        tokenizer = labs.BytePairTokenizer.train(["banana", "bandana", "🧠 banana"])
        text = "unseen λ <eos> 🧠"
        pieces = tokenizer.encode(text)
        self.assertEqual(tokenizer.decode(pieces), text)
        self.assertIn("<eos>", pieces)

    def test_attention_is_causal(self):
        result = labs.lab03()["result"]
        self.assertTrue(result["causal_invariance"])
        self.assertEqual(result["future_probability_max"], 0.0)

    def test_checkpoint_resume_is_exact(self):
        self.assertTrue(labs.lab05()["result"]["resume_matches"])
        self.assertGreater(labs.lab05()["result"]["overfit_reduction"], 0)

    def test_tiled_reference_handles_irregular_sizes(self):
        x = np.linspace(-2, 2, 101, dtype=np.float32)
        bias = np.ones_like(x) * .2
        got = labs.tiled_fused_reference(x, bias, tile=16)
        np.testing.assert_allclose(got, np.maximum(x + bias, 0) ** 2)

    def test_cached_and_uncached_attention_match(self):
        self.assertTrue(labs.lab08()["result"]["equivalent"])

    def test_quantization_size_and_error(self):
        result = labs.lab09()["result"]
        self.assertLess(result["packed_weight_bytes"] + result["metadata_bytes"],
                        result["float_weight_bytes"])
        self.assertLess(result["mean_absolute_error"], .1)
        self.assertFalse(result["speedup_claimed"])

    def test_scheduler_cleans_cancelled_request_and_obeys_bound(self):
        result = labs.lab10()["result"]
        self.assertTrue(result["cancel_cleanup"])
        self.assertTrue(result["bounded"])

    def test_simulations_are_labelled(self):
        for function in (labs.lab07, labs.lab10, labs.lab11, labs.lab15):
            self.assertEqual(function()["execution_mode"], "simulated-cpu")

    def test_cli_emits_one_json_record(self):
        completed = subprocess.run(
            [sys.executable, str(ROOT / "code/milestone_labs.py"), "--lab", "01"],
            check=True, capture_output=True, text=True)
        record = json.loads(completed.stdout)
        self.assertEqual(record["lab"], "01")
        self.assertTrue(record["result"]["unicode_round_trip"])


if __name__ == "__main__":
    unittest.main()
