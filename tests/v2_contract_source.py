"""Active Promptbook V2 contract reconstruction for semantic regression tests.

The established V1 regression assertions still run against the complete set of
live, conditionally reachable V2 clauses. Separate V2 tests validate that each
specialist clause is explicitly routed and is excluded from the ordinary read.
"""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DETAILS={
 "prompts/workflows/README.md": (
  "router-review-response","router-special-routing","router-single-maintainer",
  "router-decision","router-terminal-handover",
 ),
 "prompts/workflows/autonomous-progression.md": (
  "progression-review-closure","progression-capabilities","progression-locality",
  "progression-boundaries","progression-recovery",
 ),
 "prompts/workflows/resolved-agent-run-context.md": (
  "context-review","context-fix","context-go","context-save",
  "context-shared",
 ),
}

def read_effective_contract(path):
    path=Path(path)
    content=path.read_text(encoding="utf-8")
    try:
        relative=path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return content
    for name in DETAILS.get(relative,()):
        target=ROOT/"guides"/"conditional"/(name+".md")
        # The canonical entry point must contain a real discoverable link to
        # every expected specialist contract, not a disconnected archive.
        exact="../../guides/conditional/"+name+".md"
        if exact not in content:
            raise AssertionError(f"unreachable V2 contract: {relative} -> {name}")
        content+="\n"+target.read_text(encoding="utf-8")
    return content
