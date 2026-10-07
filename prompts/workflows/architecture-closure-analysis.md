# Architecture closure analysis

## Purpose

Derive and challenge a decision-critical architecture-closure model whose completeness does not depend on the candidate's own self-defined object, relation, transition or prose universe.

Use this workflow only for materially security-, authority-, identity-, lifecycle-, recovery/ambiguity-, irreversible-effect-, or migration/cutover-sensitive architecture work when current governed state requires architecture closure or reconstruction. It is intentionally stronger than ordinary stateful/invariant analysis and does not replace that proportional workflow for routine stateful defects.

## When to use

Use this workflow when current authoritative evidence establishes one of:

- proposed work is materially security-, authority-, identity-, recovery/ambiguity-, irreversible-effect-, or migration/cutover-sensitive **and** the resulting architecture is intended to claim or be treated as closed-world, architecture-closed, closure-ready, complete over its decision-critical authority/effect universe, or an equivalent strong completeness claim;
- an authorised architecture reconsideration whose result requires an architecture-closure proof before a candidate can safely be treated as closure-ready; or
- `CLOSURE_METHOD_FALSIFIED` / `ARCHITECTURE_CLOSURE_RECONSTRUCTION_REQUIRED` because a fresh substantive review identified an applicable unmodelled decision-critical primitive, relation, authority edge, effect boundary, recovery state, identity dependency, equivalence claim, terminal-provenance requirement or migration/fence obligation that should have been present in the prior closure universe.

The proactive trigger is conjunctive. Do not select this workflow merely because an architecture is large, because a security/authority word appears, because a review found several blockers, or because a modelled element is locally wrong. Ordinary bounded design, local architecture decisions, exploratory proposals and explicitly modelled-but-incomplete drafts remain eligible for proportionate workflows when they do not make the strong completeness claim.

For proactive entry, derive the closure artefact **before** a candidate is authored or published as closure-ready. The candidate must be a projection of the independently derived closure model; it must not define the universe used to prove its own completeness.

Architecture-closure analysis is read-only. It does not create implementation, redesign, remediation, merge, release, deployment, settings, credential, migration, production or other consequential authority.

## Prompt

```text
Perform a read-only architecture-closure analysis of <ANALYSIS_TARGET> against <GOVERNING_CONTRACT>.

Derive a closed decision-critical source/obligation universe independently from the candidate model, derive the primitive universe from it with total source → primitive coverage, construct the applicable global closure artefact, reconcile the exact candidate against it when one already exists, and return the closure disposition and any authority boundary required by this workflow.

For a proactive pre-candidate invocation, return the current closure artefact before closure-ready candidate authoring begins. Do not mutate source, create a design candidate, approve the target, or infer completeness merely from the candidate's own prose, object registry, transition table or known blocker list.
```

## Inputs

- `<ANALYSIS_TARGET>` — the exact architecture candidate, closure artefact, falsifying review, or other durable target being analysed.
- `<GOVERNING_CONTRACT>` — the current governing issue/design/policy/acceptance criteria and authority constraints that define applicable behaviour and closure obligations.

## Core rule

Do not define the closure universe by reading the candidate's headings and then checking that every listed item is internally consistent.

Instead:

1. derive a bounded **source/obligation universe** independently from the candidate by enumerating every applicable governing requirement, externally observable governed consequence/effect class, mutable authoritative fact, identity-construction obligation, observation/acquisition obligation, recovery/ambiguity obligation, equivalence/overlap claim, terminal-provenance obligation and migration/cutover obligation in the authoritative inputs for this decision;
2. assign each source/obligation a stable entry in the closure record, including its authoritative origin and applicability basis, so omission cannot be hidden by the primitive list;
3. derive the decision-critical primitive universe from that source/obligation universe and prove **total source → primitive coverage**: every applicable source/obligation maps to at least one represented primitive/relation and no decision-critical source/obligation remains unmapped;
4. construct the global closure model and the required cross-checkable inventories from that independently bounded universe;
5. reconcile the candidate against the model when a candidate already exists; and only then
6. decide whether the closure evidence is sufficient for a closure-ready architecture claim.

For proactive pre-candidate work, preserve this derivation invariant:

```text
governing sources
→ source/obligation universe
→ primitive universe
→ frozen closure snapshot
→ genuinely fresh closure review
→ approved closure snapshot
→ separately authorised candidate projection
→ validation/readiness as applicable
→ genuinely fresh candidate review
```

Never invert it into candidate → candidate-derived inventories → self-closure claim.

