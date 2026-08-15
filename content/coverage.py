"""Understanding and Using Your Coverage — hub plus six guide sections.

This follows the sequence in the approved mockups: notice the need, read the
policy, file, choose a provider, stay on claim, understand the carrier.
Numbering is used here because the order genuinely matters — each step
depends on the one before it.
"""

from layout import (article, hero_page, cta, esc, note, page, pagehead,
                    rail, record, steps, table, ul)

HUB = "using-coverage.html"

SECTIONS = [
    ("using-coverage-do-we-need-help.html", "Do we need help — and what kind?",
     "The signs it may be time, and how care needs are measured through the daily activities."),
    ("using-coverage-know-your-policy.html", "Before you need it: know your policy",
     "The five things to find in the contract, and who actually services it today."),
    ("using-coverage-filing-a-claim.html", "Filing a claim",
     "Four steps from the first phone call to the first benefit payment — and what to do if it is denied."),
    ("using-coverage-approved-providers.html", "Approved providers: your care options",
     "What policies typically cover, how benefits are paid, and what to ask any home care provider."),
    ("using-coverage-staying-on-claim.html", "Staying on claim",
     "The monthly routine that keeps benefits flowing, and what to do when they stall."),
    ("using-coverage-carrier-landscape.html", "The carrier and program landscape",
     "Why your carrier stopped selling policies, and why that does not affect your claim."),
]

RAIL_LINKS = [(href, title) for href, title, _ in SECTIONS]


def _rail(current):
    return rail("In this guide", RAIL_LINKS, current)


def _eyebrow(n):
    return f"Using your coverage · Section {n} of 6"


def _prev_next(i):
    prev = (SECTIONS[i - 1][0], SECTIONS[i - 1][1]) if i > 0 else None
    nxt = (SECTIONS[i + 1][0], SECTIONS[i + 1][1]) if i < len(SECTIONS) - 1 else (HUB, "Back to the guide")
    return prev, nxt


# ------------------------------------------------------------------- the hub

def _hub():
    cards = "".join(
        f'<a class="door" href="{href}">'
        f'<p class="door__quote">{esc(title)}</p>'
        f'<p class="door__body">{esc(blurb)}</p>'
        f'<span class="door__go">Section {i + 1} &rarr;</span></a>'
        for i, (href, title, blurb) in enumerate(SECTIONS)
    )
    body = hero_page("using-coverage.jpg",
                   "An older couple sit close together on a weathered bench, looking out over the sea.",
                   "Understanding and using your coverage",
                   "Six sections, from recognizing the need through filing a claim and keeping benefits flowing.",
                   "center 45%") + f"""<section class="band">
<div class="shell">
{note("If there is no policy in the family",
      "<p>Most of this still applies — particularly Sections 1 and 4, which are about recognizing "
      "care needs and comparing providers regardless of who pays. For funding without insurance, "
      "start with <a href=\"paying-for-care.html\">Paying for care</a>.</p>", "info")}
<div class="doors" style="grid-template-columns:1fr">{cards}</div>
</div>
</section>

<section class="band band--card">
<div class="shell">
<div class="band__head"><h2>The shortest possible version</h2></div>
{record([
    ("Find the contract",
     "<p>Not the annual statement — the full policy, riders, and amendments. You are entitled to a "
     "copy from the carrier if you cannot find it.</p>"),
    ("Start early",
     "<p>Sixty to ninety days or more commonly pass between the first phone call and the first "
     "benefit payment. You can open a claim before choosing a provider.</p>"),
    ("Get provider rules in writing",
     "<p>Care from a provider your policy does not recognize is generally not reimbursable, even "
     "when the care was exactly right.</p>"),
    ("Keep records from day one",
     "<p>Including during the waiting period. Most interrupted claims are caused by paperwork, not "
     "by health.</p>"),
    ("Claim the premium waiver",
     "<p>Most policies stop charging premiums while you are on claim — but it usually has to be "
     "requested rather than happening automatically.</p>"),
])}
</div>
</section>

{cta("Reading a policy and not sure what you are looking at?",
     "Send us the questions you are stuck on. We will help you work out what to ask your carrier, "
     "and what to get in writing.")}"""

    return page(
        HUB,
        "Understanding and using your coverage",
        "A six-part guide for families using a long-term care insurance policy: recognizing the "
        "need, reading the policy, filing a claim, choosing approved providers, and staying on claim.",
        body,
        overlay=True,
    )


