# Adoption guide and pilot charter

**Proposed approach | MOE 0.3.0**

## Start small

Select one team, one low-risk product area, one accountable sponsor, and a maker with sufficient technical context. Prefer reversible changes and approved synthetic or non-sensitive data. Keep existing security, testing, and release requirements. Do not begin with critical access-control changes or irreversible production migrations.

## Suggested sequence

| Phase | Work | Exit condition |
| --- | --- | --- |
| Baseline | Observe existing delivery, review effort, quality, cost, and defects | Agreed definitions and usable baseline |
| Map | Assign authorities; choose a profile; map the five logical records | Approved boundaries and controls |
| Shadow | Agents propose; humans execute the normal process | Useful proposals without authority violations |
| Bound | Permit sandbox execution and draft changes | Evidence, cancellation, and negative-path controls work |
| Evaluate | Compare matched work and inspect failures | Explicit expand, revise, pause, or stop decision |

The order is suggested; fixed durations and numbers of missions are not requirements. A small sample can reveal problems but may be insufficient to demonstrate an effect.

## Charter fields

State the problem, hypothesis, participating team and scope, excluded work, approved models and data classes, local risk policy, reviewer capacity, budget, baseline period, evaluation window, comparison approach, guardrails, and stop criteria.

**Example hypothesis:** for comparable low-risk changes, MOE reduces time to technically accepted delivery without increasing escaped defects, review effort, unauthorized actions, or total cost beyond agreed limits. This is a hypothesis, not a claimed benefit.

## Stop and escalation conditions

Immediately pause relevant execution on unauthorized data access, unexpected external actions, evidence tampering, missing control enforcement, or inability to revoke access. Investigate before restarting. Pause expansion if review backlog, rework, defect outcomes, or cost exceed predeclared limits.

Do not relax quality thresholds after seeing results just to declare the pilot successful. Record tool changes, team learning, task mix, and other confounders. Keep failed and cancelled missions in the analysis.

## Adoption beyond the pilot

Expand by demonstrated capability, not by a target agent count. Onboard additional teams with a profile and an authority map. Reuse templates and approved skills, but reassess repository context and data boundaries. Update local controls and training before increasing autonomy.

Use [measurement guidance](measurement.md) and the [conformance template](../templates/conformance-declaration.md).
