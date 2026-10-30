# Inputs, geometry calibration and integration

[中文](../input-and-calibration.md) | **English**

## S00: Establish input identity and available evidence

**Tutorial mapping:** import, calibration prerequisites and scripting environment in [T01–T04, T06–T07 and D01](tutorial-map.md). Provenance manifests are an additional operational rule.

Inventory files before reading their contents. For identical filenames, compare absolute paths, sizes and SHA-256 hashes. Prefer the user's latest specified input location. Do not search unrelated directories to guess sample identity. An existing GPX can be a resumption point but does not replace provenance verification.

| Input | Check | If missing |
|---|---|---|
| 2D images and sidecar metadata | Array dimensions, physical pixel dimensions/units, binning, orientation/rotation/flipping, data type and previous dark/background subtraction | Verify instrument records for critical geometry; do not infer pixel size from pixel count |
| Measured calibration standard or valid calibration project | Standard identity, lattice reference, measurement conditions/date and compatibility with sample configuration | Teaching or provisional projects are possible, but do not claim calibrated geometry |
| Wavelength/energy records | Units, monochromatic/doublet radiation, source, credibility and conflicting fields | Record conflicts; do not resolve them from filenames or arbitrary averages |
| 1D powder pattern | Axis type: 2θ, d, Q or TOF; angle units; intensities and uncertainty/weight meanings; prior integration | Declare weighting assumptions if uncertainties are absent; never treat intensity as its standard deviation |
| Instrument parameter file/standard pattern | Radiation, geometry, wavelength, angular coverage, detector settings and separation of instrument/standard broadening | Software defaults are not calibration results |
| CIF/structural model | Composition, space group/setting/origin, cell, coordinates, occupancy, ADPs and candidate-phase identity | A peak-position reference card alone is insufficient for structural Rietveld refinement; obtain a structure or limit the task to peak fitting/indexing |
| Optional blank, dark, flat-field or mask | Format, dimensions, exposure/normalization and whether already applied | Avoid duplicate or incompatible corrections |
| Existing GPX/LST/run record | Image references, PWDR provenance, phase links, last valid state and software version | Mark untraceable projects provisional and verify before resuming |

Keep originals and CIFs read-only and create a separate output directory. Record each parameter's value, unit, source, fixed/refined status and reason. Keep nominal acquisition distance separate from calibrated distance. Do not equate goniometer radius, image distance or other geometry quantities merely because their interface fields look similar.

## S01: Calibrate image geometry and handle wavelength

**Tutorial mapping:** T01 Steps 2–3; T04 when determining wavelength; T03 Step 1 for distance calibration with known wavelength.

1. Import the original image and check physical dimensions. Adjust display contrast to inspect weak rings, obstructions and bad pixels. Display clipping is not detector saturation and is not grounds for removing data.
2. Prefer a valid calibration for the same configuration. If recalibrating, import a known standard, select the correct calibrant/lattice reference, choose well-distributed ring points following the tutorial, check ring assignment and refine geometry that the data constrain.
3. Fix a credible known wavelength and adjust the necessary geometry. Distance is neither always fixed nor always free: calibration conditions determine that choice. An unknown wavelength requires sufficiently constrained standard/multiple-distance measurements and the complete T04 procedure, not unrestricted simultaneous variation of every geometrical quantity.
4. Inspect several rings and azimuths at higher magnification. Check calculated ring centers against observations, spurious rings, obstructions, residuals and parameter stability. Apparently concentric rings from an unknown sample do not replace calibration.
5. Save the calibration project, image controls and supporting evidence. Copy only to compatible configurations. Recheck changes in distance, binning, orientation or instrument setup rather than blindly copying all settings.

**Acceptance:** distinguish known and fitted quantities, establish parameter provenance and eliminate evident systematic ring misalignment. Otherwise use `needs_input` or `provisional`. Reviewable teaching may continue, but do not deliver claims of accurate absolute lattice parameters.

**Why Lam is not refined by default:** wavelength and the overall d-spacing scale are coupled through Bragg's law. A freely refined sample cell does not independently anchor wavelength. The PWDR wavelength must also be consistent with its integration. If geometry/wavelength calibration changes, evaluate reintegration rather than simply changing the final pattern's label.

## S02: Masks, integration limits and PWDR

**Tutorial mapping:** T02 Steps 2–3; T03 Step 2 Integrating the Calibrated Data.

| Decision | Evidence and action | Verification |
|---|---|---|
| Inner limit | Display limits; exclude the beamstop, shadow transitions and invalid low-angle regions while retaining trustworthy signal | Zoom into the center and read boundary angles with the cursor; a previously used angle is not a justification |
| Outer limit | Inspect valid detector coverage, edge defects and required azimuths. Complete rings are a conservative choice; partial rings require declared coverage/uniformity assumptions | Inspect several azimuths and valid pixels near the boundary; rectangular corners or full-integration mode do not guarantee complete rings |
| Masks | Treat supports, bad pixels, saturation and stray spots according to their actual shapes | Save and visually review masks. Spots can be coarse-grain diffraction rather than bad pixels |
| Azimuth | Choose full or sector integration from obstructions, texture and ring uniformity | Compare sector patterns when needed; document limitations of full-ring averaging for nonuniform rings |
| Angular bins | Start from pixels, geometry and the narrowest useful peak, then check integrated FWHM sampling | T02 recommends more than 6 points per FWHM; finer bins do not create resolution or remove pixel correlations |
| Intensity corrections | Base polarization, absorption, dark/flat/background treatment on experimental evidence and track corrections already applied | Prevent duplication between image integration and subsequent intensity models. Do not automatically clip negative background-subtracted values to zero |

For small detector tilt, `r ≈ L tan(2θ)` helps explain angular boundaries; actual settings must use calibrated GSAS-II geometry. Overlay colors may vary by version, so identify limits by their Inner/Outer labels and values.

Integrate one representative image first. Check the whole pattern, narrow peaks, positional continuity, edge artifacts, valid uncertainties/weights and sector differences. Reintegrate after geometry or mask changes and identify the official current PWDR.

Integration limits determine generated data; Rietveld `Limits` determine the fitted subset. Record reasons such as obstructions, containers or model applicability for exclusions. Do not discard difficult peaks solely to reduce Rwp.

**Checkpoint:** save a GPX with original IMG, Image Controls, Masks and the official PWDR, together with provenance links. Archive earlier trial patterns if useful, but do not silently include duplicate patterns in the final fit.
