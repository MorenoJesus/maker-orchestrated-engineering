# Changelog

## Unreleased

The license decision, reference tooling corrections and presentation polish; no schema-semantics or core-requirement change. The tooling and presentation changes are proposed and await owner review.

- License: the repository owner selected the Apache License, Version 2.0 on 2026-11-10. Added `LICENSE` and updated the documents and the roadmap slide that described the license as pending.
- Pinned the packages that enable `date-time` and `uri` format checks. Previously both formats were silently unenforced and `test_invalid_timestamp` failed on a clean install. The validator now stops when a format used by the schemas has no checker.
- Removed the script shebang lines. On Windows the `py` launcher followed them to a different interpreter than `py -m pip` installs into, so the documented command could fail.
- The reference validator now rejects accepted, delivered, observing and closed missions without a ready proof bundle and the approving decision for that state; outcome observations recorded before delivery; closed missions with no observation result; `not_applicable` checks citing a decision outside the record set; and rejection-kind decisions that do not record reject.
- Added a continuous-integration workflow that runs the validator, unit tests and slide build. It has not yet run on the hosting service.
- Every negative test now asserts the specific error it expects, so a record rejected for an unrelated reason fails the test.
- Reformatted the schemas, example records and slide source from single-line JSON to indented JSON. The parsed content is unchanged, apart from the slide wording below.
- Presentation: the deck now names Calibri instead of Inter, which rendered through substitution wherever Inter was not installed. The loop slide shows the full cycle, the architecture labels are vertically centred, and the seventh principle uses the manifesto's wording.
- Documented the known gaps between the specification text and the reference schemas, further validator limits, and an optional live demonstration. README commands now use `python`.

## 0.3.0 - 2026-11-06 - working draft

Initial repository foundation derived from the MOE design discussion. Added vendor-neutral core requirements, manifesto, roles, lifecycle capabilities, autonomy boundaries, verification semantics, conformance guidance, contract schemas, examples, templates, profiles, adoption and measurement guidance, implementation design, project governance, and presentation source.

Earlier 0.1 and 0.2 labels refer to conversational design iterations, not published repository releases. This draft is not a certification or a claim of measured organizational benefits. License selection was pending owner approval when this draft was written.
