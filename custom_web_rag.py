from langchain_experimental.graph_transformers.llm import LLMGraphTransformer
from langchain_core.documents.base import Document
from pydantic import BaseModel, Field
from custom_llm import LLMModel
from custom_website_load import WebScrapeTool

class CustomWebRAG:
    """
    Loads the website and reads the content
    Does several RAG operations including embedding into a vector DB, summarize, similarity search, generate graphs


    """
    # def __init__(self,website:str,search_str:str,prompt:str):
    def __init__(self, **kwargs):
        self.model = LLMModel()
        self.website = kwargs.get("website")
        self.search_str = kwargs.get("search_str")
        self.prompt = kwargs.get("prompt")

    def get_summary(self):
        """instantiate the custom model and get the handle to it"""
        # model = LLMModel()

        # Instantiate the custom phiData ScrapeTool and get the website details
        scrape_tool = WebScrapeTool(url=self.website)
        response = scrape_tool.getwebsitecontent()

        # create embedding, embedd into a vector store
        vector_store = self.model.create_vectorstore(response)

        # get the full content from the vector store for summarization
        doclist = vector_store.get()['documents']

        # get the Ollama Client interface to the model
        client = self.model.getclientinterface()

        # generate a llm response using client along with the RAG results
        generated_content = client.generate(
            model=self.model.MODEL_NAME,
            prompt=f"{self.prompt} {doclist}. Please summarize based on the give context "
        )
        # print(type(generated_content.response))
        return generated_content

    def do_similarity_search(self):
        """instantiate the custom model and get the handle to it"""
        # model = LLMModel()

        # Instantiate the custom phiData ScrapeTool and get the website details
        scrape_tool = WebScrapeTool(url=self.website)
        response = scrape_tool.getwebsitecontent()

        # create embedding, embedd into a vector store
        vector_store = self.model.create_vectorstore(response)

        # create a retriever from the vector store
        retriever = vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 20}
        )

        # do a similarity search using the vector store retriever on specific search query
        doclist = retriever.invoke(self.search_str)

        # get the Ollama Client interface to the model
        client = self.model.getclientinterface()

        # generate a llm response using client along with the RAG results
        generated_content = client.generate(
            model=self.model.MODEL_NAME,
            prompt=f"{self.prompt} {doclist}. Please answer based on the give context "
        )

        return generated_content
    def generateGraph(self):
        """generate graph from the content passed to it"""
        # model = LLMModel()

        # Instantiate the custom phiData ScrapeTool and get the website details
        scrape_tool = WebScrapeTool(url=self.website)
        response = scrape_tool.getwebsitecontent()

        # get the Ollama Client interface to the model
        client = self.model.getclientinterface()

        # generate a llm response using client along with the RAG results
        generated_content = client.generate(
            model=self.model.MODEL_NAME,
            prompt=f"{self.prompt} {response}",
            format="json"
        )
        return generated_content # return a string

    def createDocumentList(self, contents: list) -> list:
        """creates list of langchain document objects for the given string"""
        # contents = data.split(".")
        documents = [Document(page_content=content) for content in contents]
        return documents
    def generate_knowledge_graph(self):
        """generates the knowledge graph documents for a given content"""
        # model = LLMModel()

        # Instantiate the custom phiData ScrapeTool and get the website details
        scrape_tool = WebScrapeTool(url=self.website)
        response = scrape_tool.getwebsitecontent()
        #llm with structured output
        llm = self.model.getchatinstance()

        #create document list of the retrieved content
        documents = self.createDocumentList(response)

        # instantiate a LLMGraphTransformer and generate graph documents from the document list
        llm_transformer = LLMGraphTransformer(llm)
        graph_documents = llm_transformer.convert_to_graph_documents(documents)
        print(graph_documents)
        print(f"Nodes:{graph_documents[0].nodes}")
        print(f"Relationships:{graph_documents[0].relationships}")
        return graph_documents

    