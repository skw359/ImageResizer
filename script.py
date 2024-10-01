from pathlib import Path
from PIL import Image
import sys
import os

# Constants
TARGET_SIZE = (1080, 1920)
ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg'}

def resize_image(input_path, output_path, target_size):
    with Image.open(input_path) as img:
        # Calculate aspect ratios
        img_aspect = img.width / img.height
        target_aspect = target_size[0] / target_size[1]
        
        if img_aspect > target_aspect:
            # Image is wider than target, fit to width
            new_width = target_size[0]
            new_height = int(new_width / img_aspect)
        else:
            # Image is taller than target, fit to height
            new_height = target_size[1]
            new_width = int(new_height * img_aspect)
        
        img_resized = img.resize((new_width, new_height), Image.LANCZOS)
        
        # Create new image with target size and paste resized image
        new_img = Image.new("RGB", target_size, (0, 0, 0))
        paste_x = (target_size[0] - new_width) // 2
        paste_y = (target_size[1] - new_height) // 2
        new_img.paste(img_resized, (paste_x, paste_y))
        
        new_img.save(output_path, quality=95)

def main():
    # Get image directory from command line argument or use current directory and get all image files in the specified directory
    image_directory = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    
    image_files = [f for f in image_directory.iterdir() if f.suffix.lower() in ALLOWED_EXTENSIONS]
    
    if not image_files:
        print("No images found in the specified directory.")
        return
    
    converted_directory = image_directory / 'Converted'
    converted_directory.mkdir(exist_ok=True)
    
    # Process images
    total_images = len(image_files)
    for i, image_file in enumerate(image_files, 1):
        output_path = converted_directory / image_file.name
        try:
            resize_image(image_file, output_path, TARGET_SIZE)
            print(f"Processed {i}/{total_images}: {image_file.name}")
        except Exception as e:
            print(f"Error processing {image_file.name}: {str(e)}")
    
    print("Conversion process complete.")

if __name__ == "__main__":
    main()
