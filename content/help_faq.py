"""Contact, frequently asked questions, and the white paper."""

from layout import (PROGRAM_EMAIL, VERIFIED, faq_list, hero_page, esc, note, page, pagehead,
                    rail, record, table, ul)

FAQS = [
    ("Does Medicare pay for long-term care?",
     "<p>Medicare generally does not pay for custodial long-term care — the ongoing, non-medical "
     "help with daily activities that most long-term care actually consists of. It may cover "
     "limited skilled nursing or home health services when specific medical conditions and "
     "eligibility rules are met.</p>"),
    ("Is long-term care planning only about insurance?",
     "<p>No. A complete plan may combine income, savings, investments, insurance, annuities, home "
     "equity, public benefits, and family support. For many families the right answer involves no "
     "new insurance at all.</p>"),
    ("When should planning begin?",
     "<p>Before a health event. Long-term care insurance is medically underwritten, so earlier "
     "planning means more choices, more time to save, and greater flexibility to coordinate estate "
     "and retirement decisions. If you are already past that point, you are choosing among funding "
     "sources and providers instead — which is what most of this site covers.</p>"),
    ("How much money should be reserved?",
     "<p>It depends on local care costs, the preferred setting, available family support, insurance "
     "benefits, inflation, and how much risk the family is comfortable keeping. Start with "
     "<a href=\"paying-for-care.html#cost\">what care costs here</a> and test a year of it against "
     "your retirement income.</p>"),
    ("What is an asset-based or linked-benefit plan?",
     "<p>Generally a life insurance or annuity contract that combines long-term care benefits with "
     "another financial value, such as a death benefit, cash value, or annuity value. Features and "
     "guarantees vary considerably by contract.</p>"),
    ("Can long-term care expenses or premiums receive tax benefits?",
     "<p>Certain qualified long-term care services and limited amounts of premiums for qualified "
     "policies may be treated as medical expenses under federal tax rules. Eligibility and the "
     "value of any deduction depend on the taxpayer&rsquo;s facts and on current law. Ask a tax "
     "professional — this is not something to work out from a website.</p>"),
    ("What is the California Partnership for Long-Term Care?",
     "<p>A California program involving the state and approved insurers. Qualifying Partnership "
     "policies include consumer protections and may provide Medi-Cal asset protection equal to "
     "qualifying benefits paid, subject to program rules. A Partnership policy and a hybrid or "
     "asset-based policy are not automatically the same thing — verify whether a specific contract "
     "is Partnership-approved.</p>"),
    ("My carrier stopped selling policies. Is my policy still good?",
     "<p>Yes. A carrier leaving the sales market does not cancel your policy, and claims on existing "
     "policies are still paid — sometimes through a third-party administrator, so the name on your "
     "correspondence may differ from the name on your policy. Do not cancel a legacy policy without "
     "professional advice; older policies often contain benefits that cannot be bought at any price "
     "today. See <a href=\"using-coverage-carrier-landscape.html\">the carrier landscape</a>.</p>"),
    ("How long does a claim take?",
     "<p>Commonly 60 to 90 days or more between the first phone call and the first benefit payment, "
     "once you account for claim paperwork, the carrier&rsquo;s assessment, and the elimination "
     "period written into the policy. You can begin a claim before choosing a provider — and you "
     "should. See <a href=\"using-coverage-filing-a-claim.html\">filing a claim</a>.</p>"),
    ("Can I pay a family member to provide care?",
     "<p>Sometimes. Many policies exclude or restrict payment to spouses and relatives; some cover "
     "them. This is written into your policy&rsquo;s provider definitions, and it is worth getting "
     "the answer in writing before care starts rather than after. See "
     "<a href=\"using-coverage-approved-providers.html\">approved providers</a>.</p>"),
    ("Do you recommend specific facilities or agencies?",
     "<p>No. Our <a href=\"directory.html\">directory</a> is informational only and is not an "
     "endorsement. We are not paid by any provider listed, and we do not accept referral fees from "
     "them. We will happily help you work out what to ask them.</p>"),
    ("What happens if we do nothing?",
     "<p>The family may still pay for care, but the decision arrives during a crisis. Without a "
     "plan, care costs can force unplanned asset sales, large taxable withdrawals, caregiver strain, "
     "and far fewer choices about where care is received.</p>"),
]


