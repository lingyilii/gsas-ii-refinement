---
name: gsas-ii-refinement
description: Process powder diffraction data in GSAS-II, including 2D calibration and integration, structure import, staged Rietveld refinement, validation and traceable delivery. Supports guided teaching, execution, resuming projects and batch processing, with official tutorial references for each stage. Primarily for constant-wavelength X-ray data; other experiments require an appropriate dedicated tutorial.
---

# GSAS-II Refinement Skill

[中文](SKILL.md) | **English**

Use the user's specified data and structural models to produce evidence-based, reviewable refinements. Communicate in English when this version is selected. This skill contains methods and decision criteria, not experimental data, reference cards or previous refinement parameters. It does not guarantee a unique structure solution for every dataset.

## Starting a new conversation

1. Identify whether the user wants **teaching, execution, resuming or batch processing**. In teaching mode, give one small step at a time: location, purpose, tutorial source and evaluation criteria. Wait for `done` or a screenshot; do not operate the interface for the user. In execution mode, complete the authorized work without repeatedly requesting permission for each step.
2. Inspect the specified directory and existing run records to establish input identity. Do not select an old project elsewhere merely because its filename is similar. Ask for the data location only if it is missing; do not request information already accessible in attachments or files.
3. Read the [tutorial map](references/en/tutorial-map.md) and [inputs and calibration](references/en/input-and-calibration.md). List actual inputs, experiment type, available calibration evidence, missing information and the proposed output location. Record unknown scientific parameters as unknown; never fill them with tutorial example values.
4. Start new tasks from original inputs. Before resuming, verify provenance and the last accepted checkpoint. Store hashes, versions, paths and parameter sources in the task directory, not in this skill.
5. Use the installed GSAS-II and its matching Python environment. Check the version and available API before execution; old tutorial menu labels may differ. If another window is requested, open a separate project copy without overwriting the active project.

## Read as needed

| Work | Required reference |
|---|---|
| Input identification, 2D detector, wavelength, integration | [input-and-calibration.md](references/en/input-and-calibration.md), T01–T05 |
| Individual peaks, instrument profiles, structural refinement, diagnostics | [refinement.md](references/en/refinement.md), T05–T09 |
| Scripting, batches, acceptance, exports, resuming | [execution-and-delivery.md](references/en/execution-and-delivery.md), T07, T09, D01 |

Open the relevant official tutorial to verify the intended method. Offline, use the supplied summaries only for work that does not depend on unverified details, and state that the original source has not been rechecked. Do not invent menus, APIs or quotations. An example demonstrates a method, not the suitability of its numbers for the current data. Identify unsupported extensions explicitly rather than calling them tutorial requirements.

## Workflow

Select stages according to the inputs; not every task needs every stage:

`S00 Inputs/provenance → S01 Geometry/wavelength → S02 Masks/integration → S03 Instrument profile → S04 Structures/data links → S05 Background/scales → S06 Peak positions → S07 Peak widths → S08 Structural parameters → S09 Validation → S10 Delivery/batches`

The references specify actions, explanations, tutorial sections and acceptance criteria. Save and review each stage before expanding the variable set.

## Scientific boundaries

- **Wavelength is not a default refinement variable.** Fix a credible wavelength. An unknown wavelength requires suitable standards and geometrical constraints; freely refining wavelength and the absolute cell scale of an unknown sample does not independently validate either.
- **Peak List fitting is not Rietveld refinement.** Individual peak fitting can diagnose profiles or establish instrument parameters using a standard without a structural model. Structural refinement requires correct phase–histogram links.
- **Sample widths are not purely instrumental.** Record the instrument file's provenance and applicable configuration. Without a defensible separation, report effective profiles rather than independently reliable size and strain measurements.
- **Do not freely vary the overall scale and all phase scales without constraints.** Apply suitable constraints or reduce the independent scale variables following T09. Phase scales, weight fractions and atomic occupancies are different quantities.
- **A lower Rwp does not automatically validate a result.** Check dropped parameters, false minima, nonconvergence, unphysical parameters and missing peaks. Downgrade results under the [acceptance rules](references/en/execution-and-delivery.md) and retain the last valid checkpoint.
- **Final GPX projects from 2D inputs must retain IMG, PWDR and Phases.** These are project-tree categories. Original images are often external files whose references must remain accessible. Never fabricate IMG nodes for 1D-only inputs; state that original images are missing from the three-category delivery.
- Never turn a previous task's sample names, CIFs, wavelength, distance, integration limits, phase fractions, constraints or results into skill defaults.

## Communication and delivery

Explain decisions as “evidence → proposed change → reason → tutorial section → evaluation.” Screenshots support only visible conclusions; inspect projects or logs for hidden state. Refine checkboxes show current settings, not the complete history of whether a parameter has ever been refined.

Deliver projects, data, figures, parameters, logs and an English report under the [output contract](references/en/execution-and-delivery.md). Reopen the final GPX before presenting it. Do not label fixed values as refined; use `null` for unavailable uncertainties and explain why.

Validate representative samples and calibration groups before expanding a batch. Isolate failures and do not propagate their parameters to the next sample.

Use `scripts/input_manifest.py --language en` to fingerprint explicitly selected inputs with SHA-256. It does not identify phases, calibrate or refine. Its output may contain private paths and belongs only in the task directory. The execution agent fills [assets/run-state.en.template.json](assets/run-state.en.template.json); the user need not fill it manually.
