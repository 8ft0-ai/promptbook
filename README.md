# Promptbook

A curated collection of practical prompts and workflows for reliable, evidence-driven agentic engineering.

Promptbook is for engineers and technical practitioners who want AI assistants to do useful work with clear evidence, bounded authority, explicit failure behaviour, and less unnecessary human orchestration. It is intentionally small and curated rather than a dump of every prompt that might be useful.

## Start here

| Task | Prompt |
| --- | --- |
| Turn an issue into an implementation plan | [Plan an issue](prompts/engineering/plan-an-issue.md) |
| Review a pull request substantively | [Review a pull request](prompts/engineering/pr-review.md) |
| Continue governed work with minimal intervention | [Autonomous progression](prompts/workflows/autonomous-progression.md) |
| Re-review work from a fresh context | [Fresh independent review](prompts/workflows/fresh-independent-review.md) |

Browse the complete collection in [`prompts/`](prompts/README.md).

## How to use Promptbook

1. Open a prompt that matches the task you want to perform.
2. Copy the text in its **Prompt** section.
3. Replace the declared `<PLACEHOLDERS>` with your actual context.
4. Give the prompt to the AI assistant or agent that has the capabilities needed for the task.
5. Keep repository-local instructions, platform safety rules, and explicit task authority above generic Promptbook guidance.

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
- [Adapting prompts](guides/adapting-prompts.md)
- [Design principles](guides/design-principles.md)

## Contributing

Contributions are welcome. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and start from the [prompt template](templates/prompt-template.md). New prompts should solve a concrete reusable task, be self-contained, and avoid private or organisation-specific identifiers.

## Licence

Promptbook is licensed under the [Apache License 2.0](LICENSE).
