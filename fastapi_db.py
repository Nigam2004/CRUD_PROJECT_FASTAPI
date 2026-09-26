from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg://postgres:12345@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL)
print("Database connection created")

sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine )
def get_db():
    db = sessionLocal()

    try:
        yield db
    finally:
        db.close()
     
def test_db():  
    try:
        with engine.connect() as connection:
            print('db connected succesfully')
    except Exception as err:
        print("Connection failed:", err)