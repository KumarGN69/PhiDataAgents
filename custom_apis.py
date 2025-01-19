from flask import Flask, jsonify, request
from custom_rag import LoadWebsite
# from extract_entities import get_graph
from custom_configs import SEARCH_STRING, WEBSITE, SEARCH_PROMPT, RETRIEVED_RESPONSE,SUMMARIZE_PROMPT, GRAPH_EXTRACT_PROMPT
import json
app = Flask(__name__)

@app.route('/api/search/')
def do_search():
    custom_rag = LoadWebsite(website=WEBSITE, search_str=SEARCH_STRING, prompt=SEARCH_PROMPT)
    data =  custom_rag.do_similarity_search().response
    return jsonify(data)

@app.route('/api/generate/summary/')
def generate_summary():
    url = request.args.get('url')
    print(url)
    custom_rag = LoadWebsite(website=WEBSITE, search_str=SEARCH_STRING, prompt=SUMMARIZE_PROMPT)
    data =  custom_rag.get_summary().response
    return jsonify(data)
@app.route('/api/generate/kg/')
def generate_knowledge_graph():
    custom_rag = LoadWebsite(website=WEBSITE, search_str=SEARCH_STRING, prompt=GRAPH_EXTRACT_PROMPT)
    data =  custom_rag.generate_knowledge_graph()
    # return jsonify(data)
    return data
@app.route('/api/generate/graph/')
def getGraph():
    custom_rag = LoadWebsite(website=WEBSITE, search_str=SEARCH_STRING, prompt=GRAPH_EXTRACT_PROMPT)
    data = custom_rag.generateGraph().response
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)