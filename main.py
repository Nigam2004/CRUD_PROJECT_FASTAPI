from fastapi import FastAPI, Depends,HTTPException
from fastapi_db import get_db,test_db
from services import register_employee
from sqlalchemy.orm import Session
from schema import create_employee
app=FastAPI()
test_db()
print("========== MAIN.PY LOADED ==========")
@app.post("/")
def create_new_employee(
    data:create_employee,
    db:Session=Depends(get_db)):
    print("MAIN ENDPOINT CALLED")
    print("DATA:", data)
    return register_employee(db,data)
    