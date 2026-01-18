import chromadb
from chromadb.config import Settings


class ChromaVectorStore:
    def __init__(self, persist_dir: str = "data/chroma"):
        self.client = chromadb.Client(
            Settings(
                persist_directory=persist_dir,
                anonymized_telemetry=False
            )
        )
        self.collection = self.client.get_or_create_collection(
            name="website_content"
        )

    def add_documents(self, documents: list[dict], embeddings: list[list[float]]):
        ids = [
            str(i)
            for i in range(
                self.collection.count(),
                self.collection.count() + len(documents)
            )
        ]

        self.collection.add(
            documents=[doc["content"] for doc in documents],
            metadatas=[doc["metadata"] for doc in documents],
            embeddings=embeddings,
            ids=ids
        )

    def similarity_search(self, query_embedding: list[float], k: int = 4):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )