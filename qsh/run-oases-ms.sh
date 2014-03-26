#!/bin/bash

#SBATCH -o oms.o%j
#SBATCH -J "oms.HF01.35"

#$ -N oms.ENGPUs.45

VELVETG="$HOME/src.HTseq/velvet/1.2.03/velvetg-101"
VELVETH="$HOME/src.HTseq/velvet/1.2.03/velveth-101"
OASES="$HOME/src.HTseq/oases/0.2.06/oases-101"

FA_m="../mfasta/Crawford201309_ENGPU_stomach14.mult_fasta"
FA_s=${FA_m/mult_fasta/single_fasta}

for K in 45
#for K in 85 65 45
#for K in 75 55 35
do
  DIRNAME=$(basename $FA_m)
  DIRNAME=${DIRNAME/.mult_fasta/}".K"$K"ms"
  $VELVETH $DIRNAME $K -short -fasta $FA_m -short -fasta $FA_s
  $VELVETG $DIRNAME -read_trkg yes -cov_cutoff auto
  $OASES $DIRNAME
done
