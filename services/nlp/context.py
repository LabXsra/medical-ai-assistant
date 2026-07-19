NEGATIONS = {
    "no",
    "not",
    "without",
    "denies",
    "denied",
    "negative"
}

HIGH = {
    "severe",
    "extreme",
    "intense",
    "acute",
    "persistent"
}

MEDIUM = {
    "moderate"
}

LOW = {
    "mild",
    "slight"
}


def analyze_context(text, entity):

    words = text.lower().split()

    entity_words = entity.lower().split()

    for i in range(len(words)):

        if words[i:i+len(entity_words)] == entity_words:

            start = max(0, i-4)
            end = min(len(words), i+len(entity_words)+4)

            window = words[start:end]

            present = True

            severity = "UNKNOWN"

            if any(word in NEGATIONS for word in window):
                present = False

            if any(word in HIGH for word in window):
                severity = "HIGH"

            elif any(word in MEDIUM for word in window):
                severity = "MEDIUM"

            elif any(word in LOW for word in window):
                severity = "LOW"

            return {
                "present": present,
                "severity": severity
            }

    return {
        "present": True,
        "severity": "UNKNOWN"
    }