# ------------------------------------------------------------ section pages

def _section_1():
    prev, nxt = _prev_next(0)
    prose = f"""<h2>Signs it may be time</h2>
<p>No single sign means it is time for care. But if you are seeing several of these, it is worth
taking a closer look:</p>
{ul([
    "Missed medications, unpaid bills, or an empty refrigerator",
    "A fall — or a new fear of falling",
    "Changes in hygiene, memory, or how the house is kept",
    "A spouse or family caregiver who is exhausted, isolated, or unwell themselves",
])}
<p>That last one matters as much as the others. Caregiver burnout is one of the most common
reasons families seek help — and one of the best reasons to.</p>

<h2>The daily activities check</h2>
<p>Care professionals, doctors, and insurance companies all measure care needs the same way:
through six basic activities of daily living. Go through them honestly — not &ldquo;can they do
it on a good day,&rdquo; but &ldquo;can they do it safely and reliably, every day, without
help.&rdquo;</p>
{record([
    ("Bathing",
     "<p>Getting in and out of the tub or shower safely, washing thoroughly. Needing help looks "
     "like: skipping baths out of fear of falling, needing someone nearby &ldquo;just in "
     "case,&rdquo; or no longer washing hair or hard-to-reach areas.</p>"),
    ("Dressing",
     "<p>Choosing appropriate clothes and putting them on, including buttons, zippers, and shoes. "
     "Needing help looks like: wearing the same clothes repeatedly, clothes on inside out, or "
     "giving up on anything with fasteners.</p>"),
    ("Toileting",
     "<p>Getting to and from the toilet and managing hygiene afterward. Needing help looks like: "
     "accidents because the bathroom is too far, nighttime difficulties, or avoiding fluids to "
     "avoid trips to the bathroom.</p>"),
    ("Transferring",
     "<p>Moving safely between bed, chair, and standing. Needing help looks like: struggling to "
     "rise from a chair, needing to be pulled up, or staying in one place most of the day because "
     "moving feels risky.</p>"),
    ("Eating",
     "<p>Feeding oneself once food is prepared. Needing help looks like: difficulty using utensils, "
     "trouble swallowing, or meals left mostly uneaten. Trouble <em>preparing</em> meals matters "
     "too — it is one of the most common early needs, even when eating itself is fine.</p>"),
    ("Continence",
     "<p>Bladder and bowel control. Needing help looks like: accidents, hiding soiled clothing, or "
     "withdrawing from activities out of embarrassment.</p>"),
    ("Supervision",
     "<p>Not on the standard list. Some people can physically do all six activities but cannot "
     "safely be alone — because of memory loss, confusion, wandering, or leaving the stove on. "
     "Needing supervision due to cognitive changes is a care need in its own right, and care "
     "providers and long-term care insurance treat it as one.</p>"),
])}
{note("Seeing needs on this list?",
      "<p>In-home care — a caregiver coming to the home, from a few hours a week to around the "
      "clock — is where most families start, and many never need more. If there is a long-term "
      "care insurance policy in the family, needing help with two or more of these activities, or "
      "needing supervision, is typically what makes it pay. Keep your honest answers and continue "
      "to <a href=\"using-coverage-know-your-policy.html\">Section 2</a>.</p>")}"""

    body = article(_eyebrow(1), "Do we need help — and what kind?",
                   "Start here: the signs it may be time, and how care needs are measured.",
                   _rail(SECTIONS[0][0]), prose, prev, nxt)
    return page(SECTIONS[0][0], SECTIONS[0][1],
                "How to recognize when an older adult needs help, and how care needs are measured "
                "through the six activities of daily living.",
                body, current=HUB)


