# Official tutorials and workflow mapping

[中文](../tutorial-map.md) | **English**

Sources checked on 2026-10-30. These are official GSAS-II tutorials or API documentation. This skill is an independent compilation, not an official publication. Example materials and numerical settings are not defaults for user data.

**Citation format:** record the stage ID, tutorial ID, section title, URL and reason for the current choice. Search by section title if a page changes; do not rely on screenshot coordinates or fixed line numbers. Identify additional operational or quality rules as skill conventions, not tutorial quotations.

| ID | Official source | Relevant sections and limits |
|---|---|---|
| T00 | [Tutorial index](https://advancedphotonsource.github.io/GSAS-II-tutorials/tutorials.html) | Find dedicated methods for the experiment. CW, TOF, neutron and texture workflows are not interchangeable. |
| T01 | [Area detector calibration](https://advancedphotonsource.github.io/GSAS-II-tutorials/2DCalibration/Calibration%20of%20an%20area%20detector%20in%20GSAS.htm) | S00–S01: Step 1 image import, Step 2 image parameters, Step 3 calibration. Distinguish known experimental quantities from geometry to be calibrated. |
| T02 | [Area detector integration](https://advancedphotonsource.github.io/GSAS-II-tutorials/2DIntegration/Integration%20of%20area%20detector%20data%20in%20GSAS.htm) | S02: Prerequisite; Step 2 Integration Settings; Step 3 Perform integration. Limit overlays, angular/azimuthal bins, image corrections and PWDR generation. |
| T03 | [Multiple distances, part 2: Calibrate Detector Distances](https://advancedphotonsource.github.io/GSAS-II-tutorials/CalibrationTutorial/CalibrationTutorial.html) | S01–S02: Step 1 distinguishes set and calibrated distances; Step 2 Integrating the Calibrated Data includes obstructions and masks. |
| T04 | [Multiple distances, part 1: Determine Wavelength](https://advancedphotonsource.github.io/GSAS-II-tutorials/DeterminingWavelength/DeterminingWavelength.html) | S01: Step 2 Calibrating the Wavelength: First Image; Step 3 Calibrating all Images; Step 4 Parametric Fit to Find Wavelength. Read the complete method; the first-image estimate is not the final wavelength. |
| T05 | [Determine Starting Profile from a Standard](https://advancedphotonsource.github.io/GSAS-II-tutorials/CWInstDemo/FindProfParamCW.html) | S03: Intro, Individual peak fitting, Save Instrument Parameters. Standard-based starting profiles and the distinction between instrument and sample broadening; the example uses a laboratory instrument. |
| T06 | [Laboratory X-ray Powder Data](https://advancedphotonsource.github.io/GSAS-II-tutorials/LabData/Laboratory%20X.htm) | S04–S09: Steps 1–3 import/structure; Step 4 background; Step 5 initial refinement; Step 6 positions; Step 7 size/strain; Step 8 atomic parameters/results. Do not transfer the Bragg–Brentano displacement model directly to transmission data. |
| T07 | [Running a GSAS-II Refinement From a Python Script](https://advancedphotonsource.github.io/GSAS-II-tutorials/PythonScript/Scripting.htm) | S00, S05–S10: A. Create a Multi-step Script; B. Single-Step Refinement; C. Powder Pattern Simulation contains export/plot examples. Borrow output methods from C, not simulated data masquerading as observations. |
| T08 | [Neutron CW Powder Data](https://advancedphotonsource.github.io/GSAS-II-tutorials/CWNeutron/Neutron%20CW%20Powder%20Data.htm) | S04, S08: Step 2 structure; Step 3 atoms and the subsequent equivalence/occupancy constraint operations. Transfer constraint mechanics, not neutron scattering or instrument settings. |
| T09 | [Sequential refinement of multiple datasets](https://advancedphotonsource.github.io/GSAS-II-tutorials/SeqRefine/SequentialTutorial.html) | S04–S05: Step I / Prepare for fit: define phase fraction constraint. S10: representative fits, sequential refinement and initial-parameter propagation. |
| T10 | [Fitting the Starting Background using Fixed Points](https://advancedphotonsource.github.io/GSAS-II-tutorials/BkgFit/FitBkgTut.htm) | S05: Step 2 fixed points, Step 3 fitting, Step 4 background peak, Step 5 alternative models, Step 6 subsequent work. Distinguish background initialization from final refinement. |
| D01 | [GSASIIscriptable API](https://gsas-ii.readthedocs.io/en/latest/GSASIIscriptable.html) | Implementation reference for S00–S10: imports, G2Project, images/phases/histograms, refinement parameters and exports. Check the installed version's signatures. |

## Additional operational rules

Input hashes, manifest schemas, checkpoint names, run states, failure isolation, publication privacy checks, output directories and retention of the three project-tree categories are skill delivery conventions. The tutorials support the underlying project, calibration, refinement and scripting operations; they do not prescribe these filenames or acceptance thresholds.

The tutorials do not specify universally valid Rwp targets, background orders, angular limits or phase-content thresholds. Neither does this skill. Example values, anomalies and specific repairs do not automatically become recommendations.
