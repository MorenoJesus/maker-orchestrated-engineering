# Agents, skills, instructions, and tools

**Optional implementation pattern | MOE 0.3.0**

An **agent profile** defines a role and expected behavior. A **skill** describes a repeatable method. **Repository instructions** explain local context and conventions. A **tool adapter** performs an operation. **Host policy** decides whether the operation is allowed. None of the first three replaces the fifth.

## Suggested roles

| Role | Bounded responsibility | Typical output |
| --- | --- | --- |
| Requirements analyst | Clarify approved source material; expose unknowns | Proposed mission and acceptance conditions |
| Planner | Analyze dependencies and propose a task graph | Proposed delegation records |
| Implementer | Make scoped changes in an isolated workspace | Candidate patch and implementation notes |
| Test specialist | Derive tests from approved behavior; inspect failure cases | Tests and execution references |
| Risk reviewer | Review security, privacy, and operational implications | Findings and unresolved risks |
| Evidence auditor | Check provenance, candidate binding, and acceptance mapping | Evidence gaps and review summary |
| Documentation author | Describe verified behavior and operational requirements | Reviewed documentation draft |

One agent can perform several roles when risk permits. Several agents do not automatically provide independence. The planner is not an approval authority merely because it coordinates work.

## Suggested skills

Mission framing; impact analysis; bounded planning; test-first development where appropriate; evidence assembly; security finding triage; change review; operational documentation; and outcome observation. Organizations may use any writing standard that preserves precise intent, explicit uncertainty, and verifiability.

The repository includes a neutral [agent profile template](../templates/agent-profile.md) and [skill template](../templates/skill.md). It does not claim that arbitrary Markdown files will be automatically loaded by every IDE or agent runtime. Implementers must create and test runtime-specific adapters.

## Runtime requirements

Load approved instructions and skills from versioned, integrity-checked sources. Log their revisions when material. Separate trusted instructions from retrieved content. Mediate every tool invocation, validate structured outputs, reject unauthorized changes, and stop at budgets or escalation conditions.

Independent services must produce authoritative execution evidence. Agent-written summaries must preserve `failed`, `not_run`, and `unknown`. Updates to instructions, skills, policy, or model configuration need an appropriate review process.
