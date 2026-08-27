# Project bootstrap and shorthand commands

Use this pattern when a project or repository should use Promptbook repeatedly across chat sessions without copying full Promptbook workflow bodies into local instructions.

The intended layering is:

```text
project/workspace bootstrap and project-boundary guard
        ↓
repository-local authority
        ↓
Promptbook workflow router and task prompts
```

The bootstrap establishes the project identity, performs the pre-tool project-boundary check, and tells the agent where to start for governed work. Repository instructions remain authoritative for local scope and policy. Promptbook owns reusable workflow behaviour and shorthand semantics.

## Project bootstrap

For a ChatGPT Project or similar persistent workspace, copy the following bootstrap into the persistent project instructions and replace `<PROJECT_NAME>` and `<OWNER/REPOSITORY>` with that project's real identity. Extend `PERMITTED_CROSS_PROJECT_REFERENCES` only for repositories that are commonly referenced from this project without normally becoming its work target.

```text
CURRENT_PROJECT
name: <PROJECT_NAME>
primary_repository: <OWNER/REPOSITORY>

PERMITTED_CROSS_PROJECT_REFERENCES
- 8ft0-ai/promptbook

Before any substantive analysis, repository read, external tool call, or mutation for each new user instruction, apply a project-boundary preflight using only the project identity and conversation text already available. Do not use tools to decide the preflight.

Determine the apparent work target from strong evidence in descending order: explicit work-target language tied to a project/repository; issue, PR, branch, commit or other repository-owned identities tied to requested work; then repeated project/repository references associated with requested actions. Incidental documentation, workflow, dependency, comparison or evidence references are not work targets merely because they are mentioned. `PERMITTED_CROSS_PROJECT_REFERENCES` suppresses false positives for legitimate references only; it never authorises one of those projects as the work target.

Use these outcomes:
- `MATCH` — the instruction targets `CURRENT_PROJECT`, or naturally continues already-established work in this project without contradictory strong target evidence. Proceed silently.
- `PROJECT_MISMATCH` — strong evidence clearly makes another project the work target. Perform no substantive work, repository read, external tool call or mutation for that instruction. Warn with the current project, apparent target, reason, confirmation that no such work or tool use occurred, and recommend moving the prompt to the correct project. Require `ACKNOWLEDGE` (or an equally explicit statement to proceed here anyway) before executing the blocked instruction; otherwise stop.
- `PROJECT_AMBIGUOUS` — strong target evidence conflicts, suggests another project without a safely identifiable target, the configured project identity is missing/unresolved, or there is insufficient evidence to establish that the instruction targets `CURRENT_PROJECT` and it does not naturally continue already-established work in this project. Perform no substantive work or tool call. State the ambiguity and require the same explicit acknowledgement before proceeding here intentionally. A prompt that merely omits a project name is not ambiguous when it naturally continues this project's established work.

An acknowledgement is bound only to the exact blocked instruction and is consumed once. It does not disable this preflight for later prompts. If an acknowledgement also contains materially new work, apply the preflight separately to that new work. Do not depend on cross-project memory to infer the project identity.

For governed engineering work that passes the preflight, first read and apply repository-local instructions, including AGENTS.md when present.

Unless repository-local instructions specify another supported workflow, use `8ft0-ai/promptbook` → `prompts/workflows/README.md` as the governed-workflow entry point, using any Promptbook version/ref declared by the repository.

Reconstruct decision-critical current state from authoritative sources rather than stale conversation summaries. Preserve platform safety constraints, explicit task authority, repository-local policy, validation requirements and current evidence above Promptbook guidance.

Continue with minimal unnecessary human intervention until `EXTERNAL_REQUIRED`, `DECISION_REQUIRED`, `BLOCKED`, or `COMPLETE` applies. Interpret Promptbook shorthand commands according to the workflow router. The bootstrap selects workflow intent only and does not grant unrelated authority. A shorthand command may carry only the narrow authority intrinsic to the operation defined by the router; neither the bootstrap nor a command bypasses freshness, independence, validation or fail-closed behaviour.
```

The project-specific substitutions are mandatory for the guard to work. If `CURRENT_PROJECT` is missing or unresolved, governed or tool-using work should fail closed as `PROJECT_AMBIGUOUS` rather than pretending the current project boundary is known.

