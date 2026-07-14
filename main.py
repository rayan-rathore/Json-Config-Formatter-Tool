from formatter import *
import json
import argparse

engine = JSONEngine()

parser = argparse.ArgumentParser(description="JSON Configuration and Formatter Tool")
parser.add_argument("filepath", help="The path to the JSON file you want to read")
parser.add_argument("--mode",choices=["--pretty","--minify"],required=True,
                    help="Choose the output formatting style")

args = parser.parse_args()
try:
    with open(args.filepath, "r") as file:

except FileNotFoundError:
    print(f"Error: The file {args.filepath} was not found in this folder.")
