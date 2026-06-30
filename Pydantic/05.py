from pydantic import BaseModel

class Address(BaseModel):

    city:str
    state:str
    pin : str

class Patient(BaseModel):
    name : str
    gender : str
    address : Address

address_dict = {'city':'grugram','state':'haryana','pin':'122001'}

address1 = Address(**address_dict)

info_dict = {"name":'abcd','gender':'male','address':address1}

patient1  = Patient(**info_dict)

print(patient1.name)
print(patient1.address.city)