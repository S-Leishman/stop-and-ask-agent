"""Submission command acceptance: a judge can run a complete deny flow."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_demo_command_denies_then_verifies_replay(tmp_path):
    """Removing human denial or replay verification must make this fail."""
    result = subprocess.run(
        [
            sys.executable,
            "demo.py",
            "--decision",
            "deny",
            "--state-dir",
            str(tmp_path),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )

    evidence = json.loads(result.stdout)
    assert evidence["stage"] == "DENIED_BY_HUMAN"
    assert evidence["receipt"]["outcome"] == "DENIED_BY_HUMAN"
    assert evidence["receipt"]["tiny_verdict"]["verdict"] == "FAIL"
    assert evidence["replay"]["ok"] is True


def test_demo_command_creates_requested_evidence_directory(tmp_path):
    """Removing state-directory creation must make an otherwise valid run fail."""
    state_dir = tmp_path / "new" / "receipt-chain"
    result = subprocess.run(
        [sys.executable, "demo.py", "--decision", "deny", "--state-dir", str(state_dir)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )

    assert json.loads(result.stdout)["replay"]["ok"] is True
    assert (state_dir / "strands_spike_001_receipts.jsonl").is_file()
