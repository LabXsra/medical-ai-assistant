import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

# =====================================================
# Paths
# =====================================================

BASE_DIR = os.path.dirname(__file__)

DATASET_PATH = os.path.join(BASE_DIR, "diseases.csv")

MODEL_DIR = os.path.join(BASE_DIR, "models")

os.makedirs(MODEL_DIR, exist_ok=True)

MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")

ENCODER_PATH = os.path.join(MODEL_DIR, "label_encoder.pkl")

FEATURE_PATH = os.path.join(MODEL_DIR, "feature_columns.pkl")


# =====================================================
# Load Dataset
# =====================================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv(DATASET_PATH)

print(df.head())
print()
print("Dataset Shape:", df.shape)
print()


# =====================================================
# Features and Labels
# =====================================================

X = df.drop(columns=["disease"])

y = df["disease"]

# Save feature order for prediction
FEATURE_COLUMNS = X.columns.tolist()


# =====================================================
# Encode Labels
# =====================================================

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)


# =====================================================
# Train / Test Split
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded,
)

print("Training Samples:", len(X_train))
print("Testing Samples :", len(X_test))
print()


# =====================================================
# Train Model
# =====================================================

print("=" * 60)
print("Training Random Forest...")
print("=" * 60)

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)


# =====================================================
# Evaluation
# =====================================================

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print()
print("=" * 60)
print("Model Accuracy")
print("=" * 60)
print(f"{accuracy:.4f}")
print()

print("=" * 60)
print("Classification Report")
print("=" * 60)
print(
    classification_report(
        y_test,
        predictions,
        target_names=encoder.classes_
    )
)
print()

print("=" * 60)
print("Confusion Matrix")
print("=" * 60)
print(confusion_matrix(y_test, predictions))
print()


# =====================================================
# Save Model Artifacts
# =====================================================

joblib.dump(model, MODEL_PATH)

joblib.dump(encoder, ENCODER_PATH)

joblib.dump(FEATURE_COLUMNS, FEATURE_PATH)


# =====================================================
# Feature Importance (Bonus)
# =====================================================

feature_importance = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="importance",
    ascending=False
)

print("=" * 60)
print("Top 10 Important Features")
print("=" * 60)
print(feature_importance.head(10))
print()


# =====================================================
# Completion
# =====================================================

print("=" * 60)
print("Model Saved Successfully!")
print("=" * 60)
print("Model Path          :", MODEL_PATH)
print("Label Encoder Path  :", ENCODER_PATH)
print("Feature Columns Path:", FEATURE_PATH)
print("=" * 60)