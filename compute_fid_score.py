"""Compute FID score used for validation."""
import os
import os.path
import glob
import argparse
import numpy as np
from im2scene.eval import calculate_activation_statistics

def parse_arguments():
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        "--image-directory",
        default="data/carlacarsv3/images/64",
        type=str,
        help="Directory containing images to downsample.",
    )
    argparser.add_argument(
        "--out-directory",
        default="data/carlacarsv3/fid_files",
        type=str,
        help="Directory to save FID score.",
    )
    argparser.add_argument(
        "--label",
        default="carlacars_64",
        type=str,
        help="Name of FID file"
    )

    return argparser.parse_args()

def main():
    config = parse_arguments()
    files = glob.glob(os.path.join(config.image_directory, "*.png"))
    mu, sigma = calculate_activation_statistics(files, verbose=True)
    out_dict = {"m": mu, "s": sigma}
    os.makedirs(config.out_directory, exist_ok=True)
    out_file = os.path.join(config.out_directory, f"{config.label}.npz")
    np.savez(out_file, **out_dict)

if __name__ == "__main__":
    main()

