from flask import Flask, jsonify
from custom_rag import LoadWebsite
from custom_configs import SEARCH_STRING, WEBSITE, SEARCH_PROMPT, RETRIEVED_RESPONSE,SUMMARIZE_PROMPT
import json
app = Flask(__name__)

@app.route('/api/search/')
def do_search():
    custom_rag = LoadWebsite(website=WEBSITE, search_str=SEARCH_STRING, prompt=SEARCH_PROMPT)
    data =  custom_rag.do_similarity_search().response
    return jsonify(data)

@app.route('/api/summary/')
def generate_summary():
    custom_rag = LoadWebsite(website=WEBSITE, search_str=SEARCH_STRING, prompt=SUMMARIZE_PROMPT)
    data =  custom_rag.get_summary().response
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)