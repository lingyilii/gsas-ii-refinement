# Staged refinement and diagnostic criteria

[中文](../refinement.md) | **English**

Read [inputs and calibration](input-and-calibration.md) first. Source IDs refer to the [tutorial map](tutorial-map.md). This is a tutorial-based decision workflow; the experiment, data and current residuals determine which parameters to release.

## S03: Instrument profile and optional individual-peak diagnostics

**Tutorial mapping:** T05 / Intro, Individual peak fitting, Save Instrument Parameters.

Prefer a compatible instrument parameter file. If unavailable, use a suitable standard: background and peak areas → positions → widths when justified → instrument profile expression → save `.instprm`. Stabilize each stage before adding variables. Calibration should cover the sample's fitted angular range; declare any extrapolation.

Independent peak fits help diagnose overlap and anomalous widths; they are not mandatory before every Rietveld refinement. Peak List positions, areas and widths do not automatically become a phase's atomic structure or a Rietveld model.

If the standard has size/strain broadening, establish an evidence-based separation. Without independent support, describe the result as an effective profile. Do not absorb all sample broadening into instrument terms and then refine the same contributions again as sample size/strain.

**Evaluation:** inspect positions, maxima, both tails and background together. Negative individual-peak `sigma²`/`gamma` values need attention. Do not require every U/V/W coefficient to be positive; assess the combined Gaussian variance and actual profile throughout the fitted range. Axial asymmetry must suit the geometry, not copy a laboratory example's SH/L. Several width terms may be strongly correlated over a narrow range; reduce degrees of freedom.

Save the standard project and profile evidence. An unchecked Refine box does not mean a parameter was never refined; consult stage logs and before/after values.

## S04: Import and verify structural models

**Tutorial mapping:** T06 Steps 1–3; T08 Steps 2–3; T09 Step I / Read phase files and Map both phases.

1. Import the supplied candidate CIFs into a new or accepted integration project. Verify names against actual composition; filenames do not establish structural correctness.
2. Check space-group setting, origin, cell, symmetry-generated atom counts, element types, coordinates, occupancies and ADPs. For mixed sites, check total occupancy and composition at the same crystallographic site.
3. Link each candidate phase to the official PWDR and check `Use Histogram`. A phase present in the project is not necessarily included in that histogram's fit. Do not include old trial PWDRs unintentionally.
4. Calculate an initial pattern and compare reflection positions and major peak groups. A few matching peaks do not establish uniqueness; a CIF is a model to test. For obvious position mismatches, check wavelength, axis units, calibration and structure before changing the background.

**Checkpoint:** save the initial structural project, fixed/refined atom flags, candidate phases and links. Without atomic structural information, do not call Pawley/Le Bail extraction Rietveld refinement. Verify the appropriate tutorial before changing methods.

## S05: Background, overall scale and relative phase contributions

**Tutorial mapping:** T06 Steps 4–5; T10 Steps 2–6; T09 Step I / Prepare for fit: define phase fraction constraint.

Start with a simple background that follows nonpeak regions. Inspect low-angle scattering, broad diffuse features and container signals. Fixed background points may initialize the model; reassess whether to release background parameters in the final fit. Do not absorb weak diffraction peaks with a high-order polynomial. There is no universal background order.

Choose an identifiable scale parameterization before the first fit. Possibilities include fixing the overall scale and varying phase scales, or varying the overall scale with normalized phase-scale constraints. Do not freely vary the overall scale and every phase scale without constraints. Check the actual independent variable list and whether constraints are active.

Do not conflate phase scales, interface phase fractions, exported Wt. fractions and atomic `frac`. Read weight fractions according to GSAS-II's definition for the current model; do not simply normalize arbitrary scales and call them weight fractions. Normalized modeled crystalline fractions do not determine total amorphous content without independent calibration.

**Acceptance:** reasonable calculated magnitude, background that does not swallow peaks, and no unjustified negative or degenerate phase scales. When a phase approaches zero, its cell/structure may be unidentifiable; assess support before refining all its parameters.

## S06: Peak positions

**Tutorial mapping:** T06's position discussion after Step 5 and Step 6; geometry in T01, T03–T04.

