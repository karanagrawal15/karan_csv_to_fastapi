from fastapi import FastAPI
import pandas as pd

app = FastAPI()

try:
    # FIX: remove sep="\t"
    df = pd.read_csv(r"C:\Users\LENOVO\Downloads\students_complete.csv")

    # Optional: check if column exists before filling
    if 'gpa' in df.columns:
        df['gpa'] = df['gpa'].fillna(0)

    print("Data Loaded Successfully")
    print(df.head())  # Debug check

except Exception as e:
    print("Error:", e)
    df = pd.DataFrame()

@app.get("/")
def home():
    return {"message": "FastAPI is running successfully 🚀"}

@app.get("/data")
def get_data():
    return df.to_dict(orient="records")


# -----------------------------
#  Get Specific Student by ID
# -----------------------------
@app.get("/customer")
def get_customer(student_id: str):

    # DEBUG LINE
    print("Received:", student_id)

    result = df[df["student_id"] == student_id]

    if len(result) > 0:
        return result.to_dict(orient="records")
    else:
        return {"message": "Student not found"}
    