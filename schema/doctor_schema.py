from pydantic import BaseModel

class DoctorBase(BaseModel):
    name: str
    specialization : str
    phone: str
    is_available : bool = True


class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    id : int