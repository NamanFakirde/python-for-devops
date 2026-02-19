from fastapi import APIRouter, HTTPException
from services.health_service import get_system_meterics

router = APIRouter()

@router.get("/health",status_code=200)
def get_metrics():
    """
    This function fetches the system matrics and creates an endpoint to connect with the API 
    """
    try:
        system_info = get_system_meterics()
        return system_info
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )