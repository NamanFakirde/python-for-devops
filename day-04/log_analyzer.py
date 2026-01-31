import json

def read_log():
    try: 
        with open("day-04/app.log","r") as file:
            lines = file.readlines()
            if not lines:
                raise ValueError("log file is empty")
            return lines
    except FileNotFoundError:
        print("File not Found")
        return 
    except ValueError as e:
        print(e)
        return
    
    
def log_analyzer(lines):
    log_count = {"INFO":0, "WARNING":0, "ERROR":0}

    for line in lines:
        if "INFO" in line:
            log_count["INFO"] += 1
        elif "WARNING" in line:
            log_count["WARNING"] += 1
        elif "ERROR" in line:
            log_count["ERROR"] += 1
        else:
            pass
    
    return log_count

def write_json(log_count):
    with open("day-04/log_summary.json","w+") as json_file:
        json.dump(log_count,json_file)



lines = read_log()
if lines:
    count = log_analyzer(lines)
    print("count is: ",count)
    write_json(count)