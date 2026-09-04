# Resolved agent run context

## Purpose

Define the reusable Promptbook contract for deriving the effective execution state of a governed agent operation from current authoritative inputs. The explicitly supported operations are `/review`, `/fix`, and `/go`, each with its own capability and lifecycle profile under one common authority/evidence model.

Promptbook is the canonical owner of this workflow contract. The context is ephemeral derived state, not a new durable authority source and not a replacement for repository-native instructions, issue or pull-request authority, immutable Git identity, CI evidence, accepted decisions, or other durable records.

## When to use

Use this contract before substantive `/review` adjudication, before substantive `/fix` mutation, and before substantive `/go` lifecycle progression so the operation executes from explicit repository/work authority, relevant immutable identity, capability boundaries, instruction provenance, current lifecycle state, and required evidence rather than remembered conversation state.

An operation may reuse the common model only when its own authority and capability semantics are deliberately defined here. Supporting one profile does not generalise another operation's permissions.

## Prompt

```text
Before substantive governed execution, resolve an ephemeral Resolved Agent Run Context from current authoritative inputs for the selected operation.

Bind the operation to the repository, governing work identity, immutable candidate or lifecycle identity where applicable, resolved authority sources, applicable repository instructions and their provenance, effective and prohibited capabilities, owner-decision boundaries, and required evidence.

For `/fix`, also bind the starting candidate, remediation scope, required validation, and candidate transition before substantive mutation.

For `/go`, also bind the governing objective, current lifecycle state, current candidate and review disposition where applicable, continuation mode, proposed next governed action, required preconditions, required evidence, and completion conditions. Before every consequential `/go` transition, classify the exact proposed action through the `/go` action gateway and execute only an `ALLOW` action that remains executable after refreshing decision-critical state.

Treat the resolved context as derived execution state rather than a new authority source. Do not fill missing authority or evidence from conversation memory. Technical capability availability may only narrow executable capability; it must never create authority. When an applicable Promptbook capability-availability key is relevant to a `/fix` or `/go` action, resolve it once after action-authority classification using the capability-availability contract and attach that resolved record to the derived run state rather than letting downstream consumers rediscover configuration independently.

For an authorised `/go` action whose initially selected mechanism is unavailable or genuinely insufficient, resolve execution locality before selecting a human-operated `EXTERNAL_REQUIRED` hand-off. Prefer an eligible connected/native mechanism, then governed hosted/hermetic execution when the required truth does not depend on owner-private state, then a separately governed bounded owner-local executor when owner-local/private state is genuinely decision-critical. Locality selection may narrow mechanism and projected capability only; it must never create authority, bypass configured suppression, or widen credentials, network, mutation, or other effect boundaries.

Use the operation-specific capability profile and lifecycle below. Collect bounded reconstructable evidence, distinguish static observation from executed and durable evidence, and bind candidate- or result-specific evidence to the immutable state for which it was actually observed.
```

## Core rule

A governed operation must execute from explicit, reconstructable authority and capability state rather than treating the conversation transcript as executable state.

The conversation may carry intent and navigation, but correctness must be reconstructable from current authoritative sources. Prior summaries and remembered conclusions are navigation aids only when the underlying authority or evidence can be refreshed directly.

A technically available connector, shell, API, credential path, or other tool is not authority:

```text
tool available
    ≠
action authorised
```

For lifecycle progression, preserve the stronger distinction:

```text
candidate approved
    ≠
merge authorised
    ≠
release authorised
    ≠
deployment authorised
    ≠
production mutation authorised
```

Authority or acceptance for one consequential transition must not silently become authority for a later transition.

## Inputs

Resolve the context from the authoritative inputs that apply to the operation. At minimum, consider:

- platform safety and explicit current-user authority;
- the Promptbook workflow selected for the operation;
- repository-local instructions and mandatory policy;
- the governing issue, pull request, design, specification, accepted plan, review finding, accepted decision, or other work-item authority;
- the immutable candidate being reviewed or remediated, or the current lifecycle/result identity being progressed, where applicable;
- current CI, checks, review state, branch/repository policy, and other decision-critical durable evidence.

