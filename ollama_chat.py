from ollama import chat, ChatResponse, Client

model = Client(
    host='http://localhost:11434',
   
)

response = model.chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":"What color is the sky at different times of the day?"
        }
    ],
    
)
print(response['message']['content'])

# from ollama import chat
# from ollama import ChatResponse

# response: ChatResponse = chat(
#     model='llama3.2', 
#     messages=[
#         {
#             'role': 'user',
#             'content': 'Why is the sky blue?',
#         },
#     ]
# )

# print(response['message']['content'])


