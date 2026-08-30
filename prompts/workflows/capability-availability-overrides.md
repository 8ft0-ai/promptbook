# Capability availability overrides

## Purpose

Define a small portable Promptbook contract for explicitly narrowing use of a technically exposed capability when that capability is known to be unavailable, unreliable, or intentionally suppressed for a bounded execution context.

Capability availability is execution state, not authority. An availability override may prevent an otherwise authorised action from being attempted. It must never authorise an action that the governing repository, task, owner decision, Promptbook operation, or resolved run context does not already permit.

## When to use

Use this contract when a governed workflow has already resolved the authority for a material action but execution depends on an external capability whose availability may differ by executor, connector, managed Project, repository, or task.

Use an explicit override only for capabilities whose temporary availability materially affects safe progression. Do not turn ordinary executor discovery, feature experimentation, or general configuration into a broad feature-management system.

The first supported capability key is:

```text
pull_request.mark_ready
```

It controls only the technical transition of an existing draft pull request to ready-for-review state. It does not control whether the pull request should semantically be draft, whether review is authorised, or whether any other pull-request mutation is permitted.

## Prompt

```text
Before invoking a governed external capability that has a Promptbook availability key, resolve its effective availability from the current authoritative configuration and preserve the configuration provenance that affected the action.

Resolve authority first. Capability configuration may narrow an action already classified as authorised, but it must never turn an unauthorised, forbidden, stale, or separately governed action into an authorised one.

If the effective availability is disabled, do not invoke or probe the affected capability. Use the workflow's bounded alternative or capability-boundary hand-off instead. If the effective availability is enabled, attempt the capability only when independently authorised and otherwise executable, then verify the observed resulting state rather than treating configuration as evidence of success.

Fail conservatively for unknown values, contradictory declarations at the same effective precedence, or stale configuration whose applicability cannot be established. Do not silently widen behaviour.
```

## Inputs

Resolve only the inputs needed for the current capability decision:

- the exact governed action and its independently resolved authority classification;
- the portable capability key, when one is defined;
- explicit current-user or task-scoped availability override, if any;
- repository/task availability configuration, if any;
- managed Project availability configuration, if any;
- the documented Promptbook default;
- provenance and freshness sufficient to identify which declaration controlled the result; and
- the current lifecycle state needed to choose a safe fallback.

The representation may be textual or structured. A minimal logical declaration is:

```text
capability_availability:
  pull_request.mark_ready: enabled | disabled
```

The representation is intentionally portable. Executors and integrations may map this logical key to their own mechanism names without changing the Promptbook meaning.

## Resolution and precedence

Resolve one effective value using this precedence, highest first:

1. explicit current-user or task-scoped override for the current governed work;
2. repository/task-specific configuration;
3. managed Project configuration;
4. Promptbook documented default.

A lower-precedence source cannot override a valid higher-precedence declaration. Preserve enough provenance to identify the effective source whenever availability affects execution or a fallback.

For the initial `pull_request.mark_ready` key, the documented default is:

```text
enabled
```

`enabled` means **no Promptbook availability override suppresses the capability**. It does not mean the executor implements the capability, that the mechanism is healthy, or that the action is authorised.

Missing configuration therefore preserves pre-existing behaviour. Re-enabling a temporarily disabled capability requires only changing the applicable configuration value back to `enabled`; workflow prose does not change.

Unknown values, contradictory declarations at the same effective precedence, unresolved applicability, or stale configuration must not default to `enabled`. Treat that capability as unavailable for the current attempted action until configuration can be resolved safely.

## Authority and availability

Keep authority and availability separate:

```text
capability availability != authority
```

For a capability-bearing action, executable capability is a monotonic narrowing of independently resolved authority:

```text
effective_executable_capability =
    authority_permitted_capability
    ∩ operation_ceiling
    ∩ technically_available_capability
    ∩ configured_available_capability
```

No term on the right may add authority absent from `authority_permitted_capability` or widen an operation ceiling.

In particular, `enabled` must never grant repository mutation, review publication, merge, release, deployment, repository-settings mutation, credential use, provider mutation, production mutation, or any other separately governed effect.

`disabled` means Promptbook must not invoke or probe the affected capability in the current governed execution path. A known-disabled capability is not repeatedly retried merely because the underlying operation remains desirable.

## First capability: `pull_request.mark_ready`

### Disabled

When `pull_request.mark_ready = disabled`, do not invoke the draft-to-ready transition.

