# Resolved agent run context

## Purpose

Promptbook is the canonical owner of shared workflow semantics. The run context is **ephemeral derived state**, not a new durable authority source or competing execution policy. Operation profiles have separate capability ceilings.

## When to use

Derive decision-critical context before substantive `/go`, `/step`, `/fix`, `/review` or `/save` action. `/next`, `/status` and `/help` are read-only projections of the same evidence, not effects.

## Prompt

```text
Before a governed effect, derive the current Resolved Agent Run Context from authoritative repository/task evidence:
- selected operation, repository_identity, work_item_identity / governing_objective_identity, applicable_repository_instructions and resolved_authority_sources;
- exact immutable_candidate_identity, reviewed target snapshot or current result identity as applicable;
- effective_capabilities, prohibited_capabilities, owner_decision_boundaries and relevant approval identity;
- current_lifecycle_state, next_governed_action, required_preconditions, required_validation, required_evidence, completion_conditions and continuation_mode;
- changed-state, execution-locality and review-isolation evidence only where material.

This context is derived from current authoritative inputs, not from conversation memory or capability existence. A proposed action is not permission to execute it. Refresh only decision-critical evidence, then classify ALLOW, REQUIRE OWNER / SEPARATE AUTHORITY or FORBID. Missing or contradictory permission fails closed. If an authorised action cannot execute, determine whether a legitimate execution locality exists before involving the owner.

Keep mutable state and candidate identity current. Evidence for candidate A cannot establish candidate B's correctness or approval. Fresh review requires genuine independence and the exact target snapshot, not an agent role label. GitHub write-back and read-only review remain different authority profiles.

An action result must bind to observed evidence. A handoff or local workflow record cannot establish completion of the original goal. Under /go continue through another authorised action; under /step stop after one transition and its intrinsic verification.
```

## Cross-operation invariants

The explicitly effectful operation profiles are `/review`, `/fix`, `/go`, and `/save`; supporting one profile does not generalise another operation's permissions. Technical capability availability may only narrow executable capability; it must never create authority.

Resolve the proposed next governed action, required preconditions, required evidence, and completion conditions before consequential progression.

Use a single canonical derived execution-state contract: `/step` shares `/go`'s progression state and action gateway; `/next`, `/status`, and `/help` are read-only projections of the same state.

Equivalent authoritative inputs must not produce a different next transition merely because the user selected a different read-only projection command.

`/prompt` is pure artefact generation: prompt generation leaves the current governed state unchanged and establishes neither delegated authority nor freshness.

## Conditional capability and evidence profiles

Select only the operation and issue-specific contract that actually applies. The referenced clause becomes mandatory **before** the corresponding consequential action, but unrelated profiles must not be preloaded:

- `/go` / `/step` action gateway, exact state transition, approval consumption, execution locality → [Go context profile](../../guides/conditional/context-go.md).
- Independent `/review`, freshness, exact reviewed head, durable write-back → [Review context profile](../../guides/conditional/context-review.md).
- Bounded `/fix`, candidate transition, remediation readiness and fresh re-review → [Fix context profile](../../guides/conditional/context-fix.md).
- `/save` persistence → [Save context profile](../../guides/conditional/context-save.md).
- Shared capability availability, evidence projection and provenance edge → [Shared context evidence](../../guides/conditional/context-shared.md).

When an applicable referenced clause cannot be obtained canonically, stop rather than guessing. Do not let the amount of available tooling or a different operation's permissions widen authority.

## Inputs

- Governing objective, operation, existing scope/authorisation and repository-specific policy.
- Current authoritative work identity, immutable revisions and evidence of allowed effects.

## What it does

Provides one small common decision framework and separately loaded, fully specified operation-specific profiles. It does not require review, fix and save clauses to be loaded for ordinary goal execution.

## Boundaries / limitations

This is not credential, merge, deployment, cost, production or repository mutation authority. Preserve exact revision/currentness, genuine fresh review, GitHub write-back scope, separate approval boundaries, hard capability denial and required teardown. Do not transfer evidence between identities or substitute human action for available authorised execution.

## Status

`tested`
