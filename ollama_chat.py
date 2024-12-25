from ollama import chat, ChatResponse, Client

model = Client(
    host='http://localhost:11434',
   
)

response = model.chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":"What color is the sky at different times of the day?Respond in JSON format"
        }
    ],
    
)

print(response['message']['content'])




