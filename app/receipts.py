"""Signed, append-only receipt chain with independent replay verification."""
from __future__ import annotations

import hashlib
import json
import threading
import base64
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)

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
        self._signing_key = Ed25519PrivateKey.generate()

    def append(self, receipt: dict) -> dict:
        with self._lock:
            prev = self.receipts[-1]["receipt_sha256"] if self.receipts else GENESIS
            body = {
                k: v
                for k, v in receipt.items()
                if k not in {"receipt_sha256", "receipt_signature", "receipt_public_key"}
            }
            body["prev_receipt_sha256"] = prev
            body["sequence"] = len(self.receipts) + 1
            digest = sha(canonical(body))
            public_key = self._signing_key.public_key().public_bytes(
                serialization.Encoding.Raw, serialization.PublicFormat.Raw
            )
            signature = self._signing_key.sign(canonical(body))
            full = {
                **body,
                "receipt_sha256": digest,
                "receipt_signature": base64.b64encode(signature).decode("ascii"),
                "receipt_public_key": base64.b64encode(public_key).decode("ascii"),
            }
            self.receipts.append(full)
            with self.path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(full, sort_keys=True) + "\n")
            return full

    def verify(self) -> tuple[bool, str]:
        prev = GENESIS
        for i, r in enumerate(self.receipts):
            body = {
                k: v
                for k, v in r.items()
                if k not in {"receipt_sha256", "receipt_signature", "receipt_public_key"}
            }
            if body.get("prev_receipt_sha256") != prev:
                return False, f"chain break at {i}: prev pointer mismatch"
            if sha(canonical(body)) != r["receipt_sha256"]:
                return False, f"digest mismatch at {i}: receipt was mutated"
            try:
                public_key = base64.b64decode(r["receipt_public_key"], validate=True)
                signature = base64.b64decode(r["receipt_signature"], validate=True)
                Ed25519PublicKey.from_public_bytes(public_key).verify(signature, canonical(body))
            except (KeyError, TypeError, ValueError):
                return False, f"signature missing or malformed at {i}"
            except Exception:
                return False, f"signature mismatch at {i}: receipt was mutated"
            prev = r["receipt_sha256"]
        return True, f"replay verified: {len(self.receipts)} signed receipts, chain intact"
