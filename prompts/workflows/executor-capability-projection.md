# Executor capability projection

## Purpose

Define the Promptbook contract for projecting a resolved agent run context into a bounded executor-facing capability profile. The profile lets an execution substrate enforce no more than the capabilities already authorised for the resolved `/review`, `/fix`, or `/go` operation.

This contract is a companion to [Resolved agent run context](resolved-agent-run-context.md). Promptbook owns the workflow-side projection semantics. A consuming executor owns only its supported mechanisms, local safety policy, enforcement and evidence; it does not become a repository-policy, workflow-policy or owner-decision authority source.

## Core invariant

Projection may narrow authority but must never widen it:

```text
projected_executor_capabilities
    ⊆
resolved_effective_capabilities
```

A consuming executor may narrow again:

```text
actual_executor_capabilities =
    projected_executor_capabilities
    ∩
    executor_supported_capabilities
    ∩
    executor_local_safety_policy
```

The executor-side intersection cannot add a capability absent from the Promptbook projection.

Technical availability is never authority:

```text
executor has tool / credential / network / API access
    ≠
executor is authorised to expose or use it
```

## When to project

Project an executor profile only when a resolved operation is delegating or exposing one or more material capabilities to an execution substrate.

Do not create a profile merely because an executor exists. Advisory reasoning or work that remains entirely inside the current governed context does not acquire an executor profile unless a capability is actually being exposed or delegated.

For `/go`, projection at a consequential gate is action-specific. Do not project one broad lifecycle profile containing every capability that might eventually be useful.

## Required profile

The representation may be textual or structured and does not need to be persisted for every run. It should be logically equivalent to the decision-critical subset of:

```text
profile_version
operation
repository_identity
governing_work_or_objective_identity
bound_state_identity
resolved_context_identity_or_provenance
allowed_capabilities
denied_capabilities
execution_constraints
stale_or_expiry_conditions
required_execution_evidence
projection_provenance
```

`bound_state_identity` is the immutable candidate, lifecycle result, accepted proposal identity, or other sufficiently exact state against which the projected capability is valid.

`execution_constraints` may describe bounded repository, branch, filesystem, network, credential, provider or external-service limits when those limits are decision-critical. The profile must not contain secret values or unnecessary environment state.

The profile is derived execution state, not a durable authority source. If it conflicts with current authoritative inputs, current authoritative inputs win and the profile is stale.

## Portable capability vocabulary

Use the smallest capability vocabulary that preserves material effect boundaries. The initial portable classes are:

```text
repository_read
work_item_read
ci_evidence_read
candidate_write
work_item_evidence_update
review_publish
validation_execute
workflow_dispatch
merge
release_publish
deploy
repository_settings_write
credential_use
external_filesystem_read
external_filesystem_write
network_access
provider_mutation
production_data_mutation
```

A concrete executor may use a more specific internal vocabulary, but it must map each executable effect back to one or more projected portable classes without weakening the Promptbook boundary.

Do not infer broad capability from a narrower class. For example, `repository_read` does not imply `candidate_write`, and `merge` does not imply `release_publish` or `deploy`.

## Projection from the action gateway

For every material capability or exact action being delegated, preserve the resolved authority classification:

```text
ALLOW
  → capability may be eligible for projection

REQUIRE OWNER / SEPARATE AUTHORITY
  → capability must not be projected as executable authority

FORBID
  → capability must not be projected
```

`ALLOW` is necessary but not sufficient. Project only capability needed for the current operation/action. An executor may then remove projected capability because of unsupported mechanisms, stronger local policy, guard failure or stale state.

Keep authority and feasibility distinct. A capability denied by Promptbook authority is not the same result as a capability that is authorised but unsupported by the executor.

## No ambient authority from environment state

None of the following may widen a projection:

- a connector, shell, API or plugin being installed;
- repository write permission;
- a credential, token or cloud identity being present;
- network reachability;
- executor support for a capability;
- a previous operation having been authorised;
- a prior approval whose bounded action has already been consumed; or
- a previous successful execution.

Credential, network or provider capability may be projected only when the resolved operation establishes both the action authority and the bounded need for that capability class. A profile must never expose credential capability merely because credentials exist.

## Operation profiles

### `/review --read-only`

A representative projection may include:

```text
repository_read
work_item_read
ci_evidence_read
```

It must not include any write capability, including `review_publish`.

### Ordinary `/review`