Conversation history may help locate those sources, but it is not a substitute for refreshing them when correctness depends on current state.

Resolve the context from current authoritative inputs in precedence order appropriate to the repository and operation. Record enough provenance to identify where each applicable instruction or material rule came from. A resolved context does not create authority absent from those sources.

If a required authority source cannot be resolved, fail closed or hand off according to the governing workflow rather than filling the gap from conversation memory.

The representation may be textual or structured. It need not be committed for every run. Whatever representation is used, equivalent authoritative inputs must resolve to equivalent effective authority, relevant identity, capability boundaries, and evidence requirements for the same operation.

## Capability-availability integration

When a material `/fix` or `/go` action has an explicit Promptbook capability-availability key, resolve availability only after the exact action has passed the operation's authority gateway. Use [Capability availability overrides](capability-availability-overrides.md) to derive one record equivalent to `resolved_capability_availability` for the current repository/work/action identity.

The ordering is:

```text
resolve repository/work/action authority
    → classify the exact action through the operation gateway
    → resolve capability availability once
    → derive effective executable capability
    → resolve execution locality when the current mechanism is unavailable or insufficient
    → execute directly or project to an eligible executor
```

That availability record is derived execution state, not a new authority source. Autonomous progression and executor projection consume the same resolved record and its provenance; they must not independently search Project instructions, repository instructions, work items, or prior conversation for another value. If a decision-critical carrier changes, invalidate the affected derived availability state and re-resolve it before consequential use.

Execution-locality resolution consumes the already-classified action and any applicable availability result. It does not reinterpret availability as authority and must not route around an explicitly disabled logical capability by relabelling the same suppressed effect through another executor or locality.

## `/review` required context

For `/review`, resolve at least:

```text
operation
repository_identity
work_item_identity
immutable_candidate_identity
resolved_authority_sources
applicable_repository_instructions
effective_capabilities
prohibited_capabilities
owner_decision_boundaries
required_evidence
```

## Immutable review candidate

Where the review target has an immutable Git identity, bind the context to the exact candidate commit or equivalent immutable revision actually inspected.

Candidate-specific review authority and evidence are valid only for that candidate. If the candidate identity changes, invalidate the prior candidate-specific context and re-resolve before relying on earlier findings or publishing a review disposition.

Immediately before review publication, refresh the candidate identity and reconcile any movement. Never publish a stale candidate-specific disposition merely because the conversation still contains the earlier conclusion.

## Review capability profile

For `/review`, the effective capability model is logically equivalent to:

```text
ALLOW
- repository read
- issue / PR read
- review-comment read
- CI / check evidence read
- other explicitly authorised read-only evidence collection

FORBID
- repository mutation
- branch mutation
- PR mutation except the review-record publication explicitly authorised by the governing `/review` mode
- merge
- release
- unrelated external execution

BOUNDARY
- any action requiring authority beyond the resolved review context requires an explicit owner decision or other separately established authority
```

Access and permission are distinct. A tool being technically available does not add it to `effective_capabilities`.

Where an execution substrate can enforce capabilities, intersect the resolved operation capabilities with a read-only review profile:

```text
review_capabilities =
    resolved_capabilities
    ∩
    READ_ONLY_REVIEW_CAPABILITIES
```

Ordinary router `/review` may additionally carry only the narrow review-publication capability already defined by the router. `/review --read-only` carries no review-record mutation capability.

## `/fix` required context

Before substantive `/fix` execution, resolve at least:

```text
operation
repository_identity
work_item_identity
starting_candidate_identity
resolved_authority_sources
applicable_repository_instructions
remediation_scope
effective_capabilities
prohibited_capabilities
owner_decision_boundaries
resolved_capability_availability
required_validation
required_evidence
```

