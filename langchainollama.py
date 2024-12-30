from pprint import pprint
from custom_llm import LLMModel
from configurations import TASK_TO_PERFORM, SEARCH_STRING

#instantiating the custom model
model = LLMModel()
llm = model.getinstance()


#Invoke the model to perform a specific task and store in a list
response= []
response.append( llm.invoke(TASK_TO_PERFORM))

#print the output
print(response)

#create embeddiing, embedd into a vector store
vector_store = model.create_vectorstore(response)
# do a similarity search by query
results = vector_store.similarity_search(query=SEARCH_STRING,k=1)
pprint("\\n\\n")
pprint(results)
