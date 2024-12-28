from langchain_ollama import OllamaLLM, ChatOllama


llm = OllamaLLM(
    base_url= 'http://localhost:11434',
    model="llama3.2",
    format="json",
    temperature=0.0
)


response = llm.invoke("Why is the sky blue in color?")
print(response)