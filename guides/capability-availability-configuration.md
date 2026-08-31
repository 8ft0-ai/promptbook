# Capability availability configuration

Use capability-availability configuration only for Promptbook capability keys whose temporary technical availability materially affects safe governed progression. Configuration narrows execution; it never creates action authority.

The first supported key is:

```text
pull_request.mark_ready
```

Its values are `enabled` and `disabled`.

## Resolution order

Promptbook resolves one value using this deterministic order:

1. explicit current-instruction or bounded current-task override;
2. governing work-item declaration;
3. repository declaration;
4. managed Project declaration;
5. Promptbook documented default.

A missing optional declaration falls through to the next source. An applicable declaration that is invalid, contradictory at the same exact tier/scope, stale, target-mismatched, or required-but-unavailable fails conservatively for that capability instead of silently falling through to an enabled result.

## Current instruction or bounded task

Use an explicit declaration in the current instruction when the override should apply only to the current governed work:

```text
For this work only:
capability_availability:
  pull_request.mark_ready: disabled
```

The declaration must be unambiguously bound to the current repository/work identity. Do not treat an old conversational statement as durable configuration for later unrelated work.

## Governing work item

A governing issue, pull request, accepted plan/design record, or equivalent durable work item may carry a task-scoped declaration:

```text
capability_availability:
  pull_request.mark_ready: enabled
```

The work-item identity is part of the configuration provenance. This declaration is configuration evidence only; it does not approve implementation, review, merge, release, deployment or any other action.

## Repository declaration

For a repository-wide override, place the declaration in repository-local instructions, preferably `AGENTS.md` when that is the repository's instruction entry point:

```md
## Promptbook capability availability

```text
capability_availability:
  pull_request.mark_ready: disabled
```
```

A repository declaration applies only to that repository unless repository-local authority explicitly establishes a narrower valid scope. Do not search arbitrary repository files for hidden declarations. If the repository uses another configuration document, repository-local instructions must explicitly reference it before Promptbook treats it as a carrier.

## Managed Project declaration

For a persistent ChatGPT Project or comparable workspace, add an optional block to the persistent Project instructions:

```text
CAPABILITY_AVAILABILITY
pull_request.mark_ready: disabled
```

This block is lower precedence than current-task, governing-work-item and repository declarations. It is execution configuration only. It does not become repository policy or repository authority merely because it is persistent.

The standard Promptbook bootstrap does not need to include this optional block by default. Add it only to Projects that need an override. Keeping the default bootstrap thin avoids turning Project setup into a generic feature-configuration surface.

## Promptbook default

When no applicable higher-precedence declaration exists, the first key resolves to:

```text
pull_request.mark_ready: enabled
```

`enabled` means only that Promptbook is not suppressing this named capability. It does not prove connector/executor support, mechanism health, successful invocation, or action authority.

## Inspecting the effective value

Before consequential use, Promptbook should be able to reconstruct a resolved record equivalent to:

```text
capability_key
resolved_value
source_class
source_identity_or_reference
source_precedence
resolved_for_repository
resolved_for_work_identity
freshness_or_version_identity
resolution_result
```

A fresh context given the same authoritative carriers for the same repository/work identity should reconstruct an equivalent result. Downstream autonomous progression or executor projection consumes this resolved record instead of rediscovering the carriers independently.

## Disabling and re-enabling

To suppress the current draft-to-ready mechanism at the desired scope, set:

```text
pull_request.mark_ready: disabled
```

To restore normal Promptbook behaviour at that same scope, set:

```text
pull_request.mark_ready: enabled
```

Or remove the optional declaration so resolution falls through to the next lower-precedence carrier or documented default.

Changing this value does not change whether the underlying action is authorised. A configured-disabled action that is independently authorised may still require a bounded external hand-off. A configured-enabled action still requires independent authority and observed-state verification.

## Unsupported keys

Do not invent new executable capability semantics by adding arbitrary names to these blocks. Unsupported keys do not acquire meaning until Promptbook explicitly defines them.
