# Adapting prompts

Promptbook prompts are starting contracts, not magic strings. Adapt them to your repository, toolset, and risk level while preserving the parts that carry decision value.

## Safe things to change

You can normally change:

- tool and platform names;
- branch, issue, or review conventions;
- terminology and output formatting;
- the amount of explanation requested;
- validation commands and evidence sources;
- whether a task records its result in an issue, PR, document, or only the current conversation.

## Things to preserve deliberately

Before removing a requirement, ask what failure it prevents. Common high-value invariants are:

- reconstruct current state instead of trusting a stale summary;
- distinguish observed evidence from inference;
- keep the intended scope and non-goals visible;
- prefer the smallest sufficient change;
- validate the exact candidate that will be used or merged;
- preserve failed and negative evidence;
- stop on missing authority or material ambiguity instead of inventing an answer;
- separate fresh review from author-side reasoning when independence matters.

## Placeholders

Use explicit uppercase placeholders such as `<ISSUE_OR_TASK>` or `<REVIEW_TARGET>`. Every placeholder used in the Prompt section must be explained in the Inputs section so a reader does not need hidden context.

## When to split a prompt

Split a prompt when two parts need materially different authority, evidence, or independence. Planning and implementation can be separate because implementation mutates state; author-side implementation and fresh substantive review can be separate because the latter requires independence.
