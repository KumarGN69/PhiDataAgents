from flask import Flask, jsonify, request
from custom_web_rag import CustomWebRAG
from custom_image_read import CustomImageRead
from custom_configs import SEARCH_STRING, WEBSITE, SEARCH_PROMPT,SUMMARIZE_PROMPT, GRAPH_EXTRACT_PROMPT

from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("Tell me a joke about {topic}")

from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("Tell me a joke about {topic}")
prompt = prompt_template.invoke({"topic": "cats"}).to_string()


app = Flask(__name__)
"""
    API routing with following parameters
    /api/web/search 
        - Query web content on a specific string
        - params to the api for web search
            -> url:str - url of a website
            -> search_str:str - user query
    /api/generate/web/summary/
        - Read and generate summary of the webcontents
    /api/generate/web/graph/
        - Read the website contents and generate the knowledge graph based on the defined prompt
    /api/image/summary
        - read the image from the path passed as part of api query and summarize
"""
@app.route('/api/web/search/')
def do_web_search():
    """Create a RAG instance and search the website contents for a given text"""
    url = request.args.get('url')
    search_str = request.args.get('search_str')
    custom_web_rag = CustomWebRAG(website=WEBSITE, search_str=SEARCH_STRING, prompt=SEARCH_PROMPT)
    data =  custom_web_rag.do_similarity_search().response
    return jsonify(data)

@app.route("/api/generate/web/summary/")
def generate_web_summary():
    """Create a RAG instance and summarize the website contents"""
    url = request.args.get('url')
    search_str = request.args.get('search_str')
    custom_web_rag = CustomWebRAG(website=WEBSITE, search_str=SEARCH_STRING, prompt=SUMMARIZE_PROMPT)
    data =  custom_web_rag.get_summary().response
    return jsonify(data)
    # return data 

@app.route('/api/generate/web/graph/')
def get_web_graph():
    """Create a RAG instance and extract the knowledge graph based on a given prompt"""
    custom_web_rag = CustomWebRAG(website=WEBSITE, search_str=SEARCH_STRING, prompt=GRAPH_EXTRACT_PROMPT)
    data = custom_web_rag.generateGraph().response
    return jsonify(data)

@app.route('/api/image/summary/')
def get_image_contents():
    path = request.args.get('path')
    image_contents = CustomImageRead(path=path)
    # print(image_contents.readimage())
    return jsonify(image_contents.readimage().summary)

if __name__ == "__main__":
    app.run(debug=True)