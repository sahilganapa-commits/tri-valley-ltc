"""Getting Long-Term Care — the educational overview.

Covers the Phase 1 outline: what long-term care is, types of care, when to
start planning, how families pay, insurance basics, Medicare / Medi-Cal / VA,
and the questions families should ask.
"""

from layout import (checklist, cta, note, page, pagehead, rail, record, seq,
                    steps, table, ul)

SECTIONS = [
    ("#what", "What long-term care is"),
    ("#signs", "Signs it may be time"),
    ("#adls", "The daily activities check"),
    ("#levels", "The levels of care"),
    ("#when", "When to start planning"),
    ("#paying", "How families pay for care"),
    ("#insurance", "Long-term care insurance basics"),
    ("#public", "Medicare, Medi-Cal, and VA"),
    ("#ask", "Questions families should ask"),
]

ADL_ITEMS = [
    ("Bathing",
     "Getting in and out of the tub or shower safely and washing thoroughly. Needing help looks "
     "like: skipping baths out of fear of falling, needing someone nearby &ldquo;just in case,&rdquo; "
     "or no longer washing hair or hard-to-reach areas."),
    ("Dressing",
     "Choosing appropriate clothes and putting them on, including buttons, zippers, and shoes. "
     "Needing help looks like: wearing the same clothes repeatedly, clothes on inside out, or "
     "giving up on anything with fasteners."),
    ("Toileting",
     "Getting to and from the toilet and managing hygiene afterward. Needing help looks like: "
     "accidents because the bathroom is too far, nighttime difficulty, or avoiding fluids to "
     "avoid trips to the bathroom."),
    ("Transferring",
     "Moving safely between bed, chair, and standing. Needing help looks like: struggling to rise "
     "from a chair, needing to be pulled up, or staying in one place most of the day because "
     "moving feels risky."),
    ("Eating",
     "Feeding oneself once food is prepared. Needing help looks like: difficulty using utensils, "
     "trouble swallowing, or meals left mostly uneaten. Trouble <em>preparing</em> meals counts "
     "too — it is one of the most common early needs, even when eating itself is fine."),
    ("Continence",
     "Bladder and bowel control. Needing help looks like: accidents, hiding soiled clothing, or "
     "withdrawing from activities out of embarrassment."),
    ("Supervision",
     "Not on the standard list of six, but just as real. Some people can physically do all six "
     "activities and still cannot safely be alone — because of memory loss, confusion, wandering, "
     "or leaving the stove on. Supervision needs caused by cognitive change are a care need in "
     "their own right, and insurers treat them as one."),
]


