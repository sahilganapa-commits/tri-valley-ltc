"""Shared layout, tokens, and content components for the site build."""

import hashlib
import json
import re
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "site"
DATA = ROOT / "data"


@lru_cache(maxsize=None)
def asset_version(name):
    """Short content hash appended to asset URLs. A changed file gets a new
    URL, so a stale stylesheet can never be served from a browser cache."""
    try:
        return hashlib.sha256((ROOT / "assets" / name).read_bytes()).hexdigest()[:8]
    except OSError:
        return "dev"


SITE_NAME = "Tri-Valley Long Term Care"
TAGLINE = "Community Program"
VERIFIED = "July 27, 2026"

# Program contact details are not yet settled; these placeholders are meant to
# be obvious in review rather than to look finished.
PROGRAM_EMAIL = "hello@trivalleyltc.org"

# ---------------------------------------------------------------- navigation

NAV = [
    ("getting-care.html", "Getting care"),
    ("using-coverage.html", "Using your coverage"),
    ("paying-for-care.html", "Paying for care"),
    ("directory.html", "Care directory"),
    ("faq.html", "Questions"),
]

FOOTER_GUIDE = [
    ("getting-care.html", "Getting long-term care"),
    ("using-coverage.html", "Understanding and using your coverage"),
    ("paying-for-care.html", "Paying for care"),
    ("directory.html", "Tri-Valley care directory"),
]

FOOTER_MORE = [
    ("help.html", "Contact us"),
    ("faq.html", "Frequently asked questions"),
    ("white-paper.html", "2026 white paper"),
    ("privacy.html", "Privacy policy"),
    ("accessibility.html", "Accessibility"),
]

LOGO = """<svg class="brand__mark" viewBox="0 0 168 92" aria-hidden="true" focusable="false">
<defs><path id="h-{uid}" d="M50 88C50 88 8 60 8 34 8 18 20 8 32 8c8 0 15 4 18 12 3-8 10-12 18-12 12 0 26 10 26 26 0 26-42 54-42 54Z"/></defs>
<use href="#h-{uid}" transform="translate(70 0) scale(.95)" fill="#b9cff2"/>
<use href="#h-{uid}" transform="translate(35 9) scale(.82)" fill="#5c7fc0"/>
<use href="#h-{uid}" transform="translate(0 20) scale(.7)" fill="#26295b"/>
</svg>"""

FAVICON = (
    "data:image/svg+xml,"
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 168 92'%3E"
    "%3Cdefs%3E%3Cpath id='h' d='M50 88C50 88 8 60 8 34 8 18 20 8 32 8c8 0 15 4 18 12 3-8 "
    "10-12 18-12 12 0 26 10 26 26 0 26-42 54-42 54Z'/%3E%3C/defs%3E"
    "%3Cuse href='%23h' transform='translate(70 0) scale(.95)' fill='%23b9cff2'/%3E"
    "%3Cuse href='%23h' transform='translate(35 9) scale(.82)' fill='%235c7fc0'/%3E"
    "%3Cuse href='%23h' transform='translate(0 20) scale(.7)' fill='%2326295b'/%3E%3C/svg%3E"
)

DISCLAIMER = (
    "This website provides general educational information and does not provide legal, tax, "
    "medical, investment, insurance, or care-management advice. Program information, "
    "public-benefit rules, tax treatment, insurance products, costs, and availability may "
    "change. Visitors should consult appropriately licensed professionals regarding their "
    "individual circumstances."
)

DIRECTORY_DISCLAIMER = (
    "The care directory is informational only and does not constitute an endorsement or "
    "recommendation. Listings were compiled from public sources and verified " + VERIFIED +
    ". Confirm licensing, availability, pricing, and current inspection records directly "
    "with each provider before making a decision."
)


# ------------------------------------------------------------------ helpers

