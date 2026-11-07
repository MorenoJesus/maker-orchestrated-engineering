# Pinned ECS dependency

ECS version: **1.0.0**. Source commit: **871dbf7030cf18be6312fb0fca00b86d440f7a98**.

This directory contains the unchanged upstream heuristic checker, its MIT license, and a lock manifest. The canonical imported skill lives in `.agents/skills/engineering-clarity/` at the repository root. The managed Claude copy contains identical bytes.

Do not edit imported files in place or update the manifest merely to silence a drift error. Review an upstream revision, preserve license and attribution, compare source blobs, and update the package through a reviewed change.

Run `python scripts/check_ecs.py` from the repository root to check integrity. Run `python scripts/check_clarity.py <document.md>` to use the pinned checker. These commands do not fetch upstream content or evaluate a model session.

The manifest is a reviewable trust anchor, not a signature. Changing both the lock and the imported files can satisfy local hashes; code review and source provenance remain necessary.

See [integration guidance](../../implementation/ecs-integration.md) and [notices](../../THIRD-PARTY-NOTICES.md).
