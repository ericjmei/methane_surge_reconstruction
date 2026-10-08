# Progress and scope

The project contains nine bibliography entries. The bibliography's local
Zotero paths refer to a different computer and do not exist here. A local
copy of the published He et al. article was found in the user's papers directory.
No paper is marked read until its full text and any supplements have been reviewed.

The 2019–2022 window applies to all comparisons. Figures originally extending
to 2024 will be explicitly labeled as restricted-period reproductions.
Scientific parameter choices and deviations will be justified in LaTeX.

## Completed analysis

- Starter instructions and style guide downloaded and followed. Project-scoped
  Python/pixi repository initialized; no inversion performed.
- Derived and implemented annual budget, exact residual, loss-flux conversion,
  common-burden scenario, and analytical constant-parameter trajectory.
- Four tests of the reusable budget functions pass.
- Acquired He main text and S1–S9; Qu 2024 main text and S1–S5/Table S1;
  Peng full article, supplement, reporting summary, monthly inversion and
  Figure 4 spreadsheet; Feng article with Appendices A–C; Stevenson article
  and full supplementary workbook; Lawrence full article. Ciais main text
  and 46-page supplement, Qu 2022 main text and three-page supplement, and
  Laughner SI Appendix, team list, and both workbooks were supplied locally.
- Read and documented all nine studies and their supporting materials.
- Reconstructed He Figures 1–2 central curves approximately from the published
  rasters. Generated six additional comparison/data figures.
- Saved exact table transcriptions, digitization coordinates, processed netCDF
  outputs, download checksums, standalone one-page notes, and LaTeX report.
- Replaced the acquisition records and provisional note with complete scientific
  summaries. Added Qu 2022 native OH forcing and its sensitivity/regional tables;
  Ciais digitization, bottom-up table, and conditional OH calculation; and
  Laughner workbook transcriptions and a prescribed-OH comparison scenario.
- The final budget test run passed all four tests. Ruff check and format pass
  through pre-commit. All eight figures, the 14-page report, and nine one-page
  summaries compile. Figures and representative PDF pages were visually
  inspected; numerical-data limitations and digitization labels are explicit.
- The additional numerical audit checks the 2019 baselines, missing years,
  Qu's native OH conversion, the independent algebraic form of Ciais's
  conversion, the prescribed OH pulse, sensitivity-case totals, both workbook
  transcriptions, and agreement with Peng and Ciais published numbers.

## Findings that guide the comparison

- [certain] He's adjustment uses loss **frequency** at the 2019 burden; an OH
  removal-flux difference is not the same quantity.
- [certain] Peng's archived monthly fluxes reproduce 6.884032 Tg when integrated
  over calendar years. Fixed 365-day mean-rate normalization gives 5.35554 Tg/yr.
- [certain] Qu 2024's rounded table implies 2019 growth of −3 Tg/yr. Replacing
  that baseline with NOAA's +26.70 Tg/yr would change its anomaly calculation.
- [likely] Prior structure, initialization, OH degrees of freedom, and sampling
  contribute to differences between studies; available data do not isolate the
  causal contribution of each modeling choice.

## Literature acquisition complete

All nine full texts and supporting materials have been reviewed. The supplied
Qu file was initially a copy of the 2024 paper; it was replaced with the correct
2022 article and then its separate three-page supplement. File identities and
checksums are in `data/provided_sources.json`. No literature remains requested.

New numerical checks:

- [certain] Qu 2022 rounded native burdens and OH removal give 4.66323 Tg/yr
  OH forcing, versus the main text's rounded 5 Tg/yr. Its emission forcing is
  31 Tg/yr. The 2020 native growth anomaly is 31 Tg/yr, not the 14.2378 Tg/yr
  NOAA anomaly.
- [certain] Qu's Table S1 settings span emission forcing 19–36 Tg/yr, while
  total forcing spans 35–39. Prior errors and regularization change the split.
- [certain] Ciais's headline OH percentage averages adjacent-year fractions
  over 2019–2023. It is not He's fixed-2019 forcing fraction or an R-squared.
- [certain] Ciais emission digitization gives 21.94 Tg/yr in 2020 versus the
  reported 22.0. The conditional OH corrections explicitly assume NOAA burden
  and a 2019 OH lifetime, since native reference removal is not tabulated.
- [certain] Laughner's 2021 curves are extrapolations. Its 2–4% OH envelope
  reflects temporal variation; its inventory workbook contains no CH4 values
  for 2018–2020. A 3% uniform reduction at an 11.1-yr OH lifetime corresponds
  conditionally to 13.9742 Tg/yr at the 2019 NOAA burden.

## GitHub delivery

The private repository is
[ericjmei/methane_surge_reconstruction](https://github.com/ericjmei/methane_surge_reconstruction).
GitHub CLI and SSH authentication have both been verified as `ericjmei`.
The `origin` remote uses SSH. The worklog repository's scoped deploy key was
not repurposed. The completed literature and report update is on the
`complete-literature` branch for review. All literature is present. The remaining
limits concern numerical posterior outputs, as documented below.

## Exact reproduction limits

He does not supply the annual native posterior arrays in the acquired article
and supplement. The linked model code and input retrieval archive do not supply
the needed posterior diagnostics. The report inventories every main and
supplementary figure and states the unavailable inputs or incompatible time
interval. Digitization is not an independent reproduction of the inversion.
Common-burden adjustments are conditional sensitivity calculations, not native
posterior budgets. Full spatial and uncertainty comparisons await those data.
