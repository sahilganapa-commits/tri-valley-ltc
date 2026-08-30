"""Paying for Care, the financial-planning hub.

Kept deliberately solution-neutral, as the source content plan requires: this
page explains approaches, it does not recommend a product. The carrier-specific
illustration from the source material has been genericised, see README.
"""

from layout import (hero_page, checklist, cta, note, page, pagehead, rail, record,
                    seq, steps, table, ul)

SECTIONS = [
    ("#why", "Why planning matters"),
    ("#cost", "What care may cost"),
    ("#process", "The five-step process"),
    ("#options", "Funding options compared"),
    ("#cases", "Illustrative case studies"),
    ("#questions", "Questions to work through"),
    ("#help", "How this program helps"),
]

READINESS = [
    ("We know where care would be received, if there were a choice", ""),
    ("We know who would make financial decisions if one of us could not", ""),
    ("We have modelled a year of care at local prices against our retirement income", ""),
    ("We know which assets are liquid and available for care", ""),
    ("We know which assets are reserved for the healthy spouse or for family legacy", ""),
    ("We have read any existing life, annuity, or long-term care policies within the last two years", ""),
    ("Our plan accounts for inflation and for care lasting longer than five years", ""),
    ("We have talked with adult children about money, time, or housing expectations", ""),
    ("Beneficiary designations, powers of attorney, and trusts are current and consistent", ""),
]


