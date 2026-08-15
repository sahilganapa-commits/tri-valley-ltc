"""About us — the people behind the program.

Headshots are not supplied yet. Each card reserves the space and shows the
person's initials, so the page is presentable now and a photograph drops in
later without the layout shifting.
"""

from layout import cta, esc, page, pagehead

PEOPLE = [
    ("Dr. Sherry Hu", "Co-founder",
     "Dr. Sherry Hu is a retirement-planning professional, nonprofit founder, community leader, "
     "and Mayor of Dublin, California. After seeing many families struggle to understand and "
     "prepare for long-term care, she helped create this program to make reliable information and "
     "local resources easier to access."),

    ("Dominic Scotto", "Co-founder",
     "Dominic Scotto is President of From The Heart, a Bay Area caregiver referral agency serving "
     "families since 2002, with a prior career in health insurance and employee benefits and later "
     "in technology product leadership. He helped create this program to give families clear, "
     "practical guidance on arranging and paying for care before a crisis forces the decision."),

    ("Amanda Scotto", "Co-founder",
     "Amanda Scotto is a digital marketing professional, founder of Diablo Valley Marketing, and a "
     "leader at From the Heart Home Care, where she helps connect families with trusted care "
     "resources and support throughout the Bay Area. She is passionate about making complex senior "
     "care information easy to understand and accessible for seniors, families, and caregivers."),

    ("Milo Takemoto", "Co-founder",
     "Milo is a local high school student, researcher at a leading energy think tank, founder of a "
     "Tri-Valley nonprofit consulting firm, and an internationally ranked Ethics Bowl competitor. "
     "With relatives facing neurodegenerative disease, Milo joined Tri-Valley LTC to ensure seniors "
     "understand long-term care costs before any crisis."),

    ("Sahil Ganapa", "Co-founder",
     "Sahil is a student at Foothill High School with a strong interest in computer science and UX "
     "design. He is a five-time hackathon winner and the founder of California STEM Innovators, an "
     "organization dedicated to expanding STEM knowledge through webinars, hackathons, and "
     "workshops. He works as the lead website developer behind the website for Tri-Valley Long "
     "Term Care."),
]


def _initials(name):
    """Drop the honorific so 'Dr. Sherry Hu' reads SH rather than DS."""
    parts = [p for p in name.split() if not p.endswith(".")]
    return "".join(p[0] for p in parts[:2]).upper()


def people_cards(heading_level=2):
    """The five profile cards. Shared with the home page so the biographies
    live in exactly one place and cannot drift apart."""
    h = f"h{heading_level}"
    cards = []
    for name, role, bio in PEOPLE:
        cards.append(
            '<article class="person person--profile">'
            f'<p class="person__photo" aria-hidden="true">{esc(_initials(name))}</p>'
            '<div class="person__text">'
            f'<{h} class="person__name">{esc(name)}</{h}>'
            f'<p class="person__role">{role}</p>'
            f'<p class="person__bio">{esc(bio)}</p>'
            "</div></article>"
        )
    return f'<div class="people people--profiles">{"".join(cards)}</div>'


def build(**_):
    body = pagehead(
        "",
        "About us",
        "A nonprofit community program, built by people who watched their own families work "
        "through these decisions.",
    ) + f"""<section class="band">
<div class="shell">
<div class="prose" style="max-width:72ch">
<p>The Tri-Valley Long Term Care Resource Program was created because long-term care decisions
arrive confusing, expensive, and usually all at once. Between us we have worked in retirement
planning, health insurance, home care, local government, marketing, and technology — and each of
us has watched a family try to work this out under pressure, without a clear place to start.</p>
<p>Everything on this site is free. We do not sell insurance, care, or placement services, and we
accept no referral fees from the providers in our
<a href="directory.html">directory</a>.</p>
</div>

{people_cards()}
</div>
</section>

{cta("Have a question for us?",
     "Tell us where your family is in the process and we will point you to the right next step. "
     "No obligation, and never a sales call.")}"""

    return page(
        "about.html",
        "About us",
        "The people behind the Tri-Valley Long Term Care Community Program — a nonprofit "
        "helping Tri-Valley seniors and families understand and plan for long-term care.",
        body,
    )
