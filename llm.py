import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from configurations import LLM_MODEL_TO_USE, OUTPUT_FORMAT, MODEL_TEMP
class LLMModel:
    """
    This class defines the a custom model using Ollama
    --------------------------------------------------------
    Function getinstance() return the handle the model with specific parameters
    Takes no argument. For future this can be customize to pass the parameters to configure the llm
    returns the OllamaLLM model
    """
    def __init__(self):
        """constructor for the LLMModel class and populates the host, api key and the model to use"""
        load_dotenv()
        self.MODEL_URL = os.getenv("BASE_URL")
        self.API_KEY = os.getenv("API_KEY")
        self.MODEL_NAME = os.getenv("MODEL_NAME")
        # self.MODEL_NAME= "mistral"
        self.temperature = 0.0
    def getinstance(self):
        """Return the handle to the specific custom model
        return: OllamaLLM model with requisite configuration
        """
        return OllamaLLM(
            base_url=self.MODEL_URL,
            api_key=self.API_KEY,
            model=LLM_MODEL_TO_USE,
            # format=OUTPUT_FORMAT,
            temperature=MODEL_TEMP
        )
    def create_embedding(self) -> OllamaEmbeddings:
        """create embedding
        return: List of embedding vectors
        """
        embeddings = OllamaEmbeddings(
            base_url=self.MODEL_URL,
            model=LLM_MODEL_TO_USE,
        )
        return embeddings

    def create_vectorstore(self,input_text:list):
        """
        splits the input text in chunks with overlap,
        create embeddings using OllamaEmbedding add chunks to vector store
        and return the handle to the vector store
        :param input_text:
        :return: Chroma vector store
        """
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
            length_function=len
            )
        doc_list = text_splitter.create_documents(input_text)
        documents = text_splitter.split_documents(doc_list)
        vector_store = Chroma(
            collection_name="vector_collection",
            embedding_function=self.create_embedding(),
            persist_directory="./chroma_langchain.db"
         )
        vector_store.add_documents(documents)
        # vector_store.

        return vector_store