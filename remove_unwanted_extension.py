import os
import cv2

data_directory = "data"
wanted_image_extensions = [".jpeg", ".jpg", ".bmp", ".png"]

for image_class in os.listdir(data_directory):
    image_class_path = os.path.join(data_directory, image_class)
    for image in os.listdir(image_class_path):
        image_path = os.path.join(image_class_path, image)
        try:
            to_check_image = cv2.imread(image_path)
            image_extension = os.path.splitext(image)[1].lower()
            if image_extension not in wanted_image_extensions:
                print("Image not in list {}".format(image_path))
                # os.remove(image_path)
        except Exception as e:
            print("Issues with image {}".format(image_path))
