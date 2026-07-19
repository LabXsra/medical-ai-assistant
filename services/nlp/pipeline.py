import re

from .preprocessing import clean_text
from .medical_ner import extract_entities
from .symptom_normalizer import normalize
from .ontology_mapper import map_concept
from .context import analyze_context
from .duration import extract_duration


# ==========================================================
# Biomedical Labels
# ==========================================================

MEDICAL_LABELS = {

    "Sign_symptom",

    "Disease_disorder",

    "Medication",

    "Biological_structure"

}


# ==========================================================
# Medical Phrase Dictionary
# ==========================================================

MEDICAL_PHRASES = {

    "sore throat",

    "runny nose",

    "running nose",

    "blocked nose",

    "stuffy nose",

    "chest pain",

    "body pain",

    "body ache",

    "muscle pain",

    "joint pain",

    "abdominal pain",

    "stomach pain",

    "shortness of breath",

    "difficulty breathing",

    "light sensitivity",

    "loss of smell",

    "loss of taste",

    "dry cough",

    "wet cough",

    "high fever",

    "low fever",

    "high blood pressure",

    "high blood sugar"

}


# ==========================================================
# Age Extraction
# ==========================================================

def extract_age(text):

    text = text.lower()

    patterns = [

        r"age[: ]*(\d+)",

        r"i am (\d+)",

        r"i'm (\d+)",

        r"(\d+)\s*years old",

        r"(\d+)-year-old",

        r"(\d+)\s*y/o"

    ]

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:

            return int(match.group(1))

    return None


# ==========================================================
# Phrase Builder
# ==========================================================

def merge_phrases(text, entities):

    text_lower = text.lower()

    merged = []

    used_words = set()

    # Add predefined phrases

    for phrase in MEDICAL_PHRASES:

        if phrase in text_lower:

            merged.append({

                "text": phrase,

                "label": "Sign_symptom",

                "confidence": 0.99

            })

            for word in phrase.split():

                used_words.add(word)

    # Add transformer entities

    for entity in entities:

        word = entity["text"].lower()

        if word in used_words:

            continue

        merged.append(entity)

    return merged


# ==========================================================
# Analyze Patient
# ==========================================================

def analyze_patient(text):

    cleaned = clean_text(text)

    # -------------------------------------
    # Age
    # -------------------------------------

    age = extract_age(cleaned)

    # -------------------------------------
    # Duration
    # -------------------------------------

    duration = extract_duration(cleaned)

    # -------------------------------------
    # Biomedical NER
    # -------------------------------------

    entities = extract_entities(cleaned)

    # -------------------------------------
    # Merge Clinical Phrases
    # -------------------------------------

    entities = merge_phrases(

        cleaned,

        entities

    )

    results = []

    visited = set()

    for entity in entities:

        if entity["label"] not in MEDICAL_LABELS:

            continue

        name = normalize(entity["text"])

        # Remove duplicates

        if name in visited:

            continue

        visited.add(name)

        # Context

        context = analyze_context(

            cleaned,

            entity["text"]

        )

        # Ontology

        ontology = map_concept(name)

        results.append({

            "name": name,

            "type": entity["label"],

            "present": context["present"],

            "severity": context["severity"],

            "confidence": round(

                float(entity["confidence"]),

                3

            ),

            "ontology": ontology

        })

    # -------------------------------------
    # Final Output
    # -------------------------------------

    return {

        "age": age,

        "duration": duration,

        "symptoms": results

    }