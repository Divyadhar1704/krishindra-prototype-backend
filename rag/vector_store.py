import os
import pickle

import faiss
import numpy as np


class VectorStore:

    def __init__(self):
        self.index = None
        self.chunks = []

        self.index_path = "data/faiss.index"
        self.chunk_path = "data/chunks.pkl"

    def build(self, chunks, embeddings):

        dimension = len(embeddings[0])

        self.index = faiss.IndexFlatL2(dimension)

        vectors = np.array(embeddings, dtype="float32")

        self.index.add(vectors)

        self.chunks = chunks

    def save(self):

        os.makedirs("data", exist_ok=True)

        faiss.write_index(self.index, self.index_path)

        with open(self.chunk_path, "wb") as file:
            pickle.dump(self.chunks, file)

    def load(self):

        if not os.path.exists(self.index_path):
            return False

        if not os.path.exists(self.chunk_path):
            return False

        self.index = faiss.read_index(self.index_path)

        with open(self.chunk_path, "rb") as file:
            self.chunks = pickle.load(file)

        return True

    def search(self, query_embedding, top_k=5):

        query = np.array([query_embedding], dtype="float32")

        distances, indices = self.index.search(query, top_k)

        results = []

        for index in indices[0]:

            if index != -1:
                results.append(self.chunks[index])

        return results