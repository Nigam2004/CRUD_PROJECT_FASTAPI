from fastapi import FastAPI, Depends,HTTPException,Query
from fastapi_db import get_db,test_db
from services import register_employee, getEmplyees
from sqlalchemy.orm import Session
from schema import create_employee
app=FastAPI()
test_db()
print("========== MAIN.PY LOADED ==========")
@app.post("/")
def create_new_employee(data:create_employee,db:Session=Depends(get_db)):
    print("MAIN ENDPOINT CALLED")
    print("DATA:", data)
    return register_employee(db,data)

## QUERY PARAMETERS
@app.get("/geteEmployees")
def get_employee(db:Session=Depends(get_db),e_id:int|None=Query(None)):
    print("geteEmployees CALLED")
    return getEmplyees(db,e_id)

