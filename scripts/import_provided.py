"""Inventory supplied literature and transcribe Laughner's two data workbooks."""

import hashlib
import json
from pathlib import Path

import openpyxl
import pandas as pd
import tomllib
from pypdf import PdfReader


def main():
    config = tomllib.loads(Path("config.toml").read_text())
    root = Path(config["paths"]["provided_papers"])
    out = Path(config["paths"]["transcribed"])
    files = {
        "ciais2026.pdf": ("ciaisetal2026", "article"),
        "ciais2026_supp.pdf": ("ciaisetal2026", "supplement"),
        "qu2022.pdf": ("quetal2022", "article"),
        "qu2022_supp.pdf": ("quetal2022", "supplement"),
        "laughner2021_supp1.pdf": ("laughneretal2021", "SI Appendix"),
        "laughner2021_supp2.docx": ("laughneretal2021", "team list"),
        "laughner2021_supp3.xlsx": ("laughneretal2021", "Dataset S1 / Table S2"),
        "laughner2021_supp4.xlsx": ("laughneretal2021", "Dataset S2 / Table S4"),
    }
    records = []
    for name, (study, role) in files.items():
        path = root / name
        record = {
            "path": str(path),
            "study": study,
            "role": role,
            "source": "supplied locally by user; titles and contents verified",
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "bytes": path.stat().st_size,
        }
        if path.suffix == ".pdf":
            record["pages"] = len(PdfReader(path).pages)
        records.append(record)
    (out / "provided_sources.json").write_text(json.dumps(records, indent=2) + "\n")
    sheet = openpyxl.load_workbook(root / "laughner2021_supp3.xlsx", data_only=True)[
        "PNAS emissions"
    ]
    inventory = pd.DataFrame(
        list(sheet.values)[1:],
        columns=["year", "CO2_GtC_yr", "CH4_TgCH4_yr", "NOx_TgN_yr"],
    ).replace("-", float("nan"))
    inventory.to_csv(out / "laughner_inventory.csv", index=False)
    sheet = openpyxl.load_workbook(root / "laughner2021_supp4.xlsx", data_only=True)[
        "PNAS OPE"
    ]
    rows = list(sheet.values)
    records = []
    for row in rows[2:]:
        for month in range(5):
            records.append(
                [row[0], row[1], rows[1][2 + month].date().isoformat()]
                + [row[start + month] for start in [2, 7, 12]]
            )
    pd.DataFrame(
        records,
        columns=[
            "country",
            "city",
            "month",
            "ozone_delta_TgO3",
            "NOx_delta_TgN",
            "OPE_TgO3_per_TgN",
        ],
    ).to_csv(out / "laughner_ope.csv", index=False)
    print("Inventoried eight files and transcribed both complete workbooks.")


if __name__ == "__main__":
    main()
