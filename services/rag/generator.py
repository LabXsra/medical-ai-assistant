import requests


class MedicalGenerator:
    """
    Generates grounded medical responses using Ollama.
    """

    def __init__(self):

        self.url = "http://localhost:11434/api/generate"

        self.model = "llama3.2"

    def build_prompt(self, question, retrieved_chunks):

        context = "\n\n".join(
            chunk["text"] for chunk in retrieved_chunks
        )

        prompt = f"""
You are an AI Medical Assistant.

IMPORTANT RULES:

- Answer ONLY using the provided medical knowledge.
- Do NOT invent facts.
- Do NOT diagnose with certainty.
- Clearly mention that the information is educational.
- If the answer is unavailable, say:
"I don't have enough information in my medical knowledge base."

Medical Knowledge:
--------------------
{context}

--------------------

Patient Question:
{question}

Generate the response in the following format:

## Summary

## Possible Explanation

## Recommended Specialist

## General Advice

## Disclaimer
"""

        return prompt

    def generate(self, question, retrieved_chunks):

        prompt = self.build_prompt(
            question,
            retrieved_chunks
        )

        try:

            response = requests.post(

                self.url,

                json={

                    "model": self.model,

                    "prompt": prompt,

                    "stream": False

                },

                timeout=120

            )

            response.raise_for_status()

            return response.json()["response"]

        except Exception as e:

            return f"Generator Error:\n{e}"


if __name__ == "__main__":

    from retriever import Retriever

    retriever = Retriever()

    generator = MedicalGenerator()

    print("=" * 60)
    print("MEDICAL AI GENERATOR")
    print("=" * 60)

    while True:

        question = input("\nAsk a medical question (exit): ")

        if question.lower() == "exit":
            break

        retrieved = retriever.search(question)

        answer = generator.generate(
            question,
            retrieved
        )

        print("\n")
        print("=" * 60)
        print(answer)
        print("=" * 60)