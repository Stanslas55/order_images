import os
import shutil
import tkinter as tk
from tkinter import filedialog
import re

def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')  # Use infinity for non-numeric filenames

def count_and_rename_images(root_folder, output_folder):
    # Collect all image file paths
    image_files = []
    for subdir, dirs, files in os.walk(root_folder):
        dirs.sort()  # Sort directories alphabetically
        sorted_files = sorted(files, key=lambda x: (extract_number(x), x))
        for file in sorted_files:  # Sort files numerically, then alphabetically
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')):
                image_files.append(os.path.join(subdir, file))
    
    # Determine the total number of files
    total_files = len(image_files)
    zfill_length = len(str(total_files))

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Copy and rename files
    for index, file_path in enumerate(image_files):
        # Keep the original extension
        file_extension = os.path.splitext(file_path)[1]
        new_file_name = f"{str(index + 1).zfill(zfill_length)}{file_extension}"
        new_file_path = os.path.join(output_folder, new_file_name)
        shutil.copy2(file_path, new_file_path)
        print(f"Copied '{file_path}' to '{new_file_path}'")

def browse_folder(title):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory(title=title)
    return folder_path

if __name__ == "__main__":
    source_folder = browse_folder("Select the source folder")
    if not source_folder:
        print("Source folder selection cancelled.")
    else:
        destination_folder = browse_folder("Select the destination folder")
        if not destination_folder:
            print("Destination folder selection cancelled.")
        else:
            count_and_rename_images(source_folder, destination_folder)
