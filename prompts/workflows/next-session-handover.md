# Next-session handover

## Purpose

Produce a compact, executable prompt or external-action handoff that lets another chat, agent, or human-operated environment continue the current work without reconstructing unnecessary history.

## When to use

Use at a real context or capability boundary: fresh review, a new chat/session, a different agent, or an external execution environment.

## Prompt

```text
Create the shortest safe handover for continuing <CURRENT_WORK> in the required receiving context.

First distinguish the handover type:
- for a fresh review, new chat/session, or another agent context, produce a directly copyable next prompt;
- for human-operated external execution, provide the concrete action the human must perform now, not merely a description of the capability or context that is needed.

Preserve only information that materially affects the next decision or action. Include:
- repository/system and governing issue/task identity;
- exact current revision/head/base or other immutable identity when decision-critical;
- the next bounded objective;
- current authority and scope;
- required evidence the receiving context must reconstruct or verify;
- explicit prohibitions and stop conditions that still matter;
- exact validation/evidence expected from the next step;
- whether the new context must be genuinely fresh and, if so, what prior-information boundary must be preserved;
- continuation semantics after success.

For human-operated external execution, also include:
- the smallest complete copy/paste script or exact commands when command-line execution is appropriate, otherwise exact browser/UI steps or another concrete step-by-step procedure;
- all material prerequisites, immutable identities, guards, fail-closed checks, cleanup/revocation/restore actions, and prohibited actions needed to execute safely;
- the exact output/evidence the human must return for governed continuation;
- no secret values, truncated scripts, omitted command tails, or placeholders whose values are already known from authoritative state.

Do not require the human to ask how to perform the external action. Do not turn an already-authorised capability transfer into a new decision request. If the required external procedure cannot be determined safely and completely, report the real blocker or decision instead of presenting a vague EXTERNAL_REQUIRED handoff.

If an equivalent valid external handoff already exists and decision-critical state has not materially changed, reuse it after refreshing any guards that can become stale rather than repeating capability discovery.

Remove duplicated historical narrative, superseded identities, old run details that do not affect the next decision, and conclusions a genuinely fresh context must independently determine.

For a fresh-context handoff, the result must be directly copyable as the next prompt. For human-operated external execution, the result must be directly executable as the required action. Neither form may require the recipient to search the previous conversation for missing instructions.
```

## Inputs

- `<CURRENT_WORK>` — the present task state, including the next real boundary and any decision-critical identities.

## What it does

Turns a long working session into a minimal continuation contract while preserving the evidence and authority needed to avoid unsafe guessing. It distinguishes a fresh-context prompt handoff from a human-operated external execution handoff so capability boundaries expose the exact action to perform rather than only naming the receiving environment.

## Boundaries / limitations

Do not use handover compression to omit active blockers, required authority, security boundaries, or identities that the next decision genuinely depends on. Do not expose credentials or secret values, and do not manufacture a command sequence when the safe external procedure is not sufficiently determined.

## Status

`tested`
