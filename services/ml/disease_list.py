"""
Disease definitions with weighted symptom probabilities.
Probability:
1.0 = Almost always present
0.8 = Very common
0.5 = Sometimes
0.2 = Rare
"""

DISEASES = {

    "Common Cold":{

        "symptoms":{

            "cough":0.9,
            "runny nose":0.95,
            "sore throat":0.8,
            "sneezing":0.9,
            "fever":0.4,
            "fatigue":0.3

        }

    },

    "Influenza":{

        "symptoms":{

            "fever":0.95,
            "body pain":0.9,
            "fatigue":0.9,
            "headache":0.7,
            "cough":0.8,
            "sore throat":0.5

        }

    },

    "COVID-19":{

        "symptoms":{

            "fever":0.85,
            "dry cough":0.9,
            "fatigue":0.8,
            "loss of taste":0.7,
            "shortness of breath":0.6,
            "headache":0.5

        }

    },

    "Migraine":{

        "symptoms":{

            "headache":0.98,
            "nausea":0.7,
            "vomiting":0.5,
            "light sensitivity":0.8

        }

    },

    "Hypertension":{

        "symptoms":{

            "headache":0.4,
            "dizziness":0.5,
            "blurred vision":0.4

        }

    },

    "Bronchitis":{

        "symptoms":{

            "cough":0.95,
            "chest pain":0.6,
            "fatigue":0.5,
            "shortness of breath":0.5

        }

    },

    "Pneumonia":{

        "symptoms":{

            "fever":0.95,
            "cough":0.9,
            "difficulty breathing":0.8,
            "chest pain":0.7,
            "fatigue":0.6

        }

    },

    "Asthma":{

        "symptoms":{

            "wheezing":0.95,
            "shortness of breath":0.9,
            "chest tightness":0.8,
            "cough":0.6

        }

    },

    "Gastroenteritis":{

        "symptoms":{

            "vomiting":0.9,
            "diarrhea":0.95,
            "abdominal pain":0.8,
            "nausea":0.8,
            "fever":0.4

        }

    },

    "Allergic Rhinitis":{

        "symptoms":{

            "runny nose":0.95,
            "sneezing":0.95,
            "itchy eyes":0.85,
            "sore throat":0.3

        }

    }

}