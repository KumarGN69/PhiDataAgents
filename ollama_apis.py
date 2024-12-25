import ollama_apis
import requests, json

headers={'Cache-Control': 'no-cache'}
options ={
    "model":"llama3.2",
    "prompt":"What color is the sky at different times of the day?",
    "format":"json",
    "stream": False,
    "options":{
        "temperature":0.0,
    },
    "keep_alive":0,
    "max_retries":1,
    "messages":[
        {
            "role":"user",
            "content":"Respond using JSON"
        }
    ]
}


result = requests.post(url='http://localhost:11434/api/generate/',json=options, headers=headers)

result_json=json.loads(result.text)
print(result_json)
# print(json.loads(result_json['response']))

