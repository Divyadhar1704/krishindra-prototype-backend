from sentence_transformers import SentenceTransformer


class Embedder:

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        print("Embedding model loaded.")

    def embed(self, text):

        embedding = self.model.encode(
            text,
            convert_to_numpy=True
        )

        return embedding

    def embed_query(self, query):

        embedding = self.model.encode(
            query,
            convert_to_numpy=True
        )

        return embedding

    def embed_batch(self, texts):

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        return embeddings