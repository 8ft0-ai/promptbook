# Next-session handover

## Purpose

Produce either a compact context-transfer prompt artefact for another reasoning context or a complete human-operated external-action handoff, without making the conversation transcript itself executable state.

## When to use

Use when `/prompt` or a compatibility handoff intent requests a context-transfer artefact, when fresh review requires a manual new-context fallback because no eligible isolated review context can be established automatically, or when an authorised action genuinely requires human-operated external execution.

## Prompt

```text
Create the shortest safe transfer artefact for <CURRENT_WORK>.

First distinguish the transfer type:

- `CONTINUATION_PROMPT` — generate a prompt intended for another reasoning context to take over the governed objective. Prefer a minimal durable target or public shorthand invocation when the receiver can reconstruct current authority/state safely. Generating this prompt does not end the current context, transfer authority, or change lifecycle state.
- `DELEGATION_PROMPT` — generate a prompt for another reasoning context to perform one bounded question/task and return a result here. State the bounded objective, allowed/prohibited effects, what must be reconstructed, stop conditions, and a return contract. Generating the prompt does not create or invoke the delegate and does not grant it authority.
- `INDEPENDENT_PROMPT` — generate a prompt intended for genuinely independent adjudication, normally fresh substantive review. Transfer only safe reconstruction/navigation information; exclude author-side substantive adjudication, expected conclusion, proposed fix, or private reasoning. Generating the prompt does not establish freshness or independence; the eventual receiving context must separately satisfy the fresh-review eligibility contract.
- human-operated external execution — provide the concrete action the human must perform now, not merely a description of the capability or context that is needed.

For an unqualified `/prompt`, infer the receiving contract only when current state and user intent make it unambiguous. Otherwise expose the smallest real ambiguity instead of inventing a flag grammar or silently choosing the wrong transfer semantics.

For a delegated prompt, a default return contract should be logically equivalent to:

```text
Return:
- conclusion;
- material evidence;
- unresolved uncertainty;
- exact identities examined where decision-critical;
- no continuation of the parent objective.
```

A prompt artefact is navigation/instruction text only. The parent governed state remains unchanged until some separately authorised receiving context actually performs work and returns evidence.

For a fresh-context boundary, automatic resolution and manual handover are distinct from execution locality. Do not probe `connected/native`, `hosted/hermetic`, or owner-local execution classes merely to satisfy reasoning independence. Instead, the governing workflow first determines whether a genuinely isolated review context can be established under the fresh-review and resolved-run-context contracts. If it can, no human context handover is required. If it cannot, or isolation cannot be proved, the existing manual handover remains the fail-closed fallback.

For that manual fresh-context fallback, a minimal result may be a `Next chat:` invocation such as `/review` with the exact durable review target. Keep the genuine freshness boundary explicit. A shorthand invocation is navigation only: it does not grant approval, mutation, merge, implementation, execution, credential, production, or other authority, and the receiving context must refresh authoritative state before acting.

Preserve only information that materially affects the next decision or action. Include information in a full handover only when it cannot be safely reconstructed from the durable target, such as:
- repository/system and governing issue/task identity;
- exact current revision/head/base or other immutable identity when decision-critical;
- the next bounded objective;
- current authority and scope;
- required evidence the receiving context must reconstruct or verify;
- explicit prohibitions and stop conditions that still matter;
- exact validation/evidence expected from the next step;
- whether the new context must be genuinely fresh and, if so, what prior-information boundary must be preserved;
- continuation semantics after success.

Do not include author-side substantive conclusions, proposed review disposition, private reasoning, or hidden conversational state merely to make a fresh-review handover more informative. Shared authoritative repository rules, governing work items and durable candidate/evidence identities remain valid navigation because the receiving reviewer must reconstruct and adjudicate them independently.

For human-operated external execution, also include:
- the smallest complete copy/paste script or exact commands when command-line execution is appropriate, otherwise exact browser/UI steps or another concrete step-by-step procedure;
- all material prerequisites, immutable identities, guards, fail-closed checks, cleanup/revocation/restore actions, and prohibited actions needed to execute safely;
- the exact output/evidence the human must return for governed continuation;
- no secret values, truncated scripts, omitted command tails, or placeholders whose values are already known from authoritative state.

For human-operated command-line execution, apply [Operational artifact hand-off](operational-artifact-handoff.md). Keep a genuinely atomic, transcript-independent command inline. When execution fragility, guard coupling, or evidence complexity is material, hand off a materialised/downloadable artifact plus simple staging/invocation instructions and bounded `RESULT` / `EVIDENCE` output rather than using the conversation transcript as executable state. The artifact must preserve the governing read-only or mutation authority exactly, handle its target/working directory explicitly, and fail closed on material identity, prerequisite, integrity, collision, or authority guard failure. If downloadable-file delivery is unavailable, use only the contract's safe degraded paths; do not silently replace the artifact with a large fragile transcript program.

Do not let a shorthand next invocation replace a required human-operated external procedure. Do not require the human to ask how to perform the external action. Do not turn an already-authorised capability transfer into a new decision request. If the required external procedure cannot be determined safely and completely, report the real blocker or decision instead of presenting a vague EXTERNAL_REQUIRED handoff.

If an equivalent valid external handoff already exists and decision-critical state has not materially changed, reuse it after refreshing any guards that can become stale rather than repeating capability discovery. For a fresh-review handoff, do not repeatedly create equivalent failed automatic review contexts when the target, isolation evidence and bounded review capability state have not changed.

Remove duplicated historical narrative, superseded identities, old run details that do not affect the next decision, and conclusions a genuinely fresh context must independently determine. Prefer authoritative-state reconstruction over copying a large handover payload when durable sources make that safe.

For a context-transfer request, the result must be directly copyable as the receiving prompt or minimal shorthand invocation. For human-operated external execution, the result must be directly executable as the required action. Neither form may require the recipient to search the previous conversation for missing instructions.
```

## Inputs

- `<CURRENT_WORK>` — the present task state, including the next real boundary and any decision-critical identities.

## What it does

Generates minimal context-transfer artefacts for continuation, bounded delegation, or intended independent adjudication without changing the parent lifecycle merely by generating text. For fresh review, a manual continuation/independent prompt remains the fallback after the governing workflow cannot establish a provably isolated review context automatically; generating an independent prompt never proves freshness. The workflow separately preserves complete human-operated external execution handoffs so capability boundaries expose the exact action to perform rather than only naming the receiving environment. For complex command-line execution, the operational-artifact contract materialises execution state and coupled guards while retaining the atomic-inline exception.

## Boundaries / limitations

Do not use prompt/handover compression to omit active blockers, required authority, security boundaries, or identities that the next decision genuinely depends on. A shorthand invocation or generated prompt is navigation/instruction text, never authority. Prompt generation does not create another context, establish delegated capability, or alter parent lifecycle state. Manual fresh-context handover remains fail closed when automatic isolation is unavailable or unprovable; the generated prompt itself does not make a receiving context fresh unless that context actually satisfies the fresh-review information boundary. Do not expose credentials or secret values, do not manufacture a command sequence when the safe external procedure is not sufficiently determined, and never substitute a slash command for a complete executable external action when human-operated execution is the actual boundary. Artifact delivery never creates authority, and unavailable file delivery must not be answered with a large fragile transcript-dependent executable block.

## Status

`tested`
