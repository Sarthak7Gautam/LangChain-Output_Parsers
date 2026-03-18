from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int


person:Person = {'name':'Rahul Gandhi','age':45}

print(person)