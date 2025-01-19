# Custom classes for RAG for local models using Ollama
### **_Version of 19/Jan/25_**
- Embedding model used nomic-embed-text with local OllamaEmbeddings
- llm model used is llama3.2 locally with Ollama
- RAG implemented using Chroma DB as vector store
- Similarity search on a specific seach string

### - **_Changes Implemented_**
  - **_Used vectorstore function from_documents to crate a persistent vectorDB_**
  - **_Created a retriever and used similarity as search option_**
  - **_Used the output of the retriever as the context for RAG_**
  - **_Results are consistent after the above changes_**
  - _**Changes As of 5th Jan 2025**_
    - REST APIs for similarity search and summarization added
    - Added deepeval to evaluate LLM response
    - Class based RAG and Webscrape loader

### - ## **_To do_**
  - Try with different open scource vector DBs other than Chroma
  - **_Is Graph RAG a better implementation?_**
     - Cypher Query Language and langchain LLMGraphTransformer
         - For converting text to Graph and saving use LLMGraphTransformer from package langchain_experimental.graph_transformers.llm
             - ~~Refer https://python.langchain.com/v0.2/docs/how_to/graph_constructing/ for example~~
             - Does not work with Ollama
             - Need to check now to convert into Graph documents using Ollama
         - GraphCypherQAChain from langchain_community.chains.graph_qa.cypher can be used to query the GraphDB and get the results
           - Refer https://python.langchain.com/docs/tutorials/graph/ for example
     - How to improve the speed and performance of RAG using local models 
  - **rewrite the custom_rag file into a class**
  - Changes to webscrape to make it generic one for anytype of HTML tags for text content
  - Add ReactJS Front end, Django Bakend for Python
  - ~~Create REST APIs~~
  - Write unit tests using pytest
  - Add tools for document loading and reading
  - Rewrite the classes to separate out RAG and loaders.
    - _Need to include document loader classes. Currently supports webscraping only_
