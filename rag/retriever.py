from rag.embedder import Embedder


class Retriever:

    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.embedder = Embedder()

    def retrieve(self, question, top_k=5):

        query_embedding = self.embedder.embed_query(question)

        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        return results

    def get_context(self, question, top_k=5):

        chunks = self.retrieve(question, top_k)

        context = "\n\n".join(chunks)

        return context