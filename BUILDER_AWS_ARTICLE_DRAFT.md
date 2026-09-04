# VetProof: Give every consequential AI action a Tiny Verdict

AI agents are useful precisely because they can do work while people are not
watching. That creates a sharp question at every consequential boundary: may
this principal perform this exact effect, under this authority, against this
state, now?

VetProof answers that question with a Tiny Verdict: `PASS`, `FAIL`, or
`UNKNOWN`. The agent may continue only on `PASS`. `FAIL` denies the effect.
`UNKNOWN` becomes `HUMAN_DECISION_REQUIRED`; the agent stops rather than
guessing.

Our Agents for Humans demo uses a Strands-compatible stop-and-ask agent. A
standing authority envelope permits workspace reads and drafting but carries
zero unattended durable writes. The agent drafts a status update, proposes
`COMMIT_OUTPUT`, reaches its effect ceiling, and waits for an explicit human
decision. The decision is stored with the Tiny Verdict in an Ed25519-signed,
hash-linked receipt chain that can be replayed.

The important point is not a dashboard score. It is a narrow, inspectable,
testable answer at the exact moment an agent would have an effect.

## Run the evidence path

```bash
python demo.py --decision deny --state-dir /tmp/vetproof-demo
```

The command emits a signed `FAIL` Tiny Verdict and verifies the receipt chain.
The UI shows the same sequence: proposed action, policy check, effect ceiling,
human decision, signed receipt, and replay.

## What this demonstration does not claim

The included offline path is deterministic and does not require cloud
credentials. A live Bedrock-backed Strands run remains to be recorded once
runtime AWS credentials are available. The demo signer is ephemeral Ed25519,
not a PIV/YubiKey identity.
