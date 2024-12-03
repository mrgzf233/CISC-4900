# Option + Command + L for reformat on mac

import argparse
import csv
import json
import os
from validate_ka import validate_csv_content

# File name, method name

parser = argparse.ArgumentParser()
parser.add_argument(
    "--input-file",  # Input CSV
    required=True,
)
parser.add_argument(
    "--output-file",  # Output json
    required=True,
)
args = parser.parse_args()  # Store the parsed arguments

file_path = args.input_file
output_file = args.output_file


# Function to convert the CSV file into a JSON file
def csv_to_json(file_path, output_file):
    # Validate CSV file
    if not validate_csv_content(file_path):
        print("CSV validation failed. Exiting...")
        return

    # Dictionary to store the final JSON structure
    all_dict = {
        "curriculum": "cs2013",  # Curriculum name
        "knowledge-areas": []  # Empty list to store knowledge areas
    }

    # Read the CSV file
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)  # Read CSV rows as dictionaries

        for row in reader:
            # Build the JSON object for each knowledge area
            ka_data = {
                "short-ka": row['short_ka'],  # Short name of the knowledge area
                "long-ka": row['ka'],  # Full name of the knowledge area
                "begin-page": int(row['page_begin']),  # Start page number
                "end-page": int(row['page_end'])  # End page number
            }
            # Append each knowledge area JSON object to the list
            all_dict["knowledge-areas"].append(ka_data)

    # Write the final JSON structure to the output file
    with open(output_file, 'w') as jsonfile:
        json.dump(all_dict, jsonfile, indent=2)  # Pretty-print JSON with indentation
    print("JSON file created.")

# Run the conversion process
csv_to_json(file_path, output_file)