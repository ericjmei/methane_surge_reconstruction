"""Download only the small public inputs used by this analysis.

Run: pixi run python -m scripts.download_inputs
Existing files are checked against the recorded SHA256 and never overwritten.
NOAA snapshots are committed because the online files change over time.
"""

import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

import tomllib

from scripts.fetch import fetch


def main():
    config = tomllib.loads(Path("config.toml").read_text())
    raw = Path(config["paths"]["raw"])
    sources = json.loads(Path("data/input_sources.json").read_text())
    for name, source in sources.items():
        path = raw / name
        if not path.exists():
            result = fetch(source["url"], name)
            if result["status"] != "ok":
                raise RuntimeError(f"Download failed: {name}")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != source["sha256"]:
            raise RuntimeError(f"Source changed; review before using it: {name}")
        if path.suffix == ".zip":
            destination = path.with_suffix("")
            with ZipFile(path) as archive:
                for member in archive.infolist():
                    if (
                        not (destination / member.filename)
                        .resolve()
                        .is_relative_to(destination.resolve())
                    ):
                        raise ValueError("Unsafe archive member path")
                archive.extractall(destination)
        print(f"Verified {name}", flush=True)


if __name__ == "__main__":
    main()
