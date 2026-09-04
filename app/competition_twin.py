"""A compact operational view of the competition's real submission gates."""
from __future__ import annotations

import os
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKELETON = ROOT.parent / "SUBMISSION_SKELETON.md"


def _gate(identifier: str, verdict: str, detail: str, evidence: str) -> dict:
    return {"id": identifier, "verdict": verdict, "detail": detail, "evidence": evidence}


def competition_twin() -> dict:
    """Return operational submission truth; external claims fail closed to UNKNOWN."""
    public_repo = os.environ.get("VETPROOF_PUBLIC_REPO_URL")
    return {
        "schema": "aevion.competition-twin/v1",
        "competition": "Agents for Humans 2026",
        "deadline": "2026-09-14T17:00:00-07:00",
        "gates": [
            _gate(
                "SUBMISSION_SKELETON",
                "PASS" if SKELETON.is_file() else "FAIL",
                "submission contract is locally present" if SKELETON.is_file() else "submission contract missing",
                str(SKELETON),
            ),
            _gate(
                "ARCHITECTURE",
                "PASS" if (ROOT / "ARCHITECTURE.md").is_file() else "FAIL",
                "renderable architecture exists" if (ROOT / "ARCHITECTURE.md").is_file() else "architecture missing",
                "ARCHITECTURE.md",
            ),
            _gate(
                "PUBLIC_REPOSITORY",
                "PASS" if public_repo else "UNKNOWN",
                public_repo or "no public repository URL has been evidenced",
                "VETPROOF_PUBLIC_REPO_URL",
            ),
            _gate(
                "LIVE_BEDROCK_EXECUTION",
                "UNKNOWN",
                "no recorded provider-backed run in the local evidence bundle",
                "FREEZE_EVIDENCE.md",
            ),
            _gate(
                "VIDEO_RECORDING",
                "FAIL",
                "video skeleton exists; no recorded video artifact is evidenced",
                "VIDEO_SKELETON.md",
            ),
            _gate(
                "DEVPOST_SHELL",
                "PASS" if (ROOT / "DEVPOST_ENTRY.md").is_file() else "FAIL",
                "local Devpost fields are drafted" if (ROOT / "DEVPOST_ENTRY.md").is_file() else "Devpost shell missing",
                "DEVPOST_ENTRY.md",
            ),
        ],
        "next_required_effect": {
            "effect": "PUBLISH_REPOSITORY",
            "verdict": "UNKNOWN",
            "human_required": True,
            "reason": "the agent may prepare the repository but cannot make it public without an external authorization boundary",
        },
    }
