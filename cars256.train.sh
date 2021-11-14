#!/bin/bash
#SBATCH --gres=gpu:v100l:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=2-12:00:00
#SBATCH --job-name=giraffe.cars256.train
#SBATCH --output=/scratch/cchen795/slurm/%x-%j.out
#SBATCH --error=/scratch/cchen795/slurm/%x-%j.out

echo "load modules and Python environment"
source $HOME/scratch/py38giraffe.sh

#python test_train.py configs/64res/cars_64.yaml
python train.py configs/256res/cars_256.yaml

