# ==========================================================
# Symptom Normalizer
# ==========================================================

SYMPTOM_MAP = {

    # ------------------------------------------------------
    # Fever
    # ------------------------------------------------------

    "fever": "fever",
    "high fever": "fever",
    "low fever": "fever",
    "temperature": "fever",
    "pyrexia": "fever",

    # ------------------------------------------------------
    # Cough
    # ------------------------------------------------------

    "cough": "cough",
    "dry cough": "dry cough",
    "wet cough": "productive cough",
    "productive cough": "productive cough",

    # ------------------------------------------------------
    # Sore throat
    # ------------------------------------------------------

    "sore throat": "sore throat",
    "throat pain": "sore throat",
    "painful throat": "sore throat",
    "pharyngitis": "sore throat",

    # ------------------------------------------------------
    # Runny nose
    # ------------------------------------------------------

    "runny nose": "runny nose",
    "running nose": "runny nose",
    "nasal discharge": "runny nose",
    "rhinorrhea": "runny nose",

    # ------------------------------------------------------
    # Nasal congestion
    # ------------------------------------------------------

    "blocked nose": "nasal congestion",
    "stuffy nose": "nasal congestion",
    "nasal congestion": "nasal congestion",

    # ------------------------------------------------------
    # Sneezing
    # ------------------------------------------------------

    "sneeze": "sneezing",
    "sneezing": "sneezing",

    # ------------------------------------------------------
    # Headache
    # ------------------------------------------------------

    "headache": "headache",
    "head pain": "headache",
    "migraine": "migraine",

    # ------------------------------------------------------
    # Light sensitivity
    # ------------------------------------------------------

    "light sensitivity": "light sensitivity",
    "photophobia": "light sensitivity",

    # ------------------------------------------------------
    # Body pain
    # ------------------------------------------------------

    "body pain": "body aches",
    "body ache": "body aches",
    "muscle pain": "muscle aches",
    "muscle ache": "muscle aches",
    "myalgia": "muscle aches",

    # ------------------------------------------------------
    # Fatigue
    # ------------------------------------------------------

    "fatigue": "fatigue",
    "tired": "fatigue",
    "tiredness": "fatigue",
    "weakness": "fatigue",
    "exhaustion": "fatigue",

    # ------------------------------------------------------
    # Chills
    # ------------------------------------------------------

    "chills": "chills",
    "shivering": "chills",

    # ------------------------------------------------------
    # Shortness of breath
    # ------------------------------------------------------

    "shortness of breath": "shortness of breath",
    "breathlessness": "shortness of breath",
    "difficulty breathing": "shortness of breath",
    "dyspnea": "shortness of breath",

    # ------------------------------------------------------
    # Chest pain
    # ------------------------------------------------------

    "chest pain": "chest pain",
    "pain in chest": "chest pain",

    # ------------------------------------------------------
    # Wheezing
    # ------------------------------------------------------

    "wheezing": "wheezing",
    "wheeze": "wheezing",

    # ------------------------------------------------------
    # Nausea
    # ------------------------------------------------------

    "nausea": "nausea",
    "queasy": "nausea",

    # ------------------------------------------------------
    # Vomiting
    # ------------------------------------------------------

    "vomit": "vomiting",
    "vomiting": "vomiting",
    "throwing up": "vomiting",

    # ------------------------------------------------------
    # Diarrhea
    # ------------------------------------------------------

    "diarrhea": "diarrhea",
    "diarrhoea": "diarrhea",

    # WordPiece fragments
    "dia": "diarrhea",
    "##rr": "diarrhea",
    "##hea": "diarrhea",

    # Sometimes tokenizer splits differently
    "diar": "diarrhea",
    "rhea": "diarrhea",

    # ------------------------------------------------------
    # Abdominal pain
    # ------------------------------------------------------

    "abdominal pain": "abdominal pain",
    "abdomen pain": "abdominal pain",
    "stomach pain": "abdominal pain",
    "belly pain": "abdominal pain",

    # ------------------------------------------------------
    # Stomach upset
    # ------------------------------------------------------

    "stomach ache": "abdominal pain",

    # ------------------------------------------------------
    # Dizziness
    # ------------------------------------------------------

    "dizziness": "dizziness",
    "dizzy": "dizziness",
    "vertigo": "dizziness",

    # ------------------------------------------------------
    # Loss of smell
    # ------------------------------------------------------

    "loss of smell": "loss of smell",
    "cannot smell": "loss of smell",
    "anosmia": "loss of smell",

    # ------------------------------------------------------
    # Loss of taste
    # ------------------------------------------------------

    "loss of taste": "loss of taste",
    "cannot taste": "loss of taste",
    "ageusia": "loss of taste",

    # ------------------------------------------------------
    # Hypertension
    # ------------------------------------------------------

    "high blood pressure": "hypertension",
    "hypertension": "hypertension",

    # ------------------------------------------------------
    # Diabetes
    # ------------------------------------------------------

    "high blood sugar": "diabetes",
    "diabetes": "diabetes"

}


# ==========================================================
# Normalize Function
# ==========================================================

def normalize(symptom: str):

    if symptom is None:
        return ""

    symptom = symptom.strip().lower()

    symptom = " ".join(symptom.split())

    return SYMPTOM_MAP.get(symptom, symptom)