# Contributing

This is a working-draft framework, licensed under the [Apache License, Version 2.0](LICENSE). Under section 5 of that license, a contribution submitted for inclusion is provided under the same terms unless you state otherwise. The owner has not adopted a separate contributor agreement or sign-off requirement. Contribute only material you have the right to submit.

## A useful contribution

Describe the problem, affected requirement or document, proposed change, alternatives, and an example. Distinguish personal opinion, measured findings, hypotheses, and external sources. Do not include employer or client code, internal policies, credentials, or confidential incidents without authorization.

Core semantics and schema changes should use [an RFC](rfcs/README.md). Keep the framework vendor-neutral. Put product-specific guidance in clearly optional adapters, with dated verification and sources.

## Validation

Run `python scripts/validate.py` and `python -m unittest discover -s tests -v`. Review links and examples. Rebuild the presentation after changing slide content. The repository workflow in `.github/workflows/validate.yml` runs the same three commands on pull requests. Do not represent a successful reference validation as full organizational conformance.

For a schema change, include accepted and rejected cases and explain migration. For a security-related change, state the threat, control, and limits. For a claimed benefit, provide method, baseline, sample, and uncertainty.

## Respectful review

Critique the proposal, not the person. Welcome different organizational constraints. Do not dismiss small teams or regulated teams for needing different implementation choices. Report uncertainty directly.
