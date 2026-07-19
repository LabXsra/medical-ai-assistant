import re


PATTERNS=[

r"\d+\s*day[s]?",

r"\d+\s*week[s]?",

r"\d+\s*month[s]?",

r"since yesterday",

r"since today"

]


def extract_duration(text):

    text=text.lower()

    for pattern in PATTERNS:

        match=re.search(pattern,text)

        if match:

            return match.group()

    return None