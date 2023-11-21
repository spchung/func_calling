from pydantic import BaseModel
'''
pydantic representations of types defs
'''

# function call
class FunctionArgument(BaseModel):
    name: str
    description: str
    default: str

class Function(BaseModel):
    name: str
    description: str
    arguments: FunctionArgument
