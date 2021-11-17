"""Compute FID score used for validation."""
import os
import glob
import numpy as np
from im2scene.eval import calculate_activation_statistics

def main():
    files = glob.glob("data/carla_cars/images/*.png")
    mu, sigma = calculate_activation_statistics(files, verbose=True)
    out_dict = {"m": mu, "s": sigma}
    out_dir = "data/carla_cars/fid_files"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "carlaCars_256.npz")
    np.savez(out_file, **out_dict)

if __name__ == "__main__":
    main()