def build(**_):
    body = hero_page("paying-for-care.jpg",
                   "An older man and a younger man sit together on a sofa, going through paperwork and smiling.",
                   "Paying for the cost of care",
                   "A plan made in advance decides where care is received, how it is paid for, and which assets are protected.",
                   "center 42%") + f"""<section class="band">
<div class="shell layout">
{rail("On this page", SECTIONS, None)}
<div class="prose">

<h2 id="why">Why planning matters</h2>
<p>Someone turning age 65 has almost a <strong>70% chance</strong> of needing some form of
long-term care services and supports during the remainder of life. The duration and intensity
vary widely, and about one in five will need care for more than five years.</p>
<p>Medicare generally does not pay for long-term custodial care. Most non-medical help with
bathing, dressing, transferring, toileting, supervision, and other daily needs must be paid
privately, covered by qualifying insurance, or funded through Medi-Cal after eligibility
requirements are met.</p>
{note("Planning is not the same as buying insurance",
      "<p>It is about creating a coordinated funding strategy that matches the person&rsquo;s "
      "health, family support, assets, income, care preferences, and legacy goals. For many "
      "families the answer involves no new insurance at all.</p>")}

<h2 id="cost">What long-term care may cost</h2>
<p>Costs vary by location, setting, hours of assistance, and the level of medical or cognitive
support required. These are 2025 medians, a starting point for planning, not a quote. Note how
far California runs above the national figures.</p>
{table(
    ["Care setting", "2025 U.S. median", "2025 California median"],
    [["Non-medical caregiver at home, 44 hrs/week", "$80,080", "$91,520"],
     ["Adult day health care", "$24,700", "$24,440"],
     ["Assisted living / residential care", "$74,400", "$82,800"],
     ["Nursing home, semi-private room", "$114,975", "$146,000"],
     ["Nursing home, private room", "$129,575", "$182,135"]],
    caption="Annual medians from the CareScout 2025 Cost of Care Survey. Home care assumes 44 "
            "hours per week; part-time, overnight, and 24-hour needs produce very different totals.",
)}
{note("Use a current calculator before you plan around these",
      "<p>The figures above are national and state medians, not quotes for the Tri-Valley. Check "
      "current local figures at <a href=\"https://www.carescout.com/cost-of-care\">carescout.com/"
      "cost-of-care</a>, and see what each level of care actually includes in "
      "<a href=\"getting-care.html#levels\">the levels of care</a>.</p>", "info")}

<h2 id="process">The five-step planning process</h2>
{steps([
    ("Define care preferences",
     "<p>Where would you prefer to receive care? Who is available to help? How important is "
     "remaining at home, protecting a spouse, or preserving an inheritance? Every later decision "
     "depends on these answers, and they are the ones families most often skip.</p>"),
    ("Estimate the financial exposure",
     "<p>Model part-time home care, full-time home care, assisted living, memory care, and nursing "
     "care. Include inflation, and include the possibility that one spouse needs care while the "
     "other still has normal living expenses.</p>"),
    ("Inventory available resources",
     "<p>Retirement income, Social Security, pensions, annuities, brokerage assets, retirement "
     "accounts, home equity, insurance, HSA balances, family support, and public benefits.</p>"),
    ("Select a funding strategy",
     "<p>Determine which costs will be paid from income, which risks will be insured, which assets "
     "will be reserved for care, and what financial floor must remain for the healthy spouse.</p>"),
    ("Coordinate the plan",
     "<p>Align beneficiary designations, powers of attorney, trusts, tax planning, insurance "
     "ownership, care instructions, and the family communication plan. A plan that is not "
     "coordinated is a collection of documents that contradict each other.</p>"),
])}

<h2 id="options">Funding options compared</h2>
<p>These are presented neutrally. Most families will use a combination rather than a single
solution.</p>
{table(
    ["Approach", "How it works", "Potential strength", "Important limitation"],
    [["Current income and self-funding",
      "Use retirement income, cash, investments, or dedicated reserves.",
      "Maximum flexibility and no underwriting.",
      "Care may require selling assets during poor markets or creating large taxable withdrawals."],
     ["Traditional stand-alone LTC insurance",
      "Pay ongoing premiums for a defined pool of care benefits.",
      "Can provide substantial coverage for each premium dollar.",
      "Premiums may rise, underwriting applies, and unused benefits may not create a legacy."],
     ["Life insurance with LTC benefits",
      "A life policy allows qualifying care benefits to be accelerated or extended.",
      "Can provide care benefits, a death benefit, or both depending on use.",
      "Costs, guarantees, benefit triggers, loan treatment, and policy structure vary."],
     ["Annuity with LTC benefits",
      "An annuity value may be multiplied or enhanced for qualifying care expenses.",
      "May reposition an existing asset and provide value even if care is not needed.",
      "Liquidity, surrender charges, tax treatment, and benefit duration require review."],
     ["California Partnership policy",
      "A qualifying policy provides insurance benefits and Medi-Cal asset protection.",
      "Can protect assets equal to qualifying benefits paid, subject to program rules.",
      "Only specifically approved policies qualify; availability and suitability must be verified."],
     ["Medi-Cal or Medicaid",
      "Public programs may pay for eligible long-term services and supports.",
      "A major source of long-term care funding for eligible individuals.",
      "Financial and functional eligibility rules apply, and care choices may be constrained."],
     ["Home equity",
      "Sale proceeds, downsizing, a home-equity strategy, or a reverse mortgage when appropriate.",
      "May unlock a large household resource.",
      "Can affect housing security, heirs, interest costs, and spouse planning."],
     ["Family caregiving",
      "Relatives provide unpaid or partially paid support.",
      "May preserve familiar care and reduce cash cost.",
      "Creates time, income, health, and relationship costs for caregivers."]],
    caption="No single approach is best. Most durable plans combine several.",
)}
{note("The conclusion worth carrying away",
      "<p>There is no single best way to fund long-term care. The most resilient plans combine "
      "several resources, preserve a financial floor for the healthy spouse, and avoid depending "
      "entirely on one asset, one insurance policy, or one family caregiver.</p>")}

<h2 id="cases">Illustrative case studies</h2>
{note("Read these as illustrations, not offers",
      "<p>These are anonymized and hypothetical, and are provided for educational discussion only. "
      "They are not offers, guarantees, quotes, or recommendations. Actual benefits, premiums, tax "
      "treatment, underwriting, and product availability depend on the individual and the specific "
      "contract. No carrier or product named or implied here is endorsed by this program.</p>",
      "plain")}

<h3>Converting existing retirement assets into lifetime care protection</h3>
{record([
    ("Situation",
     "<p>A married couple, approximately ages 62 and 64, wanted meaningful protection for both "
     "spouses. They were concerned about open-ended care costs and did not want an ongoing premium "
     "that might increase later.</p>"),
    ("Illustrative approach",
     "<p>An asset-based life/LTC illustration repositioned roughly $211,000 of IRA assets under the "
     "carrier&rsquo;s permitted structure. The illustration included a benefit enhancement and "
     "showed maximum long-term care benefits of roughly $8,300 per month for each spouse, close to "
     "$100,000 per person per year, with a lifetime-benefit option.</p>"),
    ("Planning objective",
     "<p>Transform an existing asset into a larger pool of care benefits while preserving contract "
     "value or a death benefit if care is not fully used.</p>"),
    ("Why it may be useful",
     "<p>The structure can provide fixed premiums, benefits for both spouses, and protection against "
     "a very long claim. It may appeal to families comfortable repositioning assets who still want "
     "value if care is never needed.</p>"),
    ("What to review before acting",
     "<p>The carrier illustration itself, underwriting, benefit triggers, inflation option, claim "
     "method, IRA distribution and tax treatment, required minimum distributions, surrender "
     "provisions, death benefit, and whether the lifetime extension is guaranteed under the "
     "selected contract.</p>"),
])}

<h3>Traditional stand-alone coverage for a healthy couple</h3>
{record([
    ("Situation",
     "<p>A California husband age 64 and wife age 62, both in standard health, wanted to insure a "
     "defined portion of future care costs while keeping most assets invested.</p>"),
    ("Illustrative approach",
     "<p>Compare traditional policies with a meaningful monthly benefit, a three-year benefit "
     "period, a 90-day elimination period, and 3% compound inflation protection. A preliminary "
     "planning estimate is roughly $7,500 to $10,000 per year combined, subject to carrier, health "
     "class, benefits, and underwriting.</p>"),
    ("Why it may be useful",
     "<p>Traditional coverage can provide substantial insurance leverage per premium dollar, and may "
     "suit people who prefer to keep investment and estate assets separate from insurance.</p>"),
    ("What to review before acting",
     "<p>Premium affordability across the full retirement period, carrier rate-increase history, "
     "shared-care options, inflation protection, home-care coverage, nonforfeiture benefits, and the "
     "possibility that no benefit is ever paid.</p>"),
])}
{table(
    ["Illustrative traditional design", "Combined annual premium", "Interpretation"],
    [["Couple both age 60, level benefits", "$2,600", "Lower initial cost, but no automatic benefit growth"],
     ["Couple both age 60, 3% compound growth", "$5,800", "Benefit pool grows annually"],
     ["Couple both age 65, 3% compound growth", "$7,150", "Later purchase age materially increases cost"],
     ["Age-65 couple, similar designs across three carriers", "$7,137 – $12,250",
      "Carrier selection can change cost substantially"]],
    caption="2025 price-index benchmarks for select-health couples with an initial $165,000 benefit "
            "pool per spouse, from the American Association for Long-Term Care Insurance. Benchmarks "
            "are based on Illinois pricing and vary by state and carrier. They are not quotes.",
)}

<h3>Repositioning an existing annuity or conservative asset</h3>
{record([
    ("Situation",
     "<p>A retiree had an existing annuity, certificate of deposit, or conservative reserve not "
     "needed for near-term spending, and wanted to pay for future care without buying life "
     "insurance.</p>"),
    ("Illustrative approach",
     "<p>Evaluate an annuity with long-term care benefits. The annuity value may remain available "
     "under contract terms and may provide an enhanced or extended pool for qualifying care "
     "expenses.</p>"),
    ("What to review before acting",
     "<p>Eligibility for a tax-free exchange, surrender charges, benefit multiplier, elimination "
     "period, reimbursement versus cash benefit, inflation protection, liquidity, beneficiary value, "
     "and tax treatment of withdrawals and care benefits.</p>"),
])}

<h3>A blended plan for a family that can partly self-fund</h3>
{record([
    ("Situation",
     "<p>A financially secure couple could pay for several years of care but worried that a long "
     "claim might reduce the healthy spouse&rsquo;s lifestyle or force the sale of investments "
     "during a poor market.</p>"),
    ("Illustrative approach",
     "<p>Create a dedicated care reserve for the first years of care, add insurance or an "
     "asset-based policy for catastrophic duration, and preserve a separate income and housing floor "
     "for the healthy spouse.</p>"),
    ("Why it may be useful",
     "<p>The family avoids over-insuring smaller costs while transferring the risk that could cause "
     "the most financial damage. It also coordinates investment liquidity, taxes, insurance, and "
     "spouse protection.</p>"),
    ("What to review before acting",
     "<p>Size and location of the reserve, market risk, taxable retirement-account withdrawals, home "
     "equity, inflation, expected family caregiving, estate goals, and the surviving spouse&rsquo;s "
     "minimum income.</p>"),
])}
{note("The planning lesson",
      "<p>Long-term care funding looks complicated because health, taxes, insurance, investments, "
      "family support, and estate planning all interact at once. A qualified professional can help "
      "compare the alternatives and turn those moving parts into one coordinated plan.</p>",
      "plain")}

<h2 id="questions">Questions to work through</h2>
<p>Answer these before you compare any product. If several are unanswered, that is the work to
do first.</p>
{checklist("readiness", "Long-term care financial readiness",
           "<p>A short readiness check. Ticks stay in this browser; print the result and bring it "
           "to a conversation with an adviser, an attorney, or your family.</p>",
           READINESS)}
{ul([
    "Could your retirement plan absorb $75,000 to $180,000 or more per year of care costs?",
    "Would paying for care require large taxable IRA withdrawals, or selling investments during a "
    "market decline?",
    "How would one spouse&rsquo;s care costs affect the other spouse&rsquo;s housing and lifestyle?",
    "Do existing life, annuity, or long-term care policies provide benefits nobody has reviewed "
    "recently?",
    "Are adult children expected to contribute money, time, or housing, and do they know it?",
])}

<h2 id="help">How this program can help</h2>
<p>We provide education, planning tools, and referrals so families can make informed decisions
and coordinate the financial plan with care needs and care-setting choices. We do not sell
insurance, and we are not paid by anyone whose products are described on this page.</p>
{ul([
    "Estimating future care-cost exposure",
    "Reviewing retirement income and available assets",
    "Identifying risks to the healthy spouse",
    "Explaining general funding strategies",
    "Reviewing existing insurance and annuity documents",
    "Helping families prepare questions for licensed professionals",
    "Coordinating referrals to tax advisers, estate-planning attorneys, insurance professionals, "
    "and care managers",
])}
{note("Where a referral goes",
      "<p>With your consent, a financial-planning inquiry may be routed to a licensed professional "
      "you select. That professional provides separate disclosures regarding services, licensing, "
      "affiliations, fees, and insurance compensation before any engagement begins. "
      "<a href=\"help.html\">Send us a message</a> to start.</p>", "info")}

{seq(prev=("using-coverage.html", "Understanding and using your coverage"),
     nxt=("directory.html", "Tri-Valley care directory"))}
</div>
</div>
</section>

{cta("Want a second set of eyes on the numbers?",
     "Tell us what you are trying to work out, whether you can self-fund, how to protect a "
     "spouse, or what an existing policy is actually worth, and we will help you find the right "
     "licensed professional.")}"""

    return page(
        "paying-for-care.html",
        "Paying for the cost of care",
        "Estimate long-term care costs in California, compare funding options, protect a spouse, "
        "and build a coordinated financial plan before care is needed.",
        body,
        overlay=True,
    )
