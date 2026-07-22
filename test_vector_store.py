from rag.loader import load_pdf
from rag.chunker import chunk_text
from rag.embedder import Embedder
from rag.vector_store import VectorStore

print("Loading PDF...")
text = load_pdf("documents/Tomato.pdf")

print("Creating chunks...")
chunks = chunk_text(
    text,
    chunk_size=1000,
    overlap=100
)

print(f"Total chunks: {len(chunks)}")

print("Generating Gemini embeddings...")
embedder = Embedder()
embeddings = embedder.embed_batch(chunks)

print("Building FAISS index...")
store = VectorStore()
store.build(chunks, embeddings)
store.save()

print("Testing search...")

query = "What is early blight?"

query_embedding = embedder.embed_query(query)

results = store.search(query_embedding)

print("\nTop Results:\n")

for result in results:
    print("=" * 80)
    print(result)
    print()