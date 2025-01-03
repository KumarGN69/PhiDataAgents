import os
from dotenv import load_dotenv
from aisuite.client import Client
load_dotenv()

client = Client()

models = ["ollama:llama3.2", "ollama:mistral","ollama:granite3.1-moe:3b"]

messages = [
    {"role": "system", "content": "Respond in american English."},
    {"role": "user", "content": "Tell me a joke."},
]

for model in models:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.75
    )
    print(response.choices[0].message.content)