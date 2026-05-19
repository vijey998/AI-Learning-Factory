import sys
from pathlib import Path
import unittest
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
from tiny_gpt_core import TinyGPTConfig, TinyGPTCore, causal_isolation_check
from moe_routing_lab import route

class PartsSixToEightTests(unittest.TestCase):
    def test_tiny_gpt_shape_finite_and_causal(self):
        cfg = TinyGPTConfig(vocab_size=32, context_length=8, width=16, layers=2, heads=4, intermediate=32)
        model = TinyGPTCore(cfg)
        out = model([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(out.shape, (2, 3, 32))
        self.assertTrue(np.isfinite(out).all())
        self.assertTrue(causal_isolation_check())

    def test_context_and_vocabulary_guards(self):
        model = TinyGPTCore(TinyGPTConfig(context_length=2))
        with self.assertRaises(ValueError): model([[1, 2, 3]])
        with self.assertRaises(ValueError): model([[64]])

    def test_moe_accounting(self):
        logits = np.zeros((16, 4)); logits[:, 0] = 2; logits[:, 1] = 1
        result = route(logits, k=2, capacity_factor=1.0)
        self.assertEqual(int(result["counts"].sum()), 32)
        self.assertEqual(result["capacity"], 8)
        self.assertGreater(result["overflow"], 0)

if __name__ == "__main__": unittest.main()
