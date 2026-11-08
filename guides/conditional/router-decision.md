# Router Decision

**Conditional contract:** Load for a genuine owner decision, explicit approval or consequential alternative.

## Decision capsules

When a genuine human decision is required, do not end with a repository identifier or approval sentence the user must copy. Present the smallest concrete decision as a compact recommendation-first **decision capsule**.

For multiple meaningful alternatives, use compact option labels:

```text
DECISION_REQUIRED — Deployment mechanism

Recommended: A

A — GitHub Actions + Workload Identity
B — Cloud Build
C — Defer
```

For approval of one bounded proposal, use semantic choices rather than manufacturing A/B/C:

```text
DECISION_REQUIRED — Apply repository protection?

Recommended: ACCEPT

ACCEPT — Apply the approved bounded settings
REJECT — Do not apply them
CHANGE — Revise the proposal
```

Put recommendation and choices first. Add material authority, risk, or governance detail below the choices only when it affects the decision.

The canonical response protocol is semantic intent, not slash-command syntax:

- `ACCEPT` — accept the recommended bounded option;
- `REJECT` — reject only the presented proposal or choice;
- `CHOOSE <option>` — select a presented option;
- `CHANGE <instruction>` — request a revision without approving the revision.

Clear natural-language, short-form, touch, or voice equivalents may express the same intent when exactly one unresolved decision and its referent are unambiguous. Examples include `A`, `Choose A`, `yes`, `go ahead`, `accept the recommendation`, or naming the option directly. Slash aliases may be understood as conveniences, but they are not the protocol and are not added to the public shorthand-command vocabulary.

Bind every capsule to one concrete unresolved decision and the authoritative proposal/evidence needed to interpret it: the decision target, proposal or revision identity, recommendation, and bounded authority/effect of acceptance. The user should not normally need to repeat those identifiers.

Before consequential mutation after `ACCEPT` or `CHOOSE`, refresh decision-critical state. If the proposal materially changed, do not silently migrate the earlier response to the new proposal; re-present the decision. Consume accepted authority once for the bounded object only, then resume governed autonomous progression immediately when existing authority permits it.

`REJECT` does not implicitly close the issue, abandon the objective, undo prior work, or choose another option. Re-route from the changed decision state and present another recommendation when one is safely determined. `CHANGE` requests revision; after revising, re-present the decision unless the user's wording explicitly grants authority for the revised proposal.

If more than one unresolved decision exists, or a short response such as `yes`, `A`, or `accept` has more than one plausible referent, fail closed rather than guessing. Repository-local policy, validation, security controls, branch protection, and explicit task authority continue to take precedence.

See [Decision capsules](../decision-capsules.md) for the device-neutral interaction pattern and examples.
