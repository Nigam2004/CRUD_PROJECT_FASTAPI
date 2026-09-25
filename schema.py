from pydantic import BaseModel

class create_employee(BaseModel):
      id = int
      name = str
      salary = str