Candidate prose may help discover a contradiction or an undeclared use, but it must not define the source/obligation universe. A source/obligation may be classified `NOT_APPLICABLE` only with evidence from the governing contract or authoritative environment; silence in the candidate is not evidence of non-applicability.

The invalid argument is:

```text
candidate defines universe U
all elements of U are internally checked
therefore candidate is complete
```

Completeness requires evidence that the closure universe itself contains the applicable decision-critical obligations **and** that every such obligation is represented in the primitive/model universe. Primitive → source traceability alone is insufficient; source → primitive completeness is mandatory.

## Publication gate and closure-evidence freshness

When the proactive trigger applies, a candidate must not be labelled, routed, published or treated as closure-ready until a **current** architecture-closure artefact establishes the required source/obligation coverage and global closure checks **and that exact artefact has passed the required genuinely fresh architecture-closure review**.

At minimum the publication evidence must support results equivalent to:

```text
APPLICABLE_SOURCE_OBLIGATION_WITHOUT_PRIMITIVE_COUNT = 0
PRIMITIVE_WITHOUT_SOURCE_OR_DERIVATION_BASIS_COUNT = 0
UNDECLARED_DECISION_CRITICAL_REFERENCE_COUNT = 0
UNCONSTRUCTABLE_IDENTITY_COUNT = 0
UNDECLARED_STATE_COUNT = 0
AUTHORITY_WITHOUT_ISSUER_OR_PROVENANCE_COUNT = 0
STATE_SENSITIVE_AUTHORITY_WITHOUT_FRESHNESS_BINDING_COUNT = 0
IRREVERSIBLE_EFFECT_WITHOUT_CLAIM_RESULT_RECOVERY_COUNT = 0
TERMINAL_STATE_WITHOUT_EXACT_PROVENANCE_COUNT = 0
UNREACHABLE_ADVERTISED_CAPABILITY_COUNT = 0
UNPROVED_CONSEQUENCE_OVERLAP_COUNT = 0
```

Equivalent structured evidence is acceptable; the field names are not normative.

Bind the artefact to the governing contract and the architecture scope it covers. Freeze each reviewable closure generation as an exact snapshot. If its durable carrier can be edited in place while retaining the same locator, its identity must include an edit-sensitive content/version witness; the locator alone is not an exact closure identity. Material movement of the closure body, governing contract or architecture scope that introduces or changes a decision-critical primitive, authority edge, effect class, state family, identity dependency, equivalence/overlap claim, recovery obligation or migration/fence obligation creates a new closure snapshot generation and invalidates the affected prior approval/evidence for a new closure-ready claim.

Do not require full reconstruction merely because candidate bytes changed. A local correction wholly inside an already-modelled primitive may continue to rely on the existing artefact when current evidence proves the governing contract, closure universe and affected coverage remain applicable.

A current closure artefact is analysis evidence, not architecture approval. Candidate authoring, publication, remediation, merge or later lifecycle effects still require their own authority, and genuinely fresh substantive review remains a separate challenge boundary.

## Required closure artefact

Produce exactly one canonical typed closure model, or repository-appropriate equivalent canonical semantic representation, covering the following dimensions proportionately to the architecture.

The canonical model is the sole normative semantic authority for the closure generation. Its source/obligation records, primitive identities, state/transition semantics, authority/effect semantics, provenance and recovery relationships define the reviewed closure meaning. Review-oriented inventories, matrices, DAGs, witnesses and manifests are **generated projections** of that model, not separately maintained completeness authorities.

Require semantics equivalent to:

```text
CANONICAL_CLOSURE_MODEL = ONE
CLOSURE_PROJECTIONS = DERIVED_NOT_INDEPENDENT_AUTHORITIES
```

A projection may expose an inconsistency or defect in the canonical model, but it must not define the closure universe, create an obligation that is absent from authoritative sources, or silently override another projection. If two projections disagree, fail closed and correct the canonical model or projection generator; do not adjudicate completeness by choosing one hand-maintained view over another.

The required projections include, where applicable:

- source/obligation -> primitive coverage;
- object inventory;
- state/transition inventory;
- authority inventory;
- effect/recovery inventory;
- global identity-dependency DAG;
- ownership/state/transition matrix;
- positive reachability witnesses;
- equivalence/overlap and terminal-provenance views;
- migration/fence view; and
- evidence/reproducibility manifest.

The sections below define the semantic dimensions those generated projections must expose.

### 1. Closed source/obligation universe and total coverage

Construct the bounded source/obligation universe before reconciling candidate prose. At minimum enumerate applicable entries from:

