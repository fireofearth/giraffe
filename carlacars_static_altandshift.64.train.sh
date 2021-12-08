#!/bin/bash
#SBATCH --gres=gpu:p100l:4
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=2-00:00:00
#SBATCH --job-name=giraffe.carlacars_static_altandshift.64.train
#SBATCH --output=/scratch/cchen795/slurm/%x-%j.out
#SBATCH --error=/scratch/cchen795/slurm/%x-%j.out

echo "load modules and Python environment"
source $HOME/scratch/py38giraffe.sh

python train.py configs/64res/carlacars_static_altandshift.yaml

