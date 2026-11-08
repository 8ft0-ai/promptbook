# Router Special Routing

**Conditional contract:** Load for non-ordinary workflow routes, mandatory architecture or stateful analysis, non-fresh review or conflicting route evidence.

## Routing

Before routing, inspect the current conversation and the authoritative repository or task state needed for the next decision. Stale summaries are navigation aids, not authority. Select exactly one primary workflow and apply it immediately; routing itself is not a stop point.

Use the first matching case:

1. **A context-transfer prompt is explicitly the requested deliverable** → [Next-session handover](../../prompts/workflows/next-session-handover.md).
   - Generate only the requested context-transfer artefact. Select a continuation, delegation, or independent-review receiving contract from user intent and current state when unambiguous.
   - Generating the artefact does not create the receiving context, transfer authority, establish independence/freshness, or change the current lifecycle state.
   - Do not use this route to replace a complete human-operated `EXTERNAL_REQUIRED` execution handoff.

2. **Mandatory architecture/stateful analysis is required now**.
   - If materially high-risk architecture is intended to carry a strong closed-world / architecture-closed / closure-ready completeness claim and no current independently derived closure artefact covers the governing contract and architecture scope → [Architecture closure analysis](../../prompts/workflows/architecture-closure-analysis.md) before closure-ready candidate authoring/publication. Treat this as the proactive publication gate, not as repeated-review escalation or architecture reconsideration. If the current task does not provide the bounded read-only investigation/analysis authority needed to derive that artefact, surface `DECISION_REQUIRED`.
   - If current evidence establishes `CLOSURE_METHOD_FALSIFIED`, route the current strong-closure generation to `GOVERNING_DISPOSITION_REQUIRED`. Only if a separate governing disposition has explicitly authorised `AUTHORISE_NEW_STRONG_CLOSURE_GENERATION` may a new generation enter [Architecture closure analysis](../../prompts/workflows/architecture-closure-analysis.md); bind that successor to terminal predecessor evidence and new exact generation identity. Without that disposition, do not re-enter closure analysis.
   - Otherwise select [Stateful invariant analysis](../../prompts/workflows/stateful-invariant-analysis.md) when the repeated-review escalation trigger is established and no current candidate-bound analysis satisfies it.
   - Also select stateful/invariant analysis when durable evidence establishes post-closure same-family recurrence and `ARCHITECTURE_RECONSIDERATION_REQUIRED`, current authoritative evidence separately authorises the bounded read-only architecture reconsideration, and no current architecture-reconsideration record already satisfies that bound recurrence. If that reconsideration needs an architecture-closure proof, it must derive that proof through [Architecture closure analysis](../../prompts/workflows/architecture-closure-analysis.md) within the same one-shot read-only authority.
   - If recurrence establishes `ARCHITECTURE_RECONSIDERATION_REQUIRED` but the separate reconsideration authority is absent, do not select analysis; surface `DECISION_REQUIRED`. If a current bound record already establishes `ARCHITECTURE_RECONSIDERATION_COMPLETED`, do not re-enter analysis; continue from that assessment result and the remaining decision/remediation-authority boundary.
   - Also select stateful/invariant analysis for explicit read-only `/analyse` when the target is materially stateful, lifecycle-sensitive, cross-component, concurrency/retry/cache/inference-sensitive, or equivalent.
   - An explicit read-only `/analyse` request is resolved before an otherwise pending independent-review lifecycle gate. It does not discharge, bypass, weaken, or satisfy that review gate; after analysis returns, the pending fresh-review requirement remains governed by current authoritative state.
   - Do not select either analysis merely because two findings exist or because a simple local correction is available. Analysis completion creates no mutation or redesign authority.

