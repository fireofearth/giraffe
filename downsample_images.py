import os
import logging
import glob
import pathlib
import argparse
import multiprocessing as mp

import cv2
#import matplotlib.pyplot as plt

logging.basicConfig(
    format="%(asctime)s: %(levelname)s: %(message)s", level=logging.INFO
)

def parse_arguments():
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        "--image-directory",
        default="data/carlacarsv2/images/256",
        type=str,
        help="Directory containing images to downsample.",
    )
    argparser.add_argument(
        "--out-directory",
        default="data/carlacarsv2/images/64",
        type=str,
        help="Directory to downsample images.",
    )
    argparser.add_argument(
        "--size",
        default=64,
        type=int,
        help="Target size of image to downsample.",
    )
    return argparser.parse_args()


def divide(n, iterable):
    """Divide the elements from *iterable* into *n* parts as lists, maintaining order.
    Taken from more-itertools with minor modification."""
    if n < 1:
        raise ValueError('n must be at least 1')
    try:
        iterable[:0]
    except TypeError:
        seq = tuple(iterable)
    else:
        seq = iterable
    q, r = divmod(len(seq), n)
    ret = []
    stop = 0
    for i in range(1, n + 1):
        start = stop
        stop += q + 1 if i <= r else q
        ret.append(list(seq[start:stop]))
    return ret


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


def worker_task(infile_paths, out_directory, downsample_size):
    for infile_path in infile_paths:
        fn = path_to_filename(infile_path, with_suffix=True)
        outfile_path = os.path.join(out_directory, fn)
        downsample_image(infile_path, outfile_path, downsample_size)


config = parse_arguments()
os.makedirs(config.out_directory, exist_ok=True)
paths = glob.glob(os.path.join(config.image_directory, "*.png"))
cpu_count = mp.cpu_count()
n_processes = min(cpu_count, len(paths) // 5)
logging.info(f"Found {len(paths)} images in image directory {config.image_directory}")
logging.info(f"There are {cpu_count} CPUs, using {n_processes} of them.")
processes = []
for infile_paths in divide(n_processes, paths):
    p = mp.Process(
        target=worker_task,
        args=(infile_paths, config.out_directory, config.size)
    )
    p.start()
    processes.append(p)

for p in processes:
    p.join()

