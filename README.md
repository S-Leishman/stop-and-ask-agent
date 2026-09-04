# Stop-and-Ask Agent — an agent that works autonomously and stops at the boundary

**The problem.** AI agents that do real work make real changes to real systems.
The dangerous moment is not the work — it's the write that nobody explicitly
authorized. Most demos hide that moment in a log line.

**Who it's for.** Anyone who needs an agent to keep working while they're not
watching — and needs proof of exactly what the agent was allowed to do, what it
did, and which human decided the parts that mattered.

**What it does.** The agent runs inside a standing authority envelope that
carries **zero** unattended durable writes. It reads its brief, drafts the work,
and the moment it reaches the effect ceiling it stops, shows one screen —
proposed action, authority check, ceiling, decision — and waits. A human hits
APPROVE or DENY. Every decision lands in an Ed25519-signed, sha256-linked,
append-only receipt chain that replays: mutate a single byte and verification
fails.

```
PROPOSED ACTION → POLICY / AUTHORITY CHECK → EFFECT CEILING
      → HUMAN DECISION REQUIRED → (APPROVE) → EFFECT COMMITTED
      → SIGNED RECEIPT → REPLAY VERIFIED        (or) → DENIED BY HUMAN
```

**Architecture.**

```text
human principal (you)
      │  grants standing envelope (frozen contract, zero unattended writes)
      ▼
child agent envelope  ── monotonic narrowing: child ⊆ parent, ceilings only shrink
      │
Strands agent (tools: read_brief, request_commit)
      │  in-envelope work runs autonomously
      ▼
AuthorityGate (deterministic, code — not the model)
      │  effect ceiling reached → REQUIRES_HUMAN
      ▼
one-screen decision (APPROVE / DENY)
      ▼
receipt chain (Ed25519-signed, sha256-linked) ── replay verification
```

The authority decision is deterministic code. The model — whichever model —
proposes; it never grants itself permission.

## Run it

```bash
python3 -m venv .venv && ./.venv/bin/pip install -r requirements.txt
./.venv/bin/python server.py 8474
# open http://127.0.0.1:8474 and click RUN AGENT
```

Tests (no keys, no network):

```bash
./.venv/bin/python -m pytest tests -q
```

Optional LLM mode (AWS credentials with Bedrock access required):

```bash
AEVION_MODEL=bedrock ./.venv/bin/python server.py
```

## Known limitations (honest list)

- Receipts are signed with an ephemeral Ed25519 key and embed its public key
  for independent replay. They are not yet bound to a persistent PIV/YubiKey
  identity, so the demo does not claim cryptographic non-repudiation of the
  human's identity.
- The demo task is deliberately small (one read, one draft, one bounded write).
- LLM mode requires AWS credentials; scripted mode runs the identical
  authority/receipt path offline.
- Single-user, loopback only. No multi-tenant anything.

## License

Apache-2.0
