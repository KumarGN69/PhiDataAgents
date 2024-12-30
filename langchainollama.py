import os
from pprint import pprint
from custom_llm import LLMModel
from configurations import TASK_TO_PERFORM, SEARCH_STRING, WEBSITE
from webscrape import ScrapeTool


#instantiating the custom model
model = LLMModel()
llm = model.getinstance()

#Invoke the model to perform a specific task and store in a list
# response = [llm.invoke(TASK_TO_PERFORM)]

#Instantiate the custom phiData ScrapeTool and get the website details
scrape_tool = ScrapeTool(WEBSITE,TASK_TO_PERFORM)
response = scrape_tool.getwebsitedata()

#print the output
# pprint(response)

#create embeddiing, embedd into a vector store
vector_store = model.create_vectorstore(response)
# do a similarity search on vector DB for a specific query
results = vector_store.similarity_search(query=SEARCH_STRING,k=10)
# pprint(results)
#get the Ollama Client interface to the model
client = model.getclientinterface()
#generate a llm response using client along with the RAG results
final_answer = client.generate(
    model=model.MODEL_NAME,
    prompt=f"{SEARCH_STRING}.Answer using the {results} from vector store"
)
print(final_answer.response)
