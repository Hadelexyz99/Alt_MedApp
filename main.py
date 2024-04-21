from fastapi import FastAPI
from routers.doctor_router import doctor_router
from routers.patient_router import patient_router
from routers.appointment_router import appointment_router

# Create an instance of the FastAPI class
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


app.include_router(patient_router, prefix="/patients", tags=["patients"])
app.include_router(doctor_router, prefix="/doctors", tags=["doctors"])
app.include_router(appointment_router, prefix="/appointments", tags=["appointments"])



