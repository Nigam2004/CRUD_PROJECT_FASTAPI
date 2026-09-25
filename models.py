from sqlalchemy import Integer, String,Column
from sqlalchemy.orm import declarative_base
from fastapi_db import engine

base=declarative_base()


class emploee(base):
    __tablename__="Employee"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    salary = Column(Integer)

class company(base):
    __tablename__="company"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    loc = Column(String(100))

base.metadata.create_all(engine)