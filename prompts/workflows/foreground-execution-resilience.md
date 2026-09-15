# Foreground execution resilience

## Purpose

Preserve a coherent immutable continuation point when a substantial governed foreground session risks ending before all candidate-bound assurance or reconciliation can finish.

This is a persistence and reconstruction contract. It does not weaken validation, make incomplete work complete, create review freshness, or grant implementation, pull-request, merge, release, deployment, credential, settings, production, or execution-surface authority.

## When to use

Use during authorised implementation or remediation when foreground-execution exhaustion becomes a material risk before the normal lifecycle can reach its next durable boundary.

Use an approximately **18-minute** foreground budget only as an empirical, provisional operating hypothesis for ordinary Chat execution. It is configurable and revisable from observed behaviour and is **not** an asserted OpenAI or platform hard timeout. When no trustworthy remaining-time signal exists, use conservative task-shape and risk judgement rather than inventing timing precision.

## Contract

```text
When foreground-execution exhaustion is a material risk, preserve one coherent immutable governed state before spending the remaining practical foreground budget on work that can safely continue later.

For repository implementation work, the normal minimum continuation point is an exact candidate commit. Where pull-request creation is already authorised, appropriate, and executable without widening authority, an exact candidate plus a PR bound to that candidate is preferred. PR creation is never mandatory merely to beat a foreground budget.

Before establishing that checkpoint:
1. finish the smallest coherent scoped implementation state;
2. perform the minimum pre-publication safety checks needed to know the state is coherent, within scope, non-secret, and safe to preserve;
3. establish one immutable candidate identity;
4. record any unresolved lifecycle/assurance state truthfully.

Do not prefer a half-written workspace, avoidable transient multi-commit state, or known unsafe/incoherent publication merely to create a checkpoint quickly.

Distinguish pre-publication safety checks from authoritative candidate-bound assurance. Safety checks justify preserving the candidate; they are not substitutes for repository-required tests, static checks, CI, integration evidence, review, or any other required assurance. Validation evidence from different bytes must never silently transfer to the checkpoint candidate.

After the immutable candidate exists, spend remaining foreground budget on work that can be resumed safely against that exact identity, including repository-required candidate-bound assurance, exact-head CI observation, pull-request/evidence reconciliation, and preparation for the genuinely fresh review boundary.

If the session ends after the checkpoint, a later governed session may continue from the same exact candidate only after reconstructing current authority, repository/task policy, lifecycle state, candidate identity, validation/CI state, and material evidence from durable authoritative sources. Prior-chat memory must not be required for safe continuation. Crossing a session boundary grants no new implementation, mutation, pull-request, merge, release, deployment, credential, production, close-out, or other lifecycle authority.

A continuation context that authored, remediated, reconciled, or otherwise materially shaped the candidate remains non-fresh for substantive independent review. Session splitting does not create review independence; use the existing fresh-review contract.

Foreground-budget pressure may influence selection only among execution surfaces already authorised and eligible under current repository/task constraints. It must not create authority for Work, Codex, connected/native execution, hosted/hermetic execution, owner-local execution, or any other surface.

If interruption occurs after a conforming checkpoint, report the exact immutable continuation identity and unresolved lifecycle state rather than implying completion. If interruption occurs before a conforming checkpoint, report the actual incomplete durable state. Never fabricate a candidate, PR, validation result, review state, or recoverability claim.

Do not add a new conversational terminal state for foreground exhaustion. Represent the interruption and recovery evidence beneath the existing Promptbook terminal-state model.
```

## Deterministic recovery shape

The intended recoverable sequence is:

```text
substantial governed implementation
  -> foreground budget risk becomes material
  -> coherent candidate C is persisted durably
  -> session ends before CI/reconciliation completes
  -> later session starts without prior-chat memory
  -> authority and lifecycle state reconstructed from durable sources
  -> exact candidate C recovered
  -> exact-head CI/reconciliation completed
  -> genuinely fresh review boundary reached
```

The sequence remains fail closed. Candidate `C` is a persistence identity, not evidence that validation passed, review occurred, or the broader objective completed.

## Negative requirements

The contract must never be interpreted to mean that:

- approximately 18 minutes is a documented hard platform limit;
- incoherent, unsafe, secret-bearing, or knowingly out-of-scope work should be published to beat a timer;
- candidate or PR mutation authority may be manufactured by budget pressure;
- a checkpoint is validated, approved, review-ready, merged, released, deployed, or complete merely because it is durable;
- stale validation applies to changed bytes;
- a continuation session is fresh for review merely because it is new;
- an otherwise prohibited execution surface becomes eligible to avoid a foreground limit; or
- conversation memory is a required persistence store for governed continuation.

## Integration

[Implement an approved issue](../engineering/implement-an-approved-issue.md) applies this contract when implementation or remediation work faces material foreground-execution risk. [Autonomous progression](autonomous-progression.md) applies the reconstruction side when governed continuation resumes from a durable checkpoint.

## Status

`tested`
