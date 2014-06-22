#!/bin/bash

#SBATCH -o nc.o%j
#SBATCH -J "nc.foo"

#$ -N nq.foo

for FQ in $(ls *raw.fastq*)
do
  echo $FQ
  $HOME/git/HTseq-toolbox/fastq/filter-nocall.py $FQ
done
