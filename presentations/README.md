# Presentation

The 22-slide MOE overview is intended for engineering leaders, practitioners, product owners, security reviewers and potential adopters. It is vendor-neutral and includes speaker notes and source references. All graphics are editable PowerPoint shapes and text.

## Source of truth

- `slides.json`: slide content and notes.
- Speaker notes are embedded in `slides.json` and the generated PowerPoint.
- `../scripts/build_slides.py`: layout and PowerPoint generator.

Install the pinned dependencies and run `python scripts/build_slides.py`. The outputs are `dist/MOE_Framework_v0.3.pptx` and the readable `dist/MOE_Speaker_Notes.md` talk track.

The deck uses Calibri, which ships with common office suites or is replaced there by a metric-compatible font. To use another typeface, change `FONT` in the build script and review every slide for wrapping, because the layout uses fixed positions.

Generated PowerPoint and PDF files are convenience artifacts, not normative specifications. Review the core documents if a summary omits detail. PDF exports can be produced with an approved office-suite conversion workflow. This repository does not require one office suite or hosted presentation platform.

Generated files are written to `dist/`, which is not version-controlled. The presentation source is covered by the repository [license](../LICENSE). No release approval or measured productivity benefit is implied by the presentation.

## Optional live demonstration

The reference records can make slide 16 concrete. Everything shown is a synthetic fixture.

1. Run `python scripts/validate.py`. It reports PASSED although both required checks are `not_run`: the records are consistent, and nothing claims the work succeeded.
2. In `examples/basic/proof-bundle.json`, change `"assessment": "incomplete"` to `"ready_for_acceptance"` and run the validator again. It reports FAILED because the required checks have not all passed.
3. Restore the file with `git checkout -- examples/basic/proof-bundle.json`.
4. Optionally repeat with `"status": "authorized"` changed to `"accepted"` in `examples/basic/mission.json`. The validator asks for a ready proof bundle and an approving technical-acceptance decision.

`python -m unittest discover -s tests -v` lists the other rejected cases by name. A rejection shows that the reference validator caught an inconsistent record, not that an operational control exists.

## ECS integration

Slides 9 and 10 explain the MOE/ECS boundary and the five contract mappings. ECS is the repository writing standard and optional for adopters. Speaker notes distinguish package checks from unexecuted runtime evaluations. Rebuild the presentation to refresh the embedded and standalone notes.
