import os
from PIL import Image

def generate_empty_jpeg_files(folder, num_files):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    for i in range(1, num_files+1):
        # Create a new blank image with 1x1 pixels
        img = Image.new('RGB', (1, 1), color='white')
        
        # Save the image as JPEG in the specified folder
        img.save(os.path.join(folder, f"{i}.jpg"))

if __name__ == "__main__":
    folder_path = "./assets/"  # Specify your folder path here
    num_files = 100
    generate_empty_jpeg_files(folder_path, num_files)