def _section_2():
    prev, nxt = _prev_next(1)
    prose = f"""<h2>Locate the policy, and who services it today</h2>
<p>Find the full policy contract — not the annual statement — including any riders and
amendments. If you cannot find it, request a copy from the carrier; you are entitled to one.
Then confirm who administers the policy now: many policies sold in the 1990s and 2000s are
serviced by a different company than the one on the letterhead, and the customer service number
on your most recent premium statement is usually the right starting point. A carrier leaving the
sales market does not cancel your policy — claims on existing policies are still paid.</p>

<h2>Find these five things in your policy</h2>

<h3>The benefit trigger</h3>
<p>Most policies pay when a licensed health practitioner certifies that you need substantial
assistance with at least <strong>two of six activities of daily living</strong> — bathing,
dressing, toileting, transferring, eating, continence — or that you need supervision due to
cognitive impairment such as dementia. For tax-qualified policies, which is most policies sold
after 1996, the condition must be expected to last at least 90 days. These are the same six
activities from <a href="using-coverage-do-we-need-help.html">the daily activities check in
Section 1</a>.</p>

<h3>The elimination period</h3>
<p>This is the waiting period — commonly 30, 60, 90, or 100 days — before benefits begin.
Critically, check whether your policy counts <strong>calendar days</strong> or
<strong>service days</strong>.</p>
{note("Why this one question can cost you months",
      "<p>Under a service-day elimination period, only days on which you actually receive — and "
      "often pay for — covered care count toward the waiting period. A family receiving care three "
      "days a week under a 90-service-day elimination period will wait 30 weeks before benefits "
      "begin, not 90 calendar days. Some policies count one service day as a full week; read "
      "yours.</p>")}

<h3>The benefit amount</h3>
<p>Your daily or monthly maximum. If your policy includes an inflation protection rider, the
current benefit may be substantially higher than the number printed on the original policy.
Check your most recent annual statement for today&rsquo;s figure, and use that figure in your
planning.</p>

<h3>The benefit period or benefit pool</h3>
<p>Some policies pay for a set period, for example three years. Most modern policies define a
total pool of money that lasts as long as it lasts. If you spend less than the daily maximum,
the pool stretches longer — an important fact when comparing care options in
<a href="using-coverage-approved-providers.html">Section 4</a>.</p>

<h3>The covered provider definitions</h3>
<p>This is the section families most often skip, and the one that determines everything about
how you can use your benefits. Policies differ significantly in which caregivers and settings
qualify. It gets its own section:
<a href="using-coverage-approved-providers.html">Approved providers</a>.</p>
"""

    body = article(_eyebrow(2), "Before you need it: know your policy",
                   "The most common mistake families make is opening the policy for the first "
                   "time in the middle of a crisis.",
                   _rail(SECTIONS[1][0]), prose, prev, nxt)
    return page(SECTIONS[1][0], SECTIONS[1][1],
                "How to read a long-term care insurance policy: the benefit trigger, elimination "
                "period, benefit amount, benefit pool, and covered provider definitions.",
                body, current=HUB)


