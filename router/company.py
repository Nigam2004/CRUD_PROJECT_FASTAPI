from fastapi import APIRouter,Depends ,Query,HTTPException
from models import company
from schema import create_company
from fastapi_db import get_db
from sqlalchemy.orm import Session

#Router in fastAPI

router=APIRouter()

#POST API

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

#GET API
@router.get("/companyDetails")
def get_Details(query_id:int=Query(id),db:Session=Depends(get_db)):
 
    company_details=db.query(company).filter(company.id==query_id).first()
    if  not company_details:
        raise HTTPException(
            # fastapi status code erorr  through                 
            status_code=404,
            detail=f"not found query_id {query_id}"
                       )
    return{
         "res":f"result fetched succesfully gainst {query_id}",
         "details":{
              "id":company_details.id,
              "name":company_details.name
         }
    }
     