- governing requirements, acceptance criteria, policy and repository-local authority;
- externally observable governed consequence/effect classes and every admissible path capable of reaching them;
- mutable authoritative facts and ownership/serialisation obligations;
- temporal authority-scope obligations, including the state/revision/epoch against which state-sensitive authority is valid and the invalidation/reissue rule after authoritative movement;
- identity-bearing objects and identity-construction dependencies;
- observation/acquisition and negative-inference obligations;
- failure, retry, ambiguity, crash-recovery and reconciliation obligations;
- equivalence, overlap, aliasing and disjointness claims;
- terminal-result/provenance obligations; and
- migration, fencing, cutover, coexistence and drain obligations where applicable.

For each source/obligation entry record its stable identity, authoritative origin, applicability basis and the primitive/relation IDs that represent it. Require:

```text
APPLICABLE_SOURCE_OBLIGATION_WITHOUT_PRIMITIVE_COUNT = 0
PRIMITIVE_WITHOUT_SOURCE_OR_DERIVATION_BASIS_COUNT = 0
```

An applicable source/obligation with no represented primitive/relation makes the architecture `ARCHITECTURE_CLOSURE_NOT_READY`, even if every listed primitive is internally valid. Candidate silence never closes an obligation.

### 2. Decision-critical primitive universe

Derive the primitive set from the closed source/obligation universe before reconciling it with candidate prose.

Each primitive has exactly one **primary role** from this closed partition:

```text
IMMUTABLE_SOURCE
AUTHORITATIVE_OWNER
DETERMINISTIC_DERIVATION
IDENTITY_BEARING_OBJECT
STATE_TRANSITION
AUTHORITY_GRANT_OR_CONSUMPTION
EXTERNAL_EFFECT
DURABLE_RESULT
OBSERVATION_OR_ACQUISITION
RECOVERY_OR_AMBIGUITY_STATE
EQUIVALENCE_OR_OVERLAP_RELATION
MIGRATION_OR_FENCE_PRIMITIVE
EVIDENCE_ONLY
```

Secondary annotations may be used for cross-cutting concerns, but they must not replace the single primary classification. Record the source/obligation IDs that make each primitive applicable.

No security- or authority-relevant behaviour may exist only as prose outside the closure model.

### 3. Five explicit closure inventories

Project the closed source/primitive universe into five cross-checkable inventories, or a representation with exactly equivalent coverage:

1. **Objects** — every decision-critical object type, ID, set, registry, policy, proof/evidence type, snapshot, result, journal, provenance record and immutable manifest/catalog. For content-addressed objects record construction rank/stage and identity dependencies.
2. **States** — every stateful object's complete closed state enumeration, initial/terminal/blocked states and required fields/invariants by state.
3. **Operations** — every authority-changing or state-changing transition, including exact source states, reads/preconditions, required authority, emitted objects, writes/effects, resulting states, terminal/provenance behaviour and retry/ambiguity semantics.
4. **Authorities** — every grant/token/activation authority, including exact scope, bound owner/consequence, permitted operation, cardinality, consumption/reissue rules, replay/substitution constraints and terminal treatment. For every state-sensitive authority, also record the exact bound state/revision/epoch/freshness predicate, or a normative proof that the authority is intentionally revision-invariant, plus the rule by which authoritative state movement invalidates, consumes or requires reissue of that authority.
5. **Effects** — every irreversible governed consequence/effect class and every admissible path capable of reaching it, including owner, authority, immutable claim, executor, idempotency key, durable result/journal, lost-response/crash recovery, ambiguity handling and terminal provenance.

Every decision-critical noun/reference used by the architecture must resolve to this model. An undeclared object, state, operation, authority or effect makes closure not ready. A zero-count assertion is meaningful only after this universe-closure and inventory-coverage step passes.

### 4. Global identity-dependency DAG

Construct one graph covering every identity-bearing/content-addressed object and every identity-bearing derivation.

For every node record:

- exact core/envelope inputs;
- owning schema/definition;
- dependencies on other immutable identities;
- construction phase;
- whether any symbolic/self placeholder is used and its exact resolution rule.

Require:

- no direct or indirect dependency on an object's own final identity;
- one deterministic topological construction order;
- no locally valid object definitions that compose into a global cycle;
- one normative identity definition per concept; and
- later objects depending only on already-constructible immutable identities.

Acyclicity of isolated sections is insufficient.

### 5. Ownership / state / transition matrix

For every mutable authoritative fact record:

