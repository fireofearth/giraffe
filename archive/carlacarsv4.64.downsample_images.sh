#!/bin/bash
#SBATCH --cpus-per-task=8
#SBATCH --mem=1G
#SBATCH --time=0-10:00:00
#SBATCH --job-name=giraffe.carlacarsv4.64.downsample_images
#SBATCH --output=/scratch/cchen795/slurm/%x-%j.out
#SBATCH --error=/scratch/cchen795/slurm/%x-%j.out

echo "load modules and Python environment"
source $HOME/scratch/py38giraffe.sh

python downsample_images.py \
	--image-directory data/carlacarsv4/images/256 \
	--out-directory data/carlacarsv4/images/64 \
	--size 64

