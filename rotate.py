import os
import logging
from scipy import ndimage
import imageio.v2 as imageio


def setup_logging():
    """
    Sets up logging to log both to a file and to the console.
    """
    logging.basicConfig(
        format="%(asctime)s - %(message)s",
        level=logging.INFO,
        handlers=[logging.FileHandler("rotation.log"), logging.StreamHandler()],
    )


def rotate_images(input_dir, output_dir, angle=45):
    """
    Rotates all images in the input directory and saves them to the output directory.

    Args:
    input_dir (str): Path to the input directory containing images.
    output_dir (str): Path to the output directory to save rotated images.
    angle (float): Angle to rotate the images. Default is 45 degrees.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Iterate through the names of contents of the folder
    for image_name in os.listdir(input_dir):
        # Create the full input path and read the file
        input_path = os.path.join(input_dir, image_name)
        try:
            image_to_rotate = imageio.imread(input_path)

            # Rotate the image
            rotated_image = ndimage.rotate(image_to_rotate, angle)

            # Create full output path and save the file to disk
            output_path = os.path.join(output_dir, f"rotated_{image_name}")
            imageio.imwrite(output_path, rotated_image)

            logging.info(f"Rotated and saved: {output_path}")
        except Exception as e:
            logging.error(f"Error processing {input_path}: {e}")


def main():
    setup_logging()

    input_dir = input("Enter the path to the input directory: ").strip()
    output_dir = input("Enter the path to the output directory: ").strip()

    # Validate input directory
    if not os.path.isdir(input_dir):
        logging.error(
            f"Input directory '{input_dir}' does not exist. Please enter a valid directory."
        )
        return

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    try:
        angle = float(input("Enter the degree of rotation (e.g., 45): ").strip())
    except ValueError:
        logging.error("Invalid input for rotation angle. Please enter a numeric value.")
        return

    logging.info(f"Starting rotation of images in '{input_dir}' by {angle} degrees.")
    rotate_images(input_dir, output_dir, angle)
    logging.info(f"Finished rotating images.")


if __name__ == "__main__":
    main()
