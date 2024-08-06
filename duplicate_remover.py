import os
from difPy import dif

def find_and_remove_lower_quality_images(directory):
    """
    Finds and removes lower quality duplicate images from the specified directory.

    Args:
    directory (str): Path to the directory to search for duplicate images.
    """
    if not os.path.isdir(directory):
        print(f"Invalid directory: {directory}. Please make sure the directory exists.")
        return

    # Initialize difPy to search for duplicates in the given directory
    search = dif(directory=directory)

    # Check if any lower quality images were found
    if search.lower_quality:
        print(f"Found {len(search.lower_quality)} lower quality duplicate images to remove.")
        for image_path in search.lower_quality:
            try:
                os.remove(image_path)
                print(f"Removed: {image_path}")
            except Exception as e:
                print(f"Error removing {image_path}: {str(e)}")
    else:
        print("No lower quality duplicate images found.")

    # Print the search results for further inspection if needed
    print("Search results:")
    print(search.result)

# Get directory path from user
directory = input("Enter the path to the directory to search for duplicates: ").strip()

# Process the directory
find_and_remove_lower_quality_images(directory)
