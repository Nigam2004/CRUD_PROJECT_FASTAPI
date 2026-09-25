from fastapi import FastAPI
from fastapi_db import engine

app=FastAPI()

@app.get("/")
def home():
    try:
        with engine.connect():
            return'db connected succesfully'
    except Exception as err:
             return 'db connected fail'