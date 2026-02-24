from fastapi import FastAPI
import psycopg
import os
import time
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

def wait_for_db():
    print(os.getenv("DB_HOST"),":", os.getenv("DB_NAME"), ":", os.getenv("DB_USER"), ":", os.getenv("DB_PASSWORD"))
  
    for i in range(10):
        try:
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD")
            )
            conn.close()
            return True
        except:
            time.sleep(2)
    return False

@app.get("/")
def read_root():
    if wait_for_db():
        return {"database": "connected"}
    else:
        return {"database": "connection failed"}