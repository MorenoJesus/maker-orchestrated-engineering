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
    def rejected(self):
        self.assertTrue(module.validate_records(self.records))
    def test_reference_fixture_is_consistent_but_incomplete(self):
        self.assertEqual([], module.validate_records(self.records))
        self.assertEqual('incomplete', self.records['proof-bundle']['assessment'])
    def test_missing_maker(self):
        del self.records['mission']['maker']; self.rejected()
    def test_unknown_field(self):
        self.records['mission']['silent_override'] = True; self.rejected()
    def test_wrong_version(self):
        self.records['mission']['schema_version'] = '9.0.0'; self.rejected()
    def test_stale_mission(self):
        self.records['delegation']['mission']['revision'] = 2; self.rejected()
    def test_stale_policy(self):
        self.records['proof-bundle']['policy']['revision'] = 2; self.rejected()
    def test_unauthorized_action(self):
        self.records['delegation']['allowed_actions'].append('production.write'); self.rejected()
    def test_conflicting_policy(self):
        self.records['autonomy']['denied_actions'].append('checks.run'); self.rejected()
    def test_excessive_budget(self):
        self.records['delegation']['budget']['max_tool_calls'] = 300; self.rejected()
    def test_unknown_criterion(self):
        self.records['proof-bundle']['checks'][0]['criterion_ids'] = ['AC-99']; self.rejected()
    def test_duplicate_check(self):
        self.records['proof-bundle']['checks'].append(copy.deepcopy(self.records['proof-bundle']['checks'][0])); self.rejected()
    def test_missing_required_check(self):
        self.records['proof-bundle']['checks'].pop(); self.rejected()
    def test_required_marked_optional(self):
        self.records['proof-bundle']['checks'][0]['required'] = False; self.rejected()
    def test_false_ready_label(self):
        self.records['proof-bundle']['assessment'] = 'ready_for_acceptance'; self.rejected()
    def test_pass_without_artifacts(self):
        self.records['proof-bundle']['checks'][0]['outcome'] = 'passed'; self.rejected()
    def test_invalid_timestamp(self):
        self.records['decision-record']['recorded_at'] = 'yesterday'; self.rejected()
    def test_mismatched_authority(self):
        self.records['decision-record']['actor']['id'] = 'person:unknown'; self.rejected()
    def test_agent_cannot_be_maker(self):
        self.records['mission']['maker']['kind'] = 'agent'; self.rejected()
    def test_resource_escape(self):
        self.records['delegation']['resources'] = ['repo:other/private']; self.rejected()
    def test_mixed_record_modes(self):
        self.records['proof-bundle']['record_mode'] = 'operational'; self.rejected()
    def test_invalid_digest(self):
        self.records['proof-bundle']['candidate']['artifact_digest'] = 'sha256:guess'; self.rejected()
    def test_unmapped_criterion(self):
        self.records['proof-bundle']['checks'][0]['criterion_ids'] = []; self.rejected()
    def test_agent_self_report(self):
        self.records['proof-bundle']['checks'][0]['producer']['kind'] = 'agent'; self.rejected()
    def test_unapproved_authorization(self):
        self.records['decision-record']['decision'] = 'defer'; self.rejected()
    def test_ready_fixture_with_artifacts_validates_structure_only(self):
        b = self.records['proof-bundle']; b['assessment'] = 'ready_for_acceptance'
        for c in b['checks']:
            c.update(outcome='passed', run_id='synthetic-run', observed_at='2026-11-06T18:00:00Z', artifact_uri='https://example.invalid/artifacts/test.json', artifact_digest='sha256:' + 'c' * 64, reason='Synthetic positive fixture, not genuine evidence.')
        self.assertEqual([], module.validate_records(self.records))
        self.assertEqual('fixture', b['record_mode'])

if __name__ == '__main__':
    unittest.main()