This text deliberately keeps the project-boundary check inside persistent instructions. A guard loaded only after a pasted prompt triggers repository or external tool access would be too late to guarantee that a mismatch is caught before tool use. The bootstrap still avoids duplicating the full lifecycle procedures or individual Promptbook prompt bodies; those remain versioned in Promptbook.

## Project-boundary guard

Treat the ChatGPT Project or persistent workspace identity as an execution boundary. The guard is intended to catch a prompt copied from another project before it causes repository reads, tool use or mutations in the wrong context.

The preflight should use information already present in the project instructions and current conversation. It must not perform a repository lookup merely to decide whether a repository lookup is safe. Strong work-target evidence is intentionally narrower than "another repository was mentioned": explicit continuation/review/implementation language, repository-owned issue or PR identities, or repeated repository references attached to requested actions are stronger than workflow entry points, dependencies, documentation sources, comparisons or evidence links.

`PERMITTED_CROSS_PROJECT_REFERENCES` is therefore a false-positive control, not an execution allowlist. For example, a project may list `8ft0-ai/promptbook` because its workflow entry point is routinely referenced. That does not make an instruction to "continue `8ft0-ai/promptbook` issue #23" valid inside some other project; explicit work-target language still wins and should produce `PROJECT_MISMATCH`.

A warning should be compact and acknowledgement-oriented. A suitable shape is:

```text
PROJECT_MISMATCH — acknowledgement required

Current project:
  <configured project name> — <configured primary repository>

Apparent target:
  <other project/repository and issue/PR when present>

Reason:
  <short explanation of the strong target evidence>

No substantive work, repository reads, external tool calls or mutations have been performed for this instruction.

Recommended: STOP and move this prompt to the target project.

ACKNOWLEDGE — proceed with this blocked instruction here anyway
STOP — do not execute it
```

Use the same acknowledgement choices for `PROJECT_AMBIGUOUS`, replacing the target with the conflicting or unresolved target evidence. `ACKNOWLEDGE` may be expressed by an equally explicit natural-language statement such as "proceed here anyway" when exactly one blocked instruction is pending. A generic conversational response should not be stretched into cross-project execution authority when the intent is unclear.

The override is deliberately narrow. It applies only to the exact blocked instruction, is consumed once, and must not disable the guard for subsequent prompts. If the acknowledgement message introduces materially new work, apply the normal preflight separately to that new work.

## Regression scenarios

These scenarios define the intended behaviour for the reusable guard:

| Scenario | Current project | New instruction | Expected outcome |
| --- | --- | --- | --- |
| Matched | `example-co/service-a` | `Continue example-co/service-a issue #12` | `MATCH`; proceed silently |
| Mismatched | `example-co/service-a` | `Continue example-co/service-b issue #9` | `PROJECT_MISMATCH`; no tool use; acknowledgement required |
| Ambiguous | `example-co/service-a` | `Review example-co/service-b#9 and implement example-co/service-c#4` | `PROJECT_AMBIGUOUS`; no tool use; acknowledgement required |
| Insufficient target evidence | `example-co/service-a` with no established task | `Investigate the deployment failure` | `PROJECT_AMBIGUOUS`; no tool use; acknowledgement required |
| Shared reference | `example-co/service-a` with `example-co/workflows` permitted | `Use example-co/workflows as the workflow entry point; continue example-co/service-a#12` | `MATCH`; the shared reference is incidental |
| Intentional cross-project override | `example-co/service-a` after a mismatch warning | `ACKNOWLEDGE` | Resume only the exact blocked instruction once; later prompts are checked again |

A prompt that omits an explicit repository but naturally continues established work in the current project is also `MATCH`. Absence of a repository name by itself must not create friction. A genuinely new instruction with insufficient evidence to establish `CURRENT_PROJECT` as the work target, and no established current-project work to continue, is `PROJECT_AMBIGUOUS`. Conversely, when strong target evidence points outside the current project and the target cannot be safely identified, use `PROJECT_AMBIGUOUS` rather than inspecting external state to resolve the question.

The guard does not depend on cross-project memory. Explicit project instructions are the source of truth for the current project identity; current conversation text may establish the current task, but memory from other projects is neither required nor trusted for this boundary decision.

## Repository declaration

For reproducible governed work after the boundary check passes, declare the Promptbook dependency in repository-local instructions. For example, an `AGENTS.md` can include:

