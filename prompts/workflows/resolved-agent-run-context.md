# Resolved agent run context

## Purpose

Define the reusable Promptbook contract for deriving the effective execution state of a governed agent operation from current authoritative inputs. The explicitly supported operations are `/review` and `/fix`, each with its own capability and lifecycle profile under one common authority/evidence model.

Promptbook is the canonical owner of this workflow contract. The context is ephemeral derived state, not a new durable authority source and not a replacement for repository-native instructions, issue or pull-request authority, immutable Git identity, CI evidence, or other durable records.

## When to use

Use this contract before substantive `/review` adjudication and before substantive `/fix` mutation so the operation executes from explicit repository/work authority, candidate identity, capability boundaries, instruction provenance, and required evidence rather than remembered conversation state.

An operation may reuse the common model only when its own authority and capability semantics are deliberately defined here. Supporting `/fix` does not generalise `/review` permissions to mutation, and neither profile defines `/go` authority.

## Prompt

```text
Before substantive governed execution, resolve an ephemeral Resolved Agent Run Context from current authoritative inputs for the selected operation.

Bind the operation to the repository, work item, immutable candidate identity where applicable, resolved authority sources, applicable repository instructions and their provenance, effective and prohibited capabilities, owner-decision boundaries, and required evidence. For `/fix`, also bind the starting candidate, remediation scope, and required validation before substantive mutation.

Treat the resolved context as derived execution state rather than a new authority source. Do not fill missing authority or evidence from conversation memory. Technical capability availability may only narrow executable capability; it must never create authority.

Use the operation-specific capability profile and lifecycle below. Collect bounded reconstructable evidence, distinguish static observation from executed and durable evidence, and bind candidate-specific evidence to the immutable candidate for which it was actually observed.
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

## Common inputs and authority resolution

Resolve the context from the authoritative inputs that apply to the operation. At minimum, consider:

- platform safety and explicit current-user authority;
- the Promptbook workflow selected for the operation;
- repository-local instructions and mandatory policy;
- the governing issue, pull request, design, specification, accepted plan, review finding, or other work-item authority;
- the immutable candidate being reviewed or remediated where applicable;
- current CI, checks, review state, and other decision-critical durable evidence.

Conversation history may help locate those sources, but it is not a substitute for refreshing them when correctness depends on current state.

Resolve the context from current authoritative inputs in precedence order appropriate to the repository and operation. Record enough provenance to identify where each applicable instruction or material rule came from. A resolved context does not create authority absent from those sources.

If a required authority source cannot be resolved, fail closed or hand off according to the governing workflow rather than filling the gap from conversation memory.

The representation may be textual or structured. It need not be committed for every run. Whatever representation is used, equivalent authoritative inputs must resolve to equivalent effective authority, candidate identity, capability boundaries, and evidence requirements for the same operation.

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
required_validation
required_evidence
```

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

## Required evidence

Resolve the evidence necessary to support the requested operation before adjudicating or declaring remediation complete. Evidence should be proportionate, bounded, and reconstructable. Depending on the claim, it may include:

- an exact command or tool invocation and result status;
- bounded relevant output;
- a CI or check result bound to the candidate;
- a reproducible test;
- a static source observation;
- an applicable repository-rule or authority citation;
- for `/fix`, the bounded implementation delta and resulting candidate identity.

Do not fabricate executed evidence where only static analysis occurred. Identify static observations as static. If a material claim requires execution that was not performed, represent that absence rather than implying the execution succeeded.

For evidence, distinguish at least:

- `STATIC` — source, configuration, metadata, or rule observation without executing the claimed behaviour;
- `EXECUTED` — a command, test, check, or tool action was actually run and its result observed;
- `DURABLE` — repository-hosted CI, review, check, or other retained evidence was inspected.

A finding or remediation record may use more than one evidence class. Do not upgrade one class into another merely to strengthen the conclusion.

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

Makes the effective execution state of supported governed operations explicit and reconstructable without introducing a new durable per-run artefact. It separates authority from capability, preserves repository-instruction provenance, and requires honest evidence classes bound to the candidate for which they were observed.

For `/review`, it keeps the existing Promptbook review-recording model intact: ordinary router `/review` may publish only the requested review record, while `/review --read-only` remains zero-write.

For `/fix`, it permits only bounded remediation mutation derived from current authority, classifies material actions before execution, distinguishes candidate A from candidate B, and prevents A-specific review or validation from silently carrying forward after bytes change.

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

During remediation, classify each material action through the action gateway and execute only `ALLOW` actions that are actually available. After changed bytes produce B, invalidate A-specific review/validation for B, run the required validation against B, and record the resulting candidate/evidence without crossing a required fresh-review boundary.

## Delegation invariant

Future delegated or child execution contexts must never gain authority merely through delegation:

```text
child_authority ⊆ parent_authority
```

An external execution substrate should receive only the resolved authorised subset needed for the delegated action. This contract does not introduce subagent infrastructure or make the substrate a workflow-policy owner.

## Boundaries / limitations

This contract does not define `/go` run contexts, a new Switchboard schema, operating-system or network sandboxing, Guardian-style approval automation, native subagents, agentctl policy ownership, or Watchtower workflow ownership.

It does not grant merge, release, tag, deployment, infrastructure/provider, settings, credential, secret, production, or unrelated mutation authority. Those actions require a separate governing contract where they are permitted at all.

External mechanisms may enforce capability restrictions or collect evidence, but they do not become owners of Promptbook workflow policy.

## Status

`tested`
