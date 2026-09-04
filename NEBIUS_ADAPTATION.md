# Nebius × NVIDIA adaptation gate

This is the P1 adaptation plan for the same VetProof product. It is not a
claim that Nebius or Nemotron has been used yet.

## Best-fit category

**Best apps and agents.** VetProof is a usable workflow agent, not a physical
robot or an always-on personal assistant.

## Hard requirements from the live submission form

- Runtime must be Nebius Token Factory or Nebius AI Cloud.
- At least one NVIDIA open-source model must be used; the intended model is
  Nemotron.
- Public OSI-licensed repository and README must explain the Nebius/Nemotron
  integration.
- Public demo URL and public YouTube video (three minutes or less) are
  required.
- Required feedback fields must be based on an actual runtime evaluation, not
  invented ratings.
- Tavily is marked `Yes` only if the application makes a functional runtime
  Tavily API call. Otherwise it remains `No`.

## Reuse and disclosure

The Agents for Humans implementation is existing work. The Nebius submission
will select `Existing` and document the significant in-period changes:

1. Nebius Token Factory/Nemotron model adapter (`app/adapters/nebius_nemotron.py`).
2. Execution of the identical `TINY-VERDICTS-EVAL-001` benchmark across Nemotron
   variants to measure:
   - Tool/effect selection accuracy.
   - Unauthorized effect attempts vs. enforcement invariance.
   - Task completion under constrained standing envelopes.
   - Provider latency and cost per verified workflow.
   - Escalation frequency.
3. Runtime evidence receipt recording provider, model, endpoint, tokens, and latency.
4. Provider-specific tests and a live demo path.

Thesis:
> **The model can change. The authority boundary remains deterministic.**

## Acceptance gate

```text
Nebius endpoint reachable
→ Nemotron invocation succeeds
→ TINY-VERDICTS-EVAL-001 corpus executed against Nemotron
→ Tiny Verdict still gates the consequential effect (0 unauthorized commits)
→ receipt records provider/model evidence
→ replay verifies
→ public demo and <=3 minute video updated
→ required feedback fields filled from measured run
```

The P0 Agents for Humans submission remains the immediate deadline lane. This
adaptation must not weaken or rewrite the proven P0 path.
