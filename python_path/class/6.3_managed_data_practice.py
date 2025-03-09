#convert a csv file to a json file

import json
import csv

#define file paths
csv_file_path = "Resources/practice_data.csv"
json_file = "Resources/practice_data.json"

# Read the CSV file and write to JSON
with open(csv_file_path, mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file) # Read rows as dictionaries
    data = list(csv_reader) # conver to a list of dictionaries

with open(json_file, mode="w") as json_file:
    json.dump(data, json_file, indent=4) # Write to JSON file with formatting

print(f"CSV converted to JSON and saved as {json_file}.")

