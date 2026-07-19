import os
import joblib

from .feature_engineering import create_feature_vector

# =====================================================
# Paths
# =====================================================

BASE_DIR = os.path.dirname(__file__)

MODEL_DIR = os.path.join(BASE_DIR, "models")

MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
ENCODER_PATH = os.path.join(MODEL_DIR, "label_encoder.pkl")
FEATURE_PATH = os.path.join(MODEL_DIR, "feature_columns.pkl")

# =====================================================
# Load Model
# =====================================================

print("=" * 60)
print("Loading Disease Prediction Model...")
print("=" * 60)

model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)
FEATURE_COLUMNS = joblib.load(FEATURE_PATH)

print("Disease Prediction Model Loaded Successfully!")
print("=" * 60)

# =====================================================
# Disease Knowledge Base
# =====================================================

DISEASE_INFO = {

    "Common Cold": {
        "description": "A mild viral infection affecting the nose and throat.",
        "specialist": "General Physician"
    },

    "Influenza": {
        "description": "A viral respiratory infection causing fever, cough and body pain.",
        "specialist": "General Physician"
    },

    "COVID-19": {
        "description": "A contagious respiratory illness caused by SARS-CoV-2.",
        "specialist": "Infectious Disease Specialist"
    },

    "Migraine": {
        "description": "A neurological disorder causing recurrent headaches.",
        "specialist": "Neurologist"
    },

    "Hypertension": {
        "description": "Persistently elevated blood pressure.",
        "specialist": "Cardiologist"
    },

    "Bronchitis": {
        "description": "Inflammation of the bronchial tubes causing cough.",
        "specialist": "Pulmonologist"
    },

    "Pneumonia": {
        "description": "An infection that inflames the air sacs in one or both lungs.",
        "specialist": "Pulmonologist"
    },

    "Asthma": {
        "description": "A chronic inflammatory disease of the airways.",
        "specialist": "Pulmonologist"
    },

    "Gastroenteritis": {
        "description": "Inflammation of the stomach and intestines causing vomiting and diarrhea.",
        "specialist": "Gastroenterologist"
    },

    "Allergic Rhinitis": {
        "description": "An allergic reaction causing sneezing and runny nose.",
        "specialist": "Allergist"
    }

}


# =====================================================
# Risk Level
# =====================================================

def get_risk_level(confidence):

    if confidence >= 85:
        return "High"

    elif confidence >= 60:
        return "Moderate"

    elif confidence >= 30:
        return "Low"

    return "Very Low"


# =====================================================
# Disease Prediction
# =====================================================

def predict_disease(age, symptoms):

    # Build feature vector
    features = create_feature_vector(age, symptoms)

    # Match training feature order
    features = features.reindex(
        columns=FEATURE_COLUMNS,
        fill_value=0
    )

    # Predict probabilities
    probabilities = model.predict_proba(features)[0]

    diseases = encoder.inverse_transform(
        list(range(len(probabilities)))
    )

    predictions = []

    for disease, probability in zip(diseases, probabilities):

        confidence = round(float(probability) * 100, 2)

        info = DISEASE_INFO.get(
            disease,
            {
                "description": "No description available.",
                "specialist": "General Physician"
            }
        )

        predictions.append({
            "disease": disease,
            "confidence": confidence,
            "risk": get_risk_level(confidence),
            "description": info["description"],
            "recommended_specialist": info["specialist"]
        })

    predictions.sort(
        key=lambda x: x["confidence"],
        reverse=True
    )

    return predictions[:3]