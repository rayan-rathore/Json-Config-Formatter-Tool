# Application controller
"""main.py will not contain any complex logic algorithms. Its only job is to receive user
input from your argument parser, check what features were requested, and delegate the work
straight to your independent package managers."""
import sys
import json
import os
import argparse
from cli.parser import ParserCLI
from core.engine import JSONEngine
from storage.file_manager import StorageManager
from analyzer.tree_view import JSONTreeGenerator
from analyzer.validator import JSONValidator
from analyzer.statistics import JSONAnalyzer
from search.query_engine import JSONSearcher
from difference.comparator import JSONComparator
from batch.processor import BatchProcessor

def main():

    args = ParserCLI.get_inspector_parser().parse_args()
    engine = JSONEngine()
    storage = StorageManager()

    # Check for Batch Directory Mode First
    if os.path.isdir(args.filepath):
        batcher =BatchProcessor(engine,storage)
        batcher.process_directory(args.filepath, args.mode or engine.config.default_mode, args.sort_keys)
        sys.exit()

    # Run Safe Single File Operations
    if not os.path.isfile(args.filepath):
        print(f"[ERROR]: The targeted file '{args.filepath}'does not exist on disk.")
        sys.exit()
    try:
        with open(args.filepath, "r", encoding="uft-8") as file:
            raw_text = file.read()
            print(raw_text)
    except Exception as e:
        print(f"[ERROR]: {e}")

    # Intercept validation checks
    validator = JSONValidator()
    valid,error = validator.check_duplicate_keys(raw_text)
    if not valid:
        print(f"Validation failed! Reason: {error}")
        return

    # Process Analytical Options (Stats / Tree)
    data_dict = engine.validate_json(raw_text)
    if args.stats:
        analyzer = JSONAnalyzer()
        status_log = analyzer.traverse_explorer(data_dict)
        print("\n--- Structural Statistics Log ---")
        print(status_log)
    elif args.tree:
        tree_gen = JSONTreeGenerator()
        print("\n--- Visual Tree Layout ---")
        tree_gen.generate_tree(data_dict)

    # Process Query Engine Options (Search Key / Value)
    searcher = JSONSearcher()
    if args.search_key:
        key_matches = searcher.search_key(data_dict,args.search_key)
        print(f"\n--- Search key results for '{args.search_key}'")
        if key_matches:
            for path in key_matches:
                print(path)
        else:
            print(f"No matching path found for {args.search_key}.")
    elif args.search_value:
        value_matches =  searcher.search_value(data_dict,args.search_value)
        print(f"\n--- Search value results for '{args.search_value}'")
        if value_matches:
            for path in value_matches:
                print(path)
        else:
            print(f"No matching path found {args.search_value}")

    # Process Diff Comparator Operations
    if args.diff_file:
        print(f"\n--- Starting structural comparison against: {args.diff_file}.")

        if not os.path.isfile(args.diff_file):
            print(f"[ERROR]: Comparative file '{args.diff_file}' does not exist on the disk.")
        else:
            try:
                with open(args.diff_file, "r", encoding="utf-8") as file:
                    raw_text_b = file.read()

                data_dict_b = engine.validate_json(raw_text_b)
                comparator = JSONComparator()

                mismatches = comparator.compare_json(data_dict,data_dict_b)

                print("\n--- Structural Differences Found ---")
                if mismatches:
                    for diff in mismatches:
                        print(diff)
                else:
                    print("No mismatch found! The structure match perfectly.")
            except Exception as e:
                print(f"Comparison aborted. failed to process comparative file: {e}")

    # Execute Formatting and Output Results
    if args.backup:
        storage.create_backup_file(args.filepath)
        #print(f"[BACKUP] Creating safety backup file for: {args.filepath}

    active_mode = args.mode

    if active_mode is None:
        active_mode = engine.config.default_mode

    if active_mode == "pretty":
        formatted_content = engine.format_json(data_dict,args.sort_keys)

    elif active_mode == "minify":
        formatted_content = engine.compact_json(data_dict,args.sort_keys)

    else:
        print(f"[ERROR] Unknown mode '{active_mode}' encountered.")

    result = storage.save_result(
        original_path = args.filepath,
        output_path= args.output,
        in_place=args.in_place,
        content=formatted_content
    )
    print("[SUCCESS] Formatting and output routine executed cleanly.")

if __name__ == "__main__":
    main()