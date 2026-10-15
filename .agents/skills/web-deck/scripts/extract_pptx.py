#!/usr/bin/env python3
"""Print slide text from a .pptx, in slide order. Standard library only."""

import sys
import zipfile
from xml.etree import ElementTree as ET

P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def blocks(xml: bytes) -> list[list[str]]:
    root = ET.fromstring(xml)
    found: list[list[str]] = []

    def walk(el: ET.Element) -> None:
        if el.tag == P + "sp":
            lines = []
            for para in el.iter(A + "p"):
                line = "".join(t.text or "" for t in para.iter(A + "t")).strip()
                if line:
                    lines.append(line)
            if lines:
                found.append(lines)
            return
        if el.tag == P + "pic":
            found.append(["[image]"])
            return
        for child in el:
            walk(child)

    walk(root)
    return found


def slide_names(archive: zipfile.ZipFile) -> list[str]:
    names = [
        name
        for name in archive.namelist()
        if name.startswith("ppt/slides/slide") and name.endswith(".xml")
    ]

    def index(name: str) -> int:
        stem = name.rsplit("/", 1)[-1].removesuffix(".xml")
        return int(stem.removeprefix("slide"))

    return sorted(names, key=index)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: extract_pptx.py <file.pptx>", file=sys.stderr)
        return 2
    path = sys.argv[1]
    try:
        archive = zipfile.ZipFile(path)
    except FileNotFoundError:
        print(f"File not found: {path}", file=sys.stderr)
        return 1
    except zipfile.BadZipFile:
        print(f"Not a .pptx zip: {path}", file=sys.stderr)
        return 1

    with archive:
        names = slide_names(archive)
        if not names:
            print("No slides found", file=sys.stderr)
            return 1
        for number, name in enumerate(names, 1):
            print(f"\n===== SLIDE {number} =====")
            for block in blocks(archive.read(name)):
                for line in block:
                    print(line)
                print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
