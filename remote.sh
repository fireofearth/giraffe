#!/bin/bash

conda activate giraffe

jupyter notebook \
	--NotebookApp.iopub_data_rate_limit=1.0e10 \
	--no-browser \
	--ip 192.168.1.101 \
