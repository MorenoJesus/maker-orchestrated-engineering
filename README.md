# Maker-Orchestrated Engineering (MOE)

**Human Vision. Intelligent Execution. Verified Outcomes.**

**Version:** 0.3.0 | **Status:** public working draft | **Date:** 2026-11-06 | **License:** Apache-2.0

Maker-Orchestrated Engineering is a vendor-neutral, lifecycle-adaptable framework for accountable collaboration between people and intelligent agents. Human makers direct the work. Agents execute bounded tasks. Independently inspectable evidence supports acceptance. Organizational policy controls authority.

MOE is an engineering operating model, not a coding agent, product, replacement for every existing lifecycle, or certification. It does not require a particular employer, model, programming language, cloud, IDE, integration protocol, scanner, or work-tracking system. It is not yet empirically validated as a superior delivery method.

## Start here

| Reader | First documents |
| --- | --- |
| Everyone | [Manifesto](MANIFESTO.md), [framework overview](docs/overview.md) |
| Engineering leaders | [Adoption and pilot](adoption/pilot.md), [measurement](adoption/measurement.md) |
| Makers and reviewers | [Lifecycle](specification/lifecycle.md), [roles](specification/roles.md), [worked example](examples/README.md) |
| Security and governance | [Autonomy](specification/autonomy.md), [verification](specification/verification.md), [conformance](specification/conformance.md) |
| Implementers | [Contract semantics](contracts/README.md), [reference architecture](implementation/architecture.md), [agent design](implementation/agents-and-skills.md) |
| Presenters | [Deck and speaker notes](presentations/README.md) |

The [document index](docs/index.md) links the complete foundation.

## The operating loop

**Define -> Contract -> Orchestrate -> Prove -> Deliver -> Learn -> Define.**

These are capabilities, not six mandatory meetings or a waterfall. A mission is a bounded outcome represented in your existing work system. Five logical records make the work inspectable: a **Mission Contract**, **Delegation Contract**, **Autonomy Policy**, **Proof Bundle**, and **Decision Record**. They can share a ticket or document; five records do not mean five new tools.

A mission can be technically accepted and delivered while its intended business outcome is still unverified. MOE records that distinction instead of calling every successful build a business success.

## Adopt without replacing your lifecycle

Choose a [lifecycle profile](profiles/README.md). Map local roles, authority, evidence, and delivery controls. Start with one low-risk repository and a reviewable change. Keep your existing quality standards. Add autonomy only when observed performance and controls justify it.

## Validate the reference records

Requires Python 3.10 or later and the packages in `requirements.txt`.

```sh
python -m pip install -r requirements.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

On Windows, `py` can replace `python`. Where only `python3` is on the path, use that.

The validator checks schema structure, cross-record links, and selected policy invariants. It does not authenticate approvers, execute security controls, certify conformance, or prove a software change correct. All example records are synthetic fixtures, not production evidence.

A [repository workflow](.github/workflows/validate.yml) is configured to run the same commands, the ECS integrity check and the slide build on pull requests. A passing run shows that the repository is internally consistent, nothing more.

## Build the presentation

```sh
python scripts/build_slides.py
```

This creates `dist/MOE_Framework_v0.3.pptx` and `dist/MOE_Speaker_Notes.md` from editable source. The source, slide content, and notes are in this repository. Generated release files are not the normative specification.

## Status and decisions still open

MOE is licensed under the [Apache License, Version 2.0](LICENSE); see [license status](LICENSE-STATUS.md) for its scope. Governance approval, a private security-reporting route, the pilot design and a tagged release are still open owner decisions. Thresholds, adoption targets, and maturity labels in this draft are proposals, not external standards. No industry endorsement or certification is claimed. Places where the specification text and the reference schemas do not yet agree are listed under [known gaps](contracts/README.md#known-gaps). See [roadmap](ROADMAP.md) and [RFC process](rfcs/README.md).

## Engineering Clarity Standard

MOE governs accountable work. ECS helps people and agents communicate that work precisely. Independent evidence establishes what happened.

This repository uses a pinned ECS 1.0.0 skill for technical prose that contributors create or revise. ECS is recommended but optional for other organizations; it is not a core-conformance dependency. The [integration guide](implementation/ecs-integration.md) explains the boundary and the [communication profile](profiles/communication-ecs.md) maps ECS to the five contracts.

```sh
python scripts/check_ecs.py
python scripts/check_clarity.py implementation/ecs-integration.md
```

These checks inspect package integrity and possible writing issues. They do not test model activation or prove application correctness. Use the [runtime evaluation cases](evaluation/ecs/README.md) to assess actual agent behavior. Imported ECS files retain their upstream MIT license, separate from the Apache License that covers original MOE material; see [notices](THIRD-PARTY-NOTICES.md).