def _section_3():
    prev, nxt = _prev_next(2)
    prose = f"""{steps(level=2, items=[
    ("Start early — request the claim packet",
     "<p>It is common for 60 to 90 days or more to pass between the first phone call and the first "
     "benefit payment, so contact the carrier promptly — <strong>you can begin a claim before "
     "choosing a care provider</strong>. Call the claims number for your carrier or its "
     "administrator, ask for the full claim packet, and ask these questions while you have them on "
     "the phone. Take notes, and get names.</p>" + ul([
        "What documentation do you require from the physician?",
        "Does my elimination period count calendar days or service days?",
        "What are your provider eligibility requirements for home care? "
        "(<a href=\"using-coverage-approved-providers.html\">Section 4</a> — get the answer "
        "<strong>in writing</strong>.)",
        "Do you require invoices, caregiver notes, or timesheets, and on what schedule?",
        "Is my premium waived while I am on claim?",
     ])),
    ("The physician’s certification and plan of care",
     "<p>Benefits require certification from a licensed health practitioner that the benefit trigger "
     "has been met, along with a plan of care describing the services needed. Your parent&rsquo;s "
     "primary care physician can usually provide this.</p>"),
    ("Provider approval",
     "<p>The carrier also confirms that your chosen care arrangement qualifies under the "
     "policy&rsquo;s provider definitions (see "
     "<a href=\"using-coverage-approved-providers.html\">Section 4</a>). Submit the "
     "provider&rsquo;s information as early as possible, ideally with the initial claim packet. In "
     "practice the carrier&rsquo;s decision rests on two pillars: the physician&rsquo;s "
     "certification of the benefit trigger, and approval of the provider.</p>"),
    ("Decision, the elimination period, and record-keeping",
     "<p>Once approved, the elimination period clock runs according to your policy&rsquo;s rules. "
     "Keep every invoice and record of care <strong>from day one</strong> — even during the "
     "elimination period — because carriers typically require proof of qualifying care during that "
     "window, and those records establish your service days.</p>"),
])}

<h2>If the claim is denied</h2>
<p>You have the right to appeal, and denials are frequently overturned when families supply
better documentation — a more detailed physician statement, a fuller picture of the daily
activities where help is needed. Request the denial reason in writing, respond to it
specifically, and consider involving a care manager or elder law attorney for a contested
claim.</p>
{record([
    ("California Department of Insurance",
     "<p>Regulates long-term care insurance and assists consumers with claim disputes.<br>"
     "<a href=\"https://www.insurance.ca.gov/\">insurance.ca.gov</a> &middot; "
     "<span class=\"data\">1-800-927-4357</span></p>"),
])}"""

    body = article(_eyebrow(3), "Filing a claim",
                   "Four steps from the first phone call to the first benefit payment — and "
                   "what to do if the claim is denied.",
                   _rail(SECTIONS[2][0]), prose, prev, nxt)
    return page(SECTIONS[2][0], SECTIONS[2][1],
                "How to file a long-term care insurance claim: requesting the claim packet, the "
                "physician's certification and plan of care, provider approval, and appealing a denial.",
                body, current=HUB)


def _section_4():
    prev, nxt = _prev_next(3)
    prose = f"""<h2>What policies typically cover</h2>
<p>Most comprehensive policies cover care across several settings:</p>
{ul([
    "Home care",
    "Adult day programs",
    "Assisted living and residential care facilities (RCFEs)",
    "Memory care",
    "Skilled nursing facilities",
    "Hospice care",
])}
<p>For facility options across the Tri-Valley, see the
<a href="directory.html">care directory</a>.</p>

<h2>How benefits are paid: reimbursement, indemnity, and cash</h2>
<p>Before comparing providers, understand how your policy pays — it shapes your cash flow
throughout the claim.</p>
{record([
    ("Reimbursement",
     "<p>Most policies. The family pays the provider first, submits invoices, and the carrier "
     "reimburses covered costs up to the daily or monthly maximum. Some carriers can send payments "
     "directly to the provider.</p>"),
    ("Indemnity",
     "<p>Less common. Pays the full daily benefit whenever qualified care is received, regardless of "
     "the actual cost of care that day.</p>"),
    ("Cash benefit",
     "<p>Found mainly in newer hybrid products. Pays the monthly benefit once the benefit trigger is "
     "met, with no receipts required, giving families total flexibility in how care is "
     "arranged.</p>"),
])}
{note("Know the payment timing",
      "<p>Under reimbursement, you pay the provider during the elimination period — those costs are "
      "not reimbursed — and then carry a typical 30 to 60 day gap between paying and being "
      "reimbursed. That is normal, not a problem with your claim. For planning around cash flow, "
      "see <a href=\"paying-for-care.html\">Paying for care</a>.</p>")}

<h2>Questions to ask any home care provider</h2>
{ul([
    "How are caregivers screened? Background checks, registry verification, reference checks, "
    "skills evaluation?",
    "Will my insurance carrier accept your documentation? Have you billed long-term care "
    "insurance before?",
    "What happens if the caregiver is sick or quits? How quickly is a replacement available?",
    "Can I interview and choose the caregiver? Can I request a change?",
    "What is the total hourly cost, and what does it include? Are there minimums, per shift or "
    "per week?",
    "Who supervises care quality, and how often is the care plan reviewed?",
])}"""

    body = article(_eyebrow(4), "Approved providers: your care options",
                   "Care received from a non-qualifying provider is generally not reimbursable "
                   "— even if the care itself was exactly what was needed.",
                   _rail(SECTIONS[3][0]), prose, prev, nxt)
    return page(SECTIONS[3][0], SECTIONS[3][1],
                "What long-term care policies typically cover, how reimbursement, indemnity, and "
                "cash benefits differ, and what to ask any home care provider.",
                body, current=HUB)


