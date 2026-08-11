#!/usr/bin/env python3
"""Measure real text-on-photograph contrast and fail if it breaks WCAG 1.4.3.

    python3 tools/check_contrast.py            # needs the preview server running

Contrast against a photograph cannot be reasoned about from CSS — it depends on
the pixels of whichever image is in place. So this renders each page, hides the
text, samples the background exactly where that text sits, and computes the
ratio against the lightest pixel found (the worst case).

Run it after swapping any hero photograph. A picture with a brighter sky can
push the navigation below the threshold without anything in the CSS changing.

Thresholds (WCAG 2.1 AA):
  1.4.3  normal text  4.5:1
  1.4.3  large text   3:1   (>=24px, or >=18.66px bold)
"""

import json
import re
import struct
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASE = "http://127.0.0.1:8000"
SITE = Path(__file__).parent.parent / "site"

# selector -> (label, required ratio). Large display type only needs 3:1.
TARGETS = [
    (".nav__link", "nav links", 4.5),
    (".brand__name", "wordmark", 4.5),
    (".brand__sub", "tagline", 4.5),
    (".hero__headline", "hero headline", 3.0),
    (".hero__sub", "hero standfirst", 4.5),
]

PROBE = """
<style>%(hide)s{visibility:hidden!important}</style>
<script>
window.addEventListener('load',function(){setTimeout(function(){
  var out={};
  %(sel)s.forEach(function(sel){
    out[sel]=[];
    document.querySelectorAll(sel).forEach(function(el){
      var r=el.getBoundingClientRect();
      if(r.width>0&&r.height>0)
        out[sel].push([Math.round(r.left),Math.round(r.top),
                       Math.round(r.right),Math.round(r.bottom)]);
    });
  });
  document.title='BOX'+JSON.stringify(out);
},400)});
</script>
"""


def decode_png(path):
    d = path.read_bytes()
    pos, idat = 8, b""
    w = h = ct = 0
    while pos < len(d):
        ln = struct.unpack(">I", d[pos:pos + 4])[0]
        typ = d[pos + 4:pos + 8]
        if typ == b"IHDR":
            w, h, _, ct = struct.unpack(">IIBB", d[pos + 8:pos + 18])
        elif typ == b"IDAT":
            idat += d[pos + 8:pos + 8 + ln]
        pos += 12 + ln
    raw = zlib.decompress(idat)
    ch = {0: 1, 2: 3, 4: 2, 6: 4}[ct]
    stride = w * ch

    def paeth(a, b, c):
        p = a + b - c
        pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
        return a if pa <= pb and pa <= pc else (b if pb <= pc else c)

    prev, rows, i = bytearray(stride), [], 0
    for _ in range(h):
        f = raw[i]; i += 1
        line = bytearray(raw[i:i + stride]); i += stride
        for x in range(stride):
            a = line[x - ch] if x >= ch else 0
            b = prev[x]
            c = prev[x - ch] if x >= ch else 0
            if f == 1: line[x] = (line[x] + a) & 255
            elif f == 2: line[x] = (line[x] + b) & 255
            elif f == 3: line[x] = (line[x] + ((a + b) >> 1)) & 255
            elif f == 4: line[x] = (line[x] + paeth(a, b, c)) & 255
        rows.append(bytes(line)); prev = line
    return w, h, ch, rows


def luminance(rgb):
    c = [v / 255 for v in rgb]
    c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]


def contrast_with_white(rgb):
    return 1.05 / (luminance(rgb) + 0.05)


def chrome(args):
    return subprocess.run([CHROME, "--headless", "--disable-gpu", *args],
                          capture_output=True, text=True, timeout=60).stdout


def check(page, width=1470, height=900):
    selectors = [t[0] for t in TARGETS]
    probe = PROBE % {"hide": ",".join(selectors),
                     "sel": json.dumps(selectors)}
    tmp = SITE / f"_contrast-{page}.html"
    tmp.write_text(Path(SITE / f"{page}.html").read_text()
                   .replace("</body>", probe + "</body>"))
    try:
        dom = chrome([f"--window-size={width},{height}", "--virtual-time-budget=8000",
                      "--dump-dom", f"{BASE}/{tmp.name}"])
        m = re.search(r"<title>BOX(\{.*?\})</title>", dom, re.S)
        if not m:
            return [(page, "?", 0, 0, "could not measure")]
        boxes = json.loads(m.group(1))

        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
            shot = Path(f.name)
        chrome([f"--window-size={width},{height}", "--virtual-time-budget=8000",
                "--hide-scrollbars", f"--screenshot={shot}", f"{BASE}/{tmp.name}"])
        w, h, ch, rows = decode_png(shot)
        shot.unlink()

        results = []
        for sel, label, need in TARGETS:
            worst, px = 0, None
            for (l, t, r, b) in boxes.get(sel, []):
                for y in range(max(0, t), min(b, h)):
                    for x in range(max(0, l), min(r, w)):
                        o = x * ch
                        rgb = (rows[y][o], rows[y][o + 1], rows[y][o + 2])
                        lu = luminance(rgb)
                        if lu > worst:
                            worst, px = lu, rgb
            if px is None:
                continue
            results.append((page, label, contrast_with_white(px), need, px))
        return results
    finally:
        tmp.unlink(missing_ok=True)


def main():
    pages = [p.stem for p in sorted(SITE.glob("*.html"))
             if "hero--cover" in p.read_text()]
    if not pages:
        sys.exit("no pages with a photographic hero found")

    print(f"{'page':<18} {'element':<17} {'measured':>10} {'needs':>7}   result")
    print("-" * 70)
    failures = 0
    for page in pages:
        for _, label, got, need, px in check(page):
            ok = got >= need
            failures += not ok
            print(f"{page:<18} {label:<17} {got:>8.2f}:1 {need:>6}:1   "
                  f"{'pass' if ok else f'FAIL  lightest px {px}'}")

    print()
    if failures:
        print(f"{failures} contrast failure(s) — white text is not readable "
              f"against the photograph behind it.")
        sys.exit(1)
    print("All measured text clears WCAG 2.1 AA contrast against its photograph.")


if __name__ == "__main__":
    main()
