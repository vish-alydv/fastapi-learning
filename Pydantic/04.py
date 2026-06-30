from pydantic import BaseModel , EmailStr , computed_field
from typing import List , Dict



class Patient(BaseModel):

    name:str
    email: EmailStr
    age: int
    weight : float
    height : float
    married : bool
    allergies : List[str]
    contact_details: Dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    

    
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("Bmi",patient.bmi)
    print('inserted')


patient_info = {
    'name': 'nitish',
    'email': 'abc@hdfc.com',
    'age': 70,
    'weight': 54356.5,
    'height': 156.5,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'phone': '23456',
        'emergency':'6767'
    }
}


patient1 = Patient(**patient_info)


insert_patient_data(patient1)