from pprint import pprint

from services.ml.predictor import predict_disease

result = predict_disease(
    age=20,
    symptoms=[
        "cough",
        "fever",
        "runny nose"
    ]
)

print("\nTop Disease Predictions\n")

pprint(result)