from sqlalchemy.orm import Session
from schema import create_employee
from models import Employee


def register_employee(db: Session, data: create_employee):

    print("1. SERVICE STARTED")
    print("2. DATA RECIEVED:", data)

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