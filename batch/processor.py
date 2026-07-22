# Handles recursive folder scanning and multi-file batch operations
"""This module implements folder-scaling features:
Recursive Folder Formatter: Automatically crawling into subfolders to
track down files.
Batch Processing: Executing your formatting engine on every single .json
file it discovers during the sweep."""

import os

from storage import file_manager
from core import engine
class BatchProcessor:

    def __init__(self, formatter_engine, storage_manager):
        # Save instances from dependency injection cleanly
        self.formatter_engine = formatter_engine
        self.storage_manager = storage_manager

    def process_directory(self, directory_path, mode, sort_keys):
        processed_count = 0

        # Check if the folder even exists before looping to ensure defensive stability
        if not os.path.exists(directory_path):
            print(f"[ERROR] Directory '{directory_path}' does not exist.")
            return processed_count

        for root, dirs, files in os.walk(directory_path):
            for filename in files:
                if filename.endswith(".json"):
                    full_filename_path = os.path.join(root, filename)

                    try:
                        with open(full_filename_path, "r", encoding="utf-8") as file:
                            text = file.read()

                        data = self.formatter_engine.engine.validate_json(text)

                        if not isinstance(data,str):
                            formatted_content = None

                            if mode == "pretty":
                                formatted_content = self.formatter_engine.format_json(data,sort_keys)
                            elif mode == "minify":
                                formatted_content = self.formatter_engine.compact_json(data,sort_keys)

                            self.storage_manager.write_to_file(full_filename_path,formatted_content)
                            processed_count += 1

                    except SystemError as e:
                        print(e)
        print(processed_count)



