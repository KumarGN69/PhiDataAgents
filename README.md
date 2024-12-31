# PhiDataAgents
Version of 31/Dec/24
- Embedding model used nomic-embed-text with local OllamaEmbeddings
- llm model used is llama3.2 locally with Ollama
- RAG implemented using Chroma DB as vector store
- Similarity search on a specific seach string
- **_Changes Implemented_**
  - **_Used vectorstore function from_documents to crate a persistent vectorDB_**
  - **_Created a retriever and used similarity as search option_**
  - **_Used the output of the retriever as the context for RAG_**
  - **_Results are consistent after the above changes_**
- Next steps 
  - Try with different vector DBs
  - Check what is the best vectorDB retrieval function to use
  - Is Graph RAG a better implementation?