from fastapi import FastAPI, HTTPException,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field , computed_field
from typing import Annotated, Literal, Optional
import json

app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str,Field(...,description='Id Of Patient',examples=['P001'])]
    name: Annotated[str,Field(...,description='Name Of Patient')]
    city: Annotated[str,Field(...,description='Where Patient is Living')]
    age: Annotated[int,Field(...,gt=0,lt=120,description='Age of Patient ')]
    gender: Annotated[Literal['male','female','others'],Field(...,description='Gender of Patient ')]
    weight: Annotated[float,Field(...,gt=0,description='Weight of Patient ')]
    height: Annotated[float,Field(...,gt=0,description='Height of Patient ')]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi <18.5:
            return 'Underweight'
        elif self.bmi <25:
            return 'Normal'
        elif self.bmi <30:
            return 'Normal'
        else:
            return 'obese'
        

class PatientUpdate(BaseModel):

    name: Annotated[Optional[str],Field(default=None)]
    city: Annotated[Optional[str],Field(default=None)]
    age: Annotated[Optional[int],Field(default=None)]
    gender: Annotated[Optional[Literal['male','female','others']],Field(default=None)]
    weight: Annotated[Optional[float],Field(default=None,gt=0)]
    height: Annotated[Optional[float],Field(default=None,gt=0)]



def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)


@app.post('/create')
def create_patient(patient: Patient):


    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')
    
    data[patient.id] = patient.model_dump(exclude=['id'])


    save_data(data)

    return JSONResponse(status_code=201, content={'message':'Patient created Succesfully'})





@app.put('/edit/{patient.id}')

def update_patient(patient_id :str,patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not Found')
    
    existing_patient_info = data[patient_id]

    update_patient_info = patient_update.model_dump(exclude_unset=True)


    for key, value in update_patient_info.items():
        existing_patient_info[key] = value

    existing_patient_info['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_info)

    existing_patient_info = patient_pydantic_obj.model_dump(exclude='id')


    data[patient_id] = existing_patient_info


    save_data(data)


    return JSONResponse(status_code=200, content={'message':'patient updated'})




@app.delete('/delete/{patient_id}')
def delete_patient(patient_id :str):

    data=load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not Found')


    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient deleted'})










































# app= FastAPI()

# def load_data():
#     with open('patients.json','r') as f:
#         data = json.load(f)
#     return data


@app.get("/")
def hello():
    return {'message':'Pateint Management System'}

# @app.get("/about")
# def about():
#     return {'message':'A Fully Functional Api To Manage Records'}


# @app.get("/view")
# def view():
#     data = load_data()
#     return data

# @app.get('/patient/{patient_id}')
# # def view_patient(patient_id: str):
# def view_patient(patient_id: str = Path(...,description='ID Of Patient',example='P001')):
#     data = load_data()

#     if patient_id in data:
#         return data[patient_id]
#     # return {'error':'patient not found'}

#     raise HTTPException(status_code=404,detail='Patient not Found')



# @app.get('/sort')
# def sort_patients(sort_by: str = Query(...,description='Sort on The Baisis Of height , weight or bmi'),order:str = Query('asc',description='sort in asc or desc order')):

#     valid_fields = ['height','weight','bmi']


#     if sort_by not in valid_fields:
#         raise HTTPException(status_code=400,detail=f'Invalid field select from {valid_fields}')

#     if order not in ['asc','desc']:
#         raise HTTPException(status_code=400,detail=f'Invalid order select  between asc and desc ')
    

#     data = load_data()

#     sort_order = True if order=='desc'  else False


#     sorted_data = sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)

#     return sorted_data