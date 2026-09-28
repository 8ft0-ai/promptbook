# Architecture closure analysis

## Purpose

Derive and challenge a decision-critical architecture-closure model whose completeness does not depend on the candidate's own self-defined object, relation, transition or prose universe.

Use this workflow only for materially security-, authority-, identity-, lifecycle-, recovery- or migration-sensitive architecture work when current governed state requires architecture closure or reconstruction. It is intentionally stronger than ordinary stateful/invariant analysis and does not replace that proportional workflow for routine stateful defects.

## When to use

Use this workflow when current authoritative evidence establishes one of:

- an authorised architecture reconsideration whose result requires an architecture-closure proof before a candidate can safely be treated as closure-ready; or
- `CLOSURE_METHOD_FALSIFIED` / `ARCHITECTURE_CLOSURE_RECONSTRUCTION_REQUIRED` because a fresh substantive review identified an applicable unmodelled decision-critical primitive, relation, authority edge, effect boundary, recovery state, identity dependency, equivalence claim, terminal-provenance requirement or migration/fence obligation that should have been present in the prior closure universe.

Do not select this workflow merely because an architecture is large, a review found several blockers, or a modelled element is locally wrong. Ordinary architecture/design reasoning or bounded remediation remains appropriate unless the closure-completeness conditions above are established.

Architecture-closure analysis is read-only. It does not create implementation, redesign, remediation, merge, release, deployment, settings, credential, migration, production or other consequential authority.

## Core rule

Do not define the closure universe by reading the candidate's headings and then checking that every listed item is internally consistent.

Instead:

1. derive the decision-critical primitive universe independently from the governing contract, authority boundaries, externally observable consequences, mutable authoritative state, identity construction obligations, recovery/ambiguity obligations and migration/cutover obligations;
2. construct the global closure model from that independent universe;
3. reconcile the candidate against the model; and only then
4. decide whether the architecture is closure-ready.

The invalid argument is:

```text
candidate defines universe U
all elements of U are internally checked
therefore candidate is complete
```

Completeness requires evidence that the closure universe itself contains the applicable decision-critical primitives.

## Required closure artefact

Produce one canonical closure artefact, or repository-appropriate equivalent, covering the following dimensions proportionately to the architecture.

### 1. Decision-critical primitive universe

Derive the primitive set from governing requirements and externally observable behaviour before reconciling it with candidate prose.

For each applicable primitive, classify its role using one or more explicit categories such as:

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

Record the governing requirement or externally observable obligation that makes each primitive applicable.

No security- or authority-relevant behaviour may exist only as prose outside the closure model.

### 2. Global identity-dependency DAG

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

### 3. Ownership / state / transition matrix

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

### 4. Positive reachability witnesses

For every advertised lifecycle state, repair path, recovery path, migration phase or authority capability, provide at least one valid witness path from an admitted initial state under the actual validation and transition rules.

Reject vacuous safety claims where a state exists in prose but cannot be reached when needed.

Reject repair semantics whose preconditions can never be satisfied.

### 5. End-to-end authority/effect matrix

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

### 6. Observation / ambiguity / crash-recovery matrix

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

### 7. Equivalence / overlap / symmetry proofs

Whenever the architecture claims that two independently sourced inputs, profiles, namespaces or projections refer to:

- the same governed consequence;
- disjoint governed consequences;
- equivalent identities;
- compatible namespaces; or
- mutually exclusive authority domains;

require a normative proof/witness/validator contract.

A prose assertion of equivalence or disjointness is not closure evidence.

### 8. Terminal provenance matrix

Every terminal state must identify the exact durable result/outcome provenance that justifies terminality.

No terminal state may depend on:

- latest-record inference;
- comment/timestamp/search ordering;
- missing evidence interpreted as success;
- implementation convention;
- or an unmodelled external effect.

### 9. Migration / fence matrix when applicable

Where legacy/successor or old/new interpreters may coexist, include:

- the complete authority universe being transferred, fenced or drained;
- exact snapshot/acquisition semantics proving completeness;
- serialisation between fence state and every old/new authority-changing effect;
- in-flight/ambiguous work accounting;
- drain/terminal conditions;
- activation provenance; and
- proof that two interpreters cannot retain live authority over the same consequence.

## Closure decision

After deriving the model independently, reconcile the exact candidate against it.

Return one of:

### `ARCHITECTURE_CLOSURE_READY`

Use only when all applicable closure dimensions are represented and current evidence establishes:

- a complete decision-critical primitive universe for the governing contract;
- a globally acyclic constructible identity graph;
- closed authoritative ownership/transitions;
- positive reachability for advertised states/capabilities;
- end-to-end authority/effect coverage;
- closed ambiguity/recovery semantics;
- sufficient equivalence/overlap evidence;
- total terminal provenance; and
- migration/fence closure where applicable.

This is analysis evidence only. It does not approve, implement or mutate the architecture.

### `ARCHITECTURE_CLOSURE_NOT_READY`

