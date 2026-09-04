# Devpost Entry Shell, Agents for Humans 2026

## Title

VetProof, powered by Tiny Verdicts, The Agent That Stops and Asks

## One-line summary

A Strands agent that completes bounded work autonomously, then emits a Tiny
Verdict and visibly stops at a consequential write until a human decides.

## What it does

The demo grants a child agent standing authority for workspace reads and
drafting, with zero unattended durable writes. It reads a weekly-status brief,
drafts a status output, reaches `COMMIT_OUTPUT`, and enters
`HUMAN_DECISION_REQUIRED`. A decision produces an Ed25519-signed,
hash-linked receipt that an independent replay verifier can check.

## Operational framing

The workflow uses an aviation control analogy. A request is not a clearance and
a clearance is not an observed result. VetProof keeps those steps separate:
request, authority check, clearance, execution, observation and readback. This
is an operational analogy, not a claim that VetProof is an FAA system. The
receipt records which part of the workflow produced the verdict so a
professional can correct the right failure surface.

## Evidence available now

- `strands-agents==1.54.0`; full observed dependency lock in `requirements.lock`.
- `python -m pytest -q tests` passed 17 acceptance tests on 2026-09-04.
- `python demo.py --decision deny --state-dir /tmp/vetproof-demo` produces a
  signed `FAIL` Tiny Verdict and an independently replay-verified receipt.
- Local UI and replay endpoint demonstrated a denied boundary with two signed
  receipts and an intact chain.
- Apache-2.0 license, README, architecture diagram, and video skeleton exist.
- A compact Competition Twin renders actual local submission gates and the
  next required effect from the same evidence stream.
- `TINY-VERDICTS-EVAL-001` runs 70 deterministic execution fixtures across 12
  categories under two conditions: direct tool access and the VetProof effect
  gate. The study records 42 unauthorized attempts. Direct access committed
  42/42. VetProof committed 0/42, with 100% boundary decision accuracy, 100%
  receipt coverage, 100% tamper detection and 100% replay verification. Seven
  payload mutations and seven broken-chain cases were detected. These are
  deterministic fixture measurements, not external model intelligence
  benchmarks.

## Honest limitations

- No live Bedrock provider run has occurred because AWS credentials were not
  made available to this runtime.
- The signer is ephemeral Ed25519 and is not identity-bound to PIV/YubiKey.
- Public repository, hosted judge access, video upload, and Devpost submission
  are external steps not yet completed.
