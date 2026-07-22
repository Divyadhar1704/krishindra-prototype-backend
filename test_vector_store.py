from rag.loader import PDFLoader
from rag.chunker import TextChunker
from rag.embedder import Embedder
from rag.vector_store import VectorStore

loader = PDFLoader()
text = loader.load("documents/tomato.pdf")

chunker = TextChunker()
chunks = chunker.split(text)

embedder = Embedder()

embeddings = embedder.embed_batch(chunks)

store = VectorStore()
store.build(chunks, embeddings)

query = "What is early blight?"

query_embedding = embedder.embed(query)

results = store.search(query_embedding)

print("Top Results:\n")

for result in results:
    print("=" * 80)
    print(result)
    print()