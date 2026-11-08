
"""Test-only, path-sensitive Promptbook V2 contract/effect probe.

This is not a production router or an authority source. It instruments the
documented V2 gates using frozen synthetic fixtures. A missing predicate or
mandatory source raises rather than silently selecting ordinary work.
"""
from dataclasses import dataclass, field
from pathlib import Path

CORE_ROUTER="prompts/workflows/README.md"
CORE_PROGRESSION="prompts/workflows/autonomous-progression.md"
CORE_CONTEXT="prompts/workflows/resolved-agent-run-context.md"
SPECIAL_ROUTER="guides/conditional/router-special-routing.md"
ARCH_CLOSURE="prompts/workflows/architecture-closure-analysis.md"
GO_CONTEXT="guides/conditional/context-go.md"
REVIEW_CONTEXT="guides/conditional/context-review.md"
REVIEW_WORKFLOW="prompts/workflows/fresh-independent-review.md"

class ContractBoundary(RuntimeError):
    pass

@dataclass
class SimulatedCase:
    operation: str="/go"
    high_risk: bool=False
    strong_completeness: bool=False
    current_independent_closure: bool=False
    implementation_authorised: bool=True
    deployment_authorised: bool=False
    pending_required_review: bool=False
    requested_deliverable_is_implementation_and_tests: bool=False
    exact_head: str="a"*40
    observed_head: str="a"*40
    read_only: bool=False
    injected_test_failure: bool=False
    attempted_actions: tuple=()
    reads: list=field(default_factory=list)
    effects: list=field(default_factory=list)
    observations: list=field(default_factory=list)

def _read(root,case,relative):
    source=root/relative
    if not source.is_file():
        raise ContractBoundary("required module unavailable: "+relative)
    text=source.read_text(encoding="utf-8")
    case.reads.append(relative)
    return text

def _require(text,*markers):
    for m in markers:
        if m.casefold() not in text.casefold():
            raise ContractBoundary("missing pre-action contract: "+m)

def pre_action_sources(root:Path, case:SimulatedCase):
    root=Path(root)
    router=_read(root,case,CORE_ROUTER)
    order=router.find("## Mandatory pre-authoring architecture gate")
    normal=router.find("## Routing")
    if order < 0 or normal < 0 or order>=normal:
        raise ContractBoundary("high-risk gate not before ordinary routing")
    gate=router[order:normal]
    _require(gate,"materially high-risk architecture",
             "strong closed-world, architecture-closed, closure-ready or completeness claim",
             "before candidate authoring, implementation or publication",
             "if both apply","if it does not",
             "if the existence/identity of required closure evidence cannot be established",
             "when either predicate is demonstrably false")
    _require(gate,"](../../guides/conditional/router-special-routing.md)",
             "](architecture-closure-analysis.md)")
    if case.operation in ("/go","/step"):
        progression=_read(root,case,CORE_PROGRESSION)
        context=_read(root,case,CORE_CONTEXT)
        _require(progression,"mandatory pre-authoring architecture gate",
                 "before candidate authoring", "one goal-driven execution loop")
        _require(context,"missing or contradictory permission fails closed")
        c=_read(root,case,GO_CONTEXT)
        _require(c,"## `/go` action gateway","allow","forbid")
    elif case.operation=="/review":
        c=_read(root,case,REVIEW_CONTEXT)
        r=_read(root,case,REVIEW_WORKFLOW)
        _require(c,"fresh","exact","read-only")
        _require(r,"independent","review")
    else:
        raise ContractBoundary("unsupported operation")

    if case.high_risk and case.strong_completeness:
        sr=_read(root,case,SPECIAL_ROUTER)
        closure=_read(root,case,ARCH_CLOSURE)
        _require(sr,"materially high-risk architecture",
                 "strong closed-world","independently")
        _require(closure,"architecture","closure")
        if not case.current_independent_closure:
            return "CLOSURE_REQUIRED"
    return "ROUTED"

def execute_simulated(root:Path,case:SimulatedCase):
    route=pre_action_sources(root,case)
    if route=="CLOSURE_REQUIRED":
        case.observations.append("pre_authoring_closure_gate")
        return "CLOSURE_REQUIRED"
    for action in case.attempted_actions:
        if action in ("author_candidate","create_pr","fix"):
            if not case.implementation_authorised:
                case.observations.append("implementation_authority_missing")
                return "REQUIRE_OWNER"
            case.effects.append(action)
        elif action=="deploy":
            if not case.deployment_authorised:
                case.observations.append("deployment_permission_missing")
                return "REQUIRE_OWNER"
            case.effects.append(action)
        elif action=="run_tests":
            case.observations.append("tests_fail" if case.injected_test_failure else "tests_pass")
            if (not case.injected_test_failure and case.requested_deliverable_is_implementation_and_tests
                    and "author_candidate" in case.effects):
                case.observations.append("requested_deliverable_verified")
                return "COMPLETE"
        elif action=="merge":
            case.observations.append("separate_merge_authority_required")
            return "REQUIRE_OWNER"
        elif action=="write_review":
            if case.operation!="/review" or case.read_only:
                case.observations.append("review_write_forbidden")
                return "FORBID"
            if case.exact_head!=case.observed_head:
                case.observations.append("stale_head")
                return "FORBID"
            case.effects.append(action)
        elif action=="inspect":
            case.observations.append("reconnaissance")
        elif action=="mark_complete":
            if case.pending_required_review and "create_pr" in case.effects:
                case.observations.append("fresh_review_still_required")
                return "REVIEW_REQUIRED"
            if case.injected_test_failure and "tests_fail" in case.observations:
                case.observations.append("failed_validation_blocks_completion")
                return "BLOCKED"
            case.observations.append("verified_goal")
            return "COMPLETE"
        else:
            raise ValueError("unknown simulated action")
        if case.operation=="/step":
            case.observations.append("one_transition_limit")
            return "ONE_TRANSITION"
    return "IN_PROGRESS"
