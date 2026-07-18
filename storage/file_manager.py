# Handles writing to files, in-place edits, and safety backups
"""This dedicated file manager module is responsible for writing strings to disk,
safely mutating user files, and handling safety duplications. """
from pathlib import Path
import os
import shutil

class StorageManager:
    def __init__(self):
        pass

    def create_backup(self, filepath):
        target_path = Path(filepath)
        if target_path.exists() and filepath.is_file():
            backup_path = target_path.with_name(target_path.name + ".back")
            try:
                shutil.copy2(target_path,backup_path)
                return f"Backup created successfully: {backup_path.name}"
            except IOError as e:
                return f"ERROR: Could not create backup file. {e}"
        else:
            return f"Error: The file '{target_path}' does not exist."


    def output_file(self):
        