def _help():
    body = hero_page("help.jpg",
                   "An older couple walk away down a tree-lined path, side by side.",
                   "Tell us where you are, and we will point you somewhere useful",
                   "Describe your situation and we will point you to the right next step. No obligation, and never a sales call.",
                   "center 58%") + f"""<section class="band">
<div class="shell layout">
<aside class="rail" aria-label="What to expect">
<p class="rail__title">What to expect</p>
{record([
    ("Response time", "<p>Usually within one business day.</p>"),
    ("Cost", "<p>Free. We are a nonprofit program.</p>"),
    ("What we do not do",
     "<p>We do not sell insurance, care, or placement services, and we accept no referral fees "
     "from providers.</p>"),
])}
</aside>
<div class="prose">

<h2>Send us a message</h2>
<form class="form" data-form>
<div class="form__row">
<label class="field"><span class="field__label">Your name</span>
<input class="field__input" type="text" name="name" autocomplete="name" required></label>
<label class="field"><span class="field__label">Phone (optional)</span>
<input class="field__input" type="tel" name="phone" autocomplete="tel"></label>
</div>
<label class="field"><span class="field__label">Email</span>
<input class="field__input" type="email" name="email" autocomplete="email" required></label>
<label class="field"><span class="field__label">What can we help with?</span>
<select class="field__input" name="topic">
<option>Using an existing long-term care policy</option>
<option>Understanding what long-term care involves</option>
<option>Planning how to pay for care</option>
<option>Finding care in the Tri-Valley</option>
<option>Something else</option>
</select></label>
<label class="field"><span class="field__label">City or area</span>
<input class="field__input" type="text" name="city" placeholder="Dublin, Pleasanton, Livermore&hellip;"></label>
<label class="field"><span class="field__label">Tell us about your situation</span>
<textarea class="field__input" name="message" rows="6"
placeholder="Where are you in the process? What has already happened?"></textarea></label>
<label class="form__consent">
<input type="checkbox" name="consent">
<span>If my question is best answered by a licensed professional, I consent to this program
sharing my inquiry with a professional I select. I understand a referral does not require me to
buy anything.</span>
</label>
<button class="btn btn--primary" type="submit">Send message</button>
<p class="form__note">We use your information only to respond to your inquiry. See the
<a href="privacy.html">privacy policy</a>.</p>
<p class="note note--info" data-form-status hidden tabindex="-1">
<strong>This form is not connected yet.</strong> The site is still being set up, so nothing was
sent. In the meantime, email <a href="mailto:{PROGRAM_EMAIL}">{PROGRAM_EMAIL}</a> and we will
reply within one business day.</p>
</form>

<h2 id="referrals">How referrals work</h2>
<p>Some questions are ours to answer. Others need a licensed professional — an insurance agent,
a financial adviser, a tax professional, an elder law attorney, or a care manager. Here is
exactly what happens in that case.</p>
{record([
    ("1. You send the inquiry",
     "<p>Through this form, or by email. Nothing goes anywhere else at this stage.</p>"),
    ("2. We work out what kind of question it is",
     "<p>Financial planning, care management, or care settings. Often we can simply answer it, or "
     "point you at the right section of this guide.</p>"),
    ("3. You choose, and you consent",
     "<p>If a licensed professional would help, we tell you who and why. With your consent, the "
     "inquiry is routed to the professional you select. You are never routed anywhere "
     "automatically.</p>"),
    ("4. They disclose, before anything else",
     "<p>The professional provides their own disclosures about services, licensing, affiliations, "
     "fees, and any insurance compensation, before any engagement begins.</p>"),
])}
{note("Affiliation disclosure",
      "<p>The Tri-Valley Long Term Care Resource Program provides general education and referrals. "
      "Any professional you may be referred to operates a separate business, which is not part of "
      "this nonprofit. A referral does not require you to purchase a product or engage a particular "
      "professional. Any advisory fees, insurance commissions, affiliations, or compensation "
      "arrangements are disclosed to you before services are provided. This program receives no "
      "compensation for referrals.</p>")}

<h2>Financial planning contact</h2>
<p>Families with questions about funding care, reviewing an existing policy, or protecting a
spouse are commonly referred to:</p>
{record([
    ("Professional", "<p>Dr. Sherry Hu, CFP&reg;<br>Peace of Mind Finance</p>"),
    ("Website", '<p><a href="https://pomfinance.com">POMFinance.com</a></p>'),
    ("Email", '<p><a href="mailto:sherry.hu@pomfinance.com">sherry.hu@pomfinance.com</a></p>'),
    ("Phone", '<p><a href="tel:9255582712"><span class="data">(925) 558-2712</span></a></p>'),
    ("Appointments",
     '<p><a href="https://calendly.com/drsherryhu/peace-of-mind-finance-consulting-30min">'
     'Book a 30-minute consultation</a></p>'),
    ("Please note",
     "<p>Peace of Mind Finance is a separate financial-services business, not part of this "
     "nonprofit program. A referral does not require you to purchase anything.</p>"),
])}

<h2>Other places to get free help</h2>
{record([
    ("Alameda County ADRC",
     '<p>Free multilingual navigation for Medi-Cal, IHSS, caregiver supports, adult day programs, '
     'transportation, housing, and legal resources.<br>'
     '<a href="https://alameda.my-adrc.org/">alameda.my-adrc.org</a> &middot; dial '
     '<span class="data">2-1-1</span></p>'),
    ("Long-Term Care Ombudsman",
     '<p>Free, independent help with resident rights and complaints in licensed long-term care '
     'settings.<br><a href="https://aging.ca.gov/Programs_and_Services/Long-Term_Care_Ombudsman/">'
     'aging.ca.gov</a></p>'),
    ("California Dept. of Insurance",
     '<p>Regulates long-term care insurance and helps consumers with claim delays and disputes.<br>'
     '<a href="https://www.insurance.ca.gov/">insurance.ca.gov</a> &middot; '
     '<span class="data">1-800-927-4357</span></p>'),
])}
</div>
</div>
</section>"""

    return page(
        "help.html",
        "Contact us",
        "Ask the Tri-Valley Long Term Care Community Program a question about using a policy, "
        "planning for care costs, or finding local care. Free, nonprofit, and never a sales call.",
        body,
        overlay=True,
    )


