import os
import subprocess

def main():
    # Absolute path to the image directory
    image_directory = ''

    # Get all image files in the specified directory
    image_files = [f for f in os.listdir(image_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not image_files:
        print("No images found in the specified directory.")
        return

    # Ask the user for their preference
    choice = input("Select images to process (horizontal/vertical): ").strip().lower()
    
    if choice not in ['horizontal', 'vertical']:
        print("Invalid choice. Please choose 'horizontal' or 'vertical'.")
        return

    # Ensure the "Converted" folder exists within the image directory
    converted_directory = os.path.join(image_directory, 'Converted')
    if not os.path.exists(converted_directory):
        os.makedirs(converted_directory)

    # Process the images based on user choice
    for image_file in image_files:
        input_path = os.path.join(image_directory, image_file)
        output_path = os.path.join(converted_directory, image_file)

        # Construct the ImageMagick command
        cmd = ["convert", input_path]

        # If the user chose "horizontal" or "vertical", resize accordingly
        if choice == 'horizontal':
            cmd += ["-resize", "1920x1280"]
        elif choice == 'vertical':
            cmd += ["-resize", "1920x2860"]

        cmd += [output_path]

        # Run the command
        subprocess.run(cmd)

        print(f"Processed {image_file}")

    print("Conversion process complete.")

if __name__ == "__main__":
    main()
