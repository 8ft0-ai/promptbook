# Workflow router

This directory is the canonical Promptbook entry point for governed engineering workflow continuation.

Point the agent here when you want it to determine the appropriate reusable workflow from the current task state rather than choosing an individual prompt yourself. The router does not create unrelated authority: platform safety rules, explicit task authority, repository-local instructions and current authoritative evidence remain higher precedence. An explicit shorthand command may carry only the narrow authority intrinsic to the operation defined for that command; it never supplies unrelated repository or lifecycle authority.

## Using the router

For ordinary continuation:

```text
Use `8ft0-ai/promptbook` → `prompts/workflows/README.md` as the workflow entry point.
Reconstruct the material current state and continue the governed work with minimal human intervention.
```

For a bounded approval:

```text
Follow `8ft0-ai/promptbook` → `prompts/workflows/README.md`.
Approved — proceed.
```

Do not manually choose a workflow when this router can determine the route from current evidence.

## Shorthand commands

When a user message begins with one of these commands, treat it as a concise intent selector. Resolve an omitted target from the current conversation and authoritative repository/task state only when that is unambiguous. Commands do not grant authority beyond the narrow operation authority explicitly defined here, bypass repository policy, weaken freshness or independence requirements, or turn unavailable capabilities into available ones. Any intrinsic operation authority is bounded to the requested command and does not become remediation, merge, release, deployment, settings, credential, production, or other unrelated authority.

The normal public surface is:

- `/go [target]` — continue the governed objective through repeated safely authorised governed transitions until a real boundary. If the target is already established, `/go` reconstructs current state instead of asking the operator to transport routine lifecycle evidence.
- `/step [target]` — execute exactly one safely authorised governed transition, including verification intrinsic to establishing that transition's result, re-resolve once, report what follows, and stop. If the next result is a real boundary rather than an executable transition, report the boundary without consequential mutation.
- `/next [target]` — read-only. Reconstruct the same governed state used by `/go` and `/step`, then report the single next governed transition or real boundary without executing it. Natural-language "what's next?" has the same semantics.
- `/status [target]` — read-only. Reconstruct and report broader authoritative current state, decision-critical identity, blocker/boundary, the same next transition reported by `/next`, what `/go` would do, and minimum decision-critical evidence.
- `/help [topic-or-question]` — read-only advisory interpretation of the same resolved state. Recommend what the operator should do and why, explain material alternatives or blockers, and answer prospective questions without executing the described action or creating authority.
- `/plan [target]` — use [Plan an issue](../engineering/plan-an-issue.md). Planning remains non-implementation work unless separate authority says otherwise.
- `/review [target]` — request a substantive independent review using [Fresh independent review](fresh-independent-review.md). For a GitHub pull request, ordinary `/review` includes the narrow authority to durably record the requested review on GitHub after refreshing the exact candidate/head and applying repository/platform constraints. For `REVIEW_TYPE=ARCHITECTURE_CLOSURE` whose closure artefact is durably anchored in a GitHub issue or issue comment, ordinary `/review` likewise includes only the narrow authority to publish one durable closure-review record as a new top-level comment on that owning issue. Treat repository object IDs as locators, not content-version identities: bind the reviewed closure to an edit-sensitive snapshot identity (for example locator plus canonical body digest and repository-native version/update witness), bind the review record to that exact closure snapshot, and bind the review record itself to an edit-sensitive snapshot identity. The created comment ID is therefore a locator component, not sufficient identity by itself. Closure-review records are append-only evidence for this gate; an in-place edit invalidates their fresh-review status and requires a new review record. If no permitted durable repository-native review-record target is available, the assessment may still be reported but cannot satisfy `CLOSURE_REVIEW_REQUIRED`. `/review --read-only [target]`, or an unambiguous natural-language equivalent such as `review without mutation` or `review only in chat`, performs the same assessment with zero GitHub write-back and therefore cannot by itself satisfy a durable closure-review gate. Review-recording authority does not grant remediation, merge, release, deployment, issue-closure, settings, credential, production, candidate authoring, or unrelated mutation authority.
- `/fix [target]` — use [Remediate review findings](../engineering/remediate-review-findings.md) for objectively bounded findings under existing authority. If review-response synthesis has not yet been satisfied, perform that non-mutating synthesis first. Explicit `/fix` performs bounded remediation, required validation, and a proportional author-side remediation-readiness sweep, freezes the exact resulting candidate when review-ready, then returns control rather than silently continuing into fresh review, merge, or later lifecycle effects. The readiness sweep is remediation evidence, not review or approval.
- `/save [target]` — persist the current material result in the smallest correct durable repository-native home. The command carries only the narrow intrinsic persistence authority defined by the resolved-run-context contract; it does not grant branch/PR/code/cross-repository/production mutation authority.
- `/prompt [target-or-request]` — generate the shortest safe context-transfer artefact only. It may generate a continuation, delegation, or independent-review prompt contract, but it does not execute the prompt, create another context, transfer authority, establish freshness, or change the current governed lifecycle state.
- `/risk [target-or-question]` — read-only. Use [Assess risk](assess-risk.md) to characterise material risk, controls, residual risk, uncertainty and legitimate disposition boundaries. Risk assessment does not accept risk, establish owner decisions, satisfy violated invariants, or create execution authority.
- `/reflect [target-or-episode]` — read-only. Use [Reflect on completed work](reflect-on-work.md) to compare expectations with observed outcomes and derive justified episode-bound lessons. Reflection may be self-assessment but cannot satisfy fresh independent review, activate follow-up scope, or automatically promote a local lesson to policy.
- `/challenge [target-or-proposal]` — read-only. Use [Challenge assumptions](challenge-assumptions.md) to adversarially test assumptions, evidence, model, contract, or proposed course. Challenge may question the contract itself but cannot approve a candidate, amend that contract, or satisfy a qualified review gate.

For one authoritative resolved snapshot, preserve this projection invariant:

```text
/next   -> reports transition T or boundary B
/status -> reports Next: T/B
/help   -> advice is based on T/B
/step   -> executes T only when T is ALLOW and executable; otherwise reports B
/go     -> repeats the same transition loop until B
```

Keep the command set small. `--read-only` remains the one explicit `/review` modifier justified by a write-back boundary; otherwise prefer natural-language qualifiers over inventing flags or a larger command grammar.

## Compatibility intents

These legacy or advanced intents remain understandable for compatibility but are not part of the advertised normal public surface:

- `/implement [target]` — route to [Implement an approved issue](../engineering/implement-an-approved-issue.md) when the target is sufficiently approved/determined and repository mutation is already authorised.
- `/handoff [target]` — compatibility intent for generating a context-transfer prompt when that is the requested deliverable. It must not replace a complete human-operated `EXTERNAL_REQUIRED` execution handoff.
- `/record [target]` — compatibility alias for `/save`.
- `/analyse [target]` — read-only analysis/synthesis intent. When the target is materially stateful/lifecycle-sensitive or the repeated-review escalation rule is established, route through [Stateful invariant analysis](stateful-invariant-analysis.md). It may produce a plan when explicitly requested, but does not create a new lifecycle stage or mutation authority.

Do not advertise compatibility intents as equal public commands.

For ordinary `/go` continuation, **operation + durable target is the normal operator contract**. When the target unambiguously identifies the governed objective, reconstruct machine-recoverable lifecycle state from current authoritative sources rather than requiring the user to copy it into the invocation. Candidate heads, pull-request identities, validation/check runs, review dispositions, durable comment identities and lifecycle stage are evidence to derive when they are unambiguous; conversation history may help locate them but is not authority.

