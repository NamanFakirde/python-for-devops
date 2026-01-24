# You will create a Python script that:

# Calls a public API (example: GitHub API, JSONPlaceholder) list
# Fetches data using the requests library
# Parses the JSON response
# Extracts meaningful information from the response
# Prints the processed output to the terminal
# Saves the processed data into a JSON file

import requests
import json


name = input("Enter the name: ")
api_url = f"https://api.agify.io/?name={name}"
response = requests.get(url= api_url)

# print(dir(response))          # just to check what operations we can perform on the responses
for key,value in response.json().items():
    print(key,value)
    data = response.json()
    
with open("day-02/task2_output.json", "w") as f:
    json.dump(data, f)