```text
authoritative owner
revision / serialisation domain
allowed readers
allowed writers
allowed transitions
preconditions / compare set
read set
write set
emitted immutable evidence
postconditions
terminality / replay rule
```

Every authoritative mutation must occur through exactly one closed transition model or an explicitly defined atomic/composed transaction.

No authority-bearing owner, allocator, registry, reservation, selector or activation binding may exist only by convention.

Cross-check every state-sensitive authority in the Authorities inventory against this matrix. Its validity predicate must bind the exact relevant authoritative state/revision/epoch (or prove revision-invariance), and every transition that moves that binding must define whether the authority is consumed, permanently stale, explicitly carried forward, or reissued under a new identity. Returning later to a semantically similar state must not revive stale authority by state-name coincidence.

### 6. Positive reachability witnesses

For every advertised lifecycle state, repair path, recovery path, migration phase or authority capability, provide at least one valid witness path from an admitted initial state under the actual validation and transition rules.

Reject vacuous safety claims where a state exists in prose but cannot be reached when needed.

Reject repair semantics whose preconditions can never be satisfied.

### 7. End-to-end authority/effect matrix

For every authority-changing consequence, trace the complete path:

```text
authority provenance
→ reservation / ownership
→ exact candidate/state
→ review / grant basis where applicable
→ claim
→ effect attempt
→ external system boundary
→ durable result
→ lost-response / ambiguous-result handling
→ reconciliation
→ authoritative terminal projection
```

Do not stop the model at an internal `CONSUME`, commit flag, queue write, journal claim or equivalent when the governed consequence is an external effect.

Internal state closure is not end-to-end effect closure.

### 8. Observation / ambiguity / crash-recovery matrix

Every decision-critical observation must be one of:

- an authoritative stored projection;
- a deterministic derivation from named immutable inputs;
- a closed acquisition contract;
- or an explicit unknown/ambiguous state with fail-closed recovery semantics.

Cover applicable:

- duplicate delivery;
- stale observations;
- crash-before-effect;
- crash-after-effect-before-result;
- lost response;
- retry after ambiguous outcome;
- replay;
- reconciliation after partial success; and
- prolonged failure.

### 9. Equivalence / overlap / symmetry proofs

Whenever the architecture claims that two independently sourced inputs, profiles, namespaces or projections refer to:

- the same governed consequence;
- disjoint governed consequences;
- equivalent identities;
- compatible namespaces; or
- mutually exclusive authority domains;

require a normative proof/witness/validator contract.

A prose assertion of equivalence or disjointness is not closure evidence.

For irreversible governed consequences, require the stronger extensional ownership invariant:

```text
same possible irreversible governed real-world consequence
  → exactly one canonical consequence identity
  → exactly one authority owner
  → every activation / attempt / replacement / effect authority
     bound to that owner
```

For every pair of admissible effect paths, or an equivalent complete partition of the path set, establish exactly one of:

```text
SAME_CONSEQUENCE
  → both paths provably collapse to the same canonical consequence identity and owner

DISJOINT_CONSEQUENCES
  → disjointness is justified by a normative proof/witness/validator contract
```

Specifically attack aliases/sources, profiles, direct versus migration paths, replacement candidates, retries/reissues, multiple executors and protocol revisions. Opaque provenance fields are not proof of extensional ownership.

### 10. Terminal provenance matrix

Every terminal state must identify the exact durable result/outcome provenance that justifies terminality.

No terminal state may depend on:

- latest-record inference;
- comment/timestamp/search ordering;
- missing evidence interpreted as success;
- implementation convention;
- or an unmodelled external effect.

### 11. Migration / fence matrix when applicable

Where legacy/successor or old/new interpreters may coexist, include:

- the complete authority universe being transferred, fenced or drained;
- exact snapshot/acquisition semantics proving completeness;
- serialisation between fence state and every old/new authority-changing effect;
- in-flight/ambiguous work accounting;
- drain/terminal conditions;
- activation provenance; and
- proof that two interpreters cannot retain live authority over the same consequence.

### Minimum closure checks

The closure artefact must support an explicit result for at least:

