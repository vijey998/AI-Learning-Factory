"""Inspectible NumPy-only tiny GPT forward pass for Chapters 21–24.

This is an educational shape/cause test, not a training or performance implementation.
"""
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class TinyGPTConfig:
    vocab_size: int = 64
    context_length: int = 32
    width: int = 48
    layers: int = 2
    heads: int = 4
    intermediate: int = 128
    seed: int = 7

class TinyGPTCore:
    def __init__(self, cfg: TinyGPTConfig):
        if cfg.width % cfg.heads:
            raise ValueError("width must be divisible by heads")
        self.cfg = cfg
        rng = np.random.default_rng(cfg.seed)
        init = lambda *s: rng.normal(0, 0.02, s).astype(np.float32)
        self.embedding = init(cfg.vocab_size, cfg.width)
        self.position = init(cfg.context_length, cfg.width)
        self.blocks = []
        for _ in range(cfg.layers):
            self.blocks.append({
                "qkv": init(cfg.width, 3 * cfg.width),
                "out": init(cfg.width, cfg.width),
                "up": init(cfg.width, cfg.intermediate),
                "down": init(cfg.intermediate, cfg.width),
                "n1": np.ones(cfg.width, np.float32),
                "n2": np.ones(cfg.width, np.float32),
            })
        # Weight tying: logits use embedding.T rather than a second parameter.

    @staticmethod
    def rmsnorm(x, scale, eps=1e-5):
        return x * (1.0 / np.sqrt(np.mean(x * x, axis=-1, keepdims=True) + eps)) * scale

    @staticmethod
    def gelu(x):
        return 0.5 * x * (1.0 + np.tanh(np.sqrt(2.0 / np.pi) * (x + 0.044715 * x**3)))

    def attention(self, x, block):
        b, t, d = x.shape
        h, dh = self.cfg.heads, d // self.cfg.heads
        qkv = x @ block["qkv"]
        q, k, v = np.split(qkv, 3, axis=-1)
        move = lambda z: z.reshape(b, t, h, dh).transpose(0, 2, 1, 3)
        q, k, v = move(q), move(k), move(v)
        scores = q @ k.transpose(0, 1, 3, 2) / np.sqrt(dh)
        scores = np.where(np.tril(np.ones((t, t), dtype=bool)), scores, -np.inf)
        scores -= np.max(scores, axis=-1, keepdims=True)
        probs = np.exp(scores)
        probs /= np.sum(probs, axis=-1, keepdims=True)
        context = probs @ v
        context = context.transpose(0, 2, 1, 3).reshape(b, t, d)
        return context @ block["out"]

    def __call__(self, ids):
        ids = np.asarray(ids, dtype=np.int64)
        if ids.ndim != 2:
            raise ValueError("ids must have shape [B,T]")
        b, t = ids.shape
        if t > self.cfg.context_length:
            raise ValueError("sequence exceeds context_length")
        if ids.size and (ids.min() < 0 or ids.max() >= self.cfg.vocab_size):
            raise ValueError("token ID outside vocabulary")
        x = self.embedding[ids] + self.position[np.arange(t)][None, :, :]
        for block in self.blocks:
            x = x + self.attention(self.rmsnorm(x, block["n1"]), block)
            n = self.rmsnorm(x, block["n2"])
            x = x + self.gelu(n @ block["up"]) @ block["down"]
        return self.rmsnorm(x, np.ones(self.cfg.width, np.float32)) @ self.embedding.T

    def parameter_count(self):
        n = self.embedding.size + self.position.size
        for b in self.blocks:
            n += sum(v.size for v in b.values())
        return n

def causal_isolation_check():
    model = TinyGPTCore(TinyGPTConfig())
    a = np.array([[1, 2, 3, 4, 5]])
    b = np.array([[1, 2, 3, 40, 41]])
    za, zb = model(a), model(b)
    # Logits through position 2 see the same prefix and must match.
    return bool(np.allclose(za[:, :3], zb[:, :3], atol=1e-6, rtol=1e-5))

if __name__ == "__main__":
    cfg = TinyGPTConfig()
    model = TinyGPTCore(cfg)
    logits = model([[1, 2, 3, 4]])
    assert logits.shape == (1, 4, cfg.vocab_size)
    assert np.isfinite(logits).all()
    assert causal_isolation_check()
    print({"logits_shape": logits.shape, "parameters": model.parameter_count(),
           "tied_output": True, "causal_isolation": True})
