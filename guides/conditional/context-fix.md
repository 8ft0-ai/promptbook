# Context Fix

**Conditional contract:** Load for an authorised remediation/validation/readiness/fresh-review transition.

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
remediation_plan
effective_capabilities
prohibited_capabilities
owner_decision_boundaries
resolved_capability_availability
required_validation
remediation_readiness_requirements
fresh_review_boundary_requirement
required_evidence
```

`resolved_capability_availability` is required only when the current material action has an explicit availability key; otherwise its absence is explicit and carries no meaning.

`starting_candidate_identity` is the immutable reviewed candidate or equivalent revision to which the blocking findings and remediation authority apply. `remediation_scope` is derived from the governing findings, task/design, accepted plan where applicable, repository instructions, and explicit current authority. It is not inferred merely from what a tool could change.

`remediation_plan` is the candidate-bound remediation plan required when review-response synthesis has classified the response as `BOUNDED_REMEDIATION`. It binds the source candidate identity, blocker set, material finding relationships or shared invariant, bounded correction, required validation, and explicit scope boundaries that synthesis determined. The plan is authoritative synthesis input to `/fix`, not mutation authority: `/fix` must refresh current state and authority before acting, and must fail closed or return to response routing if the plan is stale, conflicts with current authoritative evidence, or would require a broader correction. When direct `/fix` follows `CHANGES REQUIRED` and no valid remediation plan exists yet, the router must perform the required non-mutating response synthesis before substantive mutation.

`remediation_readiness_requirements` describe the bounded author-side falsification that must complete before a substantive-review remediation candidate can be treated as review-ready. They are derived from the governing contract, complete review finding set and relationship diagnosis, actual changed integration paths, repository instructions, applicable producer/consumer contracts, and any already-required invariant/model artefact. They do not create mutation authority or independent review state. `fresh_review_boundary_requirement` records whether the resulting candidate requires genuinely fresh substantive review and must remain unsatisfied by this authoring/remediation context.

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
    → provisional candidate B0
    → required validation bound to B0
    → remediation-readiness sweep bound to B0
    → [bounded sibling defect still ALLOW] mutate Bn → Bn+1, invalidate affected evidence, revalidate, repeat affected readiness challenges
    → [broader authority/design/escalation boundary] stop mutation and return to routing
    → freeze final exact candidate B only when validation and readiness are current for B
    → FixResult(B, delta, validation, readiness, evidence, remaining boundaries)
```

`starting_candidate_identity` belongs to the resolved pre-mutation context for candidate A. `resulting_candidate_identity` belongs to the remediation result after candidate B exists.

Immediately before the first material write, refresh the expected starting candidate. If the candidate identity changes, invalidate the stale candidate-specific context and re-resolve before applying findings to unexpected bytes. If unexpected external candidate movement is detected during remediation, fail closed and reconcile/re-resolve before continuing.

Once changed bytes produce candidate B, prior candidate-specific review and validation attached to candidate A expire for B. They may remain historical evidence about A, but they must not silently transfer as review or validation of B.

Run the required validation against the current provisional candidate and bind the observed result to that exact identity. Before a substantive-review remediation can become review-ready, complete the proportional remediation-readiness sweep required by the governing workflow. If the sweep discovers another objectively bounded defect whose correction remains attributable to the resolved remediation scope and independently passes the action gateway as `ALLOW`, correct it in the same remediation cycle; that mutation creates a new provisional candidate, invalidates affected prior validation/readiness evidence, and requires affected validation and readiness challenges to be repeated. If the sweep exposes a broader authority/design boundary or an existing stronger escalation trigger, stop mutation and return to routing rather than widening `/fix`.

Freeze `resulting_candidate_identity` only after the current exact candidate simultaneously has current required validation and a completed readiness sweep, with no unresolved material readiness defect inside the applicable surface. Where the governing workflow requires fresh substantive review, the context that authored or materially shaped the final B must preserve that fresh-context boundary rather than reviewing B as independent evidence.

## `/fix` remediation result

The resulting remediation record or hand-off should be reconstructable as the logical equivalent of:

```text
governing_finding_or_remediation_authority
source_review_identity_and_disposition
starting_candidate_identity
bounded_implementation_delta
resulting_candidate_identity
required_validation_bound_to_resulting_candidate
remediation_readiness_surface_and_evidence
remediation_readiness_sweep_complete
exact_resulting_candidate_frozen
fresh_review_boundary_preserved
remaining_boundaries
next_governed_state
```

The record should make clear which material actions were `ALLOW`, which proposed actions were `REQUIRE OWNER / SEPARATE AUTHORITY` or `FORBID`, and which authorised actions could not be executed because of a capability boundary.

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
→ provisional candidate B0
→ B0-bound required validation
→ proportional remediation-readiness sweep
→ bounded ALLOW sibling correction loop with affected evidence invalidation/revalidation when needed
→ exact final candidate B frozen only with current B-bound validation + readiness evidence
→ remediation record / remaining boundaries
→ fresh-review boundary or other correct governed next state
```

Before substantive mutation:

1. resolve the `/fix` context from current authoritative inputs;
2. bind the exact governing findings and `starting_candidate_identity`;
3. establish instruction and authority provenance;
4. derive the bounded `remediation_scope`;
5. derive effective/prohibited capabilities by monotonic narrowing;
6. resolve `required_validation`, `remediation_readiness_requirements`, `fresh_review_boundary_requirement`, and `required_evidence`;
7. refresh candidate A immediately before the first material write.

During remediation, classify each material action through the action gateway and execute only `ALLOW` actions that are actually available. For a named availability-controlled action, consume the one resolved availability record after the gateway classification. After changed bytes produce a provisional candidate, invalidate stale candidate-specific review/validation/readiness evidence, run required validation against the current provisional identity, and complete the proportional remediation-readiness sweep. A sweep-discovered sibling correction may remain in the same cycle only when it is still attributable to the resolved remediation scope and independently passes the action gateway as `ALLOW`; after such a mutation, rebind affected validation and readiness evidence to the new provisional identity before continuing. Freeze the final exact candidate only when required validation and readiness completion are current for that same identity, record the resulting evidence, and do not cross a required fresh-review boundary. Return control to the router so that boundary can be satisfied through an eligible isolated reviewer or, failing that, the existing manual hand-off.
