from langchain_experimental.graph_transformers.llm import LLMGraphTransformer
from langchain_core.documents.base import Document
from custom_llm import LLMModel
from custom_rag import LoadWebsite
from custom_configs import SEARCH_STRING, WEBSITE, SEARCH_PROMPT, RETRIEVED_RESPONSE,SUMMARIZE_PROMPT, GRAPH_EXTRACT_PROMPT

custom_rag = LoadWebsite(website=WEBSITE, search_str=SEARCH_STRING, prompt=SUMMARIZE_PROMPT)

def createDocumentList(data: str)->list:
    """creates list of langchain document objects for the given string"""
    contents = data.split(".")
    documents = [Document(page_content=content) for content in contents]
    return documents


documents = createDocumentList(custom_rag.get_summary())
llm = LLMModel().getchatinstance()

llm_transformer = LLMGraphTransformer(
    llm= llm,
    allowed_nodes=["Person", "Country", "Organization"],
    allowed_relationships=["EVENT","LOCATION","HISTORY"]
)
graph_documents_filtered = llm_transformer.convert_to_graph_documents(documents=documents)
print(graph_documents_filtered)
print(f"Nodes:{graph_documents_filtered[0].nodes}")
print(f"Relationships:{graph_documents_filtered[0].relationships}")

