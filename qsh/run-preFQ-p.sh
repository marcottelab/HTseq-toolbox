#!/bin/bash

#SBATCH -o pair.o%j
#SBATCH -J "pair.foo"

#$ -N pair.foo

PAIR="$HOME/git/HTseq-toolbox/fastq/pair-fastq.py"

for R1 in $(ls *_R1.raw.fastq*)
do
  R2=${R1/_R1/_R2}
  OUT=${R1/_R1.raw.fastq.gz/}
  OUT=${OUT/_R1.raw.fastq/}
  $PAIR $R1 $R2 $OUT
done
