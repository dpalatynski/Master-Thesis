#!/bin/bash

#PBS -q main
#PBS -l walltime=3:00:00
#PBS -l select=1:ncpus=1:mem=200MB
#PBS -m e


cd $PBS_O_WORKDIR
MODULEPATH="$MODULEPATH:/usr/local/easybuild/python-3.6.8-gcc7.3.0/modules/all/"
module load python/3.6.8-gcc7.3.0
source $HOME/Inception/bin/activate
python simulation.py ${p} ${q} ${a} ${b} ${c} ${d} ${h}
