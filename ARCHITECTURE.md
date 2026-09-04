# Stop-and-Ask Agent Architecture

```mermaid
flowchart TD
    H[Human standing authority\nzero unattended writes] --> P[Immutable parent contract]
    P --> C[Child agent envelope\nREAD_WORKSPACE + DRAFT_OUTPUT]
    C --> S[Strands Agent\nread_brief / request_commit]
    S --> G{AuthorityGate}
    G -->|in envelope| W[Read brief and draft status]
    W --> G
    G -->|COMMIT_OUTPUT exceeds ceiling| Q[HUMAN_DECISION_REQUIRED\nvisible local UI]
    Q -->|DENY| R1[Ed25519-signed denial receipt]
    Q -->|APPROVE| E[Commit output]
    E --> R2[Ed25519-signed commit receipt]
    R1 --> V[Replay verifier]
    R2 --> V
    V --> T[Competition Twin\nreal submission gates + next obligation]
```

The contract and gate are deterministic code. The model can propose a tool call,
but it cannot enlarge the child envelope or commit beyond its write ceiling.

`requirements.lock` records the full observed dependency set for the local
demonstration. A live Bedrock provider run remains an external credential gate.

The Competition Twin is a read-only view over the same execution/submission
evidence. It does not authorize or perform an effect: it identifies the next
required effect and whether that boundary requires a human.
