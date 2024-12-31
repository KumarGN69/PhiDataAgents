### A little example ###
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from langchain_ollama import OllamaEmbeddings


embeddings = OllamaEmbeddings(
    model="nomic-embed-text:latest",
)


from custom_llm import LLMModel
# context = """
# Retrieval-Augmented Generation (RAG) is the process of optimizing the output of a large language model, so it references an authoritative knowledge base outside of its training data sources before generating a response.
# Large Language Models (LLMs) are trained on vast volumes of data and use billions of parameters to generate original output for tasks like answering questions, translating languages, and completing sentences.
# RAG extends the already powerful capabilities of LLMs to specific domains or an organization's internal knowledge base, all without the need to retrain the model.
# It is a cost-effective approach to improving LLM output so it remains relevant, accurate, and useful in various contexts.
# """
llm = LLMModel().getinstance()

prompt = """
Use the only the given context to answer the following question. If you don't know the answer, reply that you are unsure.

Context: {context}

Question: {question}
"""

prompt_template = PromptTemplate.from_template(prompt)

# chain = prompt_template | llm
#
# print(chain.invoke({
#     "context": context,
#     # "question": "What is Retrieval-Augmented Generation?",
#     "question": "What is the difference between Retrieval-Augmented Generation and semantic search?"
# }))
#

loader = WebBaseLoader('https://aws.amazon.com/what-is/retrieval-augmented-generation/')

data = loader.load()

# print(data)

# print(data[0].page_content + "\n--------\n")
# print(data[0].metadata)

splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n\n\n\n\n\n\n\n\n\n\n\n", "\n\n", "       ", "\n\n\n", "\n", "", "  "],
    chunk_size=200,
    chunk_overlap=100
)

chunks = splitter.split_text(data[0].page_content)

# print(chunks)
# print("\n---------\n")
# print([len(chunk) for chunk in chunks])
# vector_store = Chroma(
#             collection_name="vector_collection",
#             embedding_function=embeddings,
#             # persist_directory="./chroma_langchain.db",
#          )
vector_store= Chroma.from_texts(
    texts=chunks,
    embedding=embeddings
)

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 20}
)

# print(retriever.invoke("What is the difference between Retrieval-Augmented Generation and semantic search?"))

chain = ({"context": retriever, "question": RunnablePassthrough()}
        | prompt_template
        | llm
        | StrOutputParser())

user_question = "What is the difference between Retrieval-Augmented Generation and semantic search?"
result = chain.invoke(user_question)
print(result)