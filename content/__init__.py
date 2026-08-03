"""Page content for the Tri-Valley Long Term Care site."""

from . import coverage, directory_page, getting_care, help_faq, home, legal, paying


def build(directory, questions, regulatory):
    """Render every page and return the list of files written."""
    ctx = {"directory": directory, "questions": questions, "regulatory": regulatory}

    built = []
    for module in (home, getting_care, coverage, paying, directory_page, help_faq, legal):
        result = module.build(**ctx)
        built.extend(result if isinstance(result, list) else [result])
    return built