```md
## Promptbook

This repository uses `8ft0-ai/promptbook@vX.Y.Z` for reusable governed-workflow guidance.

Workflow entry point: `prompts/workflows/README.md`.

Repository-local instructions, explicit task authority, security policy and validation requirements take precedence over Promptbook. Promptbook shorthand commands do not grant unrelated authority; a command may carry only the narrow operation authority defined by the pinned Promptbook router.

Use the shorthand commands defined by the pinned Promptbook workflow router; do not copy their implementation into this repository.
```

Pinning a stable release makes the workflow dependency reproducible and reviewable. A repository may deliberately track `main` instead, but that opts into behaviour changes as Promptbook evolves. Keep the project-level bootstrap version-neutral and let the repository own the pin or override.

The ChatGPT Project identity and repository Promptbook declaration serve different purposes. `CURRENT_PROJECT` protects the conversational execution boundary before tools are used; the repository declaration controls governed workflow behaviour after the project-boundary preflight has passed.

## Single-maintainer projects

A repository with one maintainer does not need to invent a second GitHub identity merely to obtain fresh review. Promptbook treats independence as a property of the reviewing context and evidence boundary. A fresh chat/session that independently reconstructs the candidate may still use the same maintainer account that authored the PR.

When ordinary `/review` write-back is active and GitHub cannot record a formal self-`APPROVE` or self-`REQUEST_CHANGES`, record the exact disposition and rationale through a permitted `COMMENT` review or durable repository-local comment when the Promptbook single-maintainer preconditions hold. That fallback is not a formal platform approval and must not bypass branch protection or repository policy that genuinely requires a distinct reviewer or approval status. When `/review --read-only` or an equivalent zero-write instruction is active, do not create the fallback record.

After a fresh reviewer applies a bounded remediation, that context has become an authoring context for the changed candidate and cannot independently re-review its own change. Use another genuinely fresh context for the next independence-required gate; in a single-maintainer project that fresh context may still operate through the same GitHub account.

Repositories with stronger separation-of-duties requirements should state them explicitly in `AGENTS.md` or other repository-local policy. Those requirements take precedence over this solo-maintainer default.

## Shorthand commands

The canonical command semantics live in [`prompts/workflows/README.md`](../prompts/workflows/README.md). The small public vocabulary is:

- `/go [target]` — continue the governed objective through the router; when the target is already clear, `/go` alone means perform the next authorised, safely decidable action rather than merely describe the next gate.
- `/review [target]` — request a substantive fresh review as the current deliverable. For a GitHub pull request, record the requested review on GitHub by default; use `/review --read-only [target]` or an unambiguous natural-language zero-write qualifier to report only in chat. Review recording does not grant merge, remediation, release, deployment, settings, credential, production, or other unrelated authority.
- `/plan [target]` — plan bounded work using the Promptbook planning prompt.
- `/implement [target]` — implement already-approved bounded work using the Promptbook implementation prompt.
- `/fix [target]` — remediate current bounded review findings using existing authority.
- `/handoff [target]` — produce the shortest safe continuation handoff without executing the handed-off task.
- `/status [target]` — reconstruct and report authoritative current state read-only; do not mutate unless the user separately requests continuation.

Commands are intentionally not a mini CLI. The explicit `/review --read-only` modifier exists because it changes the write-back boundary; otherwise add natural-language qualifiers when needed, for example:

```text
/go until the next genuinely fresh review boundary
/status issue #42
/review PR #17
/review --read-only PR #17
```

If the target is omitted, resolve it from the current conversation and authoritative repository state. If that is not safely possible, fail closed rather than guessing.

## Direct prompt escape hatch

The router is the default for ordinary continuation. A caller may still explicitly name an individual Promptbook prompt when that exact standalone deliverable is wanted. Explicit prompt selection does not weaken repository-local precedence or create authority that the task does not already have. In particular, selecting the standalone analytical pull-request review prompt does not implicitly select router `/review` write-back behaviour.

## Updating the dependency

When a repository pins a Promptbook release, update the pin through an ordinary reviewed repository change. This keeps Promptbook functioning like a workflow dependency rather than copied configuration. The consumer repository should not need to change merely because Promptbook adds unrelated prompts; update when the newer Promptbook contract is intentionally adopted.
