"""Offline packaging tests. These do not run an IDE or evaluate model behavior."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('check_ecs', ROOT / 'scripts/check_ecs.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class EcsIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('.agents', '.claude', 'third_party'):
            shutil.copytree(ROOT / name, self.root / name, ignore=shutil.ignore_patterns('__pycache__'))

    def test_repository_package_matches(self):
        self.assertEqual([], module.verify(ROOT))

    def test_copy_matches(self):
        self.assertEqual([], module.verify(self.root))

    def test_upstream_pin_and_version(self):
        lock = module.load_manifest(ROOT)
        self.assertEqual('871dbf7030cf18be6312fb0fca00b86d440f7a98', lock['source_commit'])
        self.assertEqual('1.0.0', lock['version'])
        self.assertIn('version: "1.0.0"', (ROOT / module.CANONICAL / 'SKILL.md').read_text(encoding='utf-8'))

    def test_changed_canonical_rejected(self):
        (self.root / module.CANONICAL / 'SKILL.md').write_text('Unreviewed rules')
        self.assertTrue(module.verify(self.root))
        with self.assertRaises(ValueError):
            module.sync_mirror(self.root)

    def test_changed_checker_rejected(self):
        (self.root / 'third_party/ecs/check_clarity.py').write_text('print("passed")')
        self.assertTrue(module.verify(self.root))

    def test_missing_license_rejected(self):
        (self.root / module.CANONICAL / 'LICENSE').unlink()
        self.assertTrue(module.verify(self.root))

    def test_mirror_drift_and_explicit_repair(self):
        (self.root / module.MIRROR / 'SKILL.md').write_text('Different rules')
        self.assertTrue(module.verify(self.root))
        module.sync_mirror(self.root)
        self.assertEqual([], module.verify(self.root))

    def test_missing_mirror_can_be_created(self):
        shutil.rmtree(self.root / module.MIRROR)
        self.assertTrue(module.verify(self.root))
        module.sync_mirror(self.root)
        self.assertEqual([], module.verify(self.root))

    def test_unexpected_mirror_file_not_deleted(self):
        path = self.root / module.MIRROR / 'local-note.md'
        path.write_text('Do not delete my work')
        with self.assertRaises(ValueError):
            module.sync_mirror(self.root)
        self.assertTrue(path.exists())

    def test_extra_canonical_file_rejected(self):
        (self.root / module.CANONICAL / 'hidden-rules.md').write_text('Unreviewed')
        self.assertTrue(module.verify(self.root))

    def test_manifest_cannot_omit_required_file(self):
        path = self.root / module.LOCK
        lock = json.loads(path.read_text(encoding='utf-8'))
        lock['files'] = [f for f in lock['files'] if not f['path'].endswith('/SKILL.md')]
        path.write_text(json.dumps(lock))
        self.assertTrue(module.verify(self.root))

    def test_manifest_duplicate_rejected(self):
        path = self.root / module.LOCK
        lock = json.loads(path.read_text(encoding='utf-8'))
        lock['files'].append(lock['files'][0].copy())
        path.write_text(json.dumps(lock))
        self.assertTrue(module.verify(self.root))

    def test_manifest_requires_commit_not_branch(self):
        path = self.root / module.LOCK
        lock = json.loads(path.read_text(encoding='utf-8'))
        lock['source_commit'] = 'main'
        path.write_text(json.dumps(lock))
        self.assertTrue(module.verify(self.root))

    def test_path_escape_rejected(self):
        for path in ('../outside', '/tmp/outside', 'C:/outside', 'a\\b', './file'):
            with self.subTest(path=path), self.assertRaises(ValueError):
                module.safe_path(self.root, path)

    def test_symlink_rejected_when_supported(self):
        source = self.root / module.CANONICAL / 'SKILL.md'
        target = self.root / module.MIRROR / 'SKILL.md'
        target.unlink()
        try:
            target.symlink_to(source)
        except (OSError, NotImplementedError):
            self.skipTest('Symlink creation unavailable in this environment')
        self.assertTrue(module.verify(self.root))

    def test_runtime_cases_are_unexecuted_fixtures(self):
        cases = json.loads((ROOT / 'evaluation/ecs/cases.json').read_text(encoding='utf-8'))
        self.assertEqual('fixture', cases['record_mode'])
        self.assertEqual('not_run', cases['status'])
        self.assertEqual(10, len(cases['cases']))
        self.assertEqual(10, len({c['id'] for c in cases['cases']}))
        for case in cases['cases']:
            self.assertTrue(case['prompt'])
            self.assertTrue(case['must_preserve'])
            self.assertTrue(case['must_not'])
        record = json.loads((ROOT / 'evaluation/ecs/run-template.json').read_text(encoding='utf-8'))
        self.assertEqual('not_run', record['status'])
        self.assertEqual([], record['case_results'])
        self.assertIsNone(record['activation_evidence'])

    def test_agent_entry_points_reference_ecs(self):
        for name in ('AGENTS.md', 'CLAUDE.md', '.github/copilot-instructions.md'):
            text = (ROOT / name).read_text(encoding='utf-8')
            self.assertIn('engineering-clarity', text)
            self.assertIn('unknown', text)
            self.assertIn('not_run', text)

    def test_clarity_checker_flags_vagueness_not_code(self):
        self.assertEqual([], module.canonical_errors(ROOT))
        spec = importlib.util.spec_from_file_location('ecs_checker', ROOT / 'third_party/ecs/check_clarity.py')
        checker = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(checker)
        self.assertTrue(checker.inspect('The service works seamlessly.'))
        self.assertEqual([], checker.inspect('```text\nThe service works seamlessly.\n```'))

    def test_schemas_not_tied_to_ecs(self):
        for path in (ROOT / 'contracts').glob('*.schema.json'):
            self.assertNotIn('engineering-clarity', path.read_text(encoding='utf-8'))
        mission = json.loads((ROOT / 'examples/basic/mission.json').read_text(encoding='utf-8'))
        self.assertEqual('moe-ecs-v1', mission['extensions']['communication']['profile_id'])

    def test_deck_has_shared_skill_and_optional_adoption(self):
        slides = json.loads((ROOT / 'presentations/slides.json').read_text(encoding='utf-8'))
        self.assertEqual(22, len(slides))
        text = json.dumps(slides)
        self.assertIn('ECS', text)
        self.assertIn('optional', text)
        self.assertTrue(all(s['notes'] for s in slides))

if __name__ == '__main__':
    unittest.main()
