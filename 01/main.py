from fastapi import FastAPI
import json


app= FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data


@app.get("/")
def hello():
    return {'message':'Pateint Management System'}

@app.get("/about")
def about():
    return {'message':'A Fully Functional Api To Manage Records'}


@app.get("/view")
def view():
    data = load_data()
    return data