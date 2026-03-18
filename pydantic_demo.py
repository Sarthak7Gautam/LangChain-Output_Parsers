from pydantic import BaseModel,Field
from typing import Optional

class Student(BaseModel):

    name:str ='Sarthak Gautam'
    age:Optional[int] = None
    driving_license:int = Field(gt=18,lt=50) ## field is used for adding constraints

new_student = {'age':'12','driving_license':20}

student = Student(**new_student)

print(student)

