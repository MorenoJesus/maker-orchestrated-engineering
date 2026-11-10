# Reference contracts

**MOE 0.3.0 working draft | JSON Schema Draft 2020-12**

Five logical records are represented by five schemas plus a shared definitions file. They are reference interchange formats, not a required storage architecture. Existing tickets or systems may use other representations if the semantics are preserved.

| Record | What it establishes | What it does not establish |
| --- | --- | --- |
| Mission | Proposed intent, boundaries, owner, acceptance and observation | Authenticated authority or a completed outcome |
| Delegation | Bounded task, inputs, outputs, permissions and stop conditions | Permission broader than the governing policy |
| Autonomy | Versioned action rules, scope, budgets and revocation | A functioning enforcement service |
| Proof bundle | Candidate, check results, references and limitations | Correctness merely because the JSON validates |
| Decision record | Attributable claimed decision, scope and rationale | Verified identity or authority by itself |

## Structural conventions

Each record has schema_version, id, revision and record_mode. References bind an ID and revision. The common schema defines reusable fields. Unknown top-level properties are rejected; organization-specific data goes under extensions. The example.invalid schema identifiers are offline identifiers, not live endpoints. The validator resolves them from local files only.

## Semantics

A mission's maker must be human. An authorized mission must reference an approving decision by the assigned authority for the same revision and policy. Delegation actions and resources cannot exceed policy scope; required-action approvals still need runtime verification. Budgets cannot exceed policy limits. Check IDs and acceptance IDs must be unique and mapped.

A ready_for_acceptance label requires all required reference checks to pass; this reference validator deliberately does not implement exception adjudication or accepted not_applicable checks. Organizations that need exceptions must implement authenticated, policy-aware evaluation. Such records may be schema-valid while the reference readiness evaluator rejects them.

Acceptance and release decisions need a candidate and proof-bundle reference. Exception decisions need the affected control, scope, expiry and compensating measures. Required checks must not be silently removed or reclassified as optional.

A mission in accepted, delivered, observing or closed status requires a proof bundle labelled ready_for_acceptance. Because this reference profile validates one decision, that decision must be the approval that justifies the state: technical acceptance for accepted, release for delivered, observing and closed. An achieved or not_achieved outcome observation cannot precede delivery. A closed mission cannot leave the observation as not_yet_observed. A not_applicable check must cite an approving decision present in the validated record set; a decision the validator cannot see does not count. A rejection-kind decision must record reject.

## Evidence status

passed and failed require a producer, run identifier, timestamp, artifact URI and digest. not_run means execution is known not to have occurred. unknown means status is not established. not_applicable requires a reason and a decision reference. No state means universally safe. An artifact digest establishes byte identity, not producer authenticity.

## Validator limits

The reference validator checks structure and selected cross-record invariants for one mission, policy, delegation, proof bundle and decision. It is not a multi-mission scheduler, policy engine, cryptographic verifier, production release gate, or conformance certifier. It does not authenticate identities, fetch artifacts, inspect source ACLs, detect all policy conflicts, evaluate current policy expiry or perform application tests. Operational integrations must do those things as appropriate.

Actor kinds are taken as declared. Timestamps are checked for format but not compared with each other or with the current time, so an expired policy or exception is not detected. The validator reads one delegation and does not resolve its dependencies list.

Format keywords such as date-time and uri are enforced only when the corresponding checker packages in requirements.txt are installed. The validator stops with an error when a format used by the schemas has no checker, rather than silently skipping it.

Fixture records are explicitly synthetic and must never be promoted into operational acceptance. A fixture can pass schema and consistency checks while its required application checks remain not_run.

## Known gaps

The specification text and the reference schemas do not yet agree everywhere. The differences below are open issues for the [RFC process](../rfcs/README.md), not decisions. Until they are resolved, the specification states the intended semantics and the schemas state what the reference validator can check.

| Topic | Specification | Reference schemas |
| --- | --- | --- |
| Policy subject | [Autonomy](../specification/autonomy.md) requires a policy to state its subject. | The autonomy schema has no subject field. The fixture names the agent only in the delegation. |
| Concurrent work | [Autonomy](../specification/autonomy.md) requires budgets to bound concurrent work. | The shared budget bounds tool calls, retries and runtime only. |
| Closure reason | [Lifecycle](../specification/lifecycle.md) requires a reason when the observation result is not applicable. | outcome_observation has no accompanying reason, and it sits on the proof bundle rather than a closure record. |
| Patch compatibility | [Governance](../GOVERNANCE.md) says patch versions should not break record compatibility. | Each schema accepts schema_version 0.3.0 exactly, so a 0.3.1 record would be rejected. |
| Requirement identifiers | MUST statements appear throughout the specification. | Only C01-C10 have identifiers, so the others cannot be cited individually in a declaration. |
| Template items | The [templates](../templates/mission.md) name an outcome owner, beneficiary, concurrency limit and delegation-depth limit. | The schemas do not model these items. |
