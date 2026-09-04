# Title

VetProof: Tiny Verdicts for AI Agents

## One-line Summary

VetProof is a Strands-compatible work agent that acts inside standing authority,
stops at consequential boundaries and gives every proposed effect a signed
replayable Tiny Verdict: `PASS`, `FAIL` or `UNKNOWN`.

## Problem

Professionals need agents to handle repetitive work in the background, but a
durable action such as publishing a document, changing a record or sending an
external message should not happen merely because a model chose to do it. Today
that authority transition is commonly invisible, implicit or buried in logs.

## Solution

VetProof grants a narrow standing authority envelope. The Strands-compatible
agent reads a task brief and drafts a status output autonomously. When it
proposes a durable `COMMIT_OUTPUT`, its zero-write ceiling produces `UNKNOWN /
HUMAN_DECISION_REQUIRED`. A human approves or denies. The decision and its Tiny
Verdict are enclosed in an Ed25519-signed, SHA-256-linked receipt chain that
replays independently.

## Why This Matters

The agent still removes the repetitive work, while the person keeps authority
over the moment that has a consequential effect. This is useful for consultants,
operators, makers, and small teams that need automated preparation without
unreviewed commitments.

## How We Used AI

The project uses the Strands Agents SDK dependency and a Strands agent path with
bounded `read_brief` and `request_commit` tools. The authority gate is
deterministic code: a model can propose work but cannot enlarge its own envelope
or commit beyond the effect ceiling. The offline scripted path demonstrates the
same authority, receipt, and replay flow without cloud credentials. A live
Bedrock-backed run is an explicitly marked future evidence gate, not a claim.

## How We Used Codex

Codex helped implement the authority-envelope demo, adversarial acceptance
tests, canonical Tiny Verdict contract, receipt replay, judge-facing UI,
Competition Twin read-model, architecture, video plan, and this submission
packet. Every product claim in this draft is tied to a locally runnable path or
is explicitly labeled as pending.

## Key Features

- Standing authority envelope with zero unattended durable writes.
- Monotonic delegation: a child cannot acquire effects or ceilings absent from
  its parent.
- Tiny Verdict primitive with parent/delegated authority, proposed effect,
  observed-state hash, evidence references, policy identity, verdict, and human
  decision.
- `PASS` executes only inside authority; `FAIL` denies; `UNKNOWN` stops for a
  human decision.
- Ed25519-signed, SHA-256-linked receipts and independent replay verification.
- Empirical boundary evaluation (`TINY-VERDICTS-EVAL-001`): 70 deterministic execution cases across 10 behavioral categories, evaluated under direct and VetProof-gated conditions, plus 14 receipt-integrity checks covering tamper and chain-break detection. Under VetProof, the measured unauthorized-effect execution rate was 0.0 (0/42 unauthorized effects committed vs. 42/42 under direct access), boundary decision accuracy was 1.0, authorized completion rate was 1.0, human escalation precision was 1.0, false block rate was 0.0, tamper detection was 1.0, and replay verification was 1.0 with 100% Ed25519-signed receipt coverage.
- Compact Competition Twin showing factual submission obligations and the next
  human-required external effect.

## Architecture

The authority decision is deterministic code, separate from the effect layer:

```text
PROPOSE → TINY VERDICT → AUTHORIZE → EFFECT COMMIT → SIGNED RECEIPT → REPLAY
```

The detailed diagram is in `ARCHITECTURE.md` and `docs/architecture.svg`.

## Testing Instructions

```bash
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
./.venv/bin/python -m pytest -q tests
./.venv/bin/python -m eval.tv_eval --output-dir eval/evidence
./.venv/bin/python demo.py --decision deny --state-dir /tmp/vetproof-demo
./.venv/bin/python server.py 8474
```

The test suite currently has 17 passing acceptance tests. The evaluation command
executes the 70-case benchmark and 14 integrity checks with signed receipts. The demo command emits
`DENIED_BY_HUMAN`, a signed `FAIL` Tiny Verdict, and `replay.ok: true`. The local UI
is at `http://127.0.0.1:8474` and exposes the Competition Twin at `/api/competition-twin`.

## Public Demo Link

TODO — no deployed judge-accessible URL has been evidenced. The local runnable
path above is available now.

## Public Repository Link

https://github.com/S-Leishman/stop-and-ask-agent

Verified publicly at commit `d90674a0b815ab6a12bbfda9acf42881f3429bc7` on
2026-09-04.

## Demo Video

A 92-second local MP4 has been rendered at
`demo_assets/VetProof_Agents_for_Humans_demo.mp4`; its SHA-256 is recorded in
`demo_assets/VIDEO_README.md`. TODO — publish it to YouTube or Vimeo and add
the public URL here. The complete run-of-show is in `VIDEO_SKELETON.md` and
covers the problem, audience, working authority flow, human decision, signed
receipt, replay, and Competition Twin.

## Screenshot Shot List

1. VetProof UI at `HUMAN_DECISION_REQUIRED`, with proposed effect and Tiny
   Verdict `UNKNOWN` visible.
2. DENY result with signed receipt and replay verification.
3. Competition Twin showing local `PASS`, `FAIL`, and `UNKNOWN` submission
   gates plus `PUBLISH_DEMO_VIDEO` as the next human-required effect.
4. Architecture diagram showing authority and effect separation.

## Submission Readiness Notes

- Proposed track: **Professional Agents**.
- The project uses Strands Agents and is Apache-2.0 licensed locally.
- Required architecture file is prepared locally; Devpost accepts PNG/JPG/PDF/
  PPT/PPTX, so `docs/architecture.png` must be attached when the project is
  created.
- Required form inputs still need the participant's country of residence and
  AWS Builder ID, plus a public video URL.
- A live Bedrock-backed run and public live demo could strengthen Technical
  Implementation but are not being claimed as complete.

## Known Limitations

- The offline demonstration uses a deterministic fallback until runtime AWS
  credentials are supplied for a live Bedrock-backed execution.
- Receipt signing uses an ephemeral Ed25519 key; it is not yet bound to a
  YubiKey/PIV identity.
- The current local UI is loopback-only and single-user.

## TODO Official Form Fields

| Devpost field | Value/status |
| --- | --- |
| Submitter Type (27729) | Individual — proposed; confirm before submission |
| Country of Residence (27730) | TODO: user-provided exact selection required |
| Organization (27731) | Leave blank unless entering on behalf of an organization |
| Track (27732) | Professional Agents — proposed |
| Public code repo (27733) | https://github.com/S-Leishman/stop-and-ask-agent |
| Architecture diagram (27734) | Attach `docs/architecture.png` when project exists |
| AWS Builder ID (27735) | TODO: user-provided |
| Live demo (27736) | Optional; TODO |
| Testing instructions (28191) | Use this document's Testing Instructions section |
| Builder.aws bonus post (27737) | Optional; TODO: publish `BUILDER_AWS_ARTICLE_DRAFT.md` |
