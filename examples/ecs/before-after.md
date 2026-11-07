# ECS across MOE's five contracts

**Illustrative rewrites only. No application implementation, approval, test run, or deployment is asserted.**

This example concerns page-size validation in a synthetic catalog API. The bounds of 1 through 100 and the error code below belong to the example. They are not universal requirements.

## 1. Mission Contract

**Before:**
> Improve pagination so that it works well for everyone.

**Proposed rewrite:**
> Enable catalog clients to request bounded result pages. Given an integer `page_size` from 1 through 100, the API preserves that value. Given an out-of-range or non-integer value, it returns HTTP `400` with `INVALID_PAGE_SIZE`. Authentication changes are out of scope.

**Still unresolved:** What behavior applies when `page_size` is absent? Do existing clients rely on a different error contract? The outcome owner must resolve these questions before authorizing affected behavior.

**ECS contribution:** explicit behavior and visible unknowns. **MOE contribution:** accountable ownership, revision-bound authorization, and acceptance requirements.

## 2. Delegation Contract

**Before:**
> Fix the endpoint, add tests, and update anything else you need.

**Proposed rewrite:**
> Prepare a candidate for AC-01 and AC-02 in the assigned sandbox. Modify only the assigned catalog component, its tests, and related documentation. Preserve authentication behavior. Stop and escalate if the approved error contract conflicts with an existing client contract. Return the diff and actual execution references, or state that execution is unknown or was not run.

**ECS contribution:** bounded instructions and failure behavior. **MOE contribution:** the actual resource policy, budget, stop rules, and delegation authority.

## 3. Autonomy Policy

**Before:**
> The agent can use the repository and deploy when ready.

**Proposed rewrite:**
> The assigned executor may read the approved repository and modify its isolated sandbox. It may execute only the host-authorized checks. It must not merge, change policy, access production, or publish documentation without the applicable authorization. Host controls enforce the exact resources, commands, limits, and expiry in POLICY-001.

**ECS contribution:** explicit actor, action, and limits. **MOE contribution:** independently enforced authorization. Rewriting this paragraph does not configure those controls.

## 4. Proof Bundle

**Before:**
> Tests look good. The feature is ready.

**Proposed rewrite when no results are available:**
> Execution status for CHECK-01 and CHECK-02 is `unknown`. No authoritative run records were supplied for CANDIDATE-001. Acceptance remains blocked until required evidence is available and evaluated.

**Proposed rewrite when the task was not executed:**
> CHECK-01 and CHECK-02 are `not_run`. The executor stopped before test execution because the required dependency was unavailable. The candidate is not ready for acceptance.

**ECS contribution:** honest language about evidence. **MOE contribution:** candidate binding, required checks, evidence provenance, and acceptance authority.

## 5. Decision Record

**Before:**
> Approved. Looks safe to ship.

**Proposed rewrite:**
> Proposed decision: authorize sandbox implementation of MISSION-001 revision 1 under POLICY-001 revision 1. This proposal does not authorize merge or production release. The assigned human authority must approve it through the organizational decision mechanism. No approval has been recorded in this example.

**ECS contribution:** distinguish a proposal from an actual decision and preserve its scope. **MOE contribution:** attributable authority and a record bound to the authorized subject.

## Review boundary

A clear sentence can still be wrong. Inspect original requirements, actual artifacts, and authority records. Do not change approved thresholds, suppress a failure, or invent a rollback guarantee to improve the prose.
