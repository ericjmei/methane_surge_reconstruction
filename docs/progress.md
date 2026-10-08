# Progress and scope

The project contains nine bibliography entries. The bibliography's local
Zotero paths refer to a different computer and do not exist here. A local
copy of the published He et al. article was found in the user's papers directory.
No paper is marked read until its full text and any supplements have been reviewed.

The 2019–2022 window applies to all comparisons. Figures originally extending
to 2024 will be explicitly labeled as restricted-period reproductions.
Scientific parameter choices and deviations will be justified in LaTeX.

## Completed locally

- Starter instructions and style guide downloaded and followed. Project-scoped
  Python/pixi repository initialized; no inversion performed.
- Derived and implemented annual budget, exact residual, loss-flux conversion,
  common-burden scenario, and analytical constant-parameter trajectory.
- Four tests of the reusable budget functions pass.
- Acquired He main text and S1–S9; Qu 2024 main text and S1–S5/Table S1;
  Peng full article, supplement, reporting summary, monthly inversion and
  Figure 4 spreadsheet; Feng article with Appendices A–C; Stevenson article
  and full supplementary workbook; Lawrence full article.
- Read and documented these six studies. Main Laughner article read;
  supplementary review remains pending.
- Reconstructed He Figures 1–2 central curves approximately from the published
  rasters. Generated four additional comparison/data figures.
- Saved exact table transcriptions, digitization coordinates, processed netCDF
  outputs, download checksums, standalone one-page notes, and LaTeX report.
- Compiled the report and all nine one-page notes (six scientific summaries,
  one provisional main-text summary, two acquisition records). Executed all
  six figure cells. Verified the raw numerical input checksums locally.
- The final budget test run passed all four tests. Ruff check and format pass
  through pre-commit. Report figures and representative PDF pages were visually
  inspected; missing-material and digitization labels are retained throughout.

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

## Required inputs still requested from the user

1. Ciais et al. (2026), Science adx8262: full article and all supplements.
2. Qu et al. (2022), ERL ac8754: full article and all supplements.
3. Laughner et al. (2021): SI Appendix and Datasets S1–S2. PNAS returns 403;
   the PMC assets archive contains only main figures. The indexed Caltech
   copy returns 404 after its certificate-chain issue is accounted for.

The missing literature has not been substituted with abstracts or later-paper
summaries. Each missing entry has an explicit acquisition record. Once supplied,
read it in full, acquire its relevant data, update the comparisons and report,
and replace the corresponding incomplete note.

## GitHub delivery

The private repository is
[ericjmei/methane_surge_reconstruction](https://github.com/ericjmei/methane_surge_reconstruction).
GitHub CLI and SSH authentication have both been verified as `ericjmei`.
The `origin` remote uses SSH. The worklog repository's scoped deploy key was
not repurposed. The remaining inputs are the literature listed above.

## Exact reproduction limits

He does not supply the annual native posterior arrays in the acquired article
and supplement. The linked model code and input retrieval archive do not supply
the needed posterior diagnostics. The report inventories every main and
supplementary figure and states the unavailable inputs or incompatible time
interval. Digitization is not an independent reproduction of the inversion.
Common-burden adjustments are conditional sensitivity calculations, not native
posterior budgets. Full spatial and uncertainty comparisons await those data.
