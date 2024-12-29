# from langchain_ollama import OllamaLLM, ChatOllama
from llm import LLMModel
from configurations import TASK_TO_PERFORM

#instantiating the custom model
model = LLMModel()
llm = model.getinstance()

#Invoke the model to perform a specific task
response = llm.invoke(TASK_TO_PERFORM)

#print the output
print(type(response))
print(response)