from fastapi import FastAPI, Depends,HTTPException,Query
from fastapi_db import get_db,test_db
from services import register_employee, getEmplyees,getEmplyees_by_id,updateEmployee,deleteEmployee
from sqlalchemy.orm import Session
from schema import create_employee,update_data
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

## path parameter
@app.get("/geteEmployees/{e_id}")
def get_employee(e_id:int,db:Session=Depends(get_db)):
    # In Python, a parameter with a default value cannot come before a parameter without a default value.
    print("geteEmployees/e_id CALLED")
    return getEmplyees_by_id(db,e_id)


#update API
@app.put("/updateEmp")
def update_employee(e_id:int,data:update_data,db:Session=Depends(get_db)):
    print("updated api called")
    return updateEmployee(db,e_id,data)

#delet API
@app.delete("/deleteEmp")
def delete_employee(e_id:int,db:Session=Depends(get_db)):
     print("delete api called")
     return deleteEmployee(db,e_id)

    