def _faq():
    items = faq_list(FAQS)

    body = hero_page("faq.jpg",
                   "A younger hand and an older hand clasped together.",
                   "The questions families ask us most",
                   "Short answers, with a link to the longer version where there is one.",
                   "center 50%") + f"""<section class="band">
<div class="shell">
<div class="prose" style="max-width:74ch">
{items}

<h2 id="white-paper">Download the 2026 white paper</h2>
<p><em>Planning for Long-Term Care in a Changing Insurance Market</em> covers costs, coverage
options, the provider landscape, and asset-based strategies in more depth than these pages do —
with full source citations.</p>
<p>You can <a href="white-paper.html">read the whole thing on this site</a>, free and with no
email address required. If you would rather have a copy sent to you, leave an address below.</p>

<form class="form" data-form>
<label class="field"><span class="field__label">Email address</span>
<input class="field__input" type="email" name="email" autocomplete="email" required></label>
<label class="field"><span class="field__label">Name (optional)</span>
<input class="field__input" type="text" name="name" autocomplete="name"></label>
<label class="form__consent">
<input type="checkbox" name="updates">
<span>Also send me occasional updates from the program. We do not sell or share email addresses,
and every message has an unsubscribe link.</span>
</label>
<button class="btn btn--primary" type="submit">Send me the white paper</button>
<p class="form__note">Your address is used to send the paper and, if you tick the box, program
updates. See the <a href="privacy.html">privacy policy</a>.</p>
<p class="note note--info" data-form-status hidden tabindex="-1">
<strong>This form is not connected yet.</strong> The site is still being set up, so nothing was
sent. <a href="white-paper.html">Read the white paper here</a> in the meantime, or email
<a href="mailto:{PROGRAM_EMAIL}">{PROGRAM_EMAIL}</a>.</p>
</form>
</div>
</div>
</section>"""

    return page(
        "faq.html",
        "Frequently asked questions",
        "Answers to the long-term care questions families ask most: Medicare coverage, when to "
        "plan, legacy policies, claim timelines, and the California Partnership program.",
        body,
        overlay=True,
    )


WP_SECTIONS = [
    ("#summary", "Executive summary"),
    ("#matters", "Why planning matters"),
    ("#evolved", "How the market evolved"),
    ("#current", "The current market"),
    ("#asset", "Asset-based and linked benefit"),
    ("#providers", "Representative providers"),
    ("#framework", "A decision framework"),
    ("#california", "California considerations"),
    ("#references", "References"),
]