def _section_5():
    prev, nxt = _prev_next(4)
    prose = f"""<h2>The monthly claim routine</h2>
{record([
    ("Submit on schedule",
     "<p>Send invoices and required documentation on the carrier&rsquo;s schedule, typically "
     "monthly. Reimbursement policies pay against receipts; late or incomplete submissions delay "
     "payment and, if they pile up, can trigger a claim review.</p>"),
    ("Keep caregiver documentation",
     "<p>Most carriers require care notes or timesheets showing dates, hours, and services "
     "performed, signed by the caregiver. Establish a simple daily log from the first shift — a "
     "spiral notebook by the door works; consistency matters more than format.</p>"),
    ("Match documentation to the plan of care",
     "<p>If the plan of care says assistance with bathing, dressing, and meal preparation, the care "
     "logs should reflect those services. If needs have changed, update the plan of care rather "
     "than letting the paperwork drift out of sync.</p>"),
])}

<h2>Expect recertification</h2>
<p>Carriers periodically reassess whether the benefit trigger is still met — commonly every 6 to
12 months, usually through updated physician statements. Treat it with the same care as the
original claim: current records, and an accurate picture of a typical day.</p>

<h2>When care needs change</h2>
{record([
    ("Increasing hours or level of care",
     "<p>Notify the carrier and update the plan of care through the physician or care manager. "
     "Staying within your documented plan keeps reimbursement smooth.</p>"),
    ("Changing providers",
     "<p>Confirm the new provider meets the policy&rsquo;s definitions <em>before</em> the "
     "transition. Even one phone call to the carrier beforehand prevents most problems.</p>"),
    ("Hospitalizations and rehab stays",
     "<p>Ask the carrier how inpatient episodes interact with your claim. Home care benefits "
     "typically pause during a facility stay, and some policies have rules about restarting.</p>"),
])}

<h2>Watch the pool, not just the calendar</h2>
<p>If your policy has a total benefit pool, request the remaining balance at least annually — and
remember that spending below the daily maximum extends it. See
<a href="paying-for-care.html">Paying for care</a>.</p>

<h2>If payments stop or stall</h2>
<p>Most interruptions are administrative. Call and ask specifically what is missing, and escalate
in writing if it is unresolved.</p>
{note("Know your protections",
      "<p>For unreasonable delays or disputes, contact the California Department of Insurance "
      "consumer hotline at <span class=\"data\">1-800-927-4357</span>.</p>", "info")}"""

    body = article(_eyebrow(5), "Staying on claim: keeping benefits flowing",
                   "Most benefit interruptions are caused not by changes in health but by "
                   "lapses in paperwork.",
                   _rail(SECTIONS[4][0]), prose, prev, nxt)
    return page(SECTIONS[4][0], SECTIONS[4][1],
                "The monthly routine that keeps long-term care benefits flowing: documentation, "
                "recertification, changing providers, the benefit pool, and stalled payments.",
                body, current=HUB)