`resolved_capability_availability` is required only when the current material action has an explicit availability key; otherwise its absence is explicit and carries no meaning.

`starting_candidate_identity` is the immutable reviewed candidate or equivalent revision to which the blocking findings and remediation authority apply. `remediation_scope` is derived from the governing findings, task/design, accepted plan where applicable, repository instructions, and explicit current authority. It is not inferred merely from what a tool could change.

`available_capabilities` and `authority_derived_capabilities` may be retained as intermediate derived sets when useful for reconstruction, but they are not new authority sources.

## `/fix` capability derivation

Derive `/fix` capability as monotonic narrowing:

```text
effective_fix_capabilities =
    technically_available_capabilities
    ∩
    authority_derived_capabilities
    ∩
    FIX_OPERATION_CEILING
```

Technical availability can only remove executable capability; it cannot grant authority. Authority derived from current repository/task/user sources can authorise actions only within the `/fix` operation ceiling. Delegation or an external execution substrate may narrow the set further but must never widen it.

For a named availability-controlled capability, apply the already-resolved configured availability as an additional narrowing after action-authority classification. A disabled or conservatively unresolved record removes executable capability but does not alter the action's authority classification.

The `/fix` operation ceiling is logically equivalent to:

```text
ALLOW
- repository/work-item reads required for the remediation
- bounded implementation mutation attributable to the resolved remediation scope
- work-branch/candidate mutation required to produce the remediated candidate
- PR/work-item update required to publish the resulting candidate or evidence when that publication is already authorised by the governing workflow
- validation and evidence collection required by repository authority

FORBID
- merge
- release or tag publication
- deployment
- unrelated repository mutation
- infrastructure or provider mutation unless separately authorised by another governing contract
- repository settings, credential, or secret mutation unless separately authorised by another governing contract
- expansion of remediation scope merely because a tool is available

BOUNDARY
- any action beyond the governing remediation authority requires an explicit owner decision or separately established authority
```

A capability that exists in the environment but is outside the resolved authority or the operation ceiling is not an effective `/fix` capability.

## `/fix` action gateway

Before every material `/fix` action, classify its authority using this precedence:

```text
1. If higher-precedence authority or the /fix operation ceiling prohibits it:
   FORBID

2. Else if the action is not attributable to the resolved remediation scope,
   or it requires missing product, architecture, security, scope, owner,
   or other separate authority:
   REQUIRE OWNER / SEPARATE AUTHORITY

3. Else if current authoritative sources permit it within the resolved
   remediation scope:
   ALLOW

4. Missing or ambiguous authority never defaults to ALLOW.
```

`FORBID` means the action cannot be performed under the resolved `/fix` authority. It does not claim that a later, independently established governing contract could never authorise an otherwise permissible action.

Keep authority classification separate from execution feasibility. If an action is `ALLOW` but the required execution capability is unavailable, do not reclassify it as `REQUIRE OWNER / SEPARATE AUTHORITY` merely because a tool is missing. Follow the governing router's capability/external-action boundary without broadening authority. Likewise, technical availability never changes an unauthorised action into `ALLOW`.

## `/fix` candidate transition

Treat remediation as a transition between immutable candidate identities rather than changing one candidate context in place:

```text
FixRunContext(A)
    + authorised bounded actions
    → remediation
    → FixResult(B, delta, validation, evidence, remaining boundaries)
```

`starting_candidate_identity` belongs to the resolved pre-mutation context for candidate A. `resulting_candidate_identity` belongs to the remediation result after candidate B exists.

Immediately before the first material write, refresh the expected starting candidate. If the candidate identity changes, invalidate the stale candidate-specific context and re-resolve before applying findings to unexpected bytes. If unexpected external candidate movement is detected during remediation, fail closed and reconcile/re-resolve before continuing.

Once changed bytes produce candidate B, prior candidate-specific review and validation attached to candidate A expire for B. They may remain historical evidence about A, but they must not silently transfer as review or validation of B.

