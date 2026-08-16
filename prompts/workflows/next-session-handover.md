# Next-session handover

## Purpose

Produce a compact, executable prompt that lets another chat or agent continue the current work without reconstructing unnecessary history.

## When to use

Use at a real context or capability boundary: fresh review, a new chat/session, a different agent, or an external execution environment.

## Prompt

```text
Create the shortest safe handover prompt for continuing <CURRENT_WORK> in a new context.

Preserve only information that materially affects the next decision or action. Include:
- repository/system and governing issue/task identity;
- exact current revision/head/base or other immutable identity when decision-critical;
- the next bounded objective;
- current authority and scope;
- required evidence the new context must reconstruct or verify;
- explicit prohibitions and stop conditions that still matter;
- exact validation/evidence expected from the next step;
- whether the new context must be genuinely fresh and, if so, what prior-information boundary must be preserved;
- continuation semantics after success.

Remove duplicated historical narrative, superseded identities, old run details that do not affect the next decision, and conclusions the fresh context must independently determine.

The resulting handover must be directly copyable as the next prompt. Do not require the recipient to ask what to do next or search the previous conversation for missing instructions.
```

## Inputs

- `<CURRENT_WORK>` — the present task state, including the next real boundary and any decision-critical identities.

## What it does

Turns a long working session into a minimal continuation contract while preserving the evidence and authority needed to avoid unsafe guessing.

## Boundaries / limitations

Do not use handover compression to omit active blockers, required authority, security boundaries, or identities that the next decision genuinely depends on.

## Status

`tested`
