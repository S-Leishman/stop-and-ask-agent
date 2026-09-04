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
| Tests | `python -m pytest -q tests` | 17 passed |
| Benchmark | `python -m eval.tv_eval` | `TINY-VERDICTS-EVAL-001`: 0/42 unauthorized effects executed; 100% receipt coverage, replay verified |
| Deny path | `DENIED_BY_HUMAN`, replay verified | Fresh run `/tmp/vetproof-deny-verify` |
| Approve path | `RECEIPT_VERIFIED`, replay verified | Fresh run `/tmp/vetproof-approve-verify` |
| AWS Builder ID | TODO | Owner-supplied required field |
| Country | TODO | Owner-supplied required field |

## AFH-SHIP-001 Checklist Status

```text
1. CLAIM $50 AWS CREDITS               [OPEN - Owner action required]
2. RUN ONE REAL STRANDS + BEDROCK RUN   [OPEN - Pending #1 credentials]
3. CAPTURE RECEIPT + REPLAY FROM RUN   [OPEN - Pending #2]
4. ADD ARCHITECTURE DIAGRAM TO DEVPOST  [READY - docs/architecture.png verified]
5. DEPLOY A LIVE JUDGE-ACCESSIBLE DEMO  [READY - Vercel / Cloudflare entrypoint tested]
6. RUN A SMALL SCIENTIFIC EVAL/BENCHMARK[PASS - TINY-VERDICTS-EVAL-001 completed]
7. RECORD <=5 MINUTE VIDEO              [READY - 92s local MP4 rendered; public URL pending]
8. PUBLISH builder.aws POST             [READY - BUILDER_AWS_ARTICLE_DRAFT.md complete]
9. COMPLETE ALL DEVPOST FIELDS          [OPEN - Pending Country, Builder ID, Video URL]
10. SUBMIT                              [OPEN - Awaiting #1-9]
11. VERIFY submitted_at != null         [OPEN - Post-submission gate]
12. FREEZE COMMIT/URL/VIDEO/RECEIPT     [OPEN - Final gate]
```

## Not yet admissible

- No public YouTube/Vimeo video URL.
- Architecture image has not been attached to the Devpost field.
- AWS Builder ID and country are not recorded.
- Live Bedrock execution is not proven; AWS credentials not yet supplied.
- The Devpost project remains Draft; no submission is claimed.

## Nebius × NVIDIA — preparation only

The existing project is classified as `Existing` for that event. The required
in-period delta is a real Nebius Token Factory/Nemotron invocation, provider
receipt, and measured feedback. Until that run exists, model ratings and
platform feedback remain intentionally blank.