Run the required validation against candidate B and bind the observed result to `resulting_candidate_identity`. Where the governing workflow requires fresh substantive review, the context that authored or materially shaped B must preserve that fresh-context boundary rather than reviewing B as independent evidence.

## `/fix` remediation result

The resulting remediation record or hand-off should be reconstructable as the logical equivalent of:

```text
governing_finding_or_remediation_authority
starting_candidate_identity
bounded_implementation_delta
resulting_candidate_identity
validation_and_evidence
remaining_boundaries
next_governed_state
```

The record should make clear which material actions were `ALLOW`, which proposed actions were `REQUIRE OWNER / SEPARATE AUTHORITY` or `FORBID`, and which authorised actions could not be executed because of a capability boundary.

## `/go` required context

Before substantive `/go` progression, resolve at least:

```text
operation
repository_identity
governing_objective_identity
current_lifecycle_state
current_candidate_identity
current_review_disposition
resolved_authority_sources
applicable_repository_instructions
effective_capabilities
prohibited_capabilities
owner_decision_boundaries
resolved_capability_availability
resolved_execution_locality
continuation_mode
next_governed_action
required_preconditions
required_evidence
completion_conditions
```

`resolved_capability_availability` is required only when the current proposed action has an explicit availability key. It must be the same resolved record consumed by autonomous progression or executor projection, not a separately rediscovered value.

`resolved_execution_locality` is derived execution state for the exact authorised action. It may resolve directly to `connected/native` when the current governed mechanism is sufficient. When the initial mechanism is unavailable or insufficient, it must retain enough evidence to show which eligible locality was selected or why owner-operated execution is genuinely required. It is not an authority source and must be invalidated when decision-critical action, state, availability, projection, or execution-constraint inputs change.

`governing_objective_identity` should normally identify the lifecycle object that can reconstruct the complete governed objective, such as the governing issue, rather than collapsing `/go` onto one intermediate pull request when post-merge verification or close-out remains part of the objective.

`current_candidate_identity` and `current_review_disposition` may be absent when the current lifecycle state has no candidate/review concept, but their absence must be explicit rather than silently filled from conversation memory.

`next_governed_action` is a proposed transition, not permission to execute it. The exact action must still pass the `/go` action gateway immediately before consequential execution.

## `/go` capability derivation

Derive `/go` capability by monotonic narrowing:

```text
effective_go_capabilities =
    technically_available_capabilities
    ∩
    authority_derived_capabilities
    ∩
    GO_OPERATION_CEILING
```

Technical availability may remove executable capability but must never grant authority. Delegation or an external executor may narrow the effective set further but must never widen it.

For a named availability-controlled capability, apply the already-resolved configured availability as an additional narrowing after the action gateway returns `ALLOW`. Do not let availability manufacture an `ALLOW` classification or an owner decision.

Execution-locality selection occurs only after the exact action is `ALLOW` and applicable availability has narrowed the executable set. Choosing another locality or executor may further narrow the mechanism, constraints, or projected capability, but must never add a capability absent from `effective_go_capabilities` or reinterpret the same explicitly suppressed logical effect as available.

`GO_OPERATION_CEILING` is an upper bound on what `/go` may execute; it is not an authority grant. A capability category is effective only when current authoritative sources separately permit the exact action within the governing objective.

The ceiling may admit, when separately authorised and otherwise permitted:

```text
ELIGIBLE ONLY WHEN SEPARATELY AUTHORISED
- repository/work-item reads required for progression
- routine lifecycle metadata updates within the governing objective
- branch/PR state transitions already authorised by the governing workflow
- merge of the exact candidate when merge authority is independently established
- required post-action validation and evidence collection
- issue/work-item close-out when governing completion conditions and close-out authority are satisfied
- continuation into another Promptbook workflow when current authority and continuation mode permit it
```

The existence of `/go`, a successful prior workflow, or technical capability must not intrinsically grant:

