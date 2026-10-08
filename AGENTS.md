# AGENTS.md

This repository should use an absolutely minimal research style.

## Code

- Keep analyses and code simple, direct, and readable.
- Add code, dependencies, and directory structure only when they are needed to achieve project goals.
- Prefer small functions and plain data (NumPy arrays, xarray objects) over custom classes or frameworks.
- This is not production code. It is an initial investigation intended to clarify the dynamics. Don't worry about backwards compatibility.
- Complex code inhibits learning. Keep it simple.
- Manage the environment with `pixi`. Add dependencies with `pixi add`, not by hand-editing `pyproject.toml`. Run commands through `pixi run`.
- Compute in `src/` and `scripts/`; plot in notebooks. Notebooks under `notebooks/explore/` may also contain computation. Move code from a notebook into `src/` only once it is used in more than one place.
- Use xarray for gridded and labeled data and netCDF for storing it. Keep coordinate names, units, and dimension order explicit.
- No hardcoded paths. Paths come from a config file.
- Formatting and linting are handled by `ruff` through pre-commit (`pixi run -e dev pre-commit run --all-files`). Notebooks are excluded from linting; do not reformat them.
- Do not add tests unless a function is reused across analyses. If you add tests, use `pytest`.

## Science

- Start from first principles. Do not invent physics or chemistry.
- Prefer the simplest model that can be tested against the data. Treat a stochastic or linear model as a null hypothesis before adding mechanisms.
- Do not impose heuristic or contrived constraints, conditions, or equations of any kind unless they are clearly requested and made explicit.
- State assumptions, units, timescales, boundary conditions, and the observable prediction of each model.
- Separate observations, model output, calculations, inferences, and speculative mechanisms.
- When a result depends on a parameter choice (e.g., a lifetime, an EOF truncation, a mask), say so and check the sensitivity.
- Derive before you code. Each equation gets a short file in `docs/derivations/` before implementation.
- Cite only papers you have read in full; otherwise mark `[unread]` and ask. Check Zotero first: `find /Users/ericm/Zotero/storage -maxdepth 2 -iname "*<author>*"`.
- Follow `eric-mei-academic-style-guide.md` for academic prose.

## Working with Eric

Defaults below hold unless Eric says otherwise in the prompt.

- A question or plan is the deliverable; do not implement until told. Scientific choices (parameter ranges, thresholds, what a result means) are Eric's: report the numbers and candidate interpretations, mark `TODO(eric)`, stop.
- Say so and stop before heavy computation.
- Commit only when asked, with notebook outputs intact. Push only when asked by name. Branches, not worktrees.
- Mark confidence on claims that would change what we do if wrong: `[certain]`, `[likely]`, `[guessing]`.
- One name per thing, defined once where it is introduced.
