# Engineering Clarity Standard integration

**MOE 0.3.0 working draft | Repository adoption and optional organizational profile**

## Decision and scope

The MOE project uses Engineering Clarity Standard (ECS) for engineering prose that contributors create or revise. This includes specifications, contracts, agent instructions, pull requests, examples, and speaker notes. Existing text is not claimed to have passed an exhaustive ECS review.

For organizations adopting MOE, ECS is the recommended reference communication standard, not a core-conformance dependency. Organizations may use another standard that preserves explicit intent, observable acceptance, consistent terms, and honest evidence reporting.

This integration does not change the five contract schemas, their version, or C01-C10. It does not make a writing score an authorization, correctness, or release gate.

## Separate responsibilities

| Component | Responsibility | Limit |
| --- | --- | --- |
| MOE | Accountability, authority, delegation, verification, delivery | Does not prescribe a prose style for every organization |
| ECS | Clear intent, conditions, decisions, and evidence explanations | Does not authorize work or establish application correctness |
| Contract schemas | Required structure and selected relationships | Cannot determine whether prose is truthful |
| Host controls and verification | Enforce permissions and produce execution evidence | A passing check establishes only its stated scope |

## Versioned upstream package

The canonical imported skill is `.agents/skills/engineering-clarity/`. The source is ECS 1.0.0 at commit `871dbf7030cf18be6312fb0fca00b86d440f7a98` in `MorenoJesus/engineering-clarity-standard`.

The imported skill, references, assets, examples, and heuristic checker remain byte-identical to that commit. The lock manifest records each upstream path, Git blob ID, and SHA-256 digest. The upstream MIT license is retained beside the skill and checker. MOE's own licensing decision remains separate.

The `.claude/skills/engineering-clarity/` directory is a managed copy, not a separately edited standard. MOE-specific guidance stays in this document, the communication profile, and MOE examples. Use `docs/glossary.md` for MOE terms; do not fill in the upstream glossary template in place.

Normal validation and slide generation do not download upstream content. A pin update requires a reviewed change, source comparison, new digests, tests, and regenerated adapters. Hash checks detect local drift against the reviewed manifest. They do not authenticate an upstream author or protect against someone changing both the files and manifest.

## Apply ECS to the five contracts

| MOE contract | Application | Relevant ECS rules |
| --- | --- | --- |
| Mission | Name the beneficiary, outcome, scope, observable conditions, and unknown decisions | ECS-02, 04, 05, 10, 11, 12 |
| Delegation | State the bounded objective, exact inputs, outputs, constraints, failure paths, and stop conditions | ECS-03, 04, 07, 09, 11 |
| Autonomy | Name the actor, action, resource, environment, limits, and approval conditions | ECS-02, 04, 06, 07, 10 |
| Proof Bundle | Explain the candidate, actual results, missing evidence, and limitations without altering raw artifacts | ECS-07, 08, 11, 12 |
| Decision Record | Separate the decision from its context, authority, rationale, uncertainty, and effective scope | ECS-02, 06, 08, 11, 12 |

These mappings are MOE additions. They are not claims that upstream ECS already includes templates for all five contracts. See the [worked rewrites](../examples/ecs/before-after.md).

## Preserve semantics before improving wording

Apply the selected communication standard to human-authored text fields. Preserve schema keys, identifiers, API contracts, units, enum values, source quotes, logs, and tool results. Do not rewrite raw evidence to make a summary read better.

An approved requirement takes precedence over a proposed rewrite. MOE's core and local policy retain their authority. When wording changes technical meaning, expose the conflict for review. Do not invent a threshold merely to make a vague request measurable.

Use `passed` only for a supported result. Use `not_run` when non-execution is known. Use `unknown` when execution or results cannot be established. Use `not_applicable` only with the required rationale and policy decision. An upstream template offering `Not run` is not permission to infer non-execution from absent logs.

ECS is ASD-STE100-inspired; it is not formal ASD-STE100 compliance or certification. A clarity review does not establish MOE conformance.

## Share the skill across roles

Requirements analysts use ECS when framing missions. Planners use it for delegation. Implementers use it for change reports and limitations. Reviewers use it for findings and evidence summaries. Documentation authors use it for verified behavior and operations.

A dedicated writing agent is optional. It must not become the only role responsible for clarity. Each subagent needs the relevant skill and glossary in its own context; parent-agent loading is not assumed to propagate.

For a hosted orchestrator, explicitly load the pinned guidance into the relevant task context and record its revision. For an IDE, use its supported discovery and instruction mechanisms, then verify activation. Do not assume that a file's presence proves use.

## Repository entry points

| Entry point | Guidance | Status |
| --- | --- | --- |
| `AGENTS.md` | Repository rules, ECS loading, MOE glossary and boundaries | Packaged; runtime activation not tested |
| `.github/copilot-instructions.md` | Explicit pointer to canonical ECS and integration guidance | Packaged; runtime activation not tested |
| `CLAUDE.md` | Repository rules and the managed Claude skill | Packaged; runtime activation not tested |
| `.agents/skills/engineering-clarity/` | Canonical imported skill | Byte integrity checked by script |
| `.claude/skills/engineering-clarity/` | Managed discovery copy | Equality checked by script |

Current vendor documentation describes skill locations and conditional activation. The linked documentation is not an execution test of these adapters. Duplicate discovery, enterprise policy, or client version can affect activation; use the [runtime evaluation procedure](../evaluation/ecs/README.md).

## Local commands

Run these from the repository root. Use the same Python environment for dependency installation and execution.

```powershell
.\.venv\Scripts\python.exe scripts/check_ecs.py
.\.venv\Scripts\python.exe scripts/check_clarity.py implementation/ecs-integration.md
.\.venv\Scripts\python.exe scripts/validate.py
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

`check_ecs.py` checks package and mirror integrity without network access. `check_clarity.py` invokes the pinned upstream checker after verifying its imported package. The checker emits heuristic warnings; its default zero exit code is not a human approval. `--strict` makes warnings fail that writing check, not a software-correctness gate.

To regenerate the managed Claude copy after reviewing its changes, run `scripts/check_ecs.py --sync`. This explicitly replaces managed mirror bytes. It refuses altered canonical input, symlinks, and unexpected mirror files. It never updates the upstream pin or edits unrelated instructions.

## Updates and alternatives

To update ECS, select an immutable upstream commit and review its skill, references, templates, checker, and license. Compare every imported file with the upstream blob. Update the manifest and managed copy in one reviewed change. Re-run integrity checks, tests, clarity review, and runtime evaluation where needed.

An adopting organization may replace ECS with an equivalent standard in its own profile. Map its rules to clarity and evidence requirements, update its runtime instructions, and evaluate representative tasks. Do not modify the MOE core to require ECS solely because this repository uses it.

Sources: [upstream ECS pin](https://github.com/MorenoJesus/engineering-clarity-standard/tree/871dbf7030cf18be6312fb0fca00b86d440f7a98), [Agent Skills format](https://agentskills.io/specification), [Copilot skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills), [Visual Studio skills](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-agent-skills?view=visualstudio), [Claude Code skills](https://code.claude.com/docs/en/skills). Documentation reviewed 2026-11-06; no live-runtime test is claimed.
