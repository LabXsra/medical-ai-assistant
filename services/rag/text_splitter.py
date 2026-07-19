from typing import List


class TextSplitter:
    """
    Splits medical documents into overlapping chunks.
    """

    def __init__(
        self,
        chunk_size=400,
        overlap=80
    ):

        self.chunk_size = chunk_size
        self.overlap = overlap

    def split_document(self, text: str) -> List[str]:

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunk = text[start:end].strip()

            chunks.append(chunk)

            start += self.chunk_size - self.overlap

        return chunks

    def split_documents(self, documents):

        all_chunks = []

        for document in documents:

            chunks = self.split_document(
                document["content"]
            )

            for i, chunk in enumerate(chunks):

                all_chunks.append({

                    "filename": document["filename"],

                    "disease": document["disease"],

                    "chunk_id": i,

                    "text": chunk

                })

        return all_chunks


if __name__ == "__main__":

    from knowledge_loader import KnowledgeLoader

    loader = KnowledgeLoader()

    docs = loader.load_documents()

    splitter = TextSplitter()

    chunks = splitter.split_documents(docs)

    print("=" * 60)
    print("TEXT SPLITTER")
    print("=" * 60)

    print(f"\nDocuments Loaded : {len(docs)}")
    print(f"Chunks Generated : {len(chunks)}\n")

    for chunk in chunks[:5]:

        print(f"File      : {chunk['filename']}")
        print(f"Chunk ID  : {chunk['chunk_id']}")
        print(f"Disease   : {chunk['disease']}")
        print(chunk["text"])
        print("-" * 60)