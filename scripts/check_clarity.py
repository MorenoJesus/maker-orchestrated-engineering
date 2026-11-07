#!/usr/bin/env python3
"""Run the unchanged, pinned ECS heuristic checker after checking package integrity."""
from pathlib import Path
import subprocess
import sys
from check_ecs import canonical_errors

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    errors = canonical_errors(ROOT)
    if errors:
        for error in errors:
            print(f'ERROR: {error}', file=sys.stderr)
        return 2
    return subprocess.run(
        [sys.executable, str(ROOT / 'third_party/ecs/check_clarity.py'), *sys.argv[1:]],
        check=False,
    ).returncode

if __name__ == '__main__':
    sys.exit(main())
