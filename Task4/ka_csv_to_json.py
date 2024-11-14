import argparse
import csv
import json
import os

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


def csv_to_json(file_path, output_file):
    knowledge_areas = []
