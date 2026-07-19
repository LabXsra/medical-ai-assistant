import pickle
import faiss

from sentence_transformers import SentenceTransformer


class Retriever:

    def __init__(self):

        print("=" * 60)
        print("LOADING RETRIEVER")
        print("=" * 60)

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        self.index = faiss.read_index(
            "services/rag/vector_store/medical_index.faiss"
        )

        with open(
            "services/rag/vector_store/metadata.pkl",
            "rb"
        ) as file:

            self.metadata = pickle.load(file)

        print(f"Knowledge Chunks : {len(self.metadata)}")
        print("Retriever Ready!\n")

    def search(
        self,
        query,
        top_k=3
    ):

        query_embedding = self.model.encode(
            [query],
            convert_to_numpy=True
        ).astype("float32")

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for distance, idx in zip(
            distances[0],
            indices[0]
        ):

            chunk = self.metadata[idx]

            results.append({

                "disease": chunk["disease"],

                "filename": chunk["filename"],

                "chunk_id": chunk["chunk_id"],

                "distance": float(distance),

                "text": chunk["text"]

            })

        return results


if __name__ == "__main__":

    retriever = Retriever()

    while True:

        query = input("\nAsk Medical Question (type exit): ")

        if query.lower() == "exit":
            break

        results = retriever.search(query)

        print("\n" + "=" * 60)
        print("TOP MATCHES")
        print("=" * 60)

        for i, result in enumerate(results, 1):

            print(f"\nRank {i}")

            print(f"Disease : {result['disease']}")

            print(f"Distance: {result['distance']:.2f}")

            print("-" * 40)

            print(result["text"])

            print("-" * 60)