1. **Closed universe** — every decision-critical source obligation and noun/reference belongs to the closure model; no undeclared object/state/authority/effect is used elsewhere.
2. **Identity construction order** — every identity dependency points to an earlier construction rank/stage; no same-stage, higher-stage, self, mutual or undeclared dependency exists unless an explicit identity contract defines the exception.
3. **Total state closure** — every transition uses declared states and every non-terminal state has a permitted successor or explicit fail-closed interpretation; terminal parents do not strand prohibited live authority-relevant children.
4. **Authority scope/cardinality** — every authority binds the exact owner/consequence it may mutate and has explicit use, consumption, replay and reissue semantics.
5. **Authority freshness/state binding** — every state-sensitive authority binds the exact state/revision/epoch/freshness predicate against which it is valid, or carries normative proof of intentional revision-invariance; authoritative movement cannot silently preserve or revive stale authority, and any carry-forward or reissue is explicit and identity-bound.
6. **Extensional ownership** — any paths capable of the same irreversible consequence resolve to one canonical owner; claimed disjoint paths carry proof.
7. **Effect completion** — irreversible effects are modelled end-to-end as authority → immutable claim → execution → idempotency → durable result/journal → ambiguity/crash recovery → terminal provenance.
8. **Positive reachability** — every advertised capability/state has at least one valid witness from an admitted initial state to the intended result.

Before declaring closure ready, explicitly attack whether any noun, ID, set, state, authority, effect, result or provenance object appears anywhere but has no row/entry in the closure record. Also attack whether any authority with the correct owner/consequence/operation could remain usable after the authoritative state/revision it was issued against has moved, including paths that later return to the same named state.
## Closure decision

After deriving the model independently, resolve the entry mode before disposition:

- **Proactive pre-candidate entry:** no candidate exists yet. Assess the independently derived closure artefact against the governing contract and authoritative environment without requiring candidate reconciliation. `ARCHITECTURE_CLOSURE_READY` means the author-side closure artefact is complete enough to enter the required genuinely fresh architecture-closure review; it does **not** by itself make closure-ready candidate authoring eligible.
- **Candidate-present entry:** reconcile the exact candidate against the independently derived model before disposition. This includes reactive reconsideration/reconstruction and any later analysis of an existing candidate.

Return one of:

### `ARCHITECTURE_CLOSURE_READY`

Use only when all applicable closure dimensions are represented and current evidence establishes:

- a closed source/obligation universe for the governing contract and authoritative environment;
- total source → primitive coverage with no unmapped applicable obligation;
- a complete decision-critical primitive universe using the closed primary-role partition;
- complete cross-checkable object/state/operation/authority/effect inventories;
- a globally acyclic constructible identity graph;
- closed authoritative ownership/transitions;
- explicit authority freshness/state binding with no stale-authority revival across authoritative state/revision movement;
- positive reachability for advertised states/capabilities;
- end-to-end authority/effect coverage;
- extensional consequence ownership across every admissible effect path, or proved disjointness;
- closed ambiguity/recovery semantics;
- sufficient equivalence/overlap evidence;
- total terminal provenance; and
- migration/fence closure where applicable.

For proactive pre-candidate entry, this disposition applies to the frozen closure snapshot/model only: no candidate identity is required, and no candidate approval is implied. For candidate-present entry, it additionally requires the exact candidate reconciliation described above. `ARCHITECTURE_CLOSURE_READY` means the snapshot is eligible to enter fresh closure review; it is not candidate-projection eligibility.

When the governing lifecycle requires architecture closure before replacement/closure-ready candidate projection, this disposition establishes `CLOSURE_REVIEW_REQUIRED` bound to the exact durable closure artefact. The next gate is a genuinely fresh review of the closure artefact itself. Candidate authoring remains ineligible until that exact artefact receives `APPROVED_FOR_CANDIDATE_PROJECTION`.

This is analysis evidence only. It does not approve, implement or mutate the architecture, and it does not self-approve the closure artefact.

### `ARCHITECTURE_CLOSURE_NOT_READY`

Use when the architecture/model is incomplete, internally inconsistent, cyclic, unreachable, unproven or otherwise not closure-ready, including when the independently derived source/obligation universe is not fully represented.

Examples include an applicable source/obligation with no mapped primitive, an undeclared noun/state/operation/authority/effect, a state-sensitive authority with no exact freshness/state-revision binding or justified revision-invariance, a represented identity relation that creates a cycle, a represented transition with incomplete terminal provenance, or a represented equivalence relation with no acceptable witness.

### `CLOSURE_METHOD_FALSIFIED`

Use when fresh substantive evidence establishes an applicable decision-critical source/obligation, primitive or relationship that should have been present in the prior closure universe but was absent from it.

Classify the review evidence as logically equivalent to:

```text
UNMODELLED_DECISION_CRITICAL_PRIMITIVE
```

and bind the falsification record to:

- the prior closure artefact/model;
- the exact reviewed candidate;
- the fresh review identity/disposition;
- the omitted source/obligation, primitive or relation and why it was applicable;
- the governing contract;
- the decision-critical effect of the omission.

