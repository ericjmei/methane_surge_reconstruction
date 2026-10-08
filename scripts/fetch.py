"""Fetch a public resource and record its original URL, time, and SHA256.

Usage: pixi run python scripts/fetch.py URL relative/path [URL relative/path ...]
Paths are relative to the raw directory specified in config.toml.
Failed downloads are recorded; an HTML challenge is never accepted as a PDF.
"""

import datetime as dt
import hashlib
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import tomllib


def fetch(url, relative_path, config_path=Path("config.toml")):
    config = tomllib.loads(config_path.read_text())
    root = config_path.resolve().parent
    path = root / config["paths"]["raw"] / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "url": url,
        "path": str(path.relative_to(root)),
        "retrieved_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    }
    try:
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "methane-reconstruction/0.1 (academic reproducibility)"
            },
        )
        with urllib.request.urlopen(request, timeout=60) as response:
            content = response.read()
            redirected = urllib.parse.urlsplit(response.url)
            if "X-Amz-" in redirected.query:
                record["resolved_url"] = urllib.parse.urlunsplit(
                    (redirected.scheme, redirected.netloc, redirected.path, "", "")
                )
                record["redirect_query_removed"] = (
                    "Transient signed query omitted; original public URL retained"
                )
            else:
                record["resolved_url"] = response.url
        if path.suffix == ".pdf" and not content.startswith(b"%PDF"):
            raise ValueError("Response is not a PDF (possible access challenge)")
        path.write_bytes(content)
        record.update(
            status="ok", bytes=len(content), sha256=hashlib.sha256(content).hexdigest()
        )
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        record.update(status="failed", error=str(exc))
    manifest = root / "data" / "downloads.jsonl"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    with manifest.open("a") as stream:
        stream.write(json.dumps(record) + "\n")
    print(json.dumps(record), flush=True)
    return record


if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) % 2 != 1:
        raise SystemExit(__doc__)
    for url, relative_path in zip(sys.argv[1::2], sys.argv[2::2]):
        fetch(url, relative_path)
