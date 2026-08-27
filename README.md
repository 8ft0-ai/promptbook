# Promptbook

A curated collection of practical prompts and workflows for reliable, evidence-driven agentic engineering.

Promptbook is for engineers and technical practitioners who want AI assistants to do useful work with clear evidence, bounded authority, explicit failure behaviour, and less unnecessary human orchestration. It is intentionally small and curated rather than a dump of every prompt that might be useful.

## Start here

| Task | Prompt |
| --- | --- |
| Turn an issue into an implementation plan | [Plan an issue](prompts/engineering/plan-an-issue.md) |
| Review a pull request substantively | [Review a pull request](prompts/engineering/pr-review.md) |
| Continue governed work or determine the next workflow | [Workflow router](prompts/workflows/README.md) |
| Respond quickly to a genuine human decision | [Decision capsules](guides/decision-capsules.md) |
| Set up recurring project-chat invocation | [Project bootstrap and shorthand commands](guides/project-bootstrap.md) |
| Re-review work from a fresh context | [Fresh independent review](prompts/workflows/fresh-independent-review.md) |

Browse the complete collection in [`prompts/`](prompts/README.md).

## Quick commands

Once Promptbook is configured for a project, common workflow intents can be invoked with:

| Command | Intent |
| --- | --- |
| `/go [target]` | Continue governed work as far as safely possible |
| `/review [target]` | Review a pull request and record the requested GitHub review by default |
| `/plan [target]` | Plan bounded work |
| `/implement [target]` | Implement already-approved bounded work |
| `/fix [target]` | Remediate bounded review findings |
| `/handoff [target]` | Produce a continuation handoff without executing it |
| `/status [target]` | Reconstruct and report authoritative current state, read-only |

Examples:

```text
/go issue #42
/review PR #43
/review --read-only PR #43
/fix
/status
```

Commands are shorthand intent selectors with only the narrow authority intrinsic to the operation defined by the workflow router. For a GitHub pull request, ordinary `/review` includes the bounded write needed to record the requested review; `/review --read-only` or an unambiguous natural-language zero-write qualifier reports only in chat. Commands do not grant unrelated authority or bypass repository-local instructions, validation, security controls, freshness, or independent-review requirements. See [Project bootstrap and shorthand commands](guides/project-bootstrap.md) for setup and the [Workflow router](prompts/workflows/README.md) for canonical command semantics.

## Decision capsules

When Promptbook genuinely needs a human judgement or authority decision, it presents the recommendation and choices first instead of making you copy an approval phrase or repository identifier:

```text
DECISION_REQUIRED — Deployment mechanism

Recommended: A

A — GitHub Actions + Workload Identity
B — Cloud Build
C — Defer
```

You can answer naturally with `A`, `Choose A`, `accept`, `go ahead`, or another clear equivalent when there is exactly one unambiguous pending decision. The stable protocol is semantic `ACCEPT`, `REJECT`, `CHOOSE`, and `CHANGE` intent, so the same interaction works from keyboard, touch, or voice. See [Decision capsules](guides/decision-capsules.md) for binding, ambiguity, stale-proposal, and continuation rules.

## How to use Promptbook

1. Open a prompt that matches the task you want to perform, or start from the [workflow router](prompts/workflows/README.md) when the next governed workflow should be selected from current state.
2. Copy the text in its **Prompt** section when using an individual prompt, or follow the router invocation when using the workflow entrypoint.
3. Replace the declared `<PLACEHOLDERS>` with your actual context where applicable.
4. Give the prompt to the AI assistant or agent that has the capabilities needed for the task.
5. Keep repository-local instructions, platform safety rules, and explicit task authority above generic Promptbook guidance.

For repeated use across project chat sessions, use the [project bootstrap pattern](guides/project-bootstrap.md) so persistent project instructions stay thin while repository-local instructions own the Promptbook version/pin and the workflow router owns shorthand command behaviour.

See [Using Promptbook](guides/using-promptbook.md) for copy, adaptation, and composition patterns.

## What makes these prompts different?

Promptbook prompts are designed around engineering behaviour rather than persona wording. They tend to make evidence, scope, validation, authority, negative paths, and stop conditions explicit. They also try to distinguish routine engineering judgement from decisions that genuinely require a human.

The prompts are model-portable by default. A prompt may still require tools such as repository access, CI visibility, or file editing when the task itself requires them.

## Status labels

Every prompt has one maturity label:

- **experimental** — a useful pattern with limited real-task evidence;
- **tested** — exercised successfully on real tasks, with known limitations;
- **stable** — repeatedly useful and intentionally maintained as a reusable interface.

Status describes the evidence behind the Promptbook prompt. It is not a claim of universal model quality or best practice.

## Guides

- [Using Promptbook](guides/using-promptbook.md)
- [Project bootstrap and shorthand commands](guides/project-bootstrap.md)
- [Decision capsules](guides/decision-capsules.md)
- [Adapting prompts](guides/adapting-prompts.md)
- [Design principles](guides/design-principles.md)

## Contributing

Contributions are welcome. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and start from the [prompt template](templates/prompt-template.md). New prompts should solve a concrete reusable task, be self-contained, and avoid private or organisation-specific identifiers.

## Licence

Promptbook is licensed under the [Apache License 2.0](LICENSE).
