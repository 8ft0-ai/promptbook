# Next-session handover

## Purpose

Produce a compact, executable prompt or external-action handoff that lets another chat, agent, or human-operated environment continue the current work without reconstructing unnecessary history.

## When to use

Use at a real context or capability boundary: fresh review when no eligible isolated review context can be established automatically, a new chat/session, a different agent, or an external execution environment.

## Prompt

```text
Create the shortest safe handover for continuing <CURRENT_WORK> in the required receiving context.

First distinguish the handover type:
- for a fresh review, new chat/session, or another agent context, use this handover only after the governing workflow has resolved that no eligible/provable isolated fresh-review context can satisfy the boundary automatically, or when a handover itself is explicitly the requested deliverable; then prefer an existing public shorthand invocation when a durable target is sufficient for the receiving context to reconstruct all decision-critical current state and authority; otherwise produce the shortest directly copyable prompt that carries only the information that cannot safely be reconstructed;
- for human-operated external execution, provide the concrete action the human must perform now, not merely a description of the capability or context that is needed.

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

For a fresh-context handoff, the result must be directly copyable as the next prompt or minimal shorthand invocation. For human-operated external execution, the result must be directly executable as the required action. Neither form may require the recipient to search the previous conversation for missing instructions.
```

## Inputs

- `<CURRENT_WORK>` — the present task state, including the next real boundary and any decision-critical identities.

## What it does

Turns a long working session into a minimal continuation contract while preserving the evidence and authority needed to avoid unsafe guessing. For fresh review, it is the manual fallback after the governing workflow cannot establish a provably isolated review context automatically; when the fallback is needed, it prefers a reconstructible public shorthand invocation when durable sources already contain the needed state and retains a fuller handover only when reconstruction would be insufficient. It separately preserves complete human-operated external execution handoffs so capability boundaries expose the exact action to perform rather than only naming the receiving environment. For complex command-line execution, the operational-artifact contract materialises execution state and coupled guards while retaining the atomic-inline exception.

## Boundaries / limitations

Do not use handover compression to omit active blockers, required authority, security boundaries, or identities that the next decision genuinely depends on. A shorthand invocation is navigation, never authority. Manual fresh-context handover remains fail closed when automatic isolation is unavailable or unprovable; the handover itself does not make a receiving context fresh unless that context actually satisfies the fresh-review information boundary. Do not expose credentials or secret values, do not manufacture a command sequence when the safe external procedure is not sufficiently determined, and never substitute a slash command for a complete executable external action when human-operated execution is the actual boundary. Artifact delivery never creates authority, and unavailable file delivery must not be answered with a large fragile transcript-dependent executable block.

## Status

`tested`
