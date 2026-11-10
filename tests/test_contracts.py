"""Exercise valid and rejected synthetic MOE records; no production work is tested."""
import copy
import importlib.util
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('moe_validate', ROOT / 'scripts' / 'validate.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class ContractTests(unittest.TestCase):
    def setUp(self):
        self.records = module.load_records(ROOT / 'examples' / 'basic')
    def rejected_with(self, text):
        """Require the specific error, so a record rejected for an unrelated reason fails the test."""
        errors = module.validate_records(self.records)
        self.assertTrue(any(text in error for error in errors), errors)
    def make_ready(self):
        """Mark every check passed with synthetic artifacts. Not genuine evidence."""
        b = self.records['proof-bundle']; b['assessment'] = 'ready_for_acceptance'
        for c in b['checks']:
            c.update(outcome='passed', run_id='synthetic-run', observed_at='2026-11-06T18:00:00Z', artifact_uri='https://example.invalid/artifacts/test.json', artifact_digest='sha256:' + 'c' * 64, reason='Synthetic positive fixture, not genuine evidence.')
        return b
    def decide(self, kind, role, actor_id):
        """Replace the single decision with a synthetic approving acceptance or release decision."""
        b = self.records['proof-bundle']
        self.records['decision-record'].update(kind=kind, authority_role=role, actor={'id': actor_id, 'kind': 'human'}, decision='approve', candidate_id=b['candidate']['id'], proof_bundle={'id': b['id'], 'revision': b['revision']}, rationale='Synthetic decision for a validator test; this is not a real approval.')
    def test_reference_fixture_is_consistent_but_incomplete(self):
        self.assertEqual([], module.validate_records(self.records))
        self.assertEqual('incomplete', self.records['proof-bundle']['assessment'])
    def test_missing_maker(self):
        del self.records['mission']['maker']; self.rejected_with("'maker' is a required property")
    def test_unknown_field(self):
        self.records['mission']['silent_override'] = True; self.rejected_with("'silent_override' was unexpected")
    def test_wrong_version(self):
        self.records['mission']['schema_version'] = '9.0.0'; self.rejected_with("'0.3.0' was expected")
    def test_stale_mission(self):
        self.records['delegation']['mission']['revision'] = 2; self.rejected_with('delegation: stale or wrong mission reference')
    def test_stale_policy(self):
        self.records['proof-bundle']['policy']['revision'] = 2; self.rejected_with('proof-bundle: stale or wrong policy reference')
    def test_unauthorized_action(self):
        self.records['delegation']['allowed_actions'].append('production.write'); self.rejected_with('delegation: unauthorized action')
    def test_conflicting_policy(self):
        self.records['autonomy']['denied_actions'].append('checks.run'); self.rejected_with('autonomy: allowed and denied actions conflict')
    def test_excessive_budget(self):
        self.records['delegation']['budget']['max_tool_calls'] = 300; self.rejected_with('delegation: budget exceeds policy for max_tool_calls')
    def test_unknown_criterion(self):
        self.records['proof-bundle']['checks'][0]['criterion_ids'] = ['AC-99']; self.rejected_with('proof-bundle: unknown acceptance criterion')
    def test_duplicate_check(self):
        self.records['proof-bundle']['checks'].append(copy.deepcopy(self.records['proof-bundle']['checks'][0])); self.rejected_with('proof-bundle: duplicate check ID')
    def test_missing_required_check(self):
        self.records['proof-bundle']['checks'].pop(); self.rejected_with('proof-bundle: missing required check')
    def test_required_marked_optional(self):
        self.records['proof-bundle']['checks'][0]['required'] = False; self.rejected_with('proof-bundle: required check marked optional')
    def test_false_ready_label(self):
        self.records['proof-bundle']['assessment'] = 'ready_for_acceptance'; self.rejected_with('required checks have not all passed')
    def test_pass_without_artifacts(self):
        self.records['proof-bundle']['checks'][0]['outcome'] = 'passed'; self.rejected_with("'artifact_digest' is a required property")
    def test_invalid_timestamp(self):
        self.records['decision-record']['recorded_at'] = 'yesterday'; self.rejected_with("is not a 'date-time'")
    def test_mismatched_authority(self):
        self.records['decision-record']['actor']['id'] = 'person:unknown'; self.rejected_with('decision-record: actor does not match assigned authority')
    def test_agent_cannot_be_maker(self):
        self.records['mission']['maker']['kind'] = 'agent'; self.rejected_with('mission: maker must be human')
    def test_resource_escape(self):
        self.records['delegation']['resources'] = ['repo:other/private']; self.rejected_with('delegation: resource exceeds mission scope')
    def test_mixed_record_modes(self):
        self.records['proof-bundle']['record_mode'] = 'operational'; self.rejected_with('fixture and operational modes cannot be mixed')
    def test_invalid_digest(self):
        self.records['proof-bundle']['candidate']['artifact_digest'] = 'sha256:guess'; self.rejected_with("does not match '^sha256:")
    def test_unmapped_criterion(self):
        self.records['proof-bundle']['checks'][0]['criterion_ids'] = []; self.rejected_with('proof-bundle: unmapped acceptance criterion')
    def test_agent_self_report(self):
        self.records['proof-bundle']['checks'][0]['producer']['kind'] = 'agent'; self.rejected_with('required check cannot rely on agent self-report')
    def test_unapproved_authorization(self):
        self.records['decision-record']['decision'] = 'defer'; self.rejected_with('requires matching approving authorization')
    def test_ready_fixture_with_artifacts_validates_structure_only(self):
        b = self.make_ready()
        self.assertEqual([], module.validate_records(self.records))
        self.assertEqual('fixture', b['record_mode'])

    # Formats: a missing checker must fail loudly instead of skipping the check.
    def test_invalid_policy_expiry(self):
        self.records['autonomy']['expires_at'] = 'never'; self.rejected_with("is not a 'date-time'")
    def test_invalid_artifact_uri(self):
        self.make_ready()['checks'][0]['artifact_uri'] = 'not a uri at all'; self.rejected_with("is not a 'uri'")
    def test_unsupported_format_fails_closed(self):
        with self.assertRaises(module.MissingFormatSupport):
            module.format_checker({'example': {'type': 'string', 'format': 'no-such-format'}})

    # Later mission states need evidence and the decision that justifies the state.
    def test_later_states_without_evidence(self):
        for status in ('accepted', 'delivered', 'observing', 'closed'):
            with self.subTest(status=status):
                self.records['mission']['status'] = status; self.rejected_with('requires a proof bundle that is ready for acceptance')
    def test_accepted_needs_acceptance_decision(self):
        self.make_ready(); self.records['mission']['status'] = 'accepted'
        self.rejected_with('requires an approving technical_acceptance decision')
    def test_delivered_needs_release_decision(self):
        self.make_ready(); self.decide('technical_acceptance', 'accept', 'person:reviewer-example')
        self.records['mission']['status'] = 'delivered'; self.rejected_with('requires an approving release decision')
    def test_accepted_fixture_validates_structure_only(self):
        self.make_ready(); self.decide('technical_acceptance', 'accept', 'person:reviewer-example')
        self.records['mission']['status'] = 'accepted'
        self.assertEqual([], module.validate_records(self.records))
    def test_delivered_fixture_validates_structure_only(self):
        self.make_ready(); self.decide('release', 'release', 'person:release-example')
        self.records['mission']['status'] = 'delivered'
        self.assertEqual([], module.validate_records(self.records))
    def test_outcome_observed_before_delivery(self):
        self.records['proof-bundle']['outcome_observation'] = 'achieved'; self.rejected_with('outcome cannot be observed before delivery')
    def test_closed_without_observation_result(self):
        self.make_ready(); self.decide('release', 'release', 'person:release-example')
        self.records['mission']['status'] = 'closed'; self.rejected_with('closure requires a recorded observation result')
    def test_closed_fixture_keeps_unknown_outcome(self):
        b = self.make_ready(); self.decide('release', 'release', 'person:release-example')
        self.records['mission']['status'] = 'closed'; b['outcome_observation'] = 'unknown'
        self.assertEqual([], module.validate_records(self.records))

    # References and decision coherence.
    def test_not_applicable_unknown_decision(self):
        self.records['proof-bundle']['checks'][0].update(outcome='not_applicable', decision_id='DECISION-404')
        self.rejected_with('not_applicable check must cite an approving decision')
    def test_not_applicable_cites_known_decision(self):
        self.records['proof-bundle']['checks'][0].update(outcome='not_applicable', decision_id='DECISION-001')
        self.assertEqual([], module.validate_records(self.records))
    def test_rejection_kind_cannot_approve(self):
        self.records['mission']['status'] = 'draft'; self.records['decision-record']['kind'] = 'rejection'
        self.rejected_with('rejection kind must record a reject decision')
    def test_rejection_kind_records_reject(self):
        self.records['mission']['status'] = 'draft'; self.records['decision-record'].update(kind='rejection', decision='reject')
        self.assertEqual([], module.validate_records(self.records))

if __name__ == '__main__':
    unittest.main()
