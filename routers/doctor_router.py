from fastapi import APIRouter , HTTPException
from typing import List
from schema.doctor_schema import Doctor, DoctorCreate

doctor_router = APIRouter()

doctors: List[Doctor] = [
    Doctor(id=1, name="Dr. John Doe", specialization="Cardiologist", phone="1234567890"),
    Doctor(id=2, name="Dr. Jane Smith", specialization="Pediatrician", phone="0987654321")
]

@doctor_router.post('/', status_code=201)
def create_doctor(payload: DoctorCreate):
    doctor_id = len(doctors) + 1
    new_doctor = Doctor(
        id=doctor_id,
        name=payload.name,
        specialization=payload.specialization,
        phone=payload.phone,
        is_available=payload.is_available
    )
    doctors.append(new_doctor)
    return {'message': 'Doctor created successfully', 'data': new_doctor}

@doctor_router.get('/', status_code=200)
def list_doctors():
    return {'message': 'Success', 'data': doctors}


@doctor_router.put('/{doctor_id}', status_code=200)
def update_doctor(doctor_id: int, payload: DoctorCreate):
    for doctor in doctors:
        if doctor.id == doctor_id:
            doctor.name = payload.name
            doctor.specialization = payload.specialization
            doctor.phone = payload.phone
            doctor.is_available = payload.is_available
            return {'message': 'Doctor details updated successfully', 'data': doctor}
    raise HTTPException(status_code=404, detail='Doctor not found')

@doctor_router.delete('/{doctor_id}', status_code=200)
def delete_doctor(doctor_id: int):
    initial_length = len(doctors)
    doctors[:] = [doctor for doctor in doctors if doctor.id != doctor_id]
    
    if len(doctors) == initial_length:
        raise HTTPException(status_code=404, detail='Doctor not found')
    
    return {'message': 'Doctor deleted successfully'}


@doctor_router.put('/{doctor_id}/set_availability', status_code=200)
def set_availability(doctor_id: int, is_available: bool):
    doctor = next((doc for doc in doctors if doc.id == doctor_id), None)
    
    if doctor is None:
        raise HTTPException(status_code=404, detail='Doctor not found')
    
    doctor.is_available = is_available
    
    return {'message': 'Doctor availability updated successfully', 'data': doctor}


