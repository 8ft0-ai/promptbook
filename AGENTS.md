# Agent instructions

## Repository purpose

Promptbook is a curated public collection of reusable prompts and workflows for disciplined, evidence-driven agentic engineering. Keep changes public-safe, model-portable, task-oriented, and smaller than the private or project-specific histories from which reusable patterns may have emerged.

Do not publish credentials, private identifiers, hidden provenance, organisation-specific assumptions, or internal history that is not required to use the public prompt or workflow.

## Governing workflow

Before mutating the repository, inspect the current issue or task, repository state, relevant discussion, and validation requirements. Repository-local instructions and explicit task authority take precedence over reusable Promptbook guidance.

For governed continuation, use [`prompts/workflows/README.md`](prompts/workflows/README.md) as the workflow entry point. Continue routine authorised work without unnecessary human confirmation, but do not invent mutation, merge, release, credential, scope, or production authority.

Preserve genuine fresh-review boundaries. A context that authored or materially shaped a candidate must not present its own review as fresh independent evidence when independence is required.

Prefer the minimum safe change. Do not broaden a bounded issue with unrelated cleanup, taxonomy changes, new commands, or maturity changes unless separately authorised.

## Validation

Run the repository validation required by CI for every public-interface change. Do not weaken tests, assertions, public-safety checks, link validation, or command/bootstrap drift checks merely to make a candidate pass.

When behaviour changes, add or update regression coverage that would fail if the intended contract regressed.

## Public interface maintenance

The current public shorthand vocabulary is:

`/go`, `/review`, `/plan`, `/implement`, `/fix`, `/handoff`, `/status`.

`prompts/workflows/README.md` is canonical for command semantics. The root `README.md` is the quick-start/discovery surface, `guides/project-bootstrap.md` is the setup surface, and `BOOTSTRAP` is the copyable project-bootstrap text.

When the shorthand vocabulary or bootstrap contract changes, update all affected public surfaces in the same change and update regression coverage so CI fails on accidental drift. Keep the command set aligned across the router, README, bootstrap guide, and this maintenance declaration. Keep `BOOTSTRAP` aligned with the copyable project-bootstrap block in the guide.

Do not copy full Promptbook prompt bodies into this file, README, or consumer-repository instructions. Link to the canonical prompt or workflow instead.

## Delivery discipline

Keep issue-to-change traceability explicit. Before merge, inspect the complete diff, verify scope against the governing issue, ensure required checks pass on the exact candidate, and confirm no unresolved blocking review state remains.

After merge, verify the resulting `main` state and required post-merge validation before closing the governed objective.
