# GSAS-II Refinement Skill

[中文](README.md) | **English**

A bilingual skill for GSAS-II powder diffraction workflows: input verification, 2D calibration and integration, Rietveld refinement, diagnostics and batch delivery. Each processing stage points to an official GSAS-II tutorial section. Additional provenance, checkpoint and delivery conventions are identified separately.

This is an AI-assistant skill, not a one-click refinement program with fixed parameters. It requires a working GSAS-II installation, local file access and user-provided data with appropriate structural/calibration information.

## Choose a language

Install one copy of the skill. Request Chinese or English in the conversation:

- Chinese entry: [SKILL.md](SKILL.md).
- English entry: [SKILL.en.md](SKILL.en.md), with complete [English workflow references](references/en/tutorial-map.md).

The main SKILL.md routes English requests to the English entry. Both versions use identical stage IDs, sources, scientific rules and data schemas. Switching language does not reset an existing run. Do not install the language versions as separate same-named skills.

## Usage

Provide the **entire folder** to a skill-capable assistant, beginning with SKILL.md. Do not copy only the entry file and omit references.

In Codex, install the folder in the user skill directory supported by your version, then select it in a new conversation or invoke `$gsas-ii-refinement`. If discovery is unavailable, ask the assistant to read this folder's SKILL.md directly. Installation locations depend on the host version; see the [official skill guide](https://learn.chatgpt.com/docs/build-skills).

Example for a new task:

> Use $gsas-ii-refinement in English. Inspect the data directory I specify, verify inputs, candidate structures and calibration evidence, then perform refinement. Preserve IMG, PWDR and Phases in projects derived from 2D images, and deliver an English report with reviewable files.

Teaching example:

> Use $gsas-ii-refinement in English and teach me one step at a time. I will reply done after each operation. Explain the tutorial source, reason and evaluation criteria for every step.

Batch/resume example:

> Use $gsas-ii-refinement in English. Read run_state.json in the supplied run directory, verify the valid checkpoint, then continue unfinished samples. Isolate failures and explain them.

The skill does not remember experimental data from another conversation. Supply the data location for a new task, or the run directory to resume from manifests and checkpoints.

## Inputs and outputs

Inputs may include 2D images/metadata, measured standards or valid calibration files, 1D patterns, instrument parameters, CIFs, or existing GPX/LST files. Requirements depend on the experiment; see [input specifications](references/en/input-and-calibration.md). Missing evidence is explicitly flagged, never replaced with tutorial example values.

Outputs include native GPX, final LST, observed and calculated profiles, structural CIFs, figures, reports, stage records and batch summaries. Projects from 2D inputs retain IMG, PWDR and Phases with verified external image references. See the [output contract](references/en/execution-and-delivery.md).

## Contents

- [SKILL.en.md](SKILL.en.md): English instructions and boundaries.
- [references/en/tutorial-map.md](references/en/tutorial-map.md): official source mapping.
- [references/en/input-and-calibration.md](references/en/input-and-calibration.md): inputs, geometry, wavelength, masks and integration.
- [references/en/refinement.md](references/en/refinement.md): instrument profiles, structural refinement, diagnostics and rollback.
- [references/en/execution-and-delivery.md](references/en/execution-and-delivery.md): execution, batches, acceptance and output formats.
- [assets/run-state.en.template.json](assets/run-state.en.template.json): empty English run-state template with the same schema as the Chinese version.
- [scripts/input_manifest.py](scripts/input_manifest.py): shared Python-standard-library provenance helper. Add `--language en` for English messages; it is not a refinement script.

## Scope and privacy

Primarily for constant-wavelength X-ray powder data. TOF, neutron, magnetic, complex texture and specialized defect models require appropriate dedicated tutorials. Numerical convergence does not prove unique phase identity or a correct scientific interpretation; accurate refinement cannot be guaranteed for arbitrary inputs.

The public skill contains no experimental data, reference cards, actual research paths or sample-specific parameters. Keep generated research files in separate task directories and out of the skill repository.

This is an independent workflow compilation. GSAS-II and the linked tutorials belong to their respective authors; tutorial datasets and images are not reproduced.
