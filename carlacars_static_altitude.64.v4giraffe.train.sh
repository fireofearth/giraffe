#!/bin/bash
#SBATCH --nodes=1
#SBATCH --gres=gpu:4
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=2-00:00:00
#SBATCH --job-name=giraffe.carlacars_static_altitude.64.v4giraffe.train
#SBATCH --output=/scratch/cchen795/slurm/%x-%j.out
#SBATCH --error=/scratch/cchen795/slurm/%x-%j.out

echo "load modules and Python environment"
source $HOME/scratch/py38giraffe.sh
carlacars_static_altitude_v4giraffe.yaml
python train.py configs/64res/carlacars_static_altitude_v4giraffe.yaml \
	--exit-after 172000