def build(**_):
    body = pagehead(
        "Part one of the guide",
        "Getting long-term care",
        "Most families do not decide to get help. They notice, gradually, that something has "
        "changed. This page covers what long-term care actually is, how to tell when it is "
        "time, what the options are, and how people pay for it.",
    ) + f"""<section class="band">
<div class="shell layout">
{rail("On this page", SECTIONS, None)}
<div class="prose">

<h2 id="what">What long-term care is</h2>
<p>Long-term care is help with everyday living, not medical treatment. It supports people who
need ongoing assistance because of chronic illness, disability, cognitive impairment, or
frailty — help with bathing, dressing, eating, transferring, toileting, continence, meal
preparation, supervision, transportation, and household tasks.</p>
<p>That distinction matters more than almost anything else on this site, because it determines
who pays. Medicare covers medically necessary acute care and limited skilled services. It does
not generally cover custodial long-term care when that is the only care needed.</p>
{note("The most common misunderstanding",
      "<p>Long-term care is not simply a nursing-home issue. It includes help at home, adult day "
      "programs, assisted living, memory care, and nursing facilities. Most families start with a "
      "few hours a week of help at home, and many never need more than that.</p>")}

<h2 id="signs">Signs it may be time</h2>
<p>No single sign means it is time for care. But if several of these are showing up, it is worth
taking a closer look.</p>
{ul([
    "Missed medications, or confusion about which pills to take when",
    "Unpaid bills, unopened mail, or unusual purchases",
    "A fall — or a new fear of falling, holding walls and furniture to get around",
    "Weight loss, an empty refrigerator, or spoiled food",
    "Changes in personal hygiene, or wearing the same clothes for days",
    "The house is not being kept up the way it used to be",
    "Memory changes: repeated questions, missed appointments, getting lost on familiar routes",
    "A spouse or family member providing care who is exhausted, isolated, or unwell themselves",
])}
<p>That last one matters as much as the others. Caregiver burnout is one of the most common
reasons families seek help, and one of the best reasons to.</p>

<h2 id="adls">The daily activities check</h2>
<p>Care professionals, doctors, and insurance companies all measure care needs the same way:
through six basic activities of daily living, usually called ADLs. Go through them honestly —
not &ldquo;can they do it on a good day,&rdquo; but &ldquo;can they do it safely and reliably,
every day, without help.&rdquo;</p>
{checklist(
    "adl",
    "Which activities need help?",
    "<p>Tick each activity where help is needed. Your answers stay in this browser — we never "
    "see them — and you can print them to bring to a doctor or a carrier.</p>",
    ADL_ITEMS,
    trigger=2,
    rest_text="Answer honestly, including supervision. This list does double duty: it tells you "
              "what kind of help to look for, and it is the same test an insurance carrier applies.",
    trigger_text="Needing substantial help with two or more of these — or needing supervision "
                 "because of cognitive impairment — is typically what makes a long-term care "
                 "policy start paying. If there is a policy in the family, read Section 2 of "
                 "Using your coverage next, and keep these answers.",
)}
{note("Why this list matters twice over",
      "<p>It tells you what kind of help to look for. And if there is a long-term care insurance "
      "policy in the family, needing help with two or more of these activities — or needing "
      "supervision due to cognitive impairment — is typically what makes the policy pay. Keep "
      "your honest answers. You will use them again when you "
      "<a href=\"using-coverage-know-your-policy.html\">read the policy</a> and again when you "
      "<a href=\"using-coverage-filing-a-claim.html\">file a claim</a>.</p>", "info")}

<h2 id="levels">The levels of care, lightest to most support</h2>
{record([
    ("In-home care",
     "<p>A caregiver comes to the home, from a few hours a week to around the clock: help with the "
     "daily activities above, meals, errands, companionship, and supervision. Most families start "
     "here, and many never need more.</p>"),
    ("Adult day and PACE",
     "<p>Daytime care, activities, meals, and health services at a center, with evenings at home. "
     "Often the right fit when a family caregiver works during the day, and a meaningful source of "
     "social connection.</p>"),
    ("Assisted living and memory care",
     "<p>A residential community with staff around the clock: meals, housekeeping, and help with "
     "daily activities. Memory care adds secured surroundings and staff trained for dementia.</p>"),
    ("Skilled nursing, rehab, and hospice",
     "<p>For medical needs: nursing care, recovery after a hospital stay, or comfort-focused care "
     "near the end of life.</p>"),
])}
<p>These are not a one-way ladder. Many families combine them — adult day during the week plus
in-home care on weekends — and needs step up and down over time. Every level of care above is
represented in the <a href="directory.html">Tri-Valley care directory</a>.</p>

<h2 id="when">When to start planning</h2>
<p>Planning is most effective before a health event, for a blunt reason: long-term care insurance
is medically underwritten, so the healthier you are, the more choices you have. Earlier planning
also gives you more time to save and more flexibility to coordinate estate and retirement
decisions.</p>
<p>If you are already past that point — if a diagnosis has arrived or care is needed now — almost
everything on this site still applies. You are choosing among funding sources and providers
rather than among insurance policies.</p>
{table(
    ["Planning statistic", "Federal estimate"],
    [["Chance a person turning 65 will need some type of long-term care", "Almost 70%"],
     ["Average duration of care for women", "3.7 years"],
     ["Average duration of care for men", "2.2 years"],
     ["People turning 65 who may need care longer than five years", "About 20%"]],
    caption="Source: Administration for Community Living, &ldquo;How Much Care Will You Need?&rdquo;",
)}

<h2 id="paying">How families pay for care</h2>
<p>Almost no family pays for care from a single source. The common combination is personal
income and savings, a family caregiver providing unpaid hours, an insurance policy if one
exists, and public benefits if eligibility is met.</p>
{table(
    ["Source", "What it typically covers"],
    [["Income and savings",
      "Retirement income, Social Security, pensions, investments, and dedicated reserves. Maximum "
      "flexibility, no underwriting — but the full cost and the longevity risk stay with the family."],
     ["Long-term care insurance",
      "A defined pool of benefits for qualifying care, once the policy&rsquo;s trigger and waiting "
      "period are met. Only helps if a policy already exists or can still be underwritten."],
     ["Life insurance or annuity with LTC benefits",
      "Care benefits drawn from a policy that also carries a death benefit or contract value. "
      "Now the most common form of newly purchased coverage."],
     ["Medi-Cal (Medicaid in California)",
      "Long-term services and supports for people who meet financial and functional eligibility "
      "rules. A major source of nursing-facility funding."],
     ["VA benefits",
      "Aid and Attendance and related benefits for wartime veterans and surviving spouses who "
      "meet service, medical, and financial criteria."],
     ["Home equity",
      "Sale proceeds, downsizing, a home-equity strategy, or a reverse mortgage where appropriate. "
      "Affects housing security and heirs."],
     ["Family caregiving",
      "Unpaid or partially paid support from relatives. Preserves familiar care and reduces cash "
      "cost, at real time, income, health, and relationship cost to the caregiver."]],
    caption="Most families use several of these at once. See "
            "<a href=\"paying-for-care.html\">Paying for care</a> for how to combine them.",
)}

<h2 id="insurance">Long-term care insurance basics</h2>
<p>If you are reading a policy for the first time, five terms decide almost everything. They are
covered in depth in <a href="using-coverage-know-your-policy.html">Know your policy</a>.</p>
{record([
    ("Benefit trigger",
     "<p>What has to be true before the policy pays. Usually: a licensed health practitioner "
     "certifies substantial assistance is needed with at least two of the six activities of daily "
     "living, or supervision is needed due to cognitive impairment.</p>"),
    ("Elimination period",
     "<p>The waiting period before benefits begin — commonly 30, 60, 90, or 100 days. Check whether "
     "your policy counts <em>calendar</em> days or <em>service</em> days; the difference can be "
     "months.</p>"),
    ("Benefit amount",
     "<p>The daily or monthly maximum. If the policy has an inflation rider, today&rsquo;s figure "
     "is on your latest annual statement, not on the original policy.</p>"),
    ("Benefit period or pool",
     "<p>Either a set number of years, or a total pool of money that lasts as long as it lasts. "
     "Spending below the daily maximum stretches a pool.</p>"),
    ("Covered providers",
     "<p>Which caregivers and settings qualify. The section families skip most often, and the one "
     "that determines how you can actually use the benefits.</p>"),
])}
{note("If you are buying rather than using",
      "<p>The market changed substantially. In 2024 new-policy data, 92% of individual solutions "
      "were life-insurance-based combination products and 8% were traditional stand-alone "
      "long-term care policies. What that does and does not mean is covered in the "
      "<a href=\"white-paper.html\">2026 white paper</a>.</p>")}

<h2 id="public">Medicare, Medi-Cal, and VA</h2>
{record([
    ("Medicare",
     "<p>Covers medically necessary acute care and limited skilled services — for example, a short "
     "skilled-nursing stay after a qualifying hospital admission, or intermittent home health care "
     "under specific conditions. It does <strong>not</strong> generally pay for ongoing custodial "
     "care, which is what most long-term care actually is. "
     "<a href=\"https://www.medicare.gov/coverage/long-term-care\">medicare.gov</a></p>"),
    ("Medi-Cal",
     "<p>California&rsquo;s Medicaid program can finance extensive long-term services and supports "
     "for people who meet financial and functional eligibility rules. Related programs include "
     "In-Home Supportive Services (IHSS) and the Assisted Living Waiver, which is available in "
     "Alameda and Contra Costa counties. "
     "<a href=\"https://www.dhcs.ca.gov/services/ltc\">dhcs.ca.gov</a></p>"),
    ("California Partnership",
     "<p>A state program under which specifically approved policies include consumer protections "
     "and may provide Medi-Cal asset protection equal to qualifying benefits paid. A Partnership "
     "policy and an asset-based or hybrid policy are not automatically the same thing — verify "
     "whether a specific contract is Partnership-approved.</p>"),
    ("VA benefits",
     "<p>Wartime veterans and surviving spouses may qualify for Aid and Attendance and related "
     "benefits, subject to service, medical, and financial criteria. Start at "
     "<a href=\"https://www.va.gov/\">va.gov</a>.</p>"),
    ("Where to ask locally",
     "<p>The Alameda County Aging and Disability Resource Connection provides free, multilingual "
     "navigation for Medi-Cal, IHSS, caregiver supports, transportation, and housing. "
     "<a href=\"https://alameda.my-adrc.org/\">alameda.my-adrc.org</a>, or dial 2-1-1.</p>"),
])}

<h2 id="ask">Questions families should ask</h2>
<p>Ask these of each other before you ask them of a provider. The answers shape every decision
that follows.</p>
{steps([
    ("Where would care be received, if there were a choice?",
     "<p>Remaining at home is the most common preference and the one most often assumed rather than "
     "discussed. Ask directly, and ask early enough that the answer still matters.</p>"),
    ("Who is available to help, and at what cost to them?",
     "<p>Name the people. Then ask what caregiving would mean for their work, health, income, and "
     "relationships — because unpaid family care is the single largest funding source for "
     "long-term care in this country, and it is not free.</p>"),
    ("Who makes decisions if the person cannot?",
     "<p>Financial and medical powers of attorney, and whether the named people know they are "
     "named. This is the cheapest thing on this list and the most often missed.</p>"),
    ("What could the household absorb per year, for how long?",
     "<p>Local care runs roughly $75,000 to $180,000 a year depending on setting. Test the number "
     "against retirement income before a crisis forces the test.</p>"),
    ("Is there existing coverage nobody has read?",
     "<p>Life insurance, annuities, or a long-term care policy bought decades ago. Old policies are "
     "frequently better than anything sold today. Find the documents now, not later.</p>"),
])}

{seq(nxt=("using-coverage.html", "Understanding and using your coverage"))}
</div>
</div>
</section>

{cta("Not sure which of these applies to your family?",
     "Tell us what you are seeing and we will point you to the right section, or to someone "
     "locally who can help.")}"""

    return page(
        "getting-care.html",
        "Getting long-term care",
        "What long-term care is, how to tell when it is time, the levels of care available, "
        "how families pay for it, and what Medicare, Medi-Cal, and VA benefits do and do not cover.",
        body,
    )
