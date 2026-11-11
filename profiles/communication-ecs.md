# Optional ECS communication profile

**Profile ID:** `moe-ecs-v1` | **Applies to:** MOE 0.3.0 | **ECS:** pinned 1.0.0

This profile complements any lifecycle profile. It is the writing choice for the MOE repository and a recommended option for adopters. It is not a new core-conformance requirement.

## Required behavior when this profile is selected

Use the pinned ECS guidance for newly written or revised technical prose. Name actors and actions. Keep one meaning for each term. State conditions and observable outcomes. Preserve exact identifiers and quoted evidence. Distinguish facts, proposed behavior, assumptions, open decisions, and execution results.

Apply these rules to all five contracts, plans, review findings, documentation, and decision explanations. Raw tool output, code, and schema keys remain unchanged. Use MOE's glossary for MOE concepts and the organization's approved glossary for its domain.

Missing test output means `unknown` unless non-execution is known. Known non-execution means `not_run`. A prose review cannot authorize an action, convert a failed check to a pass, or establish that a release is safe.

## Profile record

An organization should record the selected standard, version and immutable source; profile owner; glossary; applicable artifact types; review process; exceptions; and evaluation results. The reference mission example records its selection in `extensions.communication`. That field is descriptive metadata, not an enforcement mechanism.

## Review checklist

Can the reader identify intent, scope, responsible actors, constraints, outcomes, evidence, and uncertainty? Are failure paths and limits explicit where needed? Are unknowns still visible? Did any edit alter an approved requirement or technical identifier? Does the summary match the underlying evidence?

The heuristic checker supports this review but cannot complete it. Templates and intentionally weak examples need contextual interpretation, not automatic rewriting to remove every warning.

## Substituting another standard

Document how the alternative supports explicit intent, consistent terms, observable acceptance, visible uncertainty, and accurate evidence reporting. Evaluate it with the same example tasks. ECS-specific rules do not become mandatory for that organization. MOE's authority, evidence, and conformance requirements still apply.

See [integration details](../implementation/ecs-integration.md) and [evaluation](../evaluation/ecs/README.md).