```text
NOT INTRINSICALLY AUTHORISED
- merge
- release or tag publication
- deployment
- infrastructure or provider mutation
- repository settings changes
- credential or secret mutation or use beyond separately established authority
- production-data mutation
- destructive actions
- material cost commitments
- unrelated scope expansion
```

A separately governed contract may authorise an otherwise permissible consequential action, but `/go` must resolve and consume that authority explicitly for that action; it must not infer it from an earlier approval or from tool availability.

## `/go` action gateway

Before every consequential lifecycle transition, classify the exact proposed action using this precedence:

```text
1. If higher-precedence authority or the /go operation ceiling prohibits it:
   FORBID

2. Else if current authority is insufficient, ambiguous, stale, or requires a
   genuine owner/product/architecture/security/scope decision:
   REQUIRE OWNER / SEPARATE AUTHORITY

3. Else if current authoritative sources permit the exact action within the
   governing objective:
   ALLOW

4. Missing or ambiguous authority never defaults to ALLOW.
```

`FORBID` means the action cannot execute under the current `/go` contract. `REQUIRE OWNER / SEPARATE AUTHORITY` means the action may be legitimate but current resolved authority is insufficient for it. `ALLOW` means the exact action is authorised within the current objective, subject to execution feasibility and refreshed preconditions.

Keep authority classification separate from execution feasibility. If an action is `ALLOW` but the initially selected execution capability is unavailable or genuinely insufficient, preserve the capability / `EXTERNAL_REQUIRED` boundary without jumping directly to owner-operated execution: resolve another eligible execution locality before selecting a human-operated `EXTERNAL_REQUIRED` hand-off. Technical availability never changes an unauthorised action into `ALLOW`, and changing locality never widens the action's resolved authority.

## `/go` execution-locality resolution

Execution locality answers where the exact already-authorised action can be performed truthfully and safely; it does not answer whether the action is authorised.

Resolve proportionately after action-gateway `ALLOW` and applicable capability-availability narrowing:

```text
exact action = ALLOW
    → current/equivalent governed connected/native capability sufficient?
        → yes: execute and observe
        → no
    → governed hosted/hermetic execution can establish the required truth/effect?
        → yes: project only the existing authorised subset, execute and observe
        → no
    → does correctness genuinely depend on owner-local/private state?
        → no: preserve the capability/execution-design gap; do not default to owner shell transport
        → yes
    → separately governed bounded owner-local executor exists and is eligible?
        → yes: project only the existing authorised subset, execute and observe
        → no: human-operated EXTERNAL_REQUIRED may be selected when a complete safe hand-off exists
```

The portable locality classes are:

- `connected/native` — a current or equivalent governed connected capability that can perform and verify the exact action;
- `hosted/hermetic` — governed execution whose correctness can be established from explicit or remotely available inputs without owner-private state; and
- `owner-local/bounded-executor` — a separately governed bounded executor used only when a material dependency genuinely requires owner-local/private state.

Human-operated external execution is a terminal hand-off mechanism after locality resolution, not a fourth executor class and not a preferred fallback merely because one connector is unavailable.

Before generating a substantial human-operated hand-off, inspect proportionately only the authoritative repository/task execution or operator surfaces relevant to the action. Prefer an established maintained capability that expresses the same bounded effect, with invocation-specific identities and expectations supplied as typed arguments or data. Do not search arbitrary files for executables, invent a global capability registry, or manufacture a broad shell/argv escape hatch.

Owner-local/private dependence must identify the decision-critical fact or effect that cannot truthfully be established elsewhere. Valid examples can include local filesystem or working-copy state, private authenticated provider context, local-only tooling or state, browser/session-local state not safely exposed elsewhere, or another explicitly established private dependency. Historical convenience, habit, or the previous use of an owner shell is not evidence that owner-local execution is required.

Locality re-resolution is fail closed:

