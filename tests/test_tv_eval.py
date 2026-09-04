import json

from eval.tv_eval import CASES, run


def test_tv_eval_is_reproducible_and_receipt_backed(tmp_path):
    result = run(tmp_path)
    assert result["study"] == "TV-EVAL-001"
    assert len(CASES) == 60
    assert len(result["rows"]) == len(CASES) * 3
    assert all(row["receipt_sha256"] for row in result["rows"])
    assert all(row["prev_receipt_sha256"] for row in result["rows"])
    assert all(row["condition"] in {"baseline", "native_hitl", "vetproof"} for row in result["rows"])
    vetproof = result["summary"]["vetproof"]
    assert vetproof["unauthorized_effect_execution_rate"] == 0.0
    assert vetproof["tamper_detection_rate"] == 1.0
    assert vetproof["replay_verification_rate"] == 1.0
    saved = json.loads((tmp_path / "TV-EVAL-001.json").read_text())
    assert saved["summary"] == result["summary"]
