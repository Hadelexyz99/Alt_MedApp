from fastapi import APIRouter , HTTPException
from typing import List
from schema.patient_schema import Patient, PatientCreate

patient_router = APIRouter()

patients: List[Patient] = [
    Patient(id=1, name="Alice", age=25, sex="Female", weight=60.5, height=165, phone="1111111111"),
    Patient(id=2, name="Bob", age=30, sex="Male", weight=75.0, height=180, phone="2222222222")
]

@patient_router.post('/', status_code=201)
def create_patient(payload: PatientCreate):
    patient_id = len(patients) + 1
    new_patient = Patient(
        id=patient_id,
        name=payload.name,
        age=payload.age,
        sex=payload.sex,
        weight=payload.weight,
        height=payload.height,
        phone=payload.phone
    )
    patients.append(new_patient)
    return {'message': 'Patient created successfully', 'data': new_patient}

@patient_router.get('/', status_code=200)
def list_patients():
    return {'message': 'Success', 'data': patients}


@patient_router.put('/{patient_id}', status_code=200)
def update_patient(patient_id: int, payload: PatientCreate):
    for patient in patients:
        if patient.id == patient_id:
            patient.name = payload.name
            patient.age = payload.age
            patient.sex = payload.sex
            patient.weight = payload.weight
            patient.height = payload.height
            patient.phone = payload.phone
            return {'message': 'Patient details updated successfully', 'data': patient}
    raise HTTPException(status_code=404, detail='Patient not found')

@patient_router.delete('/{patient_id}', status_code=200)
def delete_patient(patient_id: int):
    patients
    initial_length = len(patients)
    patients = [patient for patient in patients if patient.id != patient_id]
    
    if len(patients) == initial_length:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    return {'message': 'Patient deleted successfully'}