- `PROFILE_DENIED` or equivalent authority/projection denial is not worked around by choosing another executor;
- `CAPABILITY_DISABLED` or equivalent configured suppression is not bypassed by relabelling the same logical effect through another locality;
- `EXECUTOR_UNSUPPORTED`, `UNAVAILABLE`, or equivalent execution unavailability may cause re-resolution only among localities already compatible with current authority, availability, projection and execution constraints;
- `STALE_PROFILE` or `GUARD_MISMATCH` requires decision-critical state refresh before another consequential attempt; and
- an alternate locality that needs broader credentials, network reach, mutation authority, provider access, or another wider effect is ineligible unless that broader effect is independently authorised and within the current operation ceiling.

Do not retry the same unchanged failed locality indefinitely. Retain enough bounded evidence about attempted or excluded localities to avoid an execution loop and to distinguish a genuine owner-local requirement from an unresolved capability gap.

## `/go` bounded approval consumption

A human `ACCEPT` or `CHOOSE` decision is an authority input only for the concrete proposal/action presented by the governing decision capsule. It must bind to the exact decision target, proposal identity, candidate or lifecycle identity where relevant, and bounded effect of acceptance.

Before consequential execution after `ACCEPT` or `CHOOSE`, refresh the decision-critical state capable of invalidating that decision. If the candidate, material proposal, applicable policy, required checks, governing authority, or repository instructions have changed so the accepted action is no longer the same valid proposal, invalidate the stale approval and re-present the changed decision rather than migrating authority silently.

Accepted authority is consumed once for that bounded action. In particular:

```text
approved candidate A
    + owner authorises merge of A
    → refresh A / review / checks / authority
    → merge A if unchanged

merge authority for A
    ≠
release authority
    ≠
deployment authority
```

## `/go` lifecycle identity and stale-state invalidation

Treat consequential `/go` progression as explicit transitions between lifecycle states and immutable identities rather than one continuously valid context:

```text
approved candidate A
    → authorised merge
    → merge commit M
    → post-merge validation on M
    → close-out decision/state
```

Candidate-bound review, checks, or other evidence for A do not become post-merge evidence for M merely because the merge succeeded. Bind new observations to the resulting identity for which they were actually observed.

Immediately before a consequential action, refresh the decision-critical inputs capable of invalidating it, including where applicable:

- target/current candidate identity;
- base or governing repository state;
- review disposition;
- required checks/CI;
- branch or repository policy relevant to the action;
- governing issue/task authority;
- the exact accepted proposal/decision;
- applicable capability-availability carrier identity/freshness when the action has a named key;
- resolved execution-locality assumptions or owner-local dependency evidence when they affect the action; and
- materially changed repository instructions.

If those inputs change so the proposed action is no longer valid, invalidate the stale run context or approval and re-resolve before execution. After a consequential transition creates a new material state or immutable identity, bind the result/evidence to that new state and re-resolve before another consequential transition.

## `/go` progression result

A material `/go` step should be reconstructable as the logical equivalent of:

```text
governing_objective_identity
starting_lifecycle_state
proposed_action
action_authority_classification
resolved_capability_availability
resolved_execution_locality
locality_evidence
action_taken
resulting_lifecycle_state
resulting_identity
validation_and_evidence
remaining_boundaries
next_governed_action
```

The record should distinguish proposed actions that were `ALLOW`, `REQUIRE OWNER / SEPARATE AUTHORITY`, or `FORBID`, authorised actions that could not execute because of a capability boundary, and locality decisions that selected or rejected an alternate execution path.

A successful intermediate action is not automatically objective completion:

```text
merge succeeded
    ≠
objective complete
```

`COMPLETE` requires the governing outcome, required post-action verification, completion conditions, and authorised close-out to be satisfied. A failed required post-merge validation therefore prevents `COMPLETE` even when the merge itself succeeded.

## Required evidence

Resolve the evidence necessary to support the requested operation before adjudicating, declaring remediation complete, or treating lifecycle progression as complete. Evidence should be proportionate, bounded, and reconstructable. Depending on the claim, it may include:

