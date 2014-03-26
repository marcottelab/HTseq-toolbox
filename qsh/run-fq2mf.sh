#!/bin/bash

## For SLURM
#SBATCH -o fq2mf.o%j
#SBATCH -J "fq2mf.hrt"

## For SGE
#$ -N fq2mf.foo

FQ2MF="$HOME/git/HTseq-toolbox/fastq/fastq-to-mult_fasta.py"

for FQ in $(ls *.fastq)
do
  $FQ2MF $FQ
done
