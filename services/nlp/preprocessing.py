import re
import string

ABBREVIATIONS = {
    "bp": "blood pressure",
    "hr": "heart rate",
    "sob": "shortness of breath",
    "dm": "diabetes mellitus",
    "htn": "hypertension",
    "mi": "myocardial infarction"
}


def expand_abbreviations(text):

    words = text.split()

    expanded = []

    for word in words:

        key = word.lower()

        expanded.append(
            ABBREVIATIONS.get(key, word)
        )

    return " ".join(expanded)


def remove_extra_spaces(text):

    return re.sub(r"\s+", " ", text)


def clean_text(text):

    text = text.lower()

    text = expand_abbreviations(text)

    text = remove_extra_spaces(text)

    return text.strip()