def _white_paper():
    prose = f"""{note("About this paper",
      "<p>This paper offers general education for individuals, families, caregivers, and community "
      "organizations. It explains why long-term care planning matters, how the insurance market "
      "evolved, and how traditional and asset-based approaches may fit different situations. It "
      "does not recommend a specific company or product.</p>"
      f"<p>Prepared by Tri-Valley LTC, a nonprofit program &middot; {esc(VERIFIED)}</p>", "plain")}

<h2 id="summary">Executive summary</h2>
<p>Long-term care is not simply a nursing-home issue. It includes assistance at home, adult day
services, assisted living, memory care, and nursing-facility care. Someone turning age 65 has
nearly a 70% chance of needing some form of long-term services and supports during the remaining
years of life. Women on average need care longer than men, and about one in five people turning
65 may need care for more than five years.</p>
<p>The financial exposure is substantial. In 2025, the national median annual cost was
approximately $80,080 for a non-medical caregiver at 44 hours per week, $74,400 for assisted
living, and $129,575 for a private nursing-home room. California medians were higher for most
settings, including approximately $91,520 for home care and $182,135 for a private nursing-home
room.</p>
<p>Traditional stand-alone long-term care insurance has helped many families preserve assets and
obtain care. It also went through a difficult repricing era. Early policies were often priced with
assumptions that proved too optimistic about claim levels, policy lapses, and investment earnings.
Many long-time policyholders later faced premium increases or choices to reduce benefits. The NAIC
reported that among heavily affected blocks studied, the average single approved increase was 37%
and the average cumulative approved increase was 112%.</p>
<p>Today, no single solution is best for everyone. Traditional stand-alone insurance remains
available from a smaller group of carriers, but the new-sales market has shifted decisively toward
combination designs.</p>
{note("Key finding",
      "<p>The modern planning question is no longer only &ldquo;Should I buy long-term care "
      "insurance?&rdquo; A better question is &ldquo;Which combination of insurance, personal "
      "assets, public benefits, family support, and care preferences can create a durable "
      "plan?&rdquo;</p>")}

<h2 id="matters">Why long-term care planning matters</h2>
<h3>Long-term care is personal care, not ordinary medical treatment</h3>
<p>Long-term care generally supports people who need ongoing help because of chronic illness,
disability, cognitive impairment, or frailty. Common services include help with bathing, dressing,
eating, transferring, toileting, continence, meal preparation, supervision, transportation, and
household tasks. Care may be provided by paid professionals, family members, or both.</p>
<p>Medicare covers medically necessary acute care and limited skilled services, but it does not
generally cover custodial long-term care when that is the only care needed. Medicaid can finance
extensive long-term services for people who meet applicable financial and functional eligibility
rules, which vary by state.</p>

<h3>2025 cost of care</h3>
{table(
    ["Care setting", "2025 U.S. median", "2025 California median"],
    [["Non-medical caregiver, 44 hrs/week", "$80,080", "$91,520"],
     ["Adult day health care", "$24,700", "$24,440"],
     ["Assisted living / residential care", "$74,400", "$82,800"],
     ["Nursing home, semi-private room", "$114,975", "$146,000"],
     ["Nursing home, private room", "$129,575", "$182,135"]],
    caption="Figure 1. Median annual costs, CareScout 2025 Cost of Care Survey. Home care assumes "
            "44 hours per week. Actual costs vary by location, care intensity, provider, and "
            "service availability.",
)}

<h2 id="evolved">How the long-term care insurance market evolved</h2>
<h3>The first generation: traditional stand-alone coverage</h3>
<p>Individual long-term care insurance became available in the 1970s. Early contracts focused
primarily on nursing-home care. Over time, policies expanded to include home health care, adult
day care, assisted living, care coordination, and other services. Traditional policies typically
use a monthly or daily benefit, a maximum benefit pool or period, an elimination period, and
optional inflation protection.</p>

<h3>Why many older policies experienced premium increases</h3>
{ul([
    "More policyholders kept their coverage than insurers expected, so lapse rates were lower.",
    "Claims and care duration were higher than originally projected for some policy blocks.",
    "Long periods of low interest rates reduced investment income supporting future benefits.",
    "Some early products offered rich benefits, including lifetime coverage and strong inflation "
    "protection, at prices that were difficult to sustain.",
])}
<p>Premium increases generally apply to a class of similar policies after state regulatory review;
they are not based on one policyholder becoming older, sicker, or filing a claim.
<strong>Guaranteed renewable</strong> means coverage cannot be individually canceled if premiums
are paid, but it does not mean the premium is guaranteed never to increase.</p>
{note("A balanced historical conclusion",
      "<p>The premium-increase experience does not mean traditional policies failed. Many "
      "policyholders received valuable benefits that protected families and paid for years of care. "
      "It does mean consumers should understand premium stability, benefit-reduction options, "
      "carrier history, inflation design, and the difference between guaranteed coverage and "
      "guaranteed pricing.</p>", "plain")}

<h2 id="current">The current market: multiple ways to fund care</h2>
{table(
    ["Approach", "How it works", "Potential strengths", "Important tradeoffs"],
    [["Traditional stand-alone LTC insurance",
      "Premium buys a defined LTC benefit pool or period.",
      "Can provide efficient care leverage; flexible inflation and benefit design.",
      "Premiums may increase on a class basis; use-it-or-lose-it concern unless return-of-premium "
      "features apply."],
     ["Life insurance with LTC benefits",
      "Death benefit can be accelerated for qualified LTC; some plans add an extension of benefits.",
      "Care benefit if needed; remaining death benefit if care is not needed; some plans have fixed "
      "premiums.",
      "Large upfront or limited-pay premium; LTC use reduces death benefit; liquidity and surrender "
      "terms matter."],
     ["Annuity with LTC benefits",
      "An annuity value is leveraged for LTC, sometimes with an extended benefit rider.",
      "May reposition existing annuity or cash; some plans offer lifetime extension options.",
      "Opportunity cost, surrender rules, underwriting, inflation, and qualified-account tax issues "
      "require review."],
     ["Self-funding",
      "Personal investments, income, home equity, or family resources pay care expenses.",
      "Maximum control and no underwriting.",
      "Full cost and longevity risk remain with the family; market timing and caregiver stress can "
      "be severe."],
     ["Public and partnership programs",
      "Medicaid/Medi-Cal and state Partnership rules may help eligible individuals.",
      "Can protect access to essential services; Partnership policies may provide asset disregard.",
      "Eligibility, income contribution, service availability, and state rules are complex."]],
)}

<h3>What 2024 new-sales data show</h3>
<p>The composition of newly issued policies has changed dramatically. The following figures are
based on <strong>policy count</strong>, not total premium, assets deposited, benefits purchased,
or the number of older policies already in force. They describe the direction of the new market,
not the entire installed base of long-term care coverage.</p>
{table(
    ["2024 individual solution", "New policies", "Share by policy count"],
    [["Life insurance with chronic-illness rider", "327,025", "67%"],
     ["Life insurance with LTC rider", "91,619", "19%"],
     ["Linked-benefit life/LTC policy", "32,268", "6%"],
     ["Traditional stand-alone LTC insurance", "38,715", "8%"],
     ["Total", "489,627", "100%"]],
    caption="Figure 2. LIMRA/EY 2024 new-policy data. The 92% life-based share includes "
            "chronic-illness riders, qualified LTC riders, and linked-benefit policies. These "
            "categories are not interchangeable — a chronic-illness rider may use different "
            "benefit triggers, tax rules, payout methods, or benefit calculations from a "
            "tax-qualified LTC rider.",
)}
{note("How to interpret the 92% / 8% statistic",
      "<p>It does <em>not</em> show that 92% of all Americans with long-term care coverage own "
      "hybrid policies, and it does not include annuity/LTC products in the 92%. It shows that "
      "life-based combination designs accounted for 92% of the individual new-policy count reported "
      "in the cited 2024 surveys. That is strong evidence of a market shift toward multi-purpose "
      "designs, while traditional stand-alone insurance continues to serve a smaller share of new "
      "buyers.</p>")}
<p>Annuity/LTC products are measured separately. LIMRA reported record 2024 sales, more than 50%
year-over-year growth, and approximately 14% of total individual long-term care insurance sales —
though only 0.2% of total annuity sales. That indicates meaningful growth from a small base rather
than market dominance.</p>

<h3>Traditional stand-alone pricing: a practical benchmark</h3>
{table(
    ["Illustrative traditional design", "Combined annual premium", "Interpretation"],
    [["Couple both age 60, level benefits", "$2,600", "Lower initial cost, no automatic benefit growth"],
     ["Couple both age 60, 3% compound growth", "$5,800", "Benefit pool grows annually"],
     ["Couple both age 65, 3% compound growth", "$7,150", "Later purchase age materially increases cost"],
     ["Age-65 couple, similar 3% designs across three leading carriers", "$7,137 – $12,250",
      "Carrier selection can change cost substantially"],
     ["California husband 64 / wife 62, standard health", "$7,500 – $10,000",
      "Planning range only; not a carrier quote"]],
    caption="Figure 3. 2025 AALTCI price index, select-health couples, initial benefit pool of "
            "$165,000 per spouse. Benchmarks are based on Illinois pricing and vary by state and "
            "carrier.",
)}
<p>A richer design with a larger monthly benefit, five-year or shared benefits, stronger inflation
protection, or less favorable underwriting may cost more. A leaner design may cost less.
California buyers should obtain current carrier illustrations and review each insurer&rsquo;s rate
history, because traditional premiums may be increased for a policy class after regulatory
approval.</p>

<h3>Why combination products may feel more reasonable to many households</h3>
{table(
    ["Design", "How price is usually experienced", "What remains if care is not needed", "Primary concern"],
    [["Traditional stand-alone LTC",
      "Ongoing annual premium; generally lower initial asset commitment",
      "Usually no death benefit unless an optional feature applies",
      "Class-wide premium increases and use-it-or-lose-it concern"],
     ["Life/LTC linked benefit",
      "Often a larger single premium or fixed limited-pay schedule",
      "Death benefit or residual policy value may remain",
      "Liquidity, opportunity cost, policy charges, and benefit design"],
     ["Annuity/LTC",
      "Existing cash or annuity value is repositioned; optional rider cost may apply",
      "Remaining contract value may remain for owner or beneficiaries",
      "Surrender period, tax treatment, inflation, underwriting, and opportunity cost"]],
)}
<p>Combination products are not necessarily less expensive in nominal dollars. Their value
proposition is different: premiums or assets may support long-term care and also retain a death
benefit, contract value, or other financial utility. For households with suitable assets, this can
make the funding decision feel more durable and easier to maintain than an open-ended stand-alone
premium. For households seeking the greatest care benefit for the lowest current outlay,
traditional insurance may still be more efficient. The appropriate comparison is therefore total
value, guarantees, liquidity, inflation protection, claims design, and long-term affordability —
not premium alone.</p>

<h2 id="asset">Asset-based and linked-benefit long-term care</h2>
<p>&ldquo;Asset-based long-term care&rdquo; is a broad category. It generally refers to a life
insurance policy or annuity that includes qualified long-term care benefits. Note that some
carriers use similar wording as a product name, so the generic category and any particular product
name should not be treated as identical.</p>
<p>These arrangements have become prominent because they address several consumer concerns:
uncertainty about future premium increases, the fear of paying for coverage that may never be
used, and the desire to reposition an existing asset rather than add another indefinite
expense.</p>

<h3>Potential advantages</h3>
{ul([
    "Benefits are available for qualified long-term care if care is needed.",
    "If care is not needed, a death benefit or remaining contract value may still benefit the "
    "owner or family.",
    "Some products offer guaranteed premiums, guaranteed benefits, limited-pay schedules, or "
    "lifetime continuation options.",
    "Cash-indemnity designs can provide a fixed monthly benefit after claim approval without "
    "monthly reimbursement paperwork; reimbursement designs pay eligible actual expenses.",
    "A properly executed Section 1035 exchange may allow certain life insurance or annuity values "
    "to move into qualified long-term care coverage without recognizing current gain, subject to "
    "tax rules and direct-transfer requirements.",
])}

<h3>Important limitations and questions</h3>
{ul([
    "How much liquidity is surrendered or restricted?",
    "Is the premium truly guaranteed, and which benefits are guaranteed?",
    "Does the design include meaningful inflation protection?",
    "Is the claim benefit reimbursement, cash indemnity, or disability-style indemnity?",
    "Are informal caregivers, family caregivers, international care, home modifications, or care "
    "coordination covered?",
    "What is the elimination period, and is it based on calendar days or service days?",
    "Is the rider qualified long-term care under Internal Revenue Code Section 7702B, or is it a "
    "chronic-illness rider with different definitions and tax treatment?",
    "What happens to the death benefit, cash value, surrender value, and beneficiaries after LTC "
    "benefits are used?",
    "How strong is the carrier, and how does the state guaranty association apply?",
])}

<h2 id="providers">Representative providers and product categories</h2>
<p>The following table is educational, not exhaustive, and is not a ranking or endorsement.
Product availability, underwriting, state approval, riders, and marketing names change. Consumers
should use current carrier-approved materials and compare multiple solutions.</p>
{table(
    ["Provider / brand", "General category", "Notable design feature described by provider"],
    [["CareScout / Genworth", "Traditional stand-alone",
      "Genworth reported the new CareScout stand-alone product was live in 41 states as of "
      "March 31, 2026."],
     ["Mutual of Omaha", "Traditional stand-alone",
      "Dedicated LTC coverage with selectable benefits, elimination periods, and policy limits."],
     ["National Guardian Life", "Traditional stand-alone",
      "Stand-alone LTC focus; features and availability vary by state."],
     ["Thrivent", "Traditional and combination",
      "Offers dedicated LTC and a life/LTC combination approach."],
     ["OneAmerica", "Life/LTC and annuity/LTC",
      "Whole-life and annuity foundations; optional lifetime benefit features in certain designs."],
     ["Nationwide", "Life/LTC and annuity/LTC",
      "Cash-indemnity approach with no monthly bills or receipts after claim approval, subject to "
      "contract terms."],
     ["Lincoln Financial", "Life/LTC linked benefit",
      "Universal and variable universal life policies with LTC riders."],
     ["Securian Financial", "Life/LTC linked benefit",
      "Whole-life linked-benefit design with cash-indemnity LTC and return-of-premium options."]],
)}

<h2 id="framework">A practical consumer decision framework</h2>
<p>A sound long-term care review should answer these questions in order.</p>
<ol class="list list--plain" style="padding-left:1.2rem;list-style:decimal">
<li><strong>Care preference.</strong> Where would I prefer to receive care, and who would I want
involved?</li>
<li><strong>Family impact.</strong> What would caregiving mean for a spouse, children, work,
health, and relationships?</li>
<li><strong>Financial exposure.</strong> How many years of local care costs could my income and
assets absorb?</li>
<li><strong>Coverage objective.</strong> Do I want to cover the full cost, a catastrophic tail
risk, or only part of the monthly cost?</li>
<li><strong>Funding source.</strong> Ongoing premium, limited-pay premium, cash, securities, life
insurance, annuity, IRA, home equity, or a combination?</li>
<li><strong>Benefit design.</strong> Monthly amount, duration, inflation, elimination period,
home-care provisions, shared benefits, indemnity versus reimbursement, and residual value.</li>
<li><strong>Tax and legal review.</strong> Section 7702B status, Section 1035 eligibility,
qualified-account taxation, business deductions where applicable, Medi-Cal planning, ownership,
and beneficiaries.</li>
<li><strong>Carrier review.</strong> Financial strength, product history, claims process, rate
history for traditional products, and state approval.</li>
</ol>

<h2 id="california">California-specific considerations</h2>
<p>California care costs are generally above national medians in several major categories.
California also maintains the California Partnership for Long-Term Care. Partnership-approved
policies must meet state standards and can provide a Medi-Cal asset disregard based on qualifying
benefits paid, subject to program rules and future eligibility requirements.</p>
{note("An important California distinction",
      "<p>A California Partnership policy and an asset-based or linked-benefit policy are not "
      "automatically the same thing. Verify whether a specific contract is Partnership-approved and "
      "whether it qualifies for Medi-Cal asset protection.</p>")}

<h2>Conclusion</h2>
<p>The long-term care market has evolved because family needs, care settings, insurer experience,
and consumer priorities have changed. Traditional insurance can still provide efficient, dedicated
risk transfer, particularly for applicants who want a defined benefit pool and can sustain future
premiums. However, new-sales data show that life/LTC combination coverage has become the dominant
private-market solution, while annuity/LTC products are a smaller but rapidly growing segment. The
industry moved in this direction to address the central weaknesses consumers associated with older
stand-alone coverage: possible class-wide premium increases, a use-it-or-lose-it perception, and
limited value if no claim occurs. Asset-based plans often require a larger upfront or limited-pay
commitment, so they are not necessarily cheaper. Their appeal is that the funding can serve more
than one purpose and may provide more predictable contractual value.</p>
<p>The strongest plan is rarely a single product. It is an integrated strategy that identifies care
preferences, protects the family caregiver, estimates local costs, preserves liquidity, coordinates
taxes and estate planning, and uses insurance only where it improves the overall outcome.</p>

<h2 id="references">References</h2>
<ol class="list list--plain" style="padding-left:1.6rem;list-style:decimal;font-size:.95rem">
<li>Administration for Community Living, &ldquo;How Much Care Will You Need?&rdquo;
<a href="https://acl.gov/ltc/basic-needs/how-much-care-will-you-need">acl.gov</a></li>
<li>Medicare.gov, &ldquo;Long-Term Care Coverage.&rdquo;
<a href="https://www.medicare.gov/coverage/long-term-care">medicare.gov</a></li>
<li>CareScout, &ldquo;Cost of Long-Term Care by State, 2025 Cost of Care.&rdquo;
<a href="https://www.carescout.com/cost-of-care">carescout.com</a></li>
<li>CareScout, &ldquo;2025 Cost of Care Data for California,&rdquo; March 2, 2026.</li>
<li>National Association of Insurance Commissioners, &ldquo;Long-Term Care Insurance Rate Increases
and Reduced Benefit Options,&rdquo; 2022.
<a href="https://content.naic.org/insurance-topics/long-term-care-insurance">naic.org</a></li>
<li>California Department of Insurance, &ldquo;Long Term Care Insurance Rate History.&rdquo;
<a href="https://www.insurance.ca.gov/01-consumers/105-type/95-guides/05-health/01-ltc/rate-history.cfm">insurance.ca.gov</a></li>
<li>Internal Revenue Service, Notice 2011-68 / Internal Revenue Bulletin 2011-36, Sections 72,
1035, and 7702B. <a href="https://www.irs.gov/irb/2011-36_IRB">irs.gov</a></li>
<li>Internal Revenue Service, Publication 502, &ldquo;Medical and Dental Expenses.&rdquo;
<a href="https://www.irs.gov/publications/p502">irs.gov</a></li>
<li>California Department of Health Care Services, &ldquo;California Partnership for Long-Term
Care.&rdquo; <a href="https://www.dhcs.ca.gov/services/long-term-care-alternatives-home-and-community-based-service-options/the-california-partnership-for-long-term-care/">dhcs.ca.gov</a></li>
<li>EY and LIMRA, &ldquo;Hybrid Insurance on the Rise: A New Era for Long-Term Care
Protection,&rdquo; 2026, using LIMRA 2024 Annual Individual Long-Term Care Sales Survey and 2024
Annual Combination Product Sales and In-Force Survey data.
<a href="https://www.ey.com/en_us/insights/insurance">ey.com</a></li>
<li>American Association for Long-Term Care Insurance, &ldquo;2025 Long-Term Care Insurance Facts,
Data, Prices and Statistics,&rdquo; 2025 Price Index.
<a href="https://www.aaltci.org/long-term-care-insurance/learning-center/ltcfacts-2025.php">aaltci.org</a></li>
<li>LIMRA, &ldquo;Should Annuity/LTC Products Be a Bigger Part of the Conversation?&rdquo;
November 24, 2025. <a href="https://www.limra.com/">limra.com</a></li>
</ol>

<h2>Educational and legal disclosures</h2>
<p>This publication is intended for general public education and nonprofit resource use. It is not
tax, legal, investment, medical, insurance, Medicaid/Medi-Cal, or fiduciary advice. It is not an
offer or solicitation for any insurance product. Carrier and product references are illustrative
and do not imply endorsement. Product availability, state approval, underwriting, pricing, policy
forms, riders, financial ratings, and tax treatment may change. Market-share figures describe
new-policy counts in the cited surveys and should not be interpreted as market share of all
in-force policies, premium, assets, benefits, or covered lives. Pricing examples are planning
benchmarks rather than quotes.</p>
<p>Insurance guarantees depend on the claims-paying ability of the issuing insurance company.
Long-term care benefits are subject to eligibility requirements, exclusions, limitations,
elimination periods, policy maximums, and contract definitions. Life insurance loans, withdrawals,
and accelerated benefits may reduce cash value and death benefit and may create tax consequences.
Annuities may have surrender charges and tax consequences. A Section 1035 exchange must satisfy
legal requirements and generally should be completed directly between carriers.</p>"""

    body = pagehead(
        "White paper · 2026",
        "Planning for long-term care in a changing insurance market",
        "Costs, coverage options, provider landscape, and asset-based strategies. Prepared by "
        "Tri-Valley LTC for nonprofit consumer education.",
    ) + f"""<section class="band">
<div class="shell layout">
{rail("Contents", WP_SECTIONS, None)}
<div class="prose">{prose}</div>
</div>
</section>"""

    return page(
        "white-paper.html",
        "2026 white paper: planning for long-term care",
        "A nonprofit consumer-education white paper on long-term care costs, how the insurance "
        "market changed, asset-based and linked-benefit strategies, and California considerations.",
        body,
    )


def build(**_):
    return [_help(), _faq(), _white_paper()]
