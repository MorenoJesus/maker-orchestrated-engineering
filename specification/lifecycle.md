# Lifecycle capabilities

**Normative semantics; illustrative process mappings | MOE 0.3.0**

Define, Contract, Orchestrate, Prove, Deliver, and Learn are recurring capabilities. They can overlap and repeat. They do not require replacing an existing lifecycle or adding six ceremonies.

| Capability | Required result | Typical exit question |
| --- | --- | --- |
| Define | A problem, beneficiary, baseline, intended outcome, and known uncertainties | Is this worth doing, and what remains unknown? |
| Contract | Authorized scope, acceptance conditions, risk, authority, limits, and observation plan | Who authorized what, under which revision? |
| Orchestrate | Bounded work packets, dependencies, context, execution limits, and ownership | Can this work proceed within authority and review capacity? |
| Prove | Candidate-bound checks, acceptance mapping, limitations, and review evidence | What do the results actually establish? |
| Deliver | Authorized merge or release, operational readiness, recovery plan, and delivery record | Is this exact candidate authorized for this environment? |
| Learn | Observed outcomes, defects, costs, decisions, and reviewed improvements | Did the change help, and what should change next? |

## Mission state and approval boundaries

A reference state mapping is `draft -> authorized -> executing -> awaiting_acceptance -> accepted -> delivered -> observing -> closed`. `blocked`, `cancelled`, and `superseded` are explicit alternatives. Organizations MAY use other names if these distinctions remain visible.

Authorization records MUST bind a mission revision and applicable policy revision. Delegation MUST use that authorized revision. A scope, risk, acceptance, target, or policy change MUST invalidate the affected authorization until reassessed. Unaffected evidence may be reused only with a documented justification.

Acceptance authorizes only the action named in the decision. A technical acceptance does not automatically authorize production deployment. Delivery does not establish that the business outcome was achieved. Closure MUST record the observation result as achieved, not achieved, unknown, or not applicable with a reason.

## Discovery is legitimate work

A mission MAY authorize investigation without authorizing implementation. Such a mission can produce a design, benchmark, or risk assessment instead of a code change. Its acceptance conditions and proof bundle must fit that outcome. It MUST NOT silently graduate from read-only investigation into privileged execution.

## Execution and recovery

The orchestrator SHOULD use explicit task dependencies, bounded retries, deadlines, and cancellation. Failed or uncertain external writes MUST be reconciled before retrying. Jobs SHOULD use idempotency keys and preserve evidence of partial completion. Cancellation MUST stop new actions and record any actions already in progress.

Agents may propose amendments, follow-up missions, or rollback. The applicable human or policy authority decides whether those proposals can proceed. A rollback that changes data or external systems is itself a governed action.

## Documentation and knowledge

Documentation should be reviewed with the candidate it describes. Publication can occur with release or another authorized checkpoint. Draft documentation MUST NOT be represented as deployed behavior. Shared agent memory and reusable skills require review and provenance before promotion into trusted context.
