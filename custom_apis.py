from flask import Flask, jsonify, request
from custom_web_rag import CustomWebRAG
from custom_configs import SEARCH_STRING, WEBSITE, SEARCH_PROMPT,SUMMARIZE_PROMPT, GRAPH_EXTRACT_PROMPT


app = Flask(__name__)

@app.route('/api/web/search/')
def do_web_search():
    """Create a RAG instance and search the website contents for a given text"""
    custom_web_rag = CustomWebRAG(website=WEBSITE, search_str=SEARCH_STRING, prompt=SEARCH_PROMPT)
    data =  custom_web_rag.do_similarity_search().response
    return jsonify(data)

@app.route('/api/generate/web/summary/')
def generate_web_summary():
    """Create a RAG instance and summarize the website contents"""
    url = request.args.get('url')
    print(url)
    custom_web_rag = CustomWebRAG(website=WEBSITE, search_str=SEARCH_STRING, prompt=SUMMARIZE_PROMPT)
    data =  custom_web_rag.get_summary().response
    return jsonify(data)

@app.route('/api/generate/web/graph/')
def get_web_graph():
    """Create a RAG instance and extract the knowledge graph based on a given prompt"""
    custom_web_rag = CustomWebRAG(website=WEBSITE, search_str=SEARCH_STRING, prompt=GRAPH_EXTRACT_PROMPT)
    data = custom_web_rag.generateGraph().response
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)