Treat an explicit current-user identity or constraint differently from derived state. A deliberate qualifier such as `/go <target> against exact head <sha>` is an **essential assertion** that constrains the requested operation. Refresh it against authoritative state and do not silently replace it with a newer or different reconstructed value. If an explicit assertion is stale or conflicts with current state, surface the changed-state decision or fail closed under the existing terminal semantics.

Target-only invocation is valid only while reconstruction is unambiguous. If multiple active candidates, conflicting authorities, materially different pending actions, or missing decision-critical evidence prevent a unique safe interpretation, do not guess. Reducing operator input never collapses separate authority boundaries such as candidate approval, merge, release, deployment, or production mutation.

For a conceptual map of `/go` state, authority, capability, evidence rebinding and terminal boundaries, see [`/go` lifecycle](../../guides/go-lifecycle.md). The router remains the canonical behavioural contract.

Keep the command set small. `--read-only` is the one explicit `/review` modifier justified by the write-back boundary; otherwise prefer natural-language qualifiers over inventing flags or a larger command grammar.

For every substantive `/review`, discovering a material blocker ends approval eligibility but does not end the substantive inspection. Complete the bounded decision-critical review surface for the exact review target before recording the disposition; when the target is a candidate, bind that surface to the exact candidate identity. For `CHANGES REQUIRED`, report all material blockers discovered across that completed surface. The detailed coverage model and re-review rules live in [Fresh independent review](fresh-independent-review.md); the router does not replace them with a universal checklist.

When a completed review exposes `CHANGES REQUIRED`, perform response routing/synthesis before remediation. Consume the completed review's disposition, complete blocker set, relationship diagnosis, governing design and freshly reconstructed authoritative state; do not perform a second author-side substantive review. Classify the response as `BOUNDED_REMEDIATION`, `DESIGN_CHANGE_REQUIRED`, `ARCHITECTURE_ISSUE`, `REVIEW_FINDING_INVALID_OR_SUPERSEDED`, or `DECISION_REQUIRED`. A bounded invariant/boundary correction remains eligible only when it is objectively the minimum safe correction and already within remediation authority. `REVIEW_FINDING_INVALID_OR_SUPERSEDED` requires new authoritative evidence, material candidate/state movement, or an objectively demonstrable governing-contract mismatch; mere author-side disagreement with an independent blocker is insufficient. A genuine unresolved substantive disagreement must return to an appropriate independent adjudication or decision boundary rather than being silently overruled. When the completed review contains materially related blockers, preserve and synthesise their relationship before selecting the response route; this relationship assessment does not widen `/fix`, and any invariant/boundary correction is eligible only when it is already within existing remediation authority.

Before selecting ordinary `BOUNDED_REMEDIATION`, apply an evidence-based adjacent-model challenge when a fresh material blocker is classified as a new defect family after an immediately preceding remediation. Establish `ADJACENT_MODEL_OMISSION` (or a reconstructable equivalent) only when all materially apply: (1) the blocker is adjacent to that immediately preceding remediation in a materially stateful, lifecycle-, authority-, identity- or recovery-sensitive domain; (2) the remediation omitted a necessary semantic owner, state dimension, identity/currentness relation, transition class, recovery path, equivalence relation or effect boundary and therefore did not represent that decision-critical dimension; (3) representing that missing dimension can change correctness beyond the named reproduction or local predicate; and (4) another narrow patch would therefore risk continuing an example-by-example review/fix loop. This challenge does not require a prior R1/R2 invariant-closure attempt or post-closure lineage. Adjacency, shared terminology, finding count or a `new defect family` label alone is insufficient. When `ADJACENT_MODEL_OMISSION` is established, ordinary `/fix` is ineligible: do not select ordinary `BOUNDED_REMEDIATION` or route directly to `/fix`; route first to [Stateful invariant analysis](stateful-invariant-analysis.md), require reconstruction of the complete relevant shared model, bounded transition/adversarial matrix and positive reachability, and require one encompassing remediation plan derived from that model before separately authorised mutation. If the model is materially security-, authority-, identity- or recovery-sensitive and is being treated as closure-ready, invoke the existing [Architecture closure analysis](architecture-closure-analysis.md) inside that read-only analysis boundary. A genuinely independent new defect family with no evidence of an omitted shared-model dimension remains on the ordinary response-classification path. This analysis gate creates no mutation, redesign or later lifecycle authority.

When response synthesis selects `BOUNDED_REMEDIATION`, it must produce a concise candidate-bound remediation plan containing the source candidate identity, complete blocker set being addressed, material finding relationships or shared invariant, bounded correction, required validation, and explicit scope boundaries. That plan becomes the authoritative synthesis input to `/fix`; it is not mutation authority and does not make stale candidate-specific evidence current. `/fix` must refresh current candidate/state and authority before mutation and must return to response routing or fail closed if the plan is stale, conflicts with current authoritative evidence, or requires a broader correction.

Once ordinary `BOUNDED_REMEDIATION` is valid and the authorised correction has been implemented and required validation has passed, `/fix` must complete a bounded, proportional **remediation-readiness sweep** before the resulting candidate can be treated as review-ready. Treat the completed review findings as seeds for the sweep, not as the exhaustive search universe. Reconstruct the currently applicable remediation surface from the governing contract, the complete finding set and relationship diagnosis, the actual resulting candidate and changed integration paths, repository-local policy, applicable producer/consumer or caller/callee contracts, and any current invariant/model artefact already required by a stronger route. Challenge only decision-critical sibling and alternate paths that are materially applicable; a simple local correction remains lightweight and does not require a universal architecture or state-machine exercise.

The readiness sweep is author-side falsification of the remediated candidate, not a second substantive review. Where materially applicable, challenge identity/equality aliases, authority or caller-controlled semantic inputs, alternate capability/entry paths, currentness/freshness, provenance, sibling lifecycle/retry/recovery paths, fail-closed handling of unknown/incomplete/contradictory valid states, positive reachability, hostile-but-valid configuration substitution, representation symmetry, producer/consumer compatibility, and output effect/authority claims. Ask what other caller-controlled input, production path, symmetric case, adversarial-but-valid input, output identity claim, nearby state/transition, or unenforced remediation assumption could reach the corrected boundary differently. These are proportional challenge dimensions, not a checklist that every remediation must exhaust.

If the sweep exposes another objectively bounded defect within current remediation authority, keep it in the same remediation cycle: correct it, update regression evidence where feasible, re-run required validation affected by the change, and repeat the affected readiness challenges before freezing the candidate. If the new evidence requires broader product, architecture, security, scope, owner or other authority, stop further mutation and return to the existing response-routing/decision rules. If it establishes an existing stronger escalation trigger, including repeated-review stateful escalation, post-closure recurrence, closure-method falsification or `ADJACENT_MODEL_OMISSION`, that stronger route wins; the sweep cannot suppress, replace or manufacture its required analysis authority.

Successful substantive-review remediation is reconstructable only when all of `FINDINGS_ADDRESSED`, `REQUIRED_VALIDATION_PASSED`, `REMEDIATION_READINESS_SWEEP_COMPLETE`, `EXACT_RESULTING_CANDIDATE_FROZEN`, and `FRESH_REVIEW_BOUNDARY_PRESERVED` are established for the same resulting candidate. A status such as `REMEDIATION_COMPLETE_PENDING_FRESH_REVIEW` may record that state, but must not be represented as `APPROVED`, `REVIEW_PASSED`, an architecture-closure result, or independent review evidence.

