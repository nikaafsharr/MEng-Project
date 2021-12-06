#!/bin/bash

#PBS -l walltime=72:00:00
#PBS -l select=1:ncpus=1:mem=16gb

module load intel-suite

module load fix_unwritable_tmp

cd /rds/general/user/na918/home/nika/oxDNA/EXAMPLES
#Write path of where input file is present
#Navigate to the example and write pwd to get directory address

inputfile="/rds/general/user/na918/home/nika/oxDNA/EXAMPLES/input"

#cd $PBS_O_WORKDIR
runcommand="/rds/general/user/na918/home/nika/oxDNA/build/bin/oxDNA $inputfile"

timeout 200000000 $runcommand


