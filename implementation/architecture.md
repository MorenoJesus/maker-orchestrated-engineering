# Reference architecture

**Informative implementation design | MOE 0.3.0**

MOE does not require a centralized platform. The design below is an optional implementation pattern for organizations that want reliable agent execution across existing systems.

```text
Existing work system / human interface
                 |
        Mission + authority service
                 |
   Deterministic workflow and policy boundary
          /             |              \
   Context service  Task scheduler   Decision service
                         |
                Isolated executors
                         |
              Approved tool adapters
                         |
      Source / builds / tests / delivery systems
                         |
       Evidence store + acceptance evaluator
                         |
             Observation and learning
```

## Control plane and execution plane

The control plane owns authorization, state transitions, scheduling, budgets, cancellation, and evidence references. Model outputs are proposals, plans, patches, and summaries. The executor owns a bounded workspace and scoped tool access. It cannot redefine its own authorization.

Use a durable workflow when work must survive process restarts. Store transitions with optimistic concurrency and an idempotency key. Reconcile uncertain writes before retries. Tie task leases to policy expiry and revocation. Record partial completion and cancellation rather than silently restarting everything.

A task record should identify the authorized mission revision, parent delegation, dependency set, workspace, input revision, permitted outputs, deadlines, resources, and evidence obligations. Parallelize only separable work. Changes to shared contracts, schema, or dependencies need explicit ownership and integration checkpoints.

## Adapter boundaries

| Adapter | Required behavior |
| --- | --- |
| Work system | Read and update scoped work items with revision checks |
| Context retrieval | Enforce source access, classify data, retain source and freshness metadata |
| Model gateway | Use approved endpoints; minimize context; apply budgets and audit policy |
| Workspace | Pin inputs; isolate writes; validate paths and outputs |
| Execution | Run approved tasks in an isolated environment; capture actual results |
| Evidence | Store immutable references with integrity and provenance controls |
| Review and delivery | Bind decisions to candidates; honor local branch and release policy |
| Knowledge | Distinguish draft from approved material; review promotion into shared memory |

No integration protocol is required. Approved APIs, native function calls, command wrappers, or other transports can implement these boundaries. A different transport does not remove authorization or execution risk.

## Implementation sequencing

Start with an existing work item, one bounded executor, and evidence collection. Add multiple workers only after dependency handling, review limits, and cancellation work. Add additional model providers behind an adapter only when there is a concrete need. Do not build a distributed orchestration platform merely to adopt the framework.

## Operational requirements

Record correlation IDs, decision IDs, policy revisions, task attempts, model/tool versions where relevant, and evidence references. Avoid logging secrets or unrestricted prompts. Test recovery, budget exhaustion, revoked authorization, stale candidates, duplicate callbacks, unavailable tools, and blocked delivery.

This repository supplies framework documents and reference validation, not a production orchestration service.
