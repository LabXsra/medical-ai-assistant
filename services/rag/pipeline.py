from services.rag.retriever import Retriever
from services.rag.generator import MedicalGenerator


class RAGPipeline:

    def __init__(self):

        print("=" * 60)
        print("INITIALIZING MEDICAL RAG")
        print("=" * 60)

        self.retriever = Retriever()

        self.generator = MedicalGenerator()

        print("\nMedical RAG Ready!")

    def answer_question(
        self,
        question,
        top_k=3
    ):

        retrieved_chunks = self.retriever.search(
            question,
            top_k=top_k
        )

        answer = self.generator.generate(
            question,
            retrieved_chunks
        )

        return {

            "question": question,

            "retrieved_chunks": retrieved_chunks,

            "generated_answer": answer

        }


if __name__ == "__main__":

    rag = RAGPipeline()

    while True:

        question = input("\nAsk a medical question (exit): ")

        if question.lower() == "exit":
            break

        result = rag.answer_question(question)

        print("\n")
        print("=" * 60)
        print("GENERATED ANSWER")
        print("=" * 60)

        print(result["generated_answer"])

        print("\n")
        print("=" * 60)
        print("RETRIEVED CHUNKS")
        print("=" * 60)

        for i, chunk in enumerate(result["retrieved_chunks"], start=1):

            print(f"\nRank {i}")

            print(f"Disease : {chunk['disease']}")

            print(f"Chunk ID : {chunk['chunk_id']}")

            print(f"Distance : {chunk['distance']:.4f}")

            print("-" * 50)

            print(chunk["text"][:300])

            print("-" * 50)