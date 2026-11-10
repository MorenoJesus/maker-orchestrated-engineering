# Framework overview

**Informative | MOE 0.3.0 working draft**

## Purpose

MOE makes responsibility, authorization, delegation, verification, and learning explicit when people work with intelligent agents. Its central question is not how much code an agent can generate, but how a team can responsibly accept and operate the resulting change.

The maker is an accountability, not a required job title. Makers can implement, debug, test, and review directly. Delegation does not replace technical competence or turn a single person into the owner of every business and risk decision.

## Design goals

Use existing work systems. Express intent in observable terms. Keep authority outside model-generated prose. Make execution bounded and recoverable. Bind verification to the reviewed candidate. Keep changes small enough to understand. Measure outcomes, quality, cost, and attention together.

## Non-goals

MOE does not mandate autonomous coding, multiple agents, test-driven development for every task, a specific sprint length, any model vendor, or automated release. It does not promise faster delivery, prove the absence of defects, establish regulatory compliance, or eliminate engineering skill development.

## Layered model

| Layer | Responsibility | Organization chooses |
| --- | --- | --- |
| Core | Accountability, bounded authority, evidence, traceability, feedback | Local names and representation |
| Lifecycle profile | Map capabilities to the existing development process | Scrum, Kanban, continuous delivery, formal change control, or custom |
| Governance profile | Define risk, permissions, approvals, retention, exceptions | Applicable internal and external obligations |
| Execution profile | Select agent roles, skills, models, and isolation | Human-led, single-agent, or multi-agent execution |
| Integration adapters | Connect approved work, code, execution, evidence, and knowledge systems | Products, hosting, transport, and implementation language |

A profile may strengthen core requirements. It must not silently weaken them and still claim full core conformance. A local term can map to a core concept without renaming every team artifact.

## Minimal useful implementation

These seven elements are enough to begin:

- one accountable maker
- one approved task with explicit acceptance conditions
- a bounded execution environment
- an enforceable permission policy
- a reviewable change
- reliable verification results
- a recorded acceptance decision

A distributed agent platform is optional.

The five contract types are logical records. For a low-risk documentation change, their contents can fit in one issue and its linked review. For a consequential system change, the same semantics can span versioned records and controlled evidence storage.

## What makes the proposal distinct

MOE combines a mission contract, delegation boundaries, autonomy policy, proof bundle, and decision record into a portable accountability model. These are proposed design choices, not a claim that existing engineering practices lack governance or that MOE invented agentic engineering.

See [background and sources](references/sources.md) for related work. The framework is informed by those sources, not endorsed by their publishers.

## Communication without a mandatory dependency

The MOE project uses ECS to write and review technical prose. ECS is recommended, not required, for adopting organizations. Its role is clear communication; schemas, policy controls, and independent evidence retain their separate responsibilities. See [ECS integration](../implementation/ecs-integration.md).
