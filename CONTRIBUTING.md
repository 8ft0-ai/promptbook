# Contributing to Promptbook

Promptbook is a curated collection. A smaller set of prompts that solve real tasks clearly is more useful than a large catalogue of lightly tested prompt text.

## What makes a good contribution?

A new prompt should:

- solve a concrete, reusable task;
- be understandable without private conversational history;
- make required inputs explicit;
- keep the copy/paste prompt usable on its own;
- state material boundaries and limitations;
- avoid private data, credentials, internal URLs, repository-specific IDs, and organisation-specific assumptions unless the prompt explicitly targets that public system;
- avoid unsupported claims such as “best practice”, “guaranteed”, or universal model portability;
- stay as small as the intended behaviour permits;
- include a concise example or evidence of use where practical.

Use [`templates/prompt-template.md`](templates/prompt-template.md) as the starting shape.

## Required prompt sections

Published prompts must contain these headings in order:

1. `Purpose`
2. `When to use`
3. `Prompt`
4. `Inputs`
5. `What it does`
6. `Boundaries / limitations`
7. `Status`

Allowed status values are `experimental`, `tested`, and `stable`. See the root README for their meaning.

## Pull requests

Keep each pull request coherent and reviewable. Explain the reusable problem, why the prompt is needed, what evidence supports its status, and any important limitations. Prompt changes should preserve user-facing behaviour unless the PR intentionally changes it.

Run before opening a PR:

```bash
python scripts/validate_promptbook.py
python -m unittest discover -s tests -p 'test_*.py' -v
```

Normal PR validation runs the same checks automatically.

## Improving an existing prompt

Prefer fixing the smallest concrete problem. If a change materially alters the task, authority model, required inputs, or expected behaviour, explain that interface change rather than presenting it as wording cleanup.
