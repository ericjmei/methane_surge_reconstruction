"""Build numerical outputs, execute the figure notebook, and compile LaTeX.

Run from the repository root: pixi run python -m scripts.build
Requires system pdflatex and bibtex in addition to the locked pixi environment.
"""

import argparse
import subprocess
from pathlib import Path

import nbformat
import tomllib
from nbclient import NotebookClient

from scripts.prepare import main as prepare


def latex(path, bibliography=False):
    """Compile a standalone document, with logs retained for diagnosis."""
    command = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", path.name]
    result = subprocess.run(
        command, cwd=path.parent, capture_output=True, text=True, check=False
    )
    if result.returncode:
        raise RuntimeError(result.stdout[-5000:])
    if bibliography:
        result = subprocess.run(
            ["bibtex", path.stem],
            cwd=path.parent,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode:
            raise RuntimeError(result.stdout)
    for _ in range(5):
        result = subprocess.run(
            command, cwd=path.parent, capture_output=True, text=True, check=False
        )
        if result.returncode:
            raise RuntimeError(result.stdout[-5000:])
        if not any(
            warning in result.stdout
            for warning in ["Rerun to get", "Rerun LaTeX", "Rerun with"]
        ):
            break
    else:
        raise RuntimeError(f"LaTeX cross-references did not converge for {path}")
    print(f"Compiled {path.with_suffix('.pdf')}", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--processed",
        action="store_true",
        help="Use committed processed data; do not re-extract raw inputs",
    )
    args = parser.parse_args()
    config = tomllib.loads(Path("config.toml").read_text())
    if not args.processed:
        prepare()
    notebook_path = Path(config["paths"]["notebook"])
    notebook = nbformat.read(notebook_path, as_version=4)
    NotebookClient(
        notebook,
        timeout=180,
        kernel_name="python3",
        resources={"metadata": {"path": str(Path.cwd())}},
    ).execute()
    nbformat.write(notebook, notebook_path)
    print("Executed figure notebook", flush=True)
    for path in sorted(Path("literature").glob("*.tex")):
        latex(path)
    for path in sorted(Path("docs/derivations").glob("*.tex")):
        latex(path)
    report = Path(config["paths"]["report"])
    # Preserve the user's original bibliography; omit personal reading notes and
    # local Zotero paths from the bibliography printed in the report.
    source = Path("methane_surge_comparison.bib").read_text()
    metadata = ("abstract =", "file =", "note =", "urldate =")
    bibliography = "\n".join(
        line for line in source.splitlines() if not line.lstrip().startswith(metadata)
    )
    (report / "references.bib").write_text(bibliography + "\n")
    latex(report / "report.tex", bibliography=True)


if __name__ == "__main__":
    main()
