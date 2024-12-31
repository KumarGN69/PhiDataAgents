# PhiDataAgents
Version of 31/Dec/24
- Embedding model used nomic-embed-text
- llm model used is llama3.2 locally with Ollama
- RAG implemented using Chroma DB as vector store
- Similarity search on a specific seach string
- The llm generated results from RAG are inconsistent for >50% of trails.
-     Even when the search string used has not changed
-     Deleting the vector store and starting the search results in repeating pattern on inconsistent results
-     For incorrect and inconsistent results llm engine indicates that details of the search string are not in the retrieved results from vector DB
- Next steps
-     Undertand the performance and details of the  "similarity search" function
-     Try with different vector DBs
-     Check what is the best vectorDB retrieval function to use  
