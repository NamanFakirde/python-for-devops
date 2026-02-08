import json
import argparse


class log_analayzer:
    
    def __init__(self, log_file):
        self.log_file = log_file
        self.log_count = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    def read_log(self):
        try: 
            with open(self.log_file, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            print("Log file not found:", self.log_file)
            return None
        
    def analyzer(self, lines):

        self.log_count = {"INFO": 0, "WARNING": 0, "ERROR": 0}

        for line in lines:
            if "INFO" in line:
                self.log_count["INFO"] += 1
            elif "WARNING" in line:
                self.log_count["WARNING"] += 1
            elif "ERROR" in line:
                self.log_count["ERROR"] += 1
        
        return self.log_count

    def write_json(self, output_file):
        with open(output_file, "w") as json_file:
            json.dump(self.log_count, json_file, indent=4)


def main():

    parser = argparse.ArgumentParser(
        description="log analyzer CLI tool"
    )

    parser.add_argument(
        "logfile",
        help="path to log file"
    )

    parser.add_argument(
        "--output",
        default="summary.json",
        help="Output file name (default: summary.json)"
    )

    args = parser.parse_args()

    analyzer = log_analayzer(args.logfile)
    lines = analyzer.read_log()

    if not lines:
        print("No log in file")
        return 

    result = analyzer.analyzer(lines)

    print("log analysis summary:")
    for level, count in result.items():
        print(f"{level}: {count}")

    
    analyzer.write_json(args.output)


if __name__ == "__main__":
    main()
