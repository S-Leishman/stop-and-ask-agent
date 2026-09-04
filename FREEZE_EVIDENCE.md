# STRANDS-SPIKE-001 local freeze evidence

Status: `MINIMUM_VALID_SUBMISSION_CANDIDATE`

## Reproducible local acceptance

```bash
python -m pytest -q tests
python demo.py --decision deny --state-dir /tmp/vetproof-demo
```

Observed 2026-09-04:

- 14 acceptance tests passed.
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

## External gates still honest

- Live Bedrock execution needs runtime AWS credentials.
- Public repository, hosted URL, video upload, Builder.aws publication, and
  Devpost submission are external irreversible/publication actions.
