# MOE repository guidance

Read `AGENTS.md` before working in this repository. Use the `engineering-clarity` skill in `.claude/skills/engineering-clarity/SKILL.md` for technical writing and review. It is a managed copy of the pinned canonical skill in `.agents/skills/engineering-clarity/`.

Read `implementation/ecs-integration.md` and `docs/glossary.md`. Preserve identifiers, schema values, source quotes, and raw evidence. Missing results mean `unknown`; known non-execution means `not_run`. Do not invent approvals or successful checks. Give each writing subagent the relevant skill and glossary explicitly.

ECS remains optional for organizations adopting MOE. It does not replace runtime permissions, verification, or human accountability. Do not edit managed copies independently. Skill activation and behavior require the evaluation in `evaluation/ecs/README.md`; they are not established by these instructions alone.
