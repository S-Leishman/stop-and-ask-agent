# ORI Standing Goal

## Goal ID
ORI-GOAL-VETPROOF-PRODUCTIZE-001

## Standing goal

Convert VetProof from a working competition demo into a reproducible, provider- and model-portable evidence product by using Ori as the stable evaluation harness for agent behavior, while preserving deterministic authority enforcement, signed receipts, replayability, and human control.

The evaluation work must strengthen the current Agents for Humans submission first, then become reusable evidence for Nebius/NVIDIA, Hugging Face, GCP, Kaggle/Colab/Brev/Tinker, and future commercial qualification work.

## Non-negotiable invariants

- The model may propose actions; it may not grant itself authority.
- Consequential effects must pass the deterministic AuthorityGate.
- PASS, FAIL, and UNKNOWN remain distinct.
- UNKNOWN never degrades to PASS.
- Delegated authority may only narrow.
- A human decision is required when the effect ceiling is reached.
- Every accepted or denied consequential boundary must be receipted.
- Receipt replay must fail on tampering or chain breakage.
- Model quality is measured separately from control correctness.
- No benchmark result may be reported without the exact eval files, model/runtime identity, commands, counts, artifacts, and report.
- No public claim may exceed observed evidence.

## Product conversion rule

Every Ori run must leave at least one reusable company artifact:

1. eval corpus,
2. Markdown report,
3. model/runtime recommendation,
4. receipt/replay evidence,
5. benchmark/result artifact,
6. competition evidence,
7. or a documented falsification/hold.

Inventory alone is not completion.

## Current priority

P0: Agents for Humans submission.
P1: TinyVerdicts-Bench v0.1.
P2: Hugging Face public evidence surface.
P3: Nebius/NVIDIA adaptation.
P4: SmolAgents/Gemini and additional runtime qualification.

External hardware work is out of scope for this goal.