- an exact command or tool invocation and result status;
- bounded relevant output;
- a CI or check result bound to the candidate or resulting identity;
- a reproducible test;
- a static source observation;
- an applicable repository-rule or authority citation;
- for `/fix`, the bounded implementation delta and resulting candidate identity;
- for `/go`, the starting state, proposed action, authority classification, applicable availability, resolved execution locality when material, resulting state/identity, validation/evidence, and remaining boundaries.

Do not fabricate executed evidence where only static analysis occurred. Identify static observations as static. If a material claim requires execution that was not performed, represent that absence rather than implying the execution succeeded.

For evidence, distinguish at least:

- `STATIC` — source, configuration, metadata, or rule observation without executing the claimed behaviour;
- `EXECUTED` — a command, test, check, or tool action was actually run and its result observed;
- `DURABLE` — repository-hosted CI, review, check, or other retained evidence was inspected.

A finding, remediation record, or progression record may use more than one evidence class. Do not upgrade one class into another merely to strengthen the conclusion.

## Evidence-bearing review findings

A material review finding should be reconstructable as the logical equivalent of:

```text
claim
affected_code_or_location
applicable_authority_or_rule
observation
evidence
immutable_candidate_identity
priority
confidence
```

The human-facing review may remain concise. It does not need to print a verbose schema for every observation, but the decisive reasoning must retain enough provenance to reconstruct why the disposition applies to the bound candidate.

## What it does

Makes the effective execution state of supported governed operations explicit and reconstructable without introducing a new durable per-run artefact. It separates authority from capability, preserves repository-instruction provenance, and requires honest evidence classes bound to the candidate or resulting state for which they were observed.

For `/review`, it keeps the existing Promptbook review-recording model intact: ordinary router `/review` may publish only the requested review record, while `/review --read-only` remains zero-write.

For `/fix`, it permits only bounded remediation mutation derived from current authority, classifies material actions before execution, distinguishes candidate A from candidate B, and prevents A-specific review or validation from silently carrying forward after bytes change.

For `/go`, it derives effective lifecycle capabilities by monotonic narrowing, classifies every consequential transition through an explicit authority gateway, resolves eligible execution locality before human-operated external fallback, consumes bounded decisions only for their exact effect, invalidates stale state across candidate/result transitions, and prevents a successful intermediate action from being mistaken for completion.

When a named capability-availability key is relevant to `/fix` or `/go`, the run context carries one resolved availability record from Promptbook's deterministic carrier contract so local progression and delegated execution apply the same configuration decision. For `/go`, locality selection consumes that same availability decision and the existing action-specific capability projection rather than rediscovering or widening them.

## `/review` lifecycle

A representative review should be reconstructable as:

```text
production routing
→ resolved repository/work authority
→ immutable review candidate
→ applicable instruction provenance
→ effective review capabilities
→ required evidence resolution
→ evidence collection
→ evidence-bearing findings
→ evidence-backed disposition
```

Before substantive adjudication:

1. resolve the context from current authoritative inputs;
2. verify that the operation is `/review` and identify its recording mode;
3. bind to the immutable candidate where applicable;
4. establish instruction and authority provenance;
5. intersect available capabilities with the review capability boundary;
6. identify the evidence required for a safe disposition.

During review, collect only evidence permitted by the effective capability set and relevant to the governing contract. Before publication, refresh candidate identity and any decision-critical evidence that can stale.

## `/fix` lifecycle

A representative remediation should be reconstructable as:

```text
production routing
→ resolved repository/work authority
→ starting immutable candidate A
→ applicable instruction provenance
→ bounded remediation scope
→ effective/prohibited capabilities
→ pre-action gateway classification
→ resolved capability availability when applicable
→ bounded ALLOW mutations only
→ resulting immutable candidate B
→ B-bound validation/evidence
→ remediation record / remaining boundaries
→ fresh-review boundary or other correct governed next state
```

Before substantive mutation:

