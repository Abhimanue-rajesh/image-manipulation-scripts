import os
from PIL import Image
import logging


def setup_logging():
    logging.basicConfig(
        format="%(asctime)s - %(message)s",
        level=logging.INFO,
        handlers=[logging.FileHandler("conversion.log"), logging.StreamHandler()],
    )


def convert_images_to_jpg(directory, delete_originals=False):
    """
    Converts all images in the given directory and its subdirectories to JPG format.

    Args:
    directory (str): Path to the main directory containing image subdirectories.
    delete_originals (bool): Flag to delete original files after conversion.
    """
    setup_logging()

    # Iterate through all subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Construct full file path
            file_path = os.path.join(root, file)

            # Check if the file is an image
            if file.lower().endswith((".png", ".jpeg", ".gif", ".bmp")):
                try:
                    with Image.open(file_path) as img:
                        # Construct new file path with .jpg extension
                        new_file_path = os.path.splitext(file_path)[0] + ".jpg"

                        # Check if the file is already a JPG
                        if file_path.lower() == new_file_path.lower():
                            logging.info(f"Already a JPG: {file_path}")
                            continue

                        # Convert image to RGB (removes alpha channel if present)
                        rgb_img = img.convert("RGB")

                        # Save as JPG with quality setting
                        rgb_img.save(new_file_path, "JPEG", quality=90)

                        logging.info(f"Converted: {file_path} -> {new_file_path}")

                        # Remove original file if delete_originals is True
                        if delete_originals:
                            os.remove(file_path)
                            logging.info(f"Removed original: {file_path}")

                except Exception as e:
                    logging.error(f"Error processing {file_path}: {str(e)}")

            else:
                logging.info(f"Skipped non-image file: {file_path}")


# Get directory path from user
data_directory = input(
    "Enter the path to the main directory containing image subdirectories: "
).strip()
delete_originals = (
    input("Do you want to delete the original files after conversion? (yes/no): ")
    .strip()
    .lower()
    == "yes"
)

# Check if the directory exists
if os.path.isdir(data_directory):
    convert_images_to_jpg(data_directory, delete_originals)
else:
    logging.error("Invalid directory path. Please make sure the directory exists.")
