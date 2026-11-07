# Lifecycle profiles

**Informative mappings | MOE 0.3.0**

A profile maps MOE to an existing operating model. It does not silently change that operating model's rules. Each organization should version its mapping, assign an owner, identify governing policies, and record where terminology or authority differs.

| Capability | Scrum-oriented | Kanban-oriented | Continuous delivery | Formal change control |
| --- | --- | --- | --- | --- |
| Define | Product discovery and refinement | Demand intake | Small outcome proposal | Business case or change request |
| Contract | Selected backlog item and local approval | Commitment policy | Approved scope and risk policy | Authorized requirements baseline |
| Orchestrate | Sprint plan and bounded tasks | Explicit WIP limits and pull | Small isolated changes | Approved execution plan |
| Prove | Acceptance and Definition of Done evidence | Exit-policy evidence | Candidate-bound automated checks | Traceable verification records |
| Deliver | Existing release decision | Existing delivery policy | Progressive release under policy | Change and release authorization |
| Learn | Review, retrospective, operational feedback | Flow review and outcome feedback | Telemetry and incident learning | Post-implementation review |

These are proposed MOE mappings, not official modifications or endorsements of the named practices. For the Scrum accountabilities and commitments, consult the official Scrum Guide linked in the sources.

## Shared profile fields

Record `profile_id`, version, owner, scope, local lifecycle states, authority mapping, risk rules, artifact mapping, required checks, exception handling, retention, rollout controls, and observation obligations. Profiles may add requirements. Unmet core requirements must be disclosed as partial adoption.

See the [profile template](../templates/organization-profile.md).

## Communication profiles

Communication profiles complement rather than replace lifecycle profiles. The [ECS profile](communication-ecs.md) applies clear writing and evidence-reporting rules across MOE artifacts. It is optional for adopters and does not change their lifecycle or the core-conformance requirements.
