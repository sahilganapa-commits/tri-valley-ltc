#!/usr/bin/env python3
"""Static WCAG 2.1 AA checks over the built pages.

    python3 tools/check_a11y.py

Covers the criteria that can be judged from markup. Contrast against
photographs needs rendering, so that lives in tools/check_contrast.py.

This is not a substitute for testing with a real screen reader, and it cannot
judge whether alt text is *accurate* — only that it exists.
"""

import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

SITE = Path(__file__).parent.parent / "site"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}

# Link text that tells a screen-reader user nothing when read out of context.
VAGUE_LINKS = {"click here", "here", "read more", "more", "link", "this",
               "learn more", "details", "continue"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.issues = []
        self.stack = []
        self.headings = []          # (level, text)
        self.ids = Counter()
        self.landmarks = Counter()
        self.labels_for = set()
        self.fields = []            # (tag, attrs)
        self.imgs = []
        self.links = []             # (href, text)
        self.tables = 0
        self.th_scope = 0
        self.th_total = 0
        self.lang = None
        self.title = ""
        self._grab = None
        self._buf = []
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag not in VOID:
            self.stack.append(tag)
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "title":
            self._in_title = True
        if "id" in a:
            self.ids[a["id"]] += 1
        if tag in ("main", "nav", "header", "footer"):
            self.landmarks[tag] += 1
        if tag == "img":
            self.imgs.append(a)
        if tag == "label":
            self._label_depth = len(self.stack)
            if "for" in a:
                self.labels_for.add(a["for"])
        if tag in ("input", "select", "textarea"):
            # A control nested inside <label> is implicitly associated with it,
            # which is valid and what screen readers announce.
            self.fields.append((tag, a, "label" in self.stack))
        if tag == "table":
            self.tables += 1
        if tag == "th":
            self.th_total += 1
            if "scope" in a:
                self.th_scope += 1
        if re.fullmatch(r"h[1-6]", tag):
            self._grab = ("h", int(tag[1])); self._buf = []
        if tag == "a":
            self._grab = ("a", a.get("href", "")); self._buf = []

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            while self.stack and self.stack.pop() != tag:
                pass
        if self._grab:
            kind, val = self._grab
            text = " ".join("".join(self._buf).split())
            if kind == "h" and re.fullmatch(r"h[1-6]", tag):
                self.headings.append((val, text)); self._grab = None
            elif kind == "a" and tag == "a":
                self.links.append((val, text)); self._grab = None

    def handle_data(self, d):
        if self._in_title:
            self.title += d
        if self._grab:
            self._buf.append(d)


def check(path):
    src = path.read_text(encoding="utf-8")
    p = Page(); p.feed(src); p.close()
    name = path.name
    out = []

    # 3.1.1 Language of page
    if not p.lang:
        out.append("3.1.1  <html> has no lang attribute")

    # 2.4.2 Page titled
    if not p.title.strip():
        out.append("2.4.2  page has no <title>")

    # 1.3.1 / 2.4.6 heading structure
    h1s = [h for h in p.headings if h[0] == 1]
    if len(h1s) != 1:
        out.append(f"1.3.1  expected exactly one <h1>, found {len(h1s)}")
    prev = 0
    for lvl, text in p.headings:
        if prev and lvl > prev + 1:
            out.append(f"1.3.1  heading level jumps h{prev} -> h{lvl} at {text[:40]!r}")
        prev = lvl
        if not text.strip():
            out.append(f"2.4.6  empty h{lvl}")

    # 4.1.1 unique ids
    for i, n in p.ids.items():
        if n > 1:
            out.append(f"4.1.1  duplicate id {i!r} used {n} times")

    # 1.3.1 landmarks
    if p.landmarks["main"] != 1:
        out.append(f"1.3.1  expected one <main>, found {p.landmarks['main']}")

    # 1.1.1 non-text content
    for img in p.imgs:
        if "alt" not in img:
            out.append(f"1.1.1  <img> without alt: {img.get('src','?')[:60]}")

    # 3.3.2 labels for every control
    for tag, a, wrapped in p.fields:
        if a.get("type") in ("hidden", "submit", "button"):
            continue
        # aria-hidden removes the control from the accessibility tree entirely,
        # so no assistive technology can reach it and a label would be pointless.
        # The spam honeypot is the only such field on this site; it is also
        # display:none and tabindex=-1, so no visitor meets it either.
        if a.get("aria-hidden") == "true":
            continue
        fid = a.get("id")
        labelled = wrapped or (fid and fid in p.labels_for) \
            or "aria-label" in a or "aria-labelledby" in a
        if not labelled:
            out.append(f"3.3.2  <{tag} name={a.get('name','?')}> has no associated label")

    # 2.4.4 link purpose
    for href, text in p.links:
        t = text.strip().lower().rstrip(".")
        if not t and "aria-label" not in src:
            continue
        if t in VAGUE_LINKS:
            out.append(f"2.4.4  uninformative link text {text.strip()!r} -> {href}")

    # 1.3.1 table headers
    if p.tables and p.th_total and p.th_scope < p.th_total:
        out.append(f"1.3.1  {p.th_total - p.th_scope} of {p.th_total} <th> lack scope")

    # 2.4.1 bypass blocks
    if 'class="skip"' not in src:
        out.append("2.4.1  no skip link")

    # 1.4.4 / 1.4.10 zoom must not be blocked
    m = re.search(r'<meta name="viewport" content="([^"]*)"', src)
    if m and ("user-scalable=no" in m.group(1) or "maximum-scale=1" in m.group(1)):
        out.append("1.4.4  viewport blocks zoom")

    # 2.5.3 button text must not be empty
    for m in re.finditer(r"<button[^>]*>(.*?)</button>", src, re.S):
        inner = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        if not inner and "aria-label" not in m.group(0):
            out.append("2.5.3  <button> with no accessible name")

    return name, out


def main():
    pages = sorted(SITE.glob("*.html"))
    total = 0
    for path in pages:
        name, issues = check(path)
        total += len(issues)
        if issues:
            print(f"\n{name}")
            for i in issues:
                print(f"   {i}")
    print(f"\n{len(pages)} pages checked, {total} issue(s)")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
