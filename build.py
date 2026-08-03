#!/usr/bin/env python3
"""Build the Tri-Valley Long Term Care static site.

    python3 build.py

Writes plain HTML into site/ — no server, no dependencies. Open
site/index.html directly, or upload the folder to any static host.

Page copy lives in content/; shared chrome and components live in layout.py.
"""

import json
import shutil

import content
from layout import DATA, OUT, ROOT


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(ROOT / "assets", OUT / "assets")

    built = content.build(
        directory=json.loads((DATA / "directory.json").read_text(encoding="utf-8")),
        questions=json.loads((DATA / "family_questions.json").read_text(encoding="utf-8")),
        regulatory=json.loads((DATA / "regulatory.json").read_text(encoding="utf-8")),
    )

    print(f"Built {len(built)} pages into site/")
    for name in built:
        print(f"  {name}")


if __name__ == "__main__":
    main()
