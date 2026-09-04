# ≤5-Minute Demo Skeleton

1. **Problem (0:00–0:35):** Agents can do useful work autonomously, but a
   consequential write must remain visibly human-authorized.
2. **Standing authority (0:35–1:10):** Show the zero-write child envelope and
   the deterministic `AuthorityGate`.
3. **Real bounded task (1:10–2:05):** Run the local agent; it reads the weekly
   status brief and drafts the output.
4. **Stop boundary (2:05–3:00):** Show `HUMAN_DECISION_REQUIRED`, the proposed
   path and byte count, and the disabled state before the boundary is reached.
5. **Decision and evidence (3:00–4:05):** Demonstrate DENY first: no output is
   written, yet an Ed25519-signed receipt is emitted. Then use the automated
   acceptance test for the approved branch rather than claiming a live approval.
6. **Replay (4:05–4:35):** Call `/api/replay`; show that the receipt chain and
   signatures verify. State the explicit limit: the demo signer is ephemeral,
   not a PIV/YubiKey identity.
7. **Close (4:35–5:00):** The agent works inside standing authority; a person
   decides at the consequential boundary.
