#!/bin/bash
#SBATCH --cpus-per-task=16
#SBATCH --mem=1G
#SBATCH --time=0-10:00:00
#SBATCH --job-name=giraffe.carlacars_static_altitude.64.downsample_images
#SBATCH --output=/scratch/cchen795/slurm/%x-%j.out
#SBATCH --error=/scratch/cchen795/slurm/%x-%j.out

echo "load modules and Python environment"
source $HOME/scratch/py38giraffe.sh

python downsample_images.py \
	--image-directory data/carlacars_static_altitude/images/256 \
	--out-directory data/carlacars_static_altitude/images/32 \
	--size 32

