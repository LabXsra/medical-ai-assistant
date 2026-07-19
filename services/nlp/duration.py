import re


DURATION_PATTERNS = [

    r"for\s+(\d+)\s+(day|days|week|weeks|month|months|year|years)",

    r"since\s+(\d+)\s+(day|days|week|weeks|month|months|year|years)",

    r"(\d+)\s+(day|days|week|weeks|month|months|year|years)",

    r"since yesterday",

    r"since today",

    r"since last night",

    r"since this morning",

    r"yesterday",

    r"today",

    r"last night",

    r"this morning"

]


def extract_duration(text):

    text = text.lower()

    for pattern in DURATION_PATTERNS:

        match = re.search(pattern, text)

        if match:

            return match.group(0)

    return None