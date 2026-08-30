"""Privacy policy and accessibility statement.

Both are drafts for legal review, and say so. A nonprofit publishing a
privacy policy it has not had reviewed is worse than publishing none.
"""

from layout import (DISCLAIMER, PROGRAM_EMAIL, VERIFIED, esc, note, page, pagehead,
                    record, ul)

REVIEW = note(
    "Draft pending legal review",
    "<p>This page was drafted from the program&rsquo;s stated practices and has not yet been "
    "reviewed by counsel. Have it reviewed before launch, and update it whenever the site starts "
    "collecting information it does not collect today.</p>",
    "plain",
)


def _privacy():
    body = pagehead(
        "",
        "Privacy policy",
        f"How the Tri-Valley Long Term Care Community Program handles information. "
        f"Last updated {VERIFIED}.",
    ) + f"""<section class="band">
<div class="shell">
<div class="prose">
{REVIEW}

<h2>The short version</h2>
{record([
    ("What we collect",
     "<p>Only what you send us: the contents of a contact or download form, and your email address "
     "if you give it.</p>"),
    ("What we do not collect",
     "<p>We do not ask for Social Security numbers, policy numbers, financial account details, or "
     "medical records. Please do not send them through this website.</p>"),
    ("What stays on your device",
     "<p>Checklists you fill in on this site are stored in your own browser and are never "
     "transmitted to us. Clearing your browser data removes them.</p>"),
    ("What we never do",
     "<p>We do not sell, rent, or trade your information, and we do not accept payment from any "
     "provider or professional in exchange for referrals.</p>"),
])}

<h2>Information we collect</h2>
<p><strong>Information you give us.</strong> When you submit a form, we receive what you typed:
typically your name, email address, an optional phone number, your city, the topic you selected,
and your description of your situation. We also record whether you consented to a referral.</p>
<p><strong>Browser storage.</strong> This site stores two things in your browser: your response to
the cookie notice, and the state of any checklist you fill in. Both stay on your device. Neither
is sent to us, and neither identifies you.</p>
<p><strong>Server logs.</strong> Like most websites, our host may record standard technical
information such as IP address, browser type, and pages requested, for security and to keep the
site running.</p>
<p><strong>Fonts.</strong> Typefaces on this site are requested from Google Fonts, which means
Google receives the standard request information described above. If your organization would
rather not have that happen, the fonts can be self-hosted; ask us.</p>

<h2>How we use it</h2>
{ul([
    "To answer your question and follow up about it.",
    "To send you the white paper, if you requested it.",
    "To send occasional program updates, but only if you affirmatively opted in. Every message "
    "includes an unsubscribe link.",
    "To route your inquiry to a licensed professional, but only one you selected, and only with "
    "your consent.",
    "To understand, in aggregate, which pages families find useful.",
])}

<h2>Who we share it with</h2>
<p>We share your inquiry with a licensed professional only when you have consented and only with
the professional you selected. Any professional you are referred to operates a separate business
with its own privacy practices, and provides its own disclosures about services, licensing,
affiliations, fees, and compensation before any engagement begins.</p>
<p>We also use ordinary service providers, a website host and an email service, that process
information on our behalf. Beyond that, we disclose information only if required by law.</p>

<h2>How long we keep it</h2>
<p>We keep inquiry correspondence for as long as needed to help you and to maintain the
program&rsquo;s records, and then delete it. You can ask us to delete your information at any
time.</p>

<h2>Your choices</h2>
{record([
    ("Access, correct, or delete",
     f'<p>Email <a href="mailto:{PROGRAM_EMAIL}">{PROGRAM_EMAIL}</a> and ask. We will respond '
     "within 30 days.</p>"),
    ("Unsubscribe",
     "<p>Use the link in any email, or reply and ask.</p>"),
    ("California residents",
     "<p>California law gives residents rights to know what personal information is collected, to "
     "request deletion, and to not be discriminated against for exercising those rights. We do not "
     "sell personal information as that term is defined under California law.</p>"),
    ("Children",
     "<p>This site is not directed to children under 13, and we do not knowingly collect their "
     "information.</p>"),
])}

<h2>Cookies and similar technology</h2>
<p>This site does not use advertising or tracking cookies. It uses browser local storage for the
two purposes described above. Declining the cookie notice records that choice and nothing else.</p>

<h2>Changes and contact</h2>
<p>If this policy changes materially, we will update the date at the top of this page. Questions
about privacy go to <a href="mailto:{PROGRAM_EMAIL}">{PROGRAM_EMAIL}</a>.</p>

{note("General disclaimer", f"<p>{DISCLAIMER}</p>", "plain")}
</div>
</div>
</section>"""

    return page(
        "privacy.html",
        "Privacy policy",
        "How the Tri-Valley Long Term Care Community Program collects, uses, and protects "
        "information submitted through this website.",
        body,
    )


