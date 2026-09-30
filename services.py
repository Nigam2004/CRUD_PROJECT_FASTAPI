from sqlalchemy.orm import Session
from schema import create_employee,update_data
from models import Employee
from fastapi import HTTPException

#employee services
def register_employee(db: Session, data: create_employee):

    print("1. SERVICE STARTED")

    try:
        new_employee = Employee(**data.model_dump())
        print("3. EMPLOYEE OBJECT CREATED:", new_employee)

        db.add(new_employee)
        print("4. DATA ADDED TO SESSION")

        db.commit()
        print("5. COMMIT SUCCESS")

        db.refresh(new_employee)
        print("6. REFRESH SUCCESS")

    except Exception as err:
            db.rollback()
            print("========== DATABASE ERROR ==========")
            print(type(err).__name__)
            print(err)
            print("====================================")
            raise

    return {
            "msg": "Data inserted successfully",
            "data": {
                "id": new_employee.id,
                "name": new_employee.name,
                "salary": new_employee.salary
            }
        }

    # except Exception as err:
    #     db.rollback()
    #     print("========== DATABASE ERROR ==========")
    #     print(type(err).__name__)
    #     print(err)
    #     print("====================")
    #     raise


## QUERY PARAMETERS
def getEmplyees(db:Session,e_id):
    #  print("from db:",employees)
     if e_id:
          employees = db.query(Employee).filter(Employee.id==e_id).first()
     else:
            employees = db.query(Employee).all()
            for emp in employees:
                print("from db:\n",{
                    "id":emp.id,
                    "name":emp.name,
                    "slary":emp.salary   
                            })
     return {"Respons":employees}


## path parameter
def getEmplyees_by_id(db:Session,e_id):
    #  print("from path parameter:",employees)
        employees = db.query(Employee).filter(Employee.id==e_id).first()
        return {"Respons":employees}

##Update services
def updateEmployee(db:Session,e_id,data:update_data):
      employees = db.query(Employee).filter(Employee.id==e_id).first()
      if not employees:
            print(f"no record found for {e_id}")
            raise HTTPException(
                # fastapi status code erorr  through                 
                status_code=404,
                detail=f"not found e_id {e_id}"
            )
      employees.name= data.name
      employees.salary=data.salary
      db.commit()
      db.refresh(employees)
      return{
        "msg": "Employee updated successfully",
        "data": {
            "id": employees.id,
            "name": employees.name,
            "salary": employees.salary
            }
        }


##delete employee  services
def deleteEmployee(db:Session,e_id):
    employees = db.query(Employee).filter(Employee.id==e_id).first()
    if not employees:
            print(f"no record found for {e_id}")
            raise HTTPException(
                # fastapi status code erorr  through                 
                status_code=404,
                detail=f"not found e_id {e_id}"
                )
    db.delete(employees)
    db.commit()

    return{
          "res":"Employee deleted successfully",
          "id": e_id
    }


