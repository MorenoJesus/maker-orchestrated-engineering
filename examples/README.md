# Worked example: a bounded catalog change

**Synthetic illustration, not executed application work.**

A product owner requests predictable page-size bounds for a catalog endpoint. The maker frames a small, reversible mission. The policy permits source reading, sandbox patches and checks, but forbids production writes and merging. The planner delegates only the authorized subset.

The five records in basic/ deliberately stop before technical acceptance. The example decision authorizes sandbox work only. Both required application checks are not_run. The candidate digests and actor IDs are synthetic. No API, build, scan, deployment, or business outcome has been demonstrated by these fixtures.

## Walkthrough

1. Read mission.json for scope, acceptance conditions and the observation plan.
2. Read autonomy.json for the maximum authority.
3. Read delegation.json for the narrower work assignment.
4. Read proof-bundle.json for the explicit lack of application evidence.
5. Read decision-record.json for a scoped synthetic authorization, not release approval.

Run the validator to check the records' structure and relationships. Run the unit tests to see rejected mutations of the records: stale references, missing evidence, unknown criteria, unauthorized actions and excessive budgets. Those unit tests validate this reference implementation, not the fictional catalog change.

A real implementation must replace fixtures with authenticated records, enforce policy at runtime, execute applicable checks against the exact candidate, review the results, authorize delivery, and later observe the intended effect.

## Communication profile

This synthetic mission selects the optional ECS profile in `extensions.communication`. The metadata records a writing choice; it does not enforce runtime loading or add a core dependency. See [before-and-after rewrites](ecs/before-after.md) for all five contracts.
