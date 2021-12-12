#!/bin/bash
#SBATCH --gres=gpu:v100l:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=2-00:00:00
#SBATCH --job-name=giraffe.carlacars_static_altandshift.32.compute_fid_score
#SBATCH --output=/scratch/cchen795/slurm/%x-%j.out
#SBATCH --error=/scratch/cchen795/slurm/%x-%j.out

echo "load modules and Python environment"
source $HOME/scratch/py38giraffe.sh

python compute_fid_score.py \
	--image-directory data/carlacars_static_altandshift/images/32 \
	--out-directory data/carlacars_static_altandshift/fid_files \
	--label carlacars_32

