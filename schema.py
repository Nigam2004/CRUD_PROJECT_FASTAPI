from pydantic import BaseModel

class create_employee(BaseModel):
      name: str
      salary: int

class update_data(BaseModel):
      name: str
      salary: int

class create_company(BaseModel):
      name :str
      loc :str
      

