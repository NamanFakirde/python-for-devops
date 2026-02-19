# script to analyze the logs from a file

import json

def log_analyzer():
    """
    Analyzes the log in a log file
    """
    log_count = {"INFO":0, "WARNING":0, "ERROR":0}
    
    with open("services/app.log","r") as file:
        for line in file:
            if "INFO" in line:
                log_count["INFO"] += 1
            elif "WARNING" in line:
                log_count["WARNING"] += 1
            elif "ERROR" in line:
                log_count["ERROR"] += 1
            
    return{
        "INFO":log_count["INFO"],
        "WARNING":log_count["WARNING"],
        "ERROR":log_count["ERROR"]
    }