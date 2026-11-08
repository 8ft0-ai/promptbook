# Router Terminal Handover

**Conditional contract:** Load for genuine external execution/fresh-review handoff or a manual terminal continuation.

## Next-invocation guidance

When a requested workflow intentionally stops while a broader governed objective remains active, append the **smallest safely determined next invocation** after the workflow result. That invocation is navigation metadata only: it identifies how another context can resume from authoritative state, does not execute continuation in the current context, and does not grant approval, mutation, merge, implementation, execution, credential, production, or other authority. The receiving context must reconstruct the decision-critical current state and authority before acting.

Use `Next chat:` for a genuinely fresh-review boundary only when no eligible/provable isolated review context can be established automatically, or when a handover itself is explicitly the requested deliverable. When the exact review target is durably identifiable and sufficient for reconstruction, the manual fallback may be only:

```text
EXTERNAL_REQUIRED — fresh context required

Next chat:
  /review <exact review target>
```

Opening a fresh context is different from human-operated external execution. A shorthand invocation may satisfy the former when durable authoritative sources contain the needed state; it must never replace the complete commands, browser/UI procedure, guards, cleanup/prohibitions, and evidence-to-return required for the latter. An automatically delegated reviewer and a manually opened reviewer are subject to the same fresh-review completeness, exact-candidate, write-back/read-only and repository-policy rules.

When a bounded review was explicitly requested as the final deliverable, an appended `Next:` line does not violate that stop boundary or continue the workflow in the current context. If the review is `APPROVED` and the broader objective remains active, prefer the governing lifecycle object rather than the reviewed intermediate artefact when it lets the receiving context reconstruct the complete lifecycle:

```text
APPROVED

Next:
  /go <governing objective>
```

For `CHANGES REQUIRED`, suggest `/fix <target>` only when the governing contract and existing authority already make bounded remediation the safely determined next path. Do not use a convenience command to manufacture remediation authority.

Fail closed when the next invocation is not safely determined. `DECISION_REQUIRED` keeps the decision capsule and must not be bypassed by a slash command. `BLOCKED` must not manufacture `/go`, `/fix`, or `/review` merely to provide a next step. `COMPLETE` must state that no further action is required rather than inventing continuation.