### Repeated-review stateful escalation

Before routing another `/fix`, reconstruct whether durable review/remediation evidence establishes the mandatory repeated-review escalation trigger. The trigger requires all of:

1. substantive review round **R1** recorded `CHANGES REQUIRED` for behavioural/invariant domain **X**;
2. authorised remediation changed the candidate;
3. a genuinely fresh substantive review round **R2** of the resulting candidate again recorded `CHANGES REQUIRED`; and
4. at least one material R2 blocker is evidence-based and materially belongs to the same behavioural/invariant domain **X**.

A materially same behavioural/invariant domain means a shared invariant, lifecycle/state model, mechanism, trust boundary, inference rule, retry/recovery mechanism, or implementation abstraction established from evidence. Finding count or textual similarity alone is insufficient.

The initial R1/R2 trigger is not satisfied merely by two blockers in one substantive review, a duplicate/repeated review against unchanged bytes that adds no new substantive same-family blocker, materially unrelated R1/R2 domains, a governing requirement that became applicable only after R1, duplicate review records of one substantive adjudication, or a non-substantive check/test failure by itself. A later genuinely fresh substantive review may still expose a new material blocker on unchanged bytes; unchanged bytes alone never erase or suppress new review evidence.

When the trigger is established, do not route directly to another narrow `/fix`. Route first to [Stateful invariant analysis](stateful-invariant-analysis.md) and require a current read-only analysis record bound to the exact candidate, R1/R2 review identities and dispositions, materially related blocker/domain evidence, and governing contract. The escalation is process-driven rather than conclusion-driven: it does not establish that an abstraction is unsound, does not authorise redesign, does not widen `/fix`, and creates no mutation or later lifecycle authority.

Material candidate or governing-contract movement invalidates or requires refresh of candidate-bound analysis under the existing freshness/state rules. Once current analysis has completed and an authorised remediation based on it produces a new exact candidate, the initial R1/R2 analysis gate is satisfied for that remediation attempt, but the historical fact that behavioural/invariant domain X has undergone an invariant-closure attempt remains reconstructable from durable evidence.

Treat the resulting closure claim as provisional until a genuinely fresh substantive review challenges the new exact candidate. If that review independently establishes that a material evidence-based blocker belongs to the same defect family covered by X's invariant-closure attempt, classify the closure as falsified and route to separately governed architecture reconsideration rather than ordinary bounded `/fix`. A material blocker in the same broader behavioural/invariant domain X that is independently classified as a new defect family does not falsify closure; independently apply the general `ADJACENT_MODEL_OMISSION` challenge above before permitting ordinary remediation. If that review finds no blocker in the defect family covered by X's closure attempt, it may establish `CLOSURE_SURVIVED_THIS_REVIEW` and clear the pending closure-validation gate, but it must not erase `INVARIANT_CLOSURE_ATTEMPTED(X)` lineage.

After `CLOSURE_SURVIVED_THIS_REVIEW`, a later genuinely fresh substantive blocker in X is a post-closure same-family recurrence when the relevant X invariant/surface remained materially within the prior closure attempt. That recurrence requires `ARCHITECTURE_RECONSIDERATION_REQUIRED` and leaves ordinary `/fix` ineligible while the architecture boundary is unresolved. Distinguish this from an intervening regression that demonstrably broke an already-established X contract, a new defect family, an unrelated domain, a newly applicable governing requirement, or a materially out-of-boundary candidate/domain change. Those cases continue through their appropriate existing classification rather than being mechanically escalated. When the same-family recurrence is independently established as an equivalent **structural falsification** of a closure artefact that previously received `APPROVED_FOR_CANDIDATE_PROJECTION`—rather than a local regression inside a still-sound model—require `COMPLEXITY_DISPOSITION_REQUIRED` before architecture reconsideration expands that model.

`ARCHITECTURE_RECONSIDERATION_REQUIRED` is a separate-authority boundary, not authority to execute the reconsideration. If current authoritative evidence does not separately authorise the bounded read-only architecture reconsideration, `/go` and `/step` must surface `DECISION_REQUIRED` rather than enter analysis. When that separate authority is current and no current architecture-reconsideration record already satisfies the bound recurrence, route exactly one read-only architecture reconsideration through [Stateful invariant analysis](stateful-invariant-analysis.md). A current record bound to the prior closure lineage, recurrence review, exact candidate, governing contract and reconsideration-authority source establishes `ARCHITECTURE_RECONSIDERATION_COMPLETED` (or a reconstructable equivalent) for those identities and satisfies the architecture-analysis gate. Do not re-enter architecture reconsideration while that record remains current; material movement of a binding invalidates it under the normal freshness rules. Completion creates no remediation or design-mutation authority: any resulting correction requires separately established current authority and a new response-synthesis/remediation plan derived from the architecture result.

When an authorised architecture reconsideration needs to establish that a materially security-, authority-, identity-, recovery- or migration-sensitive architecture is closed before a resulting proposal can be treated as closure-ready, derive that closure through [Architecture closure analysis](architecture-closure-analysis.md) rather than treating the candidate's own prose/object list as the completeness universe. The architecture-closure proof is part of the current one-shot read-only reconsideration and inherits only that bounded analysis authority; it creates no mutation authority. Require an independently derived closed source/obligation universe, total source → primitive coverage, a closed primary-role primitive partition, cross-checkable object/state/operation/authority/effect inventories, global identity-dependency DAG, ownership/state/transition closure, positive reachability, end-to-end authority/effect coverage, extensional consequence ownership/disjointness proof, ambiguity/recovery closure, equivalence/overlap proof coverage, terminal provenance and migration/fence closure where applicable.

Whenever architecture-closure analysis returns `ARCHITECTURE_CLOSURE_READY` for work governed by the proactive, reconsideration, adjacent-model, or reconstruction path, establish `CLOSURE_REVIEW_REQUIRED` bound to that exact durable closure artefact. `ARCHITECTURE_CLOSURE_READY` is an author-side analysis disposition, not self-approval and not candidate-authoring eligibility. Before a replacement or closure-ready candidate may be authored/projected from that artefact, require a genuinely fresh [Fresh independent review](fresh-independent-review.md) with review target type `ARCHITECTURE_CLOSURE`. Only `APPROVED_FOR_CANDIDATE_PROJECTION` for the exact current closure artefact satisfies this gate. `CHANGES_REQUIRED` keeps candidate authoring ineligible and must be classified by the fresh closure review before continuation. A bounded `MODELLED_DEFECT` may consume the generation's one semantic-correction allowance; a true `PACKAGE_ONLY_DEFECT` may consume the one package-only repair allowance. `NEW_OR_OMITTED_OBLIGATION`, `STRUCTURAL_FALSIFICATION`, `SCOPE_OR_AUTHORITY_MOVEMENT`, ambiguous correction eligibility, or exhausted allowance routes to `GOVERNING_DISPOSITION_REQUIRED`. Do not author a partial candidate merely to obtain another review signal, and do not automatically create an equivalent successor closure generation. Fresh candidate review remains separately required after projection.

The canonical lifecycle transitions for this gate are:

