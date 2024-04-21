from typing import List
from schema.doctor_schema import Doctor

def is_doctor_available(doctors: List[Doctor]) -> bool:
        for doctor in doctors:
            if doctor.is_available:
                return True
    
    # Return False if no doctor is available
        return False
