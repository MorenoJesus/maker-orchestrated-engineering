# Risk-based autonomy

**Normative boundaries; illustrative levels | MOE 0.3.0**

Autonomy is a set of authorized actions, not a model personality or a score earned by confidence. An effective policy MUST specify the subject, action, resource, environment, data scope, expiry, budgets, and approval conditions. Missing or conflicting authority MUST fail closed.

## Illustrative execution levels

| Level | Typical scope | Not implied |
| --- | --- | --- |
| A0: advise | Read approved context; propose a plan | Write or execution permissions |
| A1: sandbox | Modify an isolated workspace; run allowlisted checks | External writes or production access |
| A2: propose | Create a branch, draft change request, or documentation draft | Merge or release permission |
| A3: bounded delivery | Perform explicitly preauthorized low-risk delivery actions after enforced gates | General production access or authority to change policy |

These labels are optional. Permission to create a draft document and permission to execute code have different risks; organizations should model permissions by action rather than treating levels as automatic ladders. A high-performing agent does not gain rights automatically.

## Risk assessment

Assess consequence, reversibility, data sensitivity, external exposure, architectural novelty, dependency reach, and uncertainty. Code size alone is not a risk measure. Authentication, authorization, irreversible migrations, financial operations, regulated records, and critical infrastructure typically need heightened local review; the organization defines its actual risk categories.

## Enforcement requirements

Host-side authorization MUST mediate tool calls. Scope SHOULD include repository paths, network destinations, tenants, data classifications, and allowed command arguments. Untrusted content MUST NOT be treated as an instruction to change permissions. Agents MUST NOT edit the effective policy, bypass quality gates, mint approvals, or suppress audit evidence for their own mission.

Credentials SHOULD be short-lived and kept outside model context. Execution environments SHOULD be isolated and deny unneeded outbound access. An approved command such as a build can execute repository-controlled scripts; command allowlisting alone is not sandboxing.

Budgets MUST bound runtime, retries, tool calls or an equivalent resource measure, and concurrent work. Policies MUST support cancellation and revocation. Each privileged action MUST recheck effective authority at execution time, not only at initial planning.

## Exception handling

An exception MUST identify the control, reason, approving authority, affected candidate or scope, expiry, and compensating measures. It does not change a failed test into a passed test. The agent requesting an exception cannot grant it. An exception is permitted only where the controlling policy permits that exception.

## Context safety

Read access MUST be enforced during retrieval, not merely by a prompt. Logs, embeddings, caches, memory, and tool output need classification and retention rules. Content from tickets, email, code comments, or websites is data, not authority. See [security threat model](../implementation/security.md).
