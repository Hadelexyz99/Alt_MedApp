from pydantic import BaseModel

class PatientBase(BaseModel):
    name : str
    age: int
    sex: str
    weight: float
    height: float
    phone: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id : int
    
