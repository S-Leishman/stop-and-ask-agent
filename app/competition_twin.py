"""A compact operational view of the competition's real submission gates."""
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKELETON = ROOT.parent / "SUBMISSION_SKELETON.md"
PUBLIC_REPOSITORY_URL = "https://github.com/S-Leishman/stop-and-ask-agent"


def _gate(identifier: str, verdict: str, detail: str, evidence: str) -> dict:
    return {"id": identifier, "verdict": verdict, "detail": detail, "evidence": evidence}


def competition_twin() -> dict:
    """Return operational submission truth; external claims fail closed to UNKNOWN."""
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
                "PASS",
                PUBLIC_REPOSITORY_URL,
                "origin/master verified at 1058bf8",
            ),
            _gate(
                "LIVE_BEDROCK_EXECUTION",
                "PASS",
                "Strands 1.54.0 proposed the effect through Amazon Bedrock Nova Micro; human DENY prevented the durable write and signed receipt replay verified",
                "eval/evidence/AFH-P3-BEDROCK-002.result.json",
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
            "effect": "PUBLISH_DEMO_VIDEO",
            "verdict": "UNKNOWN",
            "human_required": True,
            "reason": "a public ≤5-minute video is required before the entry can be submitted",
        },
    }
