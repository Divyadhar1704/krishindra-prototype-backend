from rag.loader import PDFLoader
from rag.chunker import TextChunker
from rag.embedder import Embedder

loader = PDFLoader()
text = loader.load("documents/tomato.pdf")

chunker = TextChunker()

chunks = chunker.split(text)

embedder = Embedder()

embedding = embedder.embed(chunks[0])

print("Embedding Length:", len(embedding))
print()
print(embedding[:10])