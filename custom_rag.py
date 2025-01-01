from custom_llm import LLMModel
from custom_configs import SEARCH_STRING, WEBSITE, PROMPT, RETRIEVED_RESPONSE
from custom_webscrape import WebScrapeTool

f


def main():
    # instantiate the custom model and get the handle to it
    model = LLMModel()

    # Instantiate the custom phiData ScrapeTool and get the website details
    scrape_tool = WebScrapeTool(url=WEBSITE)
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
    generated_content = client.generate(
        model=model.MODEL_NAME,
        prompt=f"{PROMPT} {doclist}. Please answer based on the give context "
    )

    return generated_content


if __name__ == "__main__":
    # responses = []
    # with open("results.csv", "w") as file:
    #     for i in range(0, 1):
    #         file.write(main().response + '\n')
    # print("Done!")

    print(response = main().response)

    