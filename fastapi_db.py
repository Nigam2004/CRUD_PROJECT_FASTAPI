from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg://postgres:12345@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL)
print("Database connection created")

try:
    with engine.connect() as connection:
        print('db connected succesfully')
except Exception as err:
      print("Connection failed:", err)