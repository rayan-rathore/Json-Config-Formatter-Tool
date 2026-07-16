import sys
from formatter import *
import json
import argparse


parser = argparse.ArgumentParser(description="JSON Configuration and Formatter Tool")
parser.add_argument("filepath", help="The path to the JSON file you want to read")
parser.add_argument("--mode",choices=["pretty","minify"],required=False,
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

active_mode = args.mode
if active_mode is None:
    active_mode = engine.config.default_mode


if active_mode == "pretty":
    result = engine.modify(data)
    print(result)
elif active_mode == "minify":
    result = engine.minify(data)
    print(result)
else:
    print(f"[ERROR] Unknown mode '{active_mode}' encountered.")
