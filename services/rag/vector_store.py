import os
import pickle
import faiss
import numpy as np


class VectorStore:

    def __init__(self):

        self.index = None
        self.chunks = None

    def build_index(
        self,
        embeddings_path="services/rag/vector_store/embeddings.pkl",
        chunks_path="services/rag/vector_store/chunks.pkl"
    ):

        print("=" * 60)
        print("LOADING EMBEDDINGS")
        print("=" * 60)

        with open(embeddings_path, "rb") as file:
            embeddings = pickle.load(file)

        with open(chunks_path, "rb") as file:
            self.chunks = pickle.load(file)

        embeddings = np.array(
            embeddings,
            dtype="float32"
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)

        print(f"\nEmbedding Dimension : {dimension}")
        print(f"Vectors Stored      : {self.index.ntotal}")

    def save_index(
        self,
        folder="services/rag/vector_store"
    ):

        os.makedirs(folder, exist_ok=True)

        faiss.write_index(
            self.index,
            os.path.join(folder, "medical_index.faiss")
        )

        with open(
            os.path.join(folder, "metadata.pkl"),
            "wb"
        ) as file:

            pickle.dump(
                self.chunks,
                file
            )

        print("\nIndex Saved!")

        print(
            os.path.join(
                folder,
                "medical_index.faiss"
            )
        )

        print(
            os.path.join(
                folder,
                "metadata.pkl"
            )
        )


if __name__ == "__main__":

    store = VectorStore()

    store.build_index()

    store.save_index()

    print("\nFAISS database created successfully!")