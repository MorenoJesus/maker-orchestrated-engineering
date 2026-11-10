# Roadmap

**Proposed sequence, not a delivery commitment**

## Foundation: 0.3.0 working draft

Core requirements and manifesto; lifecycle and accountability model; five logical contract types; reference schemas and synthetic fixtures; validation and negative tests; four lifecycle profiles; adoption and measurement guidance; reference architecture and threat model; presentation source and speaker notes.

## Next: validate the design

Owner reviews license and governance. Review the core with engineers, security reviewers, product owners, and operators from more than one context. Run a bounded pilot and record failures as well as benefits. Test whether the records are useful without unnecessary paperwork. Refine schema semantics and portability based on findings. Resolve the [known gaps](contracts/README.md#known-gaps) between the specification and the reference schemas through RFCs.

## Then: implementation evidence

Demonstrate an adapter against an approved work system and an isolated execution environment. Exercise stale approvals, revoked authority, evidence forgery, retries, and cancellation. Publish sanitized findings and migration guidance. Do not label this repository a production orchestrator before one exists.

## Conditions for considering 1.0

Stable core semantics, reviewed schemas, meaningful negative tests, documented adoption experience, an approved license and contribution process, explicit limitations, and independent review. A target date or download count is not a substitute for those conditions.