```text
ARCHITECTURE_CLOSURE_LIFECYCLE_V2
CURRENT | EVENT | NEXT | CANDIDATE_PROJECTION | REQUIRED_ACTION
ORDINARY_BOUNDED_REMEDIATION | REVIEW_CHANGES_REQUIRED | FIX_REQUIRED | NOT_APPLICABLE | FIX
FIX_REQUIRED | REMEDIATION_IMPLEMENTED_AND_VALIDATED | REMEDIATION_READINESS_REQUIRED | NOT_APPLICABLE | READINESS_SWEEP
ADJACENT_MODEL_OMISSION | ARCHITECTURE_CLOSURE_SELECTED | ARCHITECTURE_CLOSURE_ANALYSIS_REQUIRED | NO | ANALYSE_CLOSURE
ARCHITECTURE_CLOSURE_ANALYSIS_REQUIRED | READY_CLOSURE_SNAPSHOT_FROZEN | CLOSURE_REVIEW_REQUIRED | NO | FRESH_CLOSURE_REVIEW
CLOSURE_REVIEW_REQUIRED | DURABLE_MODELLED_DEFECT_RECORDED | CLOSURE_MODEL_CORRECTION_REQUIRED | NO | CONSUME_SEMANTIC_CORRECTION
CLOSURE_MODEL_CORRECTION_REQUIRED | SEMANTIC_CORRECTION_ALLOWANCE_AVAILABLE_AND_CORRECTED_SNAPSHOT_FROZEN | CLOSURE_REVIEW_REQUIRED | NO | FRESH_CLOSURE_REVIEW
CLOSURE_MODEL_CORRECTION_REQUIRED | SEMANTIC_CORRECTION_ALLOWANCE_EXHAUSTED | GOVERNING_DISPOSITION_REQUIRED | NO | GOVERNING_DISPOSITION
CLOSURE_REVIEW_REQUIRED | DURABLE_PACKAGE_ONLY_DEFECT_RECORDED | CLOSURE_PACKAGE_REPAIR_REQUIRED | NO | CONSUME_PACKAGE_REPAIR
CLOSURE_PACKAGE_REPAIR_REQUIRED | PACKAGE_ONLY_REPAIR_ALLOWANCE_AVAILABLE_AND_PACKAGE_READMITTED | CLOSURE_REVIEW_REQUIRED | NO | FRESH_CLOSURE_REVIEW
CLOSURE_PACKAGE_REPAIR_REQUIRED | PACKAGE_ONLY_REPAIR_ALLOWANCE_EXHAUSTED | GOVERNING_DISPOSITION_REQUIRED | NO | GOVERNING_DISPOSITION
CLOSURE_REVIEW_REQUIRED | DURABLE_NEW_OR_OMITTED_OBLIGATION_RECORDED | GOVERNING_DISPOSITION_REQUIRED | NO | GOVERNING_DISPOSITION
CLOSURE_REVIEW_REQUIRED | DURABLE_STRUCTURAL_FALSIFICATION_RECORDED | GOVERNING_DISPOSITION_REQUIRED | NO | GOVERNING_DISPOSITION
CLOSURE_REVIEW_REQUIRED | DURABLE_SCOPE_OR_AUTHORITY_MOVEMENT_RECORDED | GOVERNING_DISPOSITION_REQUIRED | NO | GOVERNING_DISPOSITION
CLOSURE_REVIEW_REQUIRED | DURABLE_AMBIGUOUS_CORRECTION_CLASSIFICATION_RECORDED | GOVERNING_DISPOSITION_REQUIRED | NO | GOVERNING_DISPOSITION
CLOSURE_REVIEW_REQUIRED | DURABLE_UNCLASSIFIED_CHANGES_REQUIRED_RECORDED | GOVERNING_DISPOSITION_REQUIRED | NO | GOVERNING_DISPOSITION
GOVERNING_DISPOSITION_REQUIRED | AUTHORISE_NEW_STRONG_CLOSURE_GENERATION | ARCHITECTURE_CLOSURE_ANALYSIS_REQUIRED | NO | START_NEW_GENERATION
GOVERNING_DISPOSITION_REQUIRED | DECOMPOSE_OR_REDUCE_ASSURANCE | ORDINARY_FLOW | NOT_APPLICABLE | FOLLOW_GOVERNED_DISPOSITION
GOVERNING_DISPOSITION_REQUIRED | DEFER_OR_ABANDON | GOVERNING_DISPOSITION_REQUIRED | NO | STOP_CURRENT_GENERATION
CLOSURE_REVIEW_REQUIRED | READ_ONLY_APPROVED_FOR_CANDIDATE_PROJECTION | CLOSURE_REVIEW_REQUIRED | NO | DURABLE_REVIEW_RECORD_REQUIRED
CLOSURE_REVIEW_REQUIRED | DURABLE_APPROVED_FOR_CURRENT_SNAPSHOT_RECORDED | CLOSURE_APPROVED | SEPARATE_AUTHORITY_REQUIRED | RESOLVE_CANDIDATE_AUTHORITY
CLOSURE_APPROVED | CANDIDATE_AUTHORITY_UNAVAILABLE | CLOSURE_APPROVED | NO | RESOLVE_CANDIDATE_AUTHORITY
CLOSURE_APPROVED | CANDIDATE_AUTHORITY_CURRENT | CANDIDATE_PROJECTION_ELIGIBLE | YES | PROJECT_CANDIDATE
CLOSURE_APPROVED | CLOSURE_SNAPSHOT_CHANGED | GOVERNING_DISPOSITION_REQUIRED | NO | GOVERNING_DISPOSITION
CLOSURE_APPROVED | CLOSURE_REVIEW_RECORD_CHANGED_OR_INVALID | CLOSURE_REVIEW_REQUIRED | NO | FRESH_CLOSURE_REVIEW
CLOSURE_APPROVED | GOVERNING_SCOPE_CHANGED | GOVERNING_DISPOSITION_REQUIRED | NO | GOVERNING_DISPOSITION
CANDIDATE_PROJECTION_ELIGIBLE | CLOSURE_SNAPSHOT_CHANGED | GOVERNING_DISPOSITION_REQUIRED | NO | GOVERNING_DISPOSITION
CANDIDATE_PROJECTION_ELIGIBLE | CLOSURE_REVIEW_RECORD_CHANGED_OR_INVALID | CLOSURE_REVIEW_REQUIRED | NO | FRESH_CLOSURE_REVIEW
CANDIDATE_PROJECTION_ELIGIBLE | GOVERNING_SCOPE_CHANGED | GOVERNING_DISPOSITION_REQUIRED | NO | GOVERNING_DISPOSITION
CANDIDATE_PROJECTION_ELIGIBLE | NEW_DECISION_CRITICAL_SEMANTICS | GOVERNING_DISPOSITION_REQUIRED | NO | GOVERNING_DISPOSITION
CANDIDATE_PROJECTION_ELIGIBLE | CANDIDATE_PROJECTED_WITHIN_APPROVED_UNIVERSE | CANDIDATE_READINESS_REQUIRED | ALREADY_PROJECTED | VALIDATE_AND_READINESS
CANDIDATE_READINESS_REQUIRED | VALIDATION_AND_READINESS_COMPLETE | CANDIDATE_REVIEW_REQUIRED | ALREADY_PROJECTED | FRESH_CANDIDATE_REVIEW
CLOSURE_REVIEW_REQUIRED | REVIEW_ATTEMPTS_IMPLEMENTATION_OR_MERGE | CLOSURE_REVIEW_REQUIRED | NO | FORBID_UNRELATED_AUTHORITY
CLOSURE_REVIEW_REQUIRED | GO_ATTEMPTS_CANDIDATE_PROJECTION | CLOSURE_REVIEW_REQUIRED | NO | FORBID_PROJECTION
APPROVED_CLOSURE_LINEAGE | CLOSURE_METHOD_FALSIFIED | GOVERNING_DISPOSITION_REQUIRED | NO | GOVERNING_DISPOSITION
APPROVED_CLOSURE_LINEAGE | EQUIVALENT_SAME_FAMILY_STRUCTURAL_FALSIFICATION | GOVERNING_DISPOSITION_REQUIRED | NO | GOVERNING_DISPOSITION
LOCAL_OR_INCOMPLETE_DESIGN | NO_STRONG_CLOSURE_CLAIM | ORDINARY_FLOW | NOT_APPLICABLE | NO_CLOSURE_REVIEW
```

