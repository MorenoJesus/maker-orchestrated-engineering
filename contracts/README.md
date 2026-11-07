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

## Evidence status

passed and failed require a producer, run identifier, timestamp, artifact URI and digest. not_run means execution is known not to have occurred. unknown means status is not established. not_applicable requires a reason and a decision reference. No state means universally safe. An artifact digest establishes byte identity, not producer authenticity.

## Validator limits

The reference validator checks structure and selected cross-record invariants for one mission, policy, delegation, proof bundle and decision. It is not a multi-mission scheduler, policy engine, cryptographic verifier, production release gate, or conformance certifier. It does not authenticate identities, fetch artifacts, inspect source ACLs, detect all policy conflicts, evaluate current policy expiry or perform application tests. Operational integrations must do those things as appropriate.

Fixture records are explicitly synthetic and must never be promoted into operational acceptance. A fixture can pass schema and consistency checks while its required application checks remain not_run.
