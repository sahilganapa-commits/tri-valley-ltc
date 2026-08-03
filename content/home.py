"""Home page.

The hero is the router, in the family's own words. Most people arriving here
are not browsing — they are somewhere specific in a hard process and need to
be pointed at one page, quickly.
"""

from layout import VERIFIED, cta, esc, page, record

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

    founders = """<div class="people">
<article class="person">
<h3 class="person__name">Dr. Sherry Hu</h3>
<p class="person__role">Co-founder &middot; Board of Directors</p>
<p class="person__bio">Dr. Sherry Hu is a retirement-planning professional, nonprofit founder,
community leader, and Mayor of Dublin, California. After seeing many families struggle to
understand and prepare for long-term care, she helped create this program to make reliable
information and local resources easier to access.</p>
</article>
<article class="person">
<h3 class="person__name">Dominic Scotto</h3>
<p class="person__role">Co-founder &middot; Board of Directors</p>
<p class="person__bio todo">Biography to be added before launch.</p>
</article>
</div>"""

    body = f"""<section class="hero">
<div class="shell">
<p class="eyebrow" data-reveal style="--i:0">A nonprofit community program &middot; Tri-Valley, California</p>
<h1 class="hero__title" data-reveal style="--i:1">Long-term care, explained for families.</h1>
<div class="hero__rule" role="presentation"></div>
<p class="lede hero__lede" data-reveal style="--i:2">Long-term care decisions arrive confusing,
stressful, and expensive — usually all at once. This is a plain-English guide to what care
costs, how it gets paid for, how to use a policy you already hold, and who provides care here
in the Tri-Valley.</p>
<p class="eyebrow" id="start" data-reveal style="--i:3;margin-top:2.75rem">Start where you are</p>
<div class="doors">{doors}</div>
</div>
</section>

<section class="band">
<div class="shell">
<div class="band__head">
<h2>What this program does</h2>
<p>We are a small nonprofit, not a business. Everything here is free, and nothing on this site
is trying to sell you anything.</p>
</div>
{program}
</div>
</section>

<section class="band band--card">
<div class="shell">
<div class="band__head">
<h2>Four things worth knowing before you start</h2>
<p>Families tell us these are the facts that would have changed their decisions if they had
known them a year earlier.</p>
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
<h2>Our founders</h2>
<p>This program was created by people who watched their own communities struggle with these
decisions.</p>
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
    )
