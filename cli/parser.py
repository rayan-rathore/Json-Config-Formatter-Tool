# Dedicated Argument Parser Configuration
import argparse



def get_inspector_parser():
    parser = argparse.ArgumentParser(description="A comprehensive JSON Inspector & DevTool CLI")

    #group for file input and targets
    file_group = parser.add_argument_group("File inputs and Targets")
    file_group.add_argument("filepath", help="The JSON target file.")
    file_group.add_argument("--diff_file", type=str, help="Path to second JSON file to"
                                                          "run structural comparison.")
    file_group.add_argument("--output", help="Takes a string path to save results.")
    file_group.add_argument("--in-place", action="store_true",
                            help="True/False flag For over-writing the original file.")
    file_group.add_argument("--backup", action="store_true",
                            help="True/False flag to creat a .back backup files.")

    #group for formatting JSON
    format_group = parser.add_argument_group("Formatting options")
    format_group.add_argument("--mode", required=False, choices=["pretty", "minify"],
                        help="Select the mode for formatting.")
    format_group.add_argument("--sort-keys",action="store_true",
                        help="True/False flag to alphabetize keys during formatting.")

    #group for analysis and inspection
    analysis_group = parser.add_argument_group("Analysis and inspection tools")
    analysis_group.add_argument("--stats", action="store_true",
                        help="True/False flag to count objects, keys, values and max depth")
    analysis_group.add_argument("--tree", action="store_true",
                        help="True/False flag to show visual structural branch view")
    analysis_group.add_argument("--search-key",
                        help="Takes a search string for matching keys")
    analysis_group.add_argument("--search-value",
                        help="Takes a search string for matching values")

    return parser
