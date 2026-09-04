# STRANDS-SPIKE-001 local freeze evidence

Status: `MINIMUM_VALID_SUBMISSION_CANDIDATE`

## Reproducible local acceptance

```bash
python -m pytest -q tests
python demo.py --decision deny --state-dir /tmp/vetproof-demo
```

Observed 2026-09-04:

- 17 acceptance tests passed.
- The command emitted `DENIED_BY_HUMAN` with Tiny Verdict `FAIL`.
- The emitted Ed25519-signed receipt replayed successfully.

## Included submission surfaces

- `README.md`: product and runnable path.
- `ARCHITECTURE.md` and `docs/architecture.svg`: architecture.
- `VIDEO_SKELETON.md`: ≤5-minute recording plan.
- `DEVPOST_ENTRY.md`: submission draft.
- `BUILDER_AWS_ARTICLE_DRAFT.md`: article draft.
- `/api/competition-twin`: read-only submission-gate payload for the local UI.
- `requirements.lock`: observed dependency lock.
- `eval/evidence/*`: frozen evaluation artifacts.

## Empirical Evaluation Evidence

TINY-VERDICTS-EVAL-001 contains 70 deterministic execution cases across 10 behavioral categories, evaluated under direct and VetProof-gated conditions, plus 14 receipt-integrity checks covering tamper and chain-break detection.

**Reproduction Command:**
```bash
python -m eval.tv_eval --output-dir eval/evidence
```

**Git SHA:**
`582e65973d6349408e27ba36e608df29da457b44`

**Evidence Manifest (SHA-256):**
```text
850c95fc9d11229f6dc742bab4eddacc240148f562f8772b353ef117f1d08330  TINY-VERDICTS-EVAL-001.json
598cee1e7d76894cda34b070e2d7083c243ef9e662bd6930734ce85b36e963f9  condition_a_direct.jsonl
4f2e2546e789adaa1e673a8c3167ee3920fbc681df7822e956631940823cb409  condition_b_vetproof.jsonl
```

## External gates still honest

- Live Bedrock execution needs runtime AWS credentials.
- Public repository, hosted URL, video upload, Builder.aws publication, and
  Devpost submission are external irreversible/publication actions.
- OSSF-style supply-chain claims remain limited to the checked lockfile, public
  license and recorded receipt hashes. No SLSA level or enterprise compliance
  claim is made by this demo.