The resulting governed state is:

```text
CLOSURE_METHOD_FALSIFIED
→ ARCHITECTURE_CLOSURE_RECONSTRUCTION_REQUIRED
→ ordinary isolated /fix ineligible
```

Do not merely append the newly discovered primitive to prose and resume the previous repair plan.
## Closure-method falsification boundary

`CLOSURE_METHOD_FALSIFIED` is a governing-disposition boundary for the current strong-closure generation.

The authority that permitted the current closure generation does not silently become authority to create another generation after the closure method was falsified. Preserve the falsifying review, prior canonical model/snapshot, exact candidate when applicable, governing contract and omitted obligation/primitive/relation as terminal predecessor evidence.

Do not automatically reconstruct or append the newly discovered primitive and continue. A later strong-closure generation requires a separately governed disposition that explicitly authorises that new generation and binds it to the predecessor evidence.

If a prior closure artefact had already received `APPROVED_FOR_CANDIDATE_PROJECTION` and later fresh evidence establishes either `CLOSURE_METHOD_FALSIFIED` or `EQUIVALENT_SAME_FAMILY_STRUCTURAL_FALSIFICATION`, the same governing disposition must consider simplification/decomposition before authorising more closure complexity. Explicitly consider state/authority/configuration/effect removal, platform-primitive reuse, moving authority to the actual authoritative boundary, lifecycle/contract decomposition, objective narrowing, and retirement of contradictory active surface.

## Modelled defect versus missing primitive

Do not falsify the closure method merely because a represented primitive is wrong.

Use a distinction equivalent to:

```text
MODELLED_BUT_WRONG
UNMODELLED_DECISION_CRITICAL_PRIMITIVE
```

`MODELLED_BUT_WRONG` may still block approval and may require architecture-level correction, but it does not prove the closure universe itself was incomplete and does not automatically establish `CLOSURE_METHOD_FALSIFIED`.

Likewise, do not falsify the prior closure method solely because:

- a new governing requirement became applicable later;
- a materially new architecture scope was introduced later;
- a genuinely unrelated defect family appears;
- duplicate review records repeat the same adjudication;
- a non-substantive check/test fails; or
- a reviewer disagrees with an architecture choice that is fully represented and whose dispute is a design/decision question.

## Remediation completeness for closure candidates

### Approved-closure candidate projection

When a candidate is to be authored from a closure artefact that is subject to the fresh closure-review gate, require durable/reconstructable bindings equivalent to:

```text
ARCHITECTURE_CLOSURE_SOURCE=<exact closure artefact identity>
ARCHITECTURE_CLOSURE_REVIEW=<exact fresh review identity with APPROVED_FOR_CANDIDATE_PROJECTION>
```

Candidate projection may realise or refine already-modelled elements, but it must not silently introduce a new decision-critical primitive, authority edge, state family, effect class, identity dependency, recovery rule, equivalence/overlap claim, migration obligation or external/platform boundary. If projection needs any such new semantic, invalidate projection eligibility and enter closure reconstruction/analysis first; freeze a new `ARCHITECTURE_CLOSURE_READY` snapshot generation before another genuinely fresh closure review. Never route directly from new decision-critical projection semantics to review of the old snapshot. Byte-level change inside an already-modelled primitive does not by itself invalidate the closure approval. After a candidate is successfully projected within the approved universe, complete the applicable validation and remediation-/authoring-readiness evidence for that exact candidate before the separately fresh candidate review.


For any later authorised architecture candidate derived from this workflow, completion evidence must establish all three layers:

```text
FINDING_CLOSURE
  every reported blocker addressed

MODEL_CLOSURE
  the affected closure universe has been rederived/revalidated
  and no newly introduced or newly exposed applicable primitive sits outside it

PARENT_NON_REGRESSION
  previously established identity/authority/state/effect/recovery invariants remain satisfied
```

Patching only the latest finding is insufficient when that finding exposed an omitted primitive.

## Strong-closure generation and well-founded recovery

Each strong architecture-closure attempt is one immutable **strong-closure generation**. Bind its identity to the governing source/obligation boundary, closure scope, canonical model identity and applicable authority source. The generation owns exactly:

```text
SEMANTIC_CORRECTION_ALLOWANCE = 1
PACKAGE_ONLY_REPAIR_ALLOWANCE = 1
```

Both the semantic-correction allowance and the package-only repair allowance are monotone and generation-owned. Renaming, repackaging, issue recreation, candidate replacement, snapshot regeneration or moving the durable carrier cannot replenish a consumed allowance.