def esc(text):
    return (str(text).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")


def nav_html(current):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        items.append(f'<li><a class="nav__link" href="{href}"{cur}>{esc(label)}</a></li>')
    cur_help = ' aria-current="page"' if current == "help.html" else ""
    return (
        '<nav class="nav" id="sitenav" data-nav data-open="false" aria-label="Main">'
        '<ul class="nav__list">' + "".join(items) +
        f'<li><a class="nav__cta" href="help.html"{cur_help}>Contact us</a></li>'
        "</ul></nav>"
    )


def header_html(current, overlay=False):
    """`overlay` lifts the header onto the hero photograph. The bar carries its
    own gradient and white type, so it stays legible over any picture without
    per-page tuning."""
    cls = "masthead masthead--overlay" if overlay else "masthead"
    attr = " data-masthead" if overlay else ""
    return f"""<header class="{cls}"{attr}>
<div class="shell masthead__bar">
<a class="brand" href="index.html">{LOGO.format(uid='hdr')}
<span><span class="brand__name">Tri-Valley Long Term Care</span><span class="brand__sub">{esc(TAGLINE)}</span></span>
</a>
<button class="navtoggle" type="button" data-navtoggle hidden aria-expanded="false" aria-controls="sitenav">Menu</button>
{nav_html(current)}
</div>
</header>"""


def footer_html():
    guide = "".join(f'<li><a href="{h}">{esc(t)}</a></li>' for h, t in FOOTER_GUIDE)
    more = "".join(f'<li><a href="{h}">{esc(t)}</a></li>' for h, t in FOOTER_MORE)
    return f"""<footer class="footer">
<div class="shell">
<div class="footer__cols">
<div>
<p class="footer__brand">Tri-Valley Long Term Care</p>
<p>A nonprofit community program serving Dublin, Pleasanton, Livermore, San&nbsp;Ramon, Danville, and the surrounding East&nbsp;Bay.</p>
<p><a href="help.html">Ask us a question</a></p>
</div>
<div>
<p class="footer__title">The guide</p>
<ul class="footer__list">{guide}</ul>
</div>
<div>
<p class="footer__title">More</p>
<ul class="footer__list">{more}</ul>
</div>
</div>
<div class="footer__legal">
<p>{esc(DISCLAIMER)}</p>
<p>The Tri-Valley Long Term Care Resource Program provides general education and referrals.
Any professional a visitor is referred to operates a separate business. A referral does not
require the visitor to purchase a product or engage a particular professional. Advisory fees,
insurance commissions, affiliations, and compensation arrangements are disclosed before
services are provided.</p>
<p>&copy; 2026 Tri-Valley Long Term Care Community Program. Content reviewed {esc(VERIFIED)}.</p>
</div>
</div>
</footer>"""


COOKIE = """<div class="cookie" data-cookie hidden role="region" aria-label="Cookie notice">
<div class="shell cookie__inner">
<p class="cookie__text">We store your cookie choice and any checklists you fill in on your
own device. Nothing is sent to us. <a href="privacy.html">Privacy policy</a>.</p>
<div class="cookie__actions">
<button class="btn btn--primary btn--small" type="button" data-cookie-choice="accepted">Accept</button>
<button class="btn btn--ghost btn--small" type="button" data-cookie-choice="declined">Decline</button>
</div>
</div>
</div>"""


def page(filename, title, description, body, current=None, overlay=False):
    """Wrap a page body in the shared shell and write it to site/."""
    current = current or filename
    full_title = title if title == SITE_NAME else f"{title} — {SITE_NAME}"
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=Poppins:wght@500;600;700&family=Public+Sans:wght@400;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="assets/styles.css?v={asset_version("styles.css")}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{header_html(current, overlay)}
<main id="main">
{body}
</main>
{footer_html()}
{COOKIE}
<script src="assets/site.js?v={asset_version("site.js")}"></script>
</body>
</html>
"""
    (OUT / filename).write_text(html, encoding="utf-8")
    return filename


# ------------------------------------------------------- content components

def pagehead(eyebrow, title, lede, extra=""):
    eb = f'<p class="eyebrow">{esc(eyebrow)}</p>' if eyebrow else ""
    ld = f'<p class="lede">{lede}</p>' if lede else ""
    return f"""<section class="pagehead">
<div class="shell">
{eb}<h1 class="pagehead__title">{esc(title)}</h1>
{ld}{extra}
</div>
</section>"""


def record(rows, dark=False):
    out = ['<dl class="record">']
    for label, value in rows:
        out.append(
            '<div class="record__row">'
            f'<dt class="record__label">{esc(label)}</dt>'
            f'<dd class="record__value">{value}</dd>'
            "</div>"
        )
    out.append("</dl>")
    return "".join(out)



def hero_page(name, alt, title, lede, focus="center 45%"):
    """Full-screen photographic header for an interior page — same treatment as
    the home page. The picture fills the viewport, the nav rides on top of it,
    and the page title sits over the bottom."""
    return f"""<section class="hero hero--cover hero--page">
<img class="hero__img" src="assets/{name}?v={asset_version(name)}" alt="{esc(alt)}"
style="object-position:{focus}">
<div class="shell hero__inner">
<h1 class="hero__headline">{esc(title)}</h1>
<p class="hero__sub">{lede}</p>
</div>
</section>"""



def faq_list(items, open_first=False):
    """Tap-to-expand questions. Built on <details>/<summary>, so it works with
    no JavaScript, is keyboard operable, and screen readers announce the
    expanded state for free."""
    out = ['<div class="faq">']
    for i, (question, answer) in enumerate(items):
        is_open = " open" if (open_first and i == 0) else ""
        out.append(
            f'<details class="faq__item"{is_open}>'
            f'<summary class="faq__q">{esc(question)}</summary>'
            f'<div class="faq__a">{answer}</div>'
            "</details>"
        )
    out.append("</div>")
    return "".join(out)


def note(title, body, kind=""):
    cls = "note" + (f" note--{kind}" if kind else "")
    t = f'<p class="note__title">{esc(title)}</p>' if title else ""
    return f'<aside class="{cls}">{t}{body}</aside>'


def table(headers, rows, caption="", first_col_header=True):
    head = "".join(f'<th scope="col">{esc(h)}</th>' for h in headers)
    body = []
    for row in rows:
        cells = []
        for i, cell in enumerate(row):
            if i == 0 and first_col_header:
                cells.append(f'<th scope="row">{cell}</th>')
            else:
                num = " class=\"num\"" if re.fullmatch(r"[$\d][\d,.$%–— a-z/]*", str(cell)) else ""
                cells.append(f"<td{num}>{cell}</td>")
        body.append("<tr>" + "".join(cells) + "</tr>")
    cap = f"<caption>{caption}</caption>" if caption else ""
    return (
        '<div class="tablewrap"><table class="table">' + cap +
        f"<thead><tr>{head}</tr></thead><tbody>" + "".join(body) +
        "</tbody></table></div>"
    )


def ul(items, plain=False):
    cls = "list list--plain" if plain else "list"
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def steps(items):
    out = ['<ol class="steps">']
    for title, body in items:
        out.append(f'<li class="step"><h3 class="step__title">{esc(title)}</h3>{body}</li>')
    out.append("</ol>")
    return "".join(out)


def checklist(cid, title, intro, items, trigger=None, rest_text="", trigger_text=""):
    """A checklist that remembers what you ticked. `items` are (bold, hint)."""
    lis = []
    for i, (bold, hint) in enumerate(items):
        iid = f"{cid}-{i}"
        hint_html = f'<span class="check__hint">{hint}</span>' if hint else ""
        lis.append(
            f'<li class="check__item"><label class="check__label" for="{iid}">'
            f'<input class="check__box" type="checkbox" id="{iid}">'
            f'<span class="check__text"><b>{bold}</b>{hint_html}</span>'
            "</label></li>"
        )
    attrs = f' data-trigger="{trigger}" data-trigger-text="{esc(trigger_text)}"' if trigger else ""
    tally = ""
    if trigger:
        tally = (
            '<div class="check__tally" data-tally hidden>'
            f'<p><span class="check__count" data-count>0 of {len(items)}</span> checked.</p>'
            f'<p class="check__verdict" data-verdict data-triggered="false">{rest_text}</p>'
            "</div>"
        )
    return f"""<div class="check" data-check{attrs}>
<div class="check__head"><h3 class="check__title">{esc(title)}</h3></div>
{intro}
<ul class="check__items">{"".join(lis)}</ul>
{tally}
<div class="check__actions">
<button class="btn btn--ghost btn--small" type="button" data-print hidden>Print this checklist</button>
<button class="btn btn--ghost btn--small" type="button" data-clear hidden>Clear</button>
</div>
</div>"""


def rail(title, links, current):
    items = []
    for href, label in links:
        cur = ' aria-current="page"' if href == current else ""
        items.append(f'<li class="rail__item"><a class="rail__link" href="{href}"{cur}>{esc(label)}</a></li>')
    return (
        f'<aside class="rail" aria-label="{esc(title)}">'
        f'<p class="rail__title">{esc(title)}</p>'
        f'<ul class="rail__list">{"".join(items)}</ul>'
        '<a class="btn btn--ghost btn--small" href="help.html">Ask us a question</a>'
        "</aside>"
    )


def seq(prev=None, nxt=None):
    parts = []
    if prev:
        parts.append(
            f'<a class="seq__link" href="{prev[0]}"><span class="seq__dir">&larr; Previous</span>'
            f'<span class="seq__name">{esc(prev[1])}</span></a>'
        )
    else:
        parts.append("<div></div>")
    if nxt:
        parts.append(
            f'<a class="seq__link seq__link--next" href="{nxt[0]}"><span class="seq__dir">Next &rarr;</span>'
            f'<span class="seq__name">{esc(nxt[1])}</span></a>'
        )
    return f'<nav class="seq" aria-label="Guide sections">{"".join(parts)}</nav>'


def cta(heading, body, label="Contact us", href="help.html"):
    return f"""<section class="band band--navy">
<div class="shell cta">
<div class="cta__text"><h2>{esc(heading)}</h2><p>{esc(body)}</p></div>
<a class="btn btn--light" href="{href}">{esc(label)}</a>
</div>
</section>"""


def article(eyebrow, title, lede, rail_html, prose, prev=None, nxt=None):
    """Standard guide-section page: sticky rail plus a measured column."""
    return pagehead(eyebrow, title, lede) + f"""<section class="band">
<div class="shell layout">
{rail_html}
<div class="prose">
{prose}
{seq(prev, nxt)}
</div>
</div>
</section>"""


