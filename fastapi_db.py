from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg://postgres:12345@localhost:5432/fastapi_db"

# db.add()	    :Put object into session
# db.flush()    :Send pending SQL to DB within transaction
# db.commit()   :Save transaction permanently
# db.rollback() :Cancel current uncommitted transaction
# db.refresh()  :Reload object from database

engine = create_engine(DATABASE_URL)
# engine conncet with database 
print("Database connection created")

sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine )
# sessionmaker is a factory that creates SQLAlchemy database sessions.(It create a session for each API)
# autoflush send the SQL operation to the database within the current transaction.(like git add.)
#autocommit=False means SQLAlchemy will not automatically commit/save database changes.

def get_db():
    db = sessionLocal() # session created
    try:
        yield db 
        # yield allows FastAPI to use the database session during the request and then continue executing the function afterward. 

    finally:
        db.close()
        # close the database after all function exicuted.(Whether your API succeeds or faild)
     
def test_db():  
    try:
        with engine.connect() as connection:
            print('db connected succesfully')
    except Exception as err:
        print("Connection failed:", err)