import os
from pprint import pprint
from custom_llm import LLMModel
from configurations import TASK_TO_PERFORM, SEARCH_STRING, WEBSITE, PROMPT
from webscrape import ScrapeTool


#instantiating the custom model
model = LLMModel()
llm = model.getinstance()

#Invoke the model to perform a specific task and store in a list
# response = [llm.invoke(TASK_TO_PERFORM)]

#Instantiate the custom phiData ScrapeTool and get the website details
scrape_tool = ScrapeTool(url=WEBSITE)
response = scrape_tool.getwebsitedata()

#print the output
# pprint(response)

#create embeddiing, embedd into a vector store
vector_store = model.create_vectorstore(response)
# do a similarity search on vector DB for a specific query
doclist = vector_store.similarity_search(query=SEARCH_STRING,k=10)
results = ''.join(doc.page_content for doc in doclist)
# print(results)
#get the Ollama Client interface to the model
client = model.getclientinterface()
#generate a llm response using client along with the RAG results
# print(f"{PROMPT}{results}. Please answer based on the above context. ")
final_answer = client.generate(
    model=model.MODEL_NAME,
    prompt=f"{PROMPT} {results}. Please answer based on the above context "
)
print(final_answer.response)