Treat this table```

Treat this table as the canonical route invariant for the strong closure-review lifecycle. Each strong-closure generation has an immutable generation identity, one monotone semantic-correction allowance and one monotone package-only repair allowance. Consuming either allowance cannot be undone by renaming, repackaging, issue recreation, candidate replacement or snapshot regeneration. Fresh review owns the negative-route classification. A `MODELLED_DEFECT` is correction-eligible only when the governing obligation/primitive is already represented and scope/authority is unchanged; a `PACKAGE_ONLY_DEFECT` is repair-eligible only when the canonical semantic model and its decision-critical inputs/outputs are unchanged. Any mixed or ambiguous finding involving omitted obligation, structural falsification, scope movement or authority movement fails closed to `GOVERNING_DISPOSITION_REQUIRED`. That state terminates active progression for the current generation; a later generation requires an explicit separately governed disposition, receives a new generation identity, and preserves terminal predecessor provenance. The durable approval event still requires an admissible repository-native review-record snapshot bound to the exact current closure snapshot; locator equality alone is insufficient for mutable objects. A chat-only/read-only approval does not satisfy the gate. Consumer workflows may add evidence but must not introduce a transition that contradicts this table.

Separately from those reactive reconsideration/reconstruction paths, apply a **proactive architecture-closure publication gate** when both conditions are established: (1) the proposed architecture is materially security-, authority-, identity-, recovery/ambiguity-, irreversible-effect-, or migration/cutover-sensitive; and (2) the resulting candidate is intended to claim or be treated as closed-world, architecture-closed, closure-ready, complete over its decision-critical authority/effect universe, or an equivalent strong completeness claim. Before such a candidate is authored, published or routed as closure-ready, require a current [Architecture closure analysis](architecture-closure-analysis.md) artefact derived independently from the candidate **and** a genuinely fresh closure review of that exact artefact with `APPROVED_FOR_CANDIDATE_PROJECTION`. The candidate must consume/project that exact approved closure snapshot rather than define the universe used to prove its own completeness, and its durable authoring/projection record must bind both the edit-sensitive closure snapshot identity and the edit-sensitive closure-review record identity. Immediately before projection, revalidate both snapshots; movement of either invalidates projection eligibility. Architecture size, keyword presence, ordinary exploratory design, explicitly incomplete drafts and bounded local design do not satisfy this trigger by themselves. Material governing-contract or architecture-scope movement that changes the covered decision-critical universe makes the affected closure evidence stale for another closure-ready claim; a local correction wholly inside an already-modelled primitive does not automatically require full reconstruction when current coverage remains applicable. This proactive gate does not create candidate-authoring, remediation, merge or other consequential authority and does not replace fresh independent review.

If a later genuinely fresh substantive review establishes that an applicable decision-critical primitive or relation should have been present in that closure universe but was absent, classify the evidence as `UNMODELLED_DECISION_CRITICAL_PRIMITIVE` and establish `CLOSURE_METHOD_FALSIFIED` and route the current strong-closure generation to `GOVERNING_DISPOSITION_REQUIRED`. Ordinary isolated `/fix` is ineligible. The earlier one-shot architecture reconsideration or closure authority does not authorise another equivalent closure generation. A later reconstruction/new generation may occur only after an explicit separately governed disposition authorises it and binds the successor to the terminal predecessor evidence; do not loop automatically into repeated reconstruction.

If a closure artefact previously had a current fresh `APPROVED_FOR_CANDIDATE_PROJECTION` review and later fresh evidence establishes either `CLOSURE_METHOD_FALSIFIED` **or `EQUIVALENT_SAME_FAMILY_STRUCTURAL_FALSIFICATION`**, require `COMPLEXITY_DISPOSITION_REQUIRED` before automatically expanding the model again. The equivalent structural class applies only when the fresh review independently establishes that the same-family recurrence demonstrates structural inadequacy of the approved closure/model rather than a local regression inside a still-sound model. Assess whether the objective can safely remove state, authority/configuration/effect paths, reuse a platform primitive, move to a more authoritative boundary, split the contract/lifecycle, narrow the objective, or retire contradictory active surface. Record `SIMPLIFY_OR_DECOMPOSE` or `ADDITIONAL_MODEL_COMPLEXITY_JUSTIFIED`. This is a forced consideration of simplification, not a requirement to hide necessary complexity.

If `/step` is invoked immediately after `CHANGES REQUIRED`, review-response synthesis is the one governed transition. When fresh review establishes `CLOSURE_METHOD_FALSIFIED`, that synthesis classifies the response as `ARCHITECTURE_ISSUE`, reports `GOVERNING_DISPOSITION_REQUIRED` as the next transition/boundary for the current strong-closure generation, and stops without remediation mutation. A later reconstruction/new generation is reachable only after a separately governed disposition explicitly authorises `AUTHORISE_NEW_STRONG_CLOSURE_GENERATION`. When post-closure same-family recurrence is established, that synthesis classifies the response as `ARCHITECTURE_ISSUE`, reports `ARCHITECTURE_RECONSIDERATION_REQUIRED` as the next transition/boundary, and stops without remediation mutation. When `ADJACENT_MODEL_OMISSION` is established, whether or not a prior R1/R2 invariant-closure attempt exists, that synthesis reports stateful/invariant analysis as the next transition and stops without remediation mutation. When the initial repeated-review escalation trigger is established, that synthesis likewise reports stateful/invariant analysis as the next transition and stops without remediation mutation. Otherwise, when it resolves to `BOUNDED_REMEDIATION`, `/step` produces the candidate-bound remediation plan, re-resolves state once, reports `/fix` as the next transition, and stops without performing remediation mutation. Under `/go`, the same synthesis transition may be followed by mandatory read-only stateful/invariant analysis, architecture reconsideration or separately authorised architecture-closure reconstruction when required, or by authorised `/fix` progression when no such analysis/architecture gate remains, because `/go` continues until a real boundary.

## Continuation policy

Continuation mode is a preference layer owned by this router. Apply it only after all hard governance constraints have been satisfied. A specialised workflow's local output, disposition, implementation record, remediation record, or other workflow record is not permission to end a routed objective in an unexplained intermediate state.

The supported continuation modes are:

- `auto` — enter the next safely authorised and executable workflow automatically. `auto` cannot make a non-fresh current context review its own work; when independent review is the next gate it may cross that hard boundary only by invoking an eligible genuinely isolated fresh-review context under the bounded `/review` profile. If no such context is eligible/provable, the boundary remains a stop and uses the existing manual fallback.
- `suggest` — do not enter the next workflow in this invocation. When a broader objective remains active, emit the smallest safely determined `Next:` or `Next chat:` navigation.
- `stop` — treat the explicitly requested deliverable as the end of this invocation and do not enter another workflow. `stop` does not suppress required terminal-state classification. When a broader governed objective is already active and its next invocation is safely determined, router postconditions may still expose that navigation unless the user explicitly requested no continuation guidance.

Hard constraints always win over continuation preferences. These include platform safety, explicit task authority, repository-local mandatory policy, fresh-independence requirements, required validation, current authoritative evidence, accepted governance records that require a stop or hand-off, and any other mandatory control established by the governing task. A continuation preference cannot create or bypass mutation, merge, deploy, credential, production, acceptance, review, validation, security, or scope authority. An eligible isolated review context satisfies a freshness requirement through independent adjudication; it does not weaken that requirement or make the authoring context fresh.

Within the remaining continuation-preference layer, resolve the effective mode in this order:

1. explicit current-user qualifier, such as `review only`, `continue afterwards`, or `/go until ...`;
2. repository/task-specific continuation preference, when one exists and is not already a mandatory hard constraint;
3. managed Project continuation preference, when one exists;
4. Promptbook command default.

The command defaults are:

| Command | Default continuation mode |
| --- | --- |
| `/go` | `auto` |
| `/step` | `stop` |
| `/next` | `stop` |
| `/status` | `stop` |
| `/help` | `stop` |
| `/plan` | `suggest` |
| `/review` | `suggest` |
| `/fix` | `suggest` |
| `/save` | `stop` |
| `/prompt` | `stop` |
| `/risk` | `stop` |
| `/reflect` | `stop` |
| `/challenge` | `stop` |

Explicit `/fix` is a scope-control request. Automatic remediation followed by further review/merge/verification progression remains available through `/go`; the bounded `/fix` invocation itself does not silently become `/go`.

Compatibility `/implement` retains its existing implementation workflow behaviour when explicitly invoked, but it is not an advertised normal command. Compatibility `/handoff`, `/record`, and `/analyse` inherit the stop/read-only semantics of the public intent they map to.

A lower-precedence preference may choose only among actions already permitted by higher-precedence constraints. Navigation emitted under `suggest` or `stop` is navigation metadata only and never supplies authority to the receiving invocation.

## Routing

Before routing, inspect the current conversation and the authoritative repository or task state needed for the next decision. Stale summaries are navigation aids, not authority. Select exactly one primary workflow and apply it immediately; routing itself is not a stop point.

Use the first matching case:

1. **A context-transfer prompt is explicitly the requested deliverable** → [Next-session handover](next-session-handover.md).
   - Generate only the requested context-transfer artefact. Select a continuation, delegation, or independent-review receiving contract from user intent and current state when unambiguous.
   - Generating the artefact does not create the receiving context, transfer authority, establish independence/freshness, or change the current lifecycle state.
   - Do not use this route to replace a complete human-operated `EXTERNAL_REQUIRED` execution handoff.

2. **Mandatory architecture/stateful analysis is required now**.
   - If materially high-risk architecture is intended to carry a strong closed-world / architecture-closed / closure-ready completeness claim and no current independently derived closure artefact covers the governing contract and architecture scope → [Architecture closure analysis](architecture-closure-analysis.md) before closure-ready candidate authoring/publication. Treat this as the proactive publication gate, not as repeated-review escalation or architecture reconsideration. If the current task does not provide the bounded read-only investigation/analysis authority needed to derive that artefact, surface `DECISION_REQUIRED`.
   - If current evidence establishes `CLOSURE_METHOD_FALSIFIED`, route the current strong-closure generation to `GOVERNING_DISPOSITION_REQUIRED`. Only if a separate governing disposition has explicitly authorised `AUTHORISE_NEW_STRONG_CLOSURE_GENERATION` may a new generation enter [Architecture closure analysis](architecture-closure-analysis.md); bind that successor to terminal predecessor evidence and new exact generation identity. Without that disposition, do not re-enter closure analysis.
   - Otherwise select [Stateful invariant analysis](stateful-invariant-analysis.md) when the repeated-review escalation trigger is established and no current candidate-bound analysis satisfies it.
   - Also select stateful/invariant analysis when durable evidence establishes post-closure same-family recurrence and `ARCHITECTURE_RECONSIDERATION_REQUIRED`, current authoritative evidence separately authorises the bounded read-only architecture reconsideration, and no current architecture-reconsideration record already satisfies that bound recurrence. If that reconsideration needs an architecture-closure proof, it must derive that proof through [Architecture closure analysis](architecture-closure-analysis.md) within the same one-shot read-only authority.
   - If recurrence establishes `ARCHITECTURE_RECONSIDERATION_REQUIRED` but the separate reconsideration authority is absent, do not select analysis; surface `DECISION_REQUIRED`. If a current bound record already establishes `ARCHITECTURE_RECONSIDERATION_COMPLETED`, do not re-enter analysis; continue from that assessment result and the remaining decision/remediation-authority boundary.
   - Also select stateful/invariant analysis for explicit read-only `/analyse` when the target is materially stateful, lifecycle-sensitive, cross-component, concurrency/retry/cache/inference-sensitive, or equivalent.
   - An explicit read-only `/analyse` request is resolved before an otherwise pending independent-review lifecycle gate. It does not discharge, bypass, weaken, or satisfy that review gate; after analysis returns, the pending fresh-review requirement remains governed by current authoritative state.
   - Do not select either analysis merely because two findings exist or because a simple local correction is available. Analysis completion creates no mutation or redesign authority.

3. **An independent substantive review is required now**.
   - If current state establishes `CLOSURE_REVIEW_REQUIRED` for an exact durable closure artefact and no current fresh review of that exact artefact has disposition `APPROVED_FOR_CANDIDATE_PROJECTION`, route `/review` to [Fresh independent review](fresh-independent-review.md) with `REVIEW_TYPE=ARCHITECTURE_CLOSURE`. A closure-review `CHANGES REQUIRED` result must follow its review-owned classification: only an eligible unused `MODELLED_DEFECT` or `PACKAGE_ONLY_DEFECT` may return within the same generation; structural/new/scope/authority/ambiguous/exhausted results route to `GOVERNING_DISPOSITION_REQUIRED`. It must not route generically to reconstruction, `/fix`, or candidate authoring. A closure-review `APPROVED_FOR_CANDIDATE_PROJECTION` result establishes projection eligibility for that exact closure artefact only; actual candidate authoring still requires separate current authority.
   - If the current context is genuinely fresh for that decision → [Fresh independent review](fresh-independent-review.md). Reconstruct the decision from the actual review target and evidence rather than inheriting the authoring conclusion; bind candidate identity additionally when the target is a candidate. Freshness is about the context/evidence boundary; it does not require a different GitHub account unless repository-local policy explicitly requires a distinct reviewer identity.
   - If the current context is not genuinely fresh, do not review in it. Resolve whether the execution surface can establish an eligible genuinely isolated review context whose information boundary excludes author-side substantive adjudication and expected conclusion. If yes, invoke [Fresh independent review](fresh-independent-review.md) there using the minimal durable review target or equivalent reconstruction reference. The receiving context must independently bootstrap applicable authority, reconstruct the exact review target/checks-or-evidence/review state, bind candidate identity when applicable, operate only under the bounded `/review` capability profile, and return a disposition/evidence record bound to the exact review target inspected. If isolation is unavailable, ambiguous, unprovable, incompatible with repository policy, or would require broader capability than `/review` permits → [Next-session handover](next-session-handover.md). Only when no eligible/provable isolated review context is available should the existing fresh-context review handoff be produced and the route stop as `EXTERNAL_REQUIRED`.
   - Fresh-review context resolution is an information-boundary mechanism, not an execution-locality class. Do not probe `connected/native`, `hosted/hermetic`, or owner-local execution merely to create reasoning independence. Creating/selecting a context is not authority, and a delegated context must not simulate a repository requirement for another human or formal reviewer.

4. **A newly supplied bounded approval or execution authority applies to the current proposal or action** → [Autonomous progression](autonomous-progression.md).
   - Identify the exact proposal or action being authorised. An unambiguous response to the current decision capsule, such as `A`, `accept`, `choose B`, or an equivalent natural-language/voice response, may supply that authority or choice.
   - Refresh decision-critical state and verify that the proposal/action and its authority boundary remain materially unchanged.
   - Consume the approval or authority once, only for that bounded object, then continue routine governed work through autonomous progression.
   - Do not treat approval as authority to expand scope, weaken controls or accept a materially changed proposal. Escalate a genuinely new human choice as `DECISION_REQUIRED`.

5. **A substantive repository documentation assessment is needed and representative reader tasks must be discovered, validated, or assessed together** → [Documentation assessment workflow](documentation-assessment.md).
   - Use this route for broad documentation-quality assessment, navigation or authority problems, or deciding the smallest justified documentation response when reader/task discovery or multi-task validation is part of the work.
   - Do not route ordinary bounded documentation edits, known corrections or explicit drafting tasks through assessment merely because documentation is involved.
   - If one concrete reader task is already known and no multi-task discovery or validation is needed, use [Repository documentation assessment](../documentation/repository-assessment.md) as the proportionate single-task path.

6. **Ordinary governed continuation** → [Autonomous progression](autonomous-progression.md).
   - Continue while current policy, evidence, scope and available capabilities safely determine the next action.

7. **No safe route fits** → fail closed.
   - Do not invent work, authority or a workflow mapping merely to keep moving.
   - Use the terminal-state rules below to identify the real boundary.

## Single-maintainer repositories

A single-person project may preserve independent review by using a genuinely fresh context while reusing the same repository owner/GitHub identity. Do not equate a distinct reviewer account with a fresh reasoning context unless repository-local policy, branch protection, regulation, or explicit task authority actually requires distinct identities.

When same-account PR authorship is already established, the repository is operating under the Promptbook single-maintainer model, and no repository-local policy, branch protection, regulation, or explicit task authority requires a distinct reviewer or formal approval status, do not attempt a formal self-`APPROVE` or self-`REQUEST_CHANGES` that the hosting platform cannot record. When review write-back is active, record the exact `APPROVED` / `CHANGES REQUIRED` disposition and concise rationale through a permitted `COMMENT` review or durable repository-local comment, make clear that record is not formal platform review state, then continue the governing workflow according to existing authority. When read-only review is active, do not create that fallback record. That platform limitation is not a terminal state by itself; when it is already known, avoid the pointless failed call rather than using the failure as discovery. If those preconditions are not established, or a stronger rule requires formal or distinct-person approval, preserve that requirement and fail or hand off rather than assuming the single-maintainer fallback. Do not invent another account, fake formal approval, or bypass a rule that genuinely requires a formal or distinct-person approval.

For an intermediate `CHANGES REQUIRED`, perform an objectively determined, already-authorised minimum-safe remediation, required validation, and the proportional author-side remediation-readiness sweep before stopping. Freeze the exact resulting candidate only when validation and readiness evidence are current for that same identity. A bounded sibling defect discovered by the sweep may remain in the same remediation cycle only when its correction is still attributable to the resolved remediation scope and passes the `/fix` action gateway; otherwise return to the existing authority/design/escalation routing. The context that performs that remediation and readiness work is no longer fresh for the changed candidate, so route the exact frozen candidate to a new genuinely fresh context; when an eligible isolated review context can be established automatically, use it, and otherwise use the existing manual fresh-context fallback. That new fresh context may still operate through the same maintainer account. For `APPROVED`, continue already-authorised merge, verification and close-out even when a formal self-approval cannot be recorded, unless repository rules make that formal status a real prerequisite.

## Decision capsules

When a genuine human decision is required, do not end with a repository identifier or approval sentence the user must copy. Present the smallest concrete decision as a compact recommendation-first **decision capsule**.

For multiple meaningful alternatives, use compact option labels:

```text
DECISION_REQUIRED — Deployment mechanism

