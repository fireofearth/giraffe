#!/bin/bash
#SBATCH --cpus-per-task=4
#SBATCH --mem=1G
#SBATCH --time=0-10:00:00
#SBATCH --job-name=giraffe.carlaCars256.downsample_images
#SBATCH --output=/scratch/cchen795/slurm/%x-%j.out
#SBATCH --error=/scratch/cchen795/slurm/%x-%j.out

echo "load modules and Python environment"
source $HOME/scratch/py38giraffe.sh

python downsample_images.py

