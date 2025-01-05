from flask import Flask, jsonify
from custom_rag import CustomRAG
from custom_configs import SEARCH_STRING, WEBSITE, PROMPT, RETRIEVED_RESPONSE
import json
app = Flask(__name__)

@app.route('/api/generate/response/')
def get_data():
    custom_rag = CustomRAG(website=WEBSITE,search_str=SEARCH_STRING,prompt=PROMPT)
    data =  custom_rag.main().response
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)