# Changelog

## Unreleased - license, reference tooling and presentation polish

The license decision, reference tooling corrections and presentation polish; no schema-semantics or core-requirement change. The tooling and presentation changes are proposed and await owner review.

- License: the repository owner selected the Apache License, Version 2.0 on 2026-11-10. Added `LICENSE` and updated the documents and the roadmap slide that described the license as pending.
- Pinned the packages that enable `date-time` and `uri` format checks. Previously both formats were silently unenforced and `test_invalid_timestamp` failed on a clean install. The validator now stops when a format used by the schemas has no checker.
- Removed the shebang lines from `scripts/validate.py` and `scripts/build_slides.py`. On Windows the `py` launcher followed them to a different interpreter than `py -m pip` installs into, so the documented command could fail.
- The reference validator now rejects five more inconsistent record sets:
  - an accepted, delivered, observing or closed mission without a ready proof bundle and the approving decision for that state;
  - an outcome observation recorded before delivery;
  - a closed mission with no observation result;
  - a `not_applicable` check that cites a decision outside the record set;
  - a rejection-kind decision that does not record reject.
- Added a continuous-integration workflow that runs the validator, the ECS integrity check, unit tests and slide build. Its first run, on pull request 1 at commit `0d9e4e7`, passed on Python 3.10, 3.12 and 3.14 on Ubuntu and Windows: [run 42892428223](https://github.com/MorenoJesus/maker-orchestrated-engineering/actions/runs/42892428223). A passing run shows that the repository is internally consistent. It is not application verification or conformance evidence.
- `tests/test_ecs_integration.py` now reads files as UTF-8. With the Windows default encoding, `test_deck_has_shared_skill_and_optional_adoption` stopped with a decoding error before it could assert anything.
- Every negative test now asserts the specific error it expects, so a record rejected for an unrelated reason fails the test.
- Reformatted the schemas, example records and slide source from single-line JSON to indented JSON. The parsed content is unchanged, apart from the slide wording below.
- Presentation: the deck now names Calibri instead of Inter, which rendered through substitution wherever Inter was not installed. The loop slide shows the full cycle, the architecture labels are vertically centred, and the seventh principle uses the manifesto's wording.
- Documented the known gaps between the specification text and the reference schemas, further validator limits, and an optional live demonstration. README commands now use `python`.

## Unreleased - ECS integration into the 0.3.0 working draft

Adopt ECS for MOE repository prose while keeping it optional for adopters. Pin upstream ECS 1.0.0, preserve its MIT license, and add explicit agent entry points. Add five contract rewrites, an optional communication profile, integrity and mirror checks, and ten runtime evaluation cases. Extend the presentation with two ECS slides and updated speaker notes. Contract schemas and the framework version remain unchanged. Live runtime activation and model-behavior evaluations are not yet run.

## 0.3.0 - 2026-11-06 - working draft

Initial repository foundation derived from the MOE design discussion. Added vendor-neutral core requirements, manifesto, roles, lifecycle capabilities, autonomy boundaries, verification semantics, conformance guidance, contract schemas, examples, templates, profiles, adoption and measurement guidance, implementation design, project governance, and presentation source.

Earlier 0.1 and 0.2 labels refer to conversational design iterations, not published repository releases. This draft is not a certification or a claim of measured organizational benefits. License selection was pending owner approval when this draft was written.
