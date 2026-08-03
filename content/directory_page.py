"""Tri-Valley care directory.

Every listing is rendered into the HTML, so the full directory is readable
with JavaScript disabled or when printed. Search and filters only hide rows.
"""

from layout import (DIRECTORY_DISCLAIMER, VERIFIED, esc, note, page, pagehead,
                    record, slug, table, ul)

CORE_CITIES = ["Dublin", "Pleasanton", "Livermore", "San Ramon", "Danville"]

CATEGORY_ORDER = [
    "In-home care",
    "Adult day programs",
    "PACE programs",
    "Assisted living",
    "Memory care",
    "Independent senior living",
    "Skilled nursing and rehabilitation",
    "Hospice and palliative care",
    "Care-management services",
    "Senior placement and referral services",
]


def _city_key(raw):
    """Listings serve overlapping areas; file each under its first named city."""
    head = raw.split("/")[0].split(";")[0].split(",")[0].strip()
    for city in CORE_CITIES:
        if city.lower() in raw.lower():
            return city
    return head


def _contact(rec):
    bits = []
    if rec["address"]:
        bits.append(esc(rec["address"]))
    for part in [p.strip() for p in rec["phone"].split(";") if p.strip()]:
        if "@" in part:
            bits.append(f'<a href="mailto:{esc(part)}">{esc(part)}</a>')
        else:
            digits = "".join(c for c in part if c.isdigit() or c == "+")
            label = f'<span class="data">{esc(part)}</span>'
            bits.append(f'<a href="tel:{digits}">{label}</a>' if len(digits) >= 10 else label)
    if rec["website"]:
        host = rec["website"].split("//")[-1].rstrip("/")
        bits.append(f'<a href="{esc(rec["website"])}">{esc(host)}</a>')
    return "<br>".join(bits)


def _listing(rec):
    cats = "|" + "|".join(slug(c) for c in rec["all_categories"]) + "|"
    city = _city_key(rec["city"])
    haystack = " ".join([
        rec["name"], rec["city"], rec["levels"], rec["services"],
        " ".join(rec["all_categories"]), rec["payment"],
    ]).lower()

    detail = record([
        ("Levels of care", f'<p>{esc(rec["levels"])}</p>'),
        ("Pricing", f'<p>{esc(rec["pricing"])}</p>'),
        ("Payment options", f'<p>{esc(rec["payment"])}</p>'),
        ("Languages and access", f'<p>{esc(rec["languages"])}</p>'),
        ("Quality indicators", f'<p>{esc(rec["quality"])}</p>'),
        ("Ask them", f'<p>{esc(rec["questions"])}</p>'),
        ("Sources", '<p class="listing__sources">' + "<br>".join(
            f'<a href="{esc(u)}">{esc(u)}</a>' for u in rec["sources"]) +
         f'<br>Verified {esc(rec["verified"])}</p>'),
    ])

    return f"""<article class="listing" data-listing data-cats="{esc(cats)}" data-city="{esc(city)}" data-text="{esc(haystack)}">
<div class="listing__top">
<h3 class="listing__name">{esc(rec["name"])}</h3>
<span class="listing__city">{esc(rec["city"])}</span>
</div>
<span class="listing__cat">{esc(rec["primary_category"])}</span>
<p class="listing__summary">{esc(rec["services"])}</p>
<p class="listing__contact">{_contact(rec)}</p>
<details class="listing__more">
<summary>Pricing, payment, quality, and what to ask</summary>
{detail}
</details>
</article>"""


def build(directory, questions, regulatory, **_):
    counts = {}
    for rec in directory:
        for cat in rec["all_categories"]:
            counts[cat] = counts.get(cat, 0) + 1

    chips = "".join(
        f'<button class="chip" type="button" data-chip="{slug(cat)}" aria-pressed="false">'
        f'{esc(cat)}<span class="chip__n">{counts.get(cat, 0)}</span></button>'
        for cat in CATEGORY_ORDER if counts.get(cat)
    )

    cities = sorted({_city_key(r["city"]) for r in directory})
    options = "".join(f'<option value="{esc(c)}">{esc(c)}</option>' for c in cities)

    order = {c: i for i, c in enumerate(CATEGORY_ORDER)}
    listings = "".join(
        _listing(r) for r in sorted(
            directory, key=lambda r: (order.get(r["primary_category"], 99), r["name"])
        )
    )

    # Family interview questions, minus the five universal requests at the end.
    qrows = [q for q in questions if not q["care_type"].isdigit()]
    qtable = table(
        ["Care type", "Costs and contract", "Care, staffing, and safety", "Quality and fit"],
        [[esc(q["care_type"]), esc(q["costs"]), esc(q["care"]), esc(q["quality"])] for q in qrows],
        caption="What to ask before you tour, and what to ask while you are there.",
    )

    reg = table(
        ["Resource", "Use it for", "What to check"],
        [[f'<a href="{esc(r["url"])}">{esc(r["resource"])}</a>', esc(r["use"]), esc(r["check"])]
         for r in regulatory],
        caption="Check licensing, inspections, complaints, and ratings yourself — every one of "
                "these is free and public.",
    )

    body = pagehead(
        "Part four of the guide",
        "Tri-Valley care directory",
        f"{len(directory)} organizations and programs across {len(CATEGORY_ORDER)} categories of "
        "care in Dublin, Pleasanton, Livermore, San&nbsp;Ramon, Danville, and the surrounding "
        f"East&nbsp;Bay. Compiled from public sources and verified {esc(VERIFIED)}.",
    ) + f"""<section class="band" data-directory>
<div class="shell">

{note("This directory is informational only", f"<p>{esc(DIRECTORY_DISCLAIMER)}</p>", "plain")}

<div class="filters">
<div class="filters__row">
<label class="field">
<span class="field__label">Search by name, service, or care type</span>
<input class="field__input" type="search" data-search placeholder="memory care, dementia, hourly&hellip;" autocomplete="off">
</label>
<label class="field">
<span class="field__label">City</span>
<select class="field__input" data-city>
<option value="">All cities</option>
{options}
</select>
</label>
</div>
<div class="chips" role="group" aria-label="Filter by care type">{chips}</div>
</div>

<p class="results">Showing <b data-count-results>{len(directory)}</b> of {len(directory)} listings.
<button class="btn btn--ghost btn--small" type="button" data-reset>Clear filters</button></p>

<div class="listings">{listings}</div>

<p class="empty" data-empty hidden>No listings match those filters. Try clearing the search box,
or <a href="help.html">ask us</a> — we keep track of providers that are not yet listed here.</p>
</div>
</section>

<section class="band band--card">
<div class="shell">
<div class="band__head">
<h2>What to ask before you choose</h2>
<p>Bring the relevant questions to every call and every tour, and request the answers in writing.</p>
</div>
{qtable}
{note("Five requests to make in writing, of any provider",
      ul([
        "An itemised all-in price estimate based on the senior&rsquo;s current needs.",
        "The most recent license, inspection, complaint, deficiency, and correction reports.",
        "A sample contract, admission agreement, discharge policy, and rate-increase history.",
        "Staffing by shift, nurse availability, turnover, call-response expectations, and backup plan.",
        "A written explanation of what the provider cannot safely do, and what triggers transfer "
        "or discharge.",
      ]))}
</div>
</section>

<section class="band">
<div class="shell">
<div class="band__head">
<h2>Check the public record yourself</h2>
<p>Published prices and ratings are snapshots. These sources are current, free, and independent
of any provider.</p>
</div>
{reg}
{note("A note on referral and placement services",
      "<p>A senior placement or referral service may be free to your family because the facility "
      "pays the referral fee. That is a legitimate business model, and it also means the service "
      "has a financial interest in where you land. Ask for written compensation and conflict "
      "disclosures, and ask whether facilities that do not pay referral fees are shown to you at "
      "all.</p>")}
</div>
</section>"""

    return page(
        "directory.html",
        "Tri-Valley care directory",
        "Assisted living, memory care, in-home care, adult day programs, skilled nursing, "
        "hospice, and care management across Dublin, Pleasanton, Livermore, San Ramon, and Danville.",
        body,
    )
