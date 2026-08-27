import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReviewWritebackContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = (ROOT / "prompts" / "workflows" / "README.md").read_text(
            encoding="utf-8"
        )
        cls.router_lower = cls.router.lower()
        cls.fresh = (
            ROOT / "prompts" / "workflows" / "fresh-independent-review.md"
        ).read_text(encoding="utf-8")
        cls.fresh_lower = cls.fresh.lower()
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")
        cls.readme_lower = cls.readme.lower()
        cls.guide = (ROOT / "guides" / "project-bootstrap.md").read_text(
            encoding="utf-8"
        )
        cls.guide_lower = cls.guide.lower()
        cls.bootstrap = (ROOT / "BOOTSTRAP").read_text(encoding="utf-8")
        cls.bootstrap_lower = cls.bootstrap.lower()
        cls.standalone = (
            ROOT / "prompts" / "engineering" / "pr-review.md"
        ).read_text(encoding="utf-8")
        cls.standalone_lower = cls.standalone.lower()

    def test_router_review_records_by_default(self):
        self.assertIn(
            "ordinary `/review` includes the narrow authority to durably record the "
            "requested review on github",
            self.router_lower,
        )
        self.assertIn("refreshing the exact candidate/head", self.router_lower)
        self.assertIn("review-recording authority does not grant remediation", self.router_lower)
        self.assertIn("| `/review` | `suggest` |", self.router)

    def test_read_only_mode_is_explicit_zero_write(self):
        self.assertIn("`/review --read-only [target]`", self.router)
        self.assertIn("performs the same assessment with zero github write-back", self.router_lower)
        self.assertIn("`review without mutation`", self.router)
        self.assertIn("`review only in chat`", self.router)
        self.assertIn("suppress every review-record mutation", self.fresh_lower)
        for prohibited_write in (
            "formal review",
            "top-level review body/comment",
            "inline review comment",
            "issue/pr fallback comment",
            "single-maintainer durable fallback record",
        ):
            self.assertIn(prohibited_write, self.fresh_lower)
        self.assertIn("report the logical disposition in chat only", self.fresh_lower)

    def test_github_event_mapping_preserves_logical_state(self):
        self.assertIn("map an approval/no-blocking-findings result to github `approve`", self.fresh_lower)
        self.assertIn("material blockers requiring correction before acceptance to `request_changes`", self.fresh_lower)
        self.assertIn("use `comment` for neutral/advisory reviews", self.fresh_lower)
        self.assertIn("do not force an undecidable or non-formal logical result", self.fresh_lower)
        self.assertIn("false formal github state", self.fresh_lower)

    def test_review_submission_refreshes_exact_candidate(self):
        self.assertIn("immediately before submitting a github review record", self.fresh_lower)
        self.assertIn("refresh the exact pull-request/head identity", self.fresh_lower)
        self.assertIn("bind the review to the candidate actually inspected", self.fresh_lower)
        self.assertIn("do not blindly submit it", self.fresh_lower)
        self.assertIn("re-review the changed candidate", self.fresh_lower)

    def test_inline_comments_are_material_and_optional(self):
        self.assertIn("inline review comments may accompany the review only when", self.fresh_lower)
        self.assertIn("materially improves precision", self.fresh_lower)
        self.assertIn("do not create inline comments to satisfy a count", self.fresh_lower)
        self.assertIn("duplicate the top-level rationale", self.fresh_lower)

    def test_single_maintainer_writeback_is_honest(self):
        self.assertIn("do not attempt a formal self-`approve` or self-`request_changes`", self.fresh_lower)
        self.assertIn("permitted `comment` review", self.fresh_lower)
        self.assertIn("durable pr comment", self.fresh_lower)
        self.assertIn("distinguish that record from formal platform review state", self.fresh_lower)
        self.assertIn("when read-only mode is active, do not create that fallback record", self.fresh_lower)
        self.assertIn("not formal platform review state", self.router_lower)

    def test_review_record_does_not_leak_lifecycle_authority(self):
        for prohibited in (
            "merge",
            "release",
            "deployment",
            "settings",
            "credential",
            "production",
        ):
            self.assertIn(prohibited, self.router_lower)
            self.assertIn(prohibited, self.fresh_lower)
        self.assertIn("a recorded `approve` is review evidence/state, not merge authority", self.fresh_lower)
        self.assertIn("a recorded `request_changes` identifies blockers, not remediation authority", self.fresh_lower)
        self.assertIn("suggest `/fix` only when bounded remediation is already the safely authorised next path", self.fresh_lower)
        self.assertIn("prefer `/go` targeting the governing objective", self.fresh_lower)

    def test_repository_local_rules_remain_higher_precedence(self):
        self.assertIn("repository-local instructions", self.router_lower)
        self.assertIn("remain higher precedence", self.router_lower)
        self.assertIn("repository-local requirements for distinct reviewers", self.fresh_lower)
        self.assertIn("no-write operation still take precedence", self.fresh_lower)
        self.assertIn("stronger rule requires formal or distinct-person approval", self.fresh_lower)

    def test_public_surfaces_expose_refined_authority_model(self):
        self.assertIn("record the requested github review by default", self.readme_lower)
        self.assertIn("`/review --read-only`", self.readme)
        self.assertIn("commands do not grant unrelated authority", self.readme_lower)
        self.assertIn("record the requested review on github by default", self.guide_lower)
        self.assertIn("`/review --read-only [target]`", self.guide)
        self.assertIn("does not grant unrelated authority", self.bootstrap_lower)
        self.assertIn("narrow authority intrinsic to the operation", self.bootstrap_lower)

    def test_bootstrap_copy_remains_exactly_aligned(self):
        self.assertIn(f"```text\n{self.bootstrap.strip()}\n```", self.guide)

    def test_standalone_pr_review_does_not_gain_implicit_writeback(self):
        self.assertNotIn("write-back", self.standalone_lower)
        self.assertNotIn("durably record", self.standalone_lower)
        self.assertNotIn("request_changes", self.standalone_lower)
        self.assertNotIn("github `approve`", self.standalone_lower)
        self.assertIn("conclude with exactly one disposition", self.standalone_lower)


if __name__ == "__main__":
    unittest.main()
