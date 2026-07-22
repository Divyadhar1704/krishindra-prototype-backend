import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


class Embedder:

    def __init__(self):

        print("Using Gemini Embedding API...")

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def embed(self, text):

        response = self.client.models.embed_content(
            model="gemini-embedding-001",
            contents=text
        )

        return response.embeddings[0].values

    def embed_query(self, query):

        return self.embed(query)

    def embed_batch(self, texts):

        embeddings = []

        for text in texts:
            embeddings.append(self.embed(text))

        return embeddings