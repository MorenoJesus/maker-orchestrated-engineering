# Conformance and honest claims

**Normative claim rules | MOE 0.3.0 working draft**

This project does not operate a certification program. A schema-valid record, successful script run, or AI review is not a certificate.

## Claim categories

**Exploring MOE** means a team is trying selected concepts without claiming core coverage.

**Partially adopting MOE** means the team maps its process to the core but discloses unmet requirements.

**Self-assessed core conformance** means the team has examined C01-C10 for an explicitly bounded implementation and documented evidence for every applicable requirement. This is a self-assessment, not an independent endorsement.

## Required declaration

A declaration MUST include all of the following:

- framework version
- organization or team scope
- products, environments, and dates assessed
- lifecycle and governance profile versions
- assessor and accountable owner
- C01-C10 evidence references
- exceptions
- known gaps
- reassessment date or trigger

All core requirements are applicable to an implementation claiming core conformance. Individual checks inside a mission may be not applicable with a justified policy decision. A team cannot declare a core requirement not applicable simply to avoid implementing it.

## Evaluation procedure

1. Map the local workflow, roles, permissions, and evidence stores to MOE concepts.
2. Select a representative sample including failed, cancelled, revised, and delivered missions.
3. Inspect authority, actual enforcement, traceability, evidence authenticity controls, and observation.
4. Exercise negative cases: stale approval, revoked access, forged evidence, excessive retries, and missing required checks.
5. Record limitations, remediation owners, and the bounded claim.

The reference validator checks data shape and selected semantic relationships only. It does not inspect production controls, identities, access policies, evidence signatures, or actual business outcomes. It MUST NOT be presented as a full conformance evaluator.

## Proportional records

A low-risk mission may keep all records in one work item. A regulated profile may require separate signed records and controlled retention. Either representation can support the same core requirements. Complexity and document count are not maturity measures.
