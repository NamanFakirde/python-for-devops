from fastapi import APIRouter
from services.log_service import log_analyzer

router = APIRouter()

@router.get("/log")
def analyze_log():
    """
    This function analyzes the log and prints the count 
    """
    count_log = log_analyzer()
    return count_log
    