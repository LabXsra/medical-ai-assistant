from transformers import pipeline

# ==========================================================
# Biomedical NER Model
# ==========================================================

MODEL_NAME = "d4data/biomedical-ner-all"

ner = pipeline(
    "token-classification",
    model=MODEL_NAME,
    tokenizer=MODEL_NAME,
    aggregation_strategy="none"
)


# ==========================================================
# Merge WordPiece Tokens
# ==========================================================

def merge_tokens(tokens):

    merged = []

    current = None

    for token in tokens:

        word = token["word"]

        # -------------------------------
        # Continuation token (##)
        # -------------------------------

        if word.startswith("##") and current is not None:

            current["text"] += word[2:]

            current["score"] = max(
                current["score"],
                token["score"]
            )

            continue

        # -------------------------------
        # SentencePiece token (▁)
        # -------------------------------

        if word.startswith("▁"):

            word = word[1:]

        # -------------------------------
        # Same entity continues
        # -------------------------------

        if (
            current is not None
            and token["entity"].endswith(current["label"])
            and token["start"] <= current["end"] + 1
        ):

            if current["text"].endswith("-"):

                current["text"] += word

            else:

                current["text"] += " " + word

            current["end"] = token["end"]

            current["score"] = max(
                current["score"],
                token["score"]
            )

        else:

            if current:

                merged.append(current)

            current = {

                "text": word,

                "label": token["entity"].split("-")[-1],

                "start": token["start"],

                "end": token["end"],

                "score": token["score"]

            }

    if current:

        merged.append(current)

    return merged


# ==========================================================
# Extract Medical Entities
# ==========================================================

def extract_entities(text):

    raw = ner(text)

    merged = merge_tokens(raw)

    entities = []

    seen = set()

    for entity in merged:

        name = entity["text"].strip().lower()

        if len(name) < 2:
            continue

        if name in seen:
            continue

        seen.add(name)

        entities.append({

            "text": name,

            "label": entity["label"],

            "confidence": round(
                float(entity["score"]),
                4
            )

        })

    return entities