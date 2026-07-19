import pandas as pd


def create_feature_vector(age, symptoms):

    feature = {
        "light sensitivity": 0,
        "age": age,

        "fever": 0,

        "cough": 0,

        "dry cough": 0,

        "runny nose": 0,

        "sore throat": 0,

        "headache": 0,

        "fatigue": 0,

        "body pain": 0,

        "loss of taste": 0,

        "shortness of breath": 0,

        "nausea": 0,

        "vomiting": 0,

        "diarrhea": 0,

        "abdominal pain": 0,

        "dizziness": 0,

        "blurred vision": 0,

        "chest pain": 0,

        "difficulty breathing": 0,

        "wheezing": 0,

        "chest tightness": 0,

        "sneezing": 0,

        "itchy eyes": 0

    }

    for symptom in symptoms:

        symptom = symptom.lower()

        if symptom in feature:

            feature[symptom] = 1

    return pd.DataFrame([feature])