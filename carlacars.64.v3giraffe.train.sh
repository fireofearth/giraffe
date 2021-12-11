#!/bin/bash
#SBATCH --gres=gpu:4
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=2-00:00:00
#SBATCH --job-name=giraffe.carlacars.64.v3giraffe.train
#SBATCH --output=/scratch/cchen795/slurm/%x-%j.out
#SBATCH --error=/scratch/cchen795/slurm/%x-%j.out

echo "load modules and Python environment"
source $HOME/scratch/py38giraffe.sh

python train.py configs/64res/carlacarsv5_64_v3giraffe.yaml \
	--exit-after 172000

