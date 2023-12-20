from typing import Any
from openai import OpenAI
import instructor
from pydantic import BaseModel
from instructor import OpenAISchema
import dotenv
from pprint import pprint
dotenv.load_dotenv()
from functools import wraps

# Enables `response_model`
client = instructor.patch(OpenAI())
client2 = OpenAI()

class UserDetail(OpenAISchema):
    '''return the result of 3 + 2'''
    name: str
    age: int

class Item(OpenAISchema):
    name: str
    price: int
    seller: str

class CallClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.func = lambda : print(self.name)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        @wraps(self.func)
        def wrapper(*args: Any, **kwds: Any) -> Any:
            return print("wrapping")
            # return self.func(*args, **kwds)
        return wrapper(*args, **kwds)

def main():
    u = UserDetail.openai_schema
    # pprint(UserDetail.openai_schema)
    res = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_model=UserDetail,
        messages=[
            {"role": "user", "content": "Extract Jason is 26 years old"},
        ]
    )

    # assert isinstance(user, UserDetail)
    # assert user.name == "Jason"
    # assert user.age == 25
    # print(user)
    # d = {"model":"gpt-3.5-turbo","messages":[{"role":"user","content":"Extract Jason is 26 years old"}],"functions":[{"name":"UserDetail","description":"Correctly extracted `UserDetail` with all the required parameters with correct types","parameters":{"properties":{"name":{"title":"Name","type":"string"},"age":{"title":"Age","type":"integer"}},"required":["age","name"],"type":"object"}}],"function_call":{"name":"UserDetail"}}
    # res = client2.chat.completions.create(
    #     **d
    # )

    pprint(res)
    c = CallClass("Jason", 25)
    c()


if __name__ == "__main__":
    main()