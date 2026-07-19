import random
import pandas as pd

from disease_list import DISEASES


BACKGROUND_RATE = 0.03


def generate_dataset(samples_per_disease=500):

    rows = []

    all_symptoms = sorted({

        symptom

        for disease in DISEASES.values()

        for symptom in disease["symptoms"]

    })

    for disease_name, info in DISEASES.items():

        symptom_probabilities = info["symptoms"]

        for _ in range(samples_per_disease):

            row = {}

            row["age"] = random.randint(5,85)

            row["disease"] = disease_name

            for symptom in all_symptoms:

                if symptom in symptom_probabilities:

                    probability = symptom_probabilities[symptom]

                else:

                    probability = BACKGROUND_RATE

                row[symptom] = int(random.random() < probability)

            rows.append(row)

    return pd.DataFrame(rows)


if __name__=="__main__":

    df = generate_dataset()

    df.to_csv("services/ml/diseases.csv",index=False)

    print(df.head())

    print()

    print(df["disease"].value_counts())

    print()

    print(df.shape)