Fresh architecture-closure review owns classification of the completed blocking finding set for routing. Use the following mutually safety-preserving outcomes:

### `MODELLED_DEFECT`

Use only when every material defect is wholly inside an obligation/primitive already represented by the current canonical model, the governing source/obligation boundary is unchanged, and no governing scope or authority movement is involved.

If the semantic-correction allowance is unused, one bounded in-generation semantic correction may:

1. correct the canonical model;
2. regenerate all affected projections/package evidence;
3. freeze a new exact snapshot inside the same generation; and
4. return to genuinely fresh closure review.

If the semantic allowance is already consumed, route to `GOVERNING_DISPOSITION_REQUIRED`.

### `PACKAGE_ONLY_DEFECT`

Use only when the canonical semantic model, governing source/obligation universe, decision-critical inputs and semantic outputs are unchanged and the defect is limited to packaging, manifest, retrievability, reproducibility or equivalent admission evidence.

If the package-only allowance is unused, perform one bounded repair, rerun the applicable deterministic admission/reconstruction checks, freeze the repaired package, and return to fresh closure review where required. This path does not consume the semantic-correction allowance.

If semantic movement is required, or package-only eligibility is ambiguous, do not use this route.

### `NEW_OR_OMITTED_OBLIGATION`, `STRUCTURAL_FALSIFICATION`, `SCOPE_OR_AUTHORITY_MOVEMENT`

Any of these routes the current generation directly to:

```text
GOVERNING_DISPOSITION_REQUIRED
```

An omitted already-authoritative obligation is immediately material when fresh review establishes its applicability and decision-critical consequence. It does **not** require a separate scope-amendment decision merely to become blocking.

Mixed or ambiguous findings fail closed to `GOVERNING_DISPOSITION_REQUIRED`; author-side evidence cannot downgrade a review-owned structural route into an in-generation correction.

### Governing disposition

`GOVERNING_DISPOSITION_REQUIRED` terminates active progression for the current generation. It is not another closure-reconstruction state.

A separately governed disposition may choose, as applicable:

- authorise a new strong-closure generation with an amended source/obligation boundary;
- decompose the architecture or objective;
- reduce the assurance/completeness claim;
- simplify by removing state, authority, effect paths or contradictory active surface;
- defer;
- reject or abandon the approach.

A new generation receives new allowances only because it has a new explicitly authorised generation identity. The predecessor remains terminal provenance and must be linked durably; no automatic successor generation is permitted.

## Fresh-review expectation

Before candidate projection when `CLOSURE_REVIEW_REQUIRED` applies, genuinely fresh review of the **closure artefact itself** must independently challenge the closure universe and return `APPROVED_FOR_CANDIDATE_PROJECTION` or `CHANGES_REQUIRED`. After projection, fresh architecture/security/authority review of the resulting candidate remains a separate gate and must challenge three independent questions:

1. **internal correctness** — are the represented primitives and relations correct?;
2. **source-universe completeness** — did the closure record omit an applicable authoritative requirement, externally observable consequence, mutable fact, identity/observation/recovery/equivalence/terminal/migration obligation before primitive derivation?; and
3. **representation completeness** — does every applicable source/obligation map to represented primitives and do the object/state/operation/authority/effect inventories and extensional ownership model cover every decision-critical use/path?

The reviewer must not inherit the author's claim that the source/obligation universe or primitive universe is complete.

The reviewer should actively attempt to derive an applicable source/obligation from the governing contract or externally observable consequence model that is absent from the source inventory, then attempt to find an inventoried obligation with no primitive mapping, an undeclared decision-critical noun/reference, or an effect path that lacks canonical-owner/disjointness proof.

A closure process that cannot survive that challenge is not complete.
## Regression examples

The reusable contract should preserve at least these failure distinctions.

### Global identity cycle hidden by locally valid objects

If registry A's final identity depends on definition D while D's final identity depends on registry A, local object schemas may each look valid but the global identity DAG is cyclic. Return `ARCHITECTURE_CLOSURE_NOT_READY`; do not accept local digest correctness as global constructibility.

### Omitted source obligation with internally valid primitives

If governing contract G requires observable consequence E, but E is omitted from the source/obligation universe while every listed primitive is internally valid, the analysis must return `ARCHITECTURE_CLOSURE_NOT_READY`. It must not infer completeness from the listed primitives. If a prior closure record nevertheless claimed ready and a fresh reviewer discovers the omitted applicable obligation, the reviewer may establish `UNMODELLED_DECISION_CRITICAL_PRIMITIVE` and therefore `CLOSURE_METHOD_FALSIFIED`.
### Unmodelled external effect

