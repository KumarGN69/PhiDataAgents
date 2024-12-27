from pydantic import BaseModel
# from pydantic_ai import AI

class UserQuery(BaseModel):
    username: str
    age: int
    height: float

dataList =[ 
    {
        "username":"John",
        "age":10,
        "height":0.8
    },

    {
        "username":"Bob",
        "age":12,
        "height":"1.8"
    },
    
]
userQueryList= []

for data in dataList:
    user_query = UserQuery(**data)
    userQueryList.append(user_query)

for query in userQueryList:
    print(query.username)
    print(query.age)
    print(query.height)