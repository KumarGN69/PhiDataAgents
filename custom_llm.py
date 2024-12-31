import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from ollama import Client
from configurations import OUTPUT_FORMAT, MODEL_TEMPERATURE

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
        self.temperature = MODEL_TEMPERATURE
        self.EMBED_MODEL = os.getenv("EMBEDDING_MODEL")
    def getinstance(self):
        """Return the handle to the specific custom model
        return: OllamaLLM model with requisite configuration
        """
        return OllamaLLM(
            base_url=self.MODEL_URL,
            api_key=self.API_KEY,
            model=self.MODEL_NAME,
            # format=OUTPUT_FORMAT,
            temperature=MODEL_TEMPERATURE
        )
    def create_embedding(self) -> OllamaEmbeddings:
        """create embedding
        return: List of embedding vectors
        """
        embeddings = OllamaEmbeddings(
            base_url=self.MODEL_URL,
            model=self.EMBED_MODEL,
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
            # length_function=len
            )
        doc_list = text_splitter.create_documents(input_text)
        # print(doc_list)
        documents = text_splitter.split_documents(doc_list)
        # print (documents)
        vector_store = Chroma(
            collection_name="vector_collection",
            embedding_function=self.create_embedding(),
            persist_directory="./chroma_langchain.db"
         )
        vector_store.add_documents(documents)

        return vector_store
    def getclientinterface(self)->Client:
        """
        Returns the Ollama client for a chat/generate/create interface
        :return: ollama Client object
        """
        return Client(self.MODEL_URL)