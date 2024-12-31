from langchain_ollama import OllamaEmbeddings


embeddings = OllamaEmbeddings(
    model="nomic-embed-text:latest",
)

### Replace this code below aftermore ###
# input_text = "two plus two is four, minus one that's three, quick maths."
# vector = embeddings.embed_query(input_text)
# print(vector)

input_texts = ["two plus two is four, minus one that's three, quick maths.", "three plus three is nine, minus one that's eight, quick maths."]
vectors = embeddings.embed_documents(input_texts)
print(len(vectors))
print(vectors)