3. **An independent substantive review is required now**.
   - If current state establishes `CLOSURE_REVIEW_REQUIRED` for an exact durable closure artefact and no current fresh review of that exact artefact has disposition `APPROVED_FOR_CANDIDATE_PROJECTION`, route `/review` to [Fresh independent review](../../prompts/workflows/fresh-independent-review.md) with `REVIEW_TYPE=ARCHITECTURE_CLOSURE`. A closure-review `CHANGES REQUIRED` result must follow its review-owned classification: only an eligible unused `MODELLED_DEFECT` or `PACKAGE_ONLY_DEFECT` may return within the same generation; structural/new/scope/authority/ambiguous/exhausted results route to `GOVERNING_DISPOSITION_REQUIRED`. It must not route generically to reconstruction, `/fix`, or candidate authoring. A closure-review `APPROVED_FOR_CANDIDATE_PROJECTION` result establishes projection eligibility for that exact closure artefact only; actual candidate authoring still requires separate current authority.
   - If the current context is genuinely fresh for that decision → [Fresh independent review](../../prompts/workflows/fresh-independent-review.md). Reconstruct the decision from the actual review target and evidence rather than inheriting the authoring conclusion; bind candidate identity additionally when the target is a candidate. Freshness is about the context/evidence boundary; it does not require a different GitHub account unless repository-local policy explicitly requires a distinct reviewer identity.
   - If the current context is not genuinely fresh, do not review in it. Resolve whether the execution surface can establish an eligible genuinely isolated review context whose information boundary excludes author-side substantive adjudication and expected conclusion. If yes, invoke [Fresh independent review](../../prompts/workflows/fresh-independent-review.md) there using the minimal durable review target or equivalent reconstruction reference. The receiving context must independently bootstrap applicable authority, reconstruct the exact review target/checks-or-evidence/review state, bind candidate identity when applicable, operate only under the bounded `/review` capability profile, and return a disposition/evidence record bound to the exact review target inspected. If isolation is unavailable, ambiguous, unprovable, incompatible with repository policy, or would require broader capability than `/review` permits → [Next-session handover](../../prompts/workflows/next-session-handover.md). Only when no eligible/provable isolated review context is available should the existing fresh-context review handoff be produced and the route stop as `EXTERNAL_REQUIRED`.
   - Fresh-review context resolution is an information-boundary mechanism, not an execution-locality class. Do not probe `connected/native`, `hosted/hermetic`, or owner-local execution merely to create reasoning independence. Creating/selecting a context is not authority, and a delegated context must not simulate a repository requirement for another human or formal reviewer.

4. **A newly supplied bounded approval or execution authority applies to the current proposal or action** → [Autonomous progression](../../prompts/workflows/autonomous-progression.md).
   - Identify the exact proposal or action being authorised. An unambiguous response to the current decision capsule, such as `A`, `accept`, `choose B`, or an equivalent natural-language/voice response, may supply that authority or choice.
   - Refresh decision-critical state and verify that the proposal/action and its authority boundary remain materially unchanged.
   - Consume the approval or authority once, only for that bounded object, then continue routine governed work through autonomous progression.
   - Do not treat approval as authority to expand scope, weaken controls or accept a materially changed proposal. Escalate a genuinely new human choice as `DECISION_REQUIRED`.

5. **A substantive repository documentation assessment is needed and representative reader tasks must be discovered, validated, or assessed together** → [Documentation assessment workflow](../../prompts/workflows/documentation-assessment.md).
   - Use this route for broad documentation-quality assessment, navigation or authority problems, or deciding the smallest justified documentation response when reader/task discovery or multi-task validation is part of the work.
   - Do not route ordinary bounded documentation edits, known corrections or explicit drafting tasks through assessment merely because documentation is involved.
   - If one concrete reader task is already known and no multi-task discovery or validation is needed, use [Repository documentation assessment](../../prompts/documentation/repository-assessment.md) as the proportionate single-task path.

6. **Ordinary governed continuation** → [Autonomous progression](../../prompts/workflows/autonomous-progression.md).
   - Continue while current policy, evidence, scope and available capabilities safely determine the next action.

7. **No safe route fits** → fail closed.
   - Do not invent work, authority or a workflow mapping merely to keep moving.
   - Use the terminal-state rules below to identify the real boundary.
