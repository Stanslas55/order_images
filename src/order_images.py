import os
import tkinter as tk
from tkinter import filedialog

# Function to check if a file has an image file extension
def is_image(filename):
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']
    return any(filename.lower().endswith(ext) for ext in image_extensions)

# Function to rename images in a folder
def rename_images(folder_path):
    # Get the list of image files in the folder
    image_files = [f for f in os.listdir(folder_path) if is_image(f)]
    # Sort the files numerically
    image_files.sort(key=lambda x: int(os.path.splitext(x)[0]))
    
    # Determine the padding length
    padding_length = len(str(len(image_files)))
    
    # Rename the files with padded numbers
    for i, filename in enumerate(image_files):
        # Generate the new filename with padded number
        new_filename = str(i+1).zfill(padding_length) + os.path.splitext(filename)[1]
        
        # Rename the file
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        print(f"Renamed {filename} to {new_filename}")

# Function to browse for a folder and initiate renaming process
def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        rename_images(folder_path)
        status_label.config(text="Images renamed successfully!")

# Create the main window
root = tk.Tk()
root.title("Image Renamer")

# Create and pack the browse button
browse_button = tk.Button(root, text="Browse Folder", command=browse_folder)
browse_button.pack(pady=10)

# Create and pack the status label
status_label = tk.Label(root, text="")
status_label.pack()

# Start the GUI event loop
root.mainloop()
