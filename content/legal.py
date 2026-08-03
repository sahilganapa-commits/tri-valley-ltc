"""Privacy policy and accessibility statement.

Both are drafts for legal review, and say so — a nonprofit publishing a
privacy policy it has not had reviewed is worse than publishing none.
"""

from layout import DISCLAIMER, PROGRAM_EMAIL, VERIFIED, note, page, pagehead, record, ul

REVIEW = note(
    "Draft pending legal review",
    "<p>This page was drafted from the program&rsquo;s stated practices and has not yet been "
    "reviewed by counsel. Have it reviewed before launch, and update it whenever the site starts "
    "collecting information it does not collect today.</p>",
    "plain",
)


def _privacy():
    body = pagehead(
        "Privacy",
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
    "To route your inquiry to a licensed professional — but only one you selected, and only with "
    "your consent.",
    "To understand, in aggregate, which pages families find useful.",
])}

<h2>Who we share it with</h2>
<p>We share your inquiry with a licensed professional only when you have consented and only with
the professional you selected. Any professional you are referred to operates a separate business
with its own privacy practices, and provides its own disclosures about services, licensing,
affiliations, fees, and compensation before any engagement begins.</p>
<p>We also use ordinary service providers — a website host and an email service — that process
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
        "Accessibility",
        "Accessibility statement",
        "This site is built for people reading it on a phone in a hospital corridor, and for "
        "people who need larger text than the average website provides. Both matter to us.",
    ) + f"""<section class="band">
<div class="shell">
<div class="prose">
{REVIEW}

<h2>What we aim for</h2>
<p>We aim to meet the Web Content Accessibility Guidelines (WCAG) 2.1 at Level AA. That is a
standard, not a certificate — if something on this site does not work for you, we want to hear
about it and fix it.</p>

<h2>What we have built in</h2>
{record([
    ("Readable type",
     "<p>Body text starts at 17 to 18 pixels and scales up with your browser or system settings, "
     "with generous line spacing. Nothing here uses the small grey type common on financial "
     "websites.</p>"),
    ("Colour contrast",
     "<p>Text meets or exceeds WCAG AA contrast ratios against its background. Colour is never the "
     "only way information is conveyed.</p>"),
    ("Keyboard navigation",
     "<p>Every link, button, form field, and filter can be reached and operated with a keyboard, "
     "and the focus indicator is always visible. A &ldquo;skip to content&rdquo; link is the first "
     "thing you reach on each page.</p>"),
    ("Screen readers",
     "<p>Pages use real headings, landmarks, lists, and tables with row and column headers, so a "
     "screen reader can navigate the structure rather than reading everything top to bottom.</p>"),
    ("Reduced motion",
     "<p>If your device is set to reduce motion, the small entrance animations do not play.</p>"),
    ("Works without JavaScript",
     "<p>Every directory listing is present in the page itself. With JavaScript disabled you lose "
     "the search and filters, not the information.</p>"),
    ("Printable",
     "<p>Every page prints cleanly, and checklists print with your answers filled in — useful for "
     "a doctor&rsquo;s appointment or a call with a carrier.</p>"),
    ("Tables on small screens",
     "<p>Wide tables scroll horizontally within their own frame, so the page itself never scrolls "
     "sideways.</p>"),
])}

<h2>Known gaps</h2>
{ul([
    "This site is currently available in English only. Language access is a priority for the next "
    "phase; in the meantime, the Alameda County ADRC provides free multilingual navigation at "
    "<a href=\"https://alameda.my-adrc.org/\">alameda.my-adrc.org</a> or by dialling 2-1-1.",
    "Documents and links on other organizations&rsquo; websites are outside our control and may "
    "not meet the same standard.",
    "This statement reflects our own testing. A full independent audit has not yet been "
    "commissioned.",
])}

<h2>Tell us what is not working</h2>
<p>If any part of this site is difficult to use, email
<a href="mailto:{PROGRAM_EMAIL}">{PROGRAM_EMAIL}</a> with the page and what happened. We treat
accessibility problems as bugs, not as feature requests, and we will also give you the information
you were looking for by another route while we fix it.</p>
</div>
</div>
</section>"""

    return page(
        "accessibility.html",
        "Accessibility statement",
        "How this site supports readable type, keyboard navigation, screen readers, reduced "
        "motion, and printing — and the gaps we are still working on.",
        body,
    )


def build(**_):
    return [_privacy(), _accessibility()]
