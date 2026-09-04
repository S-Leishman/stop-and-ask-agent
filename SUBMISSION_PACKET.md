# Submission packet status

Generated from the live Devpost requirements and local evidence on 2026-09-04.

## Agents for Humans — draft project 1417274

| Field | Value | Evidence/state |
|---|---|---|
| Title | VetProof: Tiny Verdicts for AI Agents | Live draft |
| Track | Professional Agents | Fit to professional workflow |
| Repository | https://github.com/S-Leishman/stop-and-ask-agent | Public; HEAD `1172948` |
| Architecture | `docs/architecture.png` | SHA-256 `0271f92d351b67d7a75cb46d405ff718b141d26aef756f6bfbfe5b6f6aced300` |
| Video | `demo_assets/VetProof_Agents_for_Humans_demo.mp4` | 92 seconds; SHA-256 `6a212491d9b0258ed313f7749d5b51b9d45aba2595c33f9aa4d3fe7cdc345c36`; public URL required |
| Tests | `python -m pytest -q tests` | 16 passed |
| Deny path | `DENIED_BY_HUMAN`, replay verified | Fresh run `/tmp/vetproof-deny-verify` |
| Approve path | `RECEIPT_VERIFIED`, replay verified | Fresh run `/tmp/vetproof-approve-verify` |
| AWS Builder ID | TODO | Owner-supplied required field |
| Country | TODO | Owner-supplied required field |

## Not yet admissible

- No public YouTube/Vimeo video URL.
- Architecture image has not been attached to the Devpost field.
- AWS Builder ID and country are not recorded.
- Live Bedrock execution is not proven; the current AWS profile returns an
  authorization error.
- The Devpost project remains Draft; no submission is claimed.

## Nebius × NVIDIA — preparation only

The existing project is classified as `Existing` for that event. The required
in-period delta is a real Nebius Token Factory/Nemotron invocation, provider
receipt, and measured feedback. Until that run exists, model ratings and
platform feedback remain intentionally blank.
