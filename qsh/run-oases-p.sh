#!/bin/bash

#SBATCH -o op.o%j
#SBATCH -J "op."

#$ -N op.foo

VELVETG="$HOME/src.HTseq/velvet/1.2.03/velvetg-101"
VELVETH="$HOME/src.HTseq/velvet/1.2.03/velveth-101"
OASES="$HOME/src.HTseq/oases/0.2.06/oases-101"

FQ="../fastq/Chang2013_XENLA_Ventral.paired.fastq"
INS_LEN=200

for K in 23 27 31
#for K in 21 25 29
do
  DIRNAME=$(basename $FQ)
  DIRNAME=${DIRNAME/.paired.fastq/}".K"$K"p"
  $VELVETH $DIRNAME $K -shortPaired -fastq $FQ
  $VELVETG $DIRNAME -read_trkg yes -ins_length $INS_LEN -cov_cutoff auto
  $OASES $DIRNAME
done 
