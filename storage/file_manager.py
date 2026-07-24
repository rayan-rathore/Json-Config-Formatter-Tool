# Handles writing to files, in-place edits, and safety backups
"""This dedicated file manager module is responsible for writing strings to disk,
safely mutating user files, and handling safety duplications. """
from pathlib import Path
import shutil

class StorageManager:
    def __init__(self):
        pass

    #---Action 1: create backup---
    def create_backup_file(self, filepath):
        target_path = Path(filepath)

        if target_path.exists() and target_path.is_file():
            backup_path = target_path.with_name(target_path.name + ".bak")
            try:
                shutil.copy2(target_path,backup_path)
                print( f"[INFO] Backup created successfully at {backup_path.name}")
            except IOError as e:
                print( f"[ERROR]: Could not create backup file. {e}")
        else:
            print( f"[ERROR]: The file '{target_path}' does not exist.")

    #---Action 2: write output file---
    def write_to_file(self,target_path,content):
        with open(target_path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"[SUCCESS] Formatted JSON saved to '{target_path}.")

    #---Action 3: handle intelligent mutation---
    def save_result(self, original_path, output_path, in_place, content):
        #if "output_path" is provided by user: save one on output by using action 2
        if output_path is not None:
            print(f"[INFO] Both --output and --in-place provided. Saving safely to separate path ")
            self.write_to_file(output_path,content)

        #In-place only if no safe separate output path was requested
        elif in_place is True:
            self.create_backup_file(original_path) # Auto-backup before overwrite for safety!
            self.write_to_file(original_path,content)

        #else: simply print content on the screen
        else:
            print(content)




