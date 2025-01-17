from langchain_experimental.graph_transformers.llm import LLMGraphTransformer
from langchain_core.documents.base import Document
from pydantic import BaseModel, Field
import json
from custom_llm import LLMModel
from custom_website_load import WebScrapeTool

class CustomGraph(BaseModel):
    nodes:str = Field(description="Key nodes", required=True)
    relationships:str = Field(description="Relationship", required=True)

class LoadWebsite:
    def __init__(self,website:str,search_str:str,prompt:str):
        self.website = website
        self.search_str = search_str
        self.prompt = prompt



    def get_summary(self):
        # instantiate the custom model and get the handle to it
        model = LLMModel()

        # Instantiate the custom phiData ScrapeTool and get the website details
        scrape_tool = WebScrapeTool(url=self.website)
        response = scrape_tool.getwebsitecontent()

        # create embedding, embedd into a vector store
        vector_store = model.create_vectorstore(response)

        # get the full content from the vector store for summarization
        doclist = vector_store.get()['documents']

        # get the Ollama Client interface to the model
        client = model.getclientinterface()

        # generate a llm response using client along with the RAG results
        generated_content = client.generate(
            model=model.MODEL_NAME,
            prompt=f"{self.prompt} {doclist}. Please summarize based on the give context "
        )

        return generated_content

    def do_similarity_search(self):
        # instantiate the custom model and get the handle to it
        model = LLMModel()

        # Instantiate the custom phiData ScrapeTool and get the website details
        scrape_tool = WebScrapeTool(url=self.website)
        response = scrape_tool.getwebsitecontent()

        # create embedding, embedd into a vector store
        vector_store = model.create_vectorstore(response)

        # create a retriever from the vector store
        retriever = vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 20}
        )

        # do a similarity search using the vector store retriever on specific search query
        doclist = retriever.invoke(self.search_str)

        # get the Ollama Client interface to the model
        client = model.getclientinterface()

        # generate a llm response using client along with the RAG results
        generated_content = client.generate(
            model=model.MODEL_NAME,
            prompt=f"{self.prompt} {doclist}. Please answer based on the give context "
        )

        return generated_content
    def get_graph(self):
        model = LLMModel()

        # Instantiate the custom phiData ScrapeTool and get the website details
        scrape_tool = WebScrapeTool(url=self.website)
        response = scrape_tool.getwebsitecontent()

        # get the Ollama Client interface to the model
        client = model.getclientinterface()

        # generate a llm response using client along with the RAG results
        generated_content = client.generate(
            model=model.MODEL_NAME,
            prompt=f"{self.prompt} {response}",
            format="json"
        )

        return json.loads(generated_content.response) # returns a json object
        # return generated_content.response # return a string
    def generate_knowledge_graph(self):
        model = LLMModel()

        # Instantiate the custom phiData ScrapeTool and get the website details
        scrape_tool = WebScrapeTool(url=self.website)
        response = scrape_tool.getwebsitecontent()
        response_str = ''.join(response)

        #llm with structured output
        llm = model.getinstance()
        # structured_llm = llm.with_structured_output(CustomGraph)
        llm_transformer = LLMGraphTransformer(llm)

        # convert to graph documents
        document = Document(page_content=llm.get_graph()) #create document object

        graph_documents = llm_transformer.convert_to_graph_documents(document)
        print(f"Nodes:{graph_documents[0].nodes}")
        print(f"Relationships:{graph_documents[0].relationships}")

        return graph_documents
# if __name__ == "__main__":
#     # responses = []
#     # with open("results.csv", "w") as file:
#     #     for i in range(0, 1):
#     #         file.write(main().response + '\n')
#     # print("Done!")
#
#     # print(response = main().response)

    