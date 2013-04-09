#!/bin/bash
#SBATCH -n 16
#SBATCH -p largemem
#SBATCH -t 24:00:00
#SBATCH --mail-user=$EMAIL
#SBATCH -o sbatch.o%j
# #SBATCH --mail-type=ALL

#SBATCH -J "oms.cap1C.K543"

OASES="$HOME/src.HTseq/oases/current/oases-101"
VELVETH="$HOME/src.HTseq/velvet/current/velveth-101"
VELVETG="$HOME/src.HTseq/velvet/current/velvetg-101"

FA_m="../mfasta/my.mult_fasta"

FA_s=${FA_m/.mult_fasta/.single_fasta}
for K in 55 45 35
do
DIRNAME=$(basename $FA_m)
DIRNAME=${DIRNAME/.mult_fasta/}
DIRNAME=$DIRNAME".K"$K"ms"
$VELVETH $DIRNAME $K -short -fasta $FA_m -short -fasta $FA_s
$VELVETG $DIRNAME -read_trkg yes -cov_cutoff auto
$OASES $DIRNAME
done 
