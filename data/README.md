# Data provenance and definitions

`downloads.jsonl` records successful and failed retrievals, source URLs, UTC
timestamps, byte counts, and SHA256 checksums. Publisher challenges are rejected
as PDFs. Original URLs are retained; transient redirected URLs are not needed
to reproduce a download. Papers and most raw files are excluded from Git.
The two small NOAA text snapshots are committed because their public URLs change.

`input_sources.json` identifies the exact downloaded inputs needed by the analysis.
Run `pixi run python -m scripts.download_inputs` to acquire and verify them.
All selected inputs are small; no large-data storage was needed. The much larger
Peng wetland and 3-D chemistry archives are listed in the downloaded Figshare
metadata but are not inputs to this global-budget analysis.

| Tracked input | Meaning and source |
| --- | --- |
| `he_digitization.json` | Manual pixel coordinates and linear axis calibrations for central values in He Figs. 1–2; public Europe PMC raster archive. Not original posterior arrays. Two-pixel coordinate allowance; no uncertainty-band extraction. |
| `published_annual.csv` | Qu 2022 Table 1, Qu 2024 Table S1, and Feng 2023 Table 1. Annual fluxes in Tg CH4/yr; removal is positive. Qu 2022 additionally supplies native burden in Tg. Feng annual SDs are not assumed to be anomaly SDs; its OH percentages are relative to the prior. |
| `provided_sources.json` | Identified titles/roles, page counts, byte counts, and SHA256 checksums of eight supplied files. Original papers stay in ignored `papers/`. |
| `ciais_digitization.json` | Central markers from Ciais Fig. 2A and Fig. S3. Poppler rendering sizes, PDF pages, crop, pixel coordinates, and axis calibration are explicit. Signed removal is read on the left axis and rebased from 2010 to 2019. Two-pixel reading allowance is separate from model uncertainty. |
| `ciais_bottom_up.csv` | Complete 2019 and 2020–2022 anomaly columns of Supplement Table S1. Model domains are explicit; Asian rice estimates are not added to the global rice estimate. The original 2023 column is outside scope. |
| `qu2022_sensitivity.csv` | Main base case plus all eight Table S1 cases. Differences are 2020 minus 2019. Fluxes in Tg/yr, burdens in Tg, lifetimes in yr. Rounded columns need not close exactly. |
| `qu2022_regional.csv` | Entire main Table 2 regional totals and anomalies, in Tg CH4/yr. Published anomalies are retained rather than re-differencing rounded annual columns. |
| `laughner_inventory.csv`, `laughner_ope.csv` | Full numerical transcriptions of both workbooks. Missing methane inventory years remain NaN. Ozone-production efficiency is not a methane removal flux. Original historical context is retained in the input inventory, but no plotted analysis extends beyond 2019–2022. |
| `published_attribution.csv` | Reported Peng and Stevenson attribution numbers, preserving their different physical definitions and uncertainties. |
| `lawrence_oh_diagnostics.csv` | Lawrence 2001 Tables 2–3. All OH means in 10^6 molecules/cm3; lifetimes in years. These are methodological illustrations, not 2019–2022 reconstructions. |
| `raw/noaa/*.txt` | NOAA annual surface means and January-to-January growth, downloaded October 2026. File headers report September 2026 creation. These differ from He's November 2025 snapshot. |

`scripts/prepare.py` creates these processed products:

- `he_digitized.nc/csv`: calibrated values and their 2019 anomalies; the stacked
  emission contribution is retained separately from the independently digitized
  emission curve. Their maximum discrepancy is 0.35 Tg/yr.
- `published_annual.nc/csv`: own-2019 emission and sink changes, native tabulated
  budget growth, correctly rebased Feng OH percentages, and the explicitly
  conditional OH forcing using the NOAA burden proxy. `oh_forcing_native`
  uses Qu 2022's native burden; it remains missing for other reconstructions.
- `ciais.nc/csv`: own-2019 emission and signed OH-removal changes. Conditional
  OH forcing assumes NOAA burden and a 2019 OH-only lifetime of 9, 10, 11.1,
  or 12 years. 11.1 is a benchmark motivated by He, not a recovered Ciais
  lifetime. Emission SDs are read from published caps; no OH posterior
  uncertainty is reconstructed. The 2020 emission digitization differs from
  the main-text 22 Tg/yr value by only 0.065 Tg/yr.
- `laughner_scenario.nc`: uniform 2%, 3%, or 4% OH reduction in 2020, applied
  to a fixed 2019 NOAA burden and the same OH-lifetime sensitivity. The imposed
  forcing returns to zero after 2020; this does not imply zero accumulated
  burden. No native Laughner trajectory or flux inversion is reproduced.
- `qu2022_sensitivity.csv`, `qu2022_regional.csv`: the transcribed regional
  anomalies plus reported total-minus-emissions OH forcing for each ensemble
  case. This subtraction uses rounded numbers, distinct from the 4.663 Tg/yr
  native-burden calculation from main Table 1.
- `noaa.nc`: concentration/growth snapshots, 2.77 Tg/ppb conversion, and chemical
  lifetime sensitivity at 9–12 years. Chemical lifetime excludes soil uptake.
- `peng_source_data.csv`: exact cached cells of publisher Fig4a spreadsheet.
  Its OH sink SD is 0.7 Tg/yr, whereas the main text gives 0.8; both are retained
  rather than silently harmonized. Bottom-up source numbers also differ slightly
  from rounded main-text summaries.
- `peng_inversion.nc`: net surface-flux anomaly map and global totals from
  the archived monthly inversion. Positive is emission to the atmosphere. Fluxes
  are day-weighted before annual averaging. `annual_net_flux` is a mean rate in
  Tg per 365-day year. `calendar_year_total` integrates actual month lengths.
  Their 2020 anomalies are 5.35554 Tg/365-day-year and 6.884032 Tg/calendar-year;
  only the latter reproduces the publisher table because 2020 has an extra day.
- `stevenson_4mm.csv`: cached values of supplementary Table S13a, including
  individual precursor and regional contributions, in ppb methane per year.
  Blank CO/NMVOC entries for extra aviation mean those terms were not supplied
  for that correction; the notebook draws no bars for them.
- `audit.json`: numerical reproduction checks and headline derived quantities.

All scientific anomaly series have a 2019 baseline. Missing reconstruction years
are NaN. The code does not run a flux inversion, replace a reconstruction's
baseline with NOAA, assign unknown soil/other-chemical sinks, or equate a regional
precursor response with a regional methane flux. Derivations and the report
explain the conditional common-burden calculation.
