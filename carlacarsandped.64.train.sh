#!/bin/bash
#SBATCH --gres=gpu:4
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=2-00:00:00
#SBATCH --job-name=giraffe.carlacarsandped.64.train
#SBATCH --output=/scratch/cchen795/slurm/%x-%j.out
#SBATCH --error=/scratch/cchen795/slurm/%x-%j.out

echo "load modules and Python environment"
source $HOME/scratch/py38giraffe.sh

python train.py configs/64res/carlacarsandpedv2_64.yaml
