# Maker-Orchestrated Engineering (MOE)

**Human Vision. Intelligent Execution. Verified Outcomes.**

**Version:** 0.3.0 | **Status:** public working draft | **Date:** 2026-11-06

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

```powershell
py -m pip install -r requirements.txt
py scripts/validate.py
py -m unittest discover -s tests -v
```

The validator checks schema structure, cross-record links, and selected policy invariants. It does not authenticate approvers, execute security controls, certify conformance, or prove a software change correct. All example records are synthetic fixtures, not production evidence.

## Build the presentation

```powershell
py scripts/build_slides.py
```

This creates `dist/MOE_Framework_v0.3.pptx` from editable source. The source, slide content, and notes are in this repository. Generated release files are not the normative specification.

## Status and decisions still open

The repository owner must approve a reuse license before this project claims to be open source; see [license status](LICENSE-STATUS.md). Thresholds, adoption targets, and maturity labels in this draft are proposals, not external standards. No industry endorsement or certification is claimed. See [roadmap](ROADMAP.md) and [RFC process](rfcs/README.md).
