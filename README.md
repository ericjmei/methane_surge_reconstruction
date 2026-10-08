# Methane surge reconstruction

Reproduce the published steady-state budget adjustment of He et al. (2026,
doi:10.1126/sciadv.adz9007) and compare methane reconstructions over 2019–2022.
All anomalies use 2019 as the baseline. Flux inversion is outside the scope.

The [compiled report](report/report.pdf) and [LaTeX source](report/report.tex)
are **provisional**. Two full papers, Laughner's supplementary materials, and
GitHub authentication remain missing. See [progress](docs/progress.md).

Implemented and checked:

- He's three-term annual decomposition, its exact neglected terms, and a
  separately integrated constant-budget counterfactual.
- Approximate reconstructions of He Figures 1 and 2 from digitized central
  curves, restricted to 2019–2022 and labeled as digitizations.
- Cross-study emission/OH figures, a common-burden sensitivity calculation,
  methodology tables, and regional evidence from the accessible studies.
- Numerical reproduction of Peng's 6.884032 Tg calendar-year emission change
  from archived monthly fluxes, including an explicit leap-year audit.
- Separate one-page PDF/LaTeX reading notes. Unavailable papers have clearly
  labeled acquisition records rather than invented scientific summaries.

Rebuild the figures and documents from the committed processed datasets:

```bash
pixi run python -m scripts.build --processed
```

Re-extract all numerical inputs and then build:

```bash
pixi run python -m scripts.download_inputs
pixi run python -m scripts.build
```

The build needs `pdflatex` and `bibtex` on PATH (tested with TeX Live 2022).
All Python dependencies are pinned by `pixi.lock`. The first download command
verifies checksums and uses the committed NOAA snapshot; it does not replace
that snapshot with a newer online revision. No inversion or heavy computation
is run. The figure notebook is committed with outputs.

Validation:

```bash
pixi run -e dev python -m pytest -q
pixi run -e dev pre-commit run --all-files
```

Scientific derivations are in [docs/derivations](docs/derivations/), data
definitions in [data/README.md](data/README.md), and plotting code in
[notebooks/reconstruction.ipynb](notebooks/reconstruction.ipynb).

The supplied `AGENTS.md` and academic style guide are copied from
https://github.com/ericjmei/repo_starter. The project request authorizes
implementation, documented scientific decisions, commits, and GitHub upload.

Run Python through `pixi run`. Resource locations are in `config.toml`.
Downloaded papers and large raw inputs are excluded from Git; the small NOAA
snapshots and processed numerical datasets are included. Retrieval URLs and
checksums are recorded in `data/downloads.jsonl`. No large-data directory was
needed. No pull request was merged and no deployment was performed.
