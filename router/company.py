from fastapi import APIRouter,Depends 
from models import company
from schema import create_company
from fastapi_db import get_db
from sqlalchemy.orm import Session

#Router in fastAPI

router=APIRouter()

@router.post("/register_company")
def register_company(data: create_company,db:Session=Depends(get_db)):
    try:
        new_company = company(**data.model_dump())
        db.add(new_company)
        db.commit()
        db.refresh(new_company)
    except Exception as err:
            db.rollback()
            print(type(err).__name__)
            print(err)
            raise

    return {
            "msg": "Data inserted successfully",
            "data": {
                "id": new_company.id,
                "name": new_company.name,
                "loc": new_company.loc
            }
        }