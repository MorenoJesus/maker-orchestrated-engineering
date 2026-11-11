# Third-party notices

This repository includes a pinned copy of Engineering Clarity Standard (ECS) 1.0.0 by Jesus Moreno, supplied under the MIT License.

Source: https://github.com/MorenoJesus/engineering-clarity-standard/tree/871dbf7030cf18be6312fb0fca00b86d440f7a98

The unchanged upstream skill is in `.agents/skills/engineering-clarity/`; its managed copy is in `.claude/skills/engineering-clarity/`. Each includes the upstream [LICENSE](.agents/skills/engineering-clarity/LICENSE). The unchanged checker and another license copy are in [third_party/ecs/](third_party/ecs/README.md).

The [manifest](third_party/ecs/manifest.json) identifies imported paths, their upstream paths, Git blob IDs, and SHA-256 digests. MOE-specific profiles, adapters, examples, and validation code are separate from upstream ECS.

ECS draws inspiration from ASD-STE100. It does not reproduce the official controlled dictionary or establish formal ASD-STE100 compliance. The imported license applies to ECS, not the official aerospace standard.

The upstream MIT grant applies to ECS only. Original MOE material is licensed under the Apache License, Version 2.0. See [license status](LICENSE-STATUS.md).
