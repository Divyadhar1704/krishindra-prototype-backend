from rag.loader import PDFLoader
from rag.chunker import TextChunker

loader = PDFLoader()
text = loader.load("documents/tomato.pdf")

chunker = TextChunker()

chunks = chunker.split(text)

print("Total Chunks:", len(chunks))
print()
print(chunks[0])