After overall intensities stabilize, release cell parameters supported by the data. Then consider zero or specimen displacement based on geometry and residuals. Do not release wavelength, cell, zero and multiple displacement terms together without justification. Transmission and Bragg–Brentano displacement models differ.

**Evaluation:** magnify peaks at several angles. Constant-direction and angle-dependent shifts can suggest different causes but require model testing. Positive/negative residual lobes may indicate position mismatch. Inspect cell changes, correlations and chemical plausibility, not only Rwp.

## S07: Peak widths and shapes

**Tutorial mapping:** T06 Steps 6–7; T05's instrument/sample broadening distinction.

With stable positions, preferably fix calibrated instrument profiles and test identifiable sample size and microstrain terms incrementally. Start with a simple isotropic model. Consider anisotropy only when multiple reflections show systematic hkl dependence and an appropriate tutorial/physical rationale exists. Compare candidate models from the same checkpoint so a failed fit does not contaminate the next trial.

**Evaluation:** compare maxima, flanks, tails and overlapping regions. An area adjustment alone may not resolve a height mismatch. Effective size must be positive and strain physically reasonable. Boundary-limited parameters, large uncertainties or strong instrument-term correlations support only effective widths or limits, not precise crystallite sizes.

## S08: Structural parameters and conditional intensity corrections

**Tutorial mapping:** T06 Step 8; T08's coordinates, ADPs, same-site equivalences and occupancy constraints. Find a suitable tutorial through T00 for preferred orientation or other extensions; these are not mandatory T06 steps.

Only after positions, profiles and scales stabilize should coordinates and ADPs be tested in groups. Respect symmetry; inspect bond lengths, coordination, composition and correlations. Anisotropic ADPs require sufficient information and positive-definiteness checks; simple data need not support them.

Refine occupancies, element exchange or defect concentrations only when scattering contrast and data quality support them. Establish appropriate site-total/composition constraints first and avoid compensation with scales or ADPs. Convergence alone does not validate occupancies for weakly scattering elements or elements with similar scattering factors.

If positions/widths agree but relative reflection intensities systematically disagree, first check structure, absorption, polarization and 2D ring uniformity, then assess preferred orientation. Do not assume one common axis for all layered, needle-like or plate-like materials. Avoid simultaneously freeing several mechanisms that explain the same intensity discrepancy.

## S09: Final combined review

**Tutorial mapping:** T06 / Refinement results; T07's staged execution/statistics; T09's sequential results. The following acceptance decisions are additional quality rules.

Run the final fit with the incrementally justified variable set and necessary constraints. Record before/after values, independent variable count, observation count, Rwp, reduced χ², maximum shift/σ, convergence and warnings. Unavailable version-dependent fields are unknown, not zero.

| Observation | First checks | Unsupported shortcut |
|---|---|---|
| Lower Rwp with dropped parameters, singularity or false minimum | Redundant scales, refining zero-content phases, constraints, excess variables, insufficient information | “Converged; add more parameters” |
| Systematic residual at peak maxima | Position, width, integration sampling, overlap and area; magnify locally | “Only intensity needs adjustment” |
| Independent unexplained peaks | Missing/wrong phase, container/stray signals, model defects | “Increase background order” |
| Nearly zero phase scale or large uncertainty | Independent reflections and identifiability | “The phase is definitely absent” |
| Negative Uiso, abnormal occupancy or invalid widths | Data/model problems, correlations, constraints, excess freedom | “Low Rwp validates the structure” |
| High χ² despite visual agreement | High counts, uncertainty model, correlated noise, systematic errors | “Reduce weights to make it good” |
| Difference curve entirely below zero | Display offset and actual numerical mean | “Calculated intensities are too high everywhere” |

Read the final `.lst` and GPX Covariance rather than relying only on screenshots. For divergence, NaNs, dropped parameters or false minima, return to the previous accepted state and reduce variables or repair the model based on evidence; do not merely add unlimited cycles. If OK has already loaded a failed result, preserve it as diagnostic evidence and restore a valid checkpoint instead of continuing from it.

Assign the final status using [execution-and-delivery.md](execution-and-delivery.md). There is no universal Rwp pass threshold. Direct statistical comparisons require the same fitted range, uncertainty model and input conditions.