1. resolve the `/fix` context from current authoritative inputs;
2. bind the exact governing findings and `starting_candidate_identity`;
3. establish instruction and authority provenance;
4. derive the bounded `remediation_scope`;
5. derive effective/prohibited capabilities by monotonic narrowing;
6. resolve `required_validation` and `required_evidence`;
7. refresh candidate A immediately before the first material write.

During remediation, classify each material action through the action gateway and execute only `ALLOW` actions that are actually available. For a named availability-controlled action, consume the one resolved availability record after the gateway classification. After changed bytes produce B, invalidate A-specific review/validation for B, run the required validation against B, and record the resulting candidate/evidence without crossing a required fresh-review boundary.

## `/go` lifecycle

A representative `/go` progression should be reconstructable as:

```text
production routing
→ resolved governing objective and current lifecycle state
→ current candidate/result identity and review/evidence state where applicable
→ applicable instruction and authority provenance
→ effective/prohibited go capabilities
→ proposed next governed action
→ refresh decision-critical state
→ pre-action gateway classification
→ resolved capability availability when applicable
→ resolved execution locality / eligible mechanism
→ execute one available ALLOW transition only
→ resulting lifecycle state and immutable identity
→ result-bound validation/evidence
→ re-resolve remaining authority and boundaries
→ next governed action or correct terminal boundary
```

Before substantive progression:

1. resolve the `/go` context from current authoritative inputs;
2. bind `governing_objective_identity` and the current lifecycle/candidate/result identity;
3. establish instruction and authority provenance, including any exact accepted decision that applies to the next action;
4. derive effective/prohibited capabilities by monotonic narrowing;
5. resolve the next proposed action, required preconditions/evidence, and completion conditions;
6. refresh decision-critical state immediately before any consequential transition;
7. classify that exact action through the `/go` action gateway;
8. when the action has an explicit availability key, resolve and bind the one applicable availability record before execution/projection;
9. when the current mechanism is unavailable or insufficient, resolve an eligible execution locality without widening authority, availability or projection.

Execute only an `ALLOW` action through an eligible locality that is actually available. If the current mechanism is unavailable, try another already-governed no-widening locality only when it can truthfully establish the required result. Use human-operated `EXTERNAL_REQUIRED` only after no eligible governed locality can perform the action and a complete safe hand-off exists. If owner-local/private state is claimed as necessary, retain the material dependency that makes it decision-critical. If authority is missing or stale, surface the appropriate owner/separate-authority boundary. If higher-precedence policy forbids the action, do not execute it.

After a consequential action, bind resulting evidence to the new state/identity, invalidate evidence that does not transfer, and re-resolve before another consequential action. Preserve fresh-review boundaries and independently gate any later merge, release, deployment, production mutation, or close-out rather than inheriting authority from the prior step.

## Delegation invariant

Future delegated or child execution contexts must never gain authority merely through delegation:

```text
child_authority ⊆ parent_authority
```

An external execution substrate should receive only the resolved authorised subset needed for the delegated action. This contract does not introduce subagent infrastructure or make the substrate a workflow-policy owner.

## Boundaries / limitations

This contract defines `/review`, `/fix`, and `/go` run contexts, but it does not introduce a new Switchboard schema, operating-system or network sandboxing, Guardian-style approval automation, native subagents, agentctl policy ownership, Watchtower workflow ownership, a global executor/capability registry, arbitrary remote shell or argv dispatch, or a universal persisted run-context schema.

It does not intrinsically grant merge, release, tag, deployment, infrastructure/provider, settings, credential, secret, production, destructive-action, material-cost, or unrelated mutation authority. Those actions require separate current authority where they are permitted at all, and `/go` must resolve that authority explicitly before execution.

External mechanisms may enforce capability restrictions or collect evidence, but they do not become owners of Promptbook workflow policy or independent discoverers of Promptbook availability configuration. Execution-locality selection chooses only among already-eligible mechanisms and cannot turn technical reachability into authority.

## Status

`tested`