A representative projection may include:

```text
repository_read
work_item_read
ci_evidence_read
review_publish
```

`review_publish` is the narrow router-authorised review-record write only. It does not imply candidate mutation, workflow dispatch, merge, release or deployment.

### `/fix`

A representative bounded remediation projection may include:

```text
repository_read
work_item_read
candidate_write
work_item_evidence_update
validation_execute
```

It must not include `merge`, `release_publish` or `deploy` under the `/fix` operation ceiling. Provider, settings, credential or production mutation remains absent unless another separately governed contract has already made the exact action effective authority and the current Promptbook operation permits projection of that bounded effect.

### `/go`

A `/go` profile is derived for the exact next governed action. For example, independently authorised merge of candidate A may project `merge` bound to A, while `release_publish` and `deploy` remain absent.

After merge creates result M, the A-bound profile is stale. A later release or deployment requires a newly resolved action gateway and a newly projected profile bound to the applicable resulting state and authority.

## Identity and stale-profile invalidation

Before execution, an executor must be able to verify that the profile still matches the target state and declared guards without reconstructing the full Promptbook workflow policy.

Invalidate and re-project when a decision-critical input changes, including where applicable:

- candidate or result identity;
- governing work/objective authority;
- accepted proposal identity or bounded approval state;
- operation or operation ceiling;
- required checks or other freshness-sensitive preconditions;
- repository instructions or policy that affect the action; or
- declared expiry/freshness bounds.

Examples:

```text
/review profile for candidate A
    ≠
/review profile for candidate B
```

```text
/fix profile bound to starting candidate A
    must not authorise writes against moved candidate A'
```

```text
/go merge profile for candidate A
    ≠
release or deploy profile for merge result M
```

A consumed approval is not a reusable profile input. If a proposal materially changes before execution, stale approval must be re-resolved before capability can be projected again.

## Executor enforcement result

The executor should return bounded evidence logically equivalent to:

```text
profile_identity
bound_state_identity
requested_capability
enforcement_decision
executor_capability_intersection
execution_status
result_identity_or_evidence
limitations
```

Use distinct result classes when they affect governed continuation:

- `PROFILE_DENIED` — the requested capability was not projected as executable authority;
- `EXECUTOR_UNSUPPORTED` — the capability was projected but the executor cannot provide it;
- `STALE_PROFILE` — decision-critical state no longer matches the profile;
- `GUARD_MISMATCH` — a required execution guard failed;
- `EXECUTED` — the bounded capability executed and result/evidence was observed.

The shareable result must not include raw secret values, broad environment dumps or private diagnostic content merely because the executor can observe them.

## Consumer contract

A compliant executor consumer must:

1. verify the profile version and bound identities it understands;
2. reject unknown or materially ambiguous capability semantics rather than widening them;
3. intersect the projected capabilities with supported capability and local safety policy;
4. execute only the requested capability that survives that intersection and all required guards;
5. never interpret arbitrary command text as authority when the projected contract names a bounded capability;
6. return bounded enforcement evidence; and
7. leave any next workflow, owner decision, merge/release/deploy progression or acceptance decision to the governing Promptbook/repository context.

Executor-local policy may be stricter than Promptbook projection. It must not be weaker in a way that widens executable authority.

## Delegation invariant

Projection preserves the broader delegation rule:

```text
child_authority ⊆ parent_authority
```

A child or external executor profile must be a subset of the parent operation's current effective capabilities, further narrowed to the child action need. Delegation cannot refresh stale parent authority or manufacture new capability classes.

This contract does not define native subagent infrastructure or a complete delegated-agent protocol.

## Evidence and limitations

Capability projection is itself a policy contract. Documentary presence is `STATIC` evidence. Tests exercising the contract are `EXECUTED` evidence. Repository-hosted checks or retained execution records are `DURABLE` evidence when inspected.

Do not claim machine enforcement until a real executor has consumed the profile and demonstrated enforcement. A later executor implementation must be governed separately.

## Boundaries / limitations

This contract does not implement an executor, sandbox, network policy engine, credential broker, secret distributor, remote worker, OCI runner, deployment framework, provider policy or production mutation policy.

It does not change the authority semantics of `/review`, `/fix`, or `/go`; it only projects their already-resolved effective capabilities into a form an executor can further restrict and enforce.

External executors remain mechanisms, not Promptbook workflow-policy authorities.

## Status

`candidate`
