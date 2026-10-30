# Execution, batches and output contract

[中文](../execution-and-delivery.md) | **English**

## Combining scripts and the GUI

**Tutorial mapping:** [T07](tutorial-map.md) A / Create a Multi-step Script and B / Single-Step Refinement; [D01 API](https://gsas-ii.readthedocs.io/en/latest/GSASIIscriptable.html).

Prefer GSASIIscriptable for automated execution. Use the GUI for calibration picks, masks, visual checks and presentation. State unavailable capabilities honestly: writing a script is not running it, and checking numbers is not visual acceptance.

1. Locate the installed GSAS-II, matching interpreter and source tree; record versions. Test imports before reading projects. Do not update software without a task-specific reason. Package-style and older module imports may differ; do not hide dependency failures behind broad version-fallback exceptions.
2. Generate task-specific execution scripts with paths passed through arguments/configuration. Use official objects and methods, not direct GPX binary editing. For low-level fields, inspect the installed source and record its version rather than guessing list indices.
3. Verify import, linking, calibration, integration, variable setup, fitting, result retrieval and saving individually. Check API signatures and units before using G2Project, image integration, add_phase, refinement controls or exporters. Do not ignore errors in outdated tutorial code.
4. Retain variables, constraints, before/after values and tutorial references for each stage. Inspect return status and `.lst` after fitting and save checkpoints. Start each new stage from an accepted state.
5. Do not let GUI and scripts write the same GPX simultaneously. Open the final saved copy for GUI review and verify its title/path/content rather than inspecting an older window.

## S10: Independent batches and sequential refinement

**Tutorial mapping:** T09 / Step I representative fitting and subsequent sequential refinement; T07 staged scripting. Grouping, isolation and run-state files are operational conventions.

- **Independent batches:** give each sample its own GPX. Group calibration by wavelength, distance, detector orientation/binning, optics and measurement conditions. Validate representative samples before copying compatible methods/calibration; reassess phases, masks, backgrounds, ranges and quality for each sample.
- **Sequential refinement:** use for genuinely related series. State whether initialization uses the previous frame, independent starting values or a common starting model. Reassess models for phase transitions/new peaks instead of forcing identical phases across the series.
- **Propagation gate:** propagate only accepted parameters. Isolate failed frames; start the next from a trusted group model or the nearest valid frame and record that source. Without a trustworthy start, pause that group while continuing independent groups.
- **Stopping rule:** after two targeted repairs fail to resolve the same cause, mark `failed`/`needs_input` and save evidence. This is a user-adjustable operational retry limit, not a tutorial number or refinement cycle limit. Never suppress warnings, change weights or automatically remove difficult data to finish a batch.
- If using one sequential project with multiple histograms, also save independently reviewable per-sample projects or verified extracted copies. Every delivered 2D-derived project must retain the corresponding IMG, PWDR, Phases and correct links.

## Status and acceptance

Status is not a scientific conclusion. Report numerical state separately from scientific limitations:

| Status | Meaning |
|---|---|
| `needs_input` | Critical inputs/calibration evidence are missing; dependent steps cannot be completed |
| `provisional` | Computation/presentation is possible, but calibration, model, errors or other stated assumptions remain unverified |
| `failed` | Numerical failure or unmet quality requirements; retain the last valid state |
| `accepted` | Checks below pass within declared assumptions/scope; this does not establish unique phase identity or eliminate systematic errors |

Acceptance requires at least:

1. Traceable inputs, units, instrument/geometry and phase links; calibration/mask evidence for 2D integration.
2. Normal termination and convergence evidence, without unexplained dropped parameters, singularity, false minima, nonfinite statistics or persistently excessive shift/σ. Document any quantitative thresholds and their version/rationale; missing fields do not count as passing.
3. Whole-pattern, enlarged and weak-peak views without unaddressed major systematic discrepancies. Model, justifiably exclude or explicitly downgrade unexplained signals rather than concealing them.
4. Plausible cells, occupancies, ADPs, scales, widths and chemistry; interpretable uncertainties/correlations for key parameters. Do not invent standard deviations for fixed values.
5. Successful reopening, accessible sources, exports consistent with GPX arrays and a final `.lst` from the same final refinement.

Report Rwp, Rp, Rexp when available, reduced χ², GOF, observation count and independent variable count from actual software fields. Specify whether GOF means `sqrt(reduced χ²)`. Do not change uncertainties to force a target χ²; distinguish statistical uncertainty from calibration systematics.

## Output files

**Tutorial mapping:** T02 Step 3 project saving; T05 Save Instrument Parameters; T06 Refinement results / `.lst`; T07 project/export examples; D01 Export/data access. The following directory and CSV/JSON schemas are skill conventions.

```text
run/
  input_manifest.json
  run_state.json
  execution/                  # actual scripts, configuration, environment, stdout/stderr
  calibration/                # applicable GPX, image controls, masks, instrument files, evidence
  samples/<sample_id>/
    final.gpx
    final.lst
    observed.fxye
    profile.csv
    phases/                   # final structural CIFs
    figures/                  # whole pattern, local details, 2D calibration/integration overlays
    summary.json
    stages.jsonl
    report_en.md
    checkpoints/
  batch_summary.csv           # for batch runs
```

Do not create a nominally successful final.gpx for failures: use `last_valid.gpx` or `diagnostic.gpx` with status. Failed retries must not overwrite accepted results. The `.lst` must come from the same fit as its GPX; check this when saving/renaming rather than copying an unrelated stage log.

| File | Format, contents and checks |
|---|---|
| `input_manifest.json` | UTF-8 JSON with input roles, paths, SHA-256 and sizes. The agent adds structure/standard/calibration associations; the helper generates the initial inventory |
| `run_state.json` | Status, environment, calibration groups, parameter sources, per-sample stage, last valid checkpoint and next action; use the supplied template, with null for unknowns |
| `final.gpx` | Native reopenable GSAS-II project. Preserve IMG + PWDR + Phases for 2D inputs, official histograms, correct phase links and working image references |
| `final.lst` | Final GSAS-II refinement log, preserving warnings, variables, statistics and uncertainties; retain terminal logs when needed |
| `observed.fxye` | Export the official observed pattern and uncertainties through a version-compatible GSAS-II exporter. Record exporter, axis units and header convention; do not guess FXYE angle scaling. Optional generic xye is acceptable; declare assumed uncertainties |
| `profile.csv` | UTF-8; at least `x, y_obs, y_calc, y_background, y_obs_minus_calc, weight, used_in_fit`. Declare x units in summary; for CW, default to actual 2θ degrees. Differences have no display offset; mark excluded points rather than silently deleting them |
| `phases/*.cif` | Current structures exported by GSAS-II, with available uncertainties and fixed/refined status. Verify the correct result for multiple-histogram/sequential outputs |
| `figures/` | At least a linear whole-pattern plot and key local details, PNG/PDF. Add log/square-root views when useful and label the transform. Include observations, calculation, background, difference and phase reflection markers; declare any difference offset |
| `summary.json` | Status, input hashes, versions, methods, fitted/excluded ranges, wavelength/geometry provenance, instrument file, phase parameters/uncertainties/fixed flags, statistics, warnings, limitations and output paths/hashes |
| `stages.jsonl` | One JSON object per stage: time, stage ID, tutorial URL/section, changed variables/reasons, before/after statistics, warnings, accept/rollback decision and checkpoint; extensible |
| `report_en.md` | Conclusion/status; inputs/calibration; stage reasons/tutorial links; statistics/local residuals; structures/phase contents/identifiability; limitations; file guide and resume entry point |
| `batch_summary.csv` | One row per sample: ID, status, calibration group, official histogram, Rwp, reduced χ², independent variable count, principal warnings and output path; name additional phase fields explicitly |

For 1D-only inputs, state that IMG is absent. If all three categories are required, look for original 2D data; if unavailable, mark that requirement unmet rather than fabricating nodes.

GPX does not guarantee embedded images. Keep originals in a controlled task directory, or copy required images/sidecars and repair references when the user requests a transferable data package. Reopen after relocation. Public skill publication never implies publishing research outputs.

## Resuming in a new conversation

The agent fills the template arrays from actual inputs:

- `calibration_groups[]`: `id`, `input_file_ids`, `instrument_file`, `geometry`, `wavelength`, `valid_for`, `status`. Represent each physical quantity as `{value, unit, source, fixed, uncertainty, limitation}`; unknowns are null. Sources identify a file/field or calibration stage.
- `samples[]`: `id`, `input_file_ids`, `calibration_group_id`, `phase_sources`, `histogram_names`, `status`, `current_stage`, `last_valid_checkpoint`, `last_valid_lst`, `last_valid_sha256`, `next_action`, `warnings`. Paths are relative to the run root or explicitly absolute.
- `decisions[]`: `stage`, `sample_id`, `action`, `reason`, `tutorial_id`, `tutorial_section`, `tutorial_url`, `evidence`, `time_utc`. An operational decision may have null tutorial_id but must identify itself as a skill convention.
- `associations[]` in the manifest: `sample_id`, `image_file_id`, `metadata_file_id`, `structure_file_ids`, `calibration_group_id`. Fill after inspecting inputs; the helper does not pair files by name.

Read `SKILL.md / SKILL.en.md → run_state.json → input_manifest.json → report_en.md or report_zh.md → last valid GPX/LST`. Verify input hashes, versions, paths and goals, then load the next stage reference. Project names, chat memory and screenshots alone do not establish state. Reconstruct missing records from GPX/LST and identify unrecoverable history.

Schemas and filenames are shared between languages except the report suffix. Switching language must not reset scientific state. Use the English run-state template for new English runs, or retain an existing record and change only the communication/report language.

## Publication privacy

The skill directory contains only methods, official links, generic code and empty templates. Keep research data, CIFs, images, GPX files, logs, hashes, paths, sample names, figures and fitted values in task directories. Publish from an explicit allowlist and inspect archives; `.gitignore` is supplementary, not a substitute for review.
