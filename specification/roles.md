# Accountabilities and decision rights

**Normative accountability model | MOE 0.3.0**

Roles describe responsibilities, not job titles, team size, or a required reporting structure. Several roles can be held by one person when local policy permits.

| Accountability | Owns | Does not automatically own |
| --- | --- | --- |
| Outcome owner | Problem priority, business intent, acceptance of business behavior | Technical or security exceptions |
| Maker | Technical coherence, delegation, review readiness, evidence interpretation, maintainability | Unlimited access or unilateral release authority |
| Policy owner | Risk rules, permissions, quality policy, exception process | Product priority |
| Reviewer or verifier | Assigned independent checks, review findings, evidence limitations | Approval outside delegated authority |
| Release or operations owner | Environment-specific release, recovery, monitoring ownership | Redefining acceptance criteria after implementation |
| Agent | Bounded investigation, proposals, implementation, tests, documentation | Human accountability, new authority, or self-approved exceptions |
| Orchestration service | Scheduling and enforcing approved transitions | Inventing business authority |

## Required assignment

A mission MUST name one accountable human maker or a resolvable organizational identity that identifies that person. A team name alone is insufficient when nobody can be identified as accountable. The mission MUST identify who can authorize work, accept evidence, approve exceptions, and release the result, directly or through a versioned authority map.

A maker may delegate work but not erase accountability. Human makers retain the option to implement directly, inspect code, reproduce a failure, stop execution, and reject an agent's proposal.

## Decision boundaries

The outcome owner resolves ambiguous business behavior. The maker resolves technical choices within approved bounds. The policy owner authorizes permitted exceptions. The release owner authorizes environment-specific delivery. Agents can recommend decisions; only explicitly authorized automation can execute a preapproved policy decision.

For low-risk work, policy MAY authorize automated merge after independently enforced gates. For high-risk work, policy SHOULD require explicit human review and separation of duties. MOE mandates neither universal manual merging nor unrestricted automated merging.

## Human understanding and learning

The maker SHOULD be able to explain the change, its constraints, failure modes, and recovery path. Review workload must remain sustainable. Teams SHOULD preserve deliberate coding, debugging, and design practice for developing engineers. Prompt-writing ability alone is not evidence of engineering competence.

The maker is not a heroic bottleneck. Escalation and substitution procedures SHOULD specify how accountability transfers when the assigned person is unavailable.
