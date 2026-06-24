from pydantic import BaseModel, AnyUrl, Field
from typing import List,Dict,Optional ,Annotated

class Patient(BaseModel):
    name:Annotated[str, Field(max_length=50,title='Name Of Patient',description='Give the name of patient inless than 50 char',examples=['Vishal'])]
    # url: AnyUrl   
    email:str 
    age:int = Field(gt=0 , lt=120)
    weight:float = Field(gt=0)
    married:Annotated[bool, Field(default=None,description='Is The Patient Married')
    allergies: Optional[List[str]] =None
    contact_details: Dict[str,str]



def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')


def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('updated')


patient_info = {'name':'Disco','email':'abc@gmail.com', 'age':30,'weight':56.5,'married':True,'contact_details':{'email':'abc@gmail.com','phone':'23456'}}


patient1 = Patient(**patient_info)


insert_patient_data(patient1)
# update_patient_data(patient1)