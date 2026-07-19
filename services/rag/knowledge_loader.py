import os


class KnowledgeLoader:
    """
    Loads medical documents from the knowledge base.
    Empty documents are skipped.
    """

    def __init__(self, knowledge_path="knowledge_base"):
        self.knowledge_path = knowledge_path

    def load_documents(self):

        documents = []

        if not os.path.exists(self.knowledge_path):
            raise FileNotFoundError(
                f"Knowledge base not found: {self.knowledge_path}"
            )

        for filename in sorted(os.listdir(self.knowledge_path)):

            if not filename.endswith(".txt"):
                continue

            filepath = os.path.join(
                self.knowledge_path,
                filename
            )

            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read().strip()

            if content == "":
                print(f"Skipping empty file: {filename}")
                continue

            documents.append({
                "filename": filename,
                "disease": filename.replace(".txt", ""),
                "content": content
            })

        print(f"\nLoaded {len(documents)} documents.")

        return documents


if __name__ == "__main__":

    loader = KnowledgeLoader()

    docs = loader.load_documents()

    print("\n" + "=" * 60)

    for doc in docs:

        print(doc["filename"])
        print(doc["content"][:200])
        print("-" * 60)