from custom_llm import LLMModel
from configurations import SEARCH_STRING, WEBSITE, PROMPT
from webscrape import ScrapeTool

def main():
    # instantiate the custom model and get the handle to it
    model = LLMModel()

    # Instantiate the custom phiData ScrapeTool and get the website details
    scrape_tool = ScrapeTool(url=WEBSITE)
    response = scrape_tool.getwebsitecontent()

    # create embedding, embedd into a vector store
    vector_store = model.create_vectorstore(response)

    # create a retriever from the vector store
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 20}
    )

    # do a similarity search using the vector store retriever on specific search query
    doclist = retriever.invoke(SEARCH_STRING)

    # get the Ollama Client interface to the model
    client = model.getclientinterface()

    # generate a llm response using client along with the RAG results
    final_answer = client.generate(
        model=model.MODEL_NAME,
        prompt=f"{PROMPT} {doclist}. Please answer based on the give context "
    )

    return final_answer

if __name__ == "__main__":
    print(main().response)
