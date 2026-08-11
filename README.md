# Tri-Valley Long Term Care — Community Program website

A 16-page static site built from the planning materials in
`Tri-Valley LTC Website Planning 3/`.

```
python3 build.py      # writes site/
open site/index.html  # no server needed
```

No dependencies beyond Python 3. The `site/` folder is committed, so you can
upload it to any static host (or lift the markup into Squarespace) without
running the build at all.

## Layout

| Path | What it is |
| --- | --- |
| `build.py` | Entry point. Clears `site/`, copies assets, renders pages. |
| `layout.py` | Shared shell — header, nav, footer, cookie banner, disclaimers — plus the content components (`record`, `note`, `table`, `checklist`, `steps`, `rail`). |
| `content/` | Page copy, one module per section of the site. |
| `data/*.json` | Directory, family questions, and regulatory links, extracted from the source spreadsheets. |
| `assets/` | `styles.css`, `site.js`, `logo.svg`. |
| `site/` | Build output. Do not edit by hand — it is regenerated. |

To change wording, edit the module in `content/` and rebuild. To change the
nav, edit `NAV` in `layout.py` — it updates every page at once.

## Pages

**The guide** — `index.html`, `getting-care.html`, `using-coverage.html` plus
six numbered section pages, `paying-for-care.html`, `directory.html`.

**Everything else** — `help.html`, `faq.html`, `white-paper.html`,
`privacy.html`, `accessibility.html`.

This maps the Phase 1 outline (Getting LTC / Using LTC / Care Directory,
plus privacy, cookie consent, accessibility, disclaimers) onto the five
sections named in the homepage document, and folds in the financial-planning
and white-paper content.

## Where the content came from

| Source file | Used for |
| --- | --- |
| `Homepage.docx` | Home page structure, founders, program description |
| `Tri-Valley LTC Program.pdf` | Phase 1 page outline, directory requirements, legal/accessibility scope |
| `Webpage mockups with copy review.zip` | The six "using your coverage" sections and the contact page — copy carried over close to verbatim |
| `Long_Term_Care_Financial_Planning_Webpage_Content_Revised.docx` | `paying-for-care.html`, FAQ, referral workflow and disclosures |
| `Long_Term_Care_Industry_White_Paper_2026_Revised.docx` | `white-paper.html` |
| `Tri-Valley_Senior_Care_Resource_Directory_2026.xlsx` | All 38 directory listings, family tour questions, regulatory links |
| `TVLTC_Logo_Concepts_v3.pdf` | Logo and brand colours |

`resource directorycontacts.xlsx` is a subset of the 2026 directory workbook,
so the workbook was used as the single source.

## Design

Colours come from the v3 logo: navy `#26295b`, mid blue `#5c7fc0`, pale blue
`#b9cff2`, gold `#b08d2e`, on a cool paper `#f1f4fa`. Newsreader for display,
Public Sans for body (the same face the US federal design system uses — this
site sits next to medicare.gov and dhcs.ca.gov in a reader's journey), IBM
Plex Mono for data.

The mockups used a green-and-cream palette; that was superseded by the v3
logo, so the structure and copy were kept and the palette was moved onto the
brand.

The recurring device is a **record row** — a small-caps label, a hairline
rule, and a value — because the artifacts in this subject's world are records:
policy pages, plans of care, claim logs, tour notes. The whole site is meant
to read like a form somebody already filled in for you.

## Interactive bits

All progressive enhancement — nothing breaks with JavaScript off.

- **Directory** search, city filter, and care-type chips. Every one of the 38
  listings is in the HTML, so without JS you lose the filters, not the data.
- **Checklists** on the daily-activities check, the policy inventory, and the
  financial readiness list. Ticks persist in `localStorage` and print. The
  daily-activities check counts as you go and tells you when you have hit the
  two-of-six threshold that typically triggers a policy.
- **Cookie banner**, remembering the choice.

## Accessibility

Targets WCAG 2.1 AA. Base type 17–18px scaling with user settings, all text
at AA or better, focus rings at 3:1+ on every surface (navy on light, gold on
dark), 44px minimum targets, real landmarks and table headers, skip link,
`prefers-reduced-motion` honoured, wide tables scroll inside their own frame,
and every page prints cleanly.

## Before this goes live

1. **Wire up the forms.** Both the contact form and the white-paper download
   are unconnected and say so on screen. Replace the `data-form` handler in
   `assets/site.js`, or drop the fields into Squarespace form blocks.
2. **Set the program's real email address.** `PROGRAM_EMAIL` in `layout.py` is
   a placeholder (`hello@trivalleyltc.org`) and appears on several pages.
3. **Fill in Dominic Scotto's biography** in `content/home.py`. The source
   document also had an unnamed third co-founder; that slot was left out
   rather than shipped as `[Co-Founder's Name]` — add it back if needed.
4. **Legal review of `privacy.html` and `accessibility.html`.** Both are
   drafts and are labelled as such on the page.
5. **Compliance review of the case studies** on `paying-for-care.html`. The
   source document says not to publish carrier-specific illustrations without
   compliance approval and full disclosures, and the white paper says the
   adviser-supplied illustration should be matched against the carrier's
   approved version before publication. The first case study has therefore
   been genericised — the carrier and product names were removed and it reads
   as an illustrative asset-based design. Restore the specifics only with
   sign-off and the required disclosures.
6. **Re-verify the directory.** Listings are marked verified 2026-07-27.
   Re-check before launch and set an annual review, along with the cost
   figures, tax references, and program links.

## Accessibility

Two checkers guard WCAG 2.1 AA. Run both after any visual change, and
especially after swapping a hero photograph:

```bash
python3 tools/check_a11y.py       # markup: headings, labels, landmarks, alt, ids
python3 tools/check_contrast.py   # renders pages and measures text on photos
```

`check_contrast.py` needs the preview server running (`python3 serve.py`). It
hides each piece of text, samples the photograph exactly where that text sits,
and computes contrast against the lightest pixel — the worst case. This cannot
be reasoned about from CSS, because it depends on the image in place. A
brighter sky in a new photo can push the navigation below the threshold with
nothing in the stylesheet changing.

Thresholds: 4.5:1 normal text, 3:1 large display text.

Not covered by either tool, and still outstanding: testing with real screen
readers (VoiceOver, NVDA) and an independent audit. The accessibility
statement says so plainly — keep it that way, and update it when that changes.
