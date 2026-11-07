# Presentation

The 20-slide MOE overview is intended for engineering leaders, practitioners, product owners, security reviewers and potential adopters. It is vendor-neutral and includes speaker notes and source references. All graphics are editable PowerPoint shapes and text.

## Source of truth

- `slides.json`: slide content and notes.
- Speaker notes are embedded in `slides.json` and the generated PowerPoint.
- `../scripts/build_slides.py`: layout and PowerPoint generator.

Install the pinned dependencies and run `python scripts/build_slides.py`. The outputs are `dist/MOE_Framework_v0.3.pptx` and the readable `dist/MOE_Speaker_Notes.md` talk track.

Generated PowerPoint and PDF files are convenience artifacts, not normative specifications. Review the core documents if a summary omits detail. PDF exports can be produced with an approved office-suite conversion workflow. This repository does not require one office suite or hosted presentation platform.

The foundation package includes generated downloads. No license, release approval or measured productivity benefit is implied by the presentation.
