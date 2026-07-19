from .medical_dictionary import MEDICAL_PHRASES


def detect_phrases(text):

    found = []

    lower = text.lower()

    for phrase in MEDICAL_PHRASES:

        if phrase in lower:

            found.append({

                "text": phrase,

                "label": "Sign_symptom",

                "confidence": 1.0

            })

    return found