def _accessibility():
    body = pagehead(
        "",
        "Accessibility statement",
        "What we have tested, what we have not, and how to tell us when something "
        "does not work.",
    ) + f"""<section class="band">
<div class="shell">
<div class="prose">

<h2>The standard we hold ourselves to</h2>
<p>We aim to meet the Web Content Accessibility Guidelines (WCAG) 2.1 at Level AA, the benchmark
used for public websites in the United States. This page describes what we have actually
measured rather than what we hope is true, because a statement you cannot rely on is worse than
no statement at all.</p>
<p>Last tested {esc(VERIFIED)}.</p>

<h2>What we have measured</h2>
{record([
    ("Text contrast",
     "<p>Every heading, paragraph, label, and navigation link has been measured against the exact "
     "background behind it. Where text sits over a photograph, we sample the lightest pixel of the "
     "picture underneath and compute the ratio against that worst case. All text meets at least "
     "4.5:1, and large display text at least 3:1. These checks run again whenever the site is "
     "rebuilt, so a new photograph cannot quietly break them.</p>"),
    ("Readable type",
     "<p>Body text starts at 17 to 18 pixels and grows with your browser or system text-size "
     "setting. Zooming to 200% does not cut anything off.</p>"),
    ("Keyboard use",
     "<p>Every link, button, form field, filter, and expandable question can be reached and "
     "operated from the keyboard alone. The focus indicator is always visible, and measured at "
     "3:1 or better against every surface it appears on. A &ldquo;skip to content&rdquo; link is "
     "the first thing you reach on each page.</p>"),
    ("Structure for screen readers",
     "<p>Each page has one main heading, headings descend in order without skipping levels, and "
     "the page is divided into standard landmarks. Tables carry real row and column headers. "
     "Every image has alternative text. Form fields are joined to their labels.</p>"),
    ("Things that change without reloading",
     "<p>The directory result count, the checklist tally, and form messages are announced to "
     "screen readers when they update, rather than changing silently.</p>"),
    ("Small screens",
     "<p>The site reflows to a single column down to 320 pixels wide with no sideways scrolling. "
     "Wide tables scroll within their own frame so the page itself never does. Tap targets are at "
     "least 44 pixels.</p>"),
    ("Reduced motion",
     "<p>If your device is set to reduce motion, the entrance animations do not play.</p>"),
    ("Without JavaScript",
     "<p>Every directory listing and every question and answer is in the page itself. With "
     "JavaScript switched off you lose the search and filters, not the information.</p>"),
    ("Printing",
     "<p>Every page prints cleanly. Checklists print with your answers filled in, and the "
     "questions print with their answers open.</p>"),
])}

<h2>What we have not done</h2>
<p>Being straightforward about this matters more than sounding finished.</p>
{ul([
    "<strong>No testing with real screen readers yet.</strong> Our checks confirm the markup is "
    "correct; they cannot confirm the experience is good. Testing with VoiceOver and NVDA, and "
    "with people who use them daily, is the next step.",
    "<strong>No independent audit.</strong> Everything described above is our own measurement.",
    "<strong>English only.</strong> Until that changes, the Alameda County ADRC offers free "
    "multilingual help at <a href=\"https://alameda.my-adrc.org/\">alameda.my-adrc.org</a> or by "
    "dialing 2-1-1.",
    "<strong>Other organizations&rsquo; websites.</strong> The directory links out to providers "
    "and agencies we do not control, and those sites may not meet this standard.",
])}

<h2>Tell us what is not working</h2>
<p>If any part of this site is difficult to use, email
<a href="mailto:{PROGRAM_EMAIL}">{PROGRAM_EMAIL}</a> and say which page you were on and what
happened. We treat accessibility problems as faults to be fixed, not as requests to be
considered. We will also get you the information you were after by another route while we
fix it &mdash; you should not have to wait for a code change to get an answer.</p>
</div>
</div>
</section>"""

    return page(
        "accessibility.html",
        "Accessibility statement",
        "What the Tri-Valley Long Term Care site has been tested for against WCAG 2.1 AA, "
        "what has not yet been tested, and how to report a problem.",
        body,
    )


def build(**_):
    return [_privacy(), _accessibility()]
