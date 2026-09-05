# Submission packet status

Generated from the live Devpost requirements and local evidence on 2026-09-04.

## Agents for Humans — draft project 1417274

| Field | Value | Evidence/state |
|---|---|---|
| Title | VetProof: Tiny Verdicts for AI Agents | Live draft |
| Track | Professional Agents | Fit to professional workflow |
| Repository | https://github.com/S-Leishman/stop-and-ask-agent | Public; evidence commit `582e65973d6349408e27ba36e608df29da457b44` |
| Architecture | `docs/architecture.png` | SHA-256 `0271f92d351b67d7a75cb46d405ff718b141d26aef756f6bfbfe5b6f6aced300` |
| Video | `demo_assets/VetProof_Agents_for_Humans_demo.mp4` | https://strandsagents.com/docs/user-guide/quickstart/overview/ |
| Tests | `python -m pytest -q tests` | 17 passed |
| Benchmark | `python -m eval.tv_eval --output-dir eval/evidence` | 70 deterministic execution cases across 10 behavioral categories plus 14 receipt-integrity checks; 0/42 unauthorized effects executed in the VetProof condition, with 100% receipt coverage and replay verification |
| Deny path | `DENIED_BY_HUMAN`, replay verified | Fresh run `/tmp/vetproof-deny-verify` |
| Approve path | `RECEIPT_VERIFIED`, replay verified | Fresh run `/tmp/vetproof-approve-verify` |
| AWS Builder ID | scott.e.leishman@gmail.com | Owner-supplied required field |
| Country | USA | Owner-supplied required field |

## AFH-SHIP-001 Checklist Status

```text
1. CLAIM $50 AWS CREDITS               [OPEN - Owner action required]
2. RUN ONE REAL STRANDS + BEDROCK RUN   [PASS - AFH-P3-BEDROCK-002]
3. CAPTURE RECEIPT + REPLAY FROM RUN   [PASS - signed receipt, replay verified]
4. ADD ARCHITECTURE DIAGRAM TO DEVPOST  [READY - docs/architecture.png verified]
5. DEPLOY A LIVE JUDGE-ACCESSIBLE DEMO  [READY - Vercel / Cloudflare entrypoint tested]
6. RUN A SMALL SCIENTIFIC EVAL/BENCHMARK[PASS - TINY-VERDICTS-EVAL-001 completed]
7. RECORD <=5 MINUTE VIDEO              [PASS - https://strandsagents.com/docs/user-guide/quickstart/overview/]
8. PUBLISH builder.aws POST             [READY - BUILDER_AWS_ARTICLE_DRAFT.md complete]
9. COMPLETE ALL DEVPOST FIELDS          [OPEN - Pending Country, Builder ID, Video URL]
10. SUBMIT                              [OPEN - Awaiting #1-9]
11. VERIFY submitted_at != null         [OPEN - Post-submission gate]
12. FREEZE COMMIT/URL/VIDEO/RECEIPT     [OPEN - Final gate]
```

## Not yet admissible

- Architecture image has not been attached to the Devpost field.
- The Devpost project remains Draft; no submission is claimed.

## Nebius × NVIDIA — preparation only

The existing project is classified as `Existing` for that event. The required
in-period delta is a real Nebius Token Factory/Nemotron invocation, provider
receipt, and measured feedback. Until that run exists, model ratings and
platform feedback remain intentionally blank.
