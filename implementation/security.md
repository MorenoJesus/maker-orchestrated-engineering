# Security and threat model

**Proposed implementation controls; apply local policy**

## Assets and boundaries

Protect source code, credentials, customer or organizational data, build and release authority, policy records, evidence, shared knowledge, and reviewer attention. Separate untrusted inputs from instructions, model context from credentials, sandbox execution from control services, and generated claims from authoritative evidence.

| Threat | Example | Proposed control | Negative test |
| --- | --- | --- | --- |
| Instruction injection | A source comment asks the agent to send secrets | Treat retrieved text as data; host-side authorization; restricted egress | Malicious comment cannot cause external send |
| Excessive authority | A test helper has general shell and production credentials | Scoped identities, allowlisted actions, isolated runners | Disallowed command and production access denied |
| Cross-project leakage | Retrieval returns another team's confidential text | Enforce source ACLs at query and retrieval; classify caches | Unauthorized source stays inaccessible |
| Evidence forgery | Agent writes a fake passing report | Trusted producers, immutable storage, provenance verification | Untrusted report cannot satisfy a gate |
| Stale approval | Candidate changes after approval | Bind decisions to revisions and digests; recheck before action | New candidate invalidates affected approval |
| Supply-chain execution | Build scripts execute malicious code | Sandboxing, restricted feeds, no ambient credentials | Repository script cannot escape execution boundary |
| Tool misuse | Unvalidated path escapes the workspace | Canonicalize paths; schema and resource checks | Traversal and unexpected resource blocked |
| Runaway delegation | Recursive tasks exhaust budget | Depth, concurrency, cost, time, and retry limits | Limit produces stop and escalation |
| Memory poisoning | Bad advice becomes trusted shared context | Reviewed knowledge promotion and source provenance | Unreviewed note cannot override policy |
| Human overload | Huge generated diff gets rubber-stamped | Review limits and small work packets | Work pauses when review capacity is exceeded |

## Required local decisions

Choose approved data classes, providers, endpoint regions, retention, source access, audit destinations, exception authority, credential handling, and incident response. Do not assume a vendor approval automatically approves every integration or data flow.

Host-side authorization is mandatory for core conformance. Prompt instructions, tool schemas, and a second model's review are not substitutes. A controlled API can still be dangerous if its operations are too broad. A command allowlist does not make repository code safe to execute.

The related OWASP guidance supports least privilege and bounded agent actions; NIST's SSDF provides broader secure-development context. This table is an original MOE threat-model starting point, not a complete assessment or certification. See [sources](../docs/references/sources.md).
