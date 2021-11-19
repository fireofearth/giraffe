import os
import glob
import cv2
import pathlib
import argparse
#import matplotlib.pyplot as plt

def parse_arguments():
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        "--image-directory",
        default="data/carla_cars_v2/images",
        type=str,
        help="Directory containing images to downsample.",
    )
    argparser.add_argument(
        "--out-directory",
        default="data/carla_cars_v2/images_64",
        type=str,
        help="Directory to downsample images.",
    )
    return argparser.parse_args()


def path_to_filename(path, with_suffix=True):
    """Get filename from path.
    
    Parameters
    ==========
    path : str
        Path to retrieve file name from e.g. '/path/to/image.png'.
    with_suffix : bool
        Whether to include the suffix of file path in file name.

    Returns
    =======
    str
        The file name of the path e.g. 'image.png'
        or 'image' if `with_suffix` is false.
    """
    p = pathlib.Path(path)
    if with_suffix:
        return str(p.name)
    else:
        return str(p.with_suffix("").name)

def downsample_image(infile_path, outfile_path, downsample_size):
    image = cv2.imread(infile_path, flags=cv2.IMREAD_COLOR)
    resized_image = cv2.resize(
        image,
        (downsample_size, downsample_size),
        interpolation=cv2.INTER_AREA
    )
    cv2.imwrite(outfile_path, resized_image)


#def show_image(infile_path):
#    image = cv2.imread(infile_path)
#    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#    plt.imshow(image)
#    plt.show()

"""
cv2 reads BGR as its default colour order for images, matplotlib uses RGB.
Switching the ordering of the color channels doesn't cost any compute
as the underlying pixel values don't change. Make sure to use `cv2.cvtColor()` to
change the color ordering passing image to some other library API.

https://stackoverflow.com/questions/50963283/python-opencv-imshow-doesnt-need-convert-from-bgr-to-rgb
https://stackoverflow.com/questions/39316447/opencv-giving-wrong-color-to-colored-images-on-loading
"""

config = parse_arguments()
os.makedirs(config.out_directory, exist_ok=True)
l = glob.glob(os.path.join(config.image_directory, "*.png"))
for infile_path in l:
    # show_image(infile_path)
    fn = path_to_filename(infile_path, with_suffix=True)
    outfile_path = os.path.join(config.out_directory, fn)
    downsample_image(infile_path, outfile_path, 64)

