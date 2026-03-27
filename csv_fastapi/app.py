from fastapi import FastAPI
from sqlalchemy import create_engine, text
from models import Student
from database import engine, Base
import pandas as pd
import os
from dotenv import load_dotenv


Base.metadata.create_all(bind=engine)

app = FastAPI()


try:
    
    df = pd.read_csv(r"C:\Users\LENOVO\Downloads\students_complete.csv")

    if 'gpa' in df.columns:
        df['gpa'] = df['gpa'].fillna(0)

    print("✅ Data Loaded Successfully")
    
except Exception as e:
    print("Error:", e)
    df = pd.DataFrame()


# -----------------------------
# Home API
# -----------------------------
@app.get("/")
def home():
    return {"message": "FastAPI is running with MySQL 🚀"}

# -----------------------------
# Get All Students
# -----------------------------

@app.get("/data")
def get_data():
    return df.to_dict(orient="records")

# -----------------------------
#  Get Specific Student by ID
# -----------------------------

@app.get("/student/{student_id}")
def get_student(student_id: str):

    print("Received:", student_id)

    result = df[df["student_id"] == student_id]

    if len(result) > 0:
        return result.to_dict(orient="records")
    else:
        return {"message": "Student not found"}