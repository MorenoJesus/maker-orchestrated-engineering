# Continuous-delivery profile

**Illustrative MOE mapping**

Use small missions, isolated workspaces, immutable candidates, and explicit release policies. Separate creation of a releasable artifact from authorization to release it.

A policy may preauthorize low-risk changes after trusted checks, review requirements, and deployment safeguards pass. Approval must be bound to the actual candidate and target context. High-risk changes can retain explicit human approval without forcing every low-risk change through the same process.

Use progressive exposure, health indicators, and a rehearsed recovery path where applicable. A rollback involving irreversible data or external effects requires its own safe procedure; not every deployment can be undone by reverting code.

Operational evidence belongs in the mission record. Keep business-outcome claims provisional until observed. A release that meets technical gates but harms users must trigger correction and learning.

**Local decisions:** eligible low-risk actions, gate provenance, exposure limits, release authority, observability windows, rollback authority, and incident escalation.
