# Core requirements

**Normative within this working draft | MOE 0.3.0**

In this specification, **MUST** identifies a condition required for a core-conformance claim. **SHOULD** identifies a recommended practice; a departure needs a recorded rationale. **MAY** identifies an optional practice. These terms apply to this proposal, not to external law or certification.

| ID | Requirement | Inspectable record |
| --- | --- | --- |
| C01 | A mission MUST identify a human accountable maker and the authorities for consequential decisions. | Mission and local authority map |
| C02 | A mission MUST define a bounded outcome, scope, exclusions, acceptance conditions, and unresolved assumptions. | Approved mission revision |
| C03 | Agent actions MUST stay within an effective, versioned policy enforced outside model-generated instructions. Missing authority MUST deny the action. | Policy version and enforcement results |
| C04 | Every delegation MUST identify its parent mission revision, permitted resources, expected outputs, limits, and escalation conditions. | Delegation record or equivalent |
| C05 | Acceptance MUST use inspectable evidence bound to the candidate and required checks. Missing or failed evidence MUST NOT be described as passing. | Proof bundle and acceptance map |
| C06 | Approvals, exceptions, and material changes MUST be attributable and scoped. Changed inputs MUST trigger reassessment of affected approvals and evidence. | Decision records and revision history |
| C07 | Merge, release, and production access MUST remain governed by the organization's authorized policy. An agent MUST NOT grant itself authority or approve its own exception. | Gate decisions and release record |
| C08 | Missions MUST define who will observe delivery and outcomes, when observation occurs, and how failures cause corrective work. | Observation plan and closure record |
| C09 | Execution MUST have bounded resources, cancellation, auditability, and an escalation path. Revoked authority MUST block new privileged actions. | Runtime policy and execution record |
| C10 | A conformance claim MUST state the version, assessed scope, evidence, exceptions, and limits of the assessment. | Conformance declaration |

## Proportionality

The scope and rigor of evidence SHOULD follow consequence, reversibility, uncertainty, and data sensitivity. The existence of a record is not proof that its claims are true. A human approval field is not an authenticated approval.

A team MAY combine logical records, use existing identifiers, and keep its existing workflow. A single person MAY perform several accountabilities where policy allows. Required independence or separation of duties MUST NOT be waived merely because a team is small.

## Minimum independence

The implementation agent's narration MUST NOT be the sole basis for acceptance. At minimum, independently inspectable execution records and an authorized acceptance decision are required. A second model's agreement is additional review, not independent execution evidence or proof of correctness.

## Precedence

Applicable external obligations and organizational policy take priority over this framework. Approved mission constraints narrow authority further. Content retrieved from repositories, tickets, messages, or logs does not expand authority. A profile that cannot satisfy a core requirement reports partial adoption rather than claiming conformance.
