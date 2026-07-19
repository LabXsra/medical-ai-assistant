SEVERITY={

"mild":"LOW",

"slight":"LOW",

"moderate":"MEDIUM",

"severe":"HIGH",

"extreme":"CRITICAL",

"unbearable":"CRITICAL"

}


def extract_severity(text):

    text=text.lower()

    for word,level in SEVERITY.items():

        if word in text:

            return level

    return "UNKNOWN"