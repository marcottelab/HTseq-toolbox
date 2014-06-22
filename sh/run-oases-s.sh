#!/bin/bash
#SBATCH -o os.o%j
#SBATCH -J "os.foo"

#$ -N os.foo

VELVETG="$HOME/src.HTseq/velvet/1.2.03/velvetg-101"
VELVETH="$HOME/src.HTseq/velvet/1.2.03/velveth-101"
OASES="$HOME/src.HTseq/oases/0.2.06/oases-101"

FQ="../fastq/Crawford201309_ENGPU_stomach14.called.fastq"

for K in 61
#for K in 51 47 43 39 
#for K in 65 55 45
do
  DIRNAME=$(basename $FQ)
  DIRNAME=${DIRNAME/.called.fastq/}".K"$K"s"
  $VELVETH $DIRNAME $K -short -fastq $FQ 
  $VELVETG $DIRNAME -read_trkg yes -cov_cutoff auto
  $OASES $DIRNAME
done
