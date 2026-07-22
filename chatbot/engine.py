import os

from dotenv import load_dotenv

from chatbot.prompts import SYSTEM_PROMPT
from chatbot.memory import ConversationMemory
from chatbot.llm import LLM

from rag.vector_store import VectorStore
from rag.retriever import Retriever
from rag.loader import load_pdf
from rag.chunker import chunk_text
from rag.embedder import Embedder


class ChatbotEngine:

    def __init__(self):

        load_dotenv()

        self.memory = ConversationMemory()

        self.llm = LLM()

        self.vector_store = VectorStore()

        loaded = self.vector_store.load()

        if not loaded:

            print("Building vector database...")

            text = load_pdf("documents/Tomato.pdf")

            chunks = chunk_text(
                text[:15000],
                chunk_size=1000,
                overlap=100
            )

            embedder = Embedder()

            embeddings = embedder.embed_batch(chunks)

            self.vector_store.build(
                chunks,
                embeddings
            )

            self.vector_store.save()

        else:

            print("Vector database loaded.")

        self.retriever = Retriever(
            self.vector_store
        )

    def _build_prompt(self, user_message):

        history = ""

        for message in self.memory.get_messages():

            role = message["role"].capitalize()

            history += f"{role}: {message['content']}\n"

        context = self.retriever.get_context(
            user_message,
            top_k=5
        )

        prompt = f"""
{SYSTEM_PROMPT}

Conversation History:
{history}

Context:
{context}

User:
{user_message}

Answer:
"""

        return prompt

    def get_response(self, user_message):

        self.memory.add_message(
            "user",
            user_message
        )

        prompt = self._build_prompt(
            user_message
        )

        answer = self.llm.generate(
            prompt
        )

        self.memory.add_message(
            "assistant",
            answer
        )

        return answer