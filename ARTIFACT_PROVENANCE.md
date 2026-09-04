# Artifact provenance and runtime boundary

This file keeps the competition claims aligned with the company artifact
record. It is intentionally conservative: an artifact may be real and useful
without being a proven part of this submission.

## Submission runtime (proven)

- Python 3.13 runtime with `strands-agents==1.54.0`.
- Deterministic authority gate, Tiny Verdict, signed receipt, and replay path.
- Local HTTP UI and acceptance tests are runnable from this repository.
- Public repository: https://github.com/S-Leishman/stop-and-ask-agent

## Existing company artifacts (proven in their recorded scope)

- `G:/Aevion-Backup/Aevion-Verifiable-AI/rust/aevion-tsf`: Apache-2.0 Rust
  Temporal State Fabric source with event, effect, commit, branch, store, and
  replay modules. Existing `target/` binaries are Windows artifacts and are not
  treated as Cloudflare/Linux deployment binaries.
- `C:/.../external-surface-dendrites-001`: Rust read-only synthetic registry
  crate. Its current `UNLICENSED`/non-publishable posture excludes it from the
  public competition dependency set until licensing is resolved.
- Aevion Pi PQ evidence pane: ML-DSA capability and ZymKey/PKCS#11 presence are
  recorded for the Pi host. The receipt explicitly does not prove deployment,
  owner-identity signing, or exposed keys.
- IBM Quantum receipts: physical QPU access is recorded, but no quantum
  advantage or competition relevance is claimed.

## Competition disclosure boundary

The event requires a new project and asks participants to disclose pre-existing
code/work incorporated. The current P0 entry therefore claims only the Python
Strands-compatible path above. Rust TSF/PQ integration is a future, separately
verified adaptation unless its provenance, license, Linux build, and in-period
work are documented before inclusion.

## Cloudflare deployment decision

The hosted target is a Cloudflare Container running the Python service. This
preserves the Strands/cryptography/filesystem behavior that a Python Worker
cannot currently guarantee. Deployment still requires an authenticated
Cloudflare account on an eligible paid plan and a working Docker build
environment; credits alone are not evidence of either.
