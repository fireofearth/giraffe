#!/bin/bash
#SBATCH --gres=gpu:v100l:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=2-00:00:00
#SBATCH --job-name=giraffe.carlaCars64.v2.compute_fid_score
#SBATCH --output=/scratch/cchen795/slurm/%x-%j.out
#SBATCH --error=/scratch/cchen795/slurm/%x-%j.out

echo "load modules and Python environment"
source $HOME/scratch/py38giraffe.sh

python compute_fid_score.py \
	--image-directory data/carla_cars_v2/images_64 \
	--out-directory data/carla_cars_v2/fid_files \
	--label carlaCars_64

