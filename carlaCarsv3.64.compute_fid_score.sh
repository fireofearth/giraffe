#!/bin/bash
#SBATCH --gres=gpu:v100l:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=2-00:00:00
#SBATCH --job-name=giraffe.carlacarsv3.64.compute_fid_score
#SBATCH --output=/scratch/cchen795/slurm/%x-%j.out
#SBATCH --error=/scratch/cchen795/slurm/%x-%j.out

echo "load modules and Python environment"
source $HOME/scratch/py38giraffe.sh

python compute_fid_score.py \
	--image-directory data/carlacarsv3/images/64 \
	--out-directory data/carlacarsv3/fid_files \
	--label carlacars_64

