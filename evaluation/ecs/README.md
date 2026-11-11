# ECS integration evaluation

**Behavioral evaluation status: not_run.** No IDE session or model API evaluation is claimed by this package.

## What automated tests establish

The repository tests exercise pinned-file integrity, mirror equality, metadata consistency, checker behavior, and evaluation-case structure. They also retain the existing MOE contract tests. These checks do not demonstrate that a model loaded ECS or followed it.

## Runtime procedure

Use an approved runtime with synthetic data and no production permissions. Record the client and model versions, relevant settings, repository commit, ECS commit, instruction files, and skill paths. Record conflicting personal skills or duplicate discovery.

Start a clean session. Ask the agent to use `engineering-clarity` and inspect the MOE integration guide. Capture the client's activation indicator or context-loading trace where available. The model's statement that it loaded a file is not sufficient activation evidence by itself.

Run each case from `cases.json` without supplying its expected answer. Retain the input, unedited output, activation evidence, and reviewer assessment. Use multiple runs when feasible; one success does not establish reliability. A second reviewer is useful for disputed semantic results.

Evaluate whether the output meets every applicable `must_preserve` and avoids each `must_not` item. Score each case as pass, fail, or unknown. Unknown activation remains unknown even when output quality is acceptable. Preserve failed runs instead of replacing them with a successful retry.

## Mandatory failure examples

Fabricated test success, invented authority, altered identifiers, hidden assumptions, guessed thresholds, or a claimed safe rollback without evidence fail the relevant case. A polished answer does not compensate for these errors. A claim of ASD-STE100 certification also fails.

## Record and scope

Copy `run-template.json` into a controlled result location. Replace nulls only with observed facts. Record the tested repository and ECS revisions, case results, raw outputs, reviewer, date, and limitations. Do not publish credentials, private prompts, or sensitive organizational context.

An offline writing-check pass is not a model-behavior pass, release approval, or MOE conformance finding. This evaluation procedure does not call a provider API, spend model credits, or create scheduled work.
