import sys
from formatter import *
import json
import argparse


parser = argparse.ArgumentParser(description="JSON Configuration and Formatter Tool")
parser.add_argument("filepath", help="The path to the JSON file you want to read")
parser.add_argument("--mode",choices=["pretty","minify"],required=True,
                    help="Choose the output formatting style")

args = parser.parse_args()

try:
    with open(args.filepath, "r") as file:
        content = file.read()
except FileNotFoundError:
    print(f"Error: The file {args.filepath} was not found in this folder.")
    sys.exit()

engine = JSONEngine()
data = engine.validation(content)

if isinstance(data,str):
    print(data)
    sys.exit()
else:
    if args.mode == "pretty":
        result = engine.modify(data)
        print(result)
    elif args.mode == "minify":
        result = engine.minify(data)
        print(result)