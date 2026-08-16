# Project bootstrap and shorthand commands

Use this pattern when a project or repository should use Promptbook repeatedly across chat sessions without copying Promptbook prompt bodies into local instructions.

The intended layering is:

```text
project/workspace bootstrap
        ↓
repository-local authority
        ↓
Promptbook workflow router and task prompts
```

The bootstrap tells the agent where to start. Repository instructions remain authoritative for local scope and policy. Promptbook owns reusable workflow behaviour and shorthand semantics.

## Project bootstrap

Keep persistent project or workspace instructions thin. A suitable bootstrap is:

```text
For governed engineering work, first read and apply repository-local instructions, including AGENTS.md when present.

Unless repository-local instructions specify another supported workflow, use `8ft0-ai/promptbook` → `prompts/workflows/README.md` as the governed-workflow entry point, using any Promptbook version/ref declared by the repository.

Reconstruct decision-critical current state from authoritative sources rather than stale conversation summaries. Preserve platform safety constraints, explicit task authority, repository-local policy, validation requirements and current evidence above Promptbook guidance.

Continue with minimal unnecessary human intervention until `EXTERNAL_REQUIRED`, `DECISION_REQUIRED`, `BLOCKED`, or `COMPLETE` applies. Interpret Promptbook shorthand commands according to the workflow router. The bootstrap and commands select workflow intent only: they do not grant additional authority or bypass freshness, independence, validation or fail-closed behaviour.
```

This text deliberately does not duplicate lifecycle procedures or individual prompt bodies. Those remain versioned in Promptbook.

## Repository declaration

For reproducible use, declare the Promptbook dependency in repository-local instructions. For example, an `AGENTS.md` can include:

```md
## Promptbook

This repository uses `8ft0-ai/promptbook@vX.Y.Z` for reusable governed-workflow guidance.

Workflow entry point: `prompts/workflows/README.md`.

Repository-local instructions, explicit task authority, security policy and validation requirements take precedence over Promptbook. Promptbook and its shorthand commands do not grant additional authority.

Use the shorthand commands defined by the pinned Promptbook workflow router; do not copy their implementation into this repository.
```

Pinning a stable release makes the workflow dependency reproducible and reviewable. A repository may deliberately track `main` instead, but that opts into behaviour changes as Promptbook evolves. Keep the project-level bootstrap version-neutral and let the repository own the pin or override.

## Shorthand commands

The canonical command semantics live in [`prompts/workflows/README.md`](../prompts/workflows/README.md). The small public vocabulary is:

- `/go [target]` — continue the governed objective through the router; when the target is already clear, `/go` alone means perform the next authorised, safely decidable action rather than merely describe the next gate.
- `/review [target]` — request a substantive fresh review as the current deliverable, preserving the fresh-context boundary.
- `/plan [target]` — plan bounded work using the Promptbook planning prompt.
- `/implement [target]` — implement already-approved bounded work using the Promptbook implementation prompt.
- `/fix [target]` — remediate current bounded review findings using existing authority.
- `/handoff [target]` — produce the shortest safe continuation handoff without executing the handed-off task.
- `/status [target]` — reconstruct and report authoritative current state read-only; do not mutate unless the user separately requests continuation.

Commands are intentionally not a mini CLI. Add natural-language qualifiers when needed, for example:

```text
/go until the next genuinely fresh review boundary
/status issue #42
/review PR #17
```

If the target is omitted, resolve it from the current conversation and authoritative repository state. If that is not safely possible, fail closed rather than guessing.

## Direct prompt escape hatch

The router is the default for ordinary continuation. A caller may still explicitly name an individual Promptbook prompt when that exact standalone deliverable is wanted. Explicit prompt selection does not weaken repository-local precedence or create authority that the task does not already have.

## Updating the dependency

When a repository pins a Promptbook release, update the pin through an ordinary reviewed repository change. This keeps Promptbook functioning like a workflow dependency rather than copied configuration. The consumer repository should not need to change merely because Promptbook adds unrelated prompts; update when the newer Promptbook contract is intentionally adopted.
