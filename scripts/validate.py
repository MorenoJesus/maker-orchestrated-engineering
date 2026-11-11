"""Validate MOE reference records. This is not a release or conformance gate."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from typing import Any
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
KINDS = ('mission', 'autonomy', 'delegation', 'proof-bundle', 'decision-record')
PRE_DELIVERY = {'draft', 'authorized', 'executing', 'awaiting_acceptance', 'accepted'}
# In this single-decision reference profile, the decision supplied must justify the mission's state.
STATE_DECISION = {'accepted': 'technical_acceptance', 'delivered': 'release', 'observing': 'release', 'closed': 'release'}

class MissingFormatSupport(RuntimeError):
    """A format the schemas rely on has no checker installed and would be silently skipped."""

def used_formats(node: Any) -> set[str]:
    """Collect every "format" keyword value in a schema."""
    if isinstance(node, dict):
        found = {node['format']} if isinstance(node.get('format'), str) else set()
        return found.union(*(used_formats(value) for value in node.values()))
    if isinstance(node, list):
        return set().union(*(used_formats(value) for value in node))
    return set()

def format_checker(schemas: dict[str, Any]) -> FormatChecker:
    """Return a checker covering every format the schemas use; fail closed if one is missing."""
    checker = FormatChecker()
    missing = sorted(used_formats(schemas) - set(checker.checkers))
    if missing:
        raise MissingFormatSupport(f'no checker installed for format(s): {", ".join(missing)}; install requirements.txt')
    return checker

def load_records(directory: Path) -> dict[str, Any]:
    return {kind: json.loads((directory / f'{kind}.json').read_text(encoding='utf-8')) for kind in KINDS}

def schema_registry() -> tuple[dict[str, Any], Registry]:
    schemas: dict[str, Any] = {}
    registry = Registry()
    for path in sorted((ROOT / 'contracts').glob('*.schema.json')):
        schema = json.loads(path.read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(schema)
        schemas[path.stem.removesuffix('.schema')] = schema
        registry = registry.with_resource(schema['$id'], Resource.from_contents(schema))
    return schemas, registry

def validate_records(records: dict[str, Any]) -> list[str]:
    """Return structural and selected consistency errors. No remote data is trusted."""
    errors: list[str] = []
    schemas, registry = schema_registry()
    formats = format_checker(schemas)
    for kind in KINDS:
        if kind not in records:
            errors.append(f'{kind}: missing record')
            continue
        validator = Draft202012Validator(schemas[kind], registry=registry, format_checker=formats)
        for error in sorted(validator.iter_errors(records[kind]), key=lambda e: str(list(e.path))):
            errors.append(f'{kind}:{"/".join(str(p) for p in error.path)}: {error.message}')
    if errors:
        return errors  # Do not evaluate malformed objects.
    m, p, d, b, a = (records[k] for k in KINDS)
    mr, pr = ({'id': x['id'], 'revision': x['revision']} for x in (m, p))
    for name, value in [('delegation', d), ('proof-bundle', b), ('decision-record', a)]:
        if value['mission'] != mr:
            errors.append(f'{name}: stale or wrong mission reference')
    for name, value in [('mission', m), ('delegation', d), ('proof-bundle', b), ('decision-record', a)]:
        if value['policy'] != pr:
            errors.append(f'{name}: stale or wrong policy reference')
    if len({r['record_mode'] for r in records.values()}) != 1:
        errors.append('records: fixture and operational modes cannot be mixed')
    if m['maker']['kind'] != 'human':
        errors.append('mission: maker must be human')
    if d['agent']['kind'] != 'agent':
        errors.append('delegation: agent kind must be agent')
    if a['actor']['id'] != m['authorities'][a['authority_role']]:
        errors.append('decision-record: actor does not match assigned authority')
    expected_roles = {'mission_authorization': 'authorize', 'technical_acceptance': 'accept', 'release': 'release', 'exception': 'exception'}
    if a['kind'] in expected_roles and a['authority_role'] != expected_roles[a['kind']]:
        errors.append('decision-record: kind does not match authority role')
    if a['actor']['kind'] == 'agent':
        errors.append('decision-record: agent cannot grant authority in this reference profile')
    if a['kind'] == 'rejection' and a['decision'] != 'reject':
        errors.append('decision-record: rejection kind must record a reject decision')
    if m['status'] in {'authorized', 'executing', 'awaiting_acceptance'}:
        if not (a['kind'] == 'mission_authorization' and a['decision'] == 'approve' and a['id'] in m['authorization_decision_ids']):
            errors.append('mission: reference profile requires matching approving authorization')
    if m['status'] in STATE_DECISION:
        if b['assessment'] != 'ready_for_acceptance':
            errors.append(f'mission: status {m["status"]} requires a proof bundle that is ready for acceptance')
        if not (a['kind'] == STATE_DECISION[m['status']] and a['decision'] == 'approve'):
            errors.append(f'mission: reference profile requires an approving {STATE_DECISION[m["status"]]} decision for status {m["status"]}')
    if b['outcome_observation'] in {'achieved', 'not_achieved'} and m['status'] in PRE_DELIVERY:
        errors.append('proof-bundle: outcome cannot be observed before delivery')
    if m['status'] == 'closed' and b['outcome_observation'] == 'not_yet_observed':
        errors.append('mission: closure requires a recorded observation result')
    if a['kind'] in {'technical_acceptance', 'release'}:
        if a['candidate_id'] != b['candidate']['id'] or a['proof_bundle'] != {'id': b['id'], 'revision': b['revision']}:
            errors.append('decision-record: stale or wrong candidate/proof bundle')
        if a['decision'] == 'approve' and b['assessment'] != 'ready_for_acceptance':
            errors.append('decision-record: cannot approve an incomplete bundle')
    allowed, denied = set(p['allowed_actions']), set(p['denied_actions'])
    if allowed & denied:
        errors.append('autonomy: allowed and denied actions conflict')
    if not set(p['approval_required_actions']) <= allowed:
        errors.append('autonomy: approval-required actions must be allowed actions')
    if not set(d['allowed_actions']) <= allowed or set(d['allowed_actions']) & denied:
        errors.append('delegation: unauthorized action')
    if not set(m['scope']['resources']) <= set(p['scope']['resources']):
        errors.append('mission: resource exceeds policy scope')
    if not set(d['resources']) <= set(m['scope']['resources']):
        errors.append('delegation: resource exceeds mission scope')
    if d['environment'] not in p['scope']['environments'] or b['candidate']['environment'] not in p['scope']['environments']:
        errors.append('records: environment exceeds policy scope')
    if m['scope']['data_classification'] not in p['scope']['data_classifications']:
        errors.append('mission: data classification exceeds policy scope')
    for key in p['budget']:
        if d['budget'][key] > p['budget'][key]:
            errors.append(f'delegation: budget exceeds policy for {key}')
    criteria = [c['id'] for c in m['acceptance_criteria']]
    if len(criteria) != len(set(criteria)):
        errors.append('mission: duplicate acceptance criterion')
    if not set(d['acceptance_criterion_ids']) <= set(criteria):
        errors.append('delegation: unknown acceptance criterion')
    checks = [c['id'] for c in b['checks']]
    if len(checks) != len(set(checks)):
        errors.append('proof-bundle: duplicate check ID')
    required = set(m['verification']['required_check_ids'])
    if not required <= set(checks):
        errors.append('proof-bundle: missing required check')
    mapped: set[str] = set()
    for check in b['checks']:
        mapped.update(check['criterion_ids'])
        if not set(check['criterion_ids']) <= set(criteria):
            errors.append('proof-bundle: unknown acceptance criterion')
        if check['id'] in required and not check['required']:
            errors.append('proof-bundle: required check marked optional')
        if check['required'] and check['producer']['kind'] == 'agent':
            errors.append('proof-bundle: required check cannot rely on agent self-report')
        if check['outcome'] == 'not_applicable' and not (check['decision_id'] == a['id'] and a['decision'] == 'approve'):
            errors.append('proof-bundle: not_applicable check must cite an approving decision in this record set')
        if b['assessment'] == 'ready_for_acceptance' and (check['required'] or check['id'] in required) and check['outcome'] != 'passed':
            errors.append('proof-bundle: required checks have not all passed; exceptions need a separate evaluator')
    if set(criteria) - mapped:
        errors.append('proof-bundle: unmapped acceptance criterion')
    return errors

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--example-dir', type=Path, default=ROOT / 'examples' / 'basic')
    parser.add_argument('--json', action='store_true', help='Emit machine-readable validation results.')
    args = parser.parse_args()
    try:
        records = load_records(args.example_dir)
        errors = validate_records(records)
        result = {'validation': 'failed' if errors else 'passed', 'scope': 'schema_and_selected_consistency_only', 'record_mode': records['mission'].get('record_mode', 'unknown'), 'application_tests': 'not_run', 'operational_authorization': 'not_evaluated', 'errors': errors}
    except (OSError, ValueError, KeyError, MissingFormatSupport) as exc:
        result = {'validation': 'failed', 'scope': 'schema_and_selected_consistency_only', 'errors': [str(exc)]}
        errors = result['errors']
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Reference validation: {result['validation'].upper()}")
        print('Scope: schemas and selected cross-record consistency. Not application verification or conformance certification.')
        for error in errors:
            print(f'  - {error}')
    return 1 if errors else 0

if __name__ == '__main__':
    sys.exit(main())
