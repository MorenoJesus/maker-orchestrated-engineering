#!/usr/bin/env python3
"""Check pinned ECS bytes and the managed mirror; never fetch or update upstream."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = '.agents/skills/engineering-clarity'
MIRROR = '.claude/skills/engineering-clarity'
LOCK = 'third_party/ecs/manifest.json'
REQUIRED = {
    'SKILL.md', 'LICENSE', 'references/standard.md', 'references/artifact-rules.md',
    'references/glossary.md', 'examples/before-after.md', 'assets/adr.md',
    'assets/api-contract.md', 'assets/implementation-plan.md', 'assets/pull-request.md',
    'assets/runbook.md', 'assets/user-story.md',
}

def safe_path(root: Path, relative: str) -> Path:
    """Reject traversal, absolute paths and symlinks before reading or writing."""
    posix = PurePosixPath(relative)
    if (not relative or posix.is_absolute() or '..' in posix.parts or
            '\\' in relative or ':' in relative or str(posix) != relative):
        raise ValueError(f'Unsafe package path: {relative!r}')
    base = root.resolve()
    path = base
    for part in posix.parts:
        path /= part
        if path.is_symlink():
            raise ValueError(f'Symlink not permitted in managed package: {relative}')
    if not path.resolve().is_relative_to(base):
        raise ValueError(f'Path leaves repository: {relative}')
    return path

def load_manifest(root: Path) -> dict:
    manifest = json.loads(safe_path(root, LOCK).read_text(encoding='utf-8'))
    if not isinstance(manifest, dict):
        raise ValueError('Manifest must be an object')
    if manifest.get('manifest_version') != 1:
        raise ValueError('Unsupported ECS manifest version')
    if manifest.get('name') != 'engineering-clarity' or manifest.get('license') != 'MIT':
        raise ValueError('Unexpected ECS package identity or license; review the updater')
    if manifest.get('source_repository') != 'https://github.com/MorenoJesus/engineering-clarity-standard':
        raise ValueError('Unexpected upstream repository')
    if not re.fullmatch(r'[0-9a-f]{40}', str(manifest.get('source_commit', ''))):
        raise ValueError('Upstream must be pinned to a full commit SHA')
    if manifest.get('canonical_skill_root') != CANONICAL or manifest.get('mirror_roots') != [MIRROR]:
        raise ValueError('Unexpected managed package directories')
    if not isinstance(manifest.get('files'), list):
        raise ValueError('Manifest files must be a list')
    return manifest

def inventory(root: Path, relative: str) -> set[str]:
    directory = safe_path(root, relative)
    if not directory.is_dir():
        return set()
    found = set()
    for path in directory.rglob('*'):
        rel = path.relative_to(root.resolve()).as_posix()
        safe_path(root, rel)
        if path.is_file():
            found.add(path.relative_to(directory).as_posix())
    return found

def canonical_errors(root: Path) -> list[str]:
    errors = []
    try:
        manifest = load_manifest(root)
        seen = set()
        names = set()
        for entry in manifest['files']:
            if not isinstance(entry, dict):
                raise ValueError('File entry must be an object')
            relative = entry['path']
            if relative in seen:
                errors.append(f'Duplicate manifest path: {relative}')
            seen.add(relative)
            if relative.startswith(CANONICAL + '/'):
                name = relative[len(CANONICAL) + 1:]
                names.add(name)
                source = 'LICENSE' if name == 'LICENSE' else relative
            elif relative in ('third_party/ecs/LICENSE', 'third_party/ecs/check_clarity.py'):
                source = 'LICENSE' if relative.endswith('/LICENSE') else 'scripts/check_clarity.py'
            else:
                raise ValueError(f'Unmanaged upstream path: {relative}')
            if entry.get('upstream_path') != source:
                errors.append(f'Incorrect upstream mapping: {relative}')
            path = safe_path(root, relative)
            if not path.is_file():
                errors.append(f'Missing pinned file: {relative}')
                continue
            data = path.read_bytes()
            blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            if hashlib.sha256(data).hexdigest() != entry.get('sha256') or blob != entry.get('git_blob_sha'):
                errors.append(f'Pinned bytes changed: {relative}')
        if not REQUIRED <= names:
            errors.append('Required skill files missing from manifest')
        if not {'third_party/ecs/LICENSE', 'third_party/ecs/check_clarity.py'} <= seen:
            errors.append('Checker or license missing from manifest')
        if inventory(root, CANONICAL) != names:
            errors.append('Canonical inventory does not match manifest')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f'Invalid ECS package: {exc}')
    return errors

def verify(root: Path = ROOT) -> list[str]:
    errors = canonical_errors(root)
    if errors:
        return errors
    try:
        source_names = inventory(root, CANONICAL)
        target_names = inventory(root, MIRROR)
        if source_names != target_names:
            errors.append('Managed mirror inventory differs from canonical skill')
        for name in source_names & target_names:
            if safe_path(root, f'{CANONICAL}/{name}').read_bytes() != safe_path(root, f'{MIRROR}/{name}').read_bytes():
                errors.append(f'Managed mirror differs: {name}')
    except (OSError, ValueError) as exc:
        errors.append(str(exc))
    return errors

def sync_mirror(root: Path = ROOT) -> None:
    """Explicitly replace managed mirror bytes; refuse unexpected files or bad input."""
    errors = canonical_errors(root)
    if errors:
        raise ValueError('; '.join(errors))
    source_names = inventory(root, CANONICAL)
    if inventory(root, MIRROR) - source_names:
        raise ValueError('Unexpected mirror files; review them before synchronization')
    for name in sorted(source_names):
        source = safe_path(root, f'{CANONICAL}/{name}')
        target = safe_path(root, f'{MIRROR}/{name}')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source.read_bytes())

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sync', action='store_true', help='Explicitly replace managed mirror files from verified canonical bytes.')
    args = parser.parse_args()
    try:
        if args.sync:
            sync_mirror()
        errors = verify()
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    if errors:
        for error in errors:
            print(f'ERROR: {error}', file=sys.stderr)
        return 1
    print('ECS package and managed mirror match the reviewed lock manifest.')
    print('This checks local integrity, not upstream authenticity or agent behavior.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