If an internal claim/result journal closes `CONSUME` but the real governed consequence occurs in an external system and the external effect plus lost-response recovery are absent from the closure universe, a fresh reviewer may establish `UNMODELLED_DECISION_CRITICAL_PRIMITIVE` and therefore `CLOSURE_METHOD_FALSIFIED`.

### Missing durable authority binding

If an activation transition exists but the exact adopted profile/configuration authority is not represented as durable provenance, architecture closure is not ready. If that authority primitive was absent from a previously claimed closure universe and fresh review establishes its applicability, the closure method may be falsified.

### Stale authority survives authoritative movement

If an authority has the correct owner, consequence, permitted operation and cardinality but is state-sensitive and lacks an exact state/revision/epoch/freshness binding, closure is not ready. Advancing authoritative state, or returning later to a compatible named state, must not leave the old authority usable unless a normative revision-invariance rule explicitly permits it. Reissue after movement must create the newly bound authority required by the model rather than reviving the stale authority.

### Missing equivalence proof

If two independently sourced rules claim the same canonical key/consequence space but no normative witness or validator proves that equivalence, return `ARCHITECTURE_CLOSURE_NOT_READY`.

### Missing terminal provenance

If a terminal state exists but no exact durable result/outcome object justifies terminality, return `ARCHITECTURE_CLOSURE_NOT_READY`.

### Modelled local defect

If a transition and its governing primitive were already present in the closure universe but fresh review finds a wrong predicate inside that transition, classify it as `MODELLED_BUT_WRONG`. The finding may block approval but does not automatically establish `CLOSURE_METHOD_FALSIFIED`.

### New requirement after closure

If the closure universe was complete for governing contract G1 and a genuinely new requirement G2 becomes applicable later, refresh or rederive under the current contract as required. Do not retroactively classify the prior closure method as falsified solely because G2 did not exist in G1.

## Output

Return a concise architecture-closure record containing:

- applicability and authority basis;
- entry mode (`PRE_CANDIDATE` or `CANDIDATE_PRESENT`), candidate binding (`PRE_CANDIDATE` when no candidate exists, otherwise the exact immutable candidate), and governing contract;
- closed source/obligation-universe identity and authoritative derivation basis;
- total source → primitive coverage result, including any unmapped applicable obligation;
- primitive-universe identity and closed primary-role classification result;
- object/state/operation/authority/effect inventory coverage result;
- closure artefact/model identity or durable location;
- global identity-DAG result;
- ownership/state/transition result;
- authority freshness/state-binding result, including stale-authority invalidation/reissue semantics;
- reachability result;
- authority/effect result;
- extensional consequence-ownership / disjointness result;
- ambiguity/recovery result;
- equivalence/overlap result;
- terminal-provenance result;
- migration/fence result when applicable;
- disposition: `ARCHITECTURE_CLOSURE_READY`, `ARCHITECTURE_CLOSURE_NOT_READY`, or `CLOSURE_METHOD_FALSIFIED`;
- `CLOSURE_REVIEW_REQUIRED` and the exact closure artefact identity when a fresh closure-review gate applies;
- `COMPLEXITY_DISPOSITION_REQUIRED` plus `SIMPLIFY_OR_DECOMPOSE` or `ADDITIONAL_MODEL_COMPLEXITY_JUSTIFIED` when an approved closure is later structurally falsified;
- any resulting `ARCHITECTURE_CLOSURE_RECONSTRUCTION_REQUIRED` boundary;
- explicitly untested or unresolved surface;
- required next authority/decision.

Return control to the workflow router. Do not mutate source, create a design candidate, approve the target, or manufacture follow-on authority.
## What it does

Separates architecture-universe derivation from candidate validation so a design cannot prove completeness only by checking the objects and transitions it already chose to model. It produces a reconstructable closure record that distinguishes internal model defects from closure-method falsification and binds any reconstruction requirement to the correct authority boundary.

## Boundaries / limitations

Use proportionately. This workflow does not require a theorem prover, model checker, graph database, persisted workflow-state object, or any particular artefact format. It does not replace ordinary stateful/invariant analysis, independently decide product or architecture policy, establish that redesign is necessary, or create implementation/remediation/merge/release/deployment/migration/production authority. Its completeness claim remains bounded to the governing contract and evidence actually inspected; genuinely new later requirements require refresh rather than retroactive falsification.

## Status

`tested`
