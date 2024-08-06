import os
from PIL import Image


def get_input_path():
    while True:
        input_path = input("Enter the path to the image file: ").strip()
        if os.path.isfile(input_path):
            return input_path
        else:
            print("Invalid file path. Please try again.")


def get_output_path(input_path):
    while True:
        overwrite = input(
            "Do you want to overwrite the original image? (y/n): "
        ).lower()
        if overwrite == "y":
            return input_path
        elif overwrite == "n":
            output_path = input("Enter the path to save the new image: ").strip()
            directory = os.path.dirname(output_path)
            if not directory or os.path.isdir(directory):
                return output_path
            else:
                print("Invalid directory. Please try again.")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def process_image(input_path, output_path):
    try:
        # Open the image
        with Image.open(input_path) as image:
            # Get image data
            data = list(image.getdata())

            # Create a new image with the same data
            new_image = Image.new(image.mode, image.size)
            new_image.putdata(data)

            # Save the new image
            new_image.save(output_path)

        print("Image processed and saved successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    print("Image Processing Script")
    print("----------------------")

    # Get input file path
    input_path = get_input_path()

    # Get output file path
    output_path = get_output_path(input_path)

    # Process and save the image
    process_image(input_path, output_path)


if __name__ == "__main__":
    main()