If implementation is already complete, required validation has passed, no genuine lifecycle hold remains, and independent review is the next governed gate, prefer creating the pull request as non-draft in the first place. This avoids manufacturing a later transition solely because draft creation was habitual.

Do not use that shortcut when draft state expresses a real hold. A pull request remains legitimately draft while implementation, validation, an unresolved decision, another required gate, or repository-local policy says it is not yet reviewable.

When a legitimately draft pull request later becomes reviewable and the transition is independently authorised but the capability remains disabled or otherwise unavailable, treat this as an execution capability boundary. Produce the smallest complete `EXTERNAL_REQUIRED` hand-off needed to mark that exact pull request ready. Do not reclassify the action as requiring new owner authority merely because the mechanism is unavailable, and do not repeatedly invoke the configured-disabled capability.

The hand-off must identify the exact pull request and preserve the normal Promptbook external-action requirements. Where a browser/UI transition is appropriate, the bounded procedure is:

1. open the exact draft pull request;
2. confirm it is still the intended pull request and still in draft state;
3. confirm the real hold has been cleared and current authority still permits making it reviewable;
4. choose **Ready for review** in the GitHub pull-request interface;
5. do not merge, approve, modify unrelated metadata, or perform another lifecycle transition as part of this hand-off; and
6. return evidence that the pull request is now non-draft/ready for review.

### Enabled

When `pull_request.mark_ready = enabled`, the normal transition may be attempted only after the exact action is independently authorised and current lifecycle state still requires it.

After invocation, verify the observed pull-request state. Configuration is not execution evidence. If the mechanism fails, returns an integration/schema error, or leaves the pull request draft, record that truthfully as execution unavailability/failure and route through the bounded capability fallback. Do not reinterpret a failed mechanism as an authority failure, and do not report success merely because the flag was enabled.

## Executor projection

Availability resolution composes with [Executor capability projection](executor-capability-projection.md) rather than replacing it.

Promptbook first resolves authority and the operation-specific capability ceiling. Availability may then remove an otherwise eligible capability before or during executor intersection. A projected or executor-supported capability must still respect an effective `disabled` override.

For portable projection, the pull-request ready transition belongs to the material capability class:

```text
work_item_state_transition
```

That class is narrower than general work-item or repository mutation. It does not imply `work_item_evidence_update`, `review_publish`, `candidate_write`, `merge`, `release_publish`, `deploy`, or any other effect.

When availability affects projection or execution, retain provenance sufficient to reconstruct the effective override and distinguish these cases:

- authority denied the action;
- configuration disabled the capability;
- the executor did not support the capability;
- a configured-enabled mechanism failed at runtime; and
- the capability executed and the resulting state was verified.

## Configuration provenance and freshness

Availability configuration is derived execution input, not durable action authority. Record enough provenance to identify the effective source and value when the decision affects execution, for example:

```text
capability_key
resolved_value
source_class
source_identity_or_reference
resolved_for_work_identity
resolved_at_or_freshness_bound
```

Do not embed secrets, connector diagnostics, or private environment state merely to preserve provenance.

Re-resolve before a consequential use when a decision-critical source may have changed. A configuration resolved for one task, repository, managed Project state, or capability key must not silently carry across to another context.

If the effective value cannot be reconstructed from current applicable sources, fail conservatively for that capability rather than assuming availability.

## What it does

Adds a small reversible configuration layer between independently resolved authority and capability execution. It lets Promptbook avoid known-broken or intentionally unavailable transitions without changing desired workflow semantics, and lets operators re-enable those transitions through configuration alone when the underlying integration recovers.

The first concrete behaviour avoids unnecessary draft-to-ready transitions for reviewable implementation candidates, preserves legitimate draft/WIP semantics, provides a complete bounded fallback when a real draft later becomes reviewable, and verifies enabled transitions from observed state.

The design can accommodate additional explicitly governed capability keys later, but this contract does not define or pre-authorise any additional keys.

## Boundaries / limitations

This contract does not modify or repair an external connector, implement an executor, probe capabilities automatically, create a remote feature-management service, add shorthand commands, make draft pull requests universally invalid, or grant action authority.

It does not make configuration a new repository-policy or workflow-authority source. Higher-precedence repository/task authority, operation ceilings, current evidence, freshness requirements, and explicit owner decisions remain controlling.

Automatic health probing is outside this contract. A successful probe, installed tool, credential, network path, or executor implementation could establish feasibility evidence but could never create action authority.

## Status

`experimental`
