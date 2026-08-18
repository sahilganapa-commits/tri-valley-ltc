"""About us — mission, vision, who we serve, what we do, and the leadership.

Content supplied by the program (Tri-Valley LTC | Website Content). Headshots
are not supplied yet, so each card reserves the space and shows the person's
initials; dropping a photograph in later cannot shift the layout.
"""

from layout import asset_version, cta, esc, page, pagehead, record, ul

CO_FOUNDERS = [
    ("Dr. Sherry Hu, CFP®", "Co-Founder",
     "Dr. Sherry Hu is a Certified Financial Planner™ professional, entrepreneur, and Tri-Valley "
     "community leader who serves as Mayor of the City of Dublin and previously served as a Dublin "
     "City Councilmember. Through her financial planning practice, she has extensive experience "
     "helping families prepare for retirement, long-term care, insurance, and financial security. "
     "She co-founded Tri-Valley LTC to help families understand the financial side of long-term "
     "care and prepare for future care needs before a crisis occurs."),

    ("Dominic Scotto", "Co-Founder",
     "Dominic Scotto is President of From The Heart, a Bay Area caregiver referral agency serving "
     "families since 2002, with a prior career in health insurance and employee benefits and later "
     "in technology product leadership. He helped create Tri-Valley LTC to give families clear, "
     "practical guidance on arranging and paying for care before a crisis forces the decision."),
]

STUDENT_LEADERS = [
    ("Milo Takemoto", "Student Community Leader",
     "Milo Takemoto is a Tri-Valley student and community leader with interests in public policy, "
     "global health, social entrepreneurship, and community service. He has participated in youth "
     "research, policy, nonprofit, and local business advocacy projects. At Tri-Valley LTC, Milo "
     "supports community outreach and helps share long-term care information and resources with "
     "local families."),

    ("Sahil Ganapa", "Technology and Student Community Leader",
     "Sahil Ganapa is a student technology leader with experience in artificial intelligence, "
     "machine learning, website development, assistive technology, and technology research. He is "
     "also the founder of California STEM Innovators. At Tri-Valley LTC, Sahil supports "
     "technology-related work, digital resources, and community outreach to help make long-term "
     "care information more accessible."),
]

PEOPLE = CO_FOUNDERS + STUDENT_LEADERS


def _initials(name):
    """Skip honorifics and post-nominals so 'Dr. Sherry Hu, CFP®' reads SH."""
    parts = [p.strip(",") for p in name.split()
             if not p.endswith(".") and not p.rstrip(",").isupper()]
    return "".join(p[0] for p in parts[:2]).upper()


def people_cards(people=None, heading_level=3):
    """Profile cards. Shared with the home page so the biographies live in
    exactly one place and cannot drift apart between the two."""
    h = f"h{heading_level}"
    cards = []
    for name, role, bio in (PEOPLE if people is None else people):
        cards.append(
            '<article class="person person--profile">'
            f'<p class="person__photo" aria-hidden="true">{esc(_initials(name))}</p>'
            '<div class="person__text">'
            f'<{h} class="person__name">{esc(name)}</{h}>'
            f'<p class="person__role">{esc(role)}</p>'
            f'<p class="person__bio">{esc(bio)}</p>'
            "</div></article>"
        )
    return f'<div class="people people--profiles">{"".join(cards)}</div>'


def build(**_):
    body = pagehead(
        "",
        "About us",
        "Who we are, who we serve, and how we help families approach long-term care with "
        "knowledge and preparation.",
    ) + f"""<section class="band">
<div class="shell">
<div class="prose" style="max-width:72ch">

<h2>Mission</h2>
<p>Tri-Valley LTC empowers families to plan for, understand, and navigate long-term care with
confidence. We provide trusted education, practical resources, and community support to help
families understand long-term care options, prepare financially, access appropriate care, and
make informed decisions throughout the aging journey.</p>

<h2>Vision</h2>
<p>A community where every family can approach long-term care with knowledge, preparation,
dignity, and peace of mind.</p>

<h2>Who we serve</h2>
{ul([
    "Adults planning for their future care needs",
    "Families caring for aging parents or loved ones",
    "Individuals currently facing long-term care decisions",
    "Caregivers seeking reliable information and resources",
    "Community members who want to understand long-term care before a crisis occurs",
])}
<p>Our primary focus is the Tri-Valley community, with resources that may also benefit families
beyond the region.</p>
</div>

<h2 class="band__standalone">What we do</h2>
<p class="band__standalone-note">Tri-Valley LTC organizes its work around four areas.</p>
{record([
    ("Learn",
     "<p>Provide educational information about aging, long-term care, home care, assisted living, "
     "memory care, skilled nursing, insurance, government programs, caregiving, and related "
     "resources.</p>"),
    ("Plan",
     "<p>Help families understand the financial dimensions of long-term care, including potential "
     "costs, insurance options, personal resources, and strategies for preparing before care is "
     "needed.</p>"),
    ("Navigate",
     "<p>Help families understand what to do when long-term care is needed, including evaluating "
     "care options, understanding benefits, communicating with appropriate organizations, and "
     "locating care resources.</p>"),
    ("Connect",
     "<p>Build a trusted network of community resources, care providers, financial professionals, "
     "senior organizations, volunteers, students, and other partners serving individuals and their "
     "families.</p>"),
])}
</div>
</section>

<section class="band band--card">
<div class="shell">
<div class="band__head">
<h2>Our leadership</h2>
<p>Tri-Valley LTC brings together community, care, financial, and technology experience to
provide families with practical long-term care education and resources.</p>
</div>

<figure class="teamphoto">
<img src="assets/leadership.jpg?v={asset_version('leadership.jpg')}"
alt="The four members of Tri-Valley Long Term Care standing side by side with their hands joined,
beneath a wall sign reading Tri-Valley Long Term Care.">
</figure>

<h3 class="people__group">Co-founders</h3>
{people_cards(CO_FOUNDERS, heading_level=4)}

<h3 class="people__group">Student community leaders</h3>
<p class="people__groupnote">Our student community leaders support outreach, share educational
information with the community, and help make long-term care resources easier to access.</p>
{people_cards(STUDENT_LEADERS, heading_level=4)}
</div>
</section>

{cta("Have a question for us?",
     "Tell us where your family is in the process and we will point you to the right next step. "
     "No obligation, and never a sales call.")}"""

    return page(
        "about.html",
        "About us",
        "The mission, vision, and leadership of Tri-Valley LTC — a nonprofit helping Tri-Valley "
        "families understand, plan for, and navigate long-term care.",
        body,
    )
