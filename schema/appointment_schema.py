from pydantic import BaseModel
from datetime import date
from typing import Optional

class AppointmentBase(BaseModel):
    patient_id : int
    doctor_id : int
    date : date

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(AppointmentBase):
    is_completed: Optional[bool] = False

class Appointment(AppointmentBase):
    id : int
    is_completed: bool = False
    