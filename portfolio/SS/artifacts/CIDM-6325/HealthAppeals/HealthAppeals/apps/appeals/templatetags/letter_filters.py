from django import template
import re

register = template.Library()


@register.filter(name="clean_whitespace")
def clean_whitespace(value):
    """
    Removes extra blank lines, trims whitespace,
    and returns a cleaner version of the generated letter.
    """
    if not isinstance(value, str):
        return value

    # Remove multiple blank lines
    cleaned = re.sub(r"\n\s*\n+", "\n\n", value.strip())
    return cleaned


@register.filter(name="sentence_case")
def sentence_case(value):
    """
    Ensures the first letter of the letter is capitalized.
    Useful if the AI returns lowercase starts.
    """
    if not isinstance(value, str) or not value:
        return value
    return value[0].upper() + value[1:]


@register.filter(name="insurer_format")
def insurer_format(value):
    """
    Formats insurance company names consistently:
    - Strips whitespace
    - Title-cases the input
    """
    if not isinstance(value, str):
        return value
    return value.strip().title()
