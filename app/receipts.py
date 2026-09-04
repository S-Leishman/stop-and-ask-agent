"""Tamper-evident receipt chain: append-only, sha256-linked, replay-verifiable."""
from __future__ import annotations

import hashlib
import json
import threading
from pathlib import Path

GENESIS = "0" * 64


def canonical(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


class ReceiptChain:
    """Append-only chain stored as JSONL. verify() recomputes every link."""

    def __init__(self, path: Path):
        self.path = Path(path)
        self._lock = threading.Lock()
        if self.path.exists():
            self.receipts = [json.loads(l) for l in self.path.read_text(encoding="utf-8").splitlines() if l.strip()]
        else:
            self.receipts = []

    def append(self, receipt: dict) -> dict:
        with self._lock:
            prev = self.receipts[-1]["receipt_sha256"] if self.receipts else GENESIS
            body = {k: v for k, v in receipt.items() if k != "receipt_sha256"}
            body["prev_receipt_sha256"] = prev
            body["sequence"] = len(self.receipts) + 1
            digest = sha(canonical(body))
            full = {**body, "receipt_sha256": digest}
            self.receipts.append(full)
            with self.path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(full, sort_keys=True) + "\n")
            return full

    def verify(self) -> tuple[bool, str]:
        prev = GENESIS
        for i, r in enumerate(self.receipts):
            body = {k: v for k, v in r.items() if k != "receipt_sha256"}
            if body.get("prev_receipt_sha256") != prev:
                return False, f"chain break at {i}: prev pointer mismatch"
            if sha(canonical(body)) != r["receipt_sha256"]:
                return False, f"digest mismatch at {i}: receipt was mutated"
            prev = r["receipt_sha256"]
        return True, f"replay verified: {len(self.receipts)} receipts, chain intact"
