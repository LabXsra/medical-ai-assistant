from transformers import pipeline

MODEL_NAME = "d4data/biomedical-ner-all"

print("=" * 60)
print("Loading Biomedical NER Model...")
print("Model:", MODEL_NAME)
print("=" * 60)

medical_pipeline = pipeline(
    task="token-classification",
    model=MODEL_NAME,
    tokenizer=MODEL_NAME,
    aggregation_strategy="simple"
)

print("=" * 60)
print("Biomedical NER Loaded Successfully!")
print("=" * 60)


def predict(text: str):
    """
    Run biomedical named entity recognition.
    """
    return medical_pipeline(text)