"""Home page.

The hero is the router, in the family's own words. Most people arriving here
are not browsing — they are somewhere specific in a hard process and need to
be pointed at one page, quickly.
"""

from layout import VERIFIED, asset_version, cta, esc, page, record

# One source of truth for the biographies, shared with the About us page.
from .about import people_cards

# Drop a licensed photograph at this path and it fills the hero. Until then
# the hero falls back to the brand gradient, which is why nothing looks broken.
HERO_IMAGE = "assets/hero.jpg"

DOORS = [
    ("We're noticing changes.",
     "A parent seems less steady, or less on top of things, and you are not sure whether it is time.",
     "getting-care.html#signs", "Start here"),
    ("We have a policy, and care is needed.",
     "There is long-term care insurance in the family. Find out what it covers and how to open a claim.",
     "using-coverage.html", "Using your coverage"),
    ("We're already paying for care.",
     "Care is underway. Keep benefits flowing, or work out how to fund the years ahead.",
     "paying-for-care.html", "Paying for care"),
    ("We need a name and a number.",
     "Assisted living, memory care, in-home caregivers, adult day programs across the Tri-Valley.",
     "directory.html", "Care directory"),
]


def build(directory, **_):
    doors = "".join(
        f'<a class="door" href="{href}" data-reveal style="--i:{i + 4}">'
        f'<p class="door__quote">&ldquo;{esc(quote)}&rdquo;</p>'
        f'<p class="door__body">{esc(body)}</p>'
        f'<span class="door__go">{esc(go)} &rarr;</span></a>'
        for i, (quote, body, href, go) in enumerate(DOORS)
    )

    core = ["Dublin", "Pleasanton", "Livermore", "San Ramon", "Danville"]

    program = record([
        ("Who we are",
         "A nonprofit community initiative for seniors, caregivers, and families in the Tri-Valley."),
        ("Cities served",
         " &middot; ".join(esc(c) for c in core) + ", and the surrounding East Bay."),
        ("In the directory",
         f'<span class="data">{len(directory)}</span> organizations and programs across '
         f'<span class="data">10</span> categories of care, verified {esc(VERIFIED)}.'),
        ("What it costs you",
         "Nothing. We do not sell insurance, care, or placement, and we are not paid by the "
         "providers listed in our directory."),
        ("What we are not",
         "We are not a substitute for your doctor, your attorney, your tax adviser, or your "
         "insurance carrier. We help you arrive at those conversations prepared."),
    ])

    founders = people_cards(heading_level=3)

    body = f"""<section class="hero hero--cover">
<img class="hero__img" src="{HERO_IMAGE}?v={asset_version('hero.jpg')}"
alt="An older woman and a younger woman lean close together outdoors, talking and smiling.">
<div class="shell hero__inner">
<h1 class="hero__headline" data-reveal style="--i:0">Plan Ahead, Protect What Matters</h1>
<p class="hero__sub" data-reveal style="--i:1">A trusted resource helping Tri-Valley seniors and
families understand long term care and find local support</p>
</div>
</section>

<section class="band band--card">
<div class="shell">
<p class="eyebrow" id="start">Start where you are</p>
<div class="doors" style="margin-top:1.25rem">{doors}</div>
</div>
</section>

<section class="band">
<div class="shell">
<div class="band__head">
<h2>What this program does</h2>
</div>
{program}
</div>
</section>

<section class="band band--card">
<div class="shell">
<div class="band__head">
<h2>Four things worth knowing before you start</h2>
</div>
<div class="grid grid--2">
<article class="card">
<h3 class="card__title">Medicare does not pay for most of it</h3>
<p>Medicare covers medically necessary acute care and limited skilled services. The ongoing,
non-medical help most families actually need — bathing, dressing, supervision — is generally
paid privately, by a qualifying insurance policy, or by Medi-Cal after eligibility rules are
met. <a href="getting-care.html#paying">How families pay for care</a></p>
</article>
<article class="card">
<h3 class="card__title">The odds are higher than people expect</h3>
<p>Someone turning 65 has almost a 70% chance of needing long-term services and supports at
some point. About one in five will need care for longer than five years.
<a href="paying-for-care.html#why">Why planning matters</a></p>
</article>
<article class="card">
<h3 class="card__title">A claim takes longer than a crisis allows</h3>
<p>Between claim paperwork, the carrier's assessment, and the waiting period written into the
policy, 60 to 90 days or more commonly pass before the first benefit payment arrives. Start
before it feels urgent. <a href="using-coverage-filing-a-claim.html">Filing a claim</a></p>
</article>
<article class="card">
<h3 class="card__title">Do not cancel an old policy without advice</h3>
<p>A carrier leaving the market does not cancel your policy. Older policies often contain
benefits — lifetime benefit periods, strong inflation riders — that cannot be bought at any
price today. <a href="using-coverage-carrier-landscape.html">The carrier landscape</a></p>
</article>
</div>
</div>
</section>

<section class="band">
<div class="shell">
<div class="band__head">
<h2>The people behind this program</h2>
<p>More about each of us on the <a href="about.html">About us</a> page.</p>
</div>
{founders}
</div>
</section>

{cta("Not sure where to start?",
     "Tell us where your family is in the process — understanding a policy, starting a claim, "
     "finding care, or planning ahead — and we will point you to the right place. No obligation, "
     "and never a sales call.")}"""

    return page(
        "index.html",
        "Tri-Valley Long Term Care",
        "A nonprofit community program helping Tri-Valley seniors and families understand "
        "long-term care options, use their coverage, plan for the cost, and find local providers.",
        body,
        overlay=True,
    )
