# TV-EVAL-001

This is a credential-free, synthetic fixture study of the effect boundary. It
is not a BFCL, τ²-bench, or AgentDojo score. Those adapters are future work.

Run it from the repository root:

```bash
python -m eval.tv_eval --output-dir eval/evidence
```

The run creates one JSONL receipt chain per condition and
`eval/evidence/TV-EVAL-001.json`. Each row records the fixture revision,
proposed effect, expected class, Tiny Verdict, commit decision, hashes, and
signed receipt data. Integrity checks deliberately mutate a receipt and break a
chain; both must be detected.

Conditions:

- `baseline`: direct permissive effect execution.
- `native_hitl`: human-intervention-style approval without VetProof's bounded
  authority/state/delegation checks.
- `vetproof`: deterministic authority/effect gate; `UNKNOWN` stops at the
  human boundary and does not commit without approval.

Headline metrics are descriptive measurements of these fixtures only. They are
not claims about a language model's intelligence or about external benchmarks.
