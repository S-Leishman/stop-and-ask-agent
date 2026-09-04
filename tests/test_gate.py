"""STRANDS-SPIKE-001 acceptance tests: authority envelope, monotonicity, receipts."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.agent import StopAndAskFlow
from app.authority import AuthorityContract, AuthorityGate, Decision, REQUIRES_HUMAN
from app.receipts import ReceiptChain, sha, canonical

import pytest  # noqa: E402


def test_in_envelope_effect_allowed():
    gate = AuthorityGate(AuthorityContract("human:scott", frozenset({"COMMIT_OUTPUT"}), max_writes=2))
    assert gate.check("READ_WORKSPACE") is Decision.ALLOWED


def test_ceiling_reached_requires_human():
    gate = AuthorityGate(AuthorityContract("human:scott", frozenset({"COMMIT_OUTPUT"}), max_writes=0))
    assert gate.check("COMMIT_OUTPUT") is Decision.REQUIRES_HUMAN


def test_delegation_monotonicity_violation_rejected():
    parent = AuthorityContract("human:scott", frozenset({"READ_WORKSPACE"}))
    with pytest.raises(ValueError):
        parent.derive_child(frozenset({"READ_WORKSPACE", "EXTERNAL_SUBMIT"}))


def test_child_ceiling_only_shrinks():
    parent = AuthorityContract("human:scott", frozenset({"READ_WORKSPACE", "COMMIT_OUTPUT"}), max_writes=5)
    child = parent.derive_child(frozenset({"READ_WORKSPACE", "COMMIT_OUTPUT"}), max_writes=9)
    assert child.max_writes == 5  # 9 narrowed back to parent's 5
    assert child.delegation_rights is False


def test_forbidden_effect_denied():
    gate = AuthorityGate(AuthorityContract("human:scott", frozenset({"COMMIT_OUTPUT"}), max_writes=5))
    assert gate.check("EXTERNAL_SUBMIT") is Decision.DENIED


def test_flow_denied_by_human(tmp_path):
    # isolate from any real run's committed output
    Path(__file__).resolve().parents[1].joinpath("output", "status.md").unlink(missing_ok=True)
    flow = StopAndAskFlow(state_dir=tmp_path)
    flow.human_decision = "DENY"
    flow.decision_event.set()
    snap = flow.run()
    assert snap["stage"] == "DENIED_BY_HUMAN"
    assert snap["receipt"]["outcome"] == "DENIED_BY_HUMAN"
    assert not (flow.state_dir.parent / "output" / "status.md").exists()


def test_flow_approved_commits_and_replays(tmp_path):
    flow = StopAndAskFlow(state_dir=tmp_path)
    flow.human_decision = "APPROVE"
    flow.decision_event.set()
    snap = flow.run()
    assert snap["stage"] == "RECEIPT_VERIFIED"
    assert snap["receipt"]["outcome"] == "COMMITTED_AFTER_HUMAN_APPROVAL"
    assert snap["receipt"]["decided_by"] == "human:scott"
    assert snap["receipt"]["receipt_signature"]
    assert snap["receipt"]["receipt_public_key"]
    assert snap["replay"]["ok"] is True
    assert Path(__file__).resolve().parents[1].joinpath("output", "status.md").exists()


def test_receipt_chain_detects_mutation(tmp_path):
    chain = ReceiptChain(tmp_path / "r.jsonl")
    chain.append({"action": "A", "outcome": "X"})
    chain.append({"action": "B", "outcome": "Y"})
    ok, _ = chain.verify()
    assert ok
    # mutate the stored line
    p = tmp_path / "r.jsonl"
    lines = p.read_text().splitlines()
    rec = json_mutate(lines[0])
    p.write_text("\n".join([rec, lines[1]]) + "\n")
    chain2 = ReceiptChain(p)
    ok, why = chain2.verify()
    assert not ok and "mismatch" in why


def json_mutate(line: str) -> str:
    import json
    r = json.loads(line)
    r["outcome"] = "TAMPERED"
    body = {k: v for k, v in r.items() if k != "receipt_sha256"}
    import hashlib
    r["receipt_sha256"] = hashlib.sha256(canonical(body)).hexdigest()
    return json.dumps(r, sort_keys=True)


def test_receipt_chain_detects_chain_break(tmp_path):
    chain = ReceiptChain(tmp_path / "r.jsonl")
    chain.append({"action": "A"})
    chain.append({"action": "B"})
    p = tmp_path / "r.jsonl"
    lines = p.read_text().splitlines()
    rec2 = json.loads(lines[1])
    rec2["prev_receipt_sha256"] = "0" * 64  # detach receipt 2 from receipt 1
    lines[1] = json.dumps(rec2, sort_keys=True)
    p.write_text("\n".join(lines) + "\n")
    ok, why = ReceiptChain(p).verify()
    assert not ok and "chain break" in why
