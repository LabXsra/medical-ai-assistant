import os
import pickle

from sentence_transformers import SentenceTransformer

from knowledge_loader import KnowledgeLoader
from text_splitter import TextSplitter


class EmbeddingGenerator:

    def __init__(self):

        print("\nLoading Embedding Model...")

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        print("Model Loaded Successfully!\n")

    def generate_embeddings(self, chunks):

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=True
        )

        return embeddings

    def save_embeddings(
        self,
        embeddings,
        chunks,
        save_folder="services/rag/vector_store"
    ):

        os.makedirs(
            save_folder,
            exist_ok=True
        )

        with open(
            os.path.join(
                save_folder,
                "embeddings.pkl"
            ),
            "wb"
        ) as file:

            pickle.dump(
                embeddings,
                file
            )

        with open(
            os.path.join(
                save_folder,
                "chunks.pkl"
            ),
            "wb"
        ) as file:

            pickle.dump(
                chunks,
                file
            )

        print("\nEmbeddings Saved!")

        print(
            os.path.join(
                save_folder,
                "embeddings.pkl"
            )
        )

        print(
            os.path.join(
                save_folder,
                "chunks.pkl"
            )
        )


if __name__ == "__main__":

    print("=" * 60)
    print("MEDICAL RAG EMBEDDINGS")
    print("=" * 60)

    loader = KnowledgeLoader()

    documents = loader.load_documents()

    splitter = TextSplitter()

    chunks = splitter.split_documents(
        documents
    )

    print(f"\nDocuments : {len(documents)}")
    print(f"Chunks    : {len(chunks)}")

    generator = EmbeddingGenerator()

    embeddings = generator.generate_embeddings(
        chunks
    )

    print("\nEmbedding Shape:")

    print(embeddings.shape)

    generator.save_embeddings(
        embeddings,
        chunks
    )

    print("\nDone.")