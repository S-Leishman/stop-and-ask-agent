# Devpost Entry Shell — Agents for Humans 2026

## Title

Agents for Humans: The Agent That Stops and Asks

## One-line summary

A Strands agent that completes bounded work autonomously, then visibly stops
at a consequential write until a human decides.

## What it does

The demo grants a child agent standing authority for workspace reads and
drafting, with zero unattended durable writes. It reads a weekly-status brief,
drafts a status output, reaches `COMMIT_OUTPUT`, and enters
`HUMAN_DECISION_REQUIRED`. A decision produces an Ed25519-signed,
hash-linked receipt that an independent replay verifier can check.

## Evidence available now

- `strands-agents==1.54.0`; full observed dependency lock in `requirements.lock`.
- `python -m pytest -q tests` passed 9 acceptance tests on 2026-09-04.
- Local UI and replay endpoint demonstrated a denied boundary with two signed
  receipts and an intact chain.
- Apache-2.0 license, README, architecture diagram, and video skeleton exist.

## Honest limitations

- No live Bedrock provider run has occurred because AWS credentials were not
  made available to this runtime.
- The signer is ephemeral Ed25519 and is not identity-bound to PIV/YubiKey.
- Public repository, hosted judge access, video upload, and Devpost submission
  are external steps not yet completed.
