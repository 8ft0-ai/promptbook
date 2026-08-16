# Using Promptbook

Promptbook supports four simple usage modes: copy, adapt, compose, and bootstrap.

## Copy and use

Choose the prompt closest to your task, copy its **Prompt** section, and replace every declared placeholder with real context. Do not remove evidence, validation, authority, or stop requirements merely to make the prompt shorter unless they are genuinely irrelevant to your task.

A prompt cannot provide capabilities the receiving assistant does not have. Repository review still requires repository access; implementation still requires an authorised write path; a fresh independent review still requires a context that has not inherited the earlier conclusion.

## Adapt

Adapt tool names, repository conventions, terminology, and output format freely. Preserve the behavioural invariants that make the prompt safe and useful: inspect current evidence, keep scope bounded, make assumptions explicit, validate results, and stop rather than invent missing authority or facts.

See [Adapting prompts](adapting-prompts.md) for a more detailed checklist.

## Compose

Composition works best when prompts have different responsibilities. For example, use an implementation-planning prompt first and a fresh-review prompt later. Avoid concatenating several large prompts that each try to control the entire lifecycle; overlapping authority and stop rules can become contradictory.

When guidance conflicts, apply this precedence:

1. platform and safety constraints;
2. explicit user/task authority;
3. repository-local instructions and policies;
4. the task-specific prompt;
5. generic Promptbook guidance.

If the conflict changes what is authorised or materially changes the intended outcome, resolve it explicitly rather than silently choosing the most convenient instruction.

## Bootstrap repeated project use

For project chats or other persistent workspaces, do not copy Promptbook prompt bodies into project instructions. Use a thin bootstrap that points the agent at repository-local instructions and the Promptbook workflow router, and let the repository declare any Promptbook version/pin. The router owns the public shorthand command vocabulary such as `/go`, `/review`, `/fix`, and `/status`.

See [Project bootstrap and shorthand commands](project-bootstrap.md) for copyable bootstrap text, an `AGENTS.md` declaration pattern, command semantics, and versioning guidance.

When the router reaches a genuine human choice, use the [decision capsule](decision-capsules.md) interaction rather than copying repository identifiers into an approval sentence. Recommendation-first choices and semantic `ACCEPT`, `REJECT`, `CHOOSE`, and `CHANGE` intents are designed to work consistently across keyboard, touch and voice while preserving bounded authority.
