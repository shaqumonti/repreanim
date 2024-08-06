import os

image_folder = 'path_to_your_image_folder'
image_list = os.listdir(image_folder)

for image in image_list:
    print(image)
    # Perform operations with each image
