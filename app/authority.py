"""Authority envelope for the Stop-and-Ask agent.

Delegation monotonicity: a child contract may never contain an effect,
budget, or right absent from its parent. Effects outside the standing
envelope REQUIRE a fresh human decision before they can commit.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Decision(Enum):
    ALLOWED = "ALLOWED"                    # inside standing envelope: act autonomously
    REQUIRES_HUMAN = "REQUIRES_HUMAN"      # outside envelope: stop and ask
    DENIED = "DENIED"                      # explicitly forbidden: never propose


ALLOWED, REQUIRES_HUMAN, DENIED = Decision


@dataclass(frozen=True)
class AuthorityContract:
    """Standing envelope granted by a human principal. Immutable once issued."""
    principal: str
    allowed_effects: frozenset[str]
    max_writes: int = 0                     # effect ceiling: durable writes allowed without asking
    spend_ceiling: float = 0.0
    delegation_rights: bool = False

    def derive_child(self, allowed_effects: frozenset[str], **overrides: Any) -> "AuthorityContract":
        """Monotonic narrowing: child subset ⊆ parent, ceilings only shrink."""
        illegal = allowed_effects - self.allowed_effects
        if illegal:
            raise ValueError(f"delegation monotonicity violation: child requests {sorted(illegal)} absent from parent")
        kw: dict[str, Any] = {
            "principal": overrides.get("principal", self.principal + "/child"),
            "allowed_effects": frozenset(allowed_effects),
            "max_writes": min(self.max_writes, overrides.get("max_writes", self.max_writes)),
            "spend_ceiling": min(self.spend_ceiling, overrides.get("spend_ceiling", self.spend_ceiling)),
            "delegation_rights": self.delegation_rights and overrides.get("delegation_rights", False),
        }
        return AuthorityContract(**kw)


class AuthorityGate:
    """Deterministic check: proposed effect vs standing envelope + consumed ceiling."""
    READ_EFFECTS = frozenset({"READ_WORKSPACE", "DRAFT_OUTPUT"})

    def __init__(self, contract: AuthorityContract):
        self.contract = contract
        self.writes_consumed = 0

    def check(self, effect: str) -> Decision:
        if (
            effect.startswith("DELETE")
            or effect.startswith("DROP")
            or effect.startswith("OVERWRITE_CANONICAL")
            or effect in ("DELETE_DATA", "EXTERNAL_SUBMIT", "SPEND", "CREDENTIAL_CHANGE")
        ):
            return DENIED
        if effect in self.contract.allowed_effects or effect in self.READ_EFFECTS:
            if effect.endswith("WRITE") or effect == "COMMIT_OUTPUT":
                if self.writes_consumed >= self.contract.max_writes:
                    return REQUIRES_HUMAN      # ceiling reached: stop and ask
                self.writes_consumed += 1
            return ALLOWED
        return REQUIRES_HUMAN