def _section_6():
    prev, nxt = _prev_next(5)
    prose = f"""<p>Families are often confused to discover that their carrier &ldquo;no longer
sells long-term care insurance.&rdquo; Understanding the landscape prevents two costly mistakes:
assuming an old policy is worthless, and cancelling coverage that could never be replaced
today.</p>

<h2>Carriers currently selling coverage</h2>
<p>Only a small number of insurers still sell new stand-alone long-term care policies — roughly
a half dozen nationally — with names including Mutual of Omaha, National Guardian Life, New York
Life, and Northwestern Mutual, alongside hybrid life-insurance-plus-LTC products from companies
such as Nationwide, Lincoln Financial, OneAmerica, Securian, and Brighthouse. Purchasing
decisions are covered in <a href="paying-for-care.html">Paying for care</a> and the
<a href="white-paper.html">2026 white paper</a>.</p>

<h2>Legacy carriers still servicing and paying claims</h2>
<p>This is the list most relevant to families using this guide, because most policies held by
Tri-Valley seniors were purchased 15 to 25 years ago. Companies including Genworth, John Hancock,
Transamerica, CNA, MetLife, Unum, Prudential, and Bankers Life stopped selling new individual
policies but continue to administer existing ones and pay claims — sometimes through third-party
administrators, so the name on your claim correspondence may differ from the name on your
policy.</p>
{note("Two points that matter more than any other on this page",
      "<p><strong>Your policy remains valid and claims are payable</strong> even though the carrier "
      "exited the sales market.</p>"
      "<p><strong>Do not cancel a legacy policy without professional advice.</strong> Older "
      "policies often contain benefits — lifetime benefit periods, strong inflation riders — that "
      "cannot be purchased at any price today. Even when facing a steep premium increase, options "
      "such as reduced-benefit alternatives or contingent nonforfeiture are usually better than "
      "walking away. Consult a financial adviser before making any change.</p>")}

<h2>Why premiums rose on older policies</h2>
<p>Several assumptions used in early pricing proved inaccurate: more policyholders kept their
coverage than insurers expected, claims and care duration ran higher than projected for some
blocks, long periods of low interest rates reduced investment income, and some early products
offered rich benefits at prices that were difficult to sustain.</p>
<p>Premium increases generally apply to a class of similar policies after state regulatory review.
They are not based on one policyholder becoming older, sicker, or filing a claim.
<strong>Guaranteed renewable</strong> means coverage cannot be individually canceled if premiums
are paid — it does not mean the premium is guaranteed never to increase.</p>
{note("A balanced conclusion",
      "<p>The premium-increase experience does not mean traditional policies failed. Many "
      "policyholders received valuable benefits that protected families and paid for years of care. "
      "It does mean consumers should understand premium stability, benefit-reduction options, "
      "carrier history, inflation design, and the difference between guaranteed coverage and "
      "guaranteed pricing.</p>", "plain")}

<h2>Other programs that may help pay for care</h2>
<p>Beyond private long-term care insurance, some families qualify for help through government
programs. These have their own rules and application processes.</p>
{record([
    ("VA benefits",
     "<p>For wartime veterans and surviving spouses who meet service, medical, and financial "
     "criteria. <a href=\"https://www.va.gov/\">va.gov</a></p>"),
    ("Medi-Cal and IHSS",
     "<p>Long-term services and supports, and In-Home Supportive Services, for those who meet "
     "eligibility rules. Start with your county IHSS office or the "
     "<a href=\"https://alameda.my-adrc.org/\">Alameda County ADRC</a>.</p>"),
    ("Public-employee programs",
     "<p>Such as CalPERS Long-Term Care. Contact your program&rsquo;s plan administrator.</p>"),
])}"""

    body = article(_eyebrow(6), "The carrier and program landscape",
                   "Why your carrier stopped selling policies, why that does not affect your "
                   "claim, and why cancelling an old policy is usually a mistake.",
                   _rail(SECTIONS[5][0]), prose, prev, nxt)
    return page(SECTIONS[5][0], SECTIONS[5][1],
                "Why long-term care carriers left the market, why legacy policies remain valid "
                "and payable, why premiums rose, and other programs that help pay for care.",
                body, current=HUB)


def build(**_):
    return [_hub(), _section_1(), _section_2(), _section_3(),
            _section_4(), _section_5(), _section_6()]
