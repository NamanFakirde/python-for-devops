import json

class log_analayzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.log_count = {"INFO":0, "WARNING":0, "ERROR":0}

    def read_log(self):
        try: 
            with open(self.log_file,"r") as file:
                return file.readlines()
        except FileNotFoundError:
            print("Log file not found", self.log_fle)
            return
        
    def analyzer(self, lines):

        for line in lines:
            if "INFO" in line:
                self.log_count["INFO"] += 1
            elif "WARNING" in line:
                self.log_count["WARNING"] += 1
            elif "ERROR" in line:
                self.log_count["ERROR"] += 1
            else:
                pass
        
        return self.log_count

    def write_json(self):
        with open("day-05/log_summary_oop.json","w+") as json_file:
            json.dump(self.log_count,json_file)

def main():
    analyzer = log_analayzer("day-05/app.log")
    lines = analyzer.read_log()

    if not lines:
        print("No log in file")
        return 
    result = analyzer.analyzer(lines)

    print("log analysis summary:")
    for level, count in result.items():
        print(f"{level}: {count}")
    write = analyzer.write_json()

    

if __name__ == "__main__":
    main()

