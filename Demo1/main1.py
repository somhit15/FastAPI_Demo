from fastapi import FastAPI
import json

app1 = FastAPI()

def load_data():
    with open('patient_data.json', 'r') as f:
        data = json.load(f)
    return data

@app1.get("/")
def read_root():
    return {"Message": "Patient management system"}

@app1.get("/about")
def about():
    return {"message": "A fully functional API to manage patients"}


@app1.get("/view")
def view():
    data = load_data()
    return data

@app1.get("/add")
def add():
    return {"message": "This is add page"}