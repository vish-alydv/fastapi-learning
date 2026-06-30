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


# temp = patient1.model_dump()
temp = patient1.model_dump(exclude=['name','gender'])
temp = patient1.model_dump(exclude=['address':['state']])
temp = patient1.model_dump(include=['name','gender'])