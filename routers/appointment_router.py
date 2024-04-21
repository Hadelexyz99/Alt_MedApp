from fastapi import APIRouter, HTTPException
from typing import List
from schema.appointment_schema import Appointment, AppointmentCreate
from schema.doctor_schema import Doctor
from schema.patient_schema import Patient
from routers.doctor_router import doctors
from routers.patient_router import patients

appointment_router = APIRouter()

appointments: List[Appointment] = []

def is_patient_exist(patient_id: int) -> bool:
    return any(patient.id == patient_id for patient in patients)

@appointment_router.post('/', status_code=201)
def create_appointment(payload: AppointmentCreate):
    # Check if the patient exists
    if not is_patient_exist(payload.patient_id):
        raise HTTPException(status_code=400, detail='Patient does not exist')
    
    # Check if any doctor is available
    available_doctors = [doctor for doctor in doctors if doctor.is_available]
    
    if not available_doctors:
        raise HTTPException(status_code=400, detail='No doctors available')
    
    # Find the first available doctor
    doctor = available_doctors[0]
    
    # Create a new appointment
    appointment_id = len(appointments) + 1
    new_appointment = Appointment(
        id=appointment_id,
        patient_id=payload.patient_id,
        doctor_id=doctor.id,
        date=payload.date,
        doctors_id=doctor.id
    )
    
    appointments.append(new_appointment)
    
    # Update the doctor's availability
    doctor.is_available = False
    
    return {'message': 'Appointment created successfully', 'data': new_appointment}

@appointment_router.put('/{appointment_id}/complete', status_code=200)
def complete_appointment(appointment_id: int):
    # Find the appointment by ID
    appointment = next((appt for appt in appointments if appt.id == appointment_id), None)
    
    if appointment is None:
        raise HTTPException(status_code=404, detail='Appointment not found')
    
    # Update the doctor's availability
    doctor = next((doc for doc in doctors if doc.id == appointment.doctor_id), None)
    
    if doctor is None:
        raise HTTPException(status_code=404, detail='Doctor not found')
    
    doctor.is_available = True
    
    # Update the appointment status to completed
    appointment.is_completed = True
    
    return {'message': 'Appointment completed successfully', 'data': appointment}

@appointment_router.put('/{appointment_id}/cancel', status_code=200)
def cancel_appointment(appointment_id: int):
    # Find the appointment by ID
    appointment = next((appt for appt in appointments if appt.id == appointment_id), None)
    
    if appointment is None:
        raise HTTPException(status_code=404, detail='Appointment not found')
    
    # Update the appointment status to canceled
    appointment.is_completed = False
    
    # Update the doctor's availability to True
    doctor = next((doc for doc in doctors if doc.id == appointment.doctor_id), None)
    
    if doctor is not None:
        doctor.is_available = True
    
    return {'message': 'Appointment canceled successfully', 'data': appointment}

    # Find the appointment by ID
    appointment = next((appt for appt in appointments if appt.id == appointment_id), None)
    
    if appointment is None:
        raise HTTPException(status_code=404, detail='Appointment not found')
    
    # Update the appointment status to canceled
    appointment.is_completed = False
    
    # The doctor becomes automatically unavailable when the appointment is canceled
    
    return {'message': 'Appointment canceled successfully', 'data': appointment}
