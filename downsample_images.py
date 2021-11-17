import os
import glob
import cv2
import matplotlib.pyplot as plt

import utility as util

def downsample_image(infile_path, outfile_path, downsample_size):
    image = cv2.imread(infile_path, flags=cv2.IMREAD_COLOR)
    resized_image = cv2.resize(
        image,
        (downsample_size, downsample_size),
        interpolation=cv2.INTER_AREA
    )
    cv2.imwrite(outfile_path, resized_image)

image_directory = "data/images/*.png"
out_directory = "data/images_64"

def show_image(infile_path):
    image = cv2.imread(infile_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.show()

"""
cv2 reads BGR as its default colour order for images, matplotlib uses RGB.
Switching the ordering of the color channels doesn't cost any compute
as the underlying pixel values don't change. Make sure to use `cv2.cvtColor()` to
change the color ordering passing image to some other library API.

https://stackoverflow.com/questions/50963283/python-opencv-imshow-doesnt-need-convert-from-bgr-to-rgb
https://stackoverflow.com/questions/39316447/opencv-giving-wrong-color-to-colored-images-on-loading
"""

os.makedirs(out_directory, exist_ok=True)
l = glob.glob(image_directory)
for infile_path in l:
    # show_image(infile_path)
    fn = util.path_to_filename(infile_path, with_suffix=True)
    outfile_path = os.path.join(out_directory, fn)
    downsample_image(infile_path, outfile_path, 64)