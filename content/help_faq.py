"""Contact us and the frequently asked questions."""

from layout import (FORM_ENDPOINT, PROGRAM_EMAIL, VERIFIED, faq_list, hero_page, esc, note, page, pagehead,
                    rail, record, table, ul)

FAQS = [
    ("Does Medicare pay for long-term care?",
     "<p>Medicare generally does not pay for custodial long-term care: the ongoing, non-medical "
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
     "sources and providers instead, which is what most of this site covers.</p>"),
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
     "professional. This is not something to work out from a website.</p>"),
    ("What is the California Partnership for Long-Term Care?",
     "<p>A California program involving the state and approved insurers. Qualifying Partnership "
     "policies include consumer protections and may provide Medi-Cal asset protection equal to "
     "qualifying benefits paid, subject to program rules. A Partnership policy and a hybrid or "
     "asset-based policy are not automatically the same thing. Verify whether a specific contract "
     "is Partnership-approved.</p>"),
    ("My carrier stopped selling policies. Is my policy still good?",
     "<p>Yes. A carrier leaving the sales market does not cancel your policy, and claims on existing "
     "policies are still paid, sometimes through a third-party administrator, so the name on your "
     "correspondence may differ from the name on your policy. Do not cancel a legacy policy without "
     "professional advice; older policies often contain benefits that cannot be bought at any price "
     "today.</p>"),
    ("How long does a claim take?",
     "<p>Commonly 60 to 90 days or more between the first phone call and the first benefit payment, "
     "once you account for claim paperwork, the carrier&rsquo;s assessment, and the elimination "
     "period written into the policy. You can begin a claim before choosing a provider, and you "
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
    body = f"""<section class="band">
<div class="shell">
<div class="prose">

<h1>Send us a message</h1>
<form class="form" data-form action="{FORM_ENDPOINT}" method="POST">
<input type="hidden" name="_subject" value="Tri-Valley LTC: contact form">
<input class="form__gotcha" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
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
</form>
<p class="note note--info" data-form-status hidden tabindex="-1" role="status" aria-live="polite"></p>

</div>
</div>
</section>"""

    return page(
        "help.html",
        "Contact us",
        "Ask the Tri-Valley Long Term Care Community Program a question about using a policy, "
        "planning for care costs, or finding local care. Free, nonprofit, and never a sales call.",
        body,
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


def build(**_):
    return [_help(), _faq()]