Use when the closure universe contains the relevant primitive but the architecture/model is internally incomplete, inconsistent, cyclic, unreachable, unproven or otherwise not closure-ready.

Examples include a represented identity relation that creates a cycle, a represented transition with incomplete terminal provenance, or a represented equivalence relation with no acceptable witness.

### `CLOSURE_METHOD_FALSIFIED`

Use when fresh substantive evidence establishes an applicable decision-critical primitive or relationship that should have been present in the prior closure universe but was absent from it.

Classify the review evidence as logically equivalent to:

```text
UNMODELLED_DECISION_CRITICAL_PRIMITIVE
```

and bind the falsification record to:

- the prior closure artefact/model;
- the exact reviewed candidate;
- the fresh review identity/disposition;
- the omitted primitive/relation and why it was applicable;
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

`ARCHITECTURE_CLOSURE_RECONSTRUCTION_REQUIRED` is a separate-authority boundary.

The authority that permitted the previous one-shot architecture reconsideration does not silently become unlimited authority to rerun closure reconstruction after its closure method was falsified.

Before reconstruction, require a current separately governed authority source specifically permitting that bounded read-only reconstruction. When authorised, perform exactly one fresh closure reconstruction bound to:

- the falsifying review;
- prior closure artefact;
- current exact candidate;
- governing contract; and
- reconstruction-authority source.

A current reconstruction record satisfies that analysis gate for those exact bindings. Do not loop automatically into repeated reconstruction while it remains current. Material movement of a decision-critical binding requires refresh under normal freshness rules.

The reconstruction result still creates no design-mutation/remediation authority. Any resulting candidate change requires separately established current authority and a new candidate-bound remediation/design plan derived from the reconstructed closure model.

## Modelled defect versus missing primitive

Do not falsify the closure method merely because a represented primitive is wrong.

Use a distinction equivalent to:

```text
MODELLED_BUT_WRONG
UNMODELLED_DECISION_CRITICAL_PRIMITIVE
```

`MODELLED_BUT_WRONG` may still block approval and may require architecture-level correction, but it does not prove the closure universe itself was incomplete.

Likewise, do not falsify the prior closure method solely because:

- a new governing requirement became applicable later;
- a materially new architecture scope was introduced later;
- a genuinely unrelated defect family appears;
- duplicate review records repeat the same adjudication;
- a non-substantive check/test fails; or
- a reviewer disagrees with an architecture choice that is fully represented and whose dispute is a design/decision question.

## Remediation completeness for closure candidates

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

## Fresh-review expectation

Fresh architecture/security/authority review of a closure candidate must challenge two independent questions:

1. **internal correctness** — are the represented primitives and relations correct?; and
2. **universe completeness** — is an applicable decision-critical primitive, dependency, authority edge, effect boundary, recovery state, equivalence relation, terminal provenance requirement or migration/fence obligation absent entirely?

The reviewer must not inherit the author's claim that the closure universe is complete.

The reviewer should actively attempt to derive a security/authority primitive from the governing contract or externally observable consequence model that the closure artefact omitted.

A closure process that cannot survive that challenge is not complete.

## Regression examples

The reusable contract should preserve at least these failure distinctions.

### Global identity cycle hidden by locally valid objects

If registry A's final identity depends on definition D while D's final identity depends on registry A, local object schemas may each look valid but the global identity DAG is cyclic. Return `ARCHITECTURE_CLOSURE_NOT_READY`; do not accept local digest correctness as global constructibility.

### Unmodelled external effect

If an internal claim/result journal closes `CONSUME` but the real governed consequence occurs in an external system and the external effect plus lost-response recovery are absent from the closure universe, a fresh reviewer may establish `UNMODELLED_DECISION_CRITICAL_PRIMITIVE` and therefore `CLOSURE_METHOD_FALSIFIED`.

### Missing durable authority binding

If an activation transition exists but the exact adopted profile/configuration authority is not represented as durable provenance, architecture closure is not ready. If that authority primitive was absent from a previously claimed closure universe and fresh review establishes its applicability, the closure method may be falsified.

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
- exact candidate and governing contract;
- independent primitive-universe derivation basis;
- closure artefact/model identity or durable location;
- global identity-DAG result;
- ownership/state/transition result;
- reachability result;
- authority/effect result;
- ambiguity/recovery result;
- equivalence/overlap result;
- terminal-provenance result;
- migration/fence result when applicable;
- disposition: `ARCHITECTURE_CLOSURE_READY`, `ARCHITECTURE_CLOSURE_NOT_READY`, or `CLOSURE_METHOD_FALSIFIED`;
- any resulting `ARCHITECTURE_CLOSURE_RECONSTRUCTION_REQUIRED` boundary;
- explicitly untested or unresolved surface;
- required next authority/decision.

Return control to the workflow router. Do not mutate source, create a design candidate, approve the target, or manufacture follow-on authority.

## Status

`tested`