Recommended: A

A — GitHub Actions + Workload Identity
B — Cloud Build
C — Defer
```

For approval of one bounded proposal, use semantic choices rather than manufacturing A/B/C:

```text
DECISION_REQUIRED — Apply repository protection?

Recommended: ACCEPT

ACCEPT — Apply the approved bounded settings
REJECT — Do not apply them
CHANGE — Revise the proposal
```

Put recommendation and choices first. Add material authority, risk, or governance detail below the choices only when it affects the decision.

The canonical response protocol is semantic intent, not slash-command syntax:

- `ACCEPT` — accept the recommended bounded option;
- `REJECT` — reject only the presented proposal or choice;
- `CHOOSE <option>` — select a presented option;
- `CHANGE <instruction>` — request a revision without approving the revision.

Clear natural-language, short-form, touch, or voice equivalents may express the same intent when exactly one unresolved decision and its referent are unambiguous. Examples include `A`, `Choose A`, `yes`, `go ahead`, `accept the recommendation`, or naming the option directly. Slash aliases may be understood as conveniences, but they are not the protocol and are not added to the public shorthand-command vocabulary.

Bind every capsule to one concrete unresolved decision and the authoritative proposal/evidence needed to interpret it: the decision target, proposal or revision identity, recommendation, and bounded authority/effect of acceptance. The user should not normally need to repeat those identifiers.

Before consequential mutation after `ACCEPT` or `CHOOSE`, refresh decision-critical state. If the proposal materially changed, do not silently migrate the earlier response to the new proposal; re-present the decision. Consume accepted authority once for the bounded object only, then resume governed autonomous progression immediately when existing authority permits it.

`REJECT` does not implicitly close the issue, abandon the objective, undo prior work, or choose another option. Re-route from the changed decision state and present another recommendation when one is safely determined. `CHANGE` requests revision; after revising, re-present the decision unless the user's wording explicitly grants authority for the revised proposal.

If more than one unresolved decision exists, or a short response such as `yes`, `A`, or `accept` has more than one plausible referent, fail closed rather than guessing. Repository-local policy, validation, security controls, branch protection, and explicit task authority continue to take precedence.

See [Decision capsules](../../guides/decision-capsules.md) for the device-neutral interaction pattern and examples.

## Terminal states

A routed task should end only as one of these states:

- `EXTERNAL_REQUIRED` — the next required action cannot legitimately be performed inside the eligible governed mechanism/context available to the current workflow, existing authority is sufficient, and one concrete complete external action can resolve it. For human-operated execution, resolve execution locality proportionately before selecting this state; one unavailable preferred mechanism is not enough when another already-governed no-widening locality can truthfully perform the same action. For genuinely fresh review, first resolve whether an eligible genuinely isolated review context can be established automatically; only when isolation is unavailable or unprovable does the existing manual fresh-context hand-off reach `EXTERNAL_REQUIRED`. Fresh-review context resolution remains distinct from execution locality. For human-operated execution, return the required external action explicitly in the same response: provide a complete copy/paste script or exact commands when appropriate, otherwise exact browser/UI steps or another step-by-step procedure; include material prerequisites, guards, cleanup/prohibitions, and the exact evidence/output the human should return. Do not merely name the missing capability or receiving context, and do not make the human ask how to continue.
- `DECISION_REQUIRED` — a genuine human judgement or authority decision is required; present it as a recommendation-first decision capsule.
- `BLOCKED` — no safe autonomous action, eligible execution locality, eligible isolated review context where required, complete executable external handoff or concrete human decision can resolve the condition now.
- `COMPLETE` — the governed objective is genuinely finished, including required verification and close-out.

Review readiness, validation results, PR readiness, merge readiness and ordinary next actions are not terminal states by themselves.

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

## Selection and continuation rules

- Select one primary workflow rather than concatenating the prompt set.
- Refresh material current state before consequential actions.
- Preserve repository-local authority, validation requirements, security boundaries and explicit task constraints.
- Treat access or capability as distinct from permission.
- Prefer the minimum safe change and fail closed when decision-critical evidence is missing.
- Do not ask for routine `proceed` confirmations when existing authority and evidence already determine the safe action.
- When a required independent review cannot run in the current context because that context authored or materially shaped the review target or candidate, first resolve an eligible genuinely isolated review context. Supply only the minimal durable target/reconstruction reference, require independent bootstrap and review-target/evidence reconstruction, constrain the child to the ordinary `/review` operation ceiling, and bind the result to the exact review target inspected, with candidate identity additionally bound when applicable. Do not pass author-side substantive conclusions or hidden reasoning as review evidence. If isolation cannot be proved, repository policy requires a distinct human/formal reviewer, or the child would require broader authority, preserve the manual fresh-context fallback or stronger policy boundary. Do not retry an equivalent failed delegation indefinitely while the relevant target/isolation/capability state is unchanged.
- When human-operated `EXTERNAL_REQUIRED` is being considered for an already-authorised action, first resolve whether an eligible connected/native, hosted/hermetic, or bounded owner-local executor can truthfully perform the same action without widening projected capability. Inspect only authoritative repository/task execution surfaces relevant to that action; prefer established maintained capabilities over generated shell transport. If another eligible locality exists, use it instead of handing the operation to the owner. If the action genuinely depends on owner-local/private state and no bounded executor can perform it, or no other governed locality can truthfully establish the required result, then use the complete external-action rules below. Do not use locality selection to bypass configured capability suppression, stale guards, profile denial, or missing authority. Fresh-review context resolution is separate and is not part of this locality ladder.
- When `EXTERNAL_REQUIRED` applies, reduce the human role to performing one explicit external action and returning its requested evidence. Scripts or command sequences presented as executable must be complete and self-contained for the stated operation; never expose secret values or present a truncated fragment as the handoff. If an equivalent valid external handoff is already durable and decision-critical state has not materially changed, reuse it after refreshing stale-able guards instead of repeating capability discovery. A capability limitation with sufficient authority is not itself `DECISION_REQUIRED`; if the safe external procedure cannot be determined completely, surface the real decision or blocker instead of a vague handoff.
- Treat an unambiguous returned external observation such as `PASS` or `FAIL <material defect>` only as evidence for the named check, never as new mutation, merge, production, close, or acceptance authority. After such evidence returns, resume the governing workflow automatically when existing authority already determines the next action; before any consequential mutation, refresh only the decision-critical state capable of invalidating that evidence or action. Do not delegate already-established machine-verifiable checks to the human. On `FAIL`, preserve fail-closed behaviour and route the defect through the existing governed scope and authority rather than treating the observation as acceptance.
- When `DECISION_REQUIRED` applies, present the decision capsule instead of making the user copy an approval phrase or repository identifier. Once an unambiguous `ACCEPT` or `CHOOSE` response is safely bound and refreshed, continue any already-authorised routine work without another `proceed` confirmation.
- Output or deliverable constraints inside a selected workflow apply to that workflow's record. They do not override this router's continuation semantics. After recording the local workflow result, return control to the router and apply the effective continuation mode unless a higher-precedence hard constraint or explicit current-user qualifier requires stopping.
- A fresh review disposition does not itself create mutation authority beyond the review-record write already intrinsic to an ordinary `/review`. When fresh review is an intermediate gate under this router, record its single clear disposition and concise rationale according to the selected write-back/read-only mode, then return control to the governing workflow. For `REVIEW_TYPE=ARCHITECTURE_CLOSURE`, `APPROVED_FOR_CANDIDATE_PROJECTION` is evidence that separately authorised candidate projection may consume the exact reviewed closure artefact; it is not candidate approval or mutation authority. `CHANGES_REQUIRED` keeps `CLOSURE_REVIEW_REQUIRED` unsatisfied and returns to closure revision/reconstruction rather than `/fix`. If a delegated fresh reviewer was used, refresh the exact review target and review state before continuation, plus the candidate identity when applicable, and discard stale review evidence if any decision-critical target binding moved. If `CHANGES REQUIRED` identifies a bounded defect whose minimum-safe remediation is objectively determined and already authorised, continue through autonomous progression to remediate it, run required validation, complete the proportional remediation-readiness sweep, and freeze the exact review-ready candidate without another routine approval. If the sweep discovers a bounded sibling defect, keep it in that same remediation cycle; if it discovers a broader authority/design boundary or stronger escalation evidence, return to the existing routing rules instead of widening `/fix`. Because that context authored or materially shaped the changed candidate and readiness evidence, route the resulting candidate to a genuinely fresh review context before any gate requiring independence. A single-maintainer project may use the same GitHub identity in that new fresh context. If the disposition is `APPROVED`, continue already-authorised merge, verification and close-out work rather than stopping at review completion or at a platform refusal to record formal self-approval, unless repository-local rules make that approval status mandatory.
- A requested handover is terminal for the current deliverable; execution belongs to the receiving context.
- Do not invent adjacent work after the governed objective is complete.

## Current workflows

- [Autonomous progression](autonomous-progression.md) — continue already-governed work with minimal human orchestration.
- [Bounded concern lifecycle](bounded-concern-lifecycle.md) — orchestrate explicitly selected finite concern-specific closure packages and empirical convergence without claiming universal semantic completeness.
- [Documentation assessment workflow](documentation-assessment.md) — discover and approve representative reader tasks, then continue a substantive documentation assessment with a pinned external method.
- [Fresh independent review](fresh-independent-review.md) — reconstruct and adjudicate a candidate from a genuinely fresh context, including when an eligible isolated review context is delegated by the governing workflow.
- [Assess risk](assess-risk.md) — characterise material risk and legitimate disposition boundaries without accepting risk or manufacturing authority.
- [Reflect on completed work](reflect-on-work.md) — extract justified retrospective lessons without turning self-assessment into review evidence.
- [Challenge assumptions](challenge-assumptions.md) — adversarially test assumptions or governing models without turning challenge into approval.
- [Next-session handover](next-session-handover.md) — create the shortest safe continuation prompt for another context or capability boundary, retaining manual fresh-review context transport as the fallback when automatic isolation cannot be established.
- [Stateful invariant analysis](stateful-invariant-analysis.md) — reconstruct materially stateful invariant/lifecycle semantics read-only, including mandatory escalation after repeated materially related review failures.
