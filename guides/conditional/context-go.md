# Context Go

**Conditional contract:** Load for consequential /go or /step action-gateway and exact identity decisions; not for passive status-only queries.

## `/go` required context

Before substantive `/go` or `/step` progression, resolve at least:

```text
operation
repository_identity
governing_objective_identity
current_lifecycle_state
current_candidate_identity
current_review_disposition
current_architecture_closure_identity
current_architecture_closure_snapshot_identity
current_closure_review_requirement
current_closure_review_identity
current_closure_review_snapshot_identity
current_closure_review_disposition
resolved_authority_sources
applicable_repository_instructions
effective_capabilities
prohibited_capabilities
owner_decision_boundaries
resolved_capability_availability
resolved_execution_locality
resolved_fresh_review_context
continuation_mode
next_governed_action
required_preconditions
required_evidence
completion_conditions
```

`resolved_capability_availability` is required only when the current proposed action has an explicit availability key. It must be the same resolved record consumed by autonomous progression or executor projection, not a separately rediscovered value.

`resolved_execution_locality` is derived execution state for the exact authorised action. It may resolve directly to `connected/native` when the current governed mechanism is sufficient. When the initial mechanism is unavailable or insufficient, it must retain enough evidence to show which eligible locality was selected or why owner-operated execution is genuinely required. It is not an authority source and must be invalidated when decision-critical action, state, availability, projection, or execution-constraint inputs change.

`resolved_fresh_review_context` is material only when independent review is the next governed gate and the current context is not genuinely fresh. It records the separate isolation/child-review resolution described above. It is not an execution locality and does not create review, mutation or lifecycle authority.

`governing_objective_identity` should normally identify the lifecycle object that can reconstruct the complete governed objective, such as the governing issue, rather than collapsing `/go` onto one intermediate pull request when post-merge verification or close-out remains part of the objective.

`current_candidate_identity` and `current_review_disposition` may be absent when the current lifecycle state has no candidate/review concept, but their absence must be explicit rather than silently filled from conversation memory.

The architecture-closure review fields are material only when current state is on a closure-governed path. `ARCHITECTURE_CLOSURE_READY` sets `current_closure_review_requirement=CLOSURE_REVIEW_REQUIRED` for the exact closure artefact. Candidate projection is not an executable next action until `current_closure_review_disposition=APPROVED_FOR_CANDIDATE_PROJECTION` is current for that same closure identity **and** separate candidate-authoring authority permits projection. A `CHANGES REQUIRED` closure review keeps projection ineligible and must consume the fresh review's route classification: an eligible unused `MODELLED_DEFECT` or `PACKAGE_ONLY_DEFECT` may use its bounded in-generation allowance, while `NEW_OR_OMITTED_OBLIGATION`, `STRUCTURAL_FALSIFICATION`, `SCOPE_OR_AUTHORITY_MOVEMENT`, ambiguous classification, exhausted allowance, or material movement of closure/governing bindings routes to `GOVERNING_DISPOSITION_REQUIRED`. Do not route generically to closure reconstruction or create an equivalent successor generation without a separate governing disposition.

`next_governed_action` is a proposed transition, not permission to execute it. The exact action must still pass the `/go` action gateway immediately before consequential execution. `/step` consumes this same action gateway and stops after one verified transition/re-resolution; `/next`, `/status`, and `/help` may expose or interpret the proposal read-only without executing it.

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
- resolved execution-locality assumptions or owner-local dependency evidence when they affect the action;
- resolved fresh-review isolation/result binding when a delegated review is being relied upon; and
- materially changed repository instructions.

If those inputs change so the proposed action is no longer valid, invalidate the stale run context or approval and re-resolve before execution. After a consequential transition creates a new material state or immutable identity, bind the result/evidence to that new state and re-resolve before another consequential transition. A delegated review disposition bound to candidate A does not transfer to moved candidate A'.

## `/go` progression result

A material `/go` step should be reconstructable as the logical equivalent of:

```text
governing_objective_identity
starting_lifecycle_state
proposed_action
action_authority_classification
resolved_capability_availability
resolved_execution_locality
resolved_fresh_review_context
locality_evidence
action_taken
resulting_lifecycle_state
resulting_identity
validation_and_evidence
remaining_boundaries
next_governed_action
```

The record should distinguish proposed actions that were `ALLOW`, `REQUIRE OWNER / SEPARATE AUTHORITY`, or `FORBID`, authorised actions that could not execute because of a capability boundary, locality decisions that selected or rejected an alternate execution path, and fresh-review context decisions that delegated an eligible independent review or preserved the manual fallback.

A successful intermediate action is not automatically objective completion:

```text
merge succeeded
    ≠
objective complete
```

`COMPLETE` requires the governing outcome, required post-action verification, completion conditions, and authorised close-out to be satisfied. A failed required post-merge validation therefore prevents `COMPLETE` even when the merge itself succeeded.

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
→ resolved execution locality / eligible mechanism when an execution effect is required
→ resolved fresh-review context when independent adjudication is required and current context is non-fresh
→ execute one available ALLOW transition or bounded delegated review only
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
9. when the current mechanism is unavailable or insufficient, resolve an eligible execution locality without widening authority, availability or projection;
10. when independent review is the next gate and the current context is non-fresh, resolve an eligible isolated fresh-review context separately from execution locality and bind the child `/review` projection/result state.

Execute only an `ALLOW` action through an eligible locality that is actually available. If the current mechanism is unavailable, try another already-governed no-widening locality only when it can truthfully establish the required result. Use human-operated `EXTERNAL_REQUIRED` only after no eligible governed locality can perform the action and a complete safe hand-off exists. If owner-local/private state is claimed as necessary, retain the material dependency that makes it decision-critical. If authority is missing or stale, surface the appropriate owner/separate-authority boundary. If higher-precedence policy forbids the action, do not execute it.

When the next gate is independent review, never execute that adjudication in a context that authored or materially shaped the candidate. If an eligible isolated context exists, invoke the bounded `/review` operation there and reconcile the exact-candidate-bound result. If no eligible/provable isolated context exists, use the existing manual fresh-context `EXTERNAL_REQUIRED` hand-off. Do not reinterpret either branch as execution-locality selection.

After a consequential action or delegated review result, bind resulting evidence to the state/identity for which it was observed, invalidate evidence that does not transfer, and re-resolve before another consequential action. Preserve fresh-review boundaries and independently gate any later remediation, merge, release, deployment, production mutation, or close-out rather than inheriting authority from the prior step.
