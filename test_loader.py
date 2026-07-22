from rag.loader import PDFLoader

loader = PDFLoader()

text = loader.load("documents/tomato.pdf")

print(text)