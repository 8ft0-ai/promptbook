# Decision capsules

Decision capsules are Promptbook's device-neutral handoff for a genuine `DECISION_REQUIRED` boundary. They make the smallest human choice obvious without requiring the user to copy repository identifiers or remember exact command syntax.

The governing principle is:

> Recommendation and choices first; governance detail second. Semantic intents are the stable protocol; keyboard, touch, natural language and voice are input adapters.

## Multiple-choice decisions

When there are several meaningful alternatives, present compact labelled choices:

```text
DECISION_REQUIRED — Deployment mechanism

Recommended: A

A — GitHub Actions + Workload Identity
B — Cloud Build
C — Defer
```

A user may respond with `A`, `Choose A`, `go with A`, the option name, or another clear equivalent when that decision is the only unresolved referent.

## Bounded approval decisions

When the question is whether to accept one concrete bounded proposal, do not manufacture A/B/C. Use semantic choices:

```text
DECISION_REQUIRED — Apply repository protection?

Recommended: ACCEPT

ACCEPT — Apply the approved bounded settings
REJECT — Do not apply them
CHANGE — Revise the proposal
```

Material authority, risk, cost, or security detail may follow below the choices when it changes what the human is deciding.

## Semantic intents

The stable interaction contract is:

- `ACCEPT` — accept the recommended bounded option for the current decision;
- `REJECT` — reject only the presented proposal or option;
- `CHOOSE <option>` — select a specific presented alternative;
- `CHANGE <instruction>` — request a revision to the proposal without approving that revision.

These are semantic intents rather than mandatory commands. Clear equivalents can be expressed by keyboard, touch, or voice, for example:

```text
A
Choose B
yes
go ahead
accept the recommendation
use Cloud Build
reject
change: keep the ruleset but defer secret scanning
```

Slash aliases such as `/accept` or `/choose B` may be understood as conveniences, but Promptbook does not require them and they are not part of the public shorthand-command vocabulary.

## Decision binding

A decision capsule must be bound to one concrete unresolved decision. The agent should retain enough authoritative identity to know what the response applies to, including:

- the decision target;
- the proposal or revision identity;
- the recommended choice;
- the bounded authority or effect granted by acceptance.

The human should not normally need to repeat those identifiers.

Before consequential mutation after `ACCEPT` or `CHOOSE`, refresh decision-critical state. If the proposal materially changed, do not migrate the earlier response to the new proposal. Re-present the decision instead.

Accepted authority is consumed once for the bounded object only. If existing governance already authorises the routine implementation, validation, review/merge progression, verification, or close-out that follows, continue automatically without another `proceed` confirmation.

## Rejecting and changing

`REJECT` is deliberately non-destructive. It does not automatically close the issue, abandon the overall objective, undo completed work, or select another option. Reconstruct the changed decision state and present another recommendation when one is safely determined.

`CHANGE` asks for a revision. The revised proposal must be re-presented for decision unless the user's wording explicitly grants authority for that revised proposal. A request to change something is not implicit approval of whatever revision results.

## Ambiguity and voice

Short responses are useful on phones, tablets, laptops and voice interfaces, but only when their referent is clear.

If exactly one unresolved decision exists, responses such as `yes`, `A`, `accept`, `go ahead`, or a spoken option name may be safely interpreted from context. If more than one unresolved decision or plausible referent exists, fail closed and ask which decision the user means rather than guessing authority.

If natural language conflicts with the presented labels, follow the explicit meaning rather than forcing the response into a predefined intent. For example, `Choose B but keep the current authentication model` is a choice plus a material qualifier and should be evaluated as such.

## Relationship to `/go`

Decision responses and `/go` serve different purposes:

- `/go` means continue work where no new human decision is required;
- `ACCEPT` or `CHOOSE` grants/selects the specific bounded decision just presented.

A valid accepted decision should return control to governed autonomous progression immediately when the remaining work is already authorised.

## Precedence

Decision capsules never override repository-local instructions, explicit task authority, branch protection, security controls, validation requirements, fresh-review boundaries, or platform safety constraints. They improve the human handoff; they do not weaken the governance boundary that required the decision.
