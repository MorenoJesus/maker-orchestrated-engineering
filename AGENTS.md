# Repository instructions

This repository contains the vendor-neutral MOE working draft. Keep organization-specific names, internal workflows, proprietary code and credentials out of public content. Do not add a mandatory vendor, language, model, scanner or integration protocol to the core.

Preserve the distinction between normative requirements, optional profiles, examples and implementation proposals. Do not claim certification, real-world benefits, authenticated approval, application-test success or production readiness without evidence. Synthetic fixtures must remain explicitly marked.

Keep schemas, examples, validator tests, guides and presentation content consistent. Run the reference validator and unit tests after relevant changes. Preserve failed, not_run and unknown results. Do not relax checks to make examples pass.

Treat proposed governance, licensing and RFC decisions as pending until the repository owner explicitly approves them. Do not merge, publish a release or grant new permissions merely because a document suggests doing so.

## Engineering Clarity Standard

Use ECS for newly written or revised technical prose in this repository. Read `.agents/skills/engineering-clarity/SKILL.md` and its referenced standard before substantive writing or review. Read `implementation/ecs-integration.md` for MOE mappings and `docs/glossary.md` for MOE terminology. Each subagent that writes prose needs the relevant guidance in its own context.

Preserve exact code identifiers, schema keys, enum values, quoted evidence, and raw execution artifacts. Missing results mean `unknown`; use `not_run` only when non-execution is known. Do not invent facts, thresholds, authority, test success, or a safe rollback.

ECS is this repository's writing standard and the recommended reference for adopters. It is not mandatory for MOE core conformance. Host policy and independently inspectable evidence retain their roles. A writing check does not grant approval.

Do not edit the pinned upstream package or managed mirrors independently. Run `python scripts/check_ecs.py` and the unit tests after integration changes. Use the clarity checker as a review aid, not as a correctness certificate. Runtime activation and model-behavior evaluations must remain `not_run` until actually executed.
