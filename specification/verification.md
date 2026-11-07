# Evidence and acceptance

**Normative evidence model | MOE 0.3.0**

A Proof Bundle is a reviewable set of evidence references and acceptance mappings. Its name does not imply mathematical proof, freedom from defects, regulatory compliance, or proven business value.

## Evidence requirements

A bundle MUST identify the mission and policy revisions, exact candidate, target context, checks, producers, execution times, result artifacts, and acceptance mapping. A candidate identifier must be immutable for the relevant artifact type. Examples include a source revision plus tested merge context, an immutable build digest, or a document content digest.

The bundle MUST retain `passed`, `failed`, `not_run`, `unknown`, and `not_applicable` as distinct check outcomes. A missing artifact or an unfinished run is not success. `not_applicable` requires a rationale and authorization where policy requires it. An exception can permit acceptance under policy but MUST NOT rewrite the underlying result.

Reviewers MUST be able to trace each required acceptance condition to evidence and any residual uncertainty. Model summaries MAY explain results but MUST NOT replace authoritative artifacts. Evidence needs appropriate access, integrity, retention, and provenance controls. A content hash detects a byte change; by itself it does not establish who produced the bytes or whether a claim is true.

## Candidate binding and staleness

Record source revision, target or merge context, dependencies or lockfile digest, test selection, tool configuration, environment identity, and applicable policy revision as relevant. A change to any material input MUST trigger reassessment or rerunning the affected checks. Verification against a feature branch alone may not cover the result after merge.

Evidence can be reused only when the verifier records why the unchanged inputs and scope remain applicable. The acceptance decision MUST refer to the exact bundle revision evaluated.

## Independence and test quality

Use independently inspectable execution results and an authorized acceptance decision. Independent reviewers or isolated verification services SHOULD be used according to risk. Two agents can share the same mistaken assumption; a different model name is not sufficient independence.

Agent-generated tests SHOULD be checked against approved requirements, meaningful assertions, negative cases, and known failure behavior. Removing tests or weakening checks to obtain a pass MUST be visible and separately authorized. TDD is an optional practice; when claimed, retain a meaningful failing-test result before implementation, not just a test file timestamp.

Security scanning, mutation analysis, performance checks, accessibility, and integration testing are selected by policy and applicability. No particular product or universal score is required. Surviving mutations require interpretation; a 100% score is not proof of correctness. An absence of scanner findings is not proof of security.

## Acceptance is a decision

The acceptance authority evaluates evidence, unresolved issues, applicable exceptions, and policy. Policy violations cannot be cured by a persuasive summary. Acceptance for delivery and observation of business value are separate decisions. Failures discovered after release reopen corrective work